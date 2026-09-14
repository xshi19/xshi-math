---
name: xshi-math-hub-publish
description: Build and optionally transfer the xshi-math multi-subsite HTML into the personal hub under /math/. Use when asked to rebuild the math site, run HTML checks, or refresh https://xshi19.github.io/math/. Do not use for Normix package docs at /normix/ (that stays in the normix repo gh-pages publisher).
---

# xshi-math Hub Publish

Thin publish note for this monorepo. Normix's `$docs-publish` skill and
`gh-pages` workflow remain upstream; they own
`https://xshi19.github.io/normix/`.

## Canonical facts

- Four MyST projects: landing, Incerto, IG, Normix theory (`myst.*.yml`).
- Build: `npm ci` (once), then `npm run build` → `scripts/build_sites.py`
  assembles `_build/html/`.
- Check: `npm run check:html`.
- Public base: `https://xshi19.github.io/math/` (landing) with track prefixes
  `/math/incerto/`, `/math/ig/`, `/math/normix-theory/`, plus shared
  `/math/notation/`.
- Hub checkout (typical local path): `/workspace/xshi19.github.io`.
- This repository does **not** change Pages settings or touch `/normix/`.

## Local build

```bash
npm ci
npm run build
npm run check:html
```

Preview under the real path:

```bash
mkdir -p _build/preview/math
rsync -a --delete _build/html/ _build/preview/math/
python3 -m http.server 8000 --directory _build/preview
```

Open `http://localhost:8000/math/` and the three track bases. Review equations
and desktop/mobile navigation when changing content or theme.

## Optional hub transfer

After a clean local build and HTML check, from this repository:

```bash
rsync -a --delete /workspace/xshi-math/_build/html/ /workspace/xshi19.github.io/math/
```

Trailing slashes matter. Review and commit/publish the hub change separately.
Do not run the transfer unless the user asked to refresh the live hub artifact.

## Completion Check

- Build and HTML check results are reported (or explicitly skipped).
- Hub transfer, if any, names source and destination paths.
- `/normix/` was not modified.
- Live Pages verification is reported as not run unless actually performed.
