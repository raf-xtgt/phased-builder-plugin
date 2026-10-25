<!-- SETUP.md: lives in the PARENT folder (next to project-docs/), never committed. It may hold real IDs, keys and
     account names, filled in by the user over placeholders like <YOUR_API_KEY>. The agent never asks for secrets.
     SETUP_EXAMPLE.md: the same document in the REPO root, committed, with every real value replaced by a dummy one.
     Written at the end of the first `5-setup` run and updated after every later run (and by `9-ship` for deploy
     changes). Keep both files in sync. Only steps that actually worked go here. -->

# [Project Name]: Setup

Last updated: YYYY-MM-DD (setup NN). OS this was verified on: [OS + shell].

## One-Time Setup
Everything a new machine or a new developer needs, once, in order.

### 1. Tools and versions
| Tool | Version | Install / check |
|---|---|---|
| [Flutter] | [3.47.8] | `flutter --version` |

### 2. Accounts and services
| Service | What for | Where to get the value | Value |
|---|---|---|---|
| [Google Play Console] | [publishing] | [console URL] | `<YOUR_ACCOUNT_ID>` |

### 3. Get the code and install dependencies
```bash
git clone <REPO_URL>
cd <repo>
[install command]
```

### 4. Configuration and secrets
Env vars (names → where each value comes from). Files to create from examples (e.g. `cp .env.example .env`).
```
API_KEY=<YOUR_API_KEY>
```

### 5. Platform setup
Emulators, devices, permissions, signing keys, database creation and first migration, etc.

## Run Locally
```bash
cd <repo>
[run command]
```
What you should see.

### Run the tests and checks
```bash
[test / analyze / code-generation commands]
```
What passing looks like.

## Deploy
<!-- "Not set up yet" is fine until deployment is set up. -->
Where it deploys, the exact steps (commands or console clicks), how to check it worked, how to roll back.
