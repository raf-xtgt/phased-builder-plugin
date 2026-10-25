#!/usr/bin/env python3
"""PreToolUse hook for phased-builder projects.

Rules (read from the frontmatter of project-docs/STATE.md):
  mode: mentor        -> block edits to project files outside project-docs/, CLAUDE.md and SETUP.md,
                         and block shell commands that write or move project files (8-build: user writes code).
  long_commands: user -> block installs, builds, tests, dev servers, deploys (default).
  git: user           -> block git commands that change state; read-only git is allowed (default).

Silent in projects that do not use phased-builder. These are best-effort guards:
a determined shell command can still get around them; the written rules cover the rest.
"""
import os
import re
import shlex
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pb_common import DOCS_DIR, emit, project_dir, read_frontmatter, read_hook_input, state_path  # noqa: E402

READ_ONLY_GIT = {
    "status", "log", "diff", "show", "blame", "ls-files", "rev-parse", "remote",
    "config", "shortlog", "describe", "grep", "cat-file", "ls-tree", "reflog", "help", "--version",
}

# (first token, optional second token or None for "any"). Matched after skipping env vars / sudo.
LONG_COMMANDS = {
    "npm": {"install", "i", "ci", "add", "test", "t", "run", "run-script", "start", "create", "init", "exec", "update", "upgrade", "rebuild"},
    "pnpm": None, "yarn": None, "bun": None, "npx": None, "bunx": None, "pnpx": None,
    "pip": {"install", "download", "wheel"}, "pip3": {"install", "download", "wheel"},
    "uv": {"add", "sync", "pip", "run", "venv", "tool", "lock"},
    "poetry": None, "pipenv": None, "conda": {"install", "create", "env", "update"},
    "pytest": None, "tox": None, "nox": None, "jest": None, "vitest": None, "mocha": None,
    "playwright": None, "cypress": None, "karma": None, "phpunit": None, "rspec": None,
    "go": {"test", "build", "run", "get", "install", "generate", "mod"},
    "cargo": {"build", "test", "run", "add", "install", "bench", "update"},
    "mvn": None, "gradle": None, "./gradlew": None, "./mvnw": None, "ant": None,
    "dotnet": {"build", "test", "run", "restore", "publish", "add", "new", "watch"},
    "make": None, "cmake": None, "ninja": None, "bazel": None,
    "docker": None, "docker-compose": None, "podman": None, "kubectl": None, "helm": None,
    "terraform": None, "tofu": None, "pulumi": None, "ansible-playbook": None,
    "vercel": None, "netlify": None, "fly": None, "flyctl": None, "railway": None, "heroku": None,
    "firebase": None, "wrangler": None, "supabase": None, "amplify": None, "eb": None, "sam": None, "cdk": None,
    "gcloud": None, "aws": None, "az": None, "doctl": None,
    "brew": {"install", "upgrade", "reinstall"}, "apt": {"install", "upgrade"}, "apt-get": {"install", "upgrade"},
    "dnf": {"install", "upgrade"}, "yum": {"install", "update"}, "pacman": None, "snap": {"install"}, "choco": None, "winget": None,
    "composer": {"install", "update", "require", "create-project"}, "bundle": {"install", "update", "exec"},
    "gem": {"install"}, "rails": None, "rake": None, "mix": None, "flutter": None, "dart": {"pub", "run", "test", "compile"},
    "next": None, "vite": None, "nuxt": None, "ng": None, "expo": None, "tsc": None, "webpack": None, "turbo": None, "nx": None,
    "uvicorn": None, "gunicorn": None, "hypercorn": None, "flask": None, "django-admin": None, "nodemon": None,
    "deno": {"test", "run", "task", "install", "compile"},
    "cargo-watch": None, "swift": {"build", "test", "run"}, "xcodebuild": None,
}
PY_MODULES_LONG = {"pytest", "unittest", "pip", "venv", "uvicorn", "gunicorn", "flask", "http.server", "build", "twine", "tox", "nox", "mypy"}
MANAGE_PY_LONG = {"runserver", "test", "migrate", "makemigrations", "collectstatic"}

FILE_WRITING_COMMANDS = {"rm", "rmdir", "cp", "mv", "touch", "mkdir", "ln", "install", "truncate", "dd", "patch", "tee", "chmod", "chown", "rsync", "unzip", "tar"}
IN_PLACE_FLAGS = {"sed": ("-i", "--in-place"), "perl": ("-i", "-pi", "-pie"), "ruby": ("-i",)}

SEGMENT_SPLIT = re.compile(r"\s*(?:&&|\|\||;|\||\n)\s*")
REDIRECT = re.compile(r"(?<![0-9&<>])(?:[0-9]?>>?|&>>?)\s*([^\s;&|<>]+)")


def deny(reason):
    emit("PreToolUse", permissionDecision="deny", permissionDecisionReason=reason)
    sys.exit(0)


def inside(path, base):
    try:
        path, base = os.path.realpath(path), os.path.realpath(base)
        return os.path.commonpath([path, base]) == base
    except ValueError:
        return False


def is_allowed_doc_path(path, root):
    """True for files the agent may write in mentor mode, or files outside the project."""
    if not path:
        return True
    abs_path = path if os.path.isabs(path) else os.path.join(root, path)
    if not inside(abs_path, root):
        return True  # outside the project (scratch files etc.) is not project code
    if inside(abs_path, os.path.join(root, DOCS_DIR)):
        return True
    return os.path.realpath(abs_path) in {
        os.path.realpath(os.path.join(root, name)) for name in ("CLAUDE.md", "SETUP.md")
    }


