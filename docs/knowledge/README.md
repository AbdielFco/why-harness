# Knowledge base

**English** | [Español](README.es.md)

Domain facts: what each entity is, where each datum comes from, and which rules apply. Code says *how*; this says *what is true* and *how we know*.

Why it exists and how search works: [concepts/knowledge-base](../concepts/knowledge-base.md) (in Spanish).

## Layout

```
docs/knowledge/
├── README.md                    this file: format and the list of collections
└── <collection>/<entity>.md     one file per entity
```

The project chooses its collections (`entities/`, `sources/`, `rules/`, ...). The examples in this repo use `entities/` with a fictional store domain, and their body is in Spanish.

## File format

```markdown
---
id: order
status: active
verified: 2026-11-19
---
# Order

## What it is
## Source
## Rules
## Notes
```

### Frontmatter

Flat (`key: value`), first in the file. No lists and no nesting.

| Key | Required | Values |
|---|---|---|
| `id` | yes | Stable identifier, the same one the code uses |
| `status` | yes | `active`, `deprecated`, `draft` |
| `verified` | yes | Date `YYYY-MM-DD` of the last check against the source, or `none` |

The project adds whatever keys it needs (`source`, `owner`, `code`, ...). A value that does not apply is `none`.

### Body

- One `## ` section per topic. Each section is a search fragment: short, with a heading that says what it holds.
- Every fact carries its source: a link, a `path:line`, or a command. What could not be checked says "unverified".
- When an entity has two names (one in code, one in the business), write both: the search does not understand synonyms.

## Search

```bash
rg "id: order" docs/knowledge                        # exact id
python3 -m scripts.knowledge_index search "order"    # by relevance
```

## Collections

| Collection | Holds |
|---|---|
| [entities/](entities/) | Examples: [order](entities/order.md), [customer](entities/customer.md) |
