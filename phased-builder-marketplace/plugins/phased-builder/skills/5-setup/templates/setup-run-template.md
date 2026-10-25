---
doc: setup
run: NN-short-name
status: planned              # planned | in-progress | done
os: [user's OS and shell]
---
<!-- One setup run, in project-docs/setup/NN-short-name.md. The user runs commands and does console steps; the
     agent edits config files and debugs. Each step is ticked only after it passes. Never write secret values here. -->

# Setup NN: [Name]

Why: [main setup / new library for F-03 / new cloud service ...]. From `ARCHITECTURE.md > Setup Needs`: [items].

## Decisions
- **[Decision]:** [choice] (L-ID). Standard at our scale: [one line].

## Accounts the User Creates
- [Service]: what for, free tier limits, region notes. (User signs up; never share passwords in chat.)

## Steps
<!-- Fixed fields per step, in this order. Small steps: a failure should point to one cause.
     Who: user (commands, installs, console clicks) | agent (file edits) | both. -->

- [ ] **1. [Step title]**
  Who: [user | agent | both]
  Agent edits: [files the agent changes, or "none"]
  User does: [commands from `<repo>/`, or UI steps, or "none"]
  Expect: [what the output or screen shows]
  Pass when: [the rule]
  Result: [filled after: pass / issue L-ID]

## The Proof It Works
- [ ] [The final check, e.g. "`flutter run` shows the starter app on the phone" or "the deployed URL returns the
  hello page"]: exact commands and expected output.

## Issues Hit
<!-- One line each, with the BUG/SETUP L-ID that has the details. -->

## Close
- [ ] `ARCHITECTURE.md`: Setup Needs ticked; Environment and Tooling updated with what actually worked
- [ ] `SETUP.md` (parent folder) written or updated
- [ ] `<repo>/SETUP_EXAMPLE.md` written or updated (dummy values only)
- [ ] User committed the repo files (including SETUP_EXAMPLE.md)
