---
name: 8-build
description: "Build the current feature in ordered, verified slices, in vibe mode (agent writes the code) or mentor mode (user writes the code; agent coaches and reviews). The user runs every test, server and install command and makes every commit; the agent gives exact commands and waits for pasted output. Ends by merging the feature into PRODUCT.md, ARCHITECTURE.md and the roadmap. Run after 7-spec, and again to resume."
---

# 8-build: Build the Feature

You plan the build order briefly, then work through it slice by slice. Every slice is checked by the user running
real commands, then committed by the user. One run can carry a whole feature; a new session resumes at the first
unchecked box.

Read before starting: `${CLAUDE_PLUGIN_ROOT}/shared/mode-choice.md`, `${CLAUDE_PLUGIN_ROOT}/shared/your-turn.md`; in mentor
mode also `references/mentor-guide.md` (relative to this skill). The Interaction Rules in `1-start` and the project
`CLAUDE.md` apply.

## Where Are We

Files only, never chat memory.

1. Read `STATE.md` and the current feature folder.
2. Route:
   - No feature in progress → `6-prd`; stop.
   - `prd.md` and `spec.md` not both `approved` → name what's missing; stop.
   - The spec's **Setup Needed** has unticked items and no matching `setup/` run is `done` → point to `5-setup`
     first. The user may go ahead anyway; log it.
   - No `checklist.md` → **Choose the Mode**, **Git Check**, **Plan the Build**.
   - `checklist.md` `draft` → **The Gut Check**.
   - `approved` with unchecked slices → resume at the first unchecked slice, in the mode recorded in the checklist
     (ask only if the user wants to change it). If `STATE.md > Waiting on` says the user owes output or a commit, ask first.
   - All slices checked → **Final Review**, then **Close the Feature** (resume at the first unchecked box).
3. Say back where they are in one or two sentences: feature, mode, next slice, files read.
4. `STATE.md`: `skill: 8-build`, `mode` (from the checklist or the new choice).

## Choose the Mode
New build: ask (`shared/mode-choice.md`). Record it in the checklist frontmatter and `STATE.md`.

## Git Check
- `git -C <repo> status` (read-only; `<repo>` from `STATE.md`). If it isn't a repository, tell the user and stop;
  they set up the repo. Never `git init` or clone.
- `<repo>/.gitignore` covers `.env`, `.env.*` (allowing `.env.example`). Vibe mode: add missing rules yourself;
  mentor mode: tell the user what to add.
- Secrets or private files already tracked → stop and agree on a fix. Never rewrite history.

## Plan the Build

**Slices, not layers.** A slice is a thin end-to-end piece that makes something usable and checkable. "Build the
database" is a layer; fold it into the first slice that needs it. Use the spec's **Wiring Blueprint** for order.

**Order:** usable evidence at every step, risky unknowns early, never leave the project broken, and the feature's
core behavior (what makes it lovable) early, not last. No target count.

**Write `checklist.md`** from `templates/checklist-template.md`, `status: draft`, `mode:` set. Every slice has every
field, in order, with the exact labels. `You run:` and `Pass when:` come from `spec.md > How We'll Verify`.
`Commit:` lists repo files explicitly, relative to `<repo>/`; never project-docs files.

## The Gut Check
Show the slice order in Markdown (never HTML): what becomes usable at each step and why it sits there. Ask once:
"Does this build order look good, or would you change anything?" If a change reaches into the product or design,
update `prd.md`/`spec.md` in the same pass and log it. A change that adds a feature is a scope change: explain the
cost, or park it. On approval: `status: approved`. **Don't start before approval.**

## The Loop: Vibe Mode
For each unchecked slice:
1. **Build it.** Follow `Build:`, `Spec ref:`, `PRD ref:`. Read only what the slice needs. Follow `PRODUCT.md > Look
   and Feel` / `prd.md > Look and Feel` rather than framework defaults.
