# Phase 4 public cutover runbook

Status (2026-10-10): cutover live. Hub `2386290` serves `/math/` from this repo
and `/incerto-wiki/` as a full mirror of the old live site plus 28 compatibility
pages. The private repository's own Pages was removed; it is not archived.
`xshi-math` is the only authoring home for Incerto, IG, and Normix-theory notes.
Normix package docs at `/normix/` remain upstream.

The [preparation record](../records/phase-4-cutover-prep-verification.md) retains
the 2026-10-07 local gate; the [live record](../records/phase-4-live-verification.md)
records go-live. The [Phase 5 record](../records/phase-5-verification.md) records
the supplied live recheck against `xshi-math` main `3765783` and hub `2386290`.
Owner freeze/archive, two URL-map decisions, and the retained-page asset 404
remain open. The no-JS query/hash loss is accepted.

The original cutover sequence below is retained for audit and recovery; merge,
hub publication, and Pages removal are completed steps, not pending tasks.
For routine updates, replace only `math/` and preserve the whole legacy mirror
with its compatibility pages. If compatibility changes are authorized, overlay
only the generated tree without `--delete`. Never touch `/normix/`.

## Original cutover preconditions (historical)

- Xiang has confirmed the merge and the cutover PR is merged. Use the reviewed
  `xshi-math` revision, with no further source changes during publication.
- A fresh `npm run build && npm run check:html` passes. Record the source
  revision, toolchain versions, artifact checksum, and resulting hub commit.
- Use a **new clean hub clone**. At preparation time, the existing
  `/workspace/xshi19.github.io` checkout had unrelated deletions and was excluded.
- The owner confirms the effective Pages source/settings and pauses competing
  publishers/transfers for the publication window. Confirm that neither the
  private source publisher nor a hub writer can restore old mapped pages.
- Review the two unresolved rows and the retained gaps below. Their preservation
  was the adopted cutover treatment; it does not clear deferred rights reviews.

## Artifacts and URL rules

`npm run build` still builds four independent sites, assembles `_build/html/`,
and writes 48 flat `/math/` redirects. It then invokes
[`write_legacy_incerto.py`](../../scripts/write_legacy_incerto.py), which reads
[`url-map.csv`](url-map.csv) and writes `_build/legacy/incerto-wiki/`.
No sibling checkout is needed to build or check either artifact.

The CSV currently has 31 legacy rows: 29 mapped rows produce **28 HTML files**
pointing to **28 distinct built pages**; two rows are unresolved and skipped.
The root `/incerto-wiki/` and literal `/incerto-wiki/index.html` share the same
generated `index.html`. Directory routes normalize to a trailing slash;
`index-1/` explicitly targets `/math/notation/`, normalizing the CSV's
slashless destination. Other literal `.html` routes remain literal files.

Each compatibility file has no external assets: noindex, an absolute canonical
URL, immediate meta refresh, JavaScript, and a visible destination link. The
script preserves the query and unknown hash. Without JavaScript, the refresh
and visible link use the static fallback; query/hash forwarding requires JS.
Loss of the incoming query/hash is inherent to this static meta-refresh target
and accepted. Live no-JS browser coverage is still unrecorded.

Fragment columns are currently empty. When supplied, `old_fragment` and
`new_fragment` accept labels with or without `#`; URL-embedded fragments must
agree with the columns. An empty `old_fragment` defines the page's static
fallback, including any default `new_fragment`. Additional rows translate
matching hashes, with a visible link for each translated destination. These
rows require a page-level fallback; conflicting aliases, conflicting fragments,
or fragment-only mappings fail. Matching uses decoded fragment labels. Unknown
hashes pass through unchanged. `check:html` checks mapped destination fragments;
it does not claim to audit every historical automatic heading ID. Query-specific
CSV mappings are rejected because these files preserve queries at runtime.

`npm run check:html` verifies coverage, refresh/canonical/visible-link agreement,
noindex, JavaScript mapping data, and built destinations (including mapped IDs).
It rejects unexpected generated HTML and destinations that are themselves
redirects. It prints counts and every unresolved row with its reason.
Both output trees stay under the existing `_build/` ignore rule.

## Unresolved rows and retained route gaps

