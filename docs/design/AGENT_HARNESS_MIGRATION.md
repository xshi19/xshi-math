# Agent Harness Migration

Status: active plan for installing shared Codex/Cursor skills into `xshi-math`.
Owner priority: migrate the agent harness before theme/TOC/IG polish.
Authoring date: 2026-09-13.
Model for this work: Codex `gpt-6-astra` with `xhigh` (no Cursor CloudAgent).

This document decides what to port from the Incerto and Normix agent trees,
where the canonical copies live, and how an agent should load them day-to-day.
It implements the discovery contract in
[AGENT_FRAMEWORK.md](AGENT_FRAMEWORK.md): one skill tree at `.agents/skills/`,
shared rule bodies in `docs/rules/`, and thin `.cursor/rules` adapters for
Cursor activation metadata.

## Upstream inventories (cite these)

Incerto skills under
https://github.com/xshi19/incerto-wiki/tree/main/.agents/skills/ :

- `incerto-agent-guidance`, `incerto-concept-page`, `incerto-deep-math-agent`,
  `incerto-git-conventions`, `incerto-lean-formalization`,
  `incerto-math-question`, `incerto-proof-writing`, `incerto-prose-review`,
  `incerto-reading-guide`

Normix under https://github.com/xshi19/normix/tree/master/.cursor/ :

- skills: `agent-maintenance`, `architect`, `arena`, `docs-publish`,
  `figure-it-out`, `git-conventions`, `how`, `interrogate`, `principles`,
  `running-tests`, `show-me`, `tdd`, `unslop`, `why`
- rules: `coding-conventions`, `docs-cross-links`, `maintain-*`,
  `notebook-guidelines`, `project-overview`, `rule-authoring`,
  `testing-guidelines`, `maintain-theory-docs`

Existing xshi-math guidance before this migration: root
[AGENTS.md](../../AGENTS.md), track routers under
`content/{incerto,ig,normix-theory}/AGENTS.md`, this framework, and
[docs/rules/index.md](../rules/index.md) (stub). Canonical skills belong in
`.agents/skills/`; none were installed until P0 below.

## Naming

Use the **`xshi-math-`** prefix for monorepo skills (not track prefixes).

Rationale: most writing/math workflows apply to Incerto, Information Geometry,
and Normix theory alike. Track differences belong in nested `AGENTS.md` and in
shared notation, not in duplicated skill trees. Keep upstream names in the
migration table so future agents can find the source.

Do **not** create `.cursor/skills/` (symlink or copy). Cursor discovers
`.agents/skills/` directly.

## Port / adapt / leave upstream

| Upstream | Decision | Notes |
| --- | --- | --- |
| Incerto `agent-guidance` | **Adapt →** `xshi-math-agent-guidance` | Point at this repo's framework, rule index, and skill tree |
| Incerto `concept-page` | **Adapt →** `xshi-math-concept-page` | Flat `content/*.md` stems + track hubs; not `content/concepts/` |
| Incerto `proof-writing` | **Adapt →** `xshi-math-proof-writing` | Keep proof-support types; drop Lean-pending public prose; no Lean tree yet |
| Incerto `prose-review` | **Adapt →** `xshi-math-prose-review` | Point at `docs/rules/mathematical-writing.md` |
| Incerto `math-question` | **Adapt →** `xshi-math-math-question` | Answer-first; edit only after approval; all three tracks |
| Incerto `git-conventions` | **Merge →** `xshi-math-git-conventions` | Imperative safety from Incerto + conventional-commit flavor from Normix, scoped to this repo |
| Normix `unslop` | **Adapt →** `xshi-math-unslop` | Keep pattern library and math carve-outs; rewrite registers for hub surfaces |
| Normix `docs-publish` | **Leave upstream** | Publishes `https://xshi19.github.io/normix/` from Normix `gh-pages`. Do not copy. |
| Math hub publish | **Thin note →** `xshi-math-hub-publish` | Local `npm run build` / `check:html`, then optional rsync into hub `math/`; hub owns Pages |
| Normix `principles` / `how` / `why` | **Leave upstream for now** | Heavy JAX/package/design-table grounding. Revisit thin doc kernels only after friction |
| Normix `tdd`, `arena`, `running-tests`, `architect`, `interrogate`, `show-me`, `figure-it-out`, `agent-maintenance` | **Leave upstream** | Package/TDD/JAX workflows do not match this MyST monorepo |
| Incerto `reading-guide` | **Adapt →** `xshi-math-reading-guide` | No `content/reading-guides/` tree; author on demand via flat stems/hubs; fold short maps into concept-page |
| Incerto `lean-formalization` | **Adapt →** `xshi-math-lean-formalization` | Honest: no Lean project yet; skill states prerequisites and when to open a Lean subtree |
| Incerto `deep-math-agent` | **Adapt →** `xshi-math-deep-math-agent` | Runner + archive under `docs/records/deep-math/`; deps optional until a paid run |
| Normix `.cursor/rules/*` | **Selectively extract** | P0: mathematical writing + shared notation as `docs/rules/` bodies. P1: thin `.mdc` adapters installed |
| Incerto `docs/rules/{writing,content,agent-guidance}.md` | **Synthesize** | Writing → `mathematical-writing.md`; notation invariants → `shared-notation.md`; do not clone the full Incerto rule set |

