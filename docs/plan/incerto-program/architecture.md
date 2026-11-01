# Integration design

Everything labeled proposed below is future work. The current tree and build
were inspected at the revision recorded in [README.md](README.md).

## Scope and deliverable order

The two technical books and mathematical papers define completion.
*Statistical Consequences of Fat Tails* / *Technical Incerto* uses the verified
2025 third edition, arXiv:2001.10488v4, and runs chapter by chapter before
*Dynamic Hedging*. Stochastic calculus covers only basics needed to explain
the hedging concepts. The five non-technical books can supply cited origin
references only. Retained out-of-scope IDs carry no page or evidence obligations.

For every active concept, complete website math teaching first, Python demos,
numerical illustrations, visualizations or worked cases second, and optional
Lean last. `state.yaml` stores this order and required/status flags per concept.
An existing page still needs mathematical review; an existing demo still needs
its results checked. A Lean library gap must not defer either deliverable.
Record `skipped-for-now` and the missing support at the exact claim scope.
Continuous-time claims currently have no established pinned-library support
in this project. Teach and illustrate only the selected basics needed for the
hedging concepts; an advanced formal development is outside the required scope.

M0.5 reviews the 24 existing concept bodies before SCoFT v4 chapter 1.
The optional exceedance pilot belongs to chapter 2 after teaching and demos.
Astra max owns claim review and Math Site Editor owns live reader review.
The [review contract and issues list](m0.5-review.md) records coverage and
findings for Xiang. After every later site update, Math Site Editor reads the
corresponding live pages and records the deployed revision, URLs and findings
in `docs/records/incerto-site-review-YYYY-MM-DD.md` (future records). A build
result alone does not close the reader-review gate.

## Chapter chunks and source identity

Schema 3 makes `chunks` insertion order the execution order: M0.5, SCoFT v4
chapters 1–30, Dynamic Hedging chapters 1–23, then closeout. Each chapter has
one chunk with title, locator, concepts, teaching/demo/optional-Lean flags,
dependencies, role, status and existing pages reused. Attached appendices,
modules and papers are explicit source lists within that chunk.

Active SCoFT source IDs use `scft-v4-*`. Old `scft-*` IDs are v2 correspondence
keys only; never silently reinterpret an old chapter ID under the new edition.
Concept IDs stay unchanged. Human source views link the active v4 namespace.

