# Portability across tools

**English** | [Español](portability.es.md)

## What it is

The pieces of the harness are concepts. Each agent tool puts them in a different path.

## Why it exists

A team can use more than one tool, and the harness should not be tied to one of them.

## How it works

| Piece | Cursor | Claude Code | opencode |
|---|---|---|---|
| Entry | `AGENTS.md` | `CLAUDE.md` (it can import `AGENTS.md`) | `AGENTS.md` |
| Subagents | `.cursor/agents/*.md` | `.claude/agents/*.md` | `.opencode/agent/*.md` |
| Skills | `.cursor/skills/*/SKILL.md` | `.claude/skills/*/SKILL.md` | `.opencode/skills/*/SKILL.md` |
| Hooks | `.cursor/hooks.json` | `.claude/settings.json` (`hooks`) | plugins |
| Out of the index | `.cursorignore` | `permissions.deny` | `permission.read` |

`AGENTS.md` is the shared format: several tools read it with no configuration. That is why it is the entry point, rather than a file owned by one tool.

Knowledge, memory, `init.sh`, and `knowledge_index.py` are markdown and scripts. They work the same in any tool.

## Cost in context

None extra. Only the paths change.

## Limits

- The stdin/stdout protocol of hooks differs between tools. `gates.py` follows Cursor's. For another tool, reuse `decide()` and change the `main()` wrapper.
- `readonly` on subagents does not exist the same way everywhere. Where it does not, restrict the subagent's tools instead.
- The paths in this table change with each tool's versions. Check them in that tool's documentation.

## How to adapt it

Keep a single source (the files under `.cursor/`, or those of the main tool) and link or copy toward the others. Two sources edited by hand drift apart.
