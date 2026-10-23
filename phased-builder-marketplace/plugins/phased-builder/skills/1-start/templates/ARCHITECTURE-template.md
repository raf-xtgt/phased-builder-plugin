---
doc: architecture
last_merged_phase: none
---
<!-- MASTER DOC: the system AS IT IS TODAY. Updated at the end of every phase (setup and build)
     from that phase's spec.md and what was actually built. Keep headings stable: phase specs cite them.
     If code and this doc disagree, say so and fix the doc in the merge step. -->

# [Project Name]: Architecture

## How It Works, In Plain Language
The pieces and what each does, in the user's vocabulary.

## Stack
Language, framework, key libraries, versions, doc link for each. One line of reason each (cite BUILD_LOG ID).

## Environment and Tooling
Runtime versions, package manager, linters/formatters, test runner, env vars (names only, never values).

## How to Run Locally
Exact commands, in order, and what you should see.

## How to Test
Exact commands and what passing looks like.

## Deployment
Where it runs, how to deploy, how to roll back, accounts and services used. Cost notes.

## Components
### [Component]
What it does, what it talks to, which PRODUCT.md feature it serves.

## Data Model
What data exists, where it lives, how it changes.

## External Services
Each: purpose, docs link, keys needed (names only), limits, cost.

## File Structure
Annotated tree of the real folders.

## Known Risks and Tech Debt
Each with a BUILD_LOG or PARKING_LOT reference.
