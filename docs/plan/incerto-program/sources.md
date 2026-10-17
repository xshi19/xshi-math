# Source baselines and reading limits

The SCoFT locator baseline is the **2025 third edition,
arXiv:2001.10488v4**. The 2026-10-17 revision directly compared both supplied
PDF tables of contents and their extracted files. Only titles, bibliographic
metadata and locators are retained here. No PDF, TOC extract, bibliography
file, book text or source figure was copied into the repository.

## Technical books in completion scope

| ID | Selected locator baseline | Evidence and remaining work |
| --- | --- | --- |
| `scft` | *Statistical Consequences of Fat Tails* / *Technical Incerto*, 2025 third edition, [arXiv:2001.10488v4](https://arxiv.org/abs/2001.10488v4); 30 chapters and appendices A–I | Direct local PDF TOC review, with [v2](https://arxiv.org/abs/2001.10488v2) for correspondence only. Locator reconciliation is complete; theorem hypotheses and exact claim locators remain per-chapter review work. |
| `dh` | *Dynamic Hedging*, Wiley, 1997, ISBN 9780471152804; 23 chapters and modules A–G | [Publisher](https://www.wiley-vch.de/en/areas-interest/finance-economics-law/dynamic-hedging-978-0-471-15280-4) and [catalog contents](https://www.yes24.com/product/goods/80530). Catalog chapter/module titles were rechecked; exact section/page locators require the selected copy. Stochastic-calculus depth is limited to basics needed for hedging concepts. |

The 2020 print ISBN and catalog are historical comparison metadata, not the
active SCoFT citation namespace. Do not combine v4 chapter numbers with print
or v2 pagination. Catalog contents locate material; they do not establish a
mathematical or empirical claim.

## Local v2 and v4 evidence

Read-only inputs remain under `/workspace/scoft-toc/`:

| Input | Locator evidence |
| --- | --- |
| `2001.10488v2.pdf`, `v2-toc.txt` | 455 PDF pages; TOC on PDF pages 7–14, printed vii–xiv; 25 chapters and appendices A–H |
| `2001.10488v4.pdf`, `v4-toc.txt` | 523 PDF pages; TOC on PDF pages 7–14, printed vii–xiv; 30 chapters and appendices A–I |
| `v4-bib.txt` | Bibliographic locators [177], [289], [296] identify the portfolio-correlation, single-point-forecast and probability-conflation papers |

`pdfinfo` reported 455/523 pages. Direct `pdftotext -f 7 -l 14 -layout`
extraction matched every numbered chapter and lettered appendix title/starting
page in the supplied extracts. The extracted files also contain front/back
matter; comparison was restricted to TOC records. A harmless PDF annotation
warning did not prevent extraction. SHA-256 identities:

- v2: `4dd2b89befd1295df5ef3272778aa9f3ab00ee593784d699e6d6b9facc6d31ac`
- v4: `758e18b7337840104db93296144d67cf5514bf2de128fe557dc84bc32a0ad567`

The old environment's inability to download the PDFs no longer limits TOC
reconciliation: this revision used the owner's local copies. This was a
contents/locator comparison, not a proof audit or a full edition-text diff.

## Mapping findings

The [complete correspondence table](inventory.md#v2-to-v4-correspondence)
accounts for all 33 v2 units. There is no deviation from the expected
insertion pattern. Chapters 1–11 retain their numbers; the shifts thereafter
are +2 for 12–16, +3 for 17–19, +4 for 20–24 and +5 for 25. Appendix A stays
A; B–H become C–I. The delta is **five numbered chapters and one appendix**,
not just the three main additions described in earlier metadata.

| V4 addition | Exact TOC title (capitalization normalized) | Printed page |
| --- | --- | --- |
| Chapter 12 | On single point forecasts for fat-tailed variables | 241 |
| Chapter 13 | The probability conflation | 253 |
| Chapter 19 | Tail risk of contagious diseases | 347 |
| Chapter 23 | Lindy as distance from an absorbing barrier | 405 |
| Chapter 29 | Portfolios should never rely on correlation | 459 |
| Appendix B | Fat tails from maximum entropy | 127 |

“Unchanged chapters 1–11” means unchanged numbering. Chapter 8's TOC title
is shortened in v4. Other title changes affect v2 chapter 14 → v4 16,
21 → 25, 22 → 26, and appendix B → C; both titles are in the mapping table.
No equation, theorem or section correspondence is inferred from these offsets.

The old queue's “Chapter 4 Cauchy Running Statistics” label was incorrect.
Both TOCs place limit distributions in chapter 7; the planned bounded-runtime
simulation attaches to v4 §§7.2.1/7.6 (pp. 139/148). It is an original demo
association, not a claim that the source contains a section with that name.

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

The [paper inventory](inventory.md#selected-technical-papers) now has 16
records: the 14 pinned preprints retained from the earlier review, plus the
probability-conflation reply and the journal portfolio-correlation paper.
Each has a host chapter. Incorporated papers link their v4 chapter locator;
supporting papers are marked as editorial reading attachments.

| Paper | Chapter | Publication evidence |
| --- | --- | --- |
| [On Single Point Forecasts for Fat-Tailed Variables](https://arxiv.org/abs/2007.16096v1) | V4 ch. 12 | IJF, 2022; v4 bibliography [289]. The existing preprint version remains pinned. |
| [The Probability Conflation: A Reply](https://arxiv.org/abs/2301.10985v1) | V4 ch. 13 | [IJF 39(2), 1026–1029 (2023)](https://www.sciencedirect.com/science/article/abs/pii/S0169207023000055), DOI 10.1016/j.ijforecast.2023.01.005; v4 bibliography [296]. Published title: *The probability conflation: A reply to Tetlock et al.* |
| *Pension Funds Should Never Rely on Correlation* | V4 ch. 29 | R. Lagnado and N. N. Taleb, JAI 24(4), 8–17 (2022); v4 bibliography [177]. Chapter title starts *Portfolios*; journal title starts *Pension Funds*. The [publisher DOI route](https://doi.org/10.3905/jai.2022.1.157) was inaccessible here; journal metadata is supported by the supplied bibliography, not a claimed publisher full-text review. |

The v4 chapter and bibliography records support these correspondences, not
identity of every version's claims. Existing chapter-version links include
the disease paper → ch. 19, Gini → ch. 15, quantile contributions → ch. 16,
random exponent → ch. 21, power-law options → ch. 27 and entropy → ch. 30.
Corral's critical response remains attached to the disease study.

Before writing, identify the exact section, theorem/equation and hypotheses
in each selected version. Review competing analyses and primary data for
disputed empirical applications. No paper abstract or publication status
certifies assumptions or supports a clinical, investment or policy conclusion.
On-demand inclusion remains approved for concrete mathematical claims; add a
stable versioned record and chapter attachment. Full-paper coverage is not
required merely because a paper is listed.

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
