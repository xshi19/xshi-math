> Historical record from `incerto-wiki` at `9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`.
> Source: `docs/reports/deep-math/2026-06-06-core-math-audit-integration.md`. Statements and commands below describe that repository
> at the recorded date, not current xshi-math verification. MIT; copyright (c) 2023 xshi19.

# Phase 6 Core Math Audit Integration

Date: 2026-06-06

## Artifacts

- Prompt: `docs/reports/deep-math/2026-06-06-core-math-audit-prompt.md`
- Dry-run manifest: `docs/reports/deep-math/2026-06-06-core-math-audit-dry-run.txt`
- Consultant report: `docs/reports/deep-math/2026-06-06-core-math-audit-report.md`

The dry run used `gpt-5.5-pro`, `xhigh` reasoning, and `--no-web-search`.
The final report was recovered through the Responses API background mode after
the Agents SDK path returned empty visible output. The successful recovery used
`gpt-5.5-pro`, `medium` reasoning, low text verbosity, `30000` maximum output
tokens, and no web search.

## Accepted and Integrated

- P0 double Pareto mean boundary:
  `content/concepts/distributions/double-pareto.md`,
  `incerto/distributions.py`, and `tests/test_distributions.py`.
- P0 Pareto survival-ratio support condition:
  `content/concepts/distributions/pareto.md`.
- P1 S&P 500 positive-loss sample definition:
  `content/concepts/examples/sp500-tail.md`.
- P1 Hill estimator assumptions:
  `content/concepts/methods/hill-estimator.md`.
- P1 mean-excess support and existence assumptions:
  `content/concepts/theorems/mean-excess-function.md`.
- P1 Pickands-Balkema-de Haan endpoint and support wording:
  `content/concepts/theorems/pickands-balkema-de-haan.md`.
- P2 shared EVT notation for $\beta$ and $x_F$:
  `content/notation/index.md`.
- P2 empirical title wording:
  `content/concepts/examples/sp500-tail.md`,
  `content/concepts/examples/amazon-bookrank.md`, and link text in index and
  guide pages.

## Rejected or Already Covered

- The report suggested checking whether `extreme-value-index.md` was missing.
  The file exists at `content/concepts/methods/extreme-value-index.md`, though
  it remains a planned Phase 7 stub.

## Deferred or Uncertain

- Precise theorem, section, or page citations for regular variation,
  Karamata, Hill consistency, Pickands-Balkema-de Haan, and GPD moments remain
  deferred until source PDFs or page-verified references are inspected.
- Moving `mean-excess-function.md` from theorem to method is optional and would
  be a structural change; leave it for a later concept-graph pass.
- Adjusting `max-to-sum-ratio.md` frontmatter to avoid depending on an example
  page is optional and should be handled with a concept graph regeneration.
