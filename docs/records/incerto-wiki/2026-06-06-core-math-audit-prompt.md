> Historical record from `incerto-wiki` at `9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`.
> Source: `docs/reports/deep-math/2026-06-06-core-math-audit-prompt.md`. Statements and commands below describe that repository
> at the recorded date, not current xshi-math verification. MIT; copyright (c) 2023 xshi19.

# Phase 6 Core Math Audit Request

You are a mathematical consultant for Incerto Wiki, a concept-first Jupyter Book
on fat tails, extreme value theory, and Taleb's Incerto framework. Audit the
provided repository context as an intermediate advisory report for Codex. Do not
write publish-ready wiki prose. Focus on mathematical correctness, assumptions,
notation consistency, executable-code alignment, and citation gaps.

Use only the supplied context. Hosted web search is disabled for this run. If a
fact would require an outside source that is not in the context or bibliography,
mark it as a citation gap or uncertainty instead of asserting it.

## Scope

Audit these foundation pages and their directly relevant code:

- Pareto Distribution
- Double Pareto Distribution
- Regular Variation
- Karamata's Theorem
- Pareto Moment Existence
- LLN Failure Under Infinite Mean
- Max-to-Sum Ratio
- Hill Estimator
- Pickands-Balkema-de Haan Theorem
- Mean Excess Function
- Main empirical examples: Pre-Asymptotic LLN Behavior, Amazon Book Rank, and
  S&P 500 Tail Diagnostics

Use the Chapter 3 and Chapter 4 Taleb reading guides and the Embrechts external
guide as routing context, not as primary sources to copy.

## Audit Questions

1. Are the stated definitions, formulas, theorem statements, proof sketches,
   and caveats mathematically correct under their visible assumptions?
2. Where are assumptions missing or too implicit, especially independence,
   nonnegativity, tail support, regular variation, threshold choice, moment
   existence, and asymptotic regimes?
3. Are boundary cases handled correctly, especially alpha <= 1, alpha = 1,
   alpha <= 2, p = alpha, xi >= 1, xi >= 1/2, and finite-sample versus
   asymptotic claims?
4. Is notation compatible across the concept pages, the shared notation page,
   and the reading guides?
5. Do the Python helpers and page code cells implement the same objects claimed
   in prose? Check formulas in `incerto/distributions.py`,
   `incerto/estimators.py`, and the relevant tests.
6. Do empirical examples avoid overclaiming? Flag statements that sound like
   proof of a Pareto model when they are only sample diagnostics.
7. Which citations or local proofs are missing before a claim should be treated
   as durable wiki content?

## Output Requirements

Follow this Markdown report shape:

1. `# Report`
2. `## Executive Summary`
3. `## Problem Restatement`
4. `## Assumptions and Notation`
5. `## Source and Context Inventory`
6. `## Main Analysis`
7. `## Proofs or Derivations`
8. `## Computations or Checks`
9. `## Caveats and Failure Modes`
10. `## Suggested Incerto Wiki Changes`
11. `## References`

In `Suggested Incerto Wiki Changes`, organize findings by priority:

- P0: clear mathematical error or code/prose contradiction.
- P1: missing load-bearing assumption, theorem condition, or misleading
  statement that could produce wrong reader conclusions.
- P2: citation gap, imprecise terminology, boundary-case improvement, or
  useful clarification.
- P3: optional editorial or future-work suggestion.

For each actionable finding, include:

- affected file path;
- current claim or implementation location by section/function name;
- issue;
- suggested correction;
- what verification would support the correction.

Mark any suggestion as uncertain when you cannot verify it from the supplied
context. Do not include hidden chain-of-thought, and do not reproduce
copyrighted source prose or figures.
