# Source baselines and reading limits

Bibliographic and contents metadata were checked on 2026-10-16. The inventory
uses chapter locators and short editorial topic labels, not copied chapter
text or a substitute summary of the books. The associations between chapters
and our proposed concepts are editorial judgments. They are not assertions
that every proposed theorem appears in that chapter.

## Books

| ID | Selected locator baseline | Evidence and remaining work |
| --- | --- | --- |
| `fbr` | *Fooled by Randomness*, updated second edition, 2008 hardcover, ISBN 9781400067930; 14 chapters plus opening/closing material | [Publisher edition](https://www.penguinrandomhouse.com/books/176225/fooled-by-randomness-by-nassim-nicholas-taleb/9781400067930/) and [five-volume contents metadata](https://www.kriso.ee/incerto-fooled-randomness-black-swan-bed-db-9780593243657.html?lang=en). Check postscript and page locators in the selected copy. |
| `tbs` | *The Black Swan*, second edition, 2010, ISBN 9780812973815; 19 chapters and nine sections of the robustness essay | [Publisher edition](https://www.penguinrandomhouse.com/books/176226/the-black-swan-second-edition-by-nassim-nicholas-taleb/9780812973815/) and the five-volume contents metadata above. Keep the second-edition essay distinct from numbered chapters. |
| `bop` | *The Bed of Procrustes*, 2010 thematic spine, hardcover ISBN 9781400069972; 22 unnumbered thematic units plus opening material and postface | [Hardcover record](https://www.penguinrandomhouse.com/books/210246/the-bed-of-procrustes-by-nassim-nicholas-taleb/hardcover/) and five-volume contents metadata. The [expanded 2016 paperback](https://www.penguinrandomhouse.com/books/210246/the-bed-of-procrustes-by-nassim-nicholas-taleb/), ISBN 9780812982404, needs a separate contents comparison. Publisher/catalog records can describe different revisions; do not infer expanded coverage from a matching title. |
| `af` | *Antifragile*, 2014 paperback, ISBN 9780812979688, first published 2012; 25 chapters, prologue, two appendices and glossary | [Publisher edition](https://www.penguinrandomhouse.com/books/176227/antifragile-by-nassim-nicholas-taleb/) and five-volume contents metadata. Verify mathematical-supplement details directly before citing a result. |
| `sitg` | *Skin in the Game*, 2018 ebook, ISBN 9780425284636; 19 chapters, three prologue parts, two appendices and epilogue | [Publisher edition](https://www.penguinrandomhouse.com/books/537828/skin-in-the-game-by-nassim-nicholas-taleb/9780425284636/) and five-volume contents metadata. Ebook page numbers are not portable across print editions. |
| `scft` | *Statistical Consequences of Fat Tails* / *Technical Incerto*, volume 1, 2020 print spine, ISBN 9781544508054; 25 chapters and appendices A–H | [Print contents metadata](https://www.kriso.lt/statistical-consequences-fat-tails-real-world-db-9781544508054.html) and [2020 preprint v2](https://arxiv.org/abs/2001.10488v2). This is a comparison source, not a verified assertion that print and v2 pagination match. [The 2025 v4 record](https://arxiv.org/abs/2001.10488v4) describes a third revised edition with three added chapters and an appendix. Added locators remain an explicit backlog item. |
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

This is a selected corpus, not a claim to cover every Taleb technical paper.
Add an immutable paper ID/version when a specific concept needs it. Citation
locators and proof dependencies should survive later edition additions.

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
