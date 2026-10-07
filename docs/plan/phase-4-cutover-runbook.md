# Phase 4 public cutover runbook

Status (2026-10-07): ready / in progress — artifacts in this PR; pending owner
merge + hub push. Xiang approved preparation on 2026-10-07, with confirmation
before merge. This document contains operator instructions; preparing it does
not publish, merge, freeze authoring, or archive a repository.
See the [preparation record](../records/phase-4-cutover-prep-verification.md):
the fresh build and `check:html` gate passed on 2026-10-07 in the operator's run
outside the sandbox. The remaining owner gates below still apply.

## Preconditions

- Xiang has confirmed the merge and this PR is merged. Use the reviewed
  `xshi-math` revision, with no further source changes during publication.
- A fresh `npm run build && npm run check:html` passes. Record the source
  revision, toolchain versions, artifact checksum, and resulting hub commit.
- Use a **new clean hub clone**. The existing `/workspace/xshi19.github.io`
  checkout has unrelated deletions and must not be used or repaired for this task.
- The owner confirms the effective Pages source/settings and pauses competing
  publishers/transfers for the publication window. Confirm that neither the
  private source publisher nor a hub writer can restore old mapped pages.
- Review the two unresolved rows and the retained gaps below. Their preservation
  is the proposed cutover treatment; it does not clear deferred rights reviews.

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

| Legacy URL (relative to `/incerto-wiki/`) | Preparation disposition |
| --- | --- |
| `intro/` | Skip: the manifest defers SCoFT intro for rights review. The earlier `/math/incerto/incerto-scoft-intro/` proposal has no built page; this PR clears that stale target. Retain existing hub output pending an owner decision. |
| `build/index-995d9205321c1213987db72d01de44bf.md` | Skip: no target is recorded; download treatment and artifact rights remain unresolved. Retain the existing file without changing its notices or relabeling it. |

The hub inventory uses committed filenames only, from
`1511d5e358cc8040327e5a4df33d30ac3983fcef`:

```sh
git -C /workspace/xshi19.github.io ls-tree -r --name-only HEAD incerto-wiki/
```

Of 1,755 committed files, 55 are HTML. **37 HTML files are absent from the CSV**:
21 MyST routes and 16 files in `api/`. The latter include two HTML template
assets, listed conservatively rather than assumed to be reader entry points.
No new mappings are proposed for these files in this PR. The excluded mixture
notes have related Normix pages but no asserted one-to-one Incerto destination.

| Unmapped group | Paths relative to `incerto-wiki/` |
| --- | --- |
| Examples (5) | `amazon-bookrank/index.html`, `dispersion-ratio/index.html`, `empirical-example-concepts/index.html`, `lln-preasymptotic/index.html`, `sp500-tail/index.html` |
| Reading/reference routes (8) | `ch3/index.html`, `ch4/index.html`, `ch5/index.html`, `ch6/index.html`, `ch7/index.html`, `embrechts-modelling-extremal-events/index.html`, `index-2/index.html`, `index-3/index.html` |
| Other legacy entries (8) | `api-reference/index.html`, `chinese-entry/index.html`, `dependency-dag/index.html`, `lean-blueprint/index.html`, `normal-mixture/index.html`, `releases/index.html`, `v0-1-0/index.html`, `variance-gamma/index.html` |
| API pages (9) | `api/index.html`, `api/genindex.html`, `api/py-modindex.html`, `api/search.html`, `api/modules.html`, `api/incerto.distributions.html`, `api/incerto.estimators.html`, `api/incerto.figures.html`, `api/incerto.stats.html` |
| API module views (5) | `api/_modules/index.html`, `api/_modules/incerto/distributions.html`, `api/_modules/incerto/estimators.html`, `api/_modules/incerto/figures.html`, `api/_modules/incerto/stats.html` |
| API template assets (2) | `api/_static/sbt-webpack-macros.html`, `api/_static/webpack-macros.html` |

Refresh this filename audit against the clean clone before publishing. Preserve
all unmapped HTML, the unresolved `intro/`, and every non-overwritten file:
`build/` downloads and bundled assets (1,394 files at the inspected revision),
the entire `api/` tree, images, JSON/search data, styles, discovery files, and
service-worker files. **Remove nothing under `incerto-wiki/` in Phase 4.**
The compatibility tree overlays only its exact HTML paths. Retained pages may
still expose old navigation/search; this is frozen legacy output whose eventual
treatment belongs to Phase 5. Do not copy private source or newly generated
legacy book exports into the hub.

## Publish one hub commit (owner/operator only)

Run these commands only after the preconditions hold. Edit the clone destination
to a new, unused directory. `rsync` is required. Do not run builds concurrently.

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

Confirm the staged changes contain only the full `math/` artifact and the exact
generated legacy HTML paths. `/`, `/normix/`, and all other prefixes must remain
unchanged. Then commit once and push normally:

```bash
git -C "$cutover_hub" commit -m "Publish math cutover and Incerto compatibility pages"
git -C "$cutover_hub" rev-parse HEAD > "$cutover_audit/hub-cutover.txt"
git -C "$cutover_hub" push origin main
```

Never force-push `main`. If a concurrent update
rejects the push, assemble again from the latest hub revision in a clean clone,
review its inventory, and repeat the checks before a normal push.

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
history. Wait for Pages, then verify the restored legacy behavior and sibling
prefixes. Keep the source revision and combined artifact checksum. The owner decides
which authoring source remains authoritative while the defect is repaired.

## After successful go-live (owner actions)

1. Record the deployed hub commit and passing live/browser checks. Freeze all
   Incerto authoring in the private `incerto-wiki` repository; `xshi-math` is the
   only Incerto authoring home. Confirm obsolete publishers cannot overwrite
   the compatibility files, then mark Phase 4 complete in the planning index.
2. Archive the private `incerto-wiki` repository, keeping it private as provenance
   and rollback history. This is an owner action only, after live verification
   and the authoring freeze; no archive API or command runs in this PR.
3. Start Phase 5: verify stability, settle unresolved routes/download retention,
   and prune obsolete guidance or build machinery in separate reviewed changes.
   Keep compatibility URLs and rollback artifacts. The next content plan is in
   [consolidation](consolidation.md#one-time-consolidation-phases).
