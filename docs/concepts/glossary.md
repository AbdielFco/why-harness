# Glossary

**English** | [Español](glossary.es.md)

| Term | Meaning |
|---|---|
| **Harness** | Everything around the model: entry point, rules, tools, gates, verification, and memory. See [harness](harness.md). |
| **Context window** | The tokens the model sees in one turn. Finite, and resent in full on every turn. |
| **Context engineering** | Deciding what enters the window, when, and when it leaves. |
| **Context base** | What the agent needs in order to work in the repo: `AGENTS.md` and skills. |
| **Knowledge base** | Domain facts with their source: `docs/knowledge/`. |
| **Memory** | What survives a session: the work file, decisions, knowledge. |
| **Orchestrator** | The main session. It coordinates subagents and is the only writer of the work file. |
| **Subagent** | A model instance with its own window, one role, and one permission. It returns a report. |
| **Read-only** | A subagent that cannot edit files (planner, reviewer). |
| **Pipeline** | The fixed stage order: planner, approval, test-writer, implementer, validator, reviewer. |
| **Lane** | Fast (docs, typos) or normal (logic). It decides which stages run. |
| **Gate** | A verifiable checklist on an agent, or an action that needs a human yes. |
| **Human gate** | An action that needs explicit approval: commit, push, delete, dependencies, deploy. |
| **Hook** | A script the tool runs on an agent event. Here, before every shell command. |
| **Fail-closed** | On an error or an unreadable input, deny. The opposite, fail-open, allows. |
| **Skill** | A `SKILL.md` with a `description` always loaded and a body read on demand. |
| **Progressive disclosure** | Showing that something exists at low cost, and loading the detail only when it is needed. |
| **Trigger** | A skill's `description`: it decides when the body is read. |
| **Work file** | `docs/work/<TICKET>.md`. State of the active task. |
| **ADR** | Architecture Decision Record. One file per decision, with context, the decision, and consequences. |
| **Context gap** | What an agent lacked in order to comply, and the layer it belongs in. |
| **Project layers** | `AGENTS.md` (rules), skills (how), knowledge (what). The only thing that changes between projects. |
| **Invariant** | A piece copied without edits: agents, the hook, `init.sh`, the search script. |
| **BM25** | An information-retrieval rank based on term frequency, rarity, and length. |
| **Chunk** | An indexed fragment: one `## ` section of a knowledge doc. |
| **Fail early** | Detecting a broken environment before spending the session: `init.sh`. |
