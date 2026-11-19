# Token economy

**English** | [Español](token-economy.es.md)

## What it is

The set of techniques that reduce the tokens entering the model's window **without reducing quality**. Quality often goes up, because less noise means more attention for what matters.

## Why it exists

- Every turn resends the accumulated context. A file read at the start is paid on every later turn.
- Quality drops from noise before the window limit is reached.
- Tokens are money and latency.

## The eight techniques

| # | Technique | Piece | Zone | What it avoids |
|---|---|---|---|---|
| 1 | A short entry point that links | `AGENTS.md` | always | Paying, every turn, for rules the task does not use |
| 2 | Progressive disclosure | skills | on demand | Loading the how of ten areas to touch one |
| 3 | `path:line` results | `knowledge_index.py` | on demand | Opening whole files to find one fact |
| 4 | Subagents with a fixed report | `.cursor/agents/` | isolated | One stage's reads filling the main session |
| 5 | Gates in code | `gates.py` | zero | Permission rules in the prompt of every turn |
| 6 | Fail early | `init.sh` | zero | A whole session on a broken environment |
| 7 | Memory on disk plus a session switch | work file | on demand | Dragging a degraded context along |
| 8 | Out of the index | `.cursorignore` | zero | Secrets and generated artifacts in search |

## How it works: an example

Task: "fix the order total calculation".

**Without a harness:** the agent opens the orders module (400 lines), the tests (300), two utility files (250), searches "total" across the repo, and opens three more hits. It writes the fix and the test. It reviews its own work with all of that in context. The next day, in another session, it reads everything again to remember where it left off.

**With the harness:**

1. `AGENTS.md` (about 80 lines) and the skill `description`s are already loaded.
2. The planner, in its own window, searches `"order total"` and gets `docs/knowledge/entities/order.md:18 Rules`. It reads that section and the two code files that matter. It returns a 30-line plan.
3. The main session receives only those 30 lines.
4. test-writer, implementer, and validator work in isolation. Each returns its report.
5. The reviewer receives the diff, not the history.
6. The next day: `AGENTS.md` plus the work file, and work continues from "Remaining".

The main session never saw the full files. It saw plans, reports, and a diff.

## Cost in context

What the harness always charges: `AGENTS.md` and one `description` per skill. Everything else is on demand, isolated, or zero.

## Limits

- The total tokens of the normal lane, adding up the subagents, can exceed one agent doing everything. What goes down is the main session's context and the rework.
- The agent can ignore `path:line` and read the whole file. The harness guides. It does not force.

## How to adapt it

For every new rule, pick the cheapest zone that works: code (zero), a subagent (isolated), a skill or knowledge (on demand), and only at the end `AGENTS.md` (always).
