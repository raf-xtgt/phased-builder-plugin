---
doc: prd
phase: NN-build-name
status: draft
---
<!-- `status`: draft when first saved; approved when the user clearly approves ("looks good" counts).
     One build phase = one complete feature. This PRD describes only what THIS phase adds or changes.
     The whole product as it is today lives in PRODUCT.md; cite its headings.
     Keep heading names stable: spec.md and checklist.md cite them. Drop sections that don't apply. -->

# [Feature Name]: Phase NN Product Requirements

One line: what this phase adds and for whom.
Builds on: `PRODUCT.md > [heading]`. Roadmap row: `scope.md > Roadmap` phase NN.

## The Journey
The complete path through this feature, numbered, from where the user starts to the moment it's done.

## Screens and Layout
Surfaces this phase adds or changes, and how the user moves between them. For non-visual tools,
the interaction surface. Nothing invented.

## Look and Feel
Direction for this feature, carried from `PRODUCT.md > Look and Feel`. Only what's new or different.

## Features and Behavior
### [Behavior]
What the user can do and see.
- [ ] Acceptance criterion: observable on screen, in output, or in a file.

## States and Boundaries
Only those that apply: first use, empty, error, success, what persists, who can see or do what.

## SLC Check
<!-- See shared/slc.md. All three must pass before approval. -->
- **Simple:** the one job is ___.
- **Lovable:** the specific thing that makes it nice is ___. We'll see it when ___.
- **Complete:** a user goes from ___ to ___ with no dead ends; every visible control works; states handled: ___.

## Product Decisions
- [Choice] (L-ID): [reason]. Mark assumptions as assumptions.

## What This Phase Builds
The full list. If it isn't here, it isn't built in this phase.

## Parked During This Phase
P-IDs of ideas moved to PARKING_LOT.md while planning. Nothing here appears in the product.

## Changes to PRODUCT.md (for the merge step)
Which master headings this phase adds or changes once it's built.

## Open Questions
Each: must answer before `4-spec`, or can wait.
