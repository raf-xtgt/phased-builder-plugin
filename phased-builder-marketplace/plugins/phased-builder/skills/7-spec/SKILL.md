---
name: 7-spec
description: "Plan how the current feature is built: components, data, wiring blueprint, verification plan, setup needed, and changes to the architecture. Vibe (agent proposes) or mentor (user proposes; agent coaches system design). The agent writes spec.md in both modes. With an opportunity, designs the feature for maximum impact. Run after 6-prd."
---

# 7-spec: Blueprint the Feature

You are a senior engineer. Turn the approved PRD into a blueprint `8-build` can follow. You always write the spec;
the mode decides who leads the design thinking.

Read before starting: `references/spec-patterns.md` (relative to this skill), `${CLAUDE_PLUGIN_ROOT}/shared/mode-choice.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/design-patterns.md`, `${CLAUDE_PLUGIN_ROOT}/shared/decision-card.md`; in mentor mode also
`${CLAUDE_PLUGIN_ROOT}/shared/system-design-mentor.md`; with an active opportunity also
`${CLAUDE_PLUGIN_ROOT}/shared/opportunity-impact.md`. The Interaction Rules in `1-start` and the project `CLAUDE.md` apply.

## Where Are We

Files only.

1. Read `STATE.md` and the current feature folder.
2. Route:
   - No feature in progress → point to `6-prd`; stop.
   - The feature's `prd.md` isn't `approved` → `6-prd`; stop.
   - `spec.md` `draft` → summarize; "pick up here or redo it?" (keep its recorded mode unless they want to change).
   - `spec.md` `approved` → point to `8-build`; stop, unless they want to reopen it (log a `PIVOT`).
3. Say back where they are in one or two sentences, naming the files you read.
4. **Choose the mode** (`shared/mode-choice.md`) for a new spec. `STATE.md`: `skill: 7-spec`, `mode`.

## Before You Start
Read the feature's `prd.md`, `ARCHITECTURE.md`, `scope.md > Scale`, `profile.md` (experience, learning goals), the
last ~5 log entries, and any active opportunity brief.

## Set the Frame
- Vibe: "I'll propose how to build this feature, area by area, with what's standard at your scale. You decide; I write it up."
- Mentor: "You lead the design. For each area I'll ask how you'd do it, then challenge it and explain the standard
  approach and trade-offs. You decide; I write it up."

## The Session
Aim for the areas this feature actually needs; usually 5–8 useful exchanges.
1. **Fit with the architecture:** which components and data this feature touches; small fit or architecture change
   (`references/spec-patterns.md`).
2. **Walk each PRD behavior into the system,** anchored on PRD headings ("In `prd.md > Setting the timer`, where does
   the chosen duration live, and what happens if the app is closed?").
3. **Consequential choices** with decision cards (vibe) or the mentor loop (mentor): data, new libraries, services,
   AI calls, cost.
4. **Opportunity impact** (if a brief is active): `shared/opportunity-impact.md` for this feature. In mentor mode, ask
   the user for impact ideas first.
5. **Trace the journey** through the pieces; derive file changes. Diagram if it helps.
6. **Code-level research** for this feature (`references/spec-patterns.md`): API reference, wiring, known issues.
   Then the **wiring blueprint:** build order, connections, which framework feature does each job (doc links),
   standard patterns, common mistakes.
7. **Verification plan:** for each acceptance criterion, what the user runs and what passing looks like.
8. **Setup needed:** new tools, libraries, configs, cloud services.
9. **One useful unknown:** a real uncertainty the user has, clarified or planned as a small check. Don't invent one.

Log each `DECISION` when it's made. New ideas → PARKING_LOT.

## Write `features/NN-name/spec.md`
From `templates/spec-template.md`, `status: draft`, `mode:` set. Cite `ARCHITECTURE.md` and PRD headings. Doc links for
every dependency. Save immediately. Self-review (`shared/design-patterns.md`).

## The Review
- Review Format: Markdown, or optional HTML `spec.html` (data-flow diagram, component reveals); Markdown canonical.
- Honest feedback in 2–3 bullets: every PRD behavior has a home, right size, verification realistic, anything
  unverified. New points only.
- Ask once: "Does this look good, or would you change anything?" "Looks good" approves it.
  In mentor mode, end with one sentence naming the design idea from this session most worth remembering.

## On Approval
1. `status: approved`.
2. If **Setup Needed** has items: add them to `ARCHITECTURE.md > Setup Needs` and point to `5-setup` first.
   A big architecture change: suggest `4-architecture` (refine) first. Small changes are merged into
   `ARCHITECTURE.md` when `8-build` closes the feature.
3. `STATE.md`: `skill: 8-build` (or `5-setup`), `mode: vibe`, Now, Next step.
4. Hand off: "Next is `8-build`. You'll choose vibe (I write the code) or mentor (you write it) there." A fresh
   conversation is recommended; the files carry everything.
