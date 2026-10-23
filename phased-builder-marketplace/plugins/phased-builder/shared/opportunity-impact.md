# Designing for Opportunity Impact: Agent Reference

Used by `4-architecture` (whole system) and `7-spec` (one feature) when an active brief exists in
`project-docs/opportunities/<name>/brief.md` (status not `done` or `dropped`). Skip it when there is none.

Goal: make the design have the most impact for the opportunity **without bending the product away from its
kernel or its users.**

## 1. Re-read the brief
Judging criteria and weights, required or sponsor technologies, the depth-check table, submission needs
(demo video, live URL, repo), deadline. If `checked:` is more than a few days old and the deadline is near,
re-verify the key facts (search, cite).

## 2. Map the design to what's rewarded
For the whole system (architecture) or this feature (spec):
- **Criteria hit:** which judging criteria this design serves, and how a judge would *see* it.
- **Required tech placement:** where each required/sponsor technology sits in the design. Is it on the critical
  path of the product's main value, or bolted on at the edge?
- **Depth check:** for each technology, "could a traditional approach do this job just as well?" Use the
  verdicts in the brief; for a new use, run the check now (shallow / deep, with the traditional alternative
  compared). For shallow uses, give the three choices: find a deeper use case, change the design so the tech is
  essential, or accept it as shallow knowingly. The user decides; log it.
- **Demo moment:** the one moment in a short demo where this design shows its value. Design so that moment is
  reliable (fast, no flaky external call at the wrong time, sample data ready).
- **Visible quality:** what judges usually notice (working end to end, speed, polish of the main flow) vs what
  they rarely see (internal refactors). Spend effort where it shows, unless it's needed for correctness or safety.

## 3. Ideate (in mentor mode, ask the user first)
Offer 2–3 ways to raise impact, each with its cost and risk, e.g.:
- moving a sponsor technology from a side feature into the core loop;
- a design that makes the kernel visible in the first 10 seconds of use;
- a fallback that keeps the demo working if an external API is slow or down.
Use a decision card. The user chooses.

## 4. Guard the product
State plainly if an impact idea:
- moves the product away from `scope.md > The Unique Kernel` or its target users;
- adds cost or lock-in that outlives the opportunity (paid tiers, vendor-specific data formats);
- creates work that's thrown away after the deadline.
Record accepted trade-offs in the document's **Opportunity Impact** section with L-IDs.
