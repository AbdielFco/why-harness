---
name: adopt-harness
description: Use when installing why-harness into an existing project, or when
  starting a new project from this repository as the base. Covers which files to
  copy, which blocks to fill, what to keep under the MIT license, and how to
  verify the install.
---

# Install why-harness

Two ways. Pick one from what the user asked. Do not edit the five agents in
either case. Keep `LICENSE` in every copy: the MIT terms require the copyright
and permission notice to travel with the files.

Human guide: `docs/adopt.md`.

## A. Install into an existing project

Copy these paths from this repo into the target root. Do not overwrite a file
the target already has; merge into it and say which lines you added.

```
.cursor/agents/                 the five agents, unchanged
.cursor/hooks.json
.cursor/hooks/gates.py
.cursor/skills/adopt-harness/   this skill, so later sessions can extend the install
scripts/init.sh
scripts/knowledge_index.py
scripts/__init__.py
docs/work/0000-template.md
docs/decisions/0000-template.md
docs/knowledge/README.md
docs/knowledge/README.es.md
LICENSE                         add it only when the target has no license
```

Copy `tests/test_gates.py` and `tests/test_knowledge_index.py` when the target
should keep the harness under test. Point `test_repo_examples_are_findable` at
one of the target's own knowledge docs.

Leave `docs/concepts/` and `docs/decisions/0001` through `0007` here. They
explain this repo. Copy them only if the user wants the rationale inside the
target.

Then fill the blocks in the target:

| File | Block | Put here |
|---|---|---|
| `AGENTS.md` | the four `PROJECT` blocks | what the project does, exact commands, human gates, code rules |
| `scripts/init.sh` | `PROJECT CONFIG` | `TOOLS`, `TEST_CMD`, `PROJECT_FILES` |
| `.cursor/hooks/gates.py` | the `GATES` tuple | the shell gates named in `AGENTS.md`, one regex and a name each |

`AGENTS.md` commands and `TEST_CMD` must be the same command. If the target
already has `scripts/`, keep the copied scripts and fix the paths in `init.sh`
and `AGENTS.md`. `knowledge_index.py` reads `docs/knowledge/` from the repo root.

Replace `.cursor/skills/example/` with one skill for the area the project
touches most. Description starts with "Use when" and names a path or an action.

Seed `docs/knowledge/` with three or four entities that show up in most tasks.
One file per entity, flat frontmatter (`id`, `status`, `verified`), one `## `
section per topic, every fact with a source or the word "unverified". Delete
`docs/knowledge/entities/order.md` and `customer.md` from the target: they are
samples from a fictional store.

## B. Start a new project from this repo

1. Fork https://github.com/AbdielFco/why-harness (the repo must be public for the Fork button), or clone it and point `origin` at the new remote.
2. Keep `LICENSE`, the five agents, the hook, `scripts/`, and `tests/`.
3. Fill the same three blocks as in A.
4. Replace the sample knowledge (`entities/order.md`, `entities/customer.md`) and `.cursor/skills/example/` with the project's own.
5. Keep `docs/concepts/` and `docs/decisions/`: they are why the structure exists.

## Verify

Run these in the target, from its root.

```bash
./scripts/init.sh                                              # every line [OK], exit 0
echo '{"command":"git push"}' | python3 .cursor/hooks/gates.py # permission ask
echo 'not json' | python3 .cursor/hooks/gates.py               # permission deny
python3 -m scripts.knowledge_index search "<one of your entities>"
```

Open the target as its own Cursor workspace. A parent workspace does not load a nested `hooks.json`.

## Done when

- [ ] The five agents are byte-for-byte the originals
- [ ] `PROJECT`, `PROJECT CONFIG`, and `GATES` describe the target, and the test command matches in both places
- [ ] One real skill exists, and `example/` is gone
- [ ] Knowledge has real entities and no sample store docs
- [ ] `LICENSE` is present
- [ ] The four verify commands behave as written

## Do not

- Put project rules inside an agent. A missing rule is a context gap: it goes to `AGENTS.md`, a skill, or `docs/knowledge/`.
- Grow `AGENTS.md` with area-specific rules. Those go in a skill.
- Drop the copyright notice when copying files out of this repo.
