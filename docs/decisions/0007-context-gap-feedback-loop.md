# 0007: Context gap as feedback

**English** | [Español](0007-context-gap-feedback-loop.es.md)

- Status: accepted
- Date: 2026-11-19

## Context

Agents reported what they lacked, and no step turned that report into a change. The same gap was paid on every task.

## Decision

Every report names the gap's layer (`AGENTS.md`, skill, knowledge). The orchestrator records it in the work file and, when the task closes, applies it to that layer. No gap is applied by editing an agent.

## Alternatives

| Option | Why not |
|---|---|
| Gaps with no owner | They get reported and forgotten |
| Applying them immediately | It interrupts the task and mixes harness changes with the code change |

## Consequences

The harness improves with every task. Applying gaps without judgment inflates `AGENTS.md`. The rule is to prefer the on-demand layer.
