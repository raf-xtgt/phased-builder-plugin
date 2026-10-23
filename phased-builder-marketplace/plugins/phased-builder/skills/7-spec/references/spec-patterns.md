# Spec Patterns: Agent Reference

Spec-specific guidance for `7-spec`. General design guidance is in `shared/design-patterns.md`; mentor coaching in
`shared/system-design-mentor.md`.

## A spec is a feature-sized slice of the architecture
Start from `ARCHITECTURE.md` and say which parts this feature touches. Don't redesign the system inside a spec.
- **Small fit** (uses existing components and data): spec it directly.
- **Changes the architecture** (new component, new service, new data store, different data model): design it here
  for this feature, record it under **Changes to ARCHITECTURE.md**, and if it's a big change, suggest running
  `4-architecture` (refine) first.
- **Needs new tools, libraries, configs or cloud services:** list them under **Setup Needed**; they go through
  `5-setup` before or during `8-build` (the user installs them).

## The wiring blueprint (critical in mentor-mode builds)
`8-build` may be done by the user in mentor mode, so the blueprint must let them:
- know the build order (thin end-to-end slices, not layers);
- know which file talks to which, and what data passes;
- know which framework feature or library function does each job, with the doc page;
- know the standard pattern for each part and the common mistakes.
No code in the blueprint. Small general examples only if the user asks, in chat.

## Verification plan
The user runs all checks. For each acceptance criterion: the command or manual step, and what passing looks like.
Prefer fast checks. Use the test runner set up in `5-setup`; don't add new testing tools unless a decision card agreed.

## Opportunity impact
If an active brief exists, run `shared/opportunity-impact.md` for this feature: criteria it hits, where the required
tech sits (deep or shallow), the demo moment, a fallback that keeps the demo working, and the product guard.

## Traceability
Every component heading says which PRD heading it implements. Anything `8-build` will point at needs its own heading.
Depth follows the feature's real complexity; empty headings make a spec worse.
