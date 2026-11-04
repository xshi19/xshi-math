# Notation economy

The generic, repository-independent version of this rule is the
`notation-economy` skill in the math-writing plugin (not yet published).

Apply this rule to the final draft of mathematical exposition, after claims and
proofs have settled. Scratch work and intermediate derivations may use any
helpful notation. Audit what the reader will see.

## When a symbol earns its place

- Start with the [shared canon](../../content/notation.md). Consult a relevant
  textbook or paper when choosing field notation; record the source and any
  mapping when conventions differ. Prefer established notation for the same
  object, but standard usage elsewhere does not require an alias here.
- Introduce an auxiliary symbol only when it names a meaningful mathematical
  or applied object used substantively again later, or substantially shortens
  or clarifies otherwise unwieldy formulas. Recurrence alone is insufficient:
  repeatedly substituting a letter for a short, readable expression can still
  increase the reader's memory burden.
- Judge the rendered expression, including the cost of remembering its
  definition. Saving a few LaTeX characters is insufficient. Prefer an explicit
  indicator or survival probability when its event is the point of the formula.
- Keep necessary primary variables, parameters, bound indices, and named
  objects. This is an audit of avoidable notation, not a symbol quota. A useful
  proof-local abbreviation may belong in the proof without entering the statement.
- Define retained symbols near their first substantive use. State their meaning
  and scope; avoid chains of aliases and decorative subscripts.

## Final-draft audit

1. Inventory introduced symbols and their meanings. Read the whole page and
   check relevant sibling pages before deciding what is redundant. Distinguish
   substantive later uses from definitions, restatements, and unrelated reuse
   of the same letter.
2. For each auxiliary symbol, keep it for a stated reader benefit, inline its
   expression, or defer its definition to the section that needs it. Check
   symbols used only once or twice especially carefully; a count is a review
   signal, never a deletion rule. Do not add uses to satisfy a threshold.
3. Compare the revision with the original claim by claim. Preserve assumptions,
   quantifiers, domains, units, parameter dependence, conditioning, and the
   distinction between conditional and unconditional quantities. Preserve
   strict versus non-strict events, endpoint atoms, positivity and finiteness
   conditions, and whether expectations may be infinite. Do not introduce
   undefined products, divisions, or differences of infinities.
4. Preserve every mathematical fact, caveat, attribution, and proof dependency;
   no information may disappear merely because its shorthand does. Update all
   affected uses, captions, labels, and references within the authorized scope.
   If meaning or scope is uncertain, resolve it through the concept/proof
   workflow before simplifying.
5. Read the result in order and inspect changed rendered formulas when editing
   a published page. Check that it reduces lookup effort without creating long,
   unreadable expansions. Record non-obvious decisions in the review, not as
   an extra notation inventory on the published page.

Automation may suggest candidates; it must remain report-only and must not
rewrite mathematics or fail a build on symbol counts. The optional
[`notation_audit.py`](../../scripts/notation_audit.py) is a heuristic aid, not a
correctness or readability check.

## Example

Before: define $D=\mathbf1_{\{X>u\}}$, $p_u=\bar F(u)$, $T(u)=\mathbb E[XD]$,
$C(u)=\mathbb E[(X-u)_+]$, then display $T(u)=up_u+C(u)$ and $C(u)=p_u e(u)$.

After (assume $\bar F(u)>0$; $e(u)=\mathbb E[X-u\mid X>u]$, possibly $+\infty$):

$$
\mathbb E[X\mathbf1_{\{X>u\}}]=u\bar F(u)+\mathbb E[(X-u)_+],\qquad
\mathbb E[(X-u)_+]=\bar F(u)e(u).
$$

The indicator and $\bar F(u)$ are as short as their aliases and need no lookup;
$e(u)$ stays because it is shared canon with its own note. The strict event,
positivity assumption, and possibly infinite means are preserved.

## Basis

[Halmos, *How to Write Mathematics*, §15 “Resist symbols” and §5](https://sites.math.washington.edu/~lind/Resources/Halmos.pdf)
motivates deliberate symbol choice and avoiding unnecessary names.
[Knuth, Larrabee, and Roberts, *Mathematical Writing*, §§1 and 5](https://jmlr.csail.mit.edu/reviewing-papers/knuth_mathematical_writing.pdf)
supports nearby definitions and readable exposition. These are editorial
principles; the audit above is repository practice.
