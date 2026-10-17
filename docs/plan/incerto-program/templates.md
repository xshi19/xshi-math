# Page contracts

These are templates for future original writing, not concept pages added by
this change. Replace every placeholder after source and mathematical review.
Use one page where the concept, proof and short demo fit together; use separate
flat files only when they have independent reading value. Add actual pages to
the explicit Incerto TOC and appropriate index.

All four forms inherit the
[mathematical-writing rule](../../rules/mathematical-writing.md),
[notation rule](../../rules/shared-notation.md), and applicable concept/proof
skills. Choose the title, statement and assumptions before writing a proof.
Distinguish a complete proof, sketch, derivation, cited theorem and numerical
illustration. A new note need not carry every section in a template if a
section would be empty.

Use these contracts only for the mathematical completion scope. For each
concept, deliver website teaching first, then Python demos, numerical
illustrations, visualizations or worked cases, then optional Lean. Record the
order and evidence in state. A missing Lean library is `skipped-for-now` with
a reason in the planning/evidence record; it does not remove continuous-time
teaching or numerical examples. Keep implementation status out of the reader's
mathematical explanation.

## Concept page

Proposed home: `content/incerto-<concept>.md`.

````markdown
---
title: [Concept title]
---

([stable-concept-label])=
## Definition and scope

[Define the object in our own words. State domain, support, parameter range,
moment assumptions, and local mappings to the shared notation.]

## Main claim

[State the precise mathematical claim with quantifiers and hypotheses.]

## Reasoning

[Original proof/derivation at the scope supplied, or a precise citation to a
result whose proof is not supplied. Do not present simulation as proof.]

## Example and boundary

[An original worked example; a boundary case or counterexample explaining
where the result stops. Link a longer demo if one actually exists.]

## Connections

[Relative links to existing same-track prerequisites; full public URLs for
cross-track material. Explain why the connection matters.]

## References

[Full book/paper entry with edition and source locator. Explain whether it is
related reading, the source of a definition, or support for the stated result.]
````

No interpretive or prose-only note is a completion deliverable. A brief cited
origin reference to a non-technical Incerto book may accompany the technical
definition; it does not create a chapter-coverage obligation.

## Theorem page or theorem section

Proposed separate home, only if needed:
`content/incerto-<concept>-theorem.md`. Prefer a section of the existing
concept page for M1.

````markdown
---
title: [Exact theorem subject]
---

([stable-theorem-label])=
## Statement

[Variables and types; quantifiers; nonempty/positive/finite conditions;
measurability, integrability and independence where needed; exact conclusion
and convergence mode.]

## Proof

[Our mathematical argument at exactly the stated scope. Identify cited lemmas.
A proof sketch must be labeled as such.]

## Boundaries and example

[Cases excluded by hypotheses; a counterexample if useful. A numerical example
is separate evidence and does not enlarge the checked statement.]

## Checked declaration

[Optional, after teaching and numerical work and a successful audited build:
describe the exact statement checked and link its declaration at an immutable
Git revision. Identify any difference from the theorem above. Omit this section
when Lean is skipped; record that decision and reason outside the teaching page.]

## References

[Original mathematical source with exact theorem/section/page after verification;
book chapter as related context if it is not the proof source.]
````

The declaration link has the form
`https://github.com/xshi19/xshi-math/blob/<commit>/lean/XshiMath/Incerto/<Module>.lean#L<line>`.
Record the fully qualified declaration name and checked revision. Resolve that
URL against the committed file before publishing; no fabricated commit, line
number or current `main` link as immutable evidence. Toolchain/build details
belong in the Lean README and a verification record. Omit the entire checked
declaration section until evidence exists. Do not describe a stronger
informal statement as verified because its special case builds.

## Numerical demo page

Proposed separate home, only if needed: `content/incerto-<concept>-demo.md`.

````markdown
---
title: [Numerical question]
---

([stable-demo-label])=
## Question and model

[The mathematical object being illustrated; synthetic or fixed inputs; what
this experiment can and cannot establish. Link the supporting concept.]

## Reproduce

[Exact installed-environment command, generator and seed if random, sample
sizes, replications, parameter grid, stopping rule and expected runtime. Link
the script/helper at the revision used.]

## Results

[Original table/figure with units, captions and uncertainty summaries. Separate
analytic references from simulation estimates. Record non-finite outputs,
truncation and failures rather than silently dropping them.]

