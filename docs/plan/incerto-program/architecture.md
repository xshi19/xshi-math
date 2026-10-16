# Integration design

Everything labeled proposed below is future work. The current tree and build
were inspected at the revision recorded in [README.md](README.md).

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
lean/                                   # proposed; absent today
  lean-toolchain
  lakefile.toml                         # or lakefile.lean, choose one
  lake-manifest.json
  XshiMath.lean                          # imports every checked project module
  XshiMath/Incerto/Exceedances.lean       # M1's only mathematical module
  README.md
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
docs/records/                           # future check and study evidence records
docs/plan/incerto-program/               # this design and resumable state
```

These are path conventions, not instructions to create empty directories.
Use the existing page for M1; the theorem and demo templates can be sections
within one concept page. Avoid one file per book chapter, duplicate canonical
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

Lean remains optional for reading and independent of `npm run build` and
`uv run pytest`. Once the subtree actually exists, update its guidance and the
root verification commands in the same authorized implementation change.
This design does not edit those routers or declare a passing formalization.

## Python and experiments

Keep `uv sync --locked`, `uv run pytest`, and installed `xmath` imports. Never
set `PYTHONPATH=src`: `src/math` must not shadow the standard-library `math`
module. If a future `xmath.incerto` subpackage is needed, explicitly add it and
its directory to the setuptools package list/mapping; test editable and wheel
installs in isolation and run `uv build`. M1 requires no packaging change.

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
| Plan changes | Parse state with a pinned YAML parser; validate IDs, references, dependency graphs, classifications, source mappings and counts as described in `validation.md`. |
| Lean changes | Restore the pinned toolchain/cache, build the imported root with warnings treated as errors, reject placeholders, audit changed statements and dependencies. |
| Python/helper changes | `uv sync --locked`, `uv run pytest`, bounded affected demos; for mapping/package changes also `uv build` and isolated editable/wheel import checks. |
| Content, assets or site changes | Node version satisfying `>=20`, `npm ci`, `npm run build`, then `npm run check:html`; review equations, citations, figures and desktop/mobile navigation under `/math/`. |
| Notebook/study changes | Execute the bounded reproducible fixture with declared dependencies and verify provenance; full-data runs are separate if access, scale or rights require it. |

Keep existing npm commands unchanged by default. If aggregate wrappers are
later useful, propose explicit `check:lean` and `check:python` wrappers only
after their underlying commands exist; `build` must remain the site build.
MyST's initial theme/DOI fetches may need network even after `npm ci` succeeds.
Record blocked checks honestly and rerun them outside the restricted sandbox
before accepting publication. A workflow file is a contract until a real run
has passed.
