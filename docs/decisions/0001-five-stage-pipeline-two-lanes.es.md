# 0001: Pipeline de cinco etapas con dos carriles

[English](0001-five-stage-pipeline-two-lanes.md) | **Español**

- Estado: aceptada
- Fecha: 2026-11-19

## Contexto

Un solo agente que planifica, prueba, implementa y revisa edita antes de entender y se autoaprueba. Pero pasar cada cambio por todas las etapas gasta tokens en cambios sin riesgo (typos, docs).

## Decisión

Carril normal: planner -> aprobación humana -> test-writer -> implementer -> validator -> reviewer.
Carril rápido (docs, typos, config sin lógica): orquestador -> reviewer.
Ante la duda, carril normal.

## Alternativas

| Opción | Por qué no |
|---|---|
| Un solo agente | Sesgo de autor, contexto contaminado al revisar |
| Pipeline único para todo | Cinco etapas para un typo |
| Tres etapas (plan, implementar, revisar) | Pierde el test escrito antes y separado de la implementación, y la evidencia dinámica separada del juicio estático |

## Consecuencias

Más tokens totales en el carril normal, menos contexto en la sesión principal y menos retrabajo. La clasificación de carril puede fallar; el reviewer corre en ambos.
