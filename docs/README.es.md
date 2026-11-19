# Docs

[English](README.md) | **Español**

Índice. El contenido está en cada carpeta.

| Carpeta | Qué contiene | Cuándo leerla |
|---|---|---|
| [concepts/](concepts/harness.es.md) | Qué es cada pieza, por qué existe, cómo funciona | Para entender o modificar el harness |
| [decisions/](decisions/0001-five-stage-pipeline-two-lanes.es.md) | ADRs: por qué el harness es así y no de otra forma | Antes de cambiar una pieza |
| [knowledge/](knowledge/README.es.md) | Hechos del dominio, con fuente | Cualquier cambio que dependa de un dato |
| [work/](work/0000-template.es.md) | Memoria de la tarea activa. Se borra al cerrar | Al empezar y al cerrar cada fase |
| [adopt.es.md](adopt.es.md) | Cómo instalar el harness en un proyecto | Una vez, al adoptarlo |
| [references.es.md](references.es.md) | Fuentes de investigación detrás de cada decisión | Al preguntar por qué existe una pieza |

## Conceptos

| Doc | En una línea |
|---|---|
| [harness](concepts/harness.es.md) | Agente = modelo + harness |
| [context-engineering](concepts/context-engineering.es.md) | La ventana como presupuesto, en cuatro zonas |
| [knowledge-base](concepts/knowledge-base.es.md) | Hechos con fuente, buscados por fragmento |
| [agents-and-subagents](concepts/agents-and-subagents.es.md) | Un agente por sesgo que evitar |
| [pipeline-and-lanes](concepts/pipeline-and-lanes.es.md) | Orden fijo, dos carriles, a dónde vuelve cada FAIL |
| [hooks](concepts/hooks.es.md) | Lo verificable con código no se le pide al modelo |
| [skills](concepts/skills.es.md) | Divulgación progresiva |
| [memory-and-sessions](concepts/memory-and-sessions.es.md) | Memoria en disco y cuándo empezar limpio |
| [feedback-loop](concepts/feedback-loop.es.md) | El context gap hace que el harness aprenda |
| [token-economy](concepts/token-economy.es.md) | Las ocho técnicas en una tabla |
| [portability](concepts/portability.es.md) | Las mismas piezas en otras herramientas |
| [glossary](concepts/glossary.es.md) | Términos |

El archivo sin sufijo es la versión en inglés. Esta página enlaza la versión en español.

Buscar en la knowledge: `python3 -m scripts.knowledge_index search "<consulta>"`.
Con un id exacto, buscar el texto directamente bajo `knowledge/`.
