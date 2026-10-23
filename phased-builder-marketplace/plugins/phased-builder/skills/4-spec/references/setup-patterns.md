# Setup Patterns: Agent Reference

Used by `4-spec` for setup phases. A setup phase prepares the environment so build phases can deliver
features. It is done only when something **runs** and the user has checked it.

## The walking skeleton (standard practice)
The first setup phase usually ends with a "walking skeleton": the thinnest version of the real system
running end to end. For a web app: the framework's starter page served locally, one empty test passing,
and (if deployment is in this phase) the same page live at a URL. It proves the toolchain, the
structure and the deploy path before any feature depends on them.

## What a setup spec should decide (only what applies)
Use a decision card for each choice with consequences. Check current versions and prices by searching; cite.

1. **Runtime and version:** the current LTS/stable, pinned (`.nvmrc`, `.python-version`, `engines`, toolchain file).
2. **Package manager:** the ecosystem default unless there's a reason. Commit the lockfile.
3. **Framework and starter:** the official starter/CLI where one exists. Note what it generates.
4. **Project structure:** the framework's convention first.
5. **Config and secrets:** env vars by name; `.env` git-ignored; `.env.example` with placeholders; host secret store for deployed values. Never put secrets in client-side code.
6. **Formatter and linter:** the ecosystem default, set up once.
7. **Test runner:** the ecosystem default, with one passing sample test so later phases have a working harness.
8. **CI:** only if the scale or team needs it (a decision card). Solo, small projects often start without it.
9. **Hosting and deployment:** match scale and budget. Check region availability for the user's country and for their users. Note free-tier limits, cold starts, and what happens when limits are hit. Plan rollback.
10. **Accounts:** list each account the user must create. The user creates accounts and enters credentials themselves; never ask for passwords or keys in chat.

## Existing code (adopting a project)
If the folder already has code, the setup phase documents what exists before changing anything: stack,
versions, how to run it, how to test it, what's broken. The proof is "it runs as it did before, and now it's documented."

## Turning the setup into checklist steps
Each step in **Step-by-Step Setup Order** becomes a checklist item with:
- what the agent does (vibe) or what the user does (mentor);
- the command(s) the user runs;
- the expected output and the pass/fail rule.
Steps are small enough that a failure points to one cause. The last step is **The Proof It Works**.

## Version and platform gotchas to check
- OS differences (Windows paths and shells, macOS vs Linux tools). Ask the user's OS if it matters.
- Node/Python version managers vs system installs.
- Ports already in use.
- Free hosting tiers that sleep, cap builds, or need a card.
- Services that block some countries or need a business registration.
