# Hackathon Research: Agent Reference

For any hackathon (Devpost, MLH, Devfolio, company-run, university, online or in person). Read
`research-rules.md` first.

## 1. Find and record (cite each)
- **Official page** and **rules/terms** (often a separate page or PDF). Read both.
- **Dates:** start, submission deadline, judging, results. Time zone, converted to the user's.
- **Eligibility:** countries, age, students, team size, solo allowed, in person or online.
- **Pre-existing work rule:** can you submit or extend an existing project, or must work start during the
  event? Some require new code written in the event window; some allow extending with a clear record of what's new.
  **This decides whether the user's current project can be used at all.** If unclear, say so and suggest asking the organizers.
- **Required or sponsor technologies:** each API, SDK, platform, or model the hackathon wants used, per track.
  For each: the official docs link, quickstart, pricing/free credits for participants, rate limits, region
  availability, and whether it needs an account or approval (waitlists take time).
- **Tracks and prizes:** what each track rewards. Prize payout conditions and whether payout works in the user's country.
- **Judging criteria** and weights, if published (e.g. technical depth, use of sponsor tech, impact, design, presentation).
- **Submission requirements:** demo video (length limits), public repo, live URL, slides, write-up fields,
  team info. Exact format rules.
- **IP and licensing terms:** who owns the work; any license required for the repo.
- **Communication:** Discord or forum, office hours, mentor sessions.

## 2. Depth check (for every required or sponsor technology)
Ask: **"Could a traditional approach do this job just as well?"**

| Technology | What we'd use it for | Traditional alternative compared | Verdict | Reason |
|---|---|---|---|---|
| [tech] | [feature] | [e.g. plain SQL query, a template, a cron job, a rules engine] | shallow / deep | [one or two lines] |

- **Shallow:** a traditional approach gets the same result just as well (e.g. an LLM call that only
  formats text a template could format; a vector database for 20 records a simple filter handles;
  a blockchain where a normal database works).
- **Deep:** the technology is the best fit and the feature is clearly worse, slower, or impossible without
  it (e.g. understanding free-form user language, semantic search over a large unstructured corpus,
  real-time multiplayer sync the platform provides).

Be honest. Judges often look for "meaningful use" of sponsor technology, and shallow use is easy to spot.

**For each shallow verdict, show the user three choices:**
1. **Find a deeper use case** within the product where the technology is truly needed.
2. **Change the feature** so the technology becomes essential (without twisting the product's kernel).
3. **Accept it as shallow,** knowingly, if the track still rewards it.
The user decides. Log each verdict and decision as a `DECISION` entry.

## 3. Fit and gap
- What already exists (`PRODUCT.md`) that fits a track or the judging criteria.
- What's missing: required tech integrations, features the track rewards, submission assets.
- **Time check:** days left vs. the user's hours per week (`scope.md > Scale`). Propose the smallest set of
  phases that gives a complete, SLC submission before the deadline, with slack. Say plainly if it doesn't fit.
- Typical phases: a **setup** phase for sponsor accounts, keys, SDKs and a working "hello world" call;
  one or two **build** phases for the integration; and a short submission-prep step in `6-ship`
  (demo video, repo, write-up).

## 4. Opportunity-first (no product yet)
Use the tracks, judging criteria and deep uses of the required tech as constraints for `2-scope`. Ask the
user for their own idea within those constraints; offer a few equally weighted starting points only if
they're stuck. `2-scope` asks: "Would you still build this without the hackathon?"

## 5. Submission prep (later, before the deadline)
Checklist in the brief: video (length, what it must show), repo (public, README, license if required),
live URL (if required), write-up fields, team details, sponsor-tech proof (e.g. screenshots, code links).
Ask whether the user wants to write the write-up themselves or have a draft to edit (some hackathons
require human-written text; check the rules).
