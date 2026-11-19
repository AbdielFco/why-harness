# 0003: Fail-closed shell hook

**English** | [Español](0003-fail-closed-shell-hook.es.md)

- Status: accepted
- Date: 2026-11-19

## Context

Irreversible actions (push, delete, deploy, change dependencies) are just another command to the agent. A rule in the prompt costs tokens on every turn and can be ignored.

## Decision

`beforeShellExecution` runs `gates.py`. When a `GATES` regex matches, it answers `ask`. When the payload cannot be read, `deny`. `hooks.json` sets `failClosed: true`, so a failed script blocks the command.

## Alternatives

| Option | Why not |
|---|---|
| Rules in `AGENTS.md` only | They are not mandatory and they cost tokens always |
| Fail-open on error | A broken hook would disable every brake with no warning |
| `deny` for every gate | It blocks legitimate work. `ask` leaves the decision to the human |

## Consequences

Zero tokens, and testable. It only sees shell text: file edits and writes inside a process still depend on `AGENTS.md`. It produces false positives on purpose.
