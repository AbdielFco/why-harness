# 0002: Read-only planner and reviewer

**English** | [Español](0002-readonly-planner-and-reviewer.es.md)

- Status: accepted
- Date: 2026-11-19

## Context

An agent that can edit tends to do it. The planner "takes the chance" to fix something. The reviewer "corrects it quickly" instead of reporting. In both cases the human loses the control point.

## Decision

`planner` and `reviewer` are declared `readonly: true`. The validator runs commands and does not edit code or docs.

## Alternatives

| Option | Why not |
|---|---|
| An instruction "do not edit" without readonly | It is a suggestion. The permission is a guarantee |
| A reviewer that corrects | It becomes a second implementer, with no plan and no test |

## Consequences

Every correction goes through the implementer and stays inside the plan. It depends on the tool honoring `readonly`.
