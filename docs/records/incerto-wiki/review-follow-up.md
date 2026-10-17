> Historical record from `incerto-wiki` at `9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`.
> Source: `docs/plan/review-follow-up.md`. Statements and commands below describe that repository
> at the recorded date, not current xshi-math verification. MIT; copyright (c) 2023 xshi19.

# Review follow-up

Initial baseline: local committed main `590eab8`. The milestone branch was then
updated to remote main `1f2d5ff` (NYC dog-name additions). Work is isolated from the maintainer's
uncommitted checkout. The review originally targeted `1f2d5ff`.

## Step 1: baseline

- Locked environment: Python 3.13.12, NumPy 2.4.6, SciPy 1.17.1.
- Tests: 60 passed, 1 skipped (site artifact absent before building).
- Executed MyST and Sphinx build: passed on a fresh artifact directory.
- Reproduced: normal-mixture survival returns zero at (10, .5); Pareto
  log-survival returns negative infinity at (1e200, 2); variance-gamma density
  returns NaN at (1000, 2, 1.9, 1); equal 1e308 observations give ratio zero.
- Mixture sampling with parameters [0, .5] and size (3, 2) raises ValueError.
- The blueprint omits the scaled support condition; the generalized CLT
  caveat overstates mean nonexistence at exponent one.
- The build scanner matches ordinary ValueError text; the fresh build passes
  because API output is generated after scanning. An incremental build can
  scan the previous API output and fail.
- data/cache/sp500_daily.csv is tracked despite the existing ignore policy.

## Milestones

1. Correct statements, numerical methods, build scanning, cache tracking, CI.
2. Add learning routes and revise Pareto, regular variation, and Hill.
3. Clarify graph relations/accessibility, statement anchors, and figures.
4. Check a contained Lean project, axiom policy, and precisely scoped links.

Each implementation step receives its own commit. Milestone branches are
stacked; each PR targets the preceding milestone branch until merged.
Interactivity is evaluated after the static pages and formalization work.
