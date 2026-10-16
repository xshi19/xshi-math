# Incerto program

Design baseline: 2026-10-16, branch `plan/incerto-program`, inspected revision
`998a4a11a17b7ae7ba4c306005a4c8e3109f4392`. This directory proposes future work.
It adds no public pages, Lean project, Python helpers, datasets, or CI workflows.
Implementation needs a later task; this plan does not execute a future phase.

The program gives the five Incerto books, *Statistical Consequences of Fat
Tails* / *Technical Incerto*, and *Dynamic Hedging* a shared concept curriculum
under `/math/incerto/`. The initial map has **7 books, 125 numbered chapters,
187 book source units including thematic sections and supplements, 14 papers,
and 101 unique concepts**. Twenty-four concepts already have an Incerto body
page. None has a checked Lean artifact in this repository.

Coverage is concept based: recurring ideas have one canonical explanation,
with several source locators. Mathematical statements should acquire checked
Lean 4/Mathlib support at the scope actually proved. Python supplies numerical
experiments and empirical analysis. Philosophical arguments, ethical premises,
and observations remain separately identified; Lean cannot validate them by
checking a related toy model.

## Read and resume

| File | Purpose |
| --- | --- |
| [Inventory](inventory.md) | Book → chapter or section → concept, plus the selected papers |
| [Concept register](concepts.md) | Scope, evidence classification and justification, existing coverage, proposed home, lead and milestone |
| [Architecture](architecture.md) | Future Lean/Python/page layout, build and check integration, notation and URL constraints |
| [Templates](templates.md) | Concept, theorem, demo and empirical-study page contracts and citations |
| [Sources](sources.md) | Edition baselines, locator evidence, source-review limits and copyright boundary |
| [State](state.yaml) | Canonical IDs, relationships, statuses, roles, milestones and next chunk |
| [Validation](validation.md) | State semantics, validation procedure and resume rules |
| [Verification](verification.md) | Checks performed on this design and remaining limits |

Resume at `state.yaml` → `next_chunk` → `#/chunks/m1-scope`. Before implementation,
read the current router, track guidance, relevant rule and skill again: this
design records a baseline, not a replacement for current repository instructions.
The manager can run the independent `edition-review` chunk before content work.

## Decisions fixed by this design

- Write original explanations, derivations, proofs, figures and code. Cite the
  book and chapter; never copy or closely paraphrase its text, reconstruct an
  aphorism collection, or include long quotations. Public availability of a
  source does not authorize importing it.
- Keep flat `content/incerto-*.md` bodies and the existing track hub. Book
  mappings are relationships, not seven new page trees. The plan stays outside
  the MyST TOCs.
- Propose `lean/` as the future Lean root. Preserve the installed Python name
  `xmath` and its current `src/math/` mapping. Use scripts before notebooks.
- Keep `/math/incerto/`, the shared notation canon, the hub's `/incerto-wiki/`
  mirror, and the Normix package boundary. No legacy route is resolved by this
  proposal. New original writing does not clear deferred source imports.
- Treat source editions as versioned inputs. The 2010 Procrustes thematic map
  and 2020 Technical Incerto print map are baselines. Expanded-edition coverage
  remains explicit work, not an assumed match.
- Use the owner's future roles below. Do not rewrite the repository-wide model
  policy as part of this plan.

| Role ID | Owner assignment | Work |
| --- | --- | --- |
| `astra-max` | Codex GPT-6-Astra, max | Hard mathematics, Lean and design |
| `astra-xhigh` | Codex GPT-6-Astra, xhigh | Writing and complex code |
| `cursor-grok` | Cursor Grok 4.7, xhigh | Simple code, review and site code |
| `math-site-editor` | Math Site Editor | Manager: source checks, scope, sequencing and evidence records |

The owner specified no Cursor third-party models. These assignments do not
assert client availability, create a new executable manager, or authorize
automatic delegation. Astra max was explicitly selected for this design run.

## Milestones

Milestone numbers express a proposed sequence. The manager selects one bounded
chunk at a time. An existing page can support a later chunk without its entire
advanced formalization being finished. Concept dependencies describe the
mathematics; chunk and milestone dependencies control execution.

| Milestone | Scope and exit gate |
| --- | --- |
| M0 — design | Inventory, architecture, templates and resumable state reviewed; actual validation limits recorded. No implementation. |
| M1 — one-concept pilot | Two exact finite-count results on the existing exceedance page, one imported Lean module, pinned toolchain, existing Python example, precise source links and independent checks. Detailed contract below. |
| M2 — queued estimation work | Preserve the existing queue: Moment-Estimation Failure, then Inference Asymmetry; add the bounded Cauchy simulation after its source locator is reconciled. Review the existing Pareto-moment, plug-in, threshold and catalog notes as needed. Each new mathematical claim has its own proof-scope decision. |
| M3 — decisions and interpretation | Develop a small shared spine for the five Incerto books: asymmetric payoffs, convexity/fragility, ruin, optionality, agency and selection. Add interpretive notes from the chapter map in separate batches. Review biological and behavioral evidence before making such claims. |
| M4 — estimation and empirical work | Scope Gini, quantile shares and the separately decided shadow-mean note. Then choose one licensed dataset for a reproducible study; equity returns precede historically uncertain conflict or epidemic data. Keep data acquisition separate from the site build. |
| M5 — finite-model hedging | Begin with payoff algebra, finite-state arbitrage and local sensitivities. Add discrete hedging and contract families in separate units. Continuous stochastic calculus is not an M5 prerequisite or promised deliverable. |
| M6 — advanced proofs and coverage audit | Audit Mathlib feasibility before committing to regular variation, EVT, stable limits or continuous-time pricing. Reconcile all selected editions and paper sections; close source units only after reviewing their mapped scope. Record any remaining informal claims instead of calling the series fully verified. |

