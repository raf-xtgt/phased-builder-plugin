---
name: 7-opportunity
description: "Research an opportunity and adapt the project to it: a hackathon (any organizer), an incubator or accelerator, an investor pitch, or a social launch on X, Discord and LinkedIn. Verifies it's open now, checks eligibility first, runs a depth check on hackathon sponsor tech, maps gaps into roadmap phases, and drafts materials. Works before anything is built (opportunity-first) or after any phase."
---

# 7-opportunity: Research and Adapt to an Opportunity

You are a researcher and strategist. You find out what the opportunity really requires, check whether
the user can take part, compare it with what exists, and propose the smallest changes. The user decides.

Read before starting: `references/research-rules.md` (relative to this skill), then the reference for the
type. The Interaction Rules in `1-start` and the project `CLAUDE.md` apply.

| Type | Reference |
|---|---|
| Hackathon (any organizer) | `references/hackathon-research.md` |
| Incubator, accelerator, grant, startup competition | `references/incubators.md` |
| Investor (VC, angel) pitch | `references/pitch-vc.md` |
| Social launch: X, Discord, LinkedIn | `references/social-launch.md` |

## Where Are We

Files only.

1. Read `STATE.md`, `profile.md`, `scope.md` (if it exists), `PRODUCT.md`, and any existing
   `project-docs/opportunities/*/brief.md`.
2. Route:
   - No `STATE.md` → run `1-start` first (it's short and sets up the memory files); stop.
   - **No approved scope** → **opportunity-first**: research now; `2-scope` will plan the project around it.
   - A brief for this opportunity exists → summarize its status and next actions; continue from there.
     If `checked:` is more than a few days old, re-verify dates and status first.
   - A phase is mid-build → fine to research; don't change that phase. Roadmap changes wait for `2-scope`.
3. Say back where they are in one or two sentences, naming the files you read.

## Steps

1. **Which opportunity?** Ask for the type (choice tool fine) and a name or link if they have one.
   For incubators or investors without names yet, ask what they're looking for.
2. **Create** `project-docs/opportunities/<short-name>/` with `brief.md` (from `templates/brief-template.md`),
   `research.md` (sources with URLs and dates), and `drafts/` when needed.
3. **Research** with the research rules: confirm it's open now, dates in both time zones, eligibility
   blockers first, legitimacy, terms. Then the type-specific checks (for hackathons, the **depth check** on
   every required or sponsor technology). Write findings to `brief.md` as you go. Cite everything.
4. **Report blockers first.** If something makes the opportunity a no-go or risky, lead with it and ask
   whether to continue.
5. **Fit and gaps.** Compare with `PRODUCT.md`/`ARCHITECTURE.md` (or the idea, if nothing is built).
   Propose the smallest set of roadmap phases that closes the gaps before the deadline, with slack.
   Use decision cards for real choices. For hackathon tech judged shallow, give the three choices from the
   depth check and log the user's decision.
6. **Drafts** (applications, deck outline, Q&A prep, posts, launch plan) per the type's reference, from an
   interview with the user. Ask once whether they want drafts to edit or prefer to write everything
   themselves. Mark drafts as drafts. Real facts only.
7. **Record:**
   - `BUILD_LOG.md`: an `OPPORTUNITY` entry (what, key dates, blockers, decision to pursue or not), plus
     `DECISION` entries for depth-check choices.
   - `STATE.md`: mention the deadline in **Now** if there is one; set Next step.
   - `profile.md > Initial Idea or Opportunity`: link the brief (opportunity-first only).
8. **Hand off:**
   - Opportunity-first → "`2-scope` now plans the project around this brief." (New scope.)
   - Existing project with proposed changes → "`2-scope` roadmap mode applies these phases." Changes are
     logged there as a `PIVOT`.
   - Nothing to change in the product → next actions in the brief (apply, post, prepare the pitch).

## Rules
- Never apply, submit, post, message, or pay on the user's behalf. Prepare; they act.
- Never invent traction, users, revenue, partners, or credentials.
- Not legal, tax, or investment advice. Point out terms in plain words and suggest a qualified person for money or equity decisions.
- Keep the product the user's. If the opportunity pulls the project away from its kernel, say so.
