"""Build four isolated MyST exports, then assemble the /math/ artifact.

MyST 1.10 writes to _build/html regardless of --config. Save each export
before starting the next, and clear project state while reusing the theme.
"""

import os
import re
import shutil
import subprocess
import sys
from xml.etree import ElementTree as ET

from site_layout import HTML, ORIGIN, REPO, SITES
from build_concept_graph import stage_graph_assets


def write_sitemaps():
    """Replace the theme's localhost discovery URLs with public nested URLs."""
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", namespace)
    for site in SITES:
        urlset = ET.Element(f"{{{namespace}}}urlset")
        # The landing's sitemap covers the whole assembled artifact.
        for included in (SITES if not site.key else (site,)):
            for page in included.pages:
                entry = ET.SubElement(urlset, f"{{{namespace}}}url")
                ET.SubElement(entry, f"{{{namespace}}}loc").text = ORIGIN + included.url(page)
        directory = HTML / site.key
        ET.indent(urlset)
        ET.ElementTree(urlset).write(directory / "sitemap.xml", encoding="utf-8", xml_declaration=True)
        (directory / "robots.txt").write_text(
            f"User-agent: *\nAllow: /\nSitemap: {ORIGIN}{site.base}/sitemap.xml\n"
        )


# The pinned theme bundle carries npm package metadata whose `_args` and
# `_where` values hold its upstream builder's Windows profile path (escaped in
# JS source). Rewrite only those values: `_args:[["name@version","<path>"`
# and `_where:"<path>"` directly after `_spec:"..."`, as npm writes them.
_PROFILE = r'[A-Za-z]:(?:/|\\)+Users(?:/|\\)+[^"/\\]+'
NPM_METADATA_PROFILE = re.compile(
    r'((?<![\w$])(?:_args:\[\["[^"@]+@[^"]+",|_spec:"[^"]*",_where:)")' + _PROFILE
)


def strip_npm_metadata_profiles(text):
    """Replace Windows profile prefixes in bundled npm `_where`/`_args` values."""
    return NPM_METADATA_PROFILE.sub(r"\1<user-home>", text)


def strip_checkout_paths():
    """Publish without local paths.

    MyST embeds the resolved bibliography path; publish it repo-relative.
    Replace Windows profile prefixes left in bundled npm package metadata.
    """
    prefix = f'"bibliography":["{REPO.as_posix()}/'
    for path in HTML.rglob("*"):
        if path.suffix in (".html", ".json"):
            text = path.read_text(encoding="utf-8")
            if prefix in text:
                path.write_text(text.replace(prefix, '"bibliography":["'), encoding="utf-8")
        elif path.suffix == ".js":
            data = path.read_bytes()
            if b"Users" not in data:
                continue
            # surrogateescape round-trips any non-UTF-8 bytes unchanged.
            text = data.decode("utf-8", "surrogateescape")
            cleaned = strip_npm_metadata_profiles(text)
            if cleaned != text:
                path.write_bytes(cleaned.encode("utf-8", "surrogateescape"))


def main():
    build = REPO / "_build"
    exports = build / "subsites"
    if exports.exists():
        shutil.rmtree(exports)
    exports.mkdir(parents=True)
    for site in SITES:
        key = site.key or "landing"
        for name in ("site", "html"):
            path = build / name
            if path.exists():
                shutil.rmtree(path)
        print(f"Building {site.title} at {site.base}/", flush=True)
        subprocess.run(
            [str(REPO / "node_modules/.bin/myst"), "--config", f"myst.{key}.yml",
             "build", "--html", "--strict", "--ci"],
            cwd=REPO, env={**os.environ, "BASE_URL": site.base}, check=True,
        )
        shutil.move(HTML, exports / key)

    shutil.copytree(exports / "landing", HTML)
    for site in SITES[1:]:
        shutil.copytree(exports / site.key, HTML / site.key)
    stage_graph_assets(HTML / "incerto")
    subprocess.run([sys.executable, str(REPO / "scripts/write_redirects.py")], check=True)
    write_sitemaps()
    strip_checkout_paths()
    subprocess.run([sys.executable, str(REPO / "scripts/write_legacy_incerto.py")], check=True)
    print(f"Assembled all four sites at {HTML}")


if __name__ == "__main__":
    main()
