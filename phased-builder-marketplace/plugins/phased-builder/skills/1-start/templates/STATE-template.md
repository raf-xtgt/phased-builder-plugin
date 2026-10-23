---
doc: state
skill: 1-start               # the skill in progress: 1-start ... 10-opportunity
current_feature: none        # feature folder in progress, e.g. 03-sand-animation, or none
mode: vibe                   # vibe | mentor | guide   (hooks read this)
                             #   vibe   = agent may write code and files
                             #   mentor = agent writes only project-docs/ and CLAUDE.md (user writes code)
                             #   guide  = 5-setup: agent writes only project-docs/; user does all setup steps
long_commands: user          # user | agent  (who runs installs, builds, tests, servers, deploys)
git: user                    # user | agent  (who runs git add/commit/push)
updated: YYYY-MM-DD
---
<!-- Keep this file SHORT (under ~60 lines). It is loaded at the start of every session.
     Rewrite it (do not append) at the end of every step. Details belong in other files. -->

# Project State

## Now
One or two sentences: which skill and feature we're on, and what was just finished.

## Next step
The single next action, and which skill runs it.

## Waiting on
- user: [e.g. run step 4 in setup/01-foundation.md and paste the output]
- agent: [or nothing]

## Recent decisions
<!-- Last 3–5 only, as pointers. The log is the full record. -->
- L-000: [one line]

## Open questions
- [Question] (raised in L-000 or [file > heading])

## Progress
<!-- Copied from scope.md > Roadmap: done / remaining. -->
Features: 0 built / 0 planned. Setup runs: 0.
