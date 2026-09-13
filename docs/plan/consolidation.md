# Repository Consolidation Plan

Status: Phase 0 light inventory and Phase 1 local HTML gate complete; Phase 2
Incerto Batches 1–3 and Normix Theory Batches 1–2 executed locally. Further consolidation remains planned.
See the [planning index](index.md) for current work.
Source review date: 2026-09-13.

Use `xshi-math` as the authoring home for mathematical explanations and their
computational demonstrations. Organize the material into three tracks with
shared notation, citations, presentation, and verification. Publish the resulting
site through the existing personal hub. Keep Normix's software product in its
own repository.

This document plans the remaining consolidation. The original source scaffold
now exists; see [architecture](../../ARCHITECTURE.md) and the
[verification record](../records/phase-0-1-verification.md). Twenty-six approved Incerto
concept pages (twenty-three bodies and three indexes) are now adapted; see the
[Incerto Batch 1 record](../records/phase-2-batch-1-verification.md),
[Batch 2 record](../records/phase-2-batch-2-verification.md), and
[Batch 3 record](../records/phase-2-batch-3-verification.md). Thirteen Normix
notes are also adapted; see the [Normix Batch 1 record](../records/phase-2-normix-batch-1-verification.md)
and [Batch 2 record](../records/phase-2-normix-batch-2-verification.md).
Sibling code, private history, and deployment configuration have not been migrated.

## Repository boundaries

