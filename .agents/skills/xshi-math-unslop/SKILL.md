---
name: xshi-math-unslop
description: Strip AI-writing patterns from prose while preserving xshi-math's mathematical voice. Use when writing or editing README, docs/, content/ notes, demos commentary, PR descriptions, or when the user says unslop, de-AI, or "this reads like AI". Includes math carve-outs and writing registers for this hub.
---

# xshi-math Unslop

Cut AI tells; preserve meaning, tone, and the math. Process: identify the
register → scan for patterns → rewrite → self-audit ("what still reads as
AI-generated?").

Pick the register first — what's right in a design note is wrong in a theorem
page: `references/writing-registers.md`.

Also read `docs/rules/mathematical-writing.md`. Prefer `$xshi-math-prose-review`
when the task is a full semantics-preserving pass after claims are settled;
use this skill when the focus is AI-pattern scrubbing or register choice.

## Math-hub carve-outs (override the patterns below)

1. **Em dashes are allowed** in mathematical asides. Cut only when several pile
   up in a paragraph.
2. **Mid-sentence colons are allowed** where they introduce an equation,
   definition, or list.
3. **Technical senses of flagged words are fine**: *vector* in $\mathbb{R}^d$,
   *multimodal(ity)* for densities, *surface* as "API surface" in design notes.
   Banned only as empty metaphors.
4. **"Note that" is fine** for flagging a subtlety. "It is important to note
   that" is filler; delete it.
5. **Active voice means "we" in math prose**: "we show", "we integrate by
   parts" — standard mathematical style, not chattiness.
6. **Calibrated hedging is intentional** when encoding uncertainty, asymptotics,
   or empirical limits; don't strip it there.
7. **Heading case**: match the page's existing convention; prefer sentence case
   for new long-form pages; don't churn existing headings.
8. **Shared notation**: reuse `content/notation.md`; do not "vary" symbols for
   style.

## Patterns to detect and fix

**Content.** Significance inflation ("pivotal", "testament to", "evolving
landscape") → state what happened. Superficial -ing tails → delete or say the
concrete thing. Promotional adjectives ("powerful", "seamless", "cutting-edge")
→ neutral description or the number. Vague attributions ("it is well known") →
cite or delete. Formulaic challenge framing → specific facts.

**Language.** AI vocabulary (delve, crucial, intricate, interplay, tapestry,
showcase, underscore, foster, leverage) → plain words. Copula avoidance
("serves as", "boasts", "features") → "is" / "has". Negative parallelism
("it's not just X, it's Y") → state the point. Forced groups of three → the
natural number. Synonym cycling → one term per concept. False ranges → list.

**Style.** Don't bold every noun. Inline-header bullets that restate the line →
prose. No decorative emojis. Straight quotes.

**Communication artifacts.** No chatbot phrases ("I hope this helps", "Let's
dive in!"), no sycophancy, no knowledge-cutoff disclaimers.

**Filler.** "In order to" → "to"; "due to the fact that" → "because";
"It is important to note that" → delete; stacked hedges → "may"; generic
conclusions → specific facts or nothing.

**Plain speech.** Say the mechanism or the number, not the vibe. One idea per
sentence when the reader must re-read. Cut adverbs propping up weak verbs.

## Math writing

- Every symbol is defined at first use on the page, or points to
  `/math/notation/`.
- Use MyST/LaTeX math (`$...$` or `{math}` directives). Plain-text math is not
  acceptable in notes.
- One symbol per object, one term per concept, across tracks when the concept
  is shared.
- Formulas carry their domain: "for $\alpha > 0$".
- Label equations only when referenced.
- Numerical claims are numbers with sources (demo, seed, tolerance), not
  adverbs.
- Keep proof, computation, citation, and illustration distinct.

## Gotchas

- Unslop is meaning-preserving: if a rewrite changed a mathematical statement,
  revert it.
- Don't "fix" quoted output, error messages, code identifiers, or citation
  keys.
- Cross-track links must remain full public URLs when they leave a subsite.
