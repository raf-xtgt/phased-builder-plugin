# phased-builder marketplace (private)

This folder is a local Claude Code marketplace holding one plugin: `plugins/phased-builder`.
Details: `plugins/phased-builder/README.md`.

## Install (once, from a terminal)

```bash
claude plugin marketplace add /path/to/phased-builder-marketplace
claude plugin install phased-builder@phased-builder-marketplace
```

Edits to the plugin files take effect at the next session start, or with `/reload-plugins` inside a session.

## Try without installing

```bash
claude --plugin-dir /path/to/phased-builder-marketplace/plugins/phased-builder
```

## Start a project

Open an empty project folder in Claude Code and run `/phased-builder:1-start`.

Requirements: `python3` on your PATH (for the hooks), `git`.
