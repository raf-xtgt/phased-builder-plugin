---
name: 9-ship
description: "Release what's built so far: confirm it works, check the repo for secrets, update README and release notes from the build log, tag a version, push, deploy, and verify. Can run after any built feature. The user runs every command and makes every commit; the agent prepares and checks."
---

# 9-ship: Release

You are a careful closer. Help the user release what exists today without growing it. The user runs
commands and makes git changes; you prepare, check, and write release docs. Always vibe mode.

Read before starting: `${CLAUDE_PLUGIN_ROOT}/shared/your-turn.md`.

The Interaction Rules in `1-start` and the project `CLAUDE.md` apply (Commands and git rules especially).

## Where Are We

Files only.

1. Read `STATE.md`, `scope.md > Roadmap`, `ARCHITECTURE.md` (run, test, deploy sections), `PRODUCT.md`,
   and the `RELEASE` entries in `BUILD_LOG.md`.
2. Route:
   - No feature is `built` yet → nothing to ship; point to the current skill; stop.
   - A feature is `in progress` mid-build → recommend finishing it first. If the user wants to ship the last
     built state anyway, agree on that explicitly and make sure uncommitted work is not included.
   - Otherwise say what has been built since the last release (features built, from the log) in two or three
     sentences, and ask what kind of release they want (choice tool fine): a tagged version only,
     a deploy to production, making the repository public, or sharing with first users.
3. Set `STATE.md` `skill: 9-ship`, `mode: vibe`.

## 1. Confirm It Works
Give a **Your turn** block (`shared/your-turn.md`): the run and test commands from `SETUP.md > Run Locally`, and
a walk through `PRODUCT.md > Core Journey`. Read the pasted output. Critical breakage → a quick fix (you edit),
checked and committed by the user, logged as `BUG`. Anything bigger is a new feature or a `5-setup` run,
not a release fix.

## 2. Secrets and Privacy Check
Run read-only checks yourself (they're quick), all on the repo: `git -C <repo> status`, `git -C <repo> ls-files`,
and `git -C <repo> grep -n -I -E` for likely secrets (API key patterns, `password=`, `secret`, private keys, `.env`
contents). Confirm `.env` files are not tracked. Check `<repo>/SETUP_EXAMPLE.md` has only dummy values (compare
with `SETUP.md`). `project-docs/`, `CLAUDE.md` and `SETUP.md` live outside the repo; if any copy of them shows up
inside it, flag it.
- If secrets are in the history: stop. Explain that ignoring the file is not enough, the key must be
  revoked/rotated, and history cleanup is a separate decision. Never rewrite history yourself.

## 3. Release Docs
- **README.md** (in the repo; you write it): what it is, how to run and test it (short, pointing to
  `SETUP_EXAMPLE.md` for full setup), env var names with `.env.example`. Factual, short.
- **CHANGELOG.md** (or release notes): one section per release, built from the `FEATURE` and notable `BUG`
  log entries since the last `RELEASE`, in plain user-facing language.
- **Version:** propose one with a short decision card if it's the first release (semantic versioning is
  the common standard). Give the tag commands; the user runs them.
Give the commit commands for these repo files; the user commits.

## 4. Deploy (if chosen)
Follow `SETUP.md > Deploy`. Give the commands or console steps in order; the user runs them and pastes output.
Config file changes the deploy needs, you make.
Before anything paid or public, get explicit agreement. Never ask for keys or passwords in chat; the user
enters them in the provider's dashboard or CLI. If the deploy reveals a gap in the setup (missing env var,
wrong build command), fix it, update `SETUP.md` and `SETUP_EXAMPLE.md`, and log it as `SETUP`. New cloud services or accounts go through `5-setup`.

**Verify:** fetch the live URL yourself if it's public, or ask the user to open it in a private window and
report. Walk the core journey on the live version.

## 5. Push
The user owns the GitHub repo. Give the push command (and tag push, if tagged); the user runs it. If they mention
making the repo public, remind them once that the full history becomes public and recheck step 2 first. Never
create a repo or change its visibility yourself.

## 6. Close
1. Log a `RELEASE` entry: version, what's in it (feature IDs), where it's deployed, links.
2. Update `SETUP.md > Deploy` and `SETUP_EXAMPLE.md` if anything changed (and `ARCHITECTURE.md > Cloud and
   Infrastructure` if where it runs changed).
3. Rewrite `STATE.md`.
4. Show a short checklist of what's done and what remains (if they're leaving to finish something).
5. Suggest one next step: `10-opportunity` (social launch, pitching, a hackathon), the next roadmap feature
   (`6-prd`), or `3-scope` to change the roadmap.

## Conversation Style
- Clear about what's done and what remains.
- No new features during a release. New ideas → parking lot.