| Repository | Responsibility after consolidation | Boundary |
| --- | --- | --- |
| [xshi-math](https://github.com/xshi19/xshi-math) | Math notes/tutorials, educational Python helpers and demos, optional Lean, source bibliography, site source | May depend on an installable `normix`; does not vendor its implementation or maintain its API reference |
| [normix](https://github.com/xshi19/normix) | JAX package, public API, package tests and releases, implementation design, API documentation | Theory pages selected for consolidation gain links or redirects to their new canonical home |
| [incerto-wiki](https://github.com/xshi19/incerto-wiki) (private) | Private provenance and rollback archive after cutover; material excluded from publication | Eligible math, educational code, and verification move through a reviewed export; private history stays private |
| [xshi19.github.io](https://github.com/xshi19/xshi19.github.io) | Hub: assembly and publishing boundary for the personal landing page and public build artifacts | Hosts `/normix/` and the existing `/incerto-wiki/`; `/math/` is the selected future math base; mathematical source editing happens upstream |

Here, **hub** means the `xshi19.github.io` repository and its assembled site at
`https://xshi19.github.io/`. It combines upstream build artifacts and owns their
coordinated publication. `xshi-math` owns the math source and produces the math
artifact; the hub publishes it under `/math/` alongside the other hosted sites.

The dependency direction is `xshi-math -> normix`. A demo needing a new package
capability should use an upstream Normix change and a tested dependency version.
It should not create a second implementation inside the math repo. Normix need
not depend on `xshi-math` at runtime; documentation hyperlinks are sufficient.

The owner adopted [MIT](../../LICENSE) for repository-owned material. Apply the
[Incerto import decision and notice policy](../design/LICENSE_ADVICE.md#source-license-ambiguity)
when importing; add third-party exceptions to `THIRD_PARTY_NOTICES.md` as needed.

## Tracks and shared content

| Track | Scope | First useful shape |
| --- | --- | --- |
| Incerto / fat tails | Tail behavior, probability, estimation, reading guides, numerical illustrations | Concept pages linked to source-specific reading guides and reproducible demos |
| Information Geometry | Statistical manifolds, metrics, divergences, connections, and worked examples | A small prerequisite path with precise assumptions and numerical examples; expand as learning progresses |
| Normix theory | Mathematical foundations of normal mixtures and related constructions | Derivations and examples that link to the separately maintained package/API |

Concept pages should own mathematical statements; reading guides explain how a
source uses those concepts. A shared result has one canonical page, even when
several tracks discuss it. Place a result in a track initially, then promote it
to a shared location only when real reuse warrants the move. Keep stable labels
through that change.

A useful page identifies prerequisites, definitions and assumptions, the claim
or learning objective, evidence or proof, examples and limitations, and sources.
These are semantic expectations, not a mandatory set of headings for every page.
Distinguish a conjecture, an informal argument, a numerical illustration, and a
checked formal theorem. The [agent framework](../design/AGENT_FRAMEWORK.md)
specifies how prose review preserves those distinctions.

## Proposed tree

The MyST/Python source scaffold, original track samples, shared CSS, architecture
map, verification record, and representative planning CSVs now exist. The tree
below remains the broader target: bibliography, shared notation, most demos,
Lean, data provenance, skills, and adapters are still deferred. See
[architecture](../../ARCHITECTURE.md) for the current implementation.
Content routes use unique flat Markdown stems because MyST 1.10.1 ignores
`slug:`; the TOC supplies the track hierarchy.

```text
xshi-math/
  README.md
  AGENTS.md
  ARCHITECTURE.md                  # current implementation map; present
  LICENSE                         # adopted MIT; present
  THIRD_PARTY_NOTICES.md           # introduced with material needing notices
  myst.yml                        # one project, explicit TOC, MIT owner-material metadata
  package.json                    # pinned MyST tooling
  package-lock.json
  pyproject.toml                   # NumPy library packaging and dependency groups
  uv.lock
  content/
    index.md
    bibliography.bib
    notation.md                   # proposed shared notation
    incerto.md
    incerto-counting-exceedances.md
    information-geometry.md
    information-geometry-*.md      # six entry notes present; later stems in IG outline
    normix-theory.md
    normix-conditioning-a-mixture.md
  demos/
    incerto/                      # scripts or notebooks, linked from notes
    information-geometry/
    normix/
  src/math/                       # NumPy educational library; imports as xmath
  tests/                          # checks of implemented numerical behavior
  data/README.md                   # provenance, retrieval, licenses, checksums
  assets/
    styles/math.css               # shared site presentation
    figures/                      # original or rights-cleared source figures
  lean/                           # optional, independently pinned Lean/mathlib
    AGENTS.md
    lean-toolchain
    lakefile.toml
    lake-manifest.json
    XshiMath/
  scripts/                        # real build/verification entry points as needed
  docs/
    plan/
      index.md
      consolidation.md
      migration-manifest.csv      # representative inventory; present
      url-map.csv                 # representative old-to-new candidates; present
    design/
      AGENT_FRAMEWORK.md
      LICENSE_ADVICE.md
    rules/
      index.md
    records/                      # short durable decisions/verification records
  .agents/skills/                  # sole canonical skill tree, added when useful
  .cursor/rules/                  # optional thin .mdc adapters
  .codex/
    config.toml                   # active owner-selected model defaults; present
    README.md                     # config scope and model-policy pointer; present
```

The owner selected `src/math/` for a unified **NumPy-based educational math
library**. Keep demos close to their learning purpose and move only reused
computation into that directory. A notebook should call the helper it illustrates
rather than maintain a second algorithm. A public Python package release is not
necessary for v1; local installation is enough for reproducible imports.

### Python import name

**Resolved owner decision:** keep `src/math/` and expose it as `xmath` through
explicit setuptools package configuration. The distribution name is `xshi-math`.
`[tool.setuptools]` lists `xmath`; `[tool.setuptools.package-dir]` maps it to
`src/math`. Both editable and wheel imports were verified with stdlib `math`
and NumPy. No `src/` path injection is configured. List any future subpackages
explicitly when adding them and repeat the import checks.
[Setuptools package mapping](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html).

A distribution name alone does not change imports. Avoid adding `src/` to
`PYTHONPATH`, which could expose the physical `math` directory as a conflicting
package on Python builds where stdlib `math` is an extension module.
[Python module search path](https://docs.python.org/3/tutorial/modules.html#the-module-search-path).

### Dependencies

Use separate dependency groups for site tooling, ordinary numerical work, and
Normix/JAX demonstrations. Pin a tested Python environment and a tested site
toolchain. Keep Lean's toolchain independent so reading or building ordinary
notes does not require Lean. Add optional dependencies only when an actual demo
or proof uses them.

## What moves and what stays

These are classification rules for Phase 0, not an assertion that every source
file has been inventoried:

| Source material | Proposed disposition | Acceptance condition |
| --- | --- | --- |
| Incerto concepts, notation, glossary, bibliography, reading guides | Adapt into the Incerto track or shared reference pages | Retain claim scope, sources, useful labels, and public URL mappings |
| Incerto educational Python code, demos, tests, and small permitted fixtures | Move the relevant units together; normalize layout deliberately | Behavior is reproduced; imports and data rights are accounted for |
| Incerto Lean declarations and blueprint links, if selected | Move together into the optional Lean area | Pinned build succeeds; statement correspondence and proof status remain explicit |
| Incerto CSS and build customizations | Reuse the design intent; port only what the new build needs | Review ownership and theme compatibility; do not copy the full dependency stack |
| Incerto drafts, private notes, source PDFs, credentials, large data, raw agent transcripts | Keep in the private source/archive or exclude | Any later publication gets an explicit rights/privacy disposition |
| Normix authored theory pages and theory-oriented demos | Move selected source pages; link to the installed package | Preserve mathematical and bibliographic meaning; account for existing theory URLs |
| Normix JAX modules, public API docs, release machinery, package tests, implementation notes | Stay in `normix` | New theory pages use supported imports and link to upstream API documentation |
| Existing generated HTML, search indexes, caches, downloaded assets | Rebuild from approved source; retain old output only for rollback | Public artifact passes content and URL review |
| Information Geometry | Author new material directly here after Phase 1 builds with `BASE_URL=/math`, using the owner's entry concept list | One coherent learning path; no dependency on completing the Incerto import |

Inventory every candidate as move, adapt, stay, or exclude with a reason. Maintain
private exclusion details outside the public repo; the public manifest contains
only provenance safe to disclose. Transfer a sanitized export into new public
commits, without merging the private Git history. Attribution requirements still
apply when history is omitted; see [license advice](../design/LICENSE_ADVICE.md).

**Open question:** do existing consumers import the `incerto` Python package?
Inspect those consumers before renaming it. Use the selected `src/math/`
directory and adopted [import name](#python-import-name);
preserve or stage compatibility where needed. Do not promise import compatibility
before the inventory establishes its scope.

### Migration records

The two CSVs have different jobs. Both now contain representative rows from the
[light inventory](phase-0-inventory.md), with unknowns and proposed destinations
marked. They are not a complete source, rights, or fragment audit.

- [migration-manifest.csv](migration-manifest.csv) inventories candidate material
  by stable source ID, repository/revision/path, disposition (`move`, `adapt`,
  `stay`, or `exclude`), reason, target path, license, and required notices. It
  answers what happens to each item, including items without a public URL. Only
  publishable provenance belongs here; keep sensitive exclusion details private.
- [url-map.csv](url-map.csv) maps actual old URLs and fragments to their new URLs
  and fragments, with a source ID linking back to the inventory, intended route
  behavior, and verification status. One source item may have several legacy
  URLs. It drives compatibility pages and route checks, not content disposition.

Expand and review these records as preparation and the static-host rehearsal
establish actual destinations and results.

### Information Geometry timing

Start IG entry pages after the Phase 1 MyST foundation builds successfully with
`BASE_URL=/math`, using the owner's concept list. Both prerequisites are now met:
the local foundation build passes and the
[owner curriculum](ig-entry-curriculum-draft.md) has been supplied. The
[IG outline](ig-entry-outline.md) owns the implemented first batch and later
research sequence. Full Incerto migration is not a prerequisite.

## Site and execution design

The foundation configures one MyST Markdown site with the book theme, one table
of contents, unique filename-derived page routes, and shared CSS. Add a shared
bibliography when source-citing material requires it. “Kami-like” describes the reading experience:
restrained typography, readable equations, quiet navigation,
clear theorem/proof treatment, and usable mobile layouts. It does not imply a
new application framework or a theme fork.

The source projects currently use different rendering stacks: Incerto's
[MyST configuration](https://github.com/xshi19/incerto-wiki/blob/main/myst.yml)
selects `book-theme`, while Normix's
[Sphinx configuration](https://github.com/xshi19/normix/blob/master/docs/conf.py)
uses `myst_nb` and `sphinx_book_theme`. Shared Markdown syntax and a similar look
do not make their directives, cross-references, or CSS interchangeable. Audit
those differences when adapting theory pages. Normix's API site can retain
Sphinx and its existing visual conventions.

Separate expensive numerical execution from routine site rendering. First
generate approved outputs with pinned dependencies, explicit parameters, random
seeds, data provenance, and meaningful tolerances; then build the notes around
those outputs. Record which results were rerun and which were reused. Static
figures and small browser interactions are sufficient for v1; there is no
requirement for a hosted notebook kernel or GPU service.

MyST supports a static HTML export, and its documented deployment requires the
destination base path at build time. The owner-selected base is `/math/`; the
configured build uses `BASE_URL=/math myst build --html --strict --ci` via
`npm run build`. The pinned HTML build passes locally in this environment; see
the [verification record](../records/phase-0-1-verification.md).
[MyST static export](https://mystmd.org/guide/deployment),
[MyST GitHub Pages deployment](https://mystmd.org/guide/deployment-github-pages).

## Hub deployment

Use `xshi19.github.io` as the assembly and publishing boundary described above.
The planned publication sequence is:

1. Build an immutable, reviewed math artifact from a recorded `xshi-math` commit.
   Include source revision, toolchain versions, and an artifact checksum in its
   publication record.
2. Start from the current hub revision. Replace only the owned `math/` output
   directory; add the exact compatibility pages authorized by the URL manifest.
   Preserve the personal landing page and Normix output except for separately
   reviewed navigation or theory-link changes.
3. Validate the assembled root with all hosted prefixes present. Publish a single
   combined hub revision/artifact, so a math update cannot erase a sibling site.
4. Serialize hub writes and deployments. On a concurrent update, rebuild the
   staged assembly from the latest hub revision and rerun its checks. Do not
   resolve this by force-pushing a stale hub checkout.

For v1, updating generated files in the hub fits its existing role. Cross-repo
writes need credentials scoped to the destination and a deliberate trigger; a
source repository token should not be assumed to authorize hub writes. A later
hub workflow could pull immutable artifacts instead. Choose the transfer method
after inspecting the current publishers, not by installing a second competing
Pages deployment now.

GitHub's Pages Actions path separates artifact building from publication and
documents deployment permissions and environment protection. If that path is
chosen, configure it in the hub after the local build works.
[GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

The [light inventory](phase-0-inventory.md#hub-publishing-findings) identifies
Incerto repository Pages deployment, Normix writers of its own `gh-pages`, and
successful hub dynamic Pages runs alongside committed artifact trees. None of
the inspected source workflows writes the hub repository. The transfer/root
writer, exact hub Pages settings, live-prefix precedence, and coordinated
serialization remain open before implementing artifact transfer.

## URL strategy

**Resolved by the owner:** `/math/` is the stable public base, independent of
the repository name. Keep `/` as the personal hub and `/normix/` as the package/API
entry point.
Use explicit, globally unique page slugs within the math site. A flat slug such
as `incerto-pareto` avoids relying on source-directory nesting to produce nested
web routes. The source tree can remain organized by track.

| Public route | Intended behavior |
| --- | --- |
| `/` | Personal hub with links to math and package documentation |
| `/math/` | Selected math base and future landing page |
| `/math/incerto` | Configured Incerto track entry |
| `/math/information-geometry` | Configured Information Geometry track entry |
| `/math/normix-theory` | Configured Normix theory track entry |
| `/normix/` and retained API routes | Continue serving the package documentation |
| `/incerto-wiki/` | Continue serving the old site until cutover; then compatibility entry to `/math/incerto` |
| Inventoried old Incerto pages and moved Normix theory pages | Individual mappings to corresponding new pages, including fragments |

The base path is decided; the three track routes are configured in the scaffold,
while migration destinations remain proposals. None of the new math routes has
been deployed by this work. Confirm the generated URL form, including trailing
slash and `.html` variants, in the static-host rehearsal.

Do not derive the migration map from Markdown filenames alone. Inventory the
actual published pages, redirects, fragments, downloads, and source links as
well as the source table of contents. Generated names such as `index-1` and
chapter-number slugs need explicit mappings. An old Pareto page should land on
its new Pareto explanation, not just on the math home page.

Preserve explicit theorem, equation, and section IDs when possible. Otherwise,
record old-to-new fragments. Generate internal links from source labels; record
external Normix API targets and the version of `normix` used in the demo. Give
each new page its intended canonical URL and remove stale private edit/source
links from published metadata.

Static compatibility pages should provide a visible destination link and a
canonical link, with an HTML redirect and, when needed, a small script to preserve
query strings and translate fragments. Do not assume a static Pages deployment
provides configurable HTTP 301 rules. Test direct navigation, old `.html` paths,
browser refresh, fragments, and navigation without JavaScript. Retain compatibility
pages long term; removing them is a separate URL-breaking decision.

The former `/math/` versus `/xshi-math/` question is closed: use `/math/` when
freezing the URL map. Do not publish both as competing canonical sites.

## One-time consolidation phases

“一次性全合” means completing the eligible consolidation as one bounded program,
with one coordinated public cutover and one authoring home afterward. Several
preparatory changes make that cutover reviewable. Excluded private material and
Normix's independent software product remain outside the consolidation boundary.

| Phase | Work | Exit gate |
| --- | --- | --- |
| 0. Inventory and decisions — light scope done | Classify source material; record source revisions, rights, Python consumers, actual URLs, build differences, and all hub writers; apply the adopted MIT scope and `/math/` base | Representative sample and unknowns recorded; full candidate/rights/consumer coverage remains required before import, with rollback artifacts before cutover |
| 1. Working foundation — local HTML gate complete | Add the minimal site and Python scaffold with the selected `src/math/` directory and adopted import mapping, shared style, original sample pages for the three tracks, and only useful rules/skills | Fresh-environment MyST build works with `BASE_URL=/math`; one demo runs; cross-track references and actual static output are inspected; commands are recorded where implemented |
| 2. Complete eligible preparation | Export rights-cleared Incerto material and selected Normix theory/demos; reconcile notation/citations; move corresponding tests and optional Lean units | All eligible manifest entries are accounted for; semantic review and relevant execution succeed; private/source-license audit covers staged source and output |
| 3. Publication rehearsal | Assemble `/math/` and compatibility routes beside the existing hub and Normix artifacts; review the cutover diff | Direct URLs, fragments, assets, search, downloads, and mobile pages work; sibling output is preserved; rollback is rehearsed |
| 4. Coordinated cutover | Briefly freeze affected source authoring, import the final delta, rerun gates, publish the reviewed hub revision, update sibling links, and disable obsolete publishers | Public math and legacy entry paths work; only the new repo is edited for moved material; old publishers cannot overwrite compatibility pages |
| 5. Stabilize and prune | Check the live artifact, resolve remaining mapped-link defects, archive superseded guidance, and remove duplicate build paths | Publication evidence is recorded; compatibility and rollback artifacts are retained; each fact/rule/recipe has one owner |

If preparation reveals a new issue, stay before the relevant gate; the old site
continues serving. If cutover fails, restore the recorded combined hub artifact
and its route behavior, then coordinate which source remains authoritative before
resuming edits. Keep the private source repository and prior hub artifacts for
recovery. A public content leak cannot be undone by a site rollback, which is why
source and artifact review precede publication.

## Risks and mitigations

| Risk | Mitigation and evidence |
| --- | --- |
| Private material or unclear licenses cross into public history | Sanitized export, rights disposition, staged-file and built-output inspection; apply the owner-controlled Incerto MIT decision, retain copyright notices, and identify third-party exceptions |
| Internal package shadows stdlib `math` | Maintain explicit `xmath` mapping for `src/math/`; check stdlib resolution in editable and wheel installs before numerical work |
| Legacy links or fragments break | Inventory published routes, preserve labels, test a complete mapping against static output |
| Independent publishers overwrite the hub | Explicit prefix ownership, assembly from latest revision, serialized publication, rollback of the combined artifact |
| Sphinx/MyST differences change equations or reference behavior | Representative directive and equation checks before bulk adaptation, then rendered review of changed material |
| Notebook outputs look plausible but no longer reproduce | Pinned inputs/dependencies, reruns of affected demos, checks of known cases and numerical error |
| Two copies of theory or guidance diverge | One canonical source, explicit links/adapters, disable obsolete authoring and publishing paths at cutover |
| Lean work becomes a prerequisite for all progress | Independent toolchain and explicit proof status; formalize only useful bounded statements |
| A large import hides unfinished work | Complete manifest accounting with move/adapt/stay/exclude decisions and phase gates, rather than blanket claims of completeness |

## V1 non-goals

- Moving or vendoring the Normix JAX package, changing its API, or merging its
  package release process into `xshi-math`.
- Publishing private Git history, reproducing source books, or importing every
  draft and downloaded dataset.
- Formalizing every result in Lean or presenting unchecked statements as proofs.
- Building a custom publishing framework, a theme fork, a notebook service,
  a unified search service across repositories, or a new public Python package.
- Maintaining simultaneous editable copies of migrated content or separate
  skill bodies for Codex and Cursor.
- Installing speculative CI, autonomous maintenance loops, or agent review panels
  before there is working code and a demonstrated need.

Current checks are recorded in the [foundation verification record](../records/phase-0-1-verification.md).
Phase 2 and later remain pending. Add publication evidence only when those
phases actually run; this plan establishes their completion contracts.
