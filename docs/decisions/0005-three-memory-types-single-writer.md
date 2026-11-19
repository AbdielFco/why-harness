# 0005: Tres tipos de memoria con un solo escritor

- Estado: aceptada
- Fecha: 2026-11-19

## Contexto

La conversación se compacta y se pierde entre sesiones. Una cuarta carpeta de investigaciones competía con decisiones y knowledge, y no quedaba claro dónde buscar. Varios agentes escribiendo el mismo archivo de estado producían contradicciones.

## Decisión

Tres tipos: tarea (`docs/work/`, se borra al cerrar), decisión (`docs/decisions/`, permanente), hecho (`docs/knowledge/`, permanente). Solo el orquestador escribe el work file; los subagentes devuelven reportes.

## Alternativas

| Opción | Por qué no |
|---|---|
| Memoria solo en la conversación | Se pierde al compactar o cambiar de sesión |
| Carpeta de investigaciones | Lo que vale termina siendo hecho o decisión |
| Cada subagente escribe su sección | Estados contradictorios, conflictos de edición |

## Consecuencias

Cambiar de sesión es barato. El orquestador puede olvidar actualizar el work file; el reviewer lo verifica.
