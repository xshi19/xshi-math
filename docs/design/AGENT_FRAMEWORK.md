# Agent Framework Design

Maintainer: Xiang Shi
Last updated: 2026-09-12

Operating model for Codex and Cursor in `xshi-math`. This is not a product
spec. It is how we write and update `AGENTS.md`, rules, skills, and the
docs those files point at.

No track content has been migrated yet. Skills listed below are a **starter
set to add at scaffold**, not files that exist today.

## Goal

Give both harnesses the same map, the same recipes, and the same definition
of done, without duplicating bodies or flooding context.

Agents should:

- see a short router first;
- load only the guidance the current task needs;
- preserve mathematical, bibliographic, and prose rigor;
- stop only after verification against a real artifact;
- improve the guidance system when the same friction repeats.

## Non-goals

- Do not build a custom harness before the repo needs one.
- Do not hide durable facts in chat history or unversioned memory.
- Do not make every task load every rule, skill, and design doc.
- Do not turn `AGENTS.md` into a manual.
- Do not copy full skill or rule bodies into a second tool tree.
- Do not port `normix`-only package skills (distribution recipes, Bessel
  notes, `architect` / `tdd` loops) into this repo.

## Source synthesis

This design merges two in-repo philosophies and the 2026 official discovery
rules.

### From normix

