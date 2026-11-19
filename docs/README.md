# Docs

**English** | [Español](README.es.md)

Index. The content lives in each folder.

| Folder | What it holds | When to read it |
|---|---|---|
| [concepts/](concepts/) | What each piece is, why it exists, how it works | To understand or change the harness |
| [decisions/](decisions/) | ADRs: why the harness is built this way | Before changing a piece |
| [knowledge/](knowledge/README.md) | Domain facts, each with its source | Any change that depends on a fact |
| [work/](work/0000-template.md) | Memory of the active task. Deleted when it closes. [Español](work/0000-template.es.md) | At the start and at the end of each phase |
| [adopt.md](adopt.md) | How to install the harness in a project | Once, when adopting it |
| [references.md](references.md) | Research sources behind each decision | When asking why a piece exists |

## Concepts

| Doc | In one line |
|---|---|
| [harness](concepts/harness.md) | Agent = model + harness |
| [context-engineering](concepts/context-engineering.md) | The context window as a budget, in four zones |
| [knowledge-base](concepts/knowledge-base.md) | Sourced facts, retrieved by fragment |
| [agents-and-subagents](concepts/agents-and-subagents.md) | One agent per bias it prevents |
| [pipeline-and-lanes](concepts/pipeline-and-lanes.md) | Fixed order, two lanes, where each FAIL returns |
| [hooks](concepts/hooks.md) | What code can check is not asked of the model |
| [skills](concepts/skills.md) | Progressive disclosure |
| [memory-and-sessions](concepts/memory-and-sessions.md) | Memory on disk, and when to start clean |
| [feedback-loop](concepts/feedback-loop.md) | The context gap is how the harness learns |
| [token-economy](concepts/token-economy.md) | The eight techniques in one table |
| [portability](concepts/portability.md) | The same pieces in other tools |
| [glossary](concepts/glossary.md) | Terms |

Every page has a Spanish twin named `*.es.md`, linked at the top.

Search the knowledge base: `python3 -m scripts.knowledge_index search "<query>"`.
With an exact id, search the text directly under `knowledge/`.
