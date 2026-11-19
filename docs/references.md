# Research references

**English** | [Español](references.es.md)

Sources behind the decisions in [decisions/](decisions/). Each one is an influence, not a claim that this repo implements that system. Dates and URLs were checked on 2026-11-19.

## Agents, workflows, and the harness

| Source | What it contributes here |
|---|---|
| Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents), 19 Dec 2024 | Workflows with a fixed path beat a free-running agent for a known task. The orchestrator-workers and evaluator-optimizer patterns are the pipeline: planner, implementer, validator, reviewer, with a human checkpoint. |
| Anthropic, [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents), 26 Nov 2025 | A fresh session has no memory, so state has to live on disk. Their initializer writes an `init.sh` and a progress file; the next session reads them and does one increment. That is `scripts/init.sh`, `docs/work/`, and the session-switch rule. |
| Anthropic, [Harness design for long-running apps](https://www.anthropic.com/research/harness-design-long-running-apps), 24 Mar 2026 | Splits planning, generation, and evaluation into separate agents so a spec error does not cascade silently. Same reason planner and reviewer are read-only and the validator is a different stage from the reviewer. |

## Context as a budget

| Source | What it contributes here |
|---|---|
| Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents), 2025 | The smallest set of high-signal tokens. Just-in-time retrieval by identifier instead of loading the corpus. Notes outside the window for anything that must survive compaction. That is `AGENTS.md`, `path:line` search, skills, and the work file. |
| Nelson F. Liu et al., [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172), TACL 2024 (arXiv:2307.03172, 2023) | Accuracy drops when the relevant fact sits in the middle of a long input. A reason to return a section instead of a file, and to keep the always-loaded prompt short. |

## Retrieval

| Source | What it contributes here |
|---|---|
| Stephen Robertson and Hugo Zaragoza, [The Probabilistic Relevance Framework: BM25 and Beyond](https://doi.org/10.1561/1500000019), Foundations and Trends in Information Retrieval 3(4), 333–389, 2009 | The ranking in `scripts/knowledge_index.py`: term frequency, inverse document frequency, and length normalization. In-memory and dependency-free on purpose; the tradeoff is recorded in [ADR 0004](decisions/0004-in-memory-bm25-over-embeddings.md). |

## Conventions and enforcement

| Source | What it contributes here |
|---|---|
| [AGENTS.md](https://agents.md/), stewarded by the Agentic AI Foundation under the Linux Foundation | The open, tool-neutral file for project instructions. It is the entry point so the same rules work in Cursor, Claude Code, and opencode. See [portability](concepts/portability.md). |
| Cursor, [Hooks](https://cursor.com/docs/hooks) | `beforeShellExecution` receives the command on stdin and answers `allow`, `ask`, or `deny`. `failClosed: true` blocks the command when the script fails. That is `.cursor/hooks.json` and `gates.py`. |
| Jerome H. Saltzer and Michael D. Schroeder, [The Protection of Information in Computer Systems](https://doi.org/10.1109/PROC.1975.9939), Proceedings of the IEEE 63(9), 1975 | Fail-safe defaults: a decision that cannot be made denies. The hook denies a payload it cannot read. See [ADR 0003](decisions/0003-fail-closed-shell-hook.md). |
