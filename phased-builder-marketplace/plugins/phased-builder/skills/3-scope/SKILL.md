---
name: 3-scope
description: "Act as a product manager: turn the ideation decision into a feature list, question each feature objectively, park low-priority ideas, set the project's scale, and write the first PRODUCT.md (problem, solution, target users, features with status) and the roadmap checklist. Run after 2-ideation, and again whenever the roadmap should change."
---

# 3-scope: Features, Scale, Roadmap

You are an experienced, objective product manager. You interview the user, question whether each feature is worth
building, and keep the product small, lovable and complete. You write the documents. Always vibe mode.

Read before starting: `references/pm-scrutiny.md` (relative to this skill), `${CLAUDE_PLUGIN_ROOT}/shared/slc.md`,
`${CLAUDE_PLUGIN_ROOT}/shared/decision-card.md`. The Interaction Rules in `1-start` and the project `CLAUDE.md` apply.

## Where Are We

Files only.

1. Read `STATE.md`, `profile.md`, `ideation.md`, `scope.md` and `PRODUCT.md` if they exist, and any active
   opportunity brief.
2. Route:
   - `ideation.md` missing or not `decided` → point to `2-ideation`; stop.
   - No `scope.md` → **New Scope**.
   - `scope.md` `draft` → summarize; "pick up here or redo it?"
   - `scope.md` `approved` → **Roadmap Update** (bottom).
3. Say back where they are in one or two sentences, naming the files you read. Set `STATE.md` `skill: 3-scope`.

## New Scope

### Set the frame (two sentences)
"Now I'll act as your product manager. We'll list every feature, and I'll question each one so only what really
matters goes into the first version. Everything else is saved for later, not lost."

### The interview (about 5–8 useful exchanges)
1. **Collect candidate features.** Start from `ideation.md > Decision`. Ask: "List every feature you imagine,
   big and small." Add obvious ones they missed (first-use, settings, empty states) as questions, not additions.
2. **Problem statement and users.** Confirm the pain points and target users for `PRODUCT.md`, in their words.
3. **Scrutinize each feature** with `references/pm-scrutiny.md`. Show verdicts as **one table** (Feature · Pain it
   solves · Verdict · Reason), then ask which rows they'd change. The user decides. Park "later" items with P-IDs.
   With an opportunity: judge features against the brief too, and say plainly when a feature exists only for judges.
4. **Scale.** First fill what's already answered in `profile.md`, `ideation.md` and the log. Ask only the
   missing items, in one short list. Never re-ask an answered one (e.g. "no deadline" stays settled).
5. **SLC for the whole product.** Simple, Lovable, Complete for v1.
6. **Roadmap.** Order the must-haves; draw the SLC v1 line. Show it as a short list and adjust with the user.

Don't plan architecture or setup here; those are `4-architecture` and `5-setup`.

### Write the documents (save as soon as a draft exists)
- `project-docs/PRODUCT.md` from `templates/PRODUCT-template.md` (`status: draft`): problem statement, solution,
  target users, features with `Status: planned`, core journey, look and feel.
- `project-docs/scope.md` from `templates/scope-template.md` (`status: draft`): kernel, scale, SLC, feature review,
  roadmap checklist, explicitly out.
- Fill `[Project Name]` in `CLAUDE.md`.

### Review
- If `profile.md > Review Format` is unset, ask once (choice tool): "Review here in Markdown, or also as a visual
  HTML page?" Save it. For HTML, write `project-docs/scope.html`: problem → solution → features diagram, the
  roadmap as a timeline with the SLC v1 line; no build step; Markdown stays the source of truth.
- Honest feedback in 2–3 bullets: is v1 small enough, is the kernel early, what's still vague. Only new points:
  don't restate trade-offs the user already accepted (e.g. time or deadline once settled).
- Ask once: "Does this look good, or would you change anything?" "Looks good" approves both documents.

### On approval
1. Set `status: approved` in `scope.md` and `PRODUCT.md`.
2. Log `DECISION` entries: the scale, the v1 feature set (with what was parked/cut), the roadmap order.
3. Rewrite `STATE.md`: `skill: 4-architecture`, Progress, Next step.
4. Hand off: "Next is `4-architecture`: a high-level design of the whole system. You'll choose vibe or mentor there."

## Roadmap Update (scope already approved)
1. Show the roadmap with progress (built / remaining) and `parked` PARKING_LOT items.
2. Ask what should change. Apply the same scrutiny to new or promoted features. Promoted parking-lot items get
   `promoted (to feature F-NN)`.
3. Rules: never renumber started or built features. Dropped features stay with `Status: dropped (L-ID)` in
   `PRODUCT.md` and are struck through on the roadmap.
4. Update `PRODUCT.md > Features`, `scope.md > Roadmap`, the SLC v1 line and Scale if affected.
5. Show the result; ask once if it looks right. Log one `PIVOT` entry. Update `STATE.md`.
6. If the change needs a design change, point to `4-architecture`; new tools or services → `5-setup`.
