# Docs

[English](README.md) | **Español**

Índice. El contenido está en cada carpeta.

| Carpeta | Qué contiene | Cuándo leerla |
|---|---|---|
| [concepts/](concepts/) | Qué es cada pieza, por qué existe, cómo funciona | Para entender o modificar el harness |
| [decisions/](decisions/) | ADRs: por qué el harness es así y no de otra forma | Antes de cambiar una pieza |
| [knowledge/](knowledge/README.es.md) | Hechos del dominio, con fuente | Cualquier cambio que dependa de un dato |
| [work/](work/0000-template.md) | Memoria de la tarea activa. Se borra al cerrar | Al empezar y al cerrar cada fase |
| [adopt.md](adopt.md) | Cómo instalar el harness en un proyecto | Una vez, al adoptarlo |

## Conceptos

| Doc | En una línea |
|---|---|
| [harness](concepts/harness.md) | Agente = modelo + harness |
| [context-engineering](concepts/context-engineering.md) | La ventana como presupuesto, en cuatro zonas |
| [knowledge-base](concepts/knowledge-base.md) | Hechos con fuente, buscados por fragmento |
| [agents-and-subagents](concepts/agents-and-subagents.md) | Un agente por sesgo que evitar |
| [pipeline-and-lanes](concepts/pipeline-and-lanes.md) | Orden fijo, dos carriles, a dónde vuelve cada FAIL |
| [hooks](concepts/hooks.md) | Lo verificable con código no se le pide al modelo |
| [skills](concepts/skills.md) | Divulgación progresiva |
| [memory-and-sessions](concepts/memory-and-sessions.md) | Memoria en disco y cuándo empezar limpio |
| [feedback-loop](concepts/feedback-loop.md) | El context gap hace que el harness aprenda |
| [token-economy](concepts/token-economy.md) | Las ocho técnicas en una tabla |
| [portability](concepts/portability.md) | Las mismas piezas en otras herramientas |
| [glossary](concepts/glossary.md) | Términos |

Buscar en la knowledge: `python3 -m scripts.knowledge_index search "<consulta>"`.
Con un id exacto, buscar el texto directamente bajo `knowledge/`.
