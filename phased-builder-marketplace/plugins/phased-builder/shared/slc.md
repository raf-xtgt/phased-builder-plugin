# SLC Guide (Simple, Lovable, Complete): Agent Reference

Source idea: Jason Cohen, "Your customers hate MVPs. Make a SLC instead."
(https://longform.asmartbear.com/slc/). Summary in our own words below. Use it for the product as a
whole in `2-scope` and for every build phase in `3-prd`.

## The three tests

- **Simple:** it does one main job. Small enough to build and check quickly. A simple thing is fine as long
  as it never claims to do more than it does.
- **Lovable:** there is at least one reason someone would *want* to use it, not just *could*. Love can come
  from delight in the UI, from speed, from a sharp insight, from tone, or from fitting the user's identity.
  Name the specific thing. "Clean UI" alone is weak; "you see your streak the moment you open it" is specific.
- **Complete:** a user can finish that one job from start to end with no dead ends, no broken buttons,
  no "coming soon" placeholders. It is version 1.0 of something small, not version 0.1 of something big.
  If no more work ever happened, it would still be useful.

**SLC vs MVP:** an MVP is often incomplete on purpose ("we'll learn from it"). SLC keeps the scope small
but makes what exists whole and pleasant.

## The SLC check (run before a build-phase PRD is approved)

Write it in the PRD under `## SLC Check`. One or two lines each:

- **Simple:** the one job of this phase is ___. Anything beyond that went to the parking lot (P-IDs).
- **Lovable:** the specific thing that makes it nice is ___. How we will see it during the build: ___.
- **Complete:** the user can go from ___ to ___ with no dead ends. Every visible control works.
  Empty, error and first-use states are handled: ___.

If a test fails, **shrink the job, don't leave it unfinished.** Offer the user 1–2 smaller versions
that would pass all three tests. Never pass "Complete" by hiding a gap behind a disabled button or a
"coming soon" label.

## Deferring ideas (not "coming soon")

Ideas that come up while planning or building are good. They go to `PARKING_LOT.md` with a P-ID, not into
the product as a stub. The product shows no trace of a parked idea. When the user plans new phases in
`2-scope`, the parking lot is reviewed and ideas can be promoted to phases.

## Phases add up to the product

Each build phase is SLC on its own: after it ships, the product is still whole. The roadmap should
reach a first **SLC v1** (the smallest set of phases that is useful on its own) before adding breadth.
Put the project's unique kernel in the earliest build phase possible.

## Setup phases

SLC does not apply to setup phases. Their test is: **does it run?** Every setup phase ends with a check the
user can run (a local "hello world", a passing empty test, a deployed URL that responds).