## Target layout

```text
.agents/skills/
  xshi-math-agent-guidance/SKILL.md
  xshi-math-concept-page/SKILL.md
  xshi-math-proof-writing/SKILL.md
  xshi-math-prose-review/SKILL.md
  xshi-math-math-question/SKILL.md
  xshi-math-git-conventions/SKILL.md
  xshi-math-unslop/SKILL.md (+ references/writing-registers.md)
  xshi-math-hub-publish/SKILL.md
  xshi-math-reading-guide/SKILL.md
  xshi-math-lean-formalization/SKILL.md
  xshi-math-deep-math-agent/SKILL.md (+ scripts/, references/, archive README)
docs/rules/
  index.md                 # routes to bodies
  mathematical-writing.md  # P0
  shared-notation.md       # P0
.cursor/rules/*.mdc        # P1: activation metadata + pointer, no policy body
docs/records/deep-math/    # deep-math report archive convention
AGENTS.md                  # router lists installed skills
content/{incerto,ig,normix-theory}/AGENTS.md  # track + skill pointers
.codex/config.toml         # already: gpt-6-astra + xhigh
```

Sources of truth remain as in the framework: routers route, rules constrain,
skills encode procedures, executable checks verify objective properties.

## Cross-track concerns

### Shared notation

[content/notation.md](../../content/notation.md) is the single canon, public
URL `/math/notation/`. Every concept skill and both rule bodies must send
agents there before inventing symbols. Track hubs may define local one-off
symbols; overlapping concepts extend the shared page first.

### Three independent subsites

Landing + Incerto (`/math/incerto/`) + IG (`/math/ig/`) + Normix theory
(`/math/normix-theory/`). Relative Markdown links stay inside a track.
Cross-track links use full `https://xshi19.github.io/math/...` URLs because the
theme prepends `BASE_URL` to root-absolute links. Skills must not assume a
single Jupyter Book TOC or a `content/concepts/` tree.

### Writing / prose / proof / concept-page boundaries

| Concern | Owner |
| --- | --- |
| Page shape, sources, claims, links, examples | `xshi-math-concept-page` |
| What is proved vs cited vs sketched | `xshi-math-proof-writing` |
| Semantics-preserving editorial pass | `xshi-math-prose-review` (+ `mathematical-writing` rule) |
| AI-pattern scrub + registers | `xshi-math-unslop` |
| Q&A before edits | `xshi-math-math-question` |
| Symbol reuse across tracks | `shared-notation` rule |

Do not run prose/unslop before claims and proof scope are settled. Do not treat
a numerical demo as a proof.

### Publishing boundary

