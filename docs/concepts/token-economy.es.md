# Economía de tokens

[English](token-economy.md) | **Español**

## Qué es

El conjunto de técnicas que reducen los tokens que entran a la ventana del modelo **sin reducir la calidad**. Muchas veces la calidad sube, porque menos ruido es más atención para lo que importa.

## Por qué existe

- Cada turno reenvía el contexto acumulado. Un archivo leído al principio se paga en cada turno siguiente.
- La calidad cae con el ruido antes de llegar al límite de la ventana.
- Tokens son dinero y latencia.

## Las ocho técnicas

| # | Técnica | Pieza | Zona | Qué evita |
|---|---|---|---|---|
| 1 | Entrada corta que enlaza | `AGENTS.md` | siempre | Pagar en cada turno reglas que la tarea no usa |
| 2 | Divulgación progresiva | skills | a demanda | Cargar el cómo de diez áreas para tocar una |
| 3 | Resultados `path:line` | `knowledge_index.py` | a demanda | Abrir archivos enteros para encontrar un dato |
| 4 | Subagentes con reporte fijo | `.cursor/agents/` | aislado | Que las lecturas de una etapa llenen la sesión principal |
| 5 | Gates en código | `gates.py` | cero | Reglas de permiso en el prompt de cada turno |
| 6 | Fallar temprano | `init.sh` | cero | Una sesión entera sobre un entorno roto |
| 7 | Memoria en disco + cambio de sesión | work file | a demanda | Arrastrar un contexto degradado |
| 8 | Fuera del índice | `.cursorignore` | cero | Secretos y artefactos generados en búsquedas |

## Cómo funciona: un ejemplo

Tarea: "corregir el cálculo del total de una orden".

**Sin harness:** el agente abre el módulo de órdenes (400 líneas), los tests (300), dos archivos de utilidades (250), busca "total" en todo el repo y abre tres resultados más. Escribe el fix y el test. Revisa su propio trabajo con todo eso en contexto. Al día siguiente, en otra sesión, vuelve a leer todo para recordar dónde quedó.

**Con harness:**

1. `AGENTS.md` (~80 líneas) y las `description` de las skills ya están cargados.
2. El planner, en su propia ventana, busca `"total orden"` y obtiene `docs/knowledge/entities/order.md:12 Reglas`. Lee esa sección y los dos archivos de código que importan. Devuelve un plan de 30 líneas.
3. La sesión principal solo recibe esas 30 líneas.
4. test-writer, implementer y validator trabajan aislados; cada uno devuelve su reporte.
5. El reviewer recibe el diff, no la historia.
6. Al día siguiente: `AGENTS.md` + work file y se sigue desde "Remaining".

La sesión principal nunca vio los archivos completos. Lo que vio fueron planes, reportes y un diff.

## Coste en contexto

Lo que el harness cobra siempre: `AGENTS.md` y una `description` por skill. Todo lo demás es a demanda, aislado o cero.

## Límites

- El total de tokens del carril normal (sumando subagentes) puede ser mayor que el de un solo agente. Lo que baja es el contexto de la sesión principal y el retrabajo.
- El agente puede ignorar `path:line` y leer el archivo entero. El harness guía, no obliga.

## Cómo adaptarlo

Para cada regla nueva, elige la zona más barata que funcione: código (cero), subagente (aislado), skill o knowledge (a demanda), y solo al final `AGENTS.md` (siempre).
