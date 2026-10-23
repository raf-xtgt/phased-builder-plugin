---
doc: spec
phase: NN-setup-name
status: draft
---
<!-- Setup-phase spec: environment, dependencies, tooling, cloud and deployment.
     A setup phase is done only when something RUNS and the user has checked it.
     Drop sections that don't apply; add what the stack needs. Never write secret values here. -->

# [Setup Name]: Phase NN Setup Spec

Roadmap goal: `scope.md > Roadmap` phase NN. Builds on `ARCHITECTURE.md > [headings]` (or "fresh project").

## What We're Setting Up, In Plain Language
What will exist at the end and why each part is needed, in the user's vocabulary.

## Decisions
- **[Decision]:** [choice] (L-ID). Standard at our scale: [one line]. Trade-off accepted: [one line].

## Runtime and Tools
Language/runtime version, package manager, framework, versions pinned how (lockfile, version file). Doc link each.

## Project Structure
Annotated tree of the folders and starter files this phase creates.

## Dependencies
Each package: purpose, version, doc link. Dev-only vs runtime.

## Configuration and Secrets
Env var NAMES and what each is for (values never written here). Where real values live (`.env`, host's
secret store). `.env.example` contents (placeholders only).

## Code Quality and Testing Setup
Formatter, linter, test runner: only what fits the scale (decision card). The one empty or sample test that proves the runner works.

## Cloud and Deployment
<!-- Only if this phase includes it. -->
Provider, region, services, accounts needed, free-tier limits and cost, how deploys happen
(manual command / git push / CI), how to roll back.

## Step-by-Step Setup Order
Ordered steps; each becomes a checklist item with a check the user runs.

## The Proof It Works
The final check that closes this phase, e.g. "`npm run dev` shows the hello page at localhost:3000" or
"the deployed URL returns the hello page". Exact commands and expected output.

## Changes to ARCHITECTURE.md (for the merge step)
Usually: Stack, Environment and Tooling, How to Run Locally, How to Test, Deployment, File Structure.

## Open Issues
Unverified versions, prices, or region availability to check early.
