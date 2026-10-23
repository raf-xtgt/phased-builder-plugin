# Design Patterns and Sizing: Agent Reference

Shared by `4-architecture` (whole system) and `7-spec` (one feature), in both modes. In mentor mode, also follow
`shared/system-design-mentor.md`.

## Help the user choose
Start from `PRODUCT.md`, `ARCHITECTURE.md` (what's decided or built), `scope.md > Scale`, and the profile. Ask for
their technical direction before offering options. Use a decision card (`shared/decision-card.md`) for each
consequential choice. Honor choices already in `ARCHITECTURE.md`; reopening one is a `PIVOT` and needs a reason.
A learning goal is a legitimate reason to pick a tool; make room for it by reducing other complexity.

## Size it to the scale (not a score)
Weigh: the user's experience; the number of separate services (each adds an account, a key, a failure mode, maybe
a bill); auth and payments (use well-known providers unless there's a reason not to); real-time and background
work; AI calls (cost and latency per call); deployment difficulty and cost; region availability.

- **Too big** for the scale: microservices for a solo app, Kubernetes for 100 users, six tables for a single-user
  tool, three paid services before the first feature works, a vector database for a few hundred records.
- **Too small**: no real auth on a product holding personal data, secrets in client code, no backups for data users
  can't recreate, no migrations once real users exist, AI keys shipped inside a mobile app.

## Simpler options to offer (the user decides)
| Heavy | Simpler option that keeps the idea |
|---|---|
| Custom auth | A managed auth provider, or magic links |
| Multi-user real-time sync | Refresh-based updates; real-time later |
| Self-managed database server | A managed database free tier, or SQLite / on-device storage at small scale |
| Background jobs and queues | Do the work on request; queue later |
| Custom file storage | Managed object storage, or links |
| In-house payments | A hosted checkout page |
| Email / SMS / push | On-screen notices first |
| Search infrastructure | Database text search at small scale |
| Custom ML model | A hosted model API, or rules first |
Never fake the product's kernel to save effort.

## Explaining without jargon
- Walk one real action through the system: "You press Start. The app saves the end time on the phone. When you
  reopen it, it reads that time and redraws the sand." Same design, now they can repeat it.
- Analogies that hold: a database is a spreadsheet the program reads and writes; an API is a form you submit to
  someone else's building; a server is a computer that's always on, waiting to be asked; a framework is a pile of
  decisions already made for you.
- Name a thing, then use the name. No pseudo-explaining: fluent jargon that transfers nothing is worse than silence.

## Diagrams
ASCII or Mermaid, tied to this project's real behavior. Mermaid in the docs, with an ASCII fallback for anything critical.

## Data
For every piece of data: where it lives, how it changes, what happens when the user leaves and comes back, offline,
or on another device. Once real users exist, every schema change needs a migration plan.

## External services and AI
Exact calls (endpoint, input, output, auth), docs link, limits, cost. Search for current details and cite; if you
can't verify, say so and add it to Open Issues to check early. Keep keys server-side.

## Cost
Rough monthly cost at launch and at the 12-month user number. Search current pricing; cite with date. Call out the
biggest line (often AI calls or bandwidth) and the free-tier cliff.

## Self-review before showing a design
Every feature it must serve has a home; no contradictions between components, data and folders; size fits the
scale; failure points have fallbacks; costs are sourced; every cited heading exists. Fix internal issues yourself;
ask the user only about consequential gaps.
