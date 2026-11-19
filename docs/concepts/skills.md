# Skills

**English** | [Español](skills.es.md)

## What it is

A **skill** is a `SKILL.md` file in `.cursor/skills/<name>/` with two parts:

- **frontmatter** with `name` and `description`. The `description` is **always** in context: it is the trigger.
- **body** with the operational knowledge: patterns, layout, typical mistakes. It is read **only** when the `description` matches the task.

This is **progressive disclosure**. The agent knows something exists from one line, and pays for the rest only when it needs it.

## Why it exists

The alternative is to put everything in `AGENTS.md`. With ten areas of code, each with its own rules, `AGENTS.md` grows to hundreds of lines paid on every turn even when the task touches one area.

| | Everything in AGENTS.md | Skills |
|---|---|---|
| Cost per turn | Every rule | One `description` per skill |
| Cost when used | The same | Plus the body of one skill |
| Scales with | The number of areas, always | The number of areas touched |

## How it works here

`.cursor/skills/example/SKILL.md` is the template. Agents use it like this:

1. The planner reads the skill whose `description` matches the change and names it in the plan.
2. The test-writer and the implementer read the skill the plan names.
3. When a skill misled the agent or lacked a section, the report says so under "Context gap: skill".

## What goes in a skill

| Goes in the skill | Goes somewhere else |
|---|---|
| How a module is structured here | What a domain datum means: knowledge |
| The error and logging pattern | Test and build commands: `AGENTS.md` |
| Typical mistakes and how to avoid them | Why something was decided: decisions |

## Writing a good description

- Start with "Use when" and name a concrete trigger: a path, a file type, an action.
- Say in one sentence what the body covers, so the agent can decide without opening it.
- One skill per area. A skill that triggers on everything costs tokens on everything.

Weak: `description: Coding guidelines.`
Strong: `description: Use when adding or changing an HTTP endpoint under api/. Covers routing, input validation, error responses and where the test goes.`

## Cost in context

A `description` costs 30 to 60 tokens per turn. The body costs tokens only when it is used.

## Limits

- The model decides the match. An ambiguous `description` can fire too often or not often enough.
- A skill is not mandatory. A rule that must not fail belongs in the hook or in a test.

## How to adapt it

Delete `example/` and create one skill per area of your project. Start with one: the area you touch most.
