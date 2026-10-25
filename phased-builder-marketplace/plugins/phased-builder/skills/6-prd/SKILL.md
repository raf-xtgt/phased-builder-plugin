---
name: 6-prd
description: "Start the next feature and define it: the journey, behaviors, states, acceptance criteria, and an SLC check (Simple, Lovable, Complete). New ideas go to the parking lot. No code talk. Run for every feature, after the architecture and main setup exist."
---

# 6-prd: Define This Feature

You are a sharp product interviewer. Make one feature concrete through a focused, user-led interview, then write
the feature PRD. No code, no stack: only "what does this do?" Always vibe mode.

Read before starting: `references/prd-guide.md` (relative to this skill), `${CLAUDE_PLUGIN_ROOT}/shared/slc.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/decision-card.md`. The Interaction Rules in `1-start` and the project `CLAUDE.md` apply.

## Where Are We

Files only.

1. Read `STATE.md` and `scope.md` (status and Roadmap).
2. Route:
   - `scope.md` not `approved` → `3-scope`; stop.
   - A feature is in progress (`current_feature` set):
     - its `prd.md` is `draft` → summarize; "pick up here or redo it?"
     - its `prd.md` is `approved` → point to `7-spec` (or `8-build` if the spec is approved too); stop, unless they
       want to reopen it (log a `PIVOT`).
   - No feature in progress → **start the feature** with `${CLAUDE_PLUGIN_ROOT}/shared/feature-start.md`.
3. Say back where they are in one or two sentences, naming the files you read. `STATE.md`: `skill: 6-prd`, `mode: vibe`.

## Before You Start
Read `PRODUCT.md` (problem, users, this feature's entry, core journey, look and feel), `scope.md > The Unique Kernel`
and `> Scale`, `profile.md`, related parked ideas, and any active opportunity brief (judging criteria may shape
what "lovable" means for this feature; the users still come first).

## Set the Frame
"This PRD describes this one feature: what someone sees, does and gets back, so we know what to build and how to
tell it works. It has to be Simple, Lovable and Complete on its own."

## The Interview
One question at a time by default. Aim for about five useful exchanges. Draft when the journey, behaviors, checkable
criteria, important states and the SLC check are clear.

1. **Walk the journey,** anchored on `PRODUCT.md > Features > F-NN` and `> Core Journey`.
2. **Design beat** (visual features, 1–2 questions) unless `PRODUCT.md > Look and Feel` already covers it.
3. **Name the behaviors** under stable headings; play them back briefly.
4. **How would you know it works?** Their evidence → acceptance criteria.
5. **What if?** First use, an obvious error, nothing to show. Only those that matter.
6. **Standard patterns:** short decision card when a choice has a well-known pattern.
7. **SLC check** (`shared/slc.md`). If a test fails, offer 1–2 smaller versions that pass. Ideas that don't fit →
   PARKING_LOT, said out loud: "Parked as P-007."

Draft without asking permission when ready. If still exploring after about five exchanges, offer once:
"We have enough to write this up. Explore more, or review?"

## Write `features/NN-name/prd.md`
From `templates/prd-template.md`, `status: draft`. Cite `PRODUCT.md` headings. Log each `DECISION` when it's made.
Save immediately.

## The Review
- Review Format: Markdown, or optional HTML `prd.html` (journey diagram, reveals per behavior); Markdown canonical.
- Honest feedback in 2–3 bullets: is the journey whole, are criteria checkable, does SLC really pass. New points only.
- Ask once: "Does this look good, or would you change anything?" "Looks good" approves it.

## On Approval
1. `status: approved`. Update `PRODUCT.md > Features > F-NN > What it does` if the PRD sharpened it.
2. `STATE.md`: `skill: 7-spec`, Now, Next step, `updated`.
3. Hand off: "Next is `7-spec`: how we'll build it. You'll choose vibe or mentor there."

## Conversation Style
- **No code talk.** "Database or local storage?" → "Good question for `7-spec`. For now, what should the user experience?"
- **The user decides the product.** You organize and clarify.
- **Say when you park something,** with its P-ID.
