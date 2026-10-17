# Incerto program

Design baseline: 2026-10-16; owner revision: 2026-10-17 (PR #24).
Branch `plan/incerto-program`, inspected baseline revision
`998a4a11a17b7ae7ba4c306005a4c8e3109f4392`. This directory proposes future work.
It adds no public pages, Lean project, Python helpers, datasets, or CI workflows.
Implementation needs a later task; this plan does not execute a future phase.

Completion covers **2 technical books** and mathematical papers under
`/math/incerto/`. *Statistical Consequences of Fat Tails* / *Technical Incerto*
is the first and highest-priority book, including the 2025 additions.
*Dynamic Hedging* includes continuous time as teaching and numerical work.
The current technical map has **48 numbered chapters, 64 book source units,
14 papers and 72 in-scope concepts**. The 2025 reconciliation may add units
and concepts; these counts do not claim edition-complete coverage.

The five non-technical books (*Fooled by Randomness*, *The Black Swan*,
*The Bed of Procrustes*, *Antifragile* and *Skin in the Game*) are outside
completion scope. Use them only for a cited cross-reference when a technical
concept originates there. No interpretive or prose-only coverage is planned.
The register retains all **101 stable concept IDs: 72 in scope and 29
out of scope**, each exclusion with a reason. It also retains the five excluded
book records and their 123 source units (77 numbered chapters) as historical
references. Totals retained are 7 books, 187 units and 125 numbered chapters.
Twenty-four concepts already have body pages; none has checked Lean evidence.

Every active concept follows the same deliverable order: website math teaching
first; Python demos, numerical illustrations, visualizations or worked cases
second; optional Lean last. Missing Mathlib support is recorded as
`skipped-for-now` with a reason and does not reduce teaching or numerical scope.
Lean evidence applies only to the exact checked declaration.

## Read and resume

| File | Purpose |
| --- | --- |
| [Inventory](inventory.md) | Book → chapter or section → concept, plus the selected papers |
| [Concept register](concepts.md) | Scope, evidence classification and justification, existing coverage, proposed home, lead and milestone |
| [Architecture](architecture.md) | Future Lean/Python/page layout, build and check integration, notation and URL constraints |
| [Templates](templates.md) | Concept, theorem, demo and empirical-study page contracts and citations |
| [Sources](sources.md) | Edition baselines, locator evidence, source-review limits and copyright boundary |
| [State](state.yaml) | Canonical IDs, relationships, statuses, roles, milestones and next chunk |
| [M0.5 review](m0.5-review.md) | Pending claim and live reader reviews of 24 pages; issues list for Xiang |
| [Validation](validation.md) | State semantics, validation procedure and resume rules |
| [Verification](verification.md) | Checks performed on this design and remaining limits |

Resume at `state.yaml` → `next_chunk` → `#/chunks/m0.5-review`. Before implementation,
read the current router, track guidance, relevant rule and skill again: this
design records a baseline, not a replacement for current repository instructions.
The manager can run the independent `edition-review` chunk before content work.

## Decisions fixed by this design

- Write original explanations, derivations, proofs, figures and code. Cite the
  book and chapter; never copy or closely paraphrase its text, reconstruct an
  aphorism collection, or include long quotations. Public availability of a
  source does not authorize importing it.
- Keep flat `content/incerto-*.md` bodies and the existing track hub. Book
  mappings are relationships, not new book page trees. The plan stays outside
  the MyST TOCs.
- Propose `lean/` as the future Lean root. Preserve the installed Python name
  `xmath` and its current `src/math/` mapping. Use scripts before notebooks.
- Keep `/math/incerto/`, the shared notation canon, the hub's `/incerto-wiki/`
  mirror, and the Normix package boundary. No legacy route is resolved by this
  proposal. New original writing does not clear deferred source imports.
- Keep the 2020 Technical Incerto locator namespace while reconciling the
  required 2025 additions. Edition reconciliation is about exact coverage,
  not whether to include that edition.
- Obtain financial data from the Portfolio Manager bot through Xiang's
  financial database; request additions there. Obtain other data from the
  Data Scientist bot. Record licensing and provenance for every dataset.
- Add papers on demand when a concrete mathematical claim needs them. The
  existing 14 versioned records are a starting set, not an exhaustive target.
- After every site update, the Math Site Editor reviews the corresponding live
  pages as a reader and records findings. Local build checks do not close this
  gate; see the [review contract](m0.5-review.md#standing-live-review-rule).
- Use the owner's future roles below. Do not rewrite the repository-wide model
  policy as part of this plan.

| Role ID | Owner assignment | Work |
| --- | --- | --- |
| `astra-max` | Codex GPT-6-Astra, max | Hard mathematics, M0.5 claim review, optional Lean and design |
| `astra-xhigh` | Codex GPT-6-Astra, xhigh | Writing and complex code |
| `cursor-grok` | Cursor Grok 4.7, xhigh | Simple code, review and site code |
| `math-site-editor` | Math Site Editor | Manager, source checks, live reader review and evidence records |
| `portfolio-manager` | Portfolio Manager bot | Financial data from Xiang's database; requests for additions |
| `data-scientist` | Data Scientist bot | Other data requests |

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
| M0.5 — existing-page review | Astra max reviews every mathematical claim in the 24 existing concept bodies. Math Site Editor reads all 24 corresponding live pages. Deliver the [issues list for Xiang](m0.5-review.md), with coverage, evidence, severity and proposed actions. Findings affecting M1's claims must be resolved before the pilot. |
| M1 — approved one-concept pilot | After M0.5, review the exceedance teaching page and run its existing Python example, then formalize the two approved finite-count results in one imported Lean module. Detailed contract below. |
| M2 — Technical Incerto teaching and numerics | Prioritize SCoFT: Moment-Estimation Failure, then Inference Asymmetry, then the bounded Cauchy simulation after locator reconciliation. Continue its tail, limit and inference mathematics as website explanations and numerical work. Advanced Lean feasibility does not postpone these deliverables. |
| M3 — estimation, paper models and data studies | Gini, quantile shares and the separately scoped Shadow Mean note; mathematical fragility/response/dependence models from papers; reproducible data studies through the assigned bots. Equity returns precede conflict or epidemic studies. No narrative, clinical or policy coverage. |
| M4 — Dynamic Hedging teaching and numerics | Payoff algebra, arbitrage, Greeks, discrete hedging, contract families and continuous-time stochastic calculus/pricing. State assumptions and numerical limitations. Where Lean support is unavailable or unestablished, record `skipped-for-now`; teaching and numerics remain in scope. |
| M5 — technical coverage closeout | Reconcile the required 2025 Technical Incerto additions and exact technical book/paper locators. Close mathematical source scope after teaching and numerical evidence is reviewed. Optional Lean follows per declaration; record skipped claims and reasons without making formalization a completion gate. |

The sequence is M0 → M0.5 → M1 → M2 → M3 → M4 → M5. The former
interpretation milestone is removed; later milestones are renumbered, while
concept IDs remain unchanged. Concept dependencies may use a bounded cited
prerequisite before its fuller treatment. The approved M1 pilot has its own
Lean exit gate; completion of the wider curriculum does not require Lean.

### Milestone 0.5: review output

[m0.5-review.md](m0.5-review.md) defines the 24-page coverage matrix, claim log
and consolidated issues list. Each issue records a stable ID, source claim or
live URL/fragment, severity, finding, evidence, proposed action, reviewer and
disposition. Source review and live reader review are separate fields. This
revision creates the contract only; both reviews remain `todo`.

### Milestone 1: exact scope

Use the original [counting-exceedances page](../../../content/incerto-counting-exceedances.md),
`xmath.exceedance_fraction`, and `demos/incerto/exceedances.py`. No new concept
page, data source, numerical helper or general probability theorem is needed.

For an integer `n ≥ 1`, observations `x : Fin n → ℝ`, and a real threshold `u`,
define the fraction by the cardinality of `{i : Fin n | x i > u}` divided by `n`,
with explicit casts to `ℝ`. Approved statements:

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

Xiang approved this pilot and exact-declaration scope on 2026-10-17, satisfying
the informal-scope confirmation in the
[Lean skill](../../../.agents/skills/xshi-math-lean-formalization/SKILL.md).
Do not request that confirmation again for these unchanged claims. M0.5 comes
first; this planning revision does not start proof coding. A later implementer
reviews the teaching page and existing Python example, then pins compatible
Lean/Mathlib revisions, proves both statements, audits their hypotheses and
axiom dependencies, and obtains a successful build. Only then does the page
link the checked declarations at an immutable repository revision.

Exit evidence: a clean imported Lean build without placeholders; statement
review; the existing demo outputs `1`, `1/4`, `0`; relevant Python tests; strict
site build and HTML checks; rendered equation and link review; Math Site Editor
live reader review after any site update. If CI is added,
its Lean job must check the imported root and fail on proof placeholders.
The manager records local versus CI evidence separately. The proof establishes
real-number counting facts. It does not verify NumPy floating-point execution,
the population survival function, or any sampling theorem.

## Risks and open questions for Xiang

| Question or risk | Proposed default / consequence |
| --- | --- |
| How do the 2025 Technical Incerto additions map to the 2020 baseline? | Inclusion is settled. Reconcile exact chapter, appendix and claim locators from the source; retain existing IDs and do not invent locators. |
| How much of Shadow Mean belongs in its first note? | Preserve the existing separate scope decision: begin with the bounded transform and its assumptions; keep historical conflict estimates in a separate study. |
| How deep should the stochastic-calculus teaching and numerical treatment go? | Continuous time is included. Set the depth of exposition and worked cases; Mathlib support governs only optional Lean. |
| Who closes the old publishing and rights gates? | Existing owner actions remain in the planning index/runbook. This program neither archives `incerto-wiki` nor resolves its retained `intro/` and Markdown-download routes. |

The main practical risk is scope: 72 active concepts are a backlog, not one writing
batch. Source-unit counts measure the map, not verified mathematical coverage.
Later runs should record a small completed claim or study with evidence, then
advance `next_chunk`.
