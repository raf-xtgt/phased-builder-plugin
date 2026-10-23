# Choosing the Mode: Agent Reference

Used at the start of `4-architecture`, `7-spec` and `8-build`, **every time the skill starts** (not on resume
within the same run, unless the user wants to change). The user has full freedom to pick either mode; never
steer by deadline or speed.

Ask with a choice tool (2 options), one line each, adapted to the skill:

| Skill | Vibe | Mentor |
|---|---|---|
| `4-architecture` | I propose the design with decision cards; you decide; I write it up. | You propose the design; I coach you on system design, challenge it, explain standards and costs; then I write it up. |
| `7-spec` | I propose how this feature is built; you decide; I write the spec. | You propose how it's built; I coach and challenge; then I write the spec. |
| `8-build` | I write the code; you run the checks and commit. | You write the code; I give blueprints, doc links and reviews. I don't write project code. |

Then:
1. Set `mode:` in `STATE.md` (`vibe` or `mentor`).
2. Record it in the skill's document: the `mode:` frontmatter of `spec.md` or `checklist.md`, or the
   session's row in `ARCHITECTURE.md > Design History`.
3. Log a short `DECISION` entry only if the user gives a reason worth keeping; otherwise the frontmatter is enough.

**Switching mid-skill:** only when the user says so in chat. Update `mode:` in STATE.md, the document
frontmatter, and log it. Never change the mode yourself.

**When the skill ends,** set `mode:` back to `vibe` in STATE.md (the default for every other skill).