def tokens_of(segment):
    try:
        toks = shlex.split(segment, posix=True)
    except ValueError:
        toks = segment.split()
    while toks and (re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", toks[0]) or toks[0] in ("sudo", "env", "time", "nohup", "exec", "command")):
        toks = toks[1:]
    return toks


VERSION_FLAGS = {"--version", "-v", "-V", "version", "--help", "-h", "help"}


def long_command_hit(toks):
    if not toks:
        return None
    if len(toks) == 2 and toks[1] in VERSION_FLAGS:
        return None  # quick read-only checks like `flutter --version`
    first = os.path.basename(toks[0]) if not toks[0].startswith("./") else toks[0]
    second = next((t for t in toks[1:] if not t.startswith("-")), "")
    if first in LONG_COMMANDS:
        subs = LONG_COMMANDS[first]
        if subs is None or second in subs:
            return " ".join(toks[:3])
    if first.startswith("python") or first == "py":
        if "-m" in toks:
            i = toks.index("-m")
            if i + 1 < len(toks) and toks[i + 1] in PY_MODULES_LONG:
                return " ".join(toks[: i + 2])
        if any(t.endswith("manage.py") for t in toks) and any(t in MANAGE_PY_LONG for t in toks):
            return " ".join(toks[:3])
    return None


def git_write_hit(toks):
    if not toks or os.path.basename(toks[0]) != "git":
        return None
    rest = toks[1:]
    while rest and rest[0].startswith("-"):  # skip global flags like -C dir / --no-pager
        rest = rest[2:] if rest[0] in ("-C", "-c") else rest[1:]
    sub = rest[0] if rest else ""
    if sub in READ_ONLY_GIT:
        if sub == "config" and not any(f in rest for f in ("--get", "--list", "-l", "--get-all")):
            return "git config"
        if sub == "remote" and len(rest) > 1 and rest[1] not in ("-v", "show", "get-url"):
            return "git remote " + rest[1]
        return None
    if sub == "branch" and all(t.startswith("-") and t in ("-a", "-r", "-v", "-vv", "--list", "--show-current") for t in rest[1:]):
        return None
    return "git " + sub if sub else None


def mentor_bash_hit(command, toks_list, root):
    for target in REDIRECT.findall(command):
        if target.startswith("&") or target == "/dev/null":
            continue
        if not is_allowed_doc_path(target, root):
            return f"shell redirect into {target}"
    for toks in toks_list:
        if not toks:
            continue
        first = os.path.basename(toks[0])
        args = [t for t in toks[1:] if not t.startswith("-")]
        if first in FILE_WRITING_COMMANDS:
            if not args or not all(is_allowed_doc_path(a, root) for a in args):
                return " ".join(toks[:3])
        if first in IN_PLACE_FLAGS and any(t.startswith(IN_PLACE_FLAGS[first]) for t in toks[1:]):
            if not all(is_allowed_doc_path(a, root) for a in args[1:] or [""]):
                return " ".join(toks[:3])
        if first.startswith("python") and "-c" in toks and re.search(r"open\(|write_text|write_bytes|shutil\.", command):
            return "python -c file write"
        if first == "node" and "-e" in toks and re.search(r"writeFile|appendFile|copyFile|rename", command):
            return "node -e file write"
    return None


def main():
    hook_input = read_hook_input()
    root = project_dir(hook_input)
    spath = state_path(root)
    if not os.path.isfile(spath):
        return 0
    fm = read_frontmatter(spath) or {}
    mode = fm.get("mode", "")
    restricted = mode == "mentor"
    where = fm.get("current_feature", "") or ""
    who = f"Mentor mode is on{(' for ' + where) if where and where != 'none' else ''}: the user writes the code and project files"
    tool = hook_input.get("tool_name", "")
    tin = hook_input.get("tool_input", {}) or {}

    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        if not restricted:
            return 0
        path = tin.get("file_path") or tin.get("notebook_path") or ""
        if not is_allowed_doc_path(path, root):
            deny(
                f"{who} (project-docs/STATE.md). The agent may only edit project-docs/, CLAUDE.md and SETUP.md here. "
                f"Blocked: {path}. Show the user the exact content and path, or give steps, "
                "a blueprint, doc links or review comments instead. Only the user can change the mode, in chat."
            )
        return 0

    if tool != "Bash":
        return 0
    command = tin.get("command", "") or ""
    toks_list = [tokens_of(s) for s in SEGMENT_SPLIT.split(command) if s.strip()]

    if fm.get("git", "user") != "agent":
        for toks in toks_list:
            hit = git_write_hit(toks)
            if hit:
                deny(
                    f"In this project the user makes all git changes ({hit} blocked). Give the user the exact "
                    "commands to run from the repo folder (list repo files explicitly; no blanket `git add .`; "
                    "never project-docs/, CLAUDE.md or SETUP.md), then wait for them to confirm. Read-only git "
                    "commands (status, log, diff, show) are allowed. Never create or init a repo."
                )

    if fm.get("long_commands", "user") != "agent":
        for toks in toks_list:
            hit = long_command_hit(toks)
            if hit:
                deny(
                    f"In this project the user runs installs, builds, tests, dev servers and deploys "
                    f"(`{hit}` blocked). Give the user: the folder, the exact command(s), what output to expect, "
                    "and the pass/fail rule. Then stop and wait for them to paste the output. (Config file edits "
                    "are yours to make in vibe mode.)"
                )

    if restricted:
        hit = mentor_bash_hit(command, toks_list, root)
        if hit:
            deny(
                f"{who}. Shell commands that create, change, move or delete project files are blocked "
                f"({hit}). The user makes those changes; give them the exact steps instead."
            )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # fail open: never break the session because of this hook
        sys.stderr.write(f"phased-builder guard hook error: {exc}\n")
        sys.exit(0)
