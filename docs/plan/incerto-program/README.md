# Incerto program

Design baseline: 2026-10-16. V4 chapter-order revision: 2026-10-17, branch
`plan/incerto-program`, PR #24; revision base `e7aaa5f`.
The owner authorized M0.5 review and clear source fixes on 2026-10-17.
M0.5 mathematical and live reader review are complete after published PR #27
(`fbf2c6a`). Chapter 1 implementation and max review are complete;
[its record](../../records/incerto-scft-v4-ch01.md) includes the later operator
build pass. Chapter 2 implementation and chapter-1 reader fixes are complete
on `scft/v4-ch02`; [its record](../../records/incerto-scft-v4-ch02.md) separates
completed max review from its later successful operator site checks.
Chapter 3 and the chapter-2 reader fixes are implemented on `scft/v4-ch03`;
[its record](../../records/incerto-scft-v4-ch03.md) lists the completed max review,
pending live review and blocked sandbox build.

The selected SCoFT baseline is the **2025 third edition,
arXiv:2001.10488v4: 30 chapters and nine appendices (A–I)**. Direct comparison
with the supplied v2 and v4 PDF tables of contents closes the 2025 locator
reconciliation. [Inventory](inventory.md#v2-to-v4-correspondence) records every
v2 correspondence and the six added units; [sources](sources.md) records the
evidence and title changes. Exact mathematical claims still need source review
within their chapter chunks.

Completion covers two technical books and attached mathematical papers under
`/math/incerto/`: SCoFT first, then *Dynamic Hedging*. The active map contains
**53 numbered chapters, 70 book source units, 16 papers and 75 concepts**.
All 101 previous concept IDs remain; two appended IDs bring the register to
**103 concepts: 75 in scope and 28 out of scope**. `c-lindy` is reactivated at
the technical scope of v4 chapter 23. The five non-technical books retain
123 historical source units and 77 numbered chapters for origin references
only. Totals retained: seven books, 193 units and 130 numbered chapters.
The M0.5 review inventory contains 24 concept bodies. Eighteen additional
Incerto pages, including indexes and reading guides, received an obvious-issue
skim; they do not enlarge that claim-review denominator. No checked Lean
concept was added.

Each numbered chapter is one resumable chunk: website teaching pages first,
Python demos and visualizations second, optional Lean last. Reuse canonical
concept pages across chapters; a chapter chunk is not a new page tree.
Record the chapter's claim scope and checkpoint so another run can resume it.
Lean omissions require a reason and never block the next chapter.

## Read and resume

| File | Purpose |
| --- | --- |
| [Inventory](inventory.md) | V4 chapter titles/locators, v2 correspondence, appendix/module hosts and attached papers |
| [Concept register](concepts.md) | Stable IDs, scope, source mappings, chapter chunks and evidence candidates |
| [Architecture](architecture.md) | Future page, Python and optional Lean integration |
| [Templates](templates.md) | Chapter checkpoint and teaching/demo/evidence contracts |
| [Sources](sources.md) | Edition evidence, title differences, bibliographic locators and copyright boundary |
| [State](state.yaml) | Canonical records, ordered chunks, dependencies and counts |
| [M0.5 review](m0.5-review.md) | Completed mathematical review of 24 pages, 448 claim/source/notation records, 15 issues; live review passed after PR #27 |
| [Validation](validation.md) | Schema, executable checks and resume procedure |
| [Verification](verification.md) | Historical evidence, this revision's checks and pending operator rerun |

`next_chunk` is `#/chunks/scft-v4-ch04`. Chapters 1–3 teaching,
deterministic Python examples and optional Lean skips are recorded in state.
There are now 28 implemented concept bodies; the M0.5 review denominator
remains its original 24 pages. Chapters 1–3 passed separate max review.
Chapter 3 awaits an external site build/check and the Math Site Editor's
review after publication. Its sandbox build failed at MyST's npm
preflight with `spawnSync /bin/sh EPERM`; no fresh HTML pass is claimed.

The owner reports M0.5 live review passed on 2026-10-17. Possible mixed-weight
rendering without Charter remains pending Xiang's check. Finding 007 is
resolved for chapter-3 source use; other chapter assignments remain open.
Finding 005's new chapter-3 wording needs a fresh live review after publication.
The optional Lean skips add no checked declarations.

## Decisions fixed by this design

- Use v4 chapter and appendix numbering for every active SCoFT locator.
  Active source IDs use `scft-v4-*`; old `scft-*` IDs appear only as historical
  v2 keys in the correspondence record. No concept ID is renamed.
- Keep M0.5 first, then SCoFT chapters 1–30, then Dynamic Hedging chapters
  1–23. Attach papers on demand to the chapter they support. There is no
  separate paper queue or mandatory Lean pilot ahead of chapter 1.
- Approve Shadow Mean's bounded transform and assumptions first in chapter 17;
  historical conflict estimates remain a separate study in chapter 18.
- Cover stochastic-calculus basics only as needed to explain Dynamic Hedging
  concepts. Teach the necessary assumptions and bounded numerical cases;
  no standalone advanced calculus course is scheduled.
- Write original explanations, derivations, proofs, figures and code. Source
  records reproduce titles and locators only. Keep the supplied PDFs, TOC
  extracts and bibliography outside the repository; never copy book text.
- Keep flat `content/incerto-*.md` bodies, the existing track hub, shared
  notation and the installed `xmath` import with its `src/math/` mapping.
  This planning set stays outside the MyST TOCs.
- Preserve `/math/incerto/`, the hub's `/incerto-wiki/` mirror and the Normix
  package boundary. Original writing does not resolve deferred legacy rights
  or publishing gates.
- Obtain financial inputs and additions through Portfolio Manager and Xiang's
  financial database; obtain other data through Data Scientist. Record each
  dataset's provenance and permitted uses.
- After every site update, Math Site Editor reads the corresponding live pages
  and records findings. Local HTML checks do not close that reader-review gate.

| Role ID | Owner assignment | Work |
| --- | --- | --- |
| `astra-max` | Codex GPT-6-Astra, max | Hard mathematics, M0.5 claim review, optional Lean and design |
| `astra-xhigh` | Codex GPT-6-Astra, xhigh | Writing and complex code |
| `cursor-grok` | Cursor Grok 4.7, xhigh | Simple code, review and site code |
| `math-site-editor` | Math Site Editor | Manager, source checks, live reader review and evidence records |
| `portfolio-manager` | Portfolio Manager bot | Financial data and requested additions |
| `data-scientist` | Data Scientist bot | Other data requests |

The owner chose Astra xhigh for chapter-1/2/3 writing/code and separate Astra max
runs for hard-math review (chapters 1–3 passed). Future role assignments do not
assert availability or authorize automatic delegation. No Cursor third-party
models are selected.

## Milestones and chapter order

| Milestone | Scope and exit gate |
| --- | --- |
| M0 — design | Reviewed plan, verified edition map and recorded validation limits; no implementation. |
| M0.5 — existing-page review | Astra max reviews every mathematical claim in all 24 bodies; Math Site Editor reads all 24 live pages. Deliver the issues list for Xiang with evidence, severity, assignments and dispositions. Resolve findings before affected claims are reused in a chapter. |
| M1 — SCoFT v4 | Execute chapters 1–30 in numeric order. Each chunk includes its assigned appendices/papers, teaching pages, Python demos and optional Lean. Close the chapter's scoped claims and reader-review evidence before advancing. |
| M2 — Dynamic Hedging | Execute chapters 1–23 in numeric order after SCoFT chapter 30. Attach introductory material and modules A–G; use stochastic calculus only to explain the hedging concepts. |
| M3 — technical closeout | Audit all chapter checkpoints, teaching/numerical evidence, attached-paper scope and live reader reviews. Record optional Lean results or skips; no formalization requirement for curriculum completion. |

State contains **55 ordered chunks**: M0.5, 30 SCoFT chapters, 23 Dynamic
Hedging chapters and closeout. All nine SCoFT appendices are attached to
supporting chapters: A→6, B→5, C→7, D→7, E→9, F→10, G→10, H→18, I→22.
They add no separate chunks. The [attachment table](inventory.md#supporting-unit-attachments)
also gives the Dynamic Hedging module hosts and the reasons for each choice.

Concept dependencies describe mathematical prerequisites, not execution order.
Use a reviewed existing page or a bounded cited lemma inside the current
chapter when a fuller treatment appears later. Repeated concept IDs indicate
reuse or extension at that chapter's claim scope, not repeated completion of
the entire concept.

| Existing queue item | V4 host | Scope |
| --- | --- | --- |
| Inference Asymmetry | Chapter 3, §3.5, p. 43 | A finite-sample contamination counterexample; use scoped prerequisites without moving chapter 4 ahead of it. |
| Moment-Estimation Failure | Chapter 4, §§4.4/4.4.4, pp. 79/84 | Start with moment and estimator distinctions; extend in chapters 7, 8 and 28. |
| Bounded Cauchy simulation | Chapter 7, §§7.2.1/7.6, pp. 139/148 | Bound runtime and sample sizes, not the Cauchy distribution; repeated paths and uncertainty summaries. The old chapter 4 label was incorrect. |
| Shadow Mean | Chapter 17, §§17.2/17.3, pp. 314/316 | Bounded transform and assumptions; historical estimation remains in chapter 18. |

## Optional exceedance pilot in SCoFT chapter 2

Use the original [counting-exceedances page](../../../content/incerto-counting-exceedances.md),
`xmath.exceedance_fraction`, and `demos/incerto/exceedances.py`. No new concept
page, data source, numerical helper or general probability theorem is needed.

For an integer `n ≥ 1`, observations `x : Fin n → ℝ`, and a real threshold `u`,
define the fraction by the cardinality of `{i : Fin n | x i > u}` divided by `n`,
with explicit casts to `ℝ`. Approved optional statements:

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

Xiang approved these exact claims on 2026-10-17, satisfying
the informal-scope confirmation in the
[Lean skill](../../../.agents/skills/xshi-math-lean-formalization/SKILL.md).
Do not request that confirmation again for these unchanged claims. The pilot
is now optional inside chapter 2. M0.5 and chapter 1 come first; this planning
revision does not start proof coding. If selected, a later implementer
reviews the teaching page and existing Python example, then pins compatible
Lean/Mathlib revisions, proves both statements, audits their hypotheses and
axiom dependencies, and obtains a successful build. Only then does the page
link the checked declarations at an immutable repository revision.

Evidence if the pilot is attempted: a clean imported Lean build without
placeholders; statement review; the existing demo outputs `1`, `1/4`, `0`; relevant Python tests; strict
site build and HTML checks; rendered equation and link review; Math Site Editor
live reader review after any site update. If CI is added,
its Lean job must check the imported root and fail on proof placeholders.
The manager records local versus CI evidence separately. The proof establishes
real-number counting facts. It does not verify NumPy floating-point execution,
the population survival function, or any sampling theorem.

If the pilot is skipped, record the reason and continue to chapter 3 after
chapter 2's teaching, demos and reader review close. The approval does not
make Lean a chapter-completion gate.

## Remaining open questions and limits

There are **no remaining program-scope questions**. Shadow Mean scope,
stochastic-calculus depth and 2025 edition reconciliation are closed in state.
Exact theorem locators, dataset access and mathematical review remain work
within chapter chunks, rather than unresolved scope choices.

The repository's older publishing and rights actions remain in the
[planning index](../index.md#decision-queue) and cutover runbook; this program
does not close them. Counts measure planned coverage, not verified mathematics.
