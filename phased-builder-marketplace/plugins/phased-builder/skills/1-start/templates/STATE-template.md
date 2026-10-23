---
doc: state
current_phase: none          # folder name, e.g. 03-build-login, or none
phase_type: none             # setup | build | none
mode: none                   # vibe | mentor | none  (hooks read this)
step: start                  # start | scope | prd | spec | build | review | merge | ship | opportunity
long_commands: user          # user | agent  (who runs installs, builds, tests, servers, deploys)
git: user                    # user | agent  (who runs git add/commit/push)
updated: YYYY-MM-DD
---
<!-- Keep this file SHORT (under ~60 lines). It is loaded at the start of every session.
     Rewrite it (do not append) at the end of every step. Details belong in other files. -->

# Project State

## Now
One or two sentences: what phase and step we are on, and what was just finished.

## Next step
The single next action, and which skill runs it.

## Waiting on
- user: [e.g. run the test command in phases/03-build-login/checklist.md slice 2 and paste output]
- agent: [or nothing]

## Recent decisions
<!-- Last 3–5 only, as pointers. The log is the full record. -->
- L-000: [one line]

## Open questions
- [Question] (raised in L-000 or [file > heading])

## Roadmap at a glance
<!-- Copy of the status column from scope.md > Roadmap. -->
- 01-setup-[name]: planned
