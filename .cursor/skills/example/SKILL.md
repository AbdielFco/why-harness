---
name: example
description: Use when adding or changing a script under scripts/ in this repo.
  Covers the stdout/stderr split, exit codes, and where the test goes. Replace this
  skill with one per area of your project; the description is the trigger.
---

# Writing a script in this repo

Template skill. Only the `description` above is always in context. This body is read
only when the description matches the task, so put here what would be wasted tokens
in every other task.

## Rules

- Stdlib only.
- Stdout is the command result. Diagnostics go to stderr.
- Exit `0` on success, `2` on a usage error, `1` on a runtime failure.
- Every public function has a docstring with Args and Returns.

## Layout

- Code: `scripts/<name>.py`, runnable as `python3 -m scripts.<name>`.
- Test: `tests/test_<name>.py`, `unittest`, no network.

## Writing a good description

- Start with "Use when" and name the concrete trigger: a path, a file type, an action.
- Say what the body covers in one sentence, so the agent can decide without opening it.
- One skill per area. A skill that triggers on everything costs tokens on everything.
