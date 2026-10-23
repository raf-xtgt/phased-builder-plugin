---
doc: checklist
phase: NN-type-name
status: draft
---
<!-- Progress state for `5-build`. The loop finds the next unchecked `- [ ]` slice, and the field labels
     below are a MACHINE CONTRACT: reproduce them exactly, in this order, for every slice.
       - [ ] **N. Title**  /  Becomes usable:  /  Why now:  /  PRD ref:  /  Spec ref:  /  Build:  /
       You run:  /  Pass when:  /  Try it:  /  Commit:
     Build phases: a slice is a thin end-to-end piece that makes something usable (never "build the database").
     Setup phases: each slice is one setup step from spec.md > Step-by-Step Setup Order; the last one is
     The Proof It Works. Use `PRD ref: n/a (setup phase)`.
     The examples below show the format only; replace them entirely. -->

# Phase NN Build Checklist

Mode: [vibe | mentor] · Commands run by: user · Commits by: user

## Slices

- [ ] **1. You can type an entry and see it appear in the list**
  Becomes usable: An entry typed into the form shows up in the list. Nothing persists yet.
  Why now: Proves the whole path end to end, so later slices have somewhere to land.
  PRD ref: `prd.md > The Journey` (steps 1–3)
  Spec ref: `spec.md > Components`, `spec.md > Wiring Blueprint`
  Build: Entry form component, in-memory list, render newest first.
  You run: `npm run dev`, then open http://localhost:3000
  Pass when: Server starts with no errors; a submitted entry appears at the top of the list.
  Try it: Add two entries and say whether it looks and feels the way you pictured it.
  Commit: `git add src/components/EntryForm.tsx src/app/page.tsx project-docs/phases/NN-build-name/checklist.md` then `git commit -m "Add entry form and live list"`

<!-- Continue for as many slices as the phase needs. No target count. -->

## Final Review

<!-- After all slices: the user explores the feature freely and gives feedback. Agreed fixes become
     unchecked items here, each verified (user runs) and committed (user) before ticking. -->

- [ ] User explored the whole feature and gave feedback
- [ ] Agreed fixes done, checked, and committed (or: no changes needed)
- [ ] User confirms the phase is complete (build: SLC check still passes; setup: the proof runs)

## Close the Phase

- [ ] `PRODUCT.md` updated from this phase's PRD and what was actually built (build phases only)
- [ ] `ARCHITECTURE.md` updated from this phase's spec and the actual code
- [ ] `scope.md > Roadmap`: this phase marked `done`
- [ ] `BUILD_LOG.md`: `PHASE` summary entry written
- [ ] Parking lot items from this phase shown to the user
- [ ] `STATE.md` points to the next step
- [ ] User committed the doc updates

## Optional: Learning Wrap-Up and App Map

<!-- Offered once at the end of the phase. Declining is fine: tick with "declined". -->
- [ ] Offered; outcome: [done / declined]

## Revisions

<!-- Leave empty at first. When the build finds the plan was wrong, add one bullet:
       - [What changed] — [what the build discovered] (L-ID)
     The full record is the BUILD_LOG entry. -->
