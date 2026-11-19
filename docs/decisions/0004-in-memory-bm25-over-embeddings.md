# 0004: In-memory BM25 instead of embeddings

**English** | [Español](0004-in-memory-bm25-over-embeddings.es.md)

- Status: accepted
- Date: 2026-11-19

## Context

The agent needs to find a fact without opening whole files. The usual options are vector search (embeddings) or lexical search.

## Decision

`scripts/knowledge_index.py`: BM25 over fragments (one per `## `), an index built in memory on every call, stdlib only. It returns `path:line heading score`.

## Alternatives

| Option | Why not |
|---|---|
| Embeddings plus a vector database | Dependencies, an index to regenerate that drifts, non-deterministic results |
| A committed BM25 index | It drifts from the docs and has to be regenerated |
| `grep` only | No ranking. Without an exact name it returns too much or nothing |

## Consequences

Deterministic and testable, with no dependencies. It does not understand synonyms. Revisit this if the corpus passes thousands of documents, or queries stop using the words in the docs.
