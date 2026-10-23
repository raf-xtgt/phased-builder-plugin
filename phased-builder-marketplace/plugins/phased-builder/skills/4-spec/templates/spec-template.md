---
doc: spec
phase: NN-build-name
status: draft
---
<!-- Build-phase spec. Describes only what THIS phase adds or changes to the system.
     The current system lives in ARCHITECTURE.md; cite its headings instead of repeating them.
     Anything 5-build will point at needs its own heading. Depth follows real complexity. -->

# [Feature Name]: Phase NN Technical Spec

Implements `phases/NN-build-name/prd.md`. Builds on `ARCHITECTURE.md > [headings]`.

## How This Works, In Plain Language
The new or changed pieces and what each does, in the user's vocabulary. Written so they could explain it aloud.

## The Journey Through the System
The PRD's journey traced through the pieces: "User does X → goes here → this happens → they see Y."

## Decisions
<!-- One line each, with the decision card result. Full card lives in BUILD_LOG. -->
- **[Decision]:** [choice] (L-ID). Standard at our scale: [one line]. Trade-off accepted: [one line].

## Stack Changes
New libraries or services only, with version and doc link. "None" is a fine answer.

## Components
### [Component]
What it does, what it talks to. Implements `prd.md > [heading]`.

## Data Changes
New or changed data: where it lives, how it changes, what happens when the user leaves and returns. Migrations needed.

## Wiring Blueprint
<!-- Especially important in mentor mode: the user builds from this. -->
The order to build things in, and how each piece connects: which file calls which, what data passes
between them, which framework feature does the work (with doc link). Patterns to follow (industry
standard) and common mistakes to avoid. No code.

## File Changes
Annotated tree of files added or changed in this phase.

## External Services and Calls
Each: exact call (endpoint, input, output), docs link, keys needed (names only), limits, cost.

## How We'll Verify
How each acceptance criterion gets checked: the commands the user will run and what passing looks like.
Proportional: don't add a test framework the project doesn't have unless a decision card agreed it.

## Important Failure Modes
The two or three places this will realistically break, each with its fallback.

## Changes to ARCHITECTURE.md (for the merge step)
Which master headings this phase adds or changes.

## Open Issues
Unverified facts to check early, and any remaining questions. One genuine uncertainty the user has about
this approach, and how it'll be clarified (or "none identified").
