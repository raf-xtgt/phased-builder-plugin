---
doc: scope
status: draft
---
<!-- `status`: draft when first saved; approved when the user clearly approves ("looks good" counts).
     After approval, roadmap changes are made in `2-scope` roadmap mode and logged as PIVOT entries.
     Scope is the vision and the plan of phases, not the detailed feature definition (that's each phase PRD). -->

# [Project Name]

One line: what this is.

## The Unique Kernel
The one distinctive thing that makes this not generic. One or two sentences.

## Who It's For
A specific person you can picture. What they're trying to do, and what they do today instead.

## The Core Loop
What the user does again and again. Why they come back.

## Scale
<!-- Every "standard practice at our scale" decision card reads this. Ask, don't guess. -->
- **Users:** at first release ___; in 12 months ___ (best guess is fine).
- **Team:** ___ people building it.
- **Budget:** about ___ per month for hosting and services. Free tiers only? yes/no.
- **Where users are:** region(s). **Where the builder is:** country (affects which services and payment providers work).
- **Data sensitivity:** none / personal data / payments / health / other. Any legal rules known.
- **Time:** about ___ hours per week. Deadline: none / date (and why).

## Opportunity
<!-- Only if one is driving the project. Otherwise delete this section. -->
- Brief: `opportunities/<name>/brief.md`. Deadline: ___.
- Constraints it adds: required tech, judging criteria, submission needs.
- "Would you still build this without the opportunity?" Answer: ___ (L-ID).

## What Makes the Whole Product SLC
- **Simple:** the one main job of the product.
- **Lovable:** the reason people will want it.
- **Complete:** what "useful on its own" means for v1.

## Inspiration & Identity
References, look, mood, tone. URLs welcome.

## Why This Matters to You
In the user's words.

## Roadmap
<!-- Unlimited phases. Numbers and folder names are set when the phase is planned; planned (not started)
     phases may be reordered and renumbered. Started or done phases are never renumbered.
     Type: setup | build. Mode: vibe | mentor | decide (chosen when the phase starts).
     The "SLC v1 line" marks the smallest set of phases that is useful on its own. -->

| # | Phase | Type | Goal (one line) | Mode | Status |
|---|---|---|---|---|---|
| 01 | setup-foundation | setup | Project runs locally and [deploys], checked by [command] | decide | planned |
| 02 | build-[kernel-feature] | build | [The kernel, SLC] | decide | planned |

**SLC v1 line:** after phase __.

Status values: planned · in-progress · done · dropped (with L-ID).

## Explicitly Out
Things this product will not do, each with a reason. (Ideas for *later* go to PARKING_LOT.md, not here.)
