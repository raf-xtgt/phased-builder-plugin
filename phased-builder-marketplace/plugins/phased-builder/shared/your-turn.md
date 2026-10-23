# "Your Turn" Handoff: Agent Reference

Used by `5-setup`, `8-build` and `9-ship`. The user runs installs, builds, tests, dev servers, deploys,
setup steps and all git changes (unless `STATE.md` says `long_commands: agent` or `git: agent`). A hook blocks
those commands if you try. This keeps the agent from waiting on long processes and spending tokens.

## The block
When the user needs to do something, give one numbered block, then **end your turn and wait**:

> **Your turn: [what this is, e.g. "setup step 3" or "slice 2 check"]**
> 1. Run: `exact command` (from the project root) — or for UI steps: where to click, what to enter, what to choose.
> 2. Expect: what the output or screen should show.
> 3. Pass when: the rule.
> 4. Paste the output here (the last ~40 lines is fine; all of it if there's an error). For UI steps, a
>    screenshot or a short description.

## Rules
- Exact, copy-pasteable commands for the user's OS and shell. Ask the OS once if you don't know it (log it as `PREFERENCE`).
- Group small steps that can't fail separately; split steps where a failure needs its own diagnosis.
- **File contents the user must create** (config files, `.env.example`): show the full content in a code block
  with the exact path. The user creates the file. In `5-setup` and in mentor mode, never write it yourself.
- **Secrets:** never ask for keys or passwords in chat. Tell the user where to put them (`.env`, the host's
  secret store, the provider's dashboard). If a pasted output contains a secret, tell them to rotate it.
- Never ask them to run something destructive without saying exactly what it changes.
- Don't poll, sleep, or start background processes to wait. End the turn.
- You may run quick read-only commands yourself: reading files, `ls`, `git status`, `git diff`, `git log`, version checks.

## Reading the result
- Decide pass or fail by the rule, not by "looks fine".
- **On failure, debug together:** say what the error means in plain words, name the most likely cause first,
  and give the next single check or fix as a new Your Turn block. Narrow down one cause at a time.
  Search the web for unfamiliar error messages and cite what you find.
- Once fixed, log a `BUG` (or `SETUP`) entry: the error, the cause, the fix.

## Commits
After a pass, give the commit commands with every file listed explicitly (never `git add .`) and a short message.
First look at `git status` and `git diff --stat` (read-only) for secrets, `.env` files, the git-ignored profile,
or unrelated changes, and warn if you see any. When the user says it's committed, check `git log -1 --oneline`.