M3 and M4 both depend on M2; M5 follows M3. M6 follows M3–M5. This is a roadmap,
not a schedule or an estimate of advanced formalization cost. Advanced
concepts may supply a cited prerequisite before their M6 proof work.

### Milestone 1: exact scope

Use the original [counting-exceedances page](../../../content/incerto-counting-exceedances.md),
`xmath.exceedance_fraction`, and `demos/incerto/exceedances.py`. No new concept
page, data source, numerical helper or general probability theorem is needed.

For an integer `n ≥ 1`, observations `x : Fin n → ℝ`, and a real threshold `u`,
define the fraction by the cardinality of `{i : Fin n | x i > u}` divided by `n`,
with explicit casts to `ℝ`. Proposed results:

1. The fraction lies in `[0, 1]`.
2. For real `u ≤ v`, the fraction at `v` is at most the fraction at `u`.

The existing page uses local threshold `t` and notation `Ŝ_n(t)`. Preserve its
meaning while recording the mapping to the canon's threshold `u`. The strict
comparison is essential: the sample `(1, 2, 2, 4)` at threshold `2` gives `1/4`.
Empty samples are outside the theorem's domain and remain rejected by Python.

Proposed declarations live in `lean/XshiMath/Incerto/Exceedances.lean`, imported
by `lean/XshiMath.lean`. The exact Lean names are chosen after the pinned
Mathlib search; this design does not claim they exist. The setup includes
`lean-toolchain`, `lakefile.toml` or `lakefile.lean`, `lake-manifest.json`, and a
README with actual commands. No blueprint or generated API website is needed.

Before proof coding, the owner confirms the informal claim as required by the
[Lean skill](../../../.agents/skills/xshi-math-lean-formalization/SKILL.md).
This confirmation belongs to a later implementation task, not an approval
request blocking the present design. The implementer then pins compatible
Lean/Mathlib revisions, proves both statements, audits their hypotheses and
axiom dependencies, and obtains a successful build. Only then does the page
link the checked declarations at an immutable repository revision.

Exit evidence: a clean imported Lean build without placeholders; statement
review; the existing demo outputs `1`, `1/4`, `0`; relevant Python tests; strict
site build and HTML checks; rendered equation and link review. If CI is added,
its Lean job must check the imported root and fail on proof placeholders.
The manager records local versus CI evidence separately. The proof establishes
real-number counting facts. It does not verify NumPy floating-point execution,
the population survival function, or any sampling theorem.

## Risks and open questions for Xiang

| Question or risk | Proposed default / consequence |
| --- | --- |
| Which physical/digital editions should define completion? | Keep the cited baselines for stable IDs; reconcile the 2016 Procrustes expansion and 2025 Technical Incerto additions before declaring book coverage complete. Do not invent missing chapter locators. |
| Is the one-concept M1 pilot the desired first implementation? | Use the two existing finite-count claims; defer larger probability results until the proof-to-page process has worked once. |
| How broad should a Lean-verified mathematical claim be? | Attach evidence per exact declaration. An algebraic special case never certifies an entire EVT theorem, estimator, empirical conclusion or philosophical argument. Advanced claims remain visibly cited/informal until checked. |
| How much of Shadow Mean belongs in its first note? | Preserve the existing separate scope decision: begin with the bounded transform and its assumptions; keep historical conflict estimates in a separate study. |
| Which empirical dataset and redistribution terms are acceptable? | Start with one explicitly licensed return series. Do not assume an accessible financial or historical dataset can be committed or redistributed. Resolve dataset and outcome definitions before collecting it. |
| How much stochastic calculus is worth building? | Audit the chosen Mathlib revision before promising continuous-time hedging. Finite-state and discrete-path mathematics provide useful independent milestones. |
| How broad should the paper corpus become? | Start with the 14 versioned records, including one critical response. Add papers for concrete claims, not to claim an exhaustive bibliography of Taleb's work. |
| How should interpretive coverage be judged? | Each mapped unit needs an original explanation or an explicit scoped omission. Avoid turning aphorisms into invented mathematical theorems. Historical, behavioral and biological assertions need their own primary evidence. |
| Who closes the old publishing and rights gates? | Existing owner actions remain in the planning index/runbook. This program neither archives `incerto-wiki` nor resolves its retained `intro/` and Markdown-download routes. |

The main practical risk is scope: 101 concepts are a backlog, not one writing
batch. Source-unit counts measure the map, not verified mathematical coverage.
Later runs should record a small completed claim or study with evidence, then
advance `next_chunk`.
