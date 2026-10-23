---
name: 10-opportunity
description: "Research an opportunity and use it as a launchpad: a hackathon (any organizer), an incubator or accelerator, an investor pitch, or a social launch on X, Discord and LinkedIn. Verifies it's open now, checks eligibility first, runs a depth check on required tech, maps gaps to features and design changes, and drafts materials. Run any time, or at the very beginning when an opportunity drives the project."
---

# 10-opportunity: Research and Use an Opportunity

You are a researcher and strategist. Find out what the opportunity really requires, check whether the user can take
part, compare it with the project, and propose the smallest changes with the most impact. The user decides.
Always vibe mode.

Read before starting: `references/research-rules.md` (relative to this skill), then the reference for the type.
The Interaction Rules in `1-start` and the project `CLAUDE.md` apply.

| Type | Reference |
|---|---|
| Hackathon (any organizer) | `references/hackathon-research.md` |
| Incubator, accelerator, grant, startup competition | `references/incubators.md` |
| Investor (VC, angel) pitch | `references/pitch-vc.md` |
| Social launch: X, Discord, LinkedIn | `references/social-launch.md` |

## How the brief is used later
The brief in `project-docs/opportunities/<name>/brief.md` is read by:
- `2-ideation` (fit of each direction), `3-scope` (judging features against it),
- `4-architecture` and `7-spec` (designing for maximum impact: `shared/opportunity-impact.md`),
- `9-ship` (submission assets).
So write it clearly: criteria, required tech with depth verdicts, submission needs, deadline.

## Where Are We

Files only.

1. Read `STATE.md`, `profile.md`, and whatever exists of `ideation.md`, `PRODUCT.md`, `scope.md`, `ARCHITECTURE.md`,
   and existing `project-docs/opportunities/*/brief.md`.
2. Route:
   - No `STATE.md` → run `1-start` first (short; sets up the memory files); stop.
   - A brief for this opportunity exists → summarize its status and next actions; continue. If `checked:` is more
     than a few days old, re-verify dates and status first.
   - **Nothing decided yet** (no `ideation.md` decision) → **opportunity-first**: research now; `2-ideation` explores
     with the brief as a constraint.
   - A feature is mid-build → fine to research; don't change that feature's documents. Changes go through the right skill.
3. Say back where they are in one or two sentences, naming the files you read. `STATE.md`: `skill: 10-opportunity`,
   `mode: vibe`.

## Steps
1. **Which opportunity?** Type (choice tool fine) and a name or link. For incubators or investors without names,
   ask what they're looking for.
2. **Create** `project-docs/opportunities/<short-name>/` with `brief.md` (from `templates/brief-template.md`),
   `research.md` (sources with URLs and dates), and `drafts/` when needed.
3. **Research** with the research rules: open now, dates in both time zones, eligibility blockers first,
   legitimacy, terms; then the type-specific checks (for hackathons, the **depth check** on every required technology).
   Write findings to `brief.md` as you go. Cite everything.
4. **Report blockers first.** If something makes it a no-go or risky, lead with it and ask whether to continue.
5. **Fit and gaps.** Compare with `PRODUCT.md` and `ARCHITECTURE.md` (or the idea, if nothing exists). For each gap,
   say where it goes: a new or changed **feature** (`3-scope`), a **design change** (`4-architecture`), new **tools or
   services** (`5-setup`). Time check against the deadline and `scope.md > Scale`. For shallow tech uses, give the
   three choices from the depth check and log the user's decision.
6. **Drafts** (applications, deck outline, Q&A prep, posts, launch plan) per the type's reference, from an interview
   with the user. Ask once whether they want drafts to edit or to write everything themselves. Real facts only.
7. **Record:** an `OPPORTUNITY` log entry (what, key dates, blockers, decision to pursue or not) plus `DECISION` entries
   for depth-check choices; the deadline in `STATE.md > Now`; for opportunity-first, link the brief in
   `profile.md > Initial Idea or Opportunity`.
8. **Hand off:**
   - Opportunity-first → "`2-ideation` explores ideas with this brief as a constraint."
   - Existing project → the first skill the gaps need: `3-scope` (features), `4-architecture` (design), `5-setup` (tools).
   - Nothing to change → the next actions in the brief (apply, post, prepare the pitch).

## Rules
- Never apply, submit, post, message, or pay on the user's behalf. Prepare; they act.
- Never invent traction, users, revenue, partners, or credentials.
- Not legal, tax, or investment advice. Point out terms in plain words; suggest a qualified person for money or equity.
- Keep the product the user's. If the opportunity pulls the project away from its kernel, say so.
