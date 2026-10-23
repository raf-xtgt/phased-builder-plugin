# phased-builder

A Claude Code plugin for building a project in **phases** with **flipped interaction**: the agent
interviews you, shows you what's standard at your scale, and you make the decisions.

Adapted from [challengepost/learn-ai-basics](https://github.com/challengepost/learn-ai-basics)
(MIT, © 2026 Devpost). See `LICENSE`.

## What it does

- **Unlimited phases.** Each is a **setup** phase (environment, packages, cloud, deploy; ends with
  something that runs) or a **build** phase (one complete feature, checked against **SLC**: Simple,
  Lovable, Complete).
- **Two modes per phase.** **Vibe-code:** the agent writes the code. **Mentor:** you write the code; the
  agent gives blueprints, doc links, reviews, and small general examples only when you ask.
- **You run the commands and make the commits** in both modes. The agent gives exact commands and
  expected output, then waits for you to paste the result.
- **Shared memory in files.** `STATE.md`, an add-only `BUILD_LOG.md`, a `PARKING_LOT.md` for ideas,
  and master docs (`PRODUCT.md`, `ARCHITECTURE.md`) that are updated at the end of every phase.
  The agent must cite where it found a past decision, or say it has no record.
- **Opportunities.** Research and adapt to hackathons (any organizer, with a depth check on sponsor
  tech), incubators, investor pitches, and social launches on X, Discord and LinkedIn.

## The skills

| Skill | When |
|---|---|
| `/phased-builder:1-start` | Once per project. Sets up `project-docs/` and `CLAUDE.md`. |
| `/phased-builder:2-scope` | Vision, scale, roadmap. Run again to change the roadmap. |
| `/phased-builder:3-prd` | Each build phase: what the feature does + SLC check. |
| `/phased-builder:4-spec` | Each phase: how it's built (setup or build). |
| `/phased-builder:5-build` | Each phase: slices, checks, final review, merge into master docs. |
| `/phased-builder:6-ship` | Any time after a phase: release, deploy, README, changelog. |
| `/phased-builder:7-opportunity` | Any time, or before anything is built. |

```
1-start → 2-scope → for each phase:  setup: 4-spec → 5-build
                                      build: 3-prd → 4-spec → 5-build
          6-ship and 7-opportunity whenever needed
```

## What it creates in your project

```
CLAUDE.md                 working rules (loaded every session)
project-docs/
├── STATE.md              where we are now (loaded every session by a hook)
├── scope.md              vision, scale, roadmap
├── PRODUCT.md            master: the product today
├── ARCHITECTURE.md       master: the system today
├── BUILD_LOG.md          decisions, bugs, pivots (add-only, L-001...)
├── PARKING_LOT.md        ideas for later (P-001...)
├── profile.md            your context (git-ignored)
├── phases/NN-type-name/  prd.md, spec.md, checklist.md
└── opportunities/<name>/ brief.md, research.md, drafts/
```

## Hooks (need `python3` on your PATH)

Both hooks do nothing in projects without `project-docs/STATE.md`.

- **SessionStart** (startup, resume, clear, and after a compaction): adds `STATE.md` and the latest
  log entry titles to the agent's context, plus a note after compaction that unlogged details may be lost.
- **PreToolUse** guard, reading `STATE.md`:
  - `mode: mentor` → blocks edits to project files outside `project-docs/` and `CLAUDE.md`, and shell
    commands that write, move or delete project files.
  - `long_commands: user` (default) → blocks installs, builds, tests, dev servers and deploys, so the agent
    hands them to you instead of waiting on them.
  - `git: user` (default) → blocks git commands that change state. Read-only git is allowed.

**Limits, plainly:**
- The shell checks are pattern-based. An unusual command can slip past; the written rules cover the rest.
- The agent could edit `STATE.md` to switch modes. The rules forbid it without your say-so, and the
  log would show it, but a hook can't stop it.
- There is no reliable hook to force a log update *before* compaction, so the rule is "log at the moment
  of the decision", plus the after-compaction reminder.
- To let the agent run long commands or git in a project, set `long_commands: agent` or `git: agent` in
  `STATE.md`.

## Install

**Try it for one session:**
```bash
claude --plugin-dir /path/to/phased-builder
```

**Install permanently (local marketplace):** see the README one folder up, or:
```bash
claude plugin marketplace add /path/to/phased-builder-marketplace
claude plugin install phased-builder@phased-builder-marketplace
```

Then open your project folder and run `/phased-builder:1-start`.
