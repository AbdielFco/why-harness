# 0007: Context gap como retroalimentación

- Estado: aceptada
- Fecha: 2026-11-19

## Contexto

Los agentes reportaban qué les faltó, pero ningún paso convertía ese reporte en un cambio. El mismo hueco se pagaba en cada tarea.

## Decisión

Cada reporte nombra la capa del gap (`AGENTS.md`, skill, knowledge). El orquestador lo anota en el work file, y al cerrar la tarea lo aplica a esa capa. Ningún gap se aplica editando un agente.

## Alternativas

| Opción | Por qué no |
|---|---|
| Gaps sin dueño | Se reportan y se olvidan |
| Aplicarlos en el momento | Interrumpe la tarea y mezcla cambios de harness con el cambio de código |

## Consecuencias

El harness mejora con cada tarea. Aplicar gaps sin criterio infla `AGENTS.md`; la regla es preferir la capa a demanda.
