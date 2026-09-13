# Information Geometry entry curriculum (draft)

Status: owner briefing + ChatGPT share extract, pending Phase 1 completion and an Astra Max outline pass.
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
- Local extract (working copy): `/workspace/xshi-math-codex/ig-chatgpt-share-extract.md` — also mirrored below as `ig-chatgpt-share-extract.md` when committed.

## Gate
Do not add public IG entry pages until Phase 1 MyST HTML build for `/math/` works. Then run Codex `gpt-6-astra` with **max** reasoning to produce a polished outline under `docs/plan/ig-entry-outline.md`, then implement entry pages under `content/information-geometry/`.
