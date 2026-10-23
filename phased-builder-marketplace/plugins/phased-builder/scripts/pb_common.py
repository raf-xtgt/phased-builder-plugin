"""Shared helpers for phased-builder hooks. Standard library only."""
import json
import os
import sys

DOCS_DIR = "project-docs"


def read_hook_input():
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def project_dir(hook_input):
    return os.environ.get("CLAUDE_PROJECT_DIR") or hook_input.get("cwd") or os.getcwd()


def state_path(root):
    return os.path.join(root, DOCS_DIR, "STATE.md")


def read_frontmatter(path):
    """Return the simple `key: value` pairs between the first two `---` lines."""
    data = {}
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.read().splitlines()
    except OSError:
        return None
    if not lines or lines[0].strip() != "---":
        return data
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line and not line.lstrip().startswith("#"):
            key, _, value = line.partition(":")
            value = value.split("#", 1)[0].strip().strip('"').strip("'")
            data[key.strip().lower()] = value.lower() if key.strip().lower() in (
                "mode", "long_commands", "git", "phase_type", "step") else value
    return data


def read_text(path, limit=None):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return ""
    if limit and len(text) > limit:
        text = text[:limit] + "\n[...truncated; read the full file]"
    return text


def emit(event, **fields):
    out = {"hookSpecificOutput": {"hookEventName": event, **fields}}
    sys.stdout.write(json.dumps(out))
