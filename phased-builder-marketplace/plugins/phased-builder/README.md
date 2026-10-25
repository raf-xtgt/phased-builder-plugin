# phased-builder

A Claude Code plugin for building a product plan-first with **flipped interaction**: the agent interviews you,
researches, shows you what's standard at your scale, and you make the decisions.

Adapted from [challengepost/learn-ai-basics](https://github.com/challengepost/learn-ai-basics)
(MIT, © 2026 Devpost). See `LICENSE`.

## The skills

| Skill | Job | When | Modes |
|---|---|---|---|
| `/phased-builder:1-start` | Get to know you; set up `project-docs/` and `CLAUDE.md` | Once per project | vibe |
| `/phased-builder:2-ideation` | Brainstorm, alternatives, competitor and market research, feasibility, opportunity fit | Once, to decide what to build | vibe |
| `/phased-builder:3-scope` | Product manager: feature list, scrutiny, parking lot, scale, `PRODUCT.md`, roadmap checklist | After ideation; again to change the roadmap | vibe |
| `/phased-builder:4-architecture` | High-level system design: components, data, AI, database, cloud, cost, folders | Draft once; refine any time | vibe or mentor |
| `/phased-builder:5-setup` | Stack, dependencies, dev tools, database, cloud. **You run commands and console steps; the agent edits config files and debugs.** Writes `SETUP.md` + `SETUP_EXAMPLE.md` | Main setup once; add-ons any time | vibe |
| `/phased-builder:6-prd` | One feature: journey, behaviors, criteria, SLC check | Each feature | vibe |
| `/phased-builder:7-spec` | How the feature is built (agent writes the spec in both modes) | Each feature | vibe or mentor |
| `/phased-builder:8-build` | Slices, checks, final review, merge into master docs | Each feature | vibe or mentor |
| `/phased-builder:9-ship` | Release: checks, secrets, README, changelog, deploy | After any feature | vibe |
| `/phased-builder:10-opportunity` | Hackathon, incubator, investor pitch, social launch | Any time, or first | vibe |

```
1-start → 2-ideation → 3-scope → 4-architecture → 5-setup → per feature: 6-prd → 7-spec → 8-build
          10-opportunity first if one drives the project · 9-ship after any feature
          3-scope, 4-architecture, 5-setup can be re-run whenever things change
```

**Modes** (asked every time `4-architecture`, `7-spec` or `8-build` starts):
- **Vibe:** the agent proposes and writes (code too, in `8-build`).
- **Mentor:** you lead. In architecture and spec, the agent coaches you on system design (standards, trade-offs,
  costs) and then writes the document. In build, you write all the code; the agent gives blueprints, doc links,
  reviews, and small general examples only when asked.

**You run every install, test, server and deploy command, and make every commit,** in every skill. The agent gives
exact commands and expected output, then waits for you to paste the result. **The agent edits config files itself**
(package.json, pubspec.yaml, .xml, .kts, .yaml, .toml, .gitignore…) in vibe mode and in setup.

**Responses** are short, plain English, with tables for long or comparative content. Settled points (answers you've
given, things in the docs) aren't re-asked or re-raised unless something conflicts with them or is vague.

**Opportunities:** a brief from `10-opportunity` feeds ideation, scope, and especially architecture and spec, which
design for maximum impact (judging criteria, deep vs shallow use of required tech, the demo moment) without bending
the product away from its users.

## Folder layout

Run Claude Code from a **parent folder** that holds your **one GitHub repo** (create and clone it yourself first).
Everything the plugin writes lives in the parent folder, outside git, and is never committed.

```
<parent>/                     <- run Claude Code here
├── CLAUDE.md                 working rules (loaded every session)
├── SETUP.md                  private: one-time setup, run locally, deploy (may hold real IDs/keys)
├── <repo>/                   your GitHub repo (the only thing in git)
│   └── SETUP_EXAMPLE.md      public copy of SETUP.md with dummy values (committed)
└── project-docs/             project memory
    ├── STATE.md              where we are now (loaded every session by a hook)
    ├── ideation.md           brainstorm, research, decision
    ├── PRODUCT.md            master: problem, solution, users, features with status
    ├── scope.md              scale, SLC, feature review, roadmap checklist
    ├── ARCHITECTURE.md       master: the system design, refined over time
    ├── setup/NN-name.md      each setup run: steps, issues, proof it works
    ├── features/NN-name/     prd.md, spec.md, checklist.md
    ├── BUILD_LOG.md          decisions, bugs, pivots (add-only, L-001...)
    ├── PARKING_LOT.md        ideas for later (P-001...)
    ├── profile.md            your context
    └── opportunities/<name>/ brief.md, research.md, drafts/
```

## Hooks (need `python3` on your PATH)

Both do nothing in projects without `project-docs/STATE.md`.

- **SessionStart** (startup, resume, clear, after compaction): adds `STATE.md` and the latest log titles to the
  agent's context, plus a warning after compaction that anything not logged may be lost.
- **PreToolUse** guard, reading `STATE.md`:
  - `mode: mentor` → blocks edits to project files outside `project-docs/`, `CLAUDE.md` and `SETUP.md`, and shell
    commands that write, move or delete project files.
  - `long_commands: user` (default) → blocks installs, builds, tests, dev servers and deploys (`--version` checks allowed).
  - `git: user` (default) → blocks git commands that change state (incl. `git init`). Read-only git, including
    `git -C <repo> status/log/diff`, is allowed.

**Limits, plainly:** shell checks are pattern-based, so an unusual command can slip past (the written rules cover
the rest); the agent could edit `mode:` in `STATE.md` itself (the rules forbid it, but a hook can't stop it); there's
no reliable hook to force a log update before compaction. To let the agent run long commands or git, set
`long_commands: agent` or `git: agent` in `STATE.md`.

## Install

```bash
claude plugin marketplace add /path/to/phased-builder-marketplace
claude plugin install phased-builder@phased-builder-marketplace
```

Try without installing: `claude --plugin-dir /path/to/phased-builder-marketplace/plugins/phased-builder`.
Then create a parent folder, clone your GitHub repo into it, open Claude Code in the **parent** folder, and run
`/phased-builder:1-start`.
