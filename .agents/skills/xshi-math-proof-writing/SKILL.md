---
name: xshi-math-proof-writing
description: Scope theorem and proposition statements before writing proof sections in xshi-math notes. Use when creating or revising Statement, Theorem, Proposition, Proof, Proof sketch, derivation, lemma, or corollary text under content/.
---

# xshi-math Proof Writing

Use this skill when a note states mathematical results and must clarify what is
proved, what is cited, and what is only illustrated.

## Inputs

- Target page and statement section.
- Existing statement labels, equation numbers, theorem names, or prose claims.
- Available references.
- Any future Lean status (internal tracking only; no Lean project yet).

## Workflow

1. Inventory every theorem-like claim: theorem, proposition, lemma, corollary,
   consequence, equivalence, estimator guarantee, or named formula.
2. Give each statement a stable name in prose, a displayed label, or an
   equation reference when the page has multiple statements.
3. Before the proof, add one or two reader-facing orientation sentences that say
   what the argument establishes ("We prove...", "The argument below shows...",
   or "For the full representation theorem, we cite..."). Use a compact table
   only when several independent statements would otherwise be hard to track.
4. Write proof headings that name the target when a generic `Proof` heading
   would be ambiguous.
5. Make dependency direction explicit. If later formulas use earlier theorem
   statements, say so.
6. Check that every proof paragraph refers only to assumptions already stated
   locally or in linked notation/notes.
7. Keep pending formalization notes out of ordinary public prose until a Lean
   tree exists. Do not write `Lean: pending` on rendered pages.

## Proof Support Types

Use the lightest honest support type. On public pages, turn labels into natural
exposition rather than audit-style status language.

| Type | Use when | Required support |
| --- | --- | --- |
| No proof | Full proof needs textbook-scale setup or lemmas not yet introduced. | State that the result is cited, not proved, and cite a source. |
| Proof sketch | Main idea and key steps shown; routine estimates omitted. | Say it is a sketch, include load-bearing steps, cite a full proof. |
| Partial proof | Special case, extra assumptions, or one direction/consequence only. | State the restricted claim before the proof; cite the full theorem. |
| Full proof | Self-contained enough for this hub (roughly one to two paper pages). | State all assumptions and prove each nontrivial step. |

## Completion Check

The proof work is not done until:

- every theorem-like statement has reader-facing support prose;
- every proof or sketch says which statement or consequence it supports;
- cited-but-unproved results are not described as proved by the page;
- partial proofs state extra assumptions or special cases before the proof;
- pending Lean or implementation status stays out of ordinary public prose;
- references are present for no-proof and proof-sketch items;
- equation or statement numbering cannot mislead readers about what is proved.
