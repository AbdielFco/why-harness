# 0001: Five-stage pipeline with two lanes

**English** | [Español](0001-five-stage-pipeline-two-lanes.es.md)

- Status: accepted
- Date: 2026-11-19

## Context

One agent that plans, tests, implements, and reviews edits before it understands and approves its own work. Sending every change through every stage spends tokens on changes with no risk (typos, docs).

## Decision

Normal lane: planner, human approval, test-writer, implementer, validator, reviewer.
Fast lane (docs, typos, config with no logic): orchestrator, then reviewer.
When in doubt, normal lane.

## Alternatives

| Option | Why not |
|---|---|
| One agent | Author bias, and a contaminated context at review time |
| One pipeline for everything | Five stages for a typo |
| Three stages (plan, implement, review) | Loses the test written ahead of and apart from the implementation, and runtime evidence apart from static judgment |

## Consequences

More tokens in total on the normal lane, less context in the main session, and less rework. Lane classification can be wrong. The reviewer runs on both.
