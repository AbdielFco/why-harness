# Glosario

| Término | Significado |
|---|---|
| **Harness** | Todo lo que rodea al modelo: entrada, reglas, herramientas, gates, verificación y memoria. Ver [harness](harness.md). |
| **Ventana de contexto** | Los tokens que el modelo ve en un turno. Finita, y se reenvía completa en cada turno. |
| **Context engineering** | Decidir qué entra a la ventana, cuándo y cuándo sale. |
| **Context base** | Lo que el agente necesita para trabajar en el repo: `AGENTS.md` y skills. |
| **Knowledge base** | Hechos del dominio con su fuente: `docs/knowledge/`. |
| **Memoria** | Lo que sobrevive a una sesión: work file, decisiones, knowledge. |
| **Orquestador** | La sesión principal. Coordina subagentes y es el único que escribe el work file. |
| **Subagente** | Instancia del modelo con ventana propia, un rol y un permiso. Devuelve un reporte. |
| **Readonly** | Subagente que no puede editar archivos (planner, reviewer). |
| **Pipeline** | Orden fijo de etapas: planner, aprobación, test-writer, implementer, validator, reviewer. |
| **Carril** | Rápido (docs, typos) o normal (lógica). Define qué etapas corren. |
| **Gate** | Checklist verificable de un agente, o acción que requiere un sí humano. |
| **Gate humano** | Acción que necesita aprobación explícita: commit, push, borrar, dependencias, deploy. |
| **Hook** | Script que la herramienta corre ante un evento del agente. Aquí, antes de cada comando de shell. |
| **Fail-closed** | Ante un error o una entrada ilegible, denegar. Lo contrario, fail-open, permitir. |
| **Skill** | `SKILL.md` con una `description` siempre cargada y un cuerpo leído a demanda. |
| **Divulgación progresiva** | Mostrar que algo existe con poco coste y cargar el detalle solo cuando hace falta. |
| **Trigger** | La `description` de una skill: decide cuándo se lee el cuerpo. |
| **Work file** | `docs/work/<TICKET>.md`. Estado de la tarea activa. |
| **ADR** | Architecture Decision Record. Un archivo por decisión con contexto, decisión y consecuencias. |
| **Context gap** | Lo que le faltó a un agente para cumplir, y la capa donde debe ir. |
| **Capas del proyecto** | `AGENTS.md` (reglas), skills (cómo), knowledge (qué). Lo único que cambia entre proyectos. |
| **Invariante** | Pieza que se copia sin editar: agentes, hook, `init.sh`, buscador. |
| **BM25** | Ranking de recuperación de información basado en frecuencia del término, rareza y longitud. |
| **Chunk** | Fragmento indexado: una sección `## ` de un doc de knowledge. |
| **Fallar temprano** | Detectar un entorno roto antes de gastar la sesión: `init.sh`. |