| Legacy URL (relative to `/incerto-wiki/`) | Retained disposition |
| --- | --- |
| `intro/` | Skip: the manifest defers SCoFT intro for rights review. The earlier `/math/incerto/incerto-scoft-intro/` proposal has no built page; preparation cleared that stale target. Retain existing hub output pending an owner decision. |
| `build/index-995d9205321c1213987db72d01de44bf.md` | Skip: no target is recorded; download treatment and artifact rights remain unresolved. Retain the existing file without changing its notices or relabeling it. |

The pre-cutover hub inventory below uses committed filenames only, from
`1511d5e358cc8040327e5a4df33d30ac3983fcef`:

```sh
git -C /workspace/xshi19.github.io ls-tree -r --name-only HEAD incerto-wiki/
```

Of 1,755 committed files, 55 are HTML. **37 HTML files are absent from the CSV**:
21 MyST routes and 16 files in `api/`. The latter include two HTML template
assets, listed conservatively rather than assumed to be reader entry points.
No mappings were added for these files at cutover. The excluded mixture
notes have related Normix pages but no asserted one-to-one Incerto destination.

| Unmapped group | Paths relative to `incerto-wiki/` |
| --- | --- |
| Examples (5) | `amazon-bookrank/index.html`, `dispersion-ratio/index.html`, `empirical-example-concepts/index.html`, `lln-preasymptotic/index.html`, `sp500-tail/index.html` |
| Reading/reference routes (8) | `ch3/index.html`, `ch4/index.html`, `ch5/index.html`, `ch6/index.html`, `ch7/index.html`, `embrechts-modelling-extremal-events/index.html`, `index-2/index.html`, `index-3/index.html` |
| Other legacy entries (8) | `api-reference/index.html`, `chinese-entry/index.html`, `dependency-dag/index.html`, `lean-blueprint/index.html`, `normal-mixture/index.html`, `releases/index.html`, `v0-1-0/index.html`, `variance-gamma/index.html` |
| API pages (9) | `api/index.html`, `api/genindex.html`, `api/py-modindex.html`, `api/search.html`, `api/modules.html`, `api/incerto.distributions.html`, `api/incerto.estimators.html`, `api/incerto.figures.html`, `api/incerto.stats.html` |
| API module views (5) | `api/_modules/index.html`, `api/_modules/incerto/distributions.html`, `api/_modules/incerto/estimators.html`, `api/_modules/incerto/figures.html`, `api/_modules/incerto/stats.html` |
| API template assets (2) | `api/_static/sbt-webpack-macros.html`, `api/_static/webpack-macros.html` |

The deployed mirror also includes files recovered from the old live site;
these pre-cutover counts do not describe the full deployed tree. Refresh this
filename audit against a clean clone before future compatibility updates. Preserve
all unmapped HTML, the unresolved `intro/`, and every non-overwritten file:
`build/` downloads and bundled assets (1,394 files at the inspected revision),
the entire `api/` tree, images, JSON/search data, styles, discovery files, and
service-worker files. **Preserve the entire hub `incerto-wiki/` tree.**
The compatibility tree overlays only its exact HTML paths. Retained pages may
still expose old navigation/search; this is frozen legacy output whose eventual
treatment belongs to Phase 5. Do not copy private source or newly generated
legacy book exports into the hub.

## Original publication sequence (completed; owner/operator reference)

These commands document the completed cutover. Reuse only the relevant build,
overlay, and review steps for an authorized future publication. Edit the clone
destination to a new, unused directory. `rsync` is required. Do not run builds concurrently.

```bash
set -euo pipefail
math_repo=/workspace/xshi-math
cutover_hub=/path/to/new-clean-hub-clone
cutover_audit="$math_repo/_build/phase4-publish"
mkdir -p "$cutover_audit"
cd "$math_repo"
npm ci
npm run build && npm run check:html
git rev-parse HEAD > "$cutover_audit/math-revision.txt"
node --version > "$cutover_audit/toolchain.txt"
npm --version >> "$cutover_audit/toolchain.txt"
python3 --version >> "$cutover_audit/toolchain.txt"
tar -C _build --sort=name --mtime=@0 --owner=0 --group=0 --numeric-owner \
  -cf - html legacy/incerto-wiki | sha256sum > "$cutover_audit/artifacts.sha256"

git clone --branch main --single-branch \
  https://github.com/xshi19/xshi19.github.io.git "$cutover_hub"
test -z "$(git -C "$cutover_hub" status --porcelain)"
git -C "$cutover_hub" rev-parse HEAD > "$cutover_audit/hub-before.txt"
git -C "$cutover_hub" ls-tree -r --name-only HEAD incerto-wiki/ \
  > "$cutover_audit/legacy-before.txt"
```

