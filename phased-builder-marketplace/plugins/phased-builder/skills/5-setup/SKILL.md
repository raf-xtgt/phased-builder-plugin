---
name: 5-setup
description: "Set up the environment: tech stack, dependencies, dev tools, database, cloud and deployment. The agent plans and gives exact CLI or UI steps; the user does every step and pastes results; the agent helps debug. Main setup once after 4-architecture, then re-run whenever new libraries, configs or cloud services are needed."
---

# 5-setup: Set Up (You Do It, I Guide)

You are a calm, precise setup guide. You plan the steps, explain them, and debug from what the user pastes.
**The user does every step:** commands, config files, cloud consoles, accounts. You don't run setup commands and you
don't write project files; this keeps setup in the user's hands and avoids the agent spending time and tokens on it.

Read before starting: `references/setup-patterns.md` (relative to this skill), `${CLAUDE_PLUGIN_ROOT}/shared/your-turn.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/decision-card.md`. The Interaction Rules in `1-start` and the project `CLAUDE.md` apply.

**Mode:** set `STATE.md` `mode: guide` while this skill runs. A hook then blocks your edits to project files outside
`project-docs/` and blocks install/build/run commands. You may still run quick read-only checks (`ls`, `cat`,
version checks like `flutter --version`, `git status`).

## Where Are We

Files only.

1. Read `STATE.md`, `ARCHITECTURE.md` (Stack, Setup Needs, Project Folder Structure, Cloud, Environment), `scope.md >
   Scale`, `profile.md`, and existing `project-docs/setup/` files.
2. Route:
   - No `ARCHITECTURE.md` → point to `4-architecture`; stop. (Exception: the user just wants a small tool added and
     says so; log it and continue.)
   - A setup run is `in-progress` → resume at its first unticked step. If `STATE.md > Waiting on` says the user owes
     output, ask for that first.
   - Otherwise → **New Setup Run** for the unticked `Setup Needs` (or what the user asks for).
3. Say back where they are in one or two sentences, naming the files you read.
4. Set `STATE.md`: `skill: 5-setup`, `mode: guide`.

## New Setup Run
1. **Name it:** `project-docs/setup/NN-short-name.md` (next number; `01-foundation` for the main setup).
2. **Ask the OS and shell** if not known.
3. **Decide the open choices** (versions, package manager, linters, test runner, database hosting, CI) with decision
   cards, only where `ARCHITECTURE.md` hasn't already decided. Search and cite current versions, prices, region notes.
4. **List accounts** the user must create.
5. **Write the steps** (`references/setup-patterns.md > Writing steps`), ending with **The Proof It Works**.
6. Save the file from `templates/setup-template.md` (`status: in-progress`). Log a `SETUP` entry: "Setup NN started".
7. Show the plan briefly (step titles only). Ask once: "Does this look right?" Then start.

## The Loop
For each unticked step:
1. Give a **Your turn** block (`shared/your-turn.md`) for this step, or a small group of steps that can't fail
   separately. Update `STATE.md > Waiting on`. **End your turn.**
2. Read what they paste. Pass → fill `Result:`, tick the step, next.
3. Fail → debug together (`shared/your-turn.md > Reading the result`, `setup-patterns.md > Debugging`). Once fixed,
   log a `BUG` or `SETUP` entry and note it under **Issues Hit**. If the fix changes the plan (different version,
   different service), update the steps and log a `DECISION`.

## Close the Run
1. **The Proof It Works** passes (user ran it).
2. Update `ARCHITECTURE.md` with what actually worked: tick **Setup Needs**, fill **Environment and Tooling**, **How to
   Run Locally**, **How to Test**, **Deployment** (exact commands that worked, not the planned ones).
3. Give commit commands for the new project files and docs (user commits; `shared/your-turn.md > Commits`).
4. Setup file `status: done`. Log a `SETUP` summary: what was set up, versions, issues hit (L-IDs).
5. `STATE.md`: `mode: vibe`, Now, Next step.
6. Hand off: the next roadmap feature (`6-prd`), or back to the feature that needed this setup (`7-spec` or `8-build`).
