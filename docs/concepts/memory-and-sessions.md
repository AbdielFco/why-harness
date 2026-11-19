# Memory and sessions

**English** | [Español](memory-and-sessions.es.md)

## What it is

**Memory** is what survives a session. Here it lives on disk, in three types by how long it lasts:

| Type | It answers | Where | It lasts |
|---|---|---|---|
| Task | Where did we leave off? | `docs/work/<TICKET>.md` | Until the task closes |
| Decision | Why is it this way? | `docs/decisions/NNNN-*.md` | Permanent |
| Fact | What is true? | `docs/knowledge/` | Permanent, and it gets updated |

## Why it exists

- **The conversation is not memory.** It gets compacted and summarized, and it disappears when another session opens.
- **A long session degrades.** It accumulates failed attempts, irrelevant reads, and corrections. Past a point, starting clean is cheaper than continuing.
- **Starting clean only works when the state is written down.** The work file is what makes a session switch cheap.

## How it works here

### The work file

Template at [work/0000-template.md](../work/0000-template.md): Phase, Goal, Plan, Remaining, Verification, Context gaps, Log. The headings stay in English because the agents match them.

- The orchestrator creates it when a task starts.
- **One writer:** only the orchestrator edits it. Subagents return reports and the orchestrator copies what matters. Two agents writing the same file produce contradictory state.
- It is deleted when the task closes. Anything worth keeping moves to a decision, to knowledge, or to the PR.

### When to switch session

At the end of each phase (Plan, Implement, Verify), or sooner when the session:

- repeats a question already answered in the work file,
- contradicts a recorded fact,
- is corrected twice by the human, or
- reads more than 10 files without writing anything.

Each signal means the context is contaminated or lost. The new session reads `AGENTS.md` and the work file, and continues from "Remaining".

### Why there is no investigations folder

An investigation worth keeping ends as a fact (knowledge) or a decision (decisions). A third folder competes with the other two, and nobody knows where to look.

## Cost in context

The work file is read at the start of every session, so it has to fit on one screen. When it grows, anything that is not "Remaining" gets summarized or moved.

## Limits

- The orchestrator can forget to update the work file. The reviewer checks it in its gate.
- Switching session is a decision for the human or the agent. The harness only gives the signals.

## How to adapt it

Use your tracker's ticket id as the work file name. Adjust the session-switch signals when your flow needs different ones.
