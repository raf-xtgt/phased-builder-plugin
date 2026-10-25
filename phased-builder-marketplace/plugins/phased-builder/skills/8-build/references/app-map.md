# Optional Learning Wrap-Up and App Map: Agent Reference

Offered once at the end of a feature, after Close the Feature. Optional. Declining is a complete answer.
Budget about five minutes.

## Wrap-up (pick one, suggest it, let them redirect)
- **Follow one action** through 2–3 real code locations from this feature (entry point → logic/storage →
  result). Real relative paths and function names. In mentor mode they wrote it, so ask them to lead the
  route and you fill gaps.
- **Revisit a decision:** one decision card from this feature (L-ID) and what the build showed about it.
- **Revisit a bug:** one `BUG` entry and the evidence that found the cause.

End with one reusable practice, grounded in this project's evidence. Optionally ask once: "What would you do
differently next feature?" Record personal reflections only in `profile.md` (outside the repo).

## The app map: `project-docs/app-map.html`
A single living page, updated (not recreated) at the end of each feature where the user wants it.
- Plain-language overview of the app and its main pieces (from `ARCHITECTURE.md`).
- A small inline SVG or HTML/CSS diagram: one real action → its code locations → the visible result.
- A short route per feature: real paths (relative to `<repo>/`) and symbols, one line each.
- "To change this, start here" pointers.
- Which feature added what, linking the feature folders.
- The commit it reflects; note it can drift.

Rules: no build step, no framework, no network requests, no analytics, no secrets, works with scripts
off (use `<details>` for reveals), escape code snippets. Check every path and symbol against the real code.
