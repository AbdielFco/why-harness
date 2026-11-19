# 0003: Hook de shell fail-closed

- Estado: aceptada
- Fecha: 2026-11-19

## Contexto

Las acciones irreversibles (push, borrar, deploy, cambiar dependencias) son un comando más para el agente. Una regla en el prompt cuesta tokens en cada turno y puede ignorarse.

## Decisión

`beforeShellExecution` corre `gates.py`. Si un regex de `GATES` coincide, responde `ask`. Si el payload no se puede leer, `deny`. `hooks.json` declara `failClosed: true`, así que si el script falla, el comando no corre.

## Alternativas

| Opción | Por qué no |
|---|---|
| Solo reglas en `AGENTS.md` | No son obligatorias y cuestan tokens siempre |
| Fail-open ante error | Un hook roto desactivaría todos los frenos sin aviso |
| `deny` para todo gate | Bloquea trabajo legítimo; `ask` deja decidir al humano |

## Consecuencias

Cero tokens, testeable. Solo ve texto de shell: ediciones de archivo y escrituras dentro de procesos siguen dependiendo de `AGENTS.md`. Produce falsos positivos a propósito.
