"""Build four isolated MyST exports, then assemble the /math/ artifact.

MyST 1.10 writes to _build/html regardless of --config. Save each export
before starting the next, and clear project state while reusing the theme.
"""

import os
import shutil
import subprocess
import sys
from xml.etree import ElementTree as ET

from site_layout import HTML, ORIGIN, REPO, SITES


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
    subprocess.run([sys.executable, str(REPO / "scripts/write_redirects.py")], check=True)
    write_sitemaps()
    print(f"Assembled all four sites at {HTML}")


if __name__ == "__main__":
    main()
