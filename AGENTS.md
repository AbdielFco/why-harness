# AGENTS.md

Entry point for every agent session. Keep it short: link, do not copy.
Blocks marked `PROJECT` are the only part you edit when installing the harness. Everything else is invariant.

<!-- PROJECT: one paragraph. What the project does and where its state lives. -->
`why-harness` is a generic AI harness template. Its own code is two stdlib scripts and their tests.
<!-- /PROJECT -->

## Start here

1. Run `./scripts/init.sh`. A `[FAIL]` stops the session.
2. With a ticket, read `docs/work/<TICKET>.md`. If it does not exist, create it from `docs/work/0000-template.md`. Without a ticket, use a kebab-case slug.
3. Docs index: `docs/README.md`.
4. Find a fact: search `id:` under `docs/knowledge/`. Without an exact name: `python3 -m scripts.knowledge_index search "<query>"`. Read only the chunk at the returned `path:line`.

## Commands

<!-- PROJECT: the exact commands. Agents read them from here, never guess. -->
| Purpose | Command |
|---|---|
| Session check | `./scripts/init.sh` |
| Full test suite | `python3 -m unittest discover tests` |
| Single test | `python3 -m unittest tests.<module>` |
| Lint | none |
| Knowledge search | `python3 -m scripts.knowledge_index search "<query>"` |
<!-- /PROJECT -->

## Lanes

- **Fast lane**: docs, typos, comments, config with no logic. The main session edits, then the `reviewer` runs. No plan, no test.
- **Normal lane**: any change to logic, behavior, or an interface. Full pipeline.

When in doubt, normal lane.

## Pipeline (normal lane)

`planner` -> human approval -> `test-writer` -> `implementer` -> `validator` -> `reviewer`.

Agents live in `.cursor/agents/`. Every agent returns `PASS` or `FAIL` with: what is wrong, what is incomplete, suggestions, and the context gap (`AGENTS.md`, a skill, or `docs/knowledge/`).

A `FAIL` returns to the stage that failed. A `FAIL` from `validator` or `reviewer` returns to `implementer`. Commit only on an explicit order, and only after the reviewer returns `PASS`.

## Human gates

<!-- PROJECT: actions that need an explicit yes. Mirror the shell ones in .cursor/hooks/gates.py. -->
Need an explicit yes: commit, push, deleting files or data, adding or removing a dependency, any deploy, editing secrets or permissions, editing `.cursor/hooks/`.
<!-- /PROJECT -->

`.cursor/hooks/gates.py` enforces the shell part. It cannot see a file edit or a write done inside a running process. Those still wait for a yes.

## Code rules

<!-- PROJECT: three to six rules, or a pointer to the skill that holds them. -->
- Stdlib only. No new dependency.
- No bare `except`. Errors go to stderr with a prefix; stdout is the command result.
- Every script change has a test in `tests/`.
<!-- /PROJECT -->

Do not read `.env` or credential files. Variable names live in `.env.example`.

## Memory

| Type | Lives in | Lasts |
|---|---|---|
| Task | `docs/work/<TICKET>.md` | until the task closes |
| Decision (why) | `docs/decisions/` | permanent |
| Fact (what) | `docs/knowledge/` | permanent |

The main session is the only writer of `docs/work/<TICKET>.md`. Subagents return reports and do not write it.

Switch session at the end of each phase (Plan, Implement, Verify), or sooner when the session repeats a question already answered in the work file, contradicts a recorded fact, is corrected twice, or reads more than 10 files without writing. The new session reads `AGENTS.md`, the work file, and continues from "Remaining".

## Closing a task

1. Apply every entry under "Context gaps" in the work file to its layer (`AGENTS.md`, skill, or knowledge).
2. Add a decision file when the task made a decision the code does not show.
3. Put the summary in the PR, then delete `docs/work/<TICKET>.md`.
