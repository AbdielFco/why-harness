# 0006: Agentes invariantes y tres capas de proyecto

- Estado: aceptada
- Fecha: 2026-11-19

## Contexto

En la implementación de origen, los agentes nombraban la skill, el tipo de dato, el comando de tests y la ruta de fixtures del proyecto. Instalarlos en otro proyecto obligaba a reescribirlos todos.

## Decisión

Agentes, hook, `init.sh` y buscador no contienen nada del proyecto. Lo propio del proyecto vive en tres capas: `AGENTS.md` (reglas y comandos), skills (cómo se escribe código), `docs/knowledge/` (hechos). Más dos bloques marcados: `GATES` y `PROJECT CONFIG`.

## Alternativas

| Opción | Por qué no |
|---|---|
| Agentes por proyecto | Cada proyecto mantiene su fork; las mejoras no se comparten |
| Un archivo de config que los agentes lean | Cuarta capa que duplica `AGENTS.md` |

## Consecuencias

Los agentes se actualizan copiándolos. Los comandos viven en dos lugares (`AGENTS.md` y `init.sh`); el reviewer y `adopt.md` piden que coincidan.
