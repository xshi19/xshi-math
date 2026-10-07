"""Generate the separate /incerto-wiki/ compatibility artifact from the URL map."""

import csv
from dataclasses import dataclass, field
from html import escape
import json
import shutil
from urllib.parse import quote, unquote, urlsplit, urlunsplit

from site_layout import (
    BASE, HTML, LEGACY_BASE, LEGACY_HTML, ORIGIN, URL_MAP,
    normalize_page_path, page_file,
)


@dataclass
class LegacyPage:
    old: str
    # Empty key is the static fallback; other keys translate old fragments.
    targets: dict[str, str] = field(default_factory=dict)

    @property
    def target(self):
        return self.targets[""]

    @property
    def fragments(self):
        return {key: value for key, value in self.targets.items() if key}


def fragment_value(url_fragment, column):
    column = column.removeprefix("#")
    if url_fragment and column and unquote(url_fragment) != unquote(column):
        raise ValueError("URL fragment conflicts with the fragment column")
    return unquote(column or url_fragment)


def load_legacy_routes(csv_path=URL_MAP):
    """Return pages, mapped row count, and explicitly unresolved rows.

    Fragment overrides need a page-level row for the static/no-JS fallback.
    Aliases may share a file, but must agree on all destinations.
    """
    pages = {}
    mapped = 0
    skipped = []
    with csv_path.open(newline="", encoding="utf-8") as handle:
        for line, row in enumerate(csv.DictReader(handle), start=2):
            old_url = urlsplit(row["old_url"])
            if (old_url.scheme + "://" + old_url.netloc != ORIGIN
                    or not (old_url.path == LEGACY_BASE
                            or old_url.path.startswith(LEGACY_BASE + "/"))):
                continue
            if not row["new_url"].strip():
                reason = "; ".join(filter(None, (
                    row["route_behavior"], row["verification_status"],
                )))
                if not reason:
                    raise ValueError(f"URL map line {line}: empty target needs a recorded reason")
                skipped.append({"line": line, "old_url": row["old_url"], "reason": reason})
                continue
            try:
                new_url = urlsplit(row["new_url"])
                if old_url.query or new_url.query:
                    raise ValueError("Query-specific mappings are unsupported; queries are preserved at runtime")
                if new_url.scheme + "://" + new_url.netloc != ORIGIN:
                    raise ValueError("Legacy destination must use the public origin")
                old = normalize_page_path(old_url.path)
                new = normalize_page_path(new_url.path)
                page_file(LEGACY_HTML, old, LEGACY_BASE)
                page_file(HTML, new, BASE)
                old_fragment = fragment_value(old_url.fragment, row["old_fragment"])
                new_fragment = fragment_value(new_url.fragment, row["new_fragment"])
                target = urlunsplit(("https", new_url.netloc, new, "", quote(new_fragment, safe="")))
                page = pages.setdefault(old, LegacyPage(old))
                if old_fragment in page.targets and page.targets[old_fragment] != target:
                    raise ValueError(f"Conflicting destinations for {old}#{old_fragment}")
                page.targets[old_fragment] = target
                mapped += 1
            except ValueError as error:
                raise ValueError(f"URL map line {line}: {error}") from error
    if not pages:
        raise ValueError("URL map has no mapped legacy pages")
    for page in pages.values():
        if "" not in page.targets:
            raise ValueError(f"{page.old}: fragment mappings need a page-level fallback row")
    return pages, mapped, skipped


def report_skipped(skipped):
    for row in skipped:
        print(f"UNRESOLVED (skipped, line {row['line']}): {row['old_url']} — {row['reason']}")


def script_json(value):
    """JSON embedded in a script must not be able to close its HTML element."""
    return json.dumps(value, ensure_ascii=True).replace("<", "\\u003c").replace(
        ">", "\\u003e"
    ).replace("&", "\\u0026")


def render_page(page):
    target = escape(page.target, quote=True)
    fragment_links = "".join(
        f'<li><a href="{escape(url, quote=True)}">#{escape(fragment)}</a></li>'
        for fragment, url in page.fragments.items()
    )
    if fragment_links:
        fragment_links = f"<ul>{fragment_links}</ul>"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Page moved</title>
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
<script id="legacy-redirect" type="application/json">{script_json({"target": page.target, "fragments": page.fragments})}</script>
<script>
const mapping = JSON.parse(document.getElementById("legacy-redirect").textContent);
let fragment = window.location.hash.slice(1);
try {{ fragment = decodeURIComponent(fragment); }} catch {{ /* Preserve malformed hashes. */ }}
const translated = Object.prototype.hasOwnProperty.call(mapping.fragments, fragment);
const target = new URL(translated ? mapping.fragments[fragment] : mapping.target);
target.search = window.location.search;
if (!translated && window.location.hash) target.hash = window.location.hash;
window.location.replace(target.href);
</script>
</head>
<body><p>This page has moved to <a href="{target}">{escape(page.target.removeprefix(ORIGIN))}</a>.</p>{fragment_links}</body>
</html>
"""


def main():
    pages, mapped, skipped = load_legacy_routes()
    report_skipped(skipped)
    for page in pages.values():
        for url in page.targets.values():
            if not page_file(HTML, urlsplit(url).path, BASE).is_file():
                raise SystemExit(f"Missing legacy destination: {url}")
    # This tree contains generated compatibility files only, never hub assets.
    if LEGACY_HTML.exists():
        shutil.rmtree(LEGACY_HTML)
    for page in pages.values():
        output = page_file(LEGACY_HTML, page.old, LEGACY_BASE)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render_page(page), encoding="utf-8")
    print(f"Wrote {len(pages)} legacy compatibility pages for {mapped} mapped rows; "
          f"{len(skipped)} unresolved rows skipped. Output: {LEGACY_HTML}")


if __name__ == "__main__":
    main()
