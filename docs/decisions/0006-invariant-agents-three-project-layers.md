# 0006: Invariant agents and three project layers

**English** | [Español](0006-invariant-agents-three-project-layers.es.md)

- Status: accepted
- Date: 2026-11-19

## Context

In the original implementation the agents named the project's skill, data type, test command, and fixture path. Installing them in another project meant rewriting all of them.

## Decision

The agents, the hook, `init.sh`, and the search script contain nothing about the project. What belongs to the project lives in three layers: `AGENTS.md` (rules and commands), skills (how code is written), `docs/knowledge/` (facts). Plus two marked blocks: `GATES` and `PROJECT CONFIG`.

## Alternatives

| Option | Why not |
|---|---|
| Agents per project | Each project keeps its own fork, and improvements are not shared |
| A config file the agents read | A fourth layer that duplicates `AGENTS.md` |

## Consequences

Agents are updated by copying them. Commands live in two places (`AGENTS.md` and `init.sh`). The reviewer and `adopt.md` require them to match.
