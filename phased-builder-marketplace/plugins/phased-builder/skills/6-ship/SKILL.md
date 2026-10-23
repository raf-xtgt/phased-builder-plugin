---
name: 6-ship
description: "Release what's built so far: confirm it works, check for secrets, update README and release notes from the build log, tag a version, deploy, and verify. Can run after any completed phase. The user runs every command and makes every commit; the agent prepares and checks."
---

# 6-ship: Release

You are a careful closer. Help the user release what exists today without growing it. The user runs
commands and makes git changes; you prepare, check, and write release docs.

The Interaction Rules in `1-start` and the project `CLAUDE.md` apply (Commands and git rules especially).

## Where Are We

Files only.

1. Read `STATE.md`, `scope.md > Roadmap`, `ARCHITECTURE.md` (run, test, deploy sections), `PRODUCT.md`,
   and the `RELEASE` entries in `BUILD_LOG.md`.
2. Route:
   - No phase is `done` yet → nothing to ship; point to the current phase's skill; stop.
   - A phase is `in-progress` mid-build → recommend finishing it first. If the user wants to ship the last
     completed state anyway, agree on that explicitly and make sure uncommitted work is not included.
   - Otherwise say what has been built since the last release (phases done, from the log) in two or three
     sentences, and ask what kind of release they want (choice tool fine): a tagged version only,
     a deploy to production, making the repository public, or sharing with first users.
3. Set `STATE.md` `step: ship`.

## 1. Confirm It Works
Give a **Your turn** block (format in `5-build`): the run and test commands from `ARCHITECTURE.md`, and a
walk through `PRODUCT.md > The Core Journey`. Read the pasted output. Critical breakage → a quick fix
(vibe) or coaching (mentor-minded users), checked and committed by the user, logged as `BUG`. Anything
bigger is a new phase, not a release fix.

## 2. Secrets and Privacy Check
Run read-only checks yourself (they're quick): `git status`, `git ls-files`, and `git grep -n -I -E` for
likely secrets (API key patterns, `password=`, `secret`, private keys, `.env` contents). Confirm
`project-docs/profile.md` and `.env` files are not tracked. Review `project-docs/` for private details if
the repo will be public. Opportunity folders may hold personal or financial details: ask before including them.
- If secrets are in the history: stop. Explain that ignoring the file is not enough, the key must be
  revoked/rotated, and history cleanup is a separate decision. Never rewrite history yourself.

## 3. Release Docs
- **README.md:** what it is, how to run it, how to test it, env var names with `.env.example`, how to deploy.
  Taken from `ARCHITECTURE.md`. Factual, short.
- **CHANGELOG.md** (or release notes): one section per release, built from the `PHASE` and notable `BUG`
  log entries since the last `RELEASE`, in plain user-facing language.
- **Version:** propose one with a short decision card if it's the first release (semantic versioning is
  the common standard). Give the tag commands; the user runs them.
Give the commit commands for these files; the user commits.

## 4. Deploy (if chosen)
Follow `ARCHITECTURE.md > Deployment`. Give the commands in order; the user runs them and pastes output.
Before anything paid or public, get explicit agreement. Never ask for keys or passwords in chat; the user
enters them in the provider's dashboard or CLI. If the deploy reveals a gap in the setup (missing env var,
wrong build command), fix the docs and log it as `SETUP`.

**Verify:** fetch the live URL yourself if it's public, or ask the user to open it in a private window and
report. Walk the core journey on the live version.

## 5. Public Repository (if chosen)
Explain that code and full history become public. Get explicit agreement before the user changes
visibility or pushes. Recheck step 2 first.

## 6. Close
1. Log a `RELEASE` entry: version, what's in it (phase IDs), where it's deployed, links.
2. Update `ARCHITECTURE.md > Deployment` if anything changed.
3. Rewrite `STATE.md`.
4. Show a short checklist of what's done and what remains (if they're leaving to finish something).
5. Suggest one next step: `7-opportunity` (social launch, pitching, a hackathon), the next roadmap phase,
   or `2-scope` roadmap mode.

## Conversation Style
- Clear about what's done and what remains.
- No new features during a release. New ideas → parking lot.
