# Consolidation Plan

Maintainer: Xiang Shi
Last updated: 2026-09-12

Plan for folding Xiang's personal math sites into this public monorepo in one
coordinated pass ("一次性全合"). This document is the execution plan. It does
not migrate content.

## Status

Planning only. `xshi-math` currently contains gitignore, a short README, and
these plan docs. Nothing has been copied from `incerto-wiki` or `normix`.

## Goal

One public monorepo for:

- mathematical notes and tutorials (MyST / Jupyter Book v2);
- Python visualization and numerical demos;
- optional Lean, learned while used.

Three tracks share one Kami-like visual language. The personal hub
[`xshi19.github.io`](https://xshi19.github.io/) remains the public face.

## Current landscape

| Surface | Repo | Role now |
| --- | --- | --- |
| Personal hub | [`xshi19/xshi19.github.io`](https://github.com/xshi19/xshi19.github.io) | User Pages site. Hosts committed build artifacts under `/normix/` and `/incerto-wiki/`, plus older Pelican posts. |
| Incerto wiki (source) | [`xshi19/incerto-wiki`](https://github.com/xshi19/incerto-wiki) (private) | Concept-first MyST wiki + installable `incerto` helpers + contained Lean project. CI builds the site (`BASE_URL=/incerto-wiki`) and can deploy GitHub Pages. |
| Incerto wiki (public) | `https://xshi19.github.io/incerto-wiki/` | Current public URL. Treat as **stable**. |
| Normix package | [`xshi19/normix`](https://github.com/xshi19/normix) | JAX library, API docs, tutorials, `docs/theory/*.md`. Package + API stay here. |
| Normix docs (public) | `https://xshi19.github.io/normix/` | Package documentation site. Treat as **stable**. |
| This repo | [`xshi19/xshi-math`](https://github.com/xshi19/xshi-math) | Empty public consolidation target. |

Incerto already has a Kami-derived theme (`docs/design/VISUAL_STYLE.md`,
`assets/css/incerto.css`), a concept-page contract, and a Codex-primary agent
harness. Reuse those contracts; do not invent a second wiki style.

## Target repo layout

Proposed tree after scaffold. Paths that do not exist today are marked
*(planned)*.

```text
xshi-math/
├── AGENTS.md                      # always-on router (~100 lines)
├── ARCHITECTURE.md                # (planned) repo map; add at scaffold
├── README.md
├── LICENSE                        # after license decision
├── NOTICE                         # after license decision
├── CITATION.cff                   # after license decision
├── myst.yml                       # (planned) root MyST / JB2 site
├── pyproject.toml                 # (planned) uv workspace + site tools
├── uv.lock                        # (planned)
│
├── .agents/skills/                # canonical skills (Codex + Cursor)
├── .codex/config.toml             # model defaults only
├── .cursor/rules/                 # thin .mdc adapters, not full copies
│
├── docs/
│   ├── design/                    # durable rationale (this tree)
│   ├── plan/                      # active roadmap
│   └── rules/                     # canonical constraints
│
├── site/                          # (planned) shared kit
│   ├── theme/                     # Kami-like CSS tokens
│   ├── assets/
│   └── index.md                   # multi-track landing page
│
├── packages/
│   └── incerto/                   # (planned) migrated wiki helpers
│
├── tracks/
│   ├── incerto/
│   │   ├── AGENTS.md              # (planned) track overlay
│   │   ├── content/               # concepts, reading guides, notation
│   │   └── formalization/lean/    # contained Lake project
│   ├── info-geom/
│   │   ├── AGENTS.md
│   │   └── content/               # stub first
│   └── normix/
│       ├── AGENTS.md
│       └── content/               # theory pages + demos, not the JAX pkg
│
├── data/                          # small redistributable snapshots only
├── scripts/                       # build, provenance, content-status
└── tests/                         # package + artifact checks
```

Keep repo-level design docs (`docs/design/`, `docs/plan/`, `docs/rules/`)
**out of** the published MyST TOC unless a later design doc says otherwise.
Public pages live under `site/` and `tracks/*/content/`.

`Open question:` root `myst.yml` vs `site/myst.yml`. Prefer root if Jupyter
Book / MyST discovery is simpler; move under `site/` only if the root gets
noisy.

## Track model

One MyST site, three TOC branches, one theme.

| Track | Slug | Source | v1 content |
| --- | --- | --- | --- |
| Incerto / fat tails | `incerto` | Private `incerto-wiki` after scrub | Full migration of public-safe concept pages, reading guides, notation, glossary, `incerto` helpers, Lean project |
| Information Geometry | `info-geom` | New | Landing page + notation stub + empty concept index. No fake research. |
| Normix theory | `normix` | Selected `normix/docs/theory/` | Pointers first; port pages that should read as tutorials in the shared visual language. Package implementation stays in `normix`. |

Shared contracts across tracks:

- Kami parchment / ink visual language (from Incerto `VISUAL_STYLE.md`).
- Concept pages as primary atoms; reading guides are navigation, not replicas.
- Claims backed by proof, computation, citation, or explicit caveat.
- Track-local notation tables, with a later option for a thin shared glossary.
- Python demos import installable packages (`incerto`, published `normix`),
  not notebooks or copied JAX internals.

Do not merge the three tracks into one concept graph in v1. Cross-links are
allowed; shared IDs and a unified notation table are a later design.

## What migrates vs stays

### Stays in `normix`

- The JAX package (`normix/`), tests, benchmarks, ASV, release-please, PyPI.
- Generated API reference and package-user tutorials that document the library.
- Agent skills that only make sense for package work (`architect`, `tdd`,
  distribution-adding recipes, Bessel notes).

`xshi-math` may depend on a **published or editable** `normix` install. It
must not vendor the package implementation.

### Moves into `xshi-math` (after scrub)

From `incerto-wiki`:

- `content/` → `tracks/incerto/content/`
- `incerto/` + its tests → `packages/incerto/` (see recommendation below)
- `formalization/lean/` → `tracks/incerto/formalization/lean/`
- Theme CSS and figure helpers that define the shared look → `site/theme/`
- Content rules, writing rules, and wiki skills → adapted under `docs/rules/`
  and `.agents/skills/` (generalize names; keep Incerto-specific recipes
  track-scoped)
- Build/provenance scripts that remain useful

### Does not move

- `incerto-wiki/legacy/` — leave in the archived private repo as read-only
  history.
- Incerto `docs/reports/deep-math/` consultant archives — optional later;
  not required for cutover.
- Normix `dev-notes/` and package-internal design tables.
- Hub Pelican posts and unrelated pages on `xshi19.github.io`.

### Incerto Python helpers: recommendation

**Move `incerto/` into this monorepo as `packages/incerto`.** Keep it an
installable local package (`pip install -e packages/incerto` or a uv
workspace member). Do **not** split it into a third public repo in v1.

Why move, not leave as an external dependency:

- The package is the wiki's demo/computation layer (`distributions`,
  `estimators`, `datasets`, `figures`, `tail_diagnostics`). Concept pages
  already import it.
- It is MIT, small, and not a released JAX ecosystem library. Separate
  versioning and CI would cost more than they save.
- Other tracks should not take a hard dependency on it in v1.

Why not treat it like `normix`:

- `normix` has PyPI, release-please, ASV, and an API site. That isolation is
  load-bearing. `incerto` does not.

Publish `incerto` to PyPI only if a second consumer appears. Until then,
editable workspace install is enough.

`Open question:` keep the import name `incerto` (recommended, fewer content
edits) vs rename to `xshi_incerto`. Prefer keeping `incerto`.

## Hub deploy story

### Options

| Option | How it ships | Verdict |
| --- | --- | --- |
| **A. Hub-artifact publish (primary)** | `xshi-math` CI builds MyST HTML, then a main-only job commits (or PRs) artifacts into `xshi19.github.io` under `/math/` and, during cutover, compatibility files under `/incerto-wiki/`. | **Recommend.** Matches how the hub already hosts `/normix/` and `/incerto-wiki/`. Keeps the personal homepage as the only user site. Preserves stable paths. |
| B. Project Pages from `xshi-math` | Enable Pages on this repo → `https://xshi19.github.io/xshi-math/`. Hub only links. | Cleaner repo boundary, but changes the public prefix and still needs `/incerto-wiki/` redirects on the hub. Use only if Xiang wants the math site namespaced as `/xshi-math/`. |
| C. Dual publish (hub copy **and** project Pages) | Both A and B. | Reject. Two live trees drift. |

Normix package docs keep publishing from the `normix` repo into
`/normix/`. This plan does not change that pipeline.

### Recommended sequence

1. Scaffold and shared kit land **without** a deploy workflow that pretends a
   site exists.
2. After Incerto content is in tree and builds locally, add CI that runs
   pytest + MyST build on PRs and uploads an artifact. Do not deploy from
   pull requests.
3. Add a **main-only** publish job that updates `xshi19.github.io`:
   - write the new site to `/math/`;
   - keep `/incerto-wiki/` serving equivalent pages or redirects (next
     section);
   - leave `/normix/` untouched.
4. Only then disable Incerto's own Pages deploy, so there is no gap.

`Open question:` commit HTML into the hub repo (current habit) vs a
`peaceiris/actions-gh-pages`-style push to a hub branch. Either is fine;
prefer a dedicated publish branch or bot PR on the hub so the homepage
history stays reviewable.

Incerto CI today both uploads `_build/html` and calls
`actions/deploy-pages` with `BASE_URL=/incerto-wiki`. The hub also stores a
copy of `/incerto-wiki/`. During cutover, pick **one** live publisher
(option A) and turn the other off.

## URL strategy

Keep existing public URLs working. Add a multi-track root rather than
rebasing Incerto onto `/xshi-math/`.

| URL | After cutover |
| --- | --- |
| `https://xshi19.github.io/` | Hub homepage. Add a short "Math notes" link to `/math/`. |
| `https://xshi19.github.io/math/` | **New canonical** multi-track landing (this repo's MyST site). |
| `https://xshi19.github.io/math/incerto/` | Incerto track. |
| `https://xshi19.github.io/math/info-geom/` | IG stub. |
| `https://xshi19.github.io/math/normix/` | Normix **theory / demos** in this visual language. |
| `https://xshi19.github.io/incerto-wiki/` | **Stable.** Redirect (preferred) or mirror the Incerto subtree indefinitely. |
| `https://xshi19.github.io/incerto-wiki/<page>` | Per-page redirects onto `/math/incerto/<page>` once path mapping is 1:1. |
| `https://xshi19.github.io/normix/` | Unchanged package docs from the `normix` repo. |

Redirect mechanics on the hub (static user Pages):

- Directory `index.html` with `http-equiv` refresh + canonical link, plus a
  visible fallback link.
- For a large page map, generate a redirect tree in the publish job rather
  than editing by hand.

`Open question:` keep `/incerto-wiki/` as a permanent alias (safer) vs
sunset after a stated period. Recommend **permanent alias** for v1; revisit
once inbound links are known.

`Open question:` pretty slugs. Incerto pages today live under the site root
with `BASE_URL=/incerto-wiki`. After the move they live under
`/math/incerto/`. Redirects must encode that prefix change.

Do not introduce `/wiki/` or `/notes/` as a third prefix.

## Phases for 一次性全合

"One-shot" means: approve this plan, then execute the phases below as one
program (a short stack of PRs in this repo, one hub publish PR, archive
commits on the old sources). It does **not** mean a single gigantic commit,
and it does not mean running two public Incerto sites for months.

### Phase 0 — Approve

- [ ] Accept or amend this layout, deploy option A, and URL table.
- [ ] Accept license default (MIT whole-repo) or choose dual licensing.
      See [LICENSE_ADVICE.md](../design/LICENSE_ADVICE.md).
- [ ] Confirm Incerto helper recommendation (`packages/incerto`).

### Phase 1 — Scaffold (this repo)

- [ ] Add `LICENSE` / `NOTICE` / `CITATION.cff`.
- [ ] Add `ARCHITECTURE.md` describing the empty planned tree.
- [ ] Create `site/`, `tracks/{incerto,info-geom,normix}/`, `packages/`,
      `scripts/`, `tests/` as intentional stubs (READMEs, not fake pages
      that claim results).
- [ ] Expand `.agents/skills/` and thin `.cursor/rules/*.mdc` adapters per
      [AGENT_FRAMEWORK.md](../design/AGENT_FRAMEWORK.md).
- [ ] Add `pyproject.toml` / uv workspace **only** when the first real
      package or build tool lands. No placeholder package code.

### Phase 2 — Shared kit

- [ ] Lift Kami tokens and MyST config from Incerto into `site/theme/`
      (adapt, do not fork a second aesthetic).
- [ ] One `myst.yml` (or JB2 config) with three TOC branches.
- [ ] Shared build script. CI may lint/plan-docs only until a track has
      pages that actually build.
- [ ] Figure/style helpers that other tracks can import without pulling
      Incerto math.

### Phase 3 — Private→public scrub, then migrate Incerto

Gate: nothing from the private repo lands here until the scrub list is
checked.

- [ ] Review every page, figure, snapshot, and notebook output for
      copyright, license-restricted data, private notes, and secrets.
- [ ] Paraphrase+cite Incerto/Taleb material; no copyrighted figure dumps.
- [ ] Move public-safe `content/` → `tracks/incerto/content/`.
- [ ] Move `incerto/` → `packages/incerto/` and retarget imports/tests.
- [ ] Move Lean project under `tracks/incerto/formalization/`.
- [ ] Port Incerto skills to the starter set (generalize names; keep
      track-specific recipes under `incerto-` prefixes or a nested skill
      dir).
- [ ] Prove local build: pytest + MyST + `lake build` for the Lean tree.

### Phase 4 — Information Geometry stub

- [ ] `tracks/info-geom/content/index.md` stating intent and empty concept
      index.
- [ ] Notation stub. No invented theorems.

### Phase 5 — Normix theory pointers / ports

- [ ] Landing page that links to live package docs at `/normix/` for API
      and install.
- [ ] For each `normix/docs/theory/*.md` page, choose: **pointer** (link
      only), **port** (MyST rewrite in this theme), or **defer**.
- [ ] Demos in this repo import installed `normix`. They do not copy JAX
      sources.
- [ ] Leave a short "canonical theory home" note in `normix` pointing here
      **only after** ports exist. Do not delete theory files from `normix`
      in the same breath as the first pointer page.

Likely first ports (existing files, not new research): `gig.md`, `gh.md`,
`em_algorithm.md`, `varentropy.md`. Pointer-only is acceptable for the
rest in v1.

### Phase 6 — Cutover redirects

- [ ] Publish `/math/` from `xshi-math` CI to the hub.
- [ ] Install `/incerto-wiki/` → `/math/incerto/` redirects (tree or
      mirror).
- [ ] Link `/math/` from the hub homepage.
- [ ] Disable Incerto repo Pages deploy.
- [ ] Smoke-check old and new URLs.

### Phase 7 — Archive old site sources

- [ ] `incerto-wiki` README: "moved to `xshi-math`; this repo is archive."
- [ ] Pin a final tag. Make the private repo clearly inactive (archive on
      GitHub, or `ARCHIVED.md` + freeze default branch).
- [ ] Do not delete history. `legacy/` stays there.
- [ ] `normix` remains active. Only theory *pages* may grow a pointer.

## Risks

| Risk | Mitigation |
| --- | --- |
| **Private→public leak** — Incerto source is private; this repo is public. | Phase 3 scrub is a hard gate. No "copy first, review later." |
| **Citation / copyright** — Taleb and other sources. | Companion, not replica. Paraphrase, cite, original figures. See [LICENSE_ADVICE.md](../design/LICENSE_ADVICE.md). |
| **License-restricted data** | Keep FRED / vendor series out of git. Snapshots only when redistribution is allowed (Incerto already documents this). |
| **Lean toolchain** | Keep Lake/Mathlib pinned and **track-scoped**. Lean CI is optional/path-filtered so docs-only PRs do not fetch Mathlib. |
| **Dual build times** | One MyST site, but execute only cheap cells on PR. Heavy sims stay behind scripts or precomputed artifacts (`jupyter-cache` / skip). Package pytest stays separate from full site execution. |
| **Theme drift** | One `site/theme/`. Tracks may not ship private CSS that redefines tokens. |
| **Two publishers** | Option A only. Turn off Incerto Pages at cutover. |
| **Normix theory duplication** | Pointer vs port table in Phase 5. Package API never copied. |
| **Agent-guidance bloat** | Router `AGENTS.md`; prune from observed friction. See [AGENT_FRAMEWORK.md](../design/AGENT_FRAMEWORK.md). |
| **Windows / Cloud symlink fragility** | Thin adapters for skills/rules. Do not symlink `.cursor` ↔ `.agents` trees. |

## Explicit non-goals for v1

- Migrate or vendor the `normix` JAX package, its API docs, or its
  package-only agent skills.
- Invent Information Geometry research content.
- Port every Normix tutorial, notebook, and theory file.
- Stand up interactive widget / JupyterLite suites.
- Dual-run public Incerto on both old and new trees for a long overlap.
- Enable project Pages on `xshi-math` *and* hub copies.
- Mirror full skill bodies into `.cursor/skills/` or `.claude/skills/`.
- Create CI that claims to build tracks that are still empty.
- Unify all tracks into one notation system or concept graph.
- Chinese full translation (Incerto has a bilingual entry; keep it if it
  migrates, but do not expand).
- Custom domain work.

## Open questions

Repeated from the sections above, for review:

1. `myst.yml` at repo root vs `site/myst.yml`.
2. Keep PyPI-less `incerto` import name as-is (recommended).
3. Hub HTML commits vs publish-branch bot PR.
4. Permanent `/incerto-wiki/` alias vs timed sunset (recommend permanent).
5. Which Normix theory pages to port vs pointer in the first cutover.
6. License: MIT whole-repo (recommended) vs dual MIT + CC-BY-4.0.

## Approval gate

Xiang can treat this file as the contract for 一次合. Amendments belong here
before Phase 1 starts. Do not begin content migration from this planning PR.
