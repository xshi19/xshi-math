# Source baselines and reading limits

Bibliographic and contents metadata were checked on 2026-10-16. The inventory
uses chapter locators and short editorial topic labels, not copied chapter
text or a substitute summary of the books. The associations between chapters
and our proposed concepts are editorial judgments. They are not assertions
that every proposed theorem appears in that chapter.

## Technical books in completion scope

There are two books in scope. Statistical Consequences of Fat Tails / Technical
Incerto is first and highest priority, including the 2025 additions; their
exact reconciliation remains open. Dynamic Hedging includes continuous time
as mathematical teaching and numerical work, regardless of Lean feasibility.

| ID | Selected locator baseline | Evidence and remaining work |
| --- | --- | --- |
| `scft` | *Statistical Consequences of Fat Tails* / *Technical Incerto*, volume 1, 2020 print spine, ISBN 9781544508054; 25 chapters and appendices A–H | [Print contents metadata](https://www.kriso.lt/statistical-consequences-fat-tails-real-world-db-9781544508054.html) and [2020 preprint v2](https://arxiv.org/abs/2001.10488v2). This is a comparison source, not a verified assertion that print and v2 pagination match. [The 2025 v4 record](https://arxiv.org/abs/2001.10488v4) describes a third revised edition with three added chapters and an appendix. These additions are required scope; exact locators and changed claims remain a reconciliation task. |
| `dh` | *Dynamic Hedging*, Wiley, 1997, ISBN 9780471152804; 23 chapters and modules A–G | [Publisher record and partial contents](https://www.wiley-vch.de/en/areas-interest/finance-economics-law/dynamic-hedging-978-0-471-15280-4) and [complete bibliographic contents locator](https://www.yes24.com/product/goods/80530). Reconcile exact section/page locators against the selected copy. |

The retailer/catalog records are used only to locate chapters and editions.
They supply no evidence for mathematical, financial, behavioral, medical or
historical claims. Read the primary book/paper before adopting such a claim.
No book text or source PDF is stored in this plan.

The Technical Incerto PDFs could not be fully inspected in this environment:
the browser rejected the large v2/v4 downloads, and shell retrieval lacked
working DNS. The edition map therefore rests on the accessible contents and
version metadata. This limit is recorded in state; the expansion is not
silently treated as already covered. The earlier queue's “Chapter 4 Cauchy
Running Statistics” label also needs reconciliation: the selected 2020
contents put finite-moment tails in chapter 4. The simulation concept survives
without inventing a matching chapter number.

## Retained origin references outside completion

The five non-technical books are out of scope. Their bibliographic and source
IDs remain stable so existing references resolve; no chapter, interpretation,
prose-only note or edition-review task is required. A technical page may cite
one only as an origin reference after checking the actual locator.

| ID | Retained reference | Status |
| --- | --- | --- |
| `fbr` | *Fooled by Randomness*, 2008 updated second edition, ISBN 9781400067930; [publisher](https://www.penguinrandomhouse.com/books/176225/fooled-by-randomness-by-nassim-nicholas-taleb/9781400067930/) | out-of-scope |
| `tbs` | *The Black Swan*, 2010 second edition, ISBN 9780812973815; [publisher](https://www.penguinrandomhouse.com/books/176226/the-black-swan-second-edition-by-nassim-nicholas-taleb/9780812973815/) | out-of-scope |
| `bop` | *The Bed of Procrustes*, historical 2010 locator baseline, ISBN 9781400069972; [publisher](https://www.penguinrandomhouse.com/books/210246/the-bed-of-procrustes-by-nassim-nicholas-taleb/hardcover/) | out-of-scope |
| `af` | *Antifragile*, 2014 paperback, ISBN 9780812979688; [publisher](https://www.penguinrandomhouse.com/books/176227/antifragile-by-nassim-nicholas-taleb/) | out-of-scope |
| `sitg` | *Skin in the Game*, 2018 ebook, ISBN 9780425284636; [publisher](https://www.penguinrandomhouse.com/books/537828/skin-in-the-game-by-nassim-nicholas-taleb/9780425284636/) | out-of-scope |

## Papers

The [paper inventory](inventory.md#selected-technical-papers) links 14 pinned
preprint versions, including Corral's critical response to the epidemic-tail
paper. Their titles, authors and version histories were checked on arXiv.
This run did not review every full-text proof, dataset or revision difference.
`locator_review: metadata-verified-full-text-scope-pending` records that limit.

Before writing a note, identify the precise section and theorem/equation in
the selected version, then compare definitions and hypotheses with the
proposed statement. For disputed empirical applications, inspect the primary
data and competing analysis. A paper's abstract, or the fact that it was
published, does not certify its assumptions or justify carrying its policy
conclusions into a note. The precaution and convex-response papers require
particular care to distinguish mathematical models, domain evidence and
normative conclusions.

On-demand inclusion is approved: add an immutable paper ID/version when a
concrete mathematical claim needs it. The 14 records are a starting set, not
an exhaustive bibliography or a requirement to cover every paper in full.
Interpretive, ethical, clinical and policy sections are outside completion.
Citation locators and proof dependencies should survive later edition additions.

## Existing repository coverage

The survey found 24 flat Incerto concept bodies, three concept indexes and the
track hub. Twenty-three bodies came through approved adaptation batches; the
counting-exceedances body and fixed example were original foundation work.
The [concept register](concepts.md) links every body and describes its bounded
scope. Indexes and the hub are navigation, not four additional mathematical
concepts. The numerical helper is not a historical-data study.

The survey inspected definitions, stated claims, caveats, proof/citation labels
and available executable artifacts. It was not a fresh proof audit. In
particular, general Karamata, threshold-limit and stable-limit statements must
not be labeled checked because an existing page derives a special case or
cites a source. Existing prose, runnable evidence and Lean evidence have
separate fields in state.

M0.5 now requires a claim-by-claim review of all 24 bodies by Astra max and a
reader-view review of their live counterparts by Math Site Editor. The
[review record](m0.5-review.md) defines the issues list for Xiang. Both remain
pending; the baseline survey is not evidence that either review has happened.

## Dataset sources

Financial data come from the Portfolio Manager bot through Xiang's financial
database; request additions there. Other data come from the Data Scientist
bot. Record each handoff, original provider, version, retrieval date, license,
redistribution terms, checksum, cleaning and units. Bot routing is settled;
each dataset still needs its own provenance and permitted-use record.

## Copyright and legacy material

The owner authorized original concept explanations, derivations, proofs and
code with book/chapter citations. Never copy or closely paraphrase source
text; include no long quotations, reconstructed aphorism collections, scans
or reproduced book figures. Repository-owned work remains under the repository
license; third-party sources retain their own rights. Data and borrowed code
need separate provenance and terms.

This authorization does not approve the old `intro/` SCoFT-derived asset or
the retained Markdown download. Their unresolved rows in
[the URL map](../url-map.csv) and the owner actions in
[the planning index](../index.md) remain unchanged. No legacy import, hub
transfer, freeze/archive action or site publication is part of this design.