Review that inventory against the table above. Pause if the current hub has
new routes, changed ownership, or a publisher that can overwrite the cutover.
Then copy both artifacts into that clone:

```bash
rsync -a --checksum --delete "$math_repo/_build/html/" "$cutover_hub/math/"
rsync -a --checksum "$math_repo/_build/legacy/incerto-wiki/" "$cutover_hub/incerto-wiki/"
git -C "$cutover_hub" status --short
git -C "$cutover_hub" diff --stat
git -C "$cutover_hub" diff --check
```

The first copy replaces the owned math artifact. The second has **no `--delete`**:
it replaces mapped HTML files and adds mapped routes absent from the old build.
At the inspected hub revision, 17 existing HTML files are replaced and 11 are
added; 38 legacy HTML files stay byte-for-byte (37 gaps plus `intro/`). All
non-HTML legacy files stay byte-for-byte. Do not remove old assets just because
the compatibility files themselves do not use them.

Preview the assembled clone:

```bash
python3 -m http.server 8000 --directory "$cutover_hub"
```

Check `/math/`, its three tracks, `/math/notation/`, the old home,
Pareto, and a retained gap. Verify a legacy query/hash in a browser, e.g.
`/incerto-wiki/pareto/?cutover=1#pareto-definition`, and the visible fallback
with JS disabled. Check `/` and `/normix/` still work. Stop the preview server
before continuing.

Stage the two owned trees and review the full file list, including new files:

```bash
git -C "$cutover_hub" add -- math incerto-wiki
git -C "$cutover_hub" diff --cached --check
git -C "$cutover_hub" diff --cached --stat
git -C "$cutover_hub" diff --cached --name-status
```

Confirm the staged changes contain only the full `math/` artifact, generated
legacy HTML, and missing legacy files required by the switchover ordering below.
`/`, `/normix/`, and all other prefixes must remain unchanged. Then commit once
and push normally:

```bash
git -C "$cutover_hub" commit -m "Publish math cutover and Incerto compatibility pages"
git -C "$cutover_hub" rev-parse HEAD > "$cutover_audit/hub-cutover.txt"
git -C "$cutover_hub" push origin main
```

Never force-push `main`. If a concurrent update
rejects the push, assemble again from the latest hub revision in a clean clone,
review its inventory, and repeat the checks before a normal push.

## Pages switchover ordering (finding 2026-10-10)

Finding before removal: `https://xshi19.github.io/incerto-wiki/` was served by
the private repository's own GitHub Pages (`build_type: workflow`), shadowing
the hub folder. That Pages site has now been removed and the hub serves the
legacy URL. Do not repeat Pages removal for routine math updates.

The completed switchover used this ordering to keep the URL available:

1. Publish the single hub commit above: replace `math/` and overlay the
   compatibility pages. Before committing, also fill any gaps in the hub's
   `incerto-wiki/` tree compared with the live legacy site; delete nothing there.
2. Wait for the hub Pages build and deployment of that commit. Verify the
   compatibility pages from the hub clone or hub raw files while the legacy
   Pages site still shadows the folder.
3. Record the previous `incerto-wiki` Pages settings with
   `gh api repos/xshi19/incerto-wiki/pages`: `build_type`, `source`,
   `https_enforced`, and custom domain (`cname`). Then unpublish with
   `gh api -X DELETE repos/xshi19/incerto-wiki/pages` so the hub folder serves
   the legacy URL.
4. Run the live curl verification below.
5. The `incerto-wiki` repository's `main` has no Pages deploy workflow, and its
   earlier live artifact cannot be reproduced from the repository, so re-enabling
   Pages alone restores no site. Before unpublishing, the live site was
   snapshotted: the cutover hub commit includes every live legacy file missing
   from or differing in the hub's `incerto-wiki/` tree. Reverting that commit
   restores only the older hub tree and cannot restore those live-only files.
   Prefer keeping the hub's `incerto-wiki/` copy; restore the old Pages site with
   the recorded settings only if a deployable artifact is available.

The private repository was neither archived nor deleted by the switchover.

## Verify the live deployment

Wait for the hub's Pages deployment of the recorded commit. From `xshi-math`,
run the following curl list. It tests every mapped legacy URL (including the
literal `index.html` alias), every distinct new target, five entry pages, and
three representative flat math redirects. Curl does not execute meta refresh;
the legacy response itself must be HTTP 200 with the expected HTML metadata.

