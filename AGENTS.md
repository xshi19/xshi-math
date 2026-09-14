# Agent Router

This repository contains a MyST/Python foundation for mathematical notes across
three subsites (Incerto, Information Geometry, Normix theory) plus a landing
page. Read [README.md](README.md) and [ARCHITECTURE.md](ARCHITECTURE.md) for
scope. MIT applies to repository-owned material. The
[planning index](docs/plan/index.md) records completed gates; files still
described as proposed do not yet exist.

## Model selection

Before coding or command-execution tasks in this portfolio, ask the owner to
choose a model unless they have already named one for the task or session:

- Cursor Grok 4.6 xhigh.
- Cursor Fable 5.1 high.
- Codex GPT-6-Astra xhigh (recommended; Codex is the primary client).

Honor an existing choice without asking again. Cursor quota may be exhausted;
do not assume it is available or silently switch the owner's selected model.
The active [Codex defaults](.codex/config.toml) select `gpt-6-astra` with `xhigh`;
they do not replace the owner choice when none has been supplied. See the
[framework](docs/design/AGENT_FRAMEWORK.md#model-selection-policy) for rationale.

## Read only what the task needs

| Task | Read next |
| --- | --- |
| Roadmap, current phase, unresolved decisions | [Planning index](docs/plan/index.md) |
| Repository boundaries, tracks, URLs, deployment | [Consolidation plan](docs/plan/consolidation.md) |
| Agent instructions, rules, skills, client configuration | [Agent framework](docs/design/AGENT_FRAMEWORK.md) |
| Harness migration, port decisions, day-to-day read order | [Harness migration](docs/design/AGENT_HARNESS_MIGRATION.md) |
| Licensing, source reuse, private-to-public preparation | [License advice](docs/design/LICENSE_ADVICE.md) |
| Locate a task-specific rule | [Rule index](docs/rules/index.md) |

Before changing a subtree, inspect any more specific `AGENTS.md` along its path.
When working from the repo root, explicitly read applicable nested guidance;
do not assume a client has loaded instructions below its starting directory.

Day-to-day load order: this router → track `AGENTS.md` if editing a track → one
relevant rule → one skill → touched sources. Details:
[harness read order](docs/design/AGENT_HARNESS_MIGRATION.md#day-to-day-harness-read-order).

## Skills (`.agents/skills/`)

Canonical skills live only in `.agents/skills/` (no `.cursor/skills/` mirror).

| Trigger | Skill |
| --- | --- |
| Math-content question before editing | `$xshi-math-math-question` |
| Create or substantially revise a note | `$xshi-math-concept-page` |
| Theorem / proof scoping | `$xshi-math-proof-writing` |
| Semantics-preserving prose pass | `$xshi-math-prose-review` |
| AI-pattern scrub / writing registers | `$xshi-math-unslop` |
| Git commit, branch, push, PR | `$xshi-math-git-conventions` |
| Maintain routers, rules, or skills | `$xshi-math-agent-guidance` |
| Rebuild site / optional hub `/math/` transfer | `$xshi-math-hub-publish` |

Deferred: reading-guide, lean-formalization, deep-math (P2); Cursor `.mdc`
adapters (P1). Normix package `docs-publish` stays upstream.

## Working boundaries

- Follow the user's task scope. A future phase in a plan is not an instruction
  to execute that phase. Foundation work does not authorize content migration.
- Preserve the [Normix boundary](docs/plan/consolidation.md#repository-boundaries).
- Keep durable decisions in the repository. Use links to canonical guidance;
  load rules and recipes only for the task they govern.
- Preserve assumptions, notation, attribution, and the distinction between
  proof and numerical evidence when editing mathematical prose.
- **Shared notation canon:** reuse symbols from
  [content/notation.md](content/notation.md) (public URL `/math/notation/`).
  See [shared-notation rule](docs/rules/shared-notation.md). New math notes must
  not invent parallel symbols for the same concept across tracks.

## Verification commands

- Install/test: `uv sync --locked`, then `uv run pytest`.
- Demo: `uv run python demos/incerto/exceedances.py`.
- Packaging: `uv build`; verify editable and wheel imports when mapping changes.
- Site: `npm ci`, `npm run build`, then `npm run check:html`.
- Review rendered equations, links, and desktop/mobile navigation under `/math/`.

See [README](README.md) for preview commands and the
[verification record](docs/records/phase-0-1-verification.md) for current limits.
There is no Lean project or CI workflow.

## Completion in the current phase

Review the diff and the full contents of new files; `git diff` alone omits
untracked files. Check relative links, factual citations, scope, and consistency
between current state and proposals. Run `git diff --check` and check new files
for whitespace errors separately. Run the checks relevant to changed artifacts;
record blocked checks without calling an unverified build complete.

Report changed files, verification actually performed, checks not run, and any
remaining limitations. Report Git state accurately; a written file is not a
commit, and a proposed verification contract is not passing CI.
