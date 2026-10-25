# [Project Name]: Working Rules (phased-builder)

<!-- Copied into the parent folder by `1-start`. Claude Code loads this file at the start of
     every session. Keep it short: rules here, facts in project-docs/. Not committed to git. -->

This project is built with the phased-builder plugin. Project memory lives in `project-docs/`.
Chat memory is not reliable: if it is not written in these files, assume it is forgotten.

## Folder layout
```
<parent>/              <- Claude Code runs here. Nothing in this folder is in git...
├── CLAUDE.md          this file
├── SETUP.md           private setup, run and deploy steps (may hold real IDs and keys)
├── project-docs/      project memory
└── <repo>/            ...except this: the one GitHub repo (name in STATE.md > repo). The user created it.
    └── SETUP_EXAMPLE.md   SETUP.md with dummy values (committed)
```
Never commit `project-docs/`, `CLAUDE.md` or `SETUP.md`. Never create, init or re-clone the repo.

## The flow
`1-start` → `2-ideation` → `3-scope` → `4-architecture` → `5-setup` → for each feature:
`6-prd` → `7-spec` → `8-build`. `9-ship` after any feature. `10-opportunity` any time, or first.
`3-scope`, `4-architecture` and `5-setup` can be run again whenever the roadmap, design or setup changes.

## Start of every session or skill
1. Read `project-docs/STATE.md` (it may already be in context from the session hook).
2. Say back in 1–3 sentences: current skill, feature, mode, what is waiting on whom, and which files you read.
3. Before relying on any past decision, find it in `project-docs/BUILD_LOG.md`, the master docs, or the feature docs.

## Cite-or-admit
- When you use a past decision, name its source: `BUILD_LOG L-014`, `ARCHITECTURE.md > Data Model`,
  `features/03-sand-animation/spec.md > Rendering`.
- If you cannot find a record, say "I have no record of that" and ask. Never fill the gap from memory or guesswork.
- If chat and files disagree, the files win until the user confirms a change. Then update the files.

## Where things live
| File | Holds |
|---|---|
| `project-docs/STATE.md` | Where we are now, next step, what is waiting. Short. Update at the end of every step. |
| `project-docs/ideation.md` | Brainstorm, research, and the decision on what we're building. |
| `project-docs/PRODUCT.md` | MASTER: problem, solution, target users, features with status (planned / in progress / built). |
| `project-docs/scope.md` | Scale, the product's SLC, the roadmap checklist, what's out. |
| `project-docs/ARCHITECTURE.md` | MASTER: the system design, high level first, refined over time. |
| `SETUP.md` (parent folder) | One-time setup, run locally, deploy. Private. `<repo>/SETUP_EXAMPLE.md` is the public copy. |
| `project-docs/setup/NN-name.md` | One setup run: steps the user did and what happened. |
| `project-docs/features/NN-name/` | One feature: `prd.md`, `spec.md`, `checklist.md`. |
| `project-docs/BUILD_LOG.md` | Add-only record of decisions, bugs, pivots, setup, releases. |
| `project-docs/PARKING_LOT.md` | Ideas saved for later. |
| `project-docs/opportunities/<name>/` | Research and drafts for an opportunity. |

New work reads the master docs first, not old feature folders. Old folders are history.

## Log as you go, not at the end
Write a `BUILD_LOG.md` entry at the moment a decision is made, a bug is fixed, a plan changes, or setup changes.
A conversation can be compacted at any time; anything not logged can be lost.

## Decisions: standard practice first
For any decision with real consequences, show a decision card before the user chooses:
**Decision** · **Standard practice at our scale** (see `scope.md > Scale`; search and cite when it depends on
current versions, prices or services) · **Other options** (1–2, with trade-offs) · **Recommendation** · **Your call.**
Then log the choice. No big-company practice for a small project, no hobby shortcuts for one that needs more.

## Opportunities
If `project-docs/opportunities/` has an active brief, ideation, scope, architecture and spec must consider it
(see each skill). The product's kernel still comes first.

## Ideas that come up mid-work
Do not add them to the current work. Save them to `PARKING_LOT.md` with the next `P-` number and keep going.

## Commands, files and git
- **The user runs** installs, builds, tests, dev servers, deploys and code generators (`long_commands: user`), and
  clicks through cloud consoles. Give the exact command (and folder), expected output, and pass/fail rule. Then stop
  and wait for the pasted output. Never poll or wait on long processes.
- **The agent edits files** in vibe mode and in `5-setup`: config files (package.json, pubspec.yaml, .xml, .kts,
  .yaml, .toml, requirements.txt, .gitignore...) and code. Never ask the user to hand-edit a config file.
- **Git (`git: user`):** the user makes all git changes. Give commands for repo files only, each listed. Read-only
  git (`git -C <repo> status/log/diff`) is fine. Details: the plugin's `shared/your-turn.md`.

## Modes
Asked at the start of `4-architecture`, `7-spec` and `8-build`, every time. All other skills (including `5-setup`)
are vibe.
- **vibe:** the agent proposes and writes (code in `8-build`, documents everywhere).
- **mentor:** the agent teaches. In `4-architecture` and `7-spec`: system design coaching; the user proposes, the
  agent challenges and explains, then the agent writes the document. In `8-build`: the user writes all code; the
  agent gives blueprints, doc links and reviews. Worked examples only when asked: small, general, in chat,
  different names and domain from this project, labelled as an example.
- Only the user can switch modes, in chat. Then update `mode:` in STATE.md and log it.

## How to write responses
- **Short and plain.** Simple English, short sentences. Say it once. No filler ("Great question", "Let me",
  "It's worth noting", recaps of what the user just said, closing encouragement).
- **Lead with the answer or the question.** Context after, only if needed.
- **Tables for anything long or comparative:** verdicts, options, trade-offs, findings, step summaries. Columns
  like Item · Verdict · Reason. Not stacked paragraphs.
- **One question block per turn,** at the end. Ask only what you can't find in the files.
- Explain a new term once, then use it.

## Settled points: don't repeat them
A point is settled once the user has answered it or it's recorded in `profile.md`, `scope.md`, a master doc or
`BUILD_LOG.md`. Before asking anything, check those files.
Don't re-ask a settled point and don't keep raising it as a risk or concern. Bring it up again **only** when:
1. a decision or action goes against what's settled (say which record it conflicts with), or
2. something about it is genuinely vague and needs clarifying (ask once, specifically).

## Things the user has asked for in this project
<!-- Standing preferences the user states. Add each with a BUILD_LOG reference. -->