Canonical write-up:
[`normix/dev-notes/design/agent_instructions_design.md`](https://github.com/xshi19/normix/blob/master/dev-notes/design/agent_instructions_design.md)
(Cursor-primary historically: `.cursor/rules/*.mdc` + `.cursor/skills/`).

Take:

- **Map, not manual.** `AGENTS.md` is a ~100-line table of contents.
- **Progressive disclosure.** Deeper docs load on demand.
- **Rules = preferences; skills = recipes.** Do not mix.
- **Enforce mechanically** (tests, linters, CI) before adding prose.
- **Single source of truth.** Facts live once; others point.
- **pstack-style workflow skills:** narrow triggers, recorded outputs,
  completion predicates in the body.
- Add rules/skills from observed mistakes, then prune.

### From incerto-wiki

Canonical write-up: `docs/design/AGENT_FRAMEWORK.md` in private
[`xshi19/incerto-wiki`](https://github.com/xshi19/incerto-wiki)
(Codex-primary: `.agents/skills/`, `docs/rules/*.md`, `.codex/config.toml`,
root `AGENTS.md`).

Take:

- **Guidance is a router.**
- **Context is a budget.**
- **Verification defines done.** Inspect the real artifact.
- **Local, versioned memory** (`docs/design/`, `docs/rules/`,
  `ARCHITECTURE.md`, content trees).
- **Prose quality is part of mathematical rigor.** Style passes must not
  broaden claims or drop assumptions.
- **Automate signals, not editorial judgment.** Lint structure; do not
  auto-rewrite theorems.
- Improve from observed friction; prune aggressively.

### Project-CC thin-adapter pattern

Reference layout (Xiang's Project-CC):

- Canonical bodies in one tree (`guidelines/AI协作/模块/` there).
- Thin adapters in `.agents/skills/`, `.cursor/skills/`, `.claude/skills/`
  that **point back** — they do not copy full bodies.
- `.codex/` holds project config and optional `agents/`, **not**
  `.codex/rules/` or `.codex/skills/`.

For `xshi-math` the canonical skill tree **is** `.agents/skills/`, because
both Codex and modern Cursor discover it. That removes the need to mirror
skills into `.cursor/skills/` or `.claude/skills/`.

### Official discovery (2026) — respect these facts

**Codex**
([AGENTS.md](https://developers.openai.com/codex/guides/agents-md),
[skills](https://developers.openai.com/codex/skills),
[customization](https://developers.openai.com/codex/concepts/customization)):

- Discovers `AGENTS.md` / `AGENTS.override.md` from repo root down to cwd;
  nearer wins; default combined cap ~32 KiB; empty files skipped.
- Symlinks are allowed for `AGENTS.md` discovery.
- Repo skills: `.agents/skills/<name>/SKILL.md` with frontmatter `name` +
  `description`; optional `agents/openai.yaml`; progressive load
  (description first, body on invoke).
- Nested `.agents/skills/` from cwd up to repo root are scanned.
- Project config: `.codex/config.toml` for model defaults. Keep auth,
  provider, and machine settings in `~/.codex`.

**Cursor**
([rules](https://cursor.com/docs/rules),
[skills](https://cursor.com/docs/skills)):

- `AGENTS.md` is supported, including nested files (nearer / more specific
  wins when combined).
- Structured rules: `.cursor/rules/*.mdc` with `alwaysApply`, `globs`,
  `description`. Plain `.md` in that folder is ignored.
- Skills are discovered from **both** `.agents/skills/` and
  `.cursor/skills/` (and nested copies). Also loads `.claude/skills/` and
  `.codex/skills/` for compatibility — we still will not author there.
- Progressive disclosure for skills (description first).

## Principles (merged)

1. **Guidance is a router.** Root `AGENTS.md` answers: what is this repo,
   where is truth, which skill/rule applies, what command verifies.
2. **Context is a budget.** Prefer the smallest relevant rule or skill.
3. **Rules encode preferences and constraints.** Skills encode recipes.
4. **One fact, one home.** Pointers everywhere else.
5. **Enforce mechanically, then write prose.** Tests and CI before
   always-on rules.
6. **Verification defines done.** Parse/build reports are not enough when
   the artifact is a page, figure, proof, or diff.
7. **Local versioned memory.** If a future session must know it, it lives
   in git.
8. **Prose quality is math rigor.** A smoother sentence that drops a
   hypothesis is a regression.
9. **Automate signals, not editorial judgment.**
10. **Improve from friction; prune aggressively.** Do not add guidance
    because it sounds wise.

## Single source of truth surfaces

| Fact | Canonical home | Who points here |
| --- | --- | --- |
| Task routing, commands, "start here" | root `AGENTS.md` | both harnesses (always on) |
| Repo map, module/track boundaries | `ARCHITECTURE.md` (add at scaffold) | `AGENTS.md`, design docs |
| Durable product/stack rationale | `docs/design/` | `AGENTS.md` |
| Agent-harness design | this file | `AGENTS.md`, agent-guidance skill |
| Active roadmap | `docs/plan/` | `AGENTS.md` |
| Stable constraints (copyright, content, coding, writing) | `docs/rules/*.md` | `AGENTS.md`; thin `.cursor/rules/*.mdc` |
| Repeatable workflows | `.agents/skills/<name>/SKILL.md` | `AGENTS.md` task table |
| Track-only overlays | `tracks/<name>/AGENTS.md` | Codex/Cursor nested discovery |
| Content truth | `tracks/*/content/` (once migrated) | skills and rules |
| Python truth | `packages/*` (once migrated) | coding rule, pytest |
| Lean truth | `tracks/incerto/formalization/` | lean skill |

Do not also store the same conventions in `.cursor/skills/`,
`.codex/skills/`, or `.codex/rules/`.

## Skills

**Canonical location only:** `.agents/skills/<name>/SKILL.md`.

Both Codex and modern Cursor discover that path. Do **not** mirror into
`.cursor/skills/` unless a Cursor-only asset is required (for example a
Cursor-specific `show-me` HTML helper or a `paths` / Custom Mode badge
that Codex cannot use). Even then, the adapter should be thin and should
point at the canonical `SKILL.md`.

Each skill:

- has `name` (matches folder) + `description` with trigger and
  non-trigger;
- states a one-line completion predicate per phase;
- cites `docs/rules/` instead of restating conventions;
- stays one job. Compose via routes in `AGENTS.md`, not an always-on mega
  skill.

Optional Codex metadata: `agents/openai.yaml` (display, implicit
invocation). Optional Cursor-only fields (`paths`, `icon`, `color`) may
live in the same `SKILL.md` when they are ignored harmlessly by Codex, or
in a thin `.cursor/skills/<name>/SKILL.md` adapter if they conflict.

Never duplicate full skill bodies across tools.

## Rules

**Canonical location:** `docs/rules/*.md`. Codex reaches them because
`AGENTS.md` routes to them (Codex has no glob-injected `.mdc` layer).

**Cursor adapters:** `.cursor/rules/*.mdc`, Project-CC style.

Prefer **thin** adapters:

```markdown
---
description: Content constraints for track pages
globs: tracks/**/*.md, tracks/**/*.mdx
alwaysApply: false
---

Follow `docs/rules/content.md`. Do not weaken claim backing, copyright,
or notation rules in this adapter. Add only Cursor-specific invocation
notes below.
```

Two acceptable adapter shapes:

1. Brief restatement (5–15 lines) **plus** a pointer to `docs/rules/…`.
2. Glob / `alwaysApply` wiring with Cursor-only preferences (for example
   "when editing `.mdc`, keep frontmatter valid").

Do not paste the full rule file into the `.mdc`.

Root `AGENTS.md` remains the always-on surface for both tools. Use
`alwaysApply: true` sparingly — only for a one-screen preference that
`AGENTS.md` should not grow to hold.

## Symlinks vs thin adapters

| Case | Choice |
| --- | --- |
| Skill bodies | **One tree:** `.agents/skills/`. No copies, no tree-wide symlinks. |
| Rule bodies | **Canonical Markdown** in `docs/rules/`. Thin `.mdc` adapters. |
| Identical file, same name, both tools resolve it | Symlink **OK** (Codex documents `AGENTS.md` symlinks). Example: a nested `AGENTS.md` that should be an exact alias. |
| Frontmatter or discovery path differs | **Thin adapter**, not a symlink. |
| Entire `.cursor/` ↔ `.agents/` | **Never symlink.** Different file types and discovery rules. Fragile on Windows and Cloud Agents. |
| `.codex/skills/` or `.codex/rules/` | **Do not create.** Codex uses `.agents/skills/` + `AGENTS.md`. |

If a symlink is used, it must be a single file, checked in a Linux +
Cursor Cloud smoke test, and documented in `ARCHITECTURE.md`. Prefer
adapters when unsure.

## When to use nested `AGENTS.md`

Add `tracks/<name>/AGENTS.md` only when that track needs **different
behavior** than the root router: different verify commands, content
schema, copyright posture, or package imports.

Expected v1 overlays:

| Path | Why |
| --- | --- |
| `tracks/incerto/AGENTS.md` | Concept-page schema, Taleb paraphrase+cite, `packages/incerto` imports, Lean `lake build` |
| `tracks/info-geom/AGENTS.md` | Only once real pages exist (notation + "no invented theorems") |
| `tracks/normix/AGENTS.md` | Demos depend on published `normix`; never edit JAX sources here; pointer-vs-port rule |

Keep overlays short. Repeat only the deltas. Root `AGENTS.md` must stay
useful when cwd is the repo root (Codex concatenates root → cwd and stops
at the ~32 KiB combined cap).

Use `AGENTS.override.md` only for a temporary local override, not as the
standing track file.

## Verification-defines-done

Every recurring task type needs a visible contract. "The agent said it
built" is not done.

| Task type | Done means | Command / artifact (planned) |
| --- | --- | --- |
| Site / page change | Affected pages render; no new unresolved xrefs/citations in the strict build; skipped cells reported | MyST / `jupyter-book` build of the site or track; read the HTML, not only the log |
| Python / demo change | Tests cover the changed behavior; examples import the package, not copied cells | `pytest` for `packages/` and `tests/` |
| Lean change | Declarations that were claimed to check actually check | `cd tracks/incerto/formalization/lean && lake build` |
| Prose / tutorial edit | Claims still have proof, computation, citation, or caveat; scope and notation survived the style pass | `prose-review` skill + human checkpoint for load-bearing math |
| Guidance edit | Router still short; no duplicated facts; skill descriptions still trigger correctly | `agent-guidance` skill; fail if `AGENTS.md` becomes a manual |
| Publish | Hub paths updated; old `/incerto-wiki/` URLs still resolve | `docs-publish` skill (Phase 6+); smoke old and new URLs |

If a check cannot be run, the agent must say so. Do not imply CI exists
for tracks that are still empty.

Forward-test new skills against realistic prompts and at least one
counterexample that should **not** trigger a rewrite.

## Minimal starter skill set

Port and **adapt** from Incerto; do not copy bodies in this planning
phase. Generalize names at the repo root. Keep Incerto-only recipes
prefixed or nested once the track exists.

| Skill | Role | When |
| --- | --- | --- |
| `concept-page` | Create/maintain a concept atom | Scaffold, before first real page |
| `prose-review` | Semantics-preserving final pass | With first user-facing math |
| `agent-guidance` | Update this system without bloat | Scaffold |
| `git-conventions` | Deliberate stage / commit / push | Scaffold |
| `lean` | Scoped Lake/Mathlib work | When the Lean tree migrates |
| `math-question` | Answer from sources before editing pages | When content exists |
| `docs-publish` | Build + hub publish + redirect smoke | Phase 6, not earlier |

Defer until the workflow repeats (>3 times or a whole migration phase):

- `reading-guide`, `proof-writing`, `deep-math-agent` (Incerto-specific;
  add under `tracks/incerto/` or as `incerto-*` skills at migration);
- interactive-explainer skill;
- doc-gardener / scheduled drift skill;
- any `normix` package skill.

## `.codex/config.toml`

Author **model defaults only** in the repo. A commented template lives at
[`.codex/config.toml`](../../.codex/config.toml).

Recommended starting point (matches current Incerto project defaults;
Xiang often uses high reasoning effort for this domain):

```toml
model = "gpt-5.6-sol"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
sandbox_mode = "workspace-write"
```

Keep provider, auth, telemetry, and `CODEX_HOME` in `~/.codex`. Do not add
`.codex/rules/` or `.codex/skills/`. Do not pin secrets.

`Open question:` whether `xhigh` should be the repo default or Xiang's
user-level default, with the repo at `high`. Either is fine; pick one so
Cloud and CLI do not silently differ.

## Cursor-specific notes

- Root and nested `AGENTS.md` already apply. Do not restate the whole
  router in an always-on `.mdc`.
- Use `.mdc` globs for `tracks/**/*.md`, `packages/**/*.py`,
  `**/*.lean` once those trees exist.
- Multi-model panels (normix `arena` / `interrogate`) stay optional and
  Cursor-only. Do not require them for v1 wiki work.
- Cloud Agents see project skills in `.agents/skills/`. They do not see
  unsynced `~/.agents/skills/`.

## Default workflow

1. Read root `AGENTS.md`.
2. Identify the task type and the track.
3. Read the smallest set of `ARCHITECTURE.md`, `docs/rules/`, skills, and
   nested `AGENTS.md`.
4. Make scoped changes.
5. Run the verification contract. Inspect the artifact.
6. Report what changed, what was verified, and what is still risky.
7. If the same gap will hit the next session, update a rule or skill —
   not a one-off chat note.

## Maintenance

- Add a rule after a **repeated** mistake; add a skill after a workflow
  repeats.
- Keep `AGENTS.md` as a map. If it grows past ~100–120 lines, move detail
  out.
- When rules exceed ~10 files or skills exceed ~15, consolidate.
- Delete guidance that tooling now enforces.
- After each consolidation phase, prune contradictions (especially
  leftover Incerto paths vs `tracks/incerto/`).
- Measure by friction, not by file count.

## Sources

- [normix agent instructions design](https://github.com/xshi19/normix/blob/master/dev-notes/design/agent_instructions_design.md)
- incerto-wiki `docs/design/AGENT_FRAMEWORK.md` (private; 2026-09-06)
- [OpenAI: Harness engineering](https://openai.com/index/harness-engineering/)
- [OpenAI Codex: AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- [OpenAI Codex: skills](https://developers.openai.com/codex/skills)
- [OpenAI Codex: customization](https://developers.openai.com/codex/concepts/customization)
- [Cursor: rules](https://cursor.com/docs/rules)
- [Cursor: skills](https://cursor.com/docs/skills)
- [Cursor: improving the agent harness](https://cursor.com/blog/continually-improving-agent-harness)
- [matklad: ARCHITECTURE.md](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html)
- [Anthropic: effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [pstack plugin](https://github.com/cursor/plugins/tree/main/pstack)
- Project-CC thin-adapter layout (`guidelines/AI协作/模块/` → tool skills)
