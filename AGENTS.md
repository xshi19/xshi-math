# Agent Router

Edit the mathematical notes in `content/`, the sole authoring source for the
Incerto, Information Geometry, and Normix theory subsites. The build generates
`_build/`. The hub publishes the assembled `_build/html/` under `/math/`.
Read [README.md](README.md) and [ARCHITECTURE.md](ARCHITECTURE.md) for scope.
MIT applies to repository-owned material. The
[planning index](docs/plan/index.md) records completed gates; files still
described as proposed do not yet exist.

## Model selection

For writing and review, the default is Codex `gpt-6.2-astra` at `xhigh`
reasoning, as set in the [project configuration](.codex/config.toml). Honor
an already named model for the task or session. Never ask which model to use.
When the Codex quota is exhausted, use Antigravity CLI (`agy`) with
`gemini-4-neon-high`. Run `agy -p "..." --model gemini-4-neon-high --output-format json`
from the repo root or a throwaway worktree. Add `--mode plan` for read-only
tasks. When commands are needed, whitelist them in `permissions.allow`.
Use `--dangerously-skip-permissions` only in throwaway copies. Check
`agy -p "/usage" --output-format json` before and after each run.
Never use Claude or Opus models inside agy.

See the [framework](docs/design/AGENT_FRAMEWORK.md#model-selection-policy)
for rationale.

## Read only what the task needs

| Task | Read next |
| --- | --- |
| Editing `content/ig/` | [Information Geometry track instructions](content/ig/AGENTS.md) |
| Editing `content/incerto/` | [Incerto track instructions](content/incerto/AGENTS.md) |
| Editing `content/normix-theory/` | [Normix theory track instructions](content/normix-theory/AGENTS.md) |
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

Repo skills live only in `.agents/skills/` (no `.cursor/skills/` mirror).

| Trigger | Skill |
| --- | --- |
| Math-content question before editing | `$math-question` |
| Create or substantially revise a note | `$concept-page` |
| Theorem / proof scoping | `$proof-writing` |
| Semantics-preserving prose pass | `$prose-review` |
| AI-pattern scrub / writing registers | `$unslop` |
| Git commit, branch, push, PR | `$git-conventions` |
| Maintain routers, rules, or skills | `$agent-guidance` |
| Rebuild site / optional hub `/math/` transfer | `$hub-publish` |
| Source→concept reading map | `$reading-guide` |
| Lean scoping / future formalization | `$lean-formalization` |
| Hard external math consult (GPT-5.5 pro) | `$deep-math-agent` |

Cursor thin adapters live under `.cursor/rules/*.mdc` (metadata + pointers only).
Normix package `docs-publish` stays upstream. The optional Lean prototype lives in `formalization/incerto-lean/`; see its README for checked scope.

## Working boundaries

- Follow the user's task scope. A future phase in a plan is not an instruction
  to execute that phase. Cleanup does not authorize deferred content imports.
- Preserve the [Normix boundary](docs/plan/consolidation.md#repository-boundaries).
- For hub updates, use `$hub-publish` and the
  [cutover runbook](docs/plan/phase-4-cutover-runbook.md); preserve the live
  `/incerto-wiki/` mirror and compatibility pages alongside `/math/`.
- Keep durable decisions in the repository. Use links to canonical guidance;
  load rules and recipes only for the task they govern.
- Preserve assumptions, notation, attribution, and the distinction between
  proof and numerical evidence when editing mathematical prose.
- **Shared notation canon:** reuse symbols from
  [content/notation.md](content/notation.md) (public URL `/math/notation/`).
  See [shared-notation rule](docs/rules/shared-notation.md). New math notes must
  not invent parallel symbols for the same concept across tracks.
- **Notation review:** follow the [audit integration](docs/rules/notation-economy.md)
  for the external `math-notation` skill and its installation.
- **Proof structure:** follow the [site integration](docs/rules/statement-before-proof.md)
  for the external `$statement-before-proof` skill, MyST markup, and report checker.

## Verification commands

Run these commands from the repository root.

- For package behavior, run `uv sync --locked`, then `uv run pytest`.
- Demo: `uv run python demos/incerto/exceedances.py`.
- Packaging: `uv build`; verify editable and wheel imports when mapping changes.
- Bibliography: `bib/` is a submodule of private `xshi19/bibliography`; run
  `git submodule update --init` first. Add new entries there, not here, then
  bump the submodule pointer.
- For site output, run `npm ci` the first time, then `npm run build` followed by `npm run check:html`.
- Separately inspect rendered equations, links, and desktop/mobile navigation under `/math/`.

See [README](README.md) for preview commands and the
[planning index](docs/plan/index.md) for current verification and remaining gates.
The [leak-check workflow](.github/workflows/leak-check.yml) scans pull requests
and pushes to `main` or `master`. The optional Lean prototype was checked upstream on
2026-09-05 with Lean/Mathlib v4.19.0, not rechecked here. To check it separately:
`cd formalization/incerto-lean && lake build` (requires the pinned toolchain/cache).

## Completion in the current phase

Review the diff and the full contents of new files; `git diff` alone omits
untracked files. Check relative links, factual citations, scope, and consistency
between current state and proposals. Run `git diff --check` and check new files
for whitespace errors separately. Run the checks relevant to changed artifacts;
record blocked checks without calling an unverified build complete.

Report changed files, verification actually performed, checks not run, and any
remaining limitations. Report Git state accurately; a written file is not a
commit, and a proposed verification contract is not passing CI.
