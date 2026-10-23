---
doc: architecture
status: draft                # draft | approved (first approval by 4-architecture; later refinements keep it approved)
---
<!-- MASTER DOC: the system design. Started high-level by `4-architecture`, refined by re-running it and by each
     feature's `7-spec` (merged in `8-build`). `5-setup` fills Environment, How to Run and How to Test with what
     actually worked. Mark anything not built yet as (planned). Keep headings stable: specs cite them. -->

# [Project Name]: Architecture

## How It Works, In Plain Language
The main pieces and what each does, in the user's vocabulary. One real action walked through the system.

## System Diagram
```mermaid
graph LR
  User --> Client --> Server --> Database
```
(ASCII fallback if Mermaid isn't rendered.)

## Components
### [Component]
What it owns, what it talks to, where it runs, which PRODUCT.md features it serves. (planned / built)

## Data Flow
How a request or event moves through the components, for the core journey. Sync vs async. Where validation happens.

## Data Design
Entities and relationships, the database type and why, where each piece of data lives (server, device, cache),
what happens on restart, offline, or a second device. Indexes for the main queries. Migration approach.

## AI Components
<!-- Only if the system uses AI models or agents. -->
Each: purpose, model or service, inputs and outputs, where it runs (keys server-side), cost per call, latency,
fallback when it fails or is slow, how output quality is checked.

## Cloud and Infrastructure
Where each component runs (device, serverless, container, managed service), provider, region, scaling model.

## Cost Estimate
| Item | At launch (/month) | At 12-month users (/month) | Source (date checked) |
|---|---|---|---|
Free-tier limits and what happens when they're hit.

## Security and Privacy
Authentication, authorization, secrets handling, personal data, input validation.

## Stack
Language, framework, key libraries and services, with versions and doc links. One line of reason each (L-ID).

## Project Folder Structure
Annotated tree of the planned (and later, real) folders.

## Opportunity Impact
<!-- Only if an active opportunity brief exists. See shared/opportunity-impact.md. -->
Where the required tech sits, depth-check verdicts and decisions (L-IDs), the demo moment, trade-offs accepted.

## Setup Needs
<!-- What `5-setup` must install or configure. Ticked by 5-setup when done. -->
- [ ] [Tool / service / account / config]: [why]

## Environment and Tooling
<!-- Filled by 5-setup with what actually worked. -->
Runtime versions, package manager, formatter, linter, test runner, env var names (never values).

## How to Run Locally
<!-- Filled by 5-setup. Exact commands and what you should see. -->

## How to Test
<!-- Filled by 5-setup. Exact commands and what passing looks like. -->

## Deployment
Where it runs, how to deploy and roll back. (Filled by 5-setup / 9-ship.)

## Known Risks and Tech Debt
Each with an L-ID or P-ID.

## Design History
| Date | Skill | Mode | What changed | L-IDs |
|---|---|---|---|---|
