#!/usr/bin/env python3
"""SessionStart hook: put project-docs/STATE.md and recent log IDs into context.

Silent in projects that do not use phased-builder (no project-docs/STATE.md).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pb_common import DOCS_DIR, emit, project_dir, read_frontmatter, read_hook_input, read_text, state_path  # noqa: E402


def recent_log_headings(root, count=5):
    text = read_text(os.path.join(root, DOCS_DIR, "BUILD_LOG.md"))
    heads = [h.strip() for h in re.findall(r"^##\s+(L-\d+.*)$", text, flags=re.M)]
    return heads[-count:]


def main():
    hook_input = read_hook_input()
    root = project_dir(hook_input)
    path = state_path(root)
    if not os.path.isfile(path):
        return 0

    fm = read_frontmatter(path) or {}
    source = hook_input.get("source", "startup")
    parts = [
        "This project uses the phased-builder workflow. Its working rules are in CLAUDE.md "
        "and its project memory is in project-docs/. Nothing from earlier conversations is "
        "remembered unless it is written in these files.",
        "",
        "Contents of project-docs/STATE.md:",
        read_text(path, limit=6000).strip(),
    ]

    heads = recent_log_headings(root)
    if heads:
        parts += ["", "Most recent BUILD_LOG.md entries (newest last):"] + [f"- {h}" for h in heads]

    repo = fm.get("repo", "")
    if repo and repo != "none":
        parts += ["", f"The code is in the repo folder `{repo}/`. project-docs/, CLAUDE.md and SETUP.md are in "
                  "this parent folder, outside git, and are never committed."]
    mode = fm.get("mode", "")
    if mode == "mentor":
        parts += ["", "Mentor mode is on: code and project files are written by the user; "
                  "the agent edits only project-docs/, CLAUDE.md and SETUP.md."]
    else:
        parts += ["", "Vibe mode: the agent edits code and config files itself (never asks the user to hand-edit them)."]
    parts += ["", "Responses: short, plain English, tables for long or comparative content. Don't re-ask or "
              "re-raise settled points unless something conflicts with them or is genuinely vague."]
    if fm.get("long_commands", "user") != "agent":
        parts += ["", "Installs, builds, tests, dev servers and deploys are run by the user. "
                  "The agent gives exact commands and expected output, then waits for pasted results."]
    if fm.get("git", "user") != "agent":
        parts += ["", "The user makes all git changes (add, commit, push). The agent may run read-only git commands."]

    if source == "compact":
        parts += ["", "The conversation was just compacted. Decisions from before compaction "
                  "are reliable only if they appear in project-docs/BUILD_LOG.md or the project docs. "
                  "Anything discussed but not logged may be lost and should be confirmed with the user."]
    elif source in ("resume", "clear"):
        parts += ["", f"Session source: {source}. The files above are the source of truth, not chat memory."]

    emit("SessionStart", additionalContext="\n".join(parts))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # never break a session because of this hook
        sys.stderr.write(f"phased-builder session_start hook error: {exc}\n")
        sys.exit(0)
