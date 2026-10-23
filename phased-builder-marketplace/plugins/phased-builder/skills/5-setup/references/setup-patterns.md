# Setup Patterns: Agent Reference

Used by `5-setup`. The user does every setup step; you plan the steps, explain them, and debug. A setup run is done
only when something **runs** and the user has checked it.

## The walking skeleton (standard practice for the main setup)
The first setup run usually ends with a "walking skeleton": the thinnest version of the real system running end to
end. For a web or mobile app: the framework's starter app running locally, one sample test passing, and (if
deployment is in scope now) the same thing live at a URL. It proves the toolchain, structure and deploy path before
any feature depends on them.

## What to plan (only what applies; decision card for each consequential choice)
Check current versions, prices and region availability by searching; cite.
1. **Runtime / SDK and version:** the current stable or LTS, pinned (`.nvmrc`, `.python-version`, `fvm`, toolchain
   files, `engines`).
2. **Package manager:** the ecosystem default. Commit the lockfile.
3. **Framework and starter:** the official CLI or starter (e.g. `flutter create`, `npm create vite@latest`).
   Say what it generates.
4. **Project structure:** as in `ARCHITECTURE.md > Project Folder Structure`.
5. **Config and secrets:** env var names; `.env` git-ignored; `.env.example` with placeholders; host secret store for
   deployed values. Never secrets in client-side code.
6. **Formatter and linter:** ecosystem default, set up once.
7. **Test runner:** ecosystem default, with one passing sample test.
8. **Database:** local dev database or managed free tier; how to create it, connect, run the first migration.
9. **Cloud and deployment:** provider console steps or CLI, region, free-tier limits, how to deploy and roll back.
10. **CI:** only if the scale or team needs it (decision card).
11. **Dev tools:** editor extensions, emulators/simulators, CLIs the stack needs.

## Writing steps the user can follow
- Exact commands for their OS and shell. Ask the OS once.
- UI steps (cloud consoles, app stores, dashboards): menu path, button names, what to enter, what to choose, and
  what the screen shows after. Say these UIs change often; if theirs looks different, ask for a screenshot.
- Files the user creates: full content in a code block with the exact path.
- Each step: Do / Files you create / Expect / Pass when.
- Order so later steps can't fail because of an earlier unchecked step.

## Debugging setup errors
Common causes to check first: wrong runtime version or a second install on PATH; missing system dependency;
permissions; port in use; proxy or certificate issues; wrong working directory; cached old build; an expired or
wrong-scope key; a cloud service not enabled in the console; region mismatch; free tier needs a card.
Explain the error in plain words, test the most likely cause first, one change at a time. Search unfamiliar errors
and cite.

## Existing code (adopting a project)
Document what exists before changing anything: stack, versions, how to run, how to test, what's broken. The proof is
"it runs as it did before, and now it's documented."

## Platform gotchas to check
OS differences (Windows paths and shells, macOS vs Linux tools), version managers vs system installs, Android SDK and
emulator setup, iOS needs macOS and Xcode, free hosting tiers that sleep or cap builds, services that block some
countries or need a business registration.
