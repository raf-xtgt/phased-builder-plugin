---
doc: scope
status: draft
---
<!-- Written by `3-scope` together with PRODUCT.md. `status`: draft when first saved; approved when the user
     clearly approves ("looks good" counts). After approval, roadmap changes are made by running `3-scope` again
     and are logged as PIVOT entries. What the product IS lives in PRODUCT.md; this file is the plan. -->

# [Project Name]: Scope

Source: `ideation.md > Decision`.

## The Unique Kernel
The one distinctive thing. If it were removed and nobody noticed, it isn't the kernel.

## Scale
<!-- Every "standard practice at our scale" decision card reads this. Ask, don't guess. -->
- **Users:** at first release ___; in 12 months ___ (best guess is fine).
- **Team:** ___ people building it.
- **Budget:** about ___ per month for hosting and services. Free tiers only? yes/no.
- **Platforms:** [web / iOS / Android / desktop / CLI].
- **Where users are:** region(s). **Where the builder is:** country (affects services and payment providers).
- **Data sensitivity:** none / personal data / payments / health / other.
- **Time:** about ___ hours per week. Deadline: none / date (and why).

## What Makes the Whole Product SLC
- **Simple:** the one main job of the product.
- **Lovable:** the specific reason people will want it.
- **Complete:** what "useful on its own" means for v1.

## Opportunity
<!-- Only if an active brief exists. Otherwise delete this section. -->
- Brief: `opportunities/<name>/brief.md`. Deadline: ___.
- How features were judged against it (see Feature Review).
- "Would you build this without the opportunity?" (L-ID from ideation).

## Feature Review
<!-- The product-manager pass. Every candidate feature, with the verdict. -->
| Feature | Pain it solves | Verdict | Reason |
|---|---|---|---|
| [name] | [pain point] | must-have v1 / later (P-ID) / cut | [one line] |

## Roadmap
<!-- The checklist of features, in build order. Ticked when 8-build closes the feature.
     F-numbers never change once a feature has started. Planned items may be reordered.
     Details for each feature live in PRODUCT.md > Features. -->
- [ ] F-01 [Feature name]: [one-line goal]
- [ ] F-02 [Feature name]: [one-line goal]

**SLC v1 line:** after F-__ (the smallest set of features that is useful on its own).
**Progress:** 0 built / N planned.

## Explicitly Out
Things this product will not do, each with a reason. (Ideas for *later* are in PARKING_LOT.md.)
