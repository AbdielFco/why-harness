# 0005: Three memory types, one writer

**English** | [Español](0005-three-memory-types-single-writer.es.md)

- Status: accepted
- Date: 2026-11-19

## Context

The conversation gets compacted and is lost between sessions. A fourth folder for investigations competed with decisions and knowledge, and it was unclear where to look. Several agents writing the same state file produced contradictions.

## Decision

Three types: task (`docs/work/`, deleted on close), decision (`docs/decisions/`, permanent), fact (`docs/knowledge/`, permanent). Only the orchestrator writes the work file. Subagents return reports.

## Alternatives

| Option | Why not |
|---|---|
| Memory only in the conversation | It is lost on compaction or on a session switch |
| An investigations folder | What is worth keeping ends as a fact or a decision |
| Each subagent writes its own section | Contradictory state, and edit conflicts |

## Consequences

Switching session is cheap. The orchestrator can forget to update the work file. The reviewer checks it.
