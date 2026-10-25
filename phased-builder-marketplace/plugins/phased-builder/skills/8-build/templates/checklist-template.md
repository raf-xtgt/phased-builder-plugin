---
doc: checklist
feature: F-NN (features/NN-name)
mode: vibe                   # vibe | mentor (chosen when 8-build starts)
status: draft
---
<!-- Progress state for `8-build`. The loop finds the next unchecked `- [ ]` slice, and the field labels
     below are a MACHINE CONTRACT: reproduce them exactly, in this order, for every slice.
       - [ ] **N. Title**  /  Becomes usable:  /  Why now:  /  PRD ref:  /  Spec ref:  /  Build:  /
       You run:  /  Pass when:  /  Try it:  /  Commit:
     A slice is a thin end-to-end piece that makes something usable (never "build the database").
     The examples below show the format only; replace them entirely. -->

# F-NN Build Checklist

Commands run by: user · Commits by: user

## Slices

- [ ] **1. You can type an entry and see it appear in the list**
  Becomes usable: An entry typed into the form shows up in the list. Nothing persists yet.
  Why now: Proves the whole path end to end, so later slices have somewhere to land.
  PRD ref: `prd.md > The Journey` (steps 1–3)
  Spec ref: `spec.md > Components`, `spec.md > Wiring Blueprint`
  Build: Entry form component, in-memory list, render newest first.
  You run: from `<repo>/`: `npm run dev`, then open http://localhost:3000
  Pass when: Server starts with no errors; a submitted entry appears at the top of the list.
  Try it: Add two entries and say whether it looks and feels the way you pictured it.
  Commit: from `<repo>/`: `git add src/components/EntryForm.tsx src/app/page.tsx` then `git commit -m "Add entry form and live list"`

<!-- Continue for as many slices as the feature needs. No target count. -->

## Final Review

<!-- After all slices: the user explores the feature freely and gives feedback. Agreed fixes become
     unchecked items here, each verified (user runs) and committed (user) before ticking. -->

- [ ] User explored the whole feature and gave feedback
- [ ] Agreed fixes done, checked, and committed (or: no changes needed)
- [ ] User confirms the feature is complete (the PRD's SLC check still passes)

## Close the Feature

- [ ] `PRODUCT.md`: this feature's section describes what was actually built; `Status: built`; Core Journey updated
- [ ] `ARCHITECTURE.md` updated from this feature's spec and the actual code (planned → built); Design History row added
- [ ] `scope.md > Roadmap`: this feature ticked; Progress updated
- [ ] `BUILD_LOG.md`: `FEATURE` summary entry written
- [ ] Parking lot items from this feature shown to the user
- [ ] `STATE.md` points to the next step

## Optional: Learning Wrap-Up and App Map

<!-- Offered once at the end of the feature. Declining is fine: tick with "declined". -->
- [ ] Offered; outcome: [done / declined]

## Revisions

<!-- Leave empty at first. When the build finds the plan was wrong, add one bullet:
       - [What changed] — [what the build discovered] (L-ID)
     The full record is the BUILD_LOG entry. -->
