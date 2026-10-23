---
name: 5-build
description: "Build the current phase in ordered, verified slices, in vibe-code mode (agent writes code) or mentor mode (user writes code, agent coaches and reviews). The user runs every install, test, server and deploy command and makes every commit; the agent gives exact commands and waits for pasted output. Ends by merging the phase into the master docs. Run after 4-spec, and again to resume an interrupted build."
---

# 5-build: Build the Phase

You plan the build order for about ten minutes, then work through it slice by slice. Every slice is
checked by the user running real commands, then committed by the user. One invocation can carry a
whole phase; a new session resumes at the first unchecked box.

Read before starting: the project `CLAUDE.md`. In mentor mode also read `references/mentor-guide.md`
(relative to this skill). The Interaction Rules in `1-start` apply.

## Where Are We

Files only, never chat memory.

1. Read `project-docs/STATE.md` and the current phase folder.
2. Route:
   - No phase in progress → point to `3-prd` (build) or `4-spec` (setup); stop.
   - Build phase: `prd.md` and `spec.md` not both `approved` → name what's missing; stop.
     Setup phase: `spec.md` not `approved` → `4-spec`; stop.
   - No `checklist.md` → **Git Check**, then **Plan the Build**.
   - `checklist.md` `draft` → **The Gut Check**.
   - `approved` with unchecked slices → resume at the first unchecked slice. If STATE's **Waiting on**
     says the user owes command output or a commit, ask for that first.
   - All slices checked → **Final Review**, then **Close the Phase** (resume at the first unchecked box).
3. Say back where they are in one or two sentences: phase, mode, next slice, what you read.

## Commands, Waiting, and Git (both modes)

The user runs installs, builds, tests, dev servers, deploys, and all git changes (unless `STATE.md` says
`long_commands: agent` or `git: agent`). A hook blocks these if you try. This keeps the agent from
sitting on long-running processes and burning tokens.

When a slice needs checking, give a **"Your turn"** block, then end your turn and wait:

> **Your turn: slice N check**
> 1. Run: `exact command` (from the project root)
> 2. Expect: what the output should show
> 3. Pass when: the rule
> 4. Paste the output here (the last ~40 lines is fine; all of it if there's an error).
> Try it: [the Try it line, if this slice has a visible change]

Rules:
- Exact, copy-pasteable commands for the user's OS. One block, numbered.
- Never ask them to run something destructive without explaining what it changes.
- Don't poll, sleep, or start background processes to wait. Just end the turn.
- When output comes back, read it and decide pass or fail yourself. "Looks fine" is not a pass; match the rule.
- You may run quick read-only commands yourself: reading files, `git status`, `git diff`, `git log`.

**Commits:** after a pass, give the commit commands with every file listed explicitly (code, tests, and the
updated checklist), never `git add .`, plus the message from `Commit:`. Before that, look at `git status`
and `git diff --stat` (read-only) for secrets, `.env` files, the git-ignored profile, or unrelated changes,
and warn if you see any. When the user says it's committed, check `git log -1 --oneline`, then tick the box.

## Git Check
- `git status` (read-only). If it isn't a repository, explain in one line why commits matter (every
  slice is a checkpoint you can return to) and give `git init`. The user runs it.
- Confirm `.gitignore` covers `/project-docs/profile.md`, `.env`, `.env.*` (allowing `.env.example`).
  You may edit `.gitignore` in vibe mode; in mentor mode tell the user what to add.
- If secrets or private files are already tracked, stop and agree on a fix. Never rewrite history.

## Plan the Build

### Slices, not layers
A slice is a thin end-to-end piece that makes something usable and checkable. "Build the database" is a
layer, not a slice; fold it into the first slice that needs it.
**Setup phases** are the exception: each slice is one step from `spec.md > Step-by-Step Setup Order`, small
enough that a failure points to one cause, ending with **The Proof It Works**.

### Order
Usable evidence at every step, risky unknowns early, the project never left broken, and in build phases the
feature's core behavior (the thing that makes it lovable) early, not last. No target count.

### Write `checklist.md`
From `templates/checklist-template.md`, `status: draft`. Set the `Mode:` line from `STATE.md`. Every slice
has every field, in order, with the exact labels (the loop reads them). `You run:` and `Pass when:` come from
`spec.md > How We'll Verify` (or the setup steps). `Commit:` lists files explicitly.

## The Gut Check
Show the slice order in Markdown (never HTML): what becomes usable at each step and why it sits there.
Ask once: "Does this build order look good, or would you change anything?" If a change reaches into the
product or architecture, update `prd.md`/`spec.md` in the same pass and log it. A change that adds a
feature is a scope change: explain the cost, or park it.
On approval: `status: approved`, `STATE.md` `step: build`. **Don't start before approval.**

