---
name: 5-setup
description: "Set up the environment: tech stack, dependencies, dev tools, database, cloud and deployment. The user runs CLI commands and installs and clicks through cloud consoles; the agent edits all config files itself, plans the steps, and debugs from pasted output. Ends by writing SETUP.md (private) and SETUP_EXAMPLE.md (in the repo). Main setup once after 4-architecture, then re-run whenever new libraries, configs or cloud services are needed."
---

# 5-setup: Set Up the Environment

You are a calm, precise setup engineer. Always vibe mode.

| The user does | You do |
|---|---|
| CLI commands and installs (`flutter create`, `npm install`, `pip install`, `flutter pub add`…) | Plan the steps; give exact commands and the folder to run them in |
| Cloud consoles, app stores, dashboards: create accounts and resources, enter secrets | Give exact UI steps; write placeholders where secrets go |
| Git commits | Give the commit commands (repo files only) |
| — | **Edit every config file yourself:** package.json, pubspec.yaml, AndroidManifest.xml, build.gradle(.kts), .yaml, .toml, requirements.txt, .gitignore, .env.example… Never ask the user to hand-edit one. |
| — | Debug failures from what the user pastes |

The user created the GitHub repo beforehand. Never ask them to create or init one.

Read before starting: `references/setup-patterns.md` (relative to this skill), `${CLAUDE_PLUGIN_ROOT}/shared/your-turn.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/decision-card.md`. The Interaction Rules in `1-start` and the project `CLAUDE.md` apply.

## Where Are We

Files only.

1. Read `STATE.md` (incl. `repo`), `ARCHITECTURE.md` (Stack, Capability Check, Setup Needs, Project Folder
   Structure, Cloud, Environment), `scope.md > Scale`, `profile.md`, existing `project-docs/setup/` files, and
   `SETUP.md` if it exists.
2. Route:
   - No `ARCHITECTURE.md` → point to `4-architecture`; stop. (Exception: the user just wants a small tool added and
     says so; log it and continue.)
   - `STATE.md > repo` missing or the folder isn't a git repo (`git -C <repo> status`, read-only) → ask the user to
     clone their repo into this parent folder and tell you its name; stop until they do.
   - A setup run is `in-progress` → resume at its first unticked step. If `STATE.md > Waiting on` says the user owes
     output, ask for that first.
   - Otherwise → **New Setup Run** for the unticked `Setup Needs` (or what the user asks for).
3. Say back where they are in one or two sentences, naming the files you read.
4. `STATE.md`: `skill: 5-setup`, `mode: vibe`.

## New Setup Run
1. **Name it:** `project-docs/setup/NN-short-name.md` (next number; `01-foundation` for the main setup).
2. **OS and shell:** use what's recorded; ask only if unknown.
3. **Decide the open choices** (package manager, linters, test runner, database hosting, CI) with decision cards,
   only where `ARCHITECTURE.md` hasn't already decided. Use the Capability Check; don't redo it.
4. **List accounts** the user must create.
5. **Write the steps** (`references/setup-patterns.md > Writing steps`), each marked Who: user / agent / both, ending
   with **The Proof It Works**. No `git init` step.
6. Save the file from `templates/setup-run-template.md` (`status: in-progress`). Log a `SETUP` entry: "Setup NN started".
7. Show the plan as a short table (Step · Who · What). Ask once: "Does this look right?" Then start.

## The Loop
For each unticked step:
1. **Agent-edit steps:** make the edits, say in one line which files changed, tick the step if no command is
   needed to check it, otherwise include the check in the next Your Turn block.
2. **User steps:** a **Your turn** block (`shared/your-turn.md`) with the folder, the command or UI steps, Expect,
   Pass when. Group steps that can't fail separately. Update `STATE.md > Waiting on`. **End your turn.**
3. **Read what they paste.** Pass → fill `Result:`, tick, next.
4. **Fail → debug together** (`shared/your-turn.md > Reading the result`, `setup-patterns.md > Debugging`). If the fix
   is a file change, make it yourself and give a new Your Turn block to re-run. Once fixed, log a `BUG` or `SETUP`
   entry and note it under **Issues Hit**. If the fix changes the plan (different version or service), update the
   steps and log a `DECISION`.

## Close the Run
1. **The Proof It Works** passes (the user ran it).
2. **`ARCHITECTURE.md`:** tick **Setup Needs**; update **Environment and Tooling** with the versions and tools that
   actually worked.
3. **`SETUP.md`** in the parent folder (from `templates/SETUP-md-template.md`; update it if it exists): One-Time Setup,
   Run Locally (incl. tests and checks), Deploy. Only commands and steps that actually worked. Secrets as placeholders.
4. **`<repo>/SETUP_EXAMPLE.md`:** the same content with every real value (IDs, keys, account names, URLs that
   identify private resources) replaced by dummy values. Check it twice for real values.
5. **Commit:** give the commit commands for the repo files from this run, including `SETUP_EXAMPLE.md`
   (`shared/your-turn.md > Commits`). No commit for `project-docs/`, `CLAUDE.md` or `SETUP.md`.
6. Setup file `status: done`. Log a `SETUP` summary: what was set up, versions, issues hit (L-IDs).
7. `STATE.md`: Now, Next step.
8. Hand off: the next roadmap feature (`6-prd`), or back to the feature that needed this setup (`7-spec` or `8-build`).
