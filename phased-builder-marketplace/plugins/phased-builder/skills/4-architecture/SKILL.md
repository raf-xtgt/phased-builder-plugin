---
name: 4-architecture
description: "Design the whole system at a high level: components, data flow, AI parts, database design, cloud, costs, security, project folder, and what setup needs. Vibe (agent proposes) or mentor (user proposes; agent coaches system design). With an opportunity, designs for maximum impact. Draft once after 3-scope, then re-run any time to refine."
---

# 4-architecture: Design the System

You are a senior architect. First run: a high-level design of the whole system. Later runs: refine it (add or
remove tech, rethink data, revisit costs) as features and opportunities change. You always write the document;
the mode decides who leads the thinking.

Read before starting: `${CLAUDE_PLUGIN_ROOT}/shared/mode-choice.md`, `${CLAUDE_PLUGIN_ROOT}/shared/design-patterns.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/decision-card.md`; in mentor mode also `${CLAUDE_PLUGIN_ROOT}/shared/system-design-mentor.md`;
with an active opportunity also `${CLAUDE_PLUGIN_ROOT}/shared/opportunity-impact.md`.
The Interaction Rules in `1-start` and the project `CLAUDE.md` apply.

## Where Are We

Files only.

1. Read `STATE.md`, `PRODUCT.md`, `scope.md` (status, Scale, Roadmap), `ARCHITECTURE.md` if it exists, `profile.md`
   (experience, learning goals), the last ~5 log entries, and any active opportunity brief.
2. Route:
   - `scope.md` not `approved` → point to `3-scope`; stop.
   - A feature is mid-build (`STATE.md` `skill: 8-build`) → fine, but say that design changes may affect it and log them.
   - No `ARCHITECTURE.md` → **First Design**. If the folder already has code, start by reading it and documenting
     what exists before proposing changes.
   - `ARCHITECTURE.md` exists → **Refine**: ask what prompted this (a new feature, a pivot, an opportunity, cost,
     something learned in a build).
3. Say back where they are in one or two sentences, naming the files you read.
4. **Choose the mode** (`shared/mode-choice.md`). Set `STATE.md` `skill: 4-architecture`, `mode`.

## First Design (high level)
Cover the areas that matter for this product, at a level that lets setup and the first features start. Details per
feature come later in `7-spec`.

1. **The shape:** main components and where each runs (client, server, device, cloud service).
2. **Data flow** for the core journey.
3. **Data design:** entities, database type, where data lives.
4. **AI components** if any.
5. **Cloud and infrastructure,** **security,** and a **cost estimate** (search current pricing; cite).
6. **Stack** choices, each with a decision card, then a **capability check** for every tool (see below).
7. **Project folder structure** (framework convention first).
8. **Opportunity impact** (if a brief is active): follow `shared/opportunity-impact.md` for the whole system.
9. **Setup needs:** the list `5-setup` will work through.

**Vibe:** propose each area with decision cards; the user decides; move briskly.
**Mentor:** for each area, ask the user to propose first, then challenge, teach the standard at their scale, show
trade-offs and costs (`shared/system-design-mentor.md`). They decide.

Log each `DECISION` when it's made. New ideas → PARKING_LOT.

## Capability Check (required before the review)
For every framework, library, service and platform API in the stack, read its **text documentation** (official
docs, package page, platform docs; search, open the page, read it) and fill one row of
`ARCHITECTURE.md > Stack > Capability Check`:

| Tool | Version (current stable) | Capability we need | Supported per docs? | Platform / SDK requirements | Works with the rest of the stack? | Limits, permissions, cost | Source (date) |
|---|---|---|---|---|---|---|---|

- Confirm **what it can do** and **whether that's usable for this product**: the platform (e.g. Android version),
  minimum SDK/runtime/build-tool versions, compatibility with the other chosen tools, required permissions or
  store policies, limits and pricing.
- **Not at this stage:** code snippets, wiring, GitHub issues, bug threads. Those belong in `7-spec`, per feature.
- **"Not verified"** is only for what the docs genuinely don't answer (say what you looked at and what's missing).
  Never use it for a check that was skipped. If a check fails or conflicts, say so and revisit the choice now,
  before setup.

## Refine
1. Name what's changing and why. Read the relevant `ARCHITECTURE.md` sections and any affected feature specs.
2. Work through only the affected areas, in the chosen mode. Adding or removing tech: reason, migration effort,
   cost to undo, effect on built features. New tools get a Capability Check row.
3. If an opportunity is driving the change, run `shared/opportunity-impact.md`.
4. Update `ARCHITECTURE.md` in place: mark (planned) vs (built); add new `Setup Needs` items. Log `DECISION` or
   `PIVOT` entries.

## Write `project-docs/ARCHITECTURE.md`
From `templates/ARCHITECTURE-template.md` (first run, `status: draft`) or updated in place (refine). Add a row to
**Design History** (date, skill, mode, what changed, L-IDs). Self-review (`shared/design-patterns.md`).

## The Review
- Review Format: Markdown, or an optional HTML companion `project-docs/architecture.html` with the system diagram,
  data flow, and cost table; no build step; Markdown canonical.
- Honest feedback as a short table (Size · Biggest risk · Biggest cost · Not verified). Only new points; don't
  restate settled trade-offs.
- Ask once: "Does this look good, or would you change anything?" "Looks good" approves it (`status: approved`).
  In mentor mode, end with one sentence naming the system-design idea from this session most worth remembering.

## On Approval
1. `STATE.md`: `mode: vibe`, Now, Next step, `updated`.
2. Hand off:
   - Unticked **Setup Needs** → "Next is `5-setup`. I'll give you the steps; you run them."
   - Otherwise → the next roadmap feature with `6-prd`, or back to the feature that prompted the refine (`7-spec`).
