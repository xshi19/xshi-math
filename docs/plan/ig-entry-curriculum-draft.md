# Information Geometry entry curriculum (draft)

Status: owner briefing retained; developed into the [entry outline](ig-entry-outline.md)
and first batch of public notes after the Phase 1 local HTML gate passed.
Updated: 2026-09-13.

## Owner briefing (Xiang)

Desired starting structure (not a frozen TOC — outline may be reorganized):

### Basics
- Differential geometry: only what IG needs; start from Euclidean geometry; motivate the move to manifolds and make abstract notions concrete.
- Exponential families: why special in probability/statistics; derive the definition from sufficient statistics where possible; collect properties needed later.
- Latent-variable models and EM.
- Information theory (optional): entropy, KL, and other notions that actually reappear later.

### Information geometry
- From exponential families and Fisher geometry: why not put Euclidean \(L^2\) distance on the raw parameter vector.
- Core concepts with statistical intuition: dually flat, curvature, orthogonality, information-geometry Pythagoras, \(\alpha\)-connections.
- Then deepen: EM as projection, conditional expectation as projection, joint vs marginal, formulas important to Normix.

### Later (plan now, write later)
- GH / Normix specialization and research priorities (marginal metric, missing information, EM rate, curvature on low-dimensional subfamilies).

## Source material to keep
- Shared ChatGPT conversation: [Information Geometry of Marginals](https://chatgpt.com/share/6aa5f5d6-1060-83ea-a30b-6c71f42b8768)
- [Local conversation extract](ig-chatgpt-share-extract.md), retained as a planning input.

## Gate and current implementation

The pinned Phase 1 HTML build for `/math/` now works. The owner authorized the
outline and first entry batch with Codex `gpt-6-astra` at **max** reasoning.
The [polished outline](ig-entry-outline.md) owns page scope and later work.

The original nested `content/information-geometry/` suggestion is superseded by
the owner's filename requirement: use unique `information-geometry-*.md` stems
flat under `content/`, with `information-geometry.md` as the hub. MyST 1.10.1
ignores `slug:` and repeated nested `index.md` filenames produce `index-N/`
routes. GH/Normix research remains planned for later batches.
