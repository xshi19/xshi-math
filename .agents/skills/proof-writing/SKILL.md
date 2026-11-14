---
name: proof-writing
description: Scope theorem and proposition statements before writing proof sections in xshi-math notes. Use when creating or revising Statement, Theorem, Proposition, Proof, Proof sketch, derivation, lemma, or corollary text under content/.
---

# Proof Writing

Use this skill when a note states mathematical results and must clarify what is
proved, what is cited, and what is only illustrated. Apply the
[mathematical-writing rule](../../../docs/rules/mathematical-writing.md).

## Inputs

- Target page and statement section.
- Existing statement labels, equation numbers, theorem names, or prose claims.
- Available references.
- Any future Lean status (internal tracking; imported prototype status is in the Lean skill).

## Workflow

1. Apply the external `$statement-before-proof` skill when writing or revising
   proofs and formal derivations. Its installation and this site's MyST markup,
   labels, and anchor constraints are in the
   [site integration](../../../docs/rules/statement-before-proof.md).
2. Choose the proof support type below for each result on the page.
3. Before the proof, add one or two reader-facing orientation sentences that say
   what the argument establishes ("We prove...", "The argument below shows...",
   or "For the full representation theorem, we cite..."). Use a compact table
   only when several independent statements would otherwise be hard to track.
4. Apply the site integration's MyST rendering and link-compatibility checks.
5. Run the integration's report checker on touched pages and review its findings
   alongside the external skill's audit. A clean report is not a proof review.
6. Keep pending formalization notes in records. The imported prototype checks
   only its two named algebraic declarations. Do not write `Lean: pending`
   on rendered pages.

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
- the external statement/proof audit and site rendering checks are complete;
- every proof or sketch says which statement or consequence it supports;
- cited-but-unproved results are not described as proved by the page;
- partial proofs state extra assumptions or special cases before the proof;
- pending Lean or implementation status stays out of ordinary public prose;
- references are present for no-proof and proof-sketch items;
- equation or statement numbering cannot mislead readers about what is proved.
