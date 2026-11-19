# Agents and subagents

**English** | [Español](agents-and-subagents.es.md)

## What it is

- **Main agent (orchestrator):** the session the human talks to. It has no file of its own. Its contract is `AGENTS.md`.
- **Subagent:** a model instance with its own context window, one role, and one permission, defined in `.cursor/agents/<name>.md`. It receives an input, works in isolation, and returns a report.

## Why it exists

One agent that plans, writes tests, implements, and reviews has two problems:

1. **Context.** By review time it carries the whole implementation history: failed attempts, reads, errors. Its window is full and biased.
2. **Author bias.** Whoever wrote the code reviews it with the intention in mind, not with what the diff says.

Splitting into subagents fixes both. Each one starts clean and has a single job.

## Why each agent exists

Each agent exists because it separates a responsibility that, mixed with another, produces a specific bias.

| Agent | Permission | It does | It separates | Bias it avoids |
|---|---|---|---|---|
| **planner** | read-only | Locates, reads, proposes files, the test, reuse, gates, risks | Understanding from doing | Editing before understanding |
| **test-writer** | tests only | Writes a test that fails for the reason in the plan | Specifying from implementing | A test that confirms the implementation instead of the intent |
| **implementer** | files in the plan | The smallest change that turns the test green | Implementing from widening scope | The "while I'm here" |
| **validator** | runs, does not edit | The full suite and the acceptance check | Runtime evidence from opinion | "It should work" |
| **reviewer** | read-only | Compares the diff with the plan | Judging from having written | Reviewing the intention instead of the diff |
| **orchestrator** | everything, behind gates | Collects reports, writes memory, applies context gaps | Coordinating from executing | Contradictory state between subagents |

### Why validator and reviewer stay separate

The validator runs commands and produces artifacts (test reports, coverage). The reviewer only reads the diff. Merged, the reviewer drags the test output along and loses the clean context, which is exactly what makes it useful.

### Why test-writer and implementer stay separate

If the same agent writes the test and the code, the test tends to describe what the code does. Kept apart, the test describes what the plan asks, and the implementer cannot touch it: when the test is wrong, it returns `FAIL` and says why.

### Why planner and reviewer are read-only

An agent that cannot edit has no temptation to "just fix it". The planner has to understand. The reviewer has to judge. Neither job gets better with write permission.

## How it works here: the report contract

All five return the same structure:

```markdown
## Verdict: PASS | FAIL
## Gate              the checklist for this agent
## What is wrong
## What is incomplete
## Suggestions
## Context gap       AGENTS.md | skill | knowledge
```

- **Verdict** is binary. There is no "PASS with notes". It meets the gate, or it does not.
- **Gate:** a checklist that can be verified. It stops the agent from grading itself by impression.
- **Context gap:** what it lacked in order to comply, and which layer should hold it. See [feedback-loop](feedback-loop.md).

The contract is inline in each agent, not in a shared file. A subagent does not inherit files, and an include would cost an extra read on every invocation.

### The agents are invariant

No agent names a language, a framework, or a domain. They read commands from `AGENTS.md`, the how from the skill that matches, and the facts from `docs/knowledge/`. Installing the harness in another project means copying the agents unchanged.

## Cost in context

Invoking a subagent costs its prompt (about 40 lines) plus the input. In exchange, everything it reads stays out of the main session, which receives only the report. On a normal task the planner can read 10 files and return 30 lines.

## Limits

- `readonly` depends on the tool honoring it. Cursor does. Other tools may not.
- Five stages for a typo is waste. That is why the fast lane exists ([pipeline-and-lanes](pipeline-and-lanes.md)).
- Subagents do not share memory with each other. Whatever one needs from another goes through the orchestrator.

## How to adapt it

Do not edit the agents. When an agent fails on something specific to the project, that is a context gap: it goes to `AGENTS.md`, a skill, or knowledge.