```bash
python3 - <<'PY'
import csv
import subprocess
import sys
from urllib.parse import urlsplit

sys.path.insert(0, "scripts")
from check_html import Links
from site_layout import ORIGIN, URL_MAP, normalize_page_path, redirects
from write_legacy_incerto import load_legacy_routes, report_skipped

pages, _, skipped = load_legacy_routes()
report_skipped(skipped)

def fetch(url):
    result = subprocess.run([
        "curl", "--silent", "--show-error", "--fail", "--max-time", "30",
        "--write-out", "\n%{http_code}", url.split("#", 1)[0],
    ], check=True, capture_output=True, text=True)
    body, status = result.stdout.rsplit("\n", 1)
    assert status == "200", (url, status)
    parser = Links()
    parser.feed(body)
    print("200", url)
    return parser

new_urls = {ORIGIN + path for path in (
    "/math/", "/math/incerto/", "/math/ig/", "/math/normix-theory/", "/math/notation/",
)} | {url.split("#", 1)[0] for page in pages.values() for url in page.targets.values()}
for url in sorted(new_urls):
    assert not fetch(url).refresh, url
with URL_MAP.open(newline="") as handle:
    for row in csv.DictReader(handle):
        if row["old_url"].startswith(ORIGIN + "/incerto-wiki/") and row["new_url"]:
            page = pages[normalize_page_path(urlsplit(row["old_url"]).path)]
            parser = fetch(row["old_url"])
            assert parser.canonical == [page.target], row
            assert parser.refresh == ["0; url=" + page.target], row
            assert "noindex" in parser.robots, row
            assert parser.visible_links == [page.target, *page.fragments.values()], row
for old in ("/math/incerto-pareto/", "/math/information-geometry/", "/math/normix-varentropy/"):
    new = redirects()[old]
    parser = fetch(ORIGIN + old)
    assert parser.canonical == [ORIGIN + new], old
    assert parser.refresh == ["0; url=" + new], old
    assert new in parser.visible_links, old
print("Live cutover curl checks passed.")
PY
```

Also check retained `/incerto-wiki/intro/`, one API route, a download, and the
hub and Normix homes. Browser checks must cover query/hash arrival, no-JS
fallback, rendered equations, and desktop/mobile navigation under `/math/`.
Use both a fresh browser profile and an existing one to catch retained
service-worker caches serving old HTML.
Record live results separately from the local preparation record. A local pass
does not establish live prefix ownership or historical-fragment coverage.

## Rollback

If live verification fails, the owner reverts the **single recorded hub cutover
commit** on current `main` and pushes normally. Read the recorded hash:

```bash
git -C "$cutover_hub" pull --ff-only origin main
cutover_commit="$(cat "$cutover_audit/hub-cutover.txt")"
git -C "$cutover_hub" revert "$cutover_commit"
git -C "$cutover_hub" push origin main
```

Review any conflicts against intervening hub changes; do not reset or force-push
history. Prefer preserving the hub's `incerto-wiki/` copy across the revert,
which alone loses the snapshotted live-only files; restore the old Pages site
only if a deployable artifact is available, as specified in the
[switchover ordering](#pages-switchover-ordering-finding-2026-10-10).
Wait for any resulting Pages deployments, then verify the restored legacy behavior and
sibling prefixes. Keep the source revision and combined artifact checksum. The owner decides
which authoring source remains authoritative while the defect is repaired.

## Outstanding owner and Phase 5 actions

1. Confirm the formal authoring freeze in private `incerto-wiki` and that
   obsolete publishers stay disabled. The deployed revision and live checks
   are already recorded; Phase 4 is marked live in the planning index.
2. Archive the private `incerto-wiki` repository, keeping it private as provenance
   and rollback history. This is an owner action only, after live verification
   and the authoring freeze. No archive action has been performed here.
3. Finish Phase 5: settle the two unresolved routes/download retention and fix
   the hub-only asset 404 requested by retained `intro/` and `sp500-tail/`:
   `/incerto-wiki/build/routes/$-O2KOSX5W.js`. This asset belongs to the hub mirror
   and cannot be repaired by regenerating compatibility pages in this repo.
   Track guidance cleanup and verification in the
   [Phase 5 record](../records/phase-5-verification.md).
   Keep compatibility URLs and rollback artifacts. The next content plan is in
   [consolidation](consolidation.md#one-time-consolidation-phases).
