# Starting a Feature: Agent Reference

A feature starts in `6-prd`. Do these steps once. If `STATE.md` already shows this feature as current,
skip to the skill's own work.

1. **Pick the feature.** The first unchecked item in `scope.md > Roadmap`, unless the user names another.
   A feature that isn't on the roadmap goes through `3-scope` first (a short roadmap update keeps it honest).
2. **Check the previous feature is closed.** If another feature is `in progress` and its checklist's
   "Close the Feature" items are unchecked, say so and recommend finishing it with `8-build` first. If the user
   wants to switch anyway, log a `PIVOT` and leave that feature `in progress`.
3. **Check readiness.** `ARCHITECTURE.md` should exist (from `4-architecture`) and the main setup should be done
   (a `setup/` file marked done). If not, say which skill comes first. The user may go ahead anyway; log it.
4. **Create the folder** `project-docs/features/NN-short-name/`. NN is the feature number from the roadmap
   (F-03 → `03-...`).
5. **Record it:**
   - `PRODUCT.md`: the feature's Status → `in progress`, Feature folder → the path.
   - `STATE.md`: `skill: 6-prd`, `current_feature`, `mode: vibe`, Now, Next step, `updated`.
   - `BUILD_LOG.md`: `FEATURE` entry "F-NN [name] started".
6. **Load context, lightly:** `PRODUCT.md`, `ARCHITECTURE.md`, `scope.md > Scale`, the last ~5 log entries,
   related `parked` PARKING_LOT items, and any active opportunity brief. Do not read old feature folders unless
   a master doc or log entry points you there.
7. Say back in two or three sentences what this feature is and what you read.
