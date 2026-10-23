# [Project Name]: Working Rules (phased-builder)

<!-- Copied into the project root by `1-start`. Claude Code loads this file at the start of
     every session. Keep it short: rules here, facts in project-docs/. -->

This project is built in phases with the phased-builder plugin. Project memory lives in
`project-docs/`. Chat memory is not reliable: if it is not written in these files, assume it is forgotten.

## Start of every session or skill
1. Read `project-docs/STATE.md` (it may already be in context from the session hook).
2. Say back in 1–3 sentences: current phase, mode, step, what is waiting on whom, and which files you read.
3. Before relying on any past decision, find it in `project-docs/BUILD_LOG.md`, the master docs, or the phase docs.

## Cite-or-admit
- When you use a past decision, name its source: `BUILD_LOG L-014`, `ARCHITECTURE.md > Data Model`, `phases/03-build-login/spec.md > Sessions`.
- If you cannot find a record, say "I have no record of that" and ask. Never fill the gap from memory or guesswork.
- If chat and files disagree, the files win until the user confirms a change. Then update the files.

## Where things live
| File | Holds |
|---|---|
| `project-docs/STATE.md` | Where we are now, next step, what is waiting. Short. Update at the end of every step. |
| `project-docs/scope.md` | Vision, scale, roadmap of phases. |
| `project-docs/PRODUCT.md` | MASTER: the whole product as it works today. |
| `project-docs/ARCHITECTURE.md` | MASTER: current stack, components, data, files, how to run and deploy. |
| `project-docs/BUILD_LOG.md` | Add-only record of decisions, bugs, pivots, setup, releases. |
| `project-docs/PARKING_LOT.md` | Ideas saved for later. |
| `project-docs/phases/NN-type-name/` | One phase: `prd.md` (build only), `spec.md`, `checklist.md`. |
| `project-docs/opportunities/<name>/` | Research and drafts for an opportunity. |

New phases read the master docs first, not old phase folders. Old phase folders are history.

## Log as you go, not at the end
Write a `BUILD_LOG.md` entry at the moment a decision is made, a bug is fixed, a plan changes, or setup changes.
A conversation can be compacted at any time; anything not logged can be lost.

## Decisions: standard practice first
For any decision with real consequences, show a decision card before the user chooses:
- **Decision:** what needs choosing.
- **Standard practice at our scale:** what teams of this size usually do, and why (see `scope.md > Scale`). Search the web and cite when it depends on current versions, prices or services.
- **Other options:** 1–2, each with its trade-off.
- **Recommendation:** one, with the reason.
- **Your call.** Then log the choice.
Do not suggest big-company practice for a small project, or hobby shortcuts for a project that needs more.

## Ideas that come up mid-phase
Do not add them to the current phase. Save them to `PARKING_LOT.md` with the next `P-` number and keep going.

## Commands and git
- `long_commands: user` in STATE.md: the user runs installs, builds, tests, dev servers and deploys. Give the exact command, expected output, and pass/fail rule. Then stop and wait for the pasted output. Do not poll or wait on long processes.
- `git: user` in STATE.md: the user makes all git changes. Give exact commands with files listed. Read-only git (status, log, diff) is fine.

## Modes (per phase, stored in STATE.md and the phase checklist)
- **vibe:** the agent writes the code.
- **mentor:** the agent never writes or edits project code or config. It explains, gives a blueprint, points to docs, reviews the user's code, and answers questions. Worked examples only when asked: small, general, in chat, different names and domain from this project, clearly labelled as an example.
- Only the user can switch modes, in chat. Then update `mode:` in STATE.md and log it.

## Language
Plain, simple English. Short sentences. Explain a new term once, then use it.

## Things the user has asked for in this project
<!-- Standing preferences the user states. Add each with a BUILD_LOG reference. -->
