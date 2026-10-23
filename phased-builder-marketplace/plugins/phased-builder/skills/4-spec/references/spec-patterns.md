# Spec Patterns: Agent Reference

Your architecture knowledge base for `4-spec`: how to support informed choices, how to size a design
to the project's real scale, and how to explain it to someone who doesn't have the vocabulary yet.

## Help the user choose
Start from the PRD, `ARCHITECTURE.md` (what exists), `scope.md > Scale`, and the profile. Ask for their
technical direction before offering options. For each consequential choice use a decision card
(`shared/decision-card.md`): standard practice at their scale, 1–2 options, one recommendation, their call.
Honor choices already made in `ARCHITECTURE.md`; reopening one is a `PIVOT` and needs a reason.

A learning goal is a legitimate reason to pick a tool. Make room for it by reducing other complexity.

## The complexity budget (scaled, not a score)
An informal read on whether the design is the right size for this project, this person, and this phase:
- **Their experience:** unfamiliar frameworks add debugging they may not be able to read yet.
- **Number of services:** each adds an account, a key, a failure mode, and maybe a bill.
- **Auth and payments:** necessary for some products, but heavy. Use a well-known provider unless there's a reason not to.
- **Real-time and background work:** sync, websockets, queues, cron. Hard to build, harder to debug.
- **Deployment difficulty and cost:** check free tiers and region availability (search; cite).

Too big for the scale looks like: microservices for a solo app, Kubernetes for 100 users, six tables for a
single-user tool, three paid services before the first feature works.
Too small looks like: no real auth on a product holding personal data, secrets in client code, no backups
for data users can't recreate, no migrations once real users exist.

## Simpler options to offer (not to decide)
Offer these as card options when the design is over budget. Never fake the kernel.

| Heavy | Simpler option that keeps the idea |
|---|---|
| Custom auth | A managed auth provider, or magic links |
| Multi-user real-time sync | Refresh-based updates; real-time later |
| Self-managed database server | Managed database free tier, or SQLite at small scale |
| Background jobs | Do the work on request; queue later |
| Custom file storage | Managed object storage, or links |
| Payments built in-house | A hosted checkout page |
| Email/SMS/push | On-screen notices first |
| Search infrastructure | Database text search at small scale |

## Explaining without jargon
- **Walk one real action through the system.** "You press Save. The text goes to the server function
  `saveEntry`, which writes a row in the `entries` table. Tomorrow the page asks for that table and shows it."
- **Analogies that hold:** a database is a spreadsheet the program reads and writes; an API is a form you
  submit to someone else's building; a server is a computer that's always on, waiting to be asked;
  a framework is a pile of decisions already made for you.
- **Name a thing, then use the name.**
- **No pseudo-explaining:** fluent jargon that transfers nothing is worse than silence.

## The wiring blueprint (critical in mentor mode)
The user may build this phase themselves. The blueprint must let them:
- Know the build order (thin end-to-end slices, not layers).
- Know which file talks to which, and what data passes.
- Know which framework feature or library function does each job, with the doc page.
- Know the standard pattern for each part and the common mistakes.
No code in the blueprint. Small general examples only if the user asks, in chat.

## Diagrams
Use ASCII or Mermaid in conversation and HTML companions. Tie every diagram to this project's real behavior.

## Data
For every piece of data: where does it live, how does it change, what happens when the user leaves and
comes back. Once real users exist, every schema change needs a migration plan.

## External services
Exact calls (endpoint, input, output, auth), docs link, limits, cost. Verify current details with a web
search and cite; if you can't verify, say so and list it under Open Issues to check early.

## Verification plan
The user runs all checks. For each acceptance criterion, write the command or manual step and what
passing looks like. Prefer fast checks. Don't add a test framework, CI, or coverage tools unless a
decision card agreed it for this scale.

## Spec self-review
Before showing it, check: every PRD behavior has a home; no internal contradictions between data,
files and components; complexity fits the scale; failure points have fallbacks; every cited heading exists.
Fix internal issues yourself; ask the user only about consequential gaps.