Normix package docs stay on Normix `gh-pages` (`/normix/`). Math hub HTML is
built here (`npm run build`) and assembled into hub `math/` by a separate
transfer; this repo does not own Pages settings. See
[README](../../README.md) and
[consolidation boundaries](../plan/consolidation.md#repository-boundaries).

## Phased rollout

### P0 — install writing + math skills (this PR)

1. Write this plan.
2. Install adapted skills listed under Target layout (except Cursor adapters).
3. Add `docs/rules/mathematical-writing.md` and `docs/rules/shared-notation.md`;
   refresh the rule index.
4. Point root and track `AGENTS.md` at the installed skills.
5. Leave Lean/deep-math/reading-guide, Cursor adapters, and package-centric
   Normix skills out.

### P1 — Cursor adapters (done)

Installed thin `.cursor/rules/*.mdc` files that only set `description` /
`globs` / `alwaysApply: false` and point at canonical bodies (no policy text
in the adapters):

- `mathematical-writing.mdc` → `docs/rules/mathematical-writing.md`
- `shared-notation.mdc` → `docs/rules/shared-notation.md` (+ `content/notation.md`)
- `concept-page-workflow.mdc` → `.agents/skills/xshi-math-concept-page/SKILL.md`
- `prose-review-workflow.mdc` → prose-review / unslop skills + writing rule
- `agent-guidance-workflow.mdc` → agent-guidance skill + framework docs

Normix `.cursor/rules` were used only as activation-pattern reference (globs /
alwaysApply), not as package/JAX policy to copy.

### P2 — lean / deep-math / reading-guide (done as honest adaptations)

Installed adapted skills even though supporting trees are incomplete:

- `xshi-math-reading-guide` — how to author a map on flat stems/hubs; no fake
  `content/reading-guides/` pages.
- `xshi-math-lean-formalization` — prerequisites and when to open a Lean
  subtree; does not claim `lean-blueprint` exists.
- `xshi-math-deep-math-agent` — adapted runner + `docs/records/deep-math/`
  archive; document deps; dry-run before paid calls.

Keep formalization claims out of public prose until a real `lake build` exists.

### Explicitly not blocking this harness PR

Owner-queued follow-ups (do not expand this PR):

- Theme: align Incerto subsite colors with the old wiki (cream/serif).
- TOC: hierarchical TOC for all three subsites (study Incerto wiki
  Reference/Concepts structure).
- IG: clarify `v`,`w` as tangent velocities; replace Bernoulli-as-primary
  example (Astra free to choose Normal/Gamma/etc.).

## Day-to-day harness read order

Load the smallest useful set:

1. **Root** [AGENTS.md](../../AGENTS.md) — model chooser, boundaries, verification.
2. **Track router** if editing under a track:
   `content/{incerto,ig,normix-theory}/AGENTS.md`.
3. **One rule** when constraints apply:
   - math prose → [mathematical-writing.md](../rules/mathematical-writing.md)
   - symbols → [shared-notation.md](../rules/shared-notation.md)
4. **One skill** for the procedure (trigger from skill `description`):
   - math Q&A → `$xshi-math-math-question`
   - new/substantial note → `$xshi-math-concept-page`
   - theorems/proofs → `$xshi-math-proof-writing`
   - settled prose polish → `$xshi-math-prose-review` and/or `$xshi-math-unslop`
   - git/PR → `$xshi-math-git-conventions`
   - guidance maintenance → `$xshi-math-agent-guidance`
   - local site build / hub transfer note → `$xshi-math-hub-publish`
   - source→concept reading map → `$xshi-math-reading-guide`
   - Lean scoping / future formalization → `$xshi-math-lean-formalization`
   - hard external math consult → `$xshi-math-deep-math-agent`
5. **Touched sources** (page, notation, citations, demos) and only then broader
   design docs when changing a boundary.

Do not load all skills, all three tracks, and the full consolidation plan for a
typo fix.

## Completion evidence for harness changes

- Skill folders live only under `.agents/skills/` with unique `name` fields.
- Rule bodies are ordinary Markdown under `docs/rules/`; the index links them.
- Routers mention installed skills by `$name` and do not duplicate skill bodies.
- Relative links resolve; `git diff --check` is clean on the change set.
- Client discovery of a new skill is reported as untested unless actually tried
  in Codex/Cursor.

## P0 install record

Installed with this plan:

- `.agents/skills/xshi-math-{agent-guidance,concept-page,proof-writing,prose-review,math-question,git-conventions,unslop,hub-publish}/`
- `docs/rules/mathematical-writing.md`, `docs/rules/shared-notation.md`
- Updated `docs/rules/index.md`, root `AGENTS.md`, and the three track routers

## P1 / P2 install record

- `.cursor/rules/{mathematical-writing,shared-notation,concept-page-workflow,prose-review-workflow,agent-guidance-workflow}.mdc`
- `.agents/skills/xshi-math-{reading-guide,lean-formalization,deep-math-agent}/`
- `docs/records/deep-math/README.md`
- Updated migration plan, framework status, rule index, root and track `AGENTS.md`

Honest gaps: no Lean project / blueprint; no `content/reading-guides/` tree;
deep-math Python deps (`openai` / `openai-agents`) may be absent until a run.

Still deferred: Normix package/TDD/arena skills; theme/TOC/IG content polish.
