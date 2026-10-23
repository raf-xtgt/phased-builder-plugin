# [Project Name]: Working Rules (phased-builder)

<!-- Copied into the project root by `1-start`. Claude Code loads this file at the start of
     every session. Keep it short: rules here, facts in project-docs/. -->

This project is built with the phased-builder plugin. Project memory lives in `project-docs/`.
Chat memory is not reliable: if it is not written in these files, assume it is forgotten.

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

## Commands, setup and git
- `long_commands: user`: the user runs installs, builds, tests, dev servers and deploys. Give the exact command,
  expected output, and pass/fail rule. Then stop and wait for the pasted output. Never poll or wait on long processes.
- Setup (`5-setup`): the user does every step (commands, config files, cloud consoles). The agent gives steps and
  debugs from what the user pastes. It does not write project files.
- `git: user`: the user makes all git changes. Give exact commands with files listed. Read-only git is fine.

## Modes
Asked at the start of `4-architecture`, `7-spec` and `8-build`, every time. All other skills are vibe.
- **vibe:** the agent proposes and writes (code in `8-build`, documents everywhere).
- **mentor:** the agent teaches. In `4-architecture` and `7-spec`: system design coaching; the user proposes, the
  agent challenges and explains, then the agent writes the document. In `8-build`: the user writes all code; the
  agent gives blueprints, doc links and reviews. Worked examples only when asked: small, general, in chat,
  different names and domain from this project, labelled as an example.
- Only the user can switch modes, in chat. Then update `mode:` in STATE.md and log it.

## Language
Plain, simple English. Short sentences. Explain a new term once, then use it.

## Things the user has asked for in this project
<!-- Standing preferences the user states. Add each with a BUILD_LOG reference. -->