Use one canonical page per concept, extending it at later chapter scopes.
Concept prerequisites can use reviewed pages or a bounded cited lemma; they
do not reorder execution. Store claim IDs, completed/pending deliverables,
checks, source revisions and the next action in each implementation checkpoint.
See [templates](templates.md#chapter-checkpoint) and [validation](validation.md).

## Current repository contract

The four explicit MyST TOCs build a landing project and independent Incerto,
IG and Normix theory projects. `myst.yml` extends the landing configuration;
`myst.incerto.yml` selects the Incerto hub and flat body files. `docs/plan/` is
neither in a TOC nor in the site's page glob. This design therefore adds no
rendered pages and needs no build configuration change.

Incerto currently has 28 rendered pages: one hub, three concept indexes and
24 concept bodies. The whole site has 52 pages at this baseline. These are
observations, not constants for future code to preserve. The build/check
scripts derive membership from the track globs and explicit TOCs.

`scripts/build_sites.py` builds the four projects sequentially, supplies their
base paths, stages the exports, and assembles `_build/html/`. The redirect
scripts also generate flat `/math/` compatibility pages and the separate
legacy Incerto compatibility tree. `scripts/check_html.py` checks page and
search membership, assets, links, KaTeX and compatibility behavior. Do not run
concurrent builds against the same `_build/` directory.

The Python distribution is `xshi-math`; its import is `xmath`, mapped explicitly
to `src/math/` by setuptools. It currently has one public exceedance helper,
NumPy, pytest in the dev group, and a fixed synthetic demonstration. There is
no Lean tree, CI workflow, notebook infrastructure or bibliography file.

## Proposed layout

```text
content/
  incerto/index.md                       # existing track hub
  incerto-<concept>.md                   # existing convention; one concept home
  incerto-<concept>-theorem.md            # only when a proof merits its own page
  incerto-<concept>-demo.md               # only when a demo merits its own page
  incerto-<study>-study.md                # observed-data study, when authorized
src/math/                               # existing physical home of xmath
  __init__.py
  incerto/                              # proposed only when reusable code grows
    __init__.py
    <method>.py
demos/incerto/                          # existing script-first demonstration home
  exceedances.py
  <experiment>.py
  notebooks/                            # optional later; thin views of helpers
    <study>.ipynb
tests/                                  # existing tests; new tests follow helpers
  test_<method>.py
assets/figures/incerto/                  # proposed original, reproducible figures
data/incerto/<study>/                    # proposed metadata/manifest; data only if licensed
lean/                                   # optional, last; absent today
  lean-toolchain
  lakefile.toml                         # or lakefile.lean, choose one
  lake-manifest.json
  XshiMath.lean                          # imports every checked project module
  XshiMath/Incerto/Exceedances.lean       # optional SCoFT v4 chapter 2 pilot
  README.md
docs/records/                           # future check and study evidence records
docs/plan/incerto-program/               # this design and resumable state
  m0.5-review.md                         # pending review contract and issues list
```

These are path conventions, not instructions to create empty directories.
Use the existing page for the optional chapter 2 pilot; theorem and demo
templates can be sections within one concept page. Avoid one file per book chapter, duplicate canonical
concepts, or empty pages made solely to complete a checklist. Do not introduce
`content/concepts/`, a `reading-guides/` tree, or nested track body directories.

Cross-track foundations stay at their present homes. Mixture definitions link
to `content/normix-normal-mixtures.md` and related Normix theory notes;
conditional expectation and exponential-family foundations link to IG.
Normix's JAX implementation and `/normix/` package documentation remain
upstream. New original Incerto hedging notes do not authorize importing Normix
finance code, API documentation, or deferred historical Incerto material.

## Lean evidence and workflow

Select compatible released Lean and Mathlib versions when implementation
starts; commit the toolchain file, dependency configuration and lake manifest.
Do not put a guessed future version in this design or follow an unpinned
branch. Use the official [Lake reference](https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/)
and inspect declarations in the selected [Mathlib](https://leanprover-community.github.io/mathlib4_docs/)
checkout. A search in current online documentation does not establish support
in the pinned revision.

The future README should give exact setup, cache and build commands. The
expected local sequence is `lake exe cache get` followed by `lake build` from
`lean/`, with failure on warnings configured and tested for that toolchain.
`XshiMath.lean` imports every project proof module so an unimported file cannot
silently escape the default build. Audit declarations for the intended
quantifiers, nonempty domains, integrability, independence and convergence
mode. Record `#print axioms` results or equivalent dependency evidence and
review the normal logical axioms separately from accidental assumptions.

Reject `sorry`, `admit`, `sorryAx`, new placeholder axioms and unchecked theorem
assumptions used to bypass the intended result. A text scan is a supplement to
the compiler and dependency audit, not proof of soundness. Record theorem
names, module, repository revision, Lean version, Mathlib revision, build
result, and exact covered statement in a future record. Link a checked page
to that immutable source declaration. Do not add public “Lean pending” badges
or imply every claim on a page is certified.

Lean remains optional for curriculum completion and independent of
`npm run build` and `uv run pytest`. If the optional chapter 2 pilot is
attempted, evidence must cover its two approved declarations before calling
the pilot complete. A recorded skip leaves chapter closure and the next
chapter available. All Lean work follows teaching and numerical delivery.
Evidence attaches to exact declarations; owner approval of that scope is
recorded in state and does not need to be requested again. Once the subtree
actually exists, update its guidance and the
root verification commands in the same authorized implementation change.
This design does not edit those routers or declare a passing formalization.

## Python and experiments

Keep `uv sync --locked`, `uv run pytest`, and installed `xmath` imports. Never
set `PYTHONPATH=src`: `src/math` must not shadow the standard-library `math`
module. If a future `xmath.incerto` subpackage is needed, explicitly add it and
its directory to the setuptools package list/mapping; test editable and wheel
installs in isolation and run `uv build`. The optional exceedance pilot
requires no packaging change.

Use functions for reusable numerical methods and scripts for experiments.
Every stochastic experiment declares its generator, seed, sample sizes,
replications, runtime bound, truncation rules and uncertainty summaries.
Avoid unstable assertions about one random draw. Tests should check numerical
invariants, analytic special cases, edge cases and error handling; a plot's
appearance or a mirrored implementation test is insufficient. Heavy-tail
experiments must expose overflow, censoring, non-finite outputs and changes in
the statistic's existence across parameters.

Keep synthetic/fixed examples distinct from observed-data studies. A simulated
Cauchy path is `numeric-demo`, even if an older TOC calls its section empirical.
For an actual study, record source URL, version/retrieval date, license,
checksum, units, population, inclusion/exclusion rules, cleaning, missingness,
adjustments, time zone, dependence and train/test separation where applicable.
Commit a small permitted fixture and a manifest when appropriate. Large or
restricted raw data stay outside Git; a lawful acquisition step produces a
checksum-verified local input. Never fetch financial data during MyST rendering.

Financial inputs come from the Portfolio Manager bot and Xiang's financial
database; request missing series or fields there. Other data come from the
Data Scientist bot. Record the bot request or handoff alongside original
provider provenance. This routing decision is settled; it does not replace
the license and redistribution check for each dataset.

Notebooks are optional presentations, not a second implementation. Keep shared
logic in installed helpers; execute with a declared kernel and clean outputs
before checking in a permitted artifact. Add Jupyter, SciPy, plotting or data
dependencies only for an actual approved use, in suitable optional/dev groups
with `uv.lock` updated. Matplotlib is not currently a dependency despite older
visual-style guidance assuming it. Preserve that guidance's legibility and
consistent visual style without assuming its historical figure modules exist.

## MyST, figures and page membership

Add a new body to `myst.incerto.yml` and the appropriate existing concept index.
Frontmatter `title` and stable MyST labels follow current pages; do not rely on
a `slug` field to override the filename-derived route. Python output and
figures are generated in an explicit reproducibility step, then referenced by
the note. The normal site build consumes static artifacts; it need not execute
Lean, notebooks, long simulations or data acquisition.

Use original vector figures for mathematical diagrams and plots when useful.
Link script, parameters and result record; provide a caption that distinguishes
theoretical curves, simulations and observed data. Place future assets under
the chosen figures directory and confirm that the MyST export copies them
with the correct track base path. Do not assume arbitrary source files outside
the content tree will become downloadable assets. Link code and Lean modules
to immutable repository URLs unless a deliberate downloadable artifact is
added and verified.

The HTML checker currently exempts named hub/index/notation pages from its
math-output requirement through `NO_MATH`. A future prose-only concept needs
an explicit, reviewed exemption or a deliberate metadata-aware replacement.
Do not add meaningless equations to satisfy the checker. Any such site-code
change belongs to that later content batch, with focused checks.

## URLs, notation and publication boundaries

| Concern | Contract |
| --- | --- |
| Public homes | Landing `/math/`; Incerto `/math/incerto/`; IG `/math/ig/`; Normix theory `/math/normix-theory/`. |
| New Incerto body | `content/incerto-<name>.md` → `/math/incerto/incerto-<name>/`. The paths in state are proposals until the file and build exist. |
| Same-track references | Relative Markdown file links and stable labels; check rendered fragments. |
| Cross-track references | Full public URL, for example `https://xshi19.github.io/math/notation/`. Root-absolute `/math/...` links can be prefixed twice by the current build. |
| MyST base path | The build supplies each project's `BASE_URL`. Keep the configured domain host-only; do not encode a second path prefix. |
| Flat compatibility | The build generates `/math/incerto-<name>/` redirects for discovered prefixed pages. Preserve existing behavior and check new destinations. |
| Legacy URL map | `docs/plan/url-map.csv` describes actual old routes and dispositions. Add rows only after inventorying a genuine old URL and verifying its destination; never populate it with unbuilt planned pages. |
| Retained unknowns | `incerto-scoft-intro` and `hub-incerto-home-export` keep their unresolved dispositions. This original-writing program supplies no rights clearance or replacement redirect for them. |
| Publication | Local build is not hub publication. Later transfer follows the hub-publish skill and cutover runbook, preserving the live `/incerto-wiki/` mirror, compatibility pages and `/normix/`. |

Use [the notation canon](../../../content/notation.md) and
[shared-notation rule](../../rules/shared-notation.md): `P`, `P_θ`, `F`, `F̄`,
`E`, `Var`, `Cov`, `α` for the positive tail exponent, `ξ` for extreme-value
index, `u` for threshold, `x_m` for Pareto minimum, `e(u)` for mean excess and
`L` for a slowly varying function. `ξ = 1/α` has a restricted domain. Do not
reuse `α` as an unqualified significance level, `L` as an unexplained loss,
or statistical `θ` as an unqualified time-decay Greek. Map local financial
Delta/Gamma/Theta conventions explicitly; lowercase Normix parameters already
have meanings. Extend the shared canon before publishing genuinely new shared
notation. Mixture `Y` and source-specific `W` also need an explicit mapping.

## Checks and possible CI

No workflow is installed now. When implementation starts, use independent jobs
so a numerical or site success cannot stand in for a proof build. Pin versions
and cache keys from committed lock/toolchain files. Do not add automatic hub
deployment to this program's CI design.

| Job / trigger | Future check contract |
| --- | --- |
| Plan changes | Parse state with a pinned YAML parser; validate IDs, scope/disposition, deliverable order, review gates, references, dependency graphs, classifications, source mappings and active/retained counts as described in `validation.md`. |
| Lean changes | Restore the pinned toolchain/cache, build the imported root with warnings treated as errors, reject placeholders, audit changed statements and dependencies. |
| Python/helper changes | `uv sync --locked`, `uv run pytest`, bounded affected demos; for mapping/package changes also `uv build` and isolated editable/wheel import checks. |
| Content, assets or site changes | Node version satisfying `>=20`, `npm ci`, `npm run build`, then `npm run check:html`; review equations, citations, figures and desktop/mobile navigation under `/math/`. |
| Every site update | Math Site Editor reviews the corresponding live pages as a reader after deployment and records findings and dispositions. |
| Notebook/study changes | Execute the bounded reproducible fixture with declared dependencies and verify provenance; full-data runs are separate if access, scale or rights require it. |

Keep existing npm commands unchanged by default. If aggregate wrappers are
later useful, propose explicit `check:lean` and `check:python` wrappers only
after their underlying commands exist; `build` must remain the site build.
MyST's initial theme/DOI fetches may need network even after `npm ci` succeeds.
Record blocked checks honestly and rerun them outside the restricted sandbox
before accepting publication. A workflow file is a contract until a real run
has passed.

## Chapter-10 implementation note (2026-10-29)

`content/incerto-sp500.md` is the diagnostics home; `incerto-sp500-tail.md`
continues to own data access and tail fitting. `incerto-ml-econometrics.md`
owns the F/G estimator and hinge arguments. Both reuse the existing installed
package, shared figure exporter and cache loader. No financial data are
distributed or fetched by builds/tests. The empirical gate remains open;
[the checkpoint](../../records/incerto-scft-v4-ch10.md) separates it from
completed teaching and deterministic tests. Appendix I remains chapter 22.

## Chapter-11 implementation note (2026-10-30)

`incerto-calibration-payoff.md` owns event/payoff identification, Brier
calibration and exact score laws. `incerto-point-forecast.md` owns the scoped
amount-loss comparison and will extend in chapter 12. Both link existing
payoff, moment and hinge pages. `src/math/incerto/calibration.py` uses the
existing installed-package mapping; the demo uses the shared figure helpers.
No dependency, data source, network call, or Lean subtree is added.

## Chapter-12 implementation boundary

The [chapter-12 checkpoint](../../records/incerto-scft-v4-ch12.md) extends
`c-point-forecast` in its existing canonical page. `incerto-scoft-ch12.md`
is a reading guide, not a new concept body. The helper module
`src/math/incerto/forecasting.py` supplies stable scales, quantile losses,
endpoint transforms and bounded-budget repeated Pareto scoring. It reuses
the calibration loss evaluator and the shared figure exporter.

The zero-lower-endpoint transform is elementary chapter-12 context. This
work does not implement chapter-17 shadow-mean fitting or chapter-18
historical estimation. Pandemic examples use synthetic laws only. No new
concept IDs, notation conventions, data pipeline or Lean subtree is added.
