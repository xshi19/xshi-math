---
name: xshi-math-lean-formalization
description: Prepare or perform checked Lean formalization for xshi-math claims. Use when scoping a Lean declaration, opening a Lean subtree, or reconciling informal notes with checked proofs. Honest status: this repository has no Lean project, lake manifest, or lean-blueprint yet; ordinary mathematical prose does not require formalization.
---

# xshi-math Lean Formalization

**Current status:** there is no Lean project in this repository (no `lean/`,
`formalization/lean/`, `lakefile`, pinned toolchain, Mathlib pin, or
`lean-blueprint`). Do not pretend those paths exist. Public concept prose must
not claim a statement is Lean-checked until a real build verifies it.

## When to open a Lean subtree

Open a Lean project only when the owner authorizes formalization work and the
claim is stable enough to pin. Suggested first layout (create only when
starting for real):

```text
lean/                     # or formalization/lean/ — pick one and document it
  lakefile.toml / lakefile.lean
  lean-toolchain
  XshiMath.lean           # root import
  XshiMath/               # modules
  README.md               # elan, cache, lake build, update procedure
docs/records/             # blueprint / proof-support notes (optional)
```

Prerequisites before coding proofs:

1. Owner confirms the informal claim on a content page (use
   `$xshi-math-proof-writing` to scope Statement vs Proof vs cite/sketch).
2. Pin Lean + Mathlib via the toolchain file and lake manifest; record versions
   in the Lean README.
3. Add a track or root note that Lean is optional and independent of
   `npm run build` / `uv run pytest`.
4. Update `AGENTS.md` verification commands with the actual `lake build` entry
   point once it exists.

Until that subtree exists, stop after scoping: record the exact informal
statement, intended hypotheses, and that formalization is deferred.

## Scope the statement (always, even without Lean)

1. Read the target note, `content/notation.md`, and
   `$xshi-math-proof-writing`.
2. State the exact proposed declaration and hypotheses before proving anything.
   Separate real algebra, integrability, probability-measure construction, and
   asymptotic claims.
3. Check boundary cases against the informal claim. Keep any scope reduction
   explicit in notes (do not silently weaken a public theorem).

## Implement and check (only after a Lean project exists)

1. Work under the chosen Lean root namespace. Search pinned Mathlib for
   supporting declarations; use explicit, narrow imports and inspect hypotheses.
2. Import new modules from the root `.lean` file so the default build checks
   them. Complete proofs without `sorry`, new placeholder axioms, or disabling
   warnings-as-errors.
3. Run the README's build command (typically `cd lean && lake build`). For
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
