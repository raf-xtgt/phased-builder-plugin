---
doc: setup
run: NN-short-name
status: planned              # planned | in-progress | done
os: [user's OS and shell]
---
<!-- One setup run, in project-docs/setup/NN-short-name.md. The user does every step; the agent gives the
     steps and debugs. Each step is ticked only after the user's output passes. Never write secret values here. -->

# Setup NN: [Name]

Why: [main setup / new library for F-03 / new cloud service ...]. From `ARCHITECTURE.md > Setup Needs`: [items].

## Decisions
- **[Decision]:** [choice] (L-ID). Standard at our scale: [one line].

## Accounts the User Creates
- [Service]: what for, free tier limits, region notes. (User signs up; never share passwords in chat.)

## Steps
<!-- Fixed fields per step, in this order. Small steps: a failure should point to one cause. -->

- [ ] **1. [Step title]**
  Do: [commands, or UI steps: where to click, what to enter]
  Files you create: [path + full content shown in chat, or "none"]
  Expect: [what the output or screen shows]
  Pass when: [the rule]
  Result: [filled after: pass / issue L-ID]

## The Proof It Works
- [ ] [The final check, e.g. "`flutter run -d chrome` shows the starter page" or "the deployed URL returns the
  hello page"]: exact commands and expected output.

## Issues Hit
<!-- One line each, with the BUG/SETUP L-ID that has the details. -->

## Updates Made to ARCHITECTURE.md
- [ ] Setup Needs ticked
- [ ] Environment and Tooling / How to Run Locally / How to Test / Deployment updated with what actually worked
