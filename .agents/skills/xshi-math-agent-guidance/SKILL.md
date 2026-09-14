---
name: xshi-math-agent-guidance
description: Maintain xshi-math agent guidance. Use when changing AGENTS.md, ARCHITECTURE.md, docs/design/AGENT_FRAMEWORK.md, docs/design/AGENT_HARNESS_MIGRATION.md, docs/rules/, or .agents/skills/, especially routing, stable rules, repeatable workflows, skill metadata, and guidance cleanup.
---

# xshi-math Agent Guidance

Use this skill when changing `AGENTS.md`, `ARCHITECTURE.md`,
`docs/design/AGENT_FRAMEWORK.md`, `docs/design/AGENT_HARNESS_MIGRATION.md`,
`docs/rules/`, or `.agents/skills/`.

## Inputs

- The behavior or confusion that motivated the guidance change.
- The current relevant guidance files.
- Any source files or docs that changed the project reality.

## Workflow

1. Read `docs/design/AGENT_FRAMEWORK.md` and
   `docs/design/AGENT_HARNESS_MIGRATION.md`.
2. Classify the change:
   - route → `AGENTS.md` or a track `content/*/AGENTS.md`;
   - map or invariant → `ARCHITECTURE.md`;
   - rationale → `docs/design/`;
   - stable constraint → `docs/rules/`;
   - repeatable workflow → `.agents/skills/<name>/SKILL.md`;
   - skill metadata → `.agents/skills/<name>/agents/openai.yaml`.
3. Search for overlapping guidance before adding new text.
4. Prefer editing the narrowest existing file. Keep skills only under
   `.agents/skills/` (never `.cursor/skills/`).
5. Add task triggers and completion checks where useful.
6. For skills, keep `SKILL.md` concise, include only `name` and `description`
   in frontmatter, and make the description carry the trigger. Prefer the
   `xshi-math-` name prefix.
7. Update indexes or routers only when future agents need discovery.
8. Check links and paths. Do not duplicate rule text inside skills or adapters.

## Completion Check

The guidance update is not done until:

- it has a clear trigger;
- it does not duplicate nearby guidance;
- it points to the right source of truth;
- it keeps `AGENTS.md` short;
- it reports any deferred cleanup.
