# Harness

**English** | [Español](harness.es.md)

## What it is

The **harness** is everything around the model that is not the model: what it reads at the start, which rules it follows, which tools it has, what it cannot do without permission, how its work is checked, and where it keeps what it learns.

The word comes from *test harness*: the scaffolding that runs code under controlled conditions and checks the result. Here the code under test is the agent's behavior.

```
agent = model + harness
```

Two agents with the same model and a different harness perform differently. The model supplies the capability. The harness decides how much of that capability reaches the result.

## Why it exists

Without a harness, a coding agent:

- **Reads too much.** It opens whole files "just in case" and fills the context window with noise.
- **Forgets.** What it decided 40 messages ago gets diluted or summarized badly.
- **Edits before it understands.** It can, so it does.
- **Approves its own work.** It writes the code and the test, and the test confirms what the code does, not what it was supposed to do.
- **Crosses limits.** An `rm`, a `push`, or a deploy is just another command.

Every piece of this repo targets one of those failures.

## How it relates to other terms

| Term | Question it answers | Scope |
|---|---|---|
| Prompt engineering | How do I word this instruction? | One message |
| Context engineering | What information enters the window, and when? | One session |
| Harness engineering | What structure makes every session come out right? | The project, every session |

The harness contains the other two. `AGENTS.md` and the agents are carefully written prompts. Fragment search and skills are context engineering. What the harness adds is what does **not** depend on the model: deterministic hooks, `init.sh`, the report contract, and memory on disk.

## How it works here

| Failure | Piece | Doc |
|---|---|---|
| Reads too much | `path:line` search, skills on demand | [knowledge-base](knowledge-base.md), [skills](skills.md) |
| Forgets | Work file, decisions, knowledge | [memory-and-sessions](memory-and-sessions.md) |
| Edits before understanding | read-only planner plus human approval | [agents-and-subagents](agents-and-subagents.md) |
| Approves its own work | a separate test-writer, a reviewer with a clean context | [agents-and-subagents](agents-and-subagents.md) |
| Crosses limits | The `gates.py` hook | [hooks](hooks.md) |
| Repeats the same mistakes | Context gap | [feedback-loop](feedback-loop.md) |

## Cost in context

The harness spends tokens too. `AGENTS.md` and every skill `description` are always loaded. That is why `AGENTS.md` stays short and links instead of copying. A line that is always loaded has to save more tokens than it costs.

## Limits

- The harness does not make the model smarter. It removes ways to fail.
- Rules in markdown are suggestions to the model. Only the hook and `init.sh` are mandatory.
- A harness that grows too large becomes its own problem: every always-loaded line competes with the real work.

## How to adapt it

Do not edit this concept. Fill the three project layers. See [adopt](../adopt.md).
