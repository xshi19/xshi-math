# Incerto Lean MVP

This contained [Lean](https://lean-lang.org/) project checks two elementary
Pareto identities in the `Incerto` namespace. Python and site builds do not
depend on it.

Imported from incerto-wiki at `9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`.
The source records a passing build on **2026-09-05** with Lean/Mathlib
**v4.19.0**. It has **not been rechecked in xshi-math**. No Lean toolchain or
network download is required for Python tests or the site build.

Copyright (c) 2023 xshi19; MIT, see
[the imported-material notice](../../THIRD_PARTY_NOTICES.md).

## Build

Install [elan](https://github.com/leanprover/elan#installation), then run from
the repository root:

```bash
cd formalization/incerto-lean
lake exe cache get
lake build
```

The first run downloads the pinned toolchain, dependencies, and compiled
[Mathlib](https://github.com/leanprover-community/mathlib4) cache. Later proof
edits normally need only `lake build`. If `lake` is missing from your shell's
path after installing elan, restart the shell or add `$HOME/.elan/bin` to `PATH`.

Lean and Mathlib are both pinned to `v4.19.0`, the version used to verify this
prototype. `lake-manifest.json` locks transitive dependencies. Update the
toolchain and Mathlib together, regenerate the manifest with `lake update`,
then rerun the build. Do not track dependencies on a floating branch.

## Checked scope

Both declarations live in [Incerto/Pareto.lean](Incerto/Pareto.lean) and are
imported by the default library target, [Incerto.lean](Incerto.lean).

| Declaration | What it proves |
| --- | --- |
| `Incerto.moment_exponent_threshold` | For real `p` and `alpha`, `p - alpha - 1 < -1` iff `p < alpha`. This is the exponent comparison, not an integrability theorem. |
| `Incerto.pareto_survival_scale` | The piecewise Pareto survival expression has ratio `t ^ (-alpha)` when `xm > 0`, `alpha > 0`, `t > 0`, `xm ≤ x`, and `xm ≤ t * x`. No probability measure is constructed. |

The scaled-threshold condition matters when `t < 1`: below the cutoff the
survival expression is constant at one, so the power ratio need not hold.
Equality at either cutoff is allowed.

Project warnings are errors, so a proof containing `sorry` fails the build.
Use explicit hypotheses and checked proofs; do not add axioms to stand in for
unfinished results. Add future modules to `Incerto.lean` so `lake build`
continues to check the entire track.

The [historical blueprint](../../docs/records/incerto-wiki/lean-blueprint.md) separates
these checked algebraic facts from the remaining integral and asymptotic work.