## Interpretation and sensitivity

[Compare alternative seeds, sample sizes or parameters where relevant; explain
finite-sample limits. A single trajectory does not establish an asymptotic law.]

## References

[Book/chapter for motivation, precise mathematical result for the model, and
reproducibility record for the computation.]
````

Static M1 inputs require no random seed or uncertainty interval. The example's
exact fractions and strict comparison are sufficient. A Cauchy simulation
needs repeated paths and a clear distinction between undefined population
moments and finite machine outputs.

## Empirical-study page

Proposed home: `content/incerto-<study>-study.md`. Reserve a unique stem when a
study is selected; state currently proposes only its concept home.

````markdown
---
title: [Population, outcome, and empirical question]
---

([stable-study-label])=
## Question and estimand

[Population, observational unit, time window, outcome and target quantity.
Distinguish descriptive fit, prediction, and causal claims.]

## Data and provenance

[Financial data: Portfolio Manager bot / Xiang's database; request additions
there. Other data: Data Scientist bot. Record the handoff, original provider,
exact dataset/version, retrieval date, license/terms, checksum and manifest.
Units, exposure denominators, missingness, revisions, censoring,
reporting uncertainty and cleaning decisions.]

## Design and methods

[Inclusion rules and chosen analysis before inspecting decisive outcomes;
dependence treatment, threshold choices, comparisons, uncertainty method,
multiple-testing controls and train/test split if applicable.]

## Reproduce

[Lawful data acquisition separately from analysis; exact command and lockfile
revision. Identify a redistributable fixture if full data cannot be included.]

## Results

[Original figures/tables with uncertainty and data coverage. Separate measured
quantities, model estimates and analytic identities.]

## Sensitivity and limitations

[Alternative thresholds, distributions, time windows, missing-data assumptions,
and finite upper bounds. Include conflicting primary analyses where relevant.
Do not infer a universal tail law or policy conclusion from one fitted sample.]

## References and data access

[Book/chapter context; exact paper versions and methods; dataset citation and
terms. State what inputs are unavailable and how that limits reproducibility.]
````

## Citation and attribution format

Use ordinary Markdown reference entries initially; no bibliography engine is
installed. Bibliographic details belong to the selected edition, not a mixture
of print and preprint page numbers. Preferred forms:

- Book: `Author. Title. Edition, publisher, year, ISBN. Chapter N, section or
  verified pages. [Publisher or authorized source link].` Match locators to
  the selected technical edition; retained planner ordinals are not citations.
- Paper: `Authors. Title. Journal/DOI when verified; arXiv identifier and
  version, year. Section/Theorem/Equation and pages actually consulted.
  [Versioned primary source].` Do not treat a retailer TOC as mathematical
  evidence or assume preprint and published theorem numbers agree.
- Dataset: `Provider. Dataset and version, coverage dates, retrieved date,
  persistent URL/DOI, license and checksum/manifest.`
- Formal result: fully qualified declaration, module, immutable source link,
  checked Lean/Mathlib versions and verification record. This complements the
  mathematical citation; it does not transfer authorship of the source theorem.

A concrete book locator format is: Nassim Nicholas Taleb, *Dynamic Hedging*,
Wiley, 1997, ISBN 9780471152804, ch. 1,
[publisher record](https://www.wiley-vch.de/en/areas-interest/finance-economics-law/dynamic-hedging-978-0-471-15280-4).
This supplies bibliographic context; exact mathematical claim and page
locators still require the selected copy. Add papers when a concrete claim
needs them, with exact version and section recorded.

## Review and evidence handoff

Before M1, use [the M0.5 review record](m0.5-review.md) for Astra max's
claim-by-claim review and Math Site Editor's live reader review of all 24
existing concept pages. After every site update, the editor records a fresh
live reader review with deployment revision, date, URLs, findings, severity,
proposed actions and dispositions. Keep that review separate from build,
numerical and Lean evidence; no such review is claimed by these templates.

Write from the mathematical object and our argument, then cite the source.
Do not rewrite a book paragraph sentence by sentence. Avoid quotations in
these notes, borrowed examples with only cosmetic changes, source figures,
scanned pages or copied tables. Each note's references should say what was
used. Rights review of any external dataset, illustration or code is separate
from the owner's permission to write original explanations.
