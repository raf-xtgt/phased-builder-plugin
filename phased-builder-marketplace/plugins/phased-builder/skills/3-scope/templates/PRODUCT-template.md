---
doc: product
status: draft                # draft until 3-scope is approved, then approved
---
<!-- MASTER DOC: what the product is and which features it has.
     Written first by `3-scope`. Feature status is updated by `6-prd` (in progress) and `8-build` (built).
     A built feature's section describes what was actually built, not the plan.
     Keep heading names stable: feature PRDs and specs cite them. -->

# [Project Name]

One line: what it is and who it's for.

## Problem Statement
The pain points, in the users' terms. What they do today instead, and why that hurts.
- **[Pain point]:** [what happens, how often, how bad].

## Solution
How the product solves those pains, in a few sentences. The kernel: the one distinctive thing
(see `scope.md > The Unique Kernel`).

## Target Users
Specific people you can picture. For each: who they are, what they're trying to do, where they are.

## Features
<!-- One heading per feature, in roadmap order. Status: planned | in progress | built | dropped (L-ID).
     Planned features: 2–4 lines of intent. Built features: what the user can do and see, as built. -->

### F-01 [Feature name]
- **Status:** planned
- **Solves:** [pain point]
- **What it does:** [2–4 lines]
- **Feature folder:** (set when work starts) `features/01-[name]/`

## Core Journey
The main path through the product, numbered. Mark steps that aren't built yet as (planned).

## Look and Feel
Visual and tone direction for the whole product.

## Known Limits
What the product deliberately does not do yet. Link to PARKING_LOT entries where relevant.
