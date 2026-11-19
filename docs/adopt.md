# Adopt the harness in a project

**English** | [Español](adopt.es.md)

About an hour for the base. After that it grows through context gaps.

For an agent to do it, the skill is [`.cursor/skills/adopt-harness/SKILL.md`](../.cursor/skills/adopt-harness/SKILL.md). It covers both paths: install into a project that already exists, or fork this repo and use it as the base. The license is MIT ([LICENSE](../LICENSE)): you can copy and modify it, and the copyright notice travels with the files.

## 1. Copy the invariants

```
.cursor/agents/           the five agents, unchanged
.cursor/hooks.json
.cursor/hooks/gates.py
scripts/init.sh
scripts/knowledge_index.py
scripts/__init__.py
docs/work/0000-template.md
docs/decisions/0000-template.md
docs/knowledge/README.md
```

When the project already has `scripts/`, adjust the paths in `init.sh` and in `AGENTS.md`. The search script reads `docs/knowledge/` relative to the repo root.

Also copy `tests/test_gates.py` and `tests/test_knowledge_index.py` when the project's suite should protect the harness. Point `test_repo_examples_are_findable` at your own knowledge.

## 2. Fill the editable blocks

| File | Block | What to put |
|---|---|---|
| `AGENTS.md` | `PROJECT` (4 blocks) | Description, exact commands, human gates, code rules |
| `scripts/init.sh` | `PROJECT CONFIG` | `TOOLS`, `TEST_CMD`, `PROJECT_FILES` |
| `.cursor/hooks/gates.py` | `GATES` | The shell gates from your `AGENTS.md` |

The commands in `AGENTS.md` and `TEST_CMD` in `init.sh` must match.

## 3. Create the first skill

One, for the area of code you touch most. Use `.cursor/skills/example/SKILL.md` as the template and delete it afterwards. See [skills](concepts/skills.md).

## 4. Seed the knowledge

Do not document the whole domain at once. Start with the three or four entities that show up in most tasks. The rest arrives through context gaps. See [knowledge/README](knowledge/README.md).

## 5. Verify

```bash
./scripts/init.sh
echo '{"command":"git push"}' | python3 .cursor/hooks/gates.py   # must answer ask
echo 'not json' | python3 .cursor/hooks/gates.py                 # must answer deny
python3 -m scripts.knowledge_index search "<one of your entities>"
```

## 6. First task

Pick a small normal-lane task and run it end to end. On close, apply the context gaps. The first three tasks improve the harness the most.

## What not to do

- Do not edit the agents to add project rules. That is a context gap: it goes to a layer.
- Do not grow `AGENTS.md` with everything. A rule that applies to one area goes in its skill.
- Do not open the workspace on a parent folder if you want the hook to run: Cursor loads the `hooks.json` of the workspace you opened.
