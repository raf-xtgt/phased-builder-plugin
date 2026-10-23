# Starting a Phase: Agent Reference

A phase starts in `3-prd` (build phases) or `4-spec` (setup phases). Do these steps once, at the
start of the phase. If `STATE.md` already shows this phase as current, skip to the skill's own work.

1. **Pick the phase.** Use the first `planned` row in `scope.md > Roadmap`, unless the user names another.
   If the user wants a phase that isn't on the roadmap, send them to `2-scope` roadmap mode first (it's a
   quick step and keeps the roadmap honest).
2. **Check the previous phase is closed.** If a phase is `in-progress` and its checklist's merge items are
   unchecked, say so. Recommend finishing it with `5-build` first. If the user wants to switch anyway,
   log a `PIVOT` entry and leave that phase `in-progress`.
3. **Create the folder** `project-docs/phases/NN-type-name/` (e.g. `03-build-login`), matching the roadmap row.
4. **Choose the mode** (unless the roadmap row already says vibe or mentor and the user confirms it).
   Explain in two lines, then ask (choice tool is fine):
   - **Vibe-code:** I write the code; you review, run the checks I give you, and commit.
   - **Mentor:** you write the code; I give you a blueprint, doc links and reviews, and answer questions.
     I won't write project code. Small general examples only if you ask.
   Use `profile.md > Learning Goals` to say which fits better this time, in one sentence, without pushing.
5. **Record it:**
   - `scope.md > Roadmap`: set Mode and `Status: in-progress`.
   - `STATE.md`: `current_phase`, `phase_type`, `mode`, `step`, Now, Next step, `updated`.
   - `BUILD_LOG.md`: `PHASE` entry "Phase NN-name started · type · mode".
6. **Load context, lightly:** `PRODUCT.md` and `ARCHITECTURE.md` (the master docs, the current truth),
   the last ~5 log entries, and any `parked` PARKING_LOT items related to this phase. Do not read old
   phase folders unless a master doc or log entry points you there.
7. Say back in two or three sentences what this phase is, its mode, and what you read.