2. **Explain briefly** what changed and where (2–4 lines, the user's vocabulary).
3. **Your turn** block (`shared/your-turn.md`). Update `STATE.md > Waiting on`. **End the turn.**
4. **Read the output.** Fail → find the cause, fix, new Your turn block. A real bug gets a `BUG` entry once fixed.
   Can't fix after real attempts → **Safe Recovery**.
5. **Pass → commit commands.** The user commits; check `git log -1 --oneline`; tick the box immediately.
6. **Continue** without asking permission. Pause only for a plan change that changes what the user gets, a failure
   you can't safely fix, or a decision that needs a card.

## The Loop: Mentor Mode
You never write or edit project code or config (`references/mentor-guide.md`; a hook enforces it). For each slice:
1. **Slice brief:** goal, files, wiring, tools with doc links, standard practice, watch-outs, done-when.
2. **The user builds.** Answer questions with the hint ladder. Worked examples only if asked: small, general, in chat,
   different names and domain, labelled.
3. **Review** when they say it's ready: read their files; specific feedback (`file:line`, what, why, what to look up).
   Blocking issues first. No rewritten code.
4. **Your turn** block with the checks. On failure, coach the debugging rather than fixing it.
5. **Commit** commands (user commits). Tick the box.
6. **Continue.**

## When the Plan Turns Out Wrong
1. Say so plainly; this is normal.
2. Check impact across `prd.md`, `spec.md`, later slices, `ARCHITECTURE.md`.
3. Update only what's affected; add a bullet under `## Revisions` with an L-ID; log it now (`DECISION` or `PIVOT`).
4. Get agreement first if it changes what the user gets, their chosen stack, or the kernel. New tools or services →
   `5-setup` (the user installs them). Internal corrections need no discussion; log and continue.

## Safe Recovery
The last commit is the recovery point. Never discard work. You don't run destructive git commands: explain exactly
what would be lost, offer the smallest safe option (usually set aside only this slice's changes), and give the user
the command. Treat it as a plan revision and log it.

## Final Review
1. The user starts the app and explores the feature freely. Ask: "What did you notice, and what would you change?"
2. Ask follow-ups before revising: "What happened, and what did you expect?"
3. Agreed fixes → unchecked items under **Final Review**, each built (vibe) or coached (mentor), checked and committed
   by the user. New features → parking lot.
4. Re-run the PRD's SLC check against what exists.
5. Tick "User confirms the feature is complete" only when they say so.

## Close the Feature
Tick each as you go:
1. **`PRODUCT.md`:** this feature's section rewritten to describe what was actually built; `Status: built`; Core Journey
   and Look and Feel updated if they changed.
2. **`ARCHITECTURE.md`:** merge `spec.md > Changes to ARCHITECTURE.md`, checked against the real code (read it); mark
   (planned) → (built); run and test commands are the ones that actually worked; add a **Design History** row.
3. **`scope.md > Roadmap`:** tick the feature; update Progress (and `STATE.md > Progress`).
4. **Log a `FEATURE` summary:** what shipped, key decisions (L-IDs), bugs (L-IDs), parked ideas (P-IDs).
5. **Show the parking lot** items added during this feature, in one short list.
6. **Rewrite `STATE.md`:** `current_feature: none`, `mode: vibe`, `skill` and Next step for what's next.
   (Doc updates are outside git: no commit step.)
7. **Offer once:** the optional learning wrap-up and app map (`references/app-map.md`).

## Hand Off
"F-NN is built and merged into the master docs." Then suggest one next step: the next roadmap feature (`6-prd`);
`9-ship` if they want to release (e.g. the SLC v1 line was just reached); `3-scope` to change the roadmap;
`4-architecture` if the design needs rethinking; `10-opportunity` if one came up.

## Conversation Style
- **Executor in vibe mode, coach in mentor mode.** Don't add, reorder or skip slices without a logged revision.
- **Build, don't narrate.**
- **The user's vocabulary,** plain and simple.
