# "Your Turn" Handoff: Agent Reference

Used by `5-setup`, `8-build` and `9-ship`.

## Who does what
| The user does | The agent does |
|---|---|
| Runs CLI commands: installs, builds, tests, dev servers, deploys, code generators (`long_commands: user`) | Plans the steps, gives exact commands, reads the pasted output, debugs |
| Clicks through cloud consoles, app stores and dashboards; creates accounts; enters secrets | Gives the exact UI steps; writes placeholders where secrets go |
| All git changes: add, commit, push (`git: user`) | Gives the commit commands; runs read-only git checks |
| — | **Edits project files itself** in vibe mode and in `5-setup`: config files (`package.json`, `pubspec.yaml`, `.xml`, `.kts`, `.gradle`, `.yaml`, `.toml`, `requirements.txt`, `.gitignore`, `.env.example`…) and code |

In **mentor mode** (`8-build`), the user also writes code and project files; the agent explains instead.
A hook blocks the commands in the left column if the agent tries to run them. This keeps the agent from waiting on
long processes and spending tokens.

## Folders
Claude Code runs in the **parent folder**. The code lives in the repo folder named by `STATE.md > repo`.
- Every command block starts with the folder: `cd <repo>` (or says "from `<repo>/`").
- Git commands: `git -C <repo> ...` or from inside `<repo>/`.
- `project-docs/`, `CLAUDE.md` and `SETUP.md` are in the parent folder, outside git. **Never** include them in a commit.

## The block
When the user needs to do something, give one numbered block, then **end your turn and wait**:

> **Your turn: [what this is, e.g. "setup step 3" or "slice 2 check"]**
> 1. Run (from `<repo>/`): `exact command` — or for UI steps: where to click, what to enter, what to choose.
> 2. Expect: what the output or screen should show.
> 3. Pass when: the rule.
> 4. Paste: the output (last ~40 lines is fine; all of it on error), or a screenshot for UI steps.

Before the block, if you edited files for this step, list them in one line ("I edited `android/app/build.gradle.kts`
and `AndroidManifest.xml`.") so the user knows what changed.

## Rules
- Exact, copy-pasteable commands for the user's OS and shell (ask once if unknown; log it as `PREFERENCE`).
- Group small steps that can't fail separately; split steps where a failure needs its own diagnosis.
- **Secrets:** never ask for keys or passwords in chat. Write placeholders (`<YOUR_API_KEY>`) and tell the user where
  to put real values (`.env`, `SETUP.md`, the host's secret store). If pasted output shows a secret, tell them to rotate it.
- Never ask them to run something destructive without saying exactly what it changes.
- Don't poll, sleep, or start background processes to wait. End the turn.
- You may run quick read-only commands yourself: reading files, `ls`, `--version` checks, `git status`, `git diff`, `git log`.

## Reading the result
- Decide pass or fail by the rule, not by "looks fine".
- **On failure, debug together:** what the error means in plain words, the most likely cause first, then the next
  single check or fix. If the fix is a file edit, make it yourself (vibe/setup) and give a new Your Turn block to re-run.
  Search the web for unfamiliar errors and cite what you find.
- Once fixed, log a `BUG` (or `SETUP`) entry: the error, the cause, the fix.

## Commits
After a pass, give the commit commands for **repo files only**, each listed explicitly (never `git add .`), with
paths relative to `<repo>/` and a short message:
```
cd <repo>
git add pubspec.yaml lib/main.dart
git commit -m "Add sandglass timer screen"
```
First check `git -C <repo> status` and `git -C <repo> diff --stat` (read-only) for secrets, `.env` files, or unrelated
changes, and warn if you see any. Doc-only updates (`project-docs/`, `CLAUDE.md`, `SETUP.md`) need **no** commit step.
When the user says it's committed, check `git -C <repo> log -1 --oneline`.

The user creates and owns the GitHub repo. Never ask them to create, init, or re-clone a repo, or to change its
visibility, unless they ask.
