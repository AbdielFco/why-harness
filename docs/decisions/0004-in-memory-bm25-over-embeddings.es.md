# 0004: BM25 en memoria en lugar de embeddings

[English](0004-in-memory-bm25-over-embeddings.md) | **Español**

- Estado: aceptada
- Fecha: 2026-11-19

## Contexto

El agente necesita encontrar un hecho sin abrir archivos enteros. Las opciones habituales son búsqueda vectorial (embeddings) o léxica.

## Decisión

`scripts/knowledge_index.py`: BM25 sobre fragmentos (uno por `## `), índice construido en memoria en cada llamada, solo stdlib. Devuelve `path:line heading score`.

## Alternativas

| Opción | Por qué no |
|---|---|
| Embeddings + base vectorial | Dependencias, índice que regenerar y que se desfasa, resultados no deterministas |
| Índice BM25 commiteado | Se desfasa de los docs y obliga a regenerarlo |
| Solo `grep` | Sin ranking; sin nombre exacto devuelve demasiado o nada |

## Consecuencias

Determinista y testeable, sin dependencias. No entiende sinónimos. Revisar si el corpus pasa de miles de documentos o las consultas dejan de usar los términos de los docs.
