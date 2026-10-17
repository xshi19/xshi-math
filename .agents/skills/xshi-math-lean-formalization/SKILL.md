---
name: xshi-math-lean-formalization
description: Prepare or perform checked Lean formalization for xshi-math claims. Use when scoping a Lean declaration, opening a Lean subtree, or reconciling informal notes with checked proofs. Honest status: formalization/incerto-lean is an optional imported prototype, checked upstream on 2026-09-05 with Lean/Mathlib v4.19.0 and not rechecked here; ordinary mathematical prose does not require formalization.
---

# xshi-math Lean Formalization

**Current status:** `formalization/incerto-lean/` contains the imported
Lake/Mathlib prototype, pinned to Lean/Mathlib `v4.19.0`. Its two algebraic
Pareto declarations were checked in incerto-wiki on **2026-09-05**; they have
**not been rechecked in xshi-math**. See the
[project README](../../../formalization/incerto-lean/README.md) for the exact
hypotheses and the [historical blueprint](../../../docs/records/incerto-wiki/lean-blueprint.md).
Neither result constructs a probability measure or proves moment integrability.

## Existing subtree

Work in `formalization/incerto-lean/` and retain its pinned toolchain, Mathlib
revision, and transitive lake manifest. Python tests and site builds remain
independent. Before extending it, scope the informal claim with
`$xshi-math-proof-writing`; do not imply that migration rechecked the proofs.

Build from the project directory with `lake build`; initial setup may need
`lake exe cache get` and network access. Record the actual toolchain, command,
result, and checked declaration scope before updating a public proof claim.

## Scope the statement (always, even without Lean)

1. Read the target note, `content/notation.md`, and
   `$xshi-math-proof-writing`.
2. State the exact proposed declaration and hypotheses before proving anything.
   Separate real algebra, integrability, probability-measure construction, and
   asymptotic claims.
3. Check boundary cases against the informal claim. Keep any scope reduction
   explicit in notes (do not silently weaken a public theorem).

## Implement and check

1. Work under the chosen Lean root namespace. Search pinned Mathlib for
   supporting declarations; use explicit, narrow imports and inspect hypotheses.
2. Import new modules from the root `.lean` file so the default build checks
   them. Complete proofs without `sorry`, new placeholder axioms, or disabling
   warnings-as-errors.
3. Run the README's build command (`cd formalization/incerto-lean && lake build`). For
   first-time setup, follow elan/cache instructions in that README.
4. Inspect the final declaration as well as the build: a checked proof of a
   weaker or vacuous statement does not establish the intended claim.

## Reconcile informal notes

After a successful build, link the exact declaration from any blueprint or
proof-support note and update the concept page only with accurate checked
scope. Use `$xshi-math-concept-page` and `$xshi-math-proof-writing` for prose
edits. Keep ordinary concept prose focused on mathematics; project bookkeeping
belongs in Lean README / records.

Report declaration names, checked hypotheses and scope, build result, and
remaining informal-only claims. If Lean is absent or the build cannot run,
leave the claim unverified and say so. Python and site builds stay independent
of Lean.

## Completion Check

- Prerequisites and absence/presence of a Lean tree are stated honestly.
- Informal claim scope is explicit before any proof work.
- No public prose asserts Lean-checked status without a successful audited
  build of the corresponding declaration.
- Skipped setup or build steps are reported.
