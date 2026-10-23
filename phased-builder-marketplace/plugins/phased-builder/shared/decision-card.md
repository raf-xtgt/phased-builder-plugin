# Decision Cards and Standard Practice: Agent Reference

The user wants to see what is **industry-standard at their scale** before deciding. Use a decision card
for every choice with real consequences: stack, data storage, auth, hosting, project structure, testing
approach, important UX patterns, pricing of services, anything hard to undo.

Don't use a card for routine details that follow from an earlier decision (file names, small refactors).
Make those yourself and say so.

## Format

> **Decision:** [what needs choosing, one line]
>
> **Standard practice at your scale:** [what teams of this size usually do, and why it became standard].
> [Source link + date checked, if it depends on current tools, versions or prices.]
>
> **Other options:**
> - **[Option A]:** [when it's better] / [cost or risk]
> - **[Option B]:** ...
>
> **My recommendation:** [one option], because [reason tied to this project: scale, kernel, learning goal].
>
> **Your call.**

A multiple-choice tool is fine for the answer. Always allow "other".

## "At your scale"

Read `project-docs/scope.md > Scale` first: users now and in 12 months, team size, budget, region,
data sensitivity, deadline. Match the practice to it.

- A solo project with 50 users does not need microservices, Kubernetes, or a multi-region database.
- A product holding payments or health data does need real auth, secrets handling and backups, even when small.
- If the scale is not written down yet, ask for the missing piece before giving the card.

Say plainly when the standard depends on scale: "At 10,000+ users teams usually add X; at your size,
Y is standard and you can move later. Here's what moving would cost."

## Research rules

- **Search the web before claiming anything current:** library versions, whether a library is maintained,
  service prices and free tiers, API limits, deprecations. Cite the source and say when you checked it.
- **Prefer primary sources:** official docs, changelogs, pricing pages.
- **If you can't verify, say so** and add "verify early" to the spec's open issues.
- **Region check:** if a service or payment provider may not be available in the user's country, say so
  at the top, not as a footnote.

## After the decision

Write a `DECISION` entry in `BUILD_LOG.md` right away: what was chosen, the standard practice, options
considered, and "Decided by: user" (or "user accepted agent recommendation"). Then record it in the
document (scope, architecture, PRD or spec) with the log ID.
