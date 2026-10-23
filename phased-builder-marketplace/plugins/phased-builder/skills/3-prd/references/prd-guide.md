# PRD Guide: Agent Reference

For you, not a lesson for the user. Run a product interview at the user's level. They supply intentions
and decisions; you organize them and write the PRD.

## Start from the master doc and scope, not a guessed feature
Read `PRODUCT.md` (what exists), the roadmap row for this phase, `scope.md > The Unique Kernel` and
`> Scale`. Use real headings as question anchors: "In `PRODUCT.md > The Core Journey`, step 3 is [x].
Where does this feature start from there?" Never write a guessed journey and ask for approval; ask the
user to walk it.

## Useful prompts (territory, not a script)
- "What does someone see first in this feature, and how is it arranged?"
- "What happens after that action?"
- "What would you see that proves it worked?"
- "What should someone see before there's any data?"
- "What happens when the input can't be used?"
- "What's still there when they come back tomorrow?"
- "Which part is essential for this to feel complete?"

## Standard practice for product patterns
Many features have well-known patterns: sign-up and password reset, search with filters, onboarding,
notifications, empty states, destructive-action confirmation, pagination vs infinite scroll.
When the user is about to decide one of these, show a short decision card
(`shared/decision-card.md`): what most products at their scale do, 1–2 alternatives, your
recommendation. Product choices stay theirs. Cite well-known guidance (platform design guidelines,
accessibility rules such as WCAG) when it helps.

## Visual direction
For a visual feature, 1–2 questions on look and feel if `PRODUCT.md > Look and Feel` doesn't already
cover it. Explain once that unspecified visuals drift toward generic AI-app styling. Non-visual tools:
output readability and tone only, if useful.

## Implied complexity
Catch hidden infrastructure: "my saved items" may need accounts or just local storage; "share with a
friend" may need links, permissions, or email. Ask what experience they actually need. Make the cost
concrete. Never silently add infrastructure; if it is real infrastructure work, it may belong in a
setup phase (suggest `2-scope` roadmap mode).

## Keep the phase SLC
Every time a requirement grows the phase: "That makes this phase bigger. Does it help this feature feel
complete, or is it a new idea for later?" New ideas → PARKING_LOT with a P-ID. Never "coming soon" stubs.

## Acceptance criteria
Turn the user's evidence of success into observable criteria: what's on screen, in the terminal, in a
file. Cover the happy path and the few empty and error states that matter. No invented performance
numbers, no exhaustive test matrices.

## Decisions and assumptions
Product identity, behavior, priorities and boundaries come from the user. Record their choices under
**Product Decisions** with L-IDs. Mark your own assumptions as assumptions and resolve the important ones
before approval.
