# AGENTS.md

`xshi-math` is Xiang Shi's public math-notes monorepo. Right now it holds
**plans and harness design only**. No tracks, packages, or site build have
been migrated.

Use this file as a router. Load the smallest relevant doc.

## Start here

- Roadmap: `docs/plan/index.md`
- Consolidation (layout, migrate vs stay, hub, URLs, phases): `docs/plan/consolidation.md`
- Dual Codex + Cursor harness: `docs/design/AGENT_FRAMEWORK.md`
- License decision: `docs/design/LICENSE_ADVICE.md`
- Rules index (placeholder): `docs/rules/index.md`
- Canonical skills (none yet): `.agents/skills/`

`ARCHITECTURE.md` does not exist until the scaffold phase.

## Load by task

- Changing the cutover sequence, URLs, or repo tree: `docs/plan/consolidation.md`.
- Changing skills, rules, adapters, or nested `AGENTS.md` policy: `docs/design/AGENT_FRAMEWORK.md` and `docs/rules/index.md`.
- License / NOTICE / CITATION: `docs/design/LICENSE_ADVICE.md`.
- Git commit or PR work: keep diffs to the files the task named; do not
  invent packages, CI, or migrated content.

## Current constraints

- Do not copy content from `incerto-wiki` or `normix`.
- Do not add workflows that claim to build tracks that are not here.
- Do not vendor the `normix` JAX package. Theory pages may depend on a
  published install later.
- Do not duplicate skill bodies into `.cursor/skills/`. Canonical path is
  `.agents/skills/` when skills are added.
- Canonical rules will live in `docs/rules/*.md`. `.cursor/rules/*.mdc`
  adapters stay thin.
- Keep this file as a map (~100 lines). Put detail in `docs/`.

## Verification

There is no site or package test suite yet.

- Planning edits: check internal Markdown links and that open questions
  stay marked `Open question:`.
- When content exists, use the contracts in `docs/design/AGENT_FRAMEWORK.md`
  (MyST build, pytest, `lake build`, prose review).
