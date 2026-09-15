# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A personal collection of learning scripts for an ethical hacking / Python course
(`ethicalhacking20262`). There is no application, package, build system, test
suite, or dependency manifest — each `.py` file is a standalone script meant to
be read and run individually to demonstrate one topic.

## Running scripts

There is no build, lint, or test tooling in this repo. Run any script directly
with the venv's interpreter:

```bash
source venv/bin/activate
python3 <script>.py
# e.g.
python3 app.py
python3 foundationspython/session1.py
```

The venv (`venv/`, Python 3.14) has no third-party packages installed — scripts
only use the standard library (`os`, `subprocess`, `getpass`, etc.).

## Structure

- Top-level scripts (`app.py`, `testingmachine.py`) cover Linux/Python
  integration: shelling out via `os.system`/`subprocess`, and SSH automation
  against a lab host using `sshpass`/`getpass`.
- `foundationspython/` holds numbered `sessionN.py` files that build up core
  Python language features (variables, conditionals, loops, lists,
  dictionaries, functions) one lesson at a time.

## Conventions to preserve when editing

- Scripts often keep earlier lesson code commented out above the active code
  (see `foundationspython/session1.py`) as a running lecture history — don't
  delete commented blocks unless asked.
- `testingmachine.py` targets a specific lab host/user (`172.17.130.102`,
  `jenn`) and prompts for a password with `getpass` rather than hardcoding
  credentials — keep secrets out of the script if extending it.