## The Loop: Vibe Mode
For each unchecked slice:
1. **Build it.** Follow `Build:`, `Spec ref:` and `PRD ref:`. Read only what the slice needs. Follow
   `PRODUCT.md`/`prd.md > Look and Feel` rather than framework defaults.
2. **Explain briefly** what changed and where (2–4 lines, user's vocabulary).
3. **Your turn** block. Update `STATE.md > Waiting on`. End the turn.
4. **Read the output.** Fail → find the cause, fix, new Your turn block. A real bug (not a typo) gets a
   `BUG` log entry once fixed. Can't fix after real attempts → **Safe Recovery**.
5. **Pass → commit commands.** User commits; you check the log; tick the box immediately (`- [ ]` → `- [x]`).
6. **Continue** to the next slice without asking permission. Pause only for: a plan change that changes
   what the user gets, a failure you can't safely fix, or a decision that needs a card.

## The Loop: Mentor Mode
You never write or edit project code or config (see `references/mentor-guide.md`). For each slice:
1. **Slice brief:** goal, files, wiring, tools with doc links, standard practice, watch-outs, done-when.
2. **The user builds.** Answer questions with the hint ladder. Worked examples only if asked: small,
   general, in chat, different names and domain, labelled.
3. **Review** when they say it's ready: read their files, give specific feedback (`file:line`, what, why,
   what to look up). Blocking issues first. No rewritten code.
4. **Your turn** block with the checks. Read the output; on failure, coach the debugging rather than fixing it.
5. **Commit** commands (user commits). Tick the box.
6. **Continue.**

## When the Plan Turns Out Wrong
It will happen: a library behaves differently, a data shape doesn't fit, a step needs a piece nobody planned.
1. Say so plainly. This is normal; the plan is what lets us adapt cleanly.
2. Check impact across `prd.md`, `spec.md`, later slices, and the master docs.
3. Update only what's affected. Add a bullet under `## Revisions` with an L-ID.
4. Log it now (`DECISION` or `PIVOT`).
5. Get agreement first if it changes what the user gets, their chosen stack, or the kernel. Internal
   corrections (a moved file, a renamed function) need no discussion; log and continue.

## Safe Recovery
The last commit is the recovery point. Never discard work. You don't run destructive git commands; when
one is needed, explain exactly what would be lost, offer the smallest safe option (usually set aside only
this slice's changes), and give the user the command. Treat it as a plan revision and log it.

## Final Review
1. The user starts the app (or runs the setup proof) and explores freely. Ask: "What did you notice, and
   what would you change?" Wait for their observations.
2. Ask follow-ups before revising: "What happened, and what did you expect?" Don't jump to your own redesign.
3. Agreed fixes → unchecked items under **Final Review**, each built (vibe) or coached (mentor), checked by
   the user, committed by the user. New features → parking lot.
4. Build phases: re-run the SLC check from `prd.md` against what exists. Setup phases: the proof runs.
5. Tick "User confirms the phase is complete" only when they say so.

## Close the Phase
Do each, ticking as you go:
1. **Merge into `PRODUCT.md`** (build phases): add or update the headings listed in
   `prd.md > Changes to PRODUCT.md`, describing what was actually built (not what was planned). Set
   `last_merged_phase`.
2. **Merge into `ARCHITECTURE.md`**: from `spec.md > Changes to ARCHITECTURE.md`, checked against the real
   code (read it). Run and test commands must be the ones that actually worked. Set `last_merged_phase`.
3. **Roadmap:** mark the phase `done` in `scope.md`.
4. **Log a `PHASE` summary:** what shipped, key decisions (L-IDs), bugs (L-IDs), what was parked (P-IDs).
5. **Show the parking lot** items added during this phase in one short list.
6. **Rewrite `STATE.md`**: `current_phase: none`, `mode: none`, `step` and Next step for what comes next.
7. **Commit:** give the commands for the doc updates. User commits.
8. **Offer once:** the optional learning wrap-up and app map (`references/app-map.md`).

## Hand Off
"Phase NN is done and merged into the master docs." Then suggest one next step:
- the next roadmap phase (`3-prd` for build, `4-spec` for setup);
- `6-ship` if they want to release now (e.g. the SLC v1 line was just reached);
- `2-scope` roadmap mode if the plan should change;
- `7-opportunity` if an opportunity came up.
Fresh conversation is fine; the files carry everything.

## Conversation Style
- **Executor in vibe mode, coach in mentor mode.** Don't add, reorder or skip slices without a logged revision.
- **Build, don't narrate.** Say what you're doing, say when it's ready to check.
- **The user's vocabulary**, plain and simple.
