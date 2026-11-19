# 0002: Planner y reviewer readonly

[English](0002-readonly-planner-and-reviewer.md) | **Español**

- Estado: aceptada
- Fecha: 2026-11-19

## Contexto

Un agente que puede editar tiende a hacerlo: el planner "aprovecha" para arreglar, el reviewer "corrige rápido" en lugar de reportar. En ambos casos el humano pierde el punto de control.

## Decisión

`planner` y `reviewer` se declaran `readonly: true`. El validator ejecuta comandos pero no edita código ni docs.

## Alternativas

| Opción | Por qué no |
|---|---|
| Instrucción "no edites" sin readonly | Es una sugerencia; el permiso es una garantía |
| Reviewer que corrige | Se convierte en un segundo implementer sin plan ni test |

## Consecuencias

Cada corrección pasa por el implementer y queda dentro del plan. Depende de que la herramienta respete `readonly`.
