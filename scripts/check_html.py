"""Check every assembled page, independent navigation, and old flat redirect.

Run after ``npm run build``. Browser interaction is reviewed separately.
"""

from html.parser import HTMLParser
import json
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree as ET

from site_layout import BASE, HTML, ORIGIN, REPO, SITES, redirects

# The IG home contains a display equation. Only these indexes lack equations.
NO_MATH = {
    "/math/", "/math/incerto/", "/math/normix-theory/",
    "/math/incerto/incerto-theorem-concepts/",
    "/math/incerto/incerto-method-concepts/",
    "/math/incerto/incerto-distribution-concepts/",
}
HOST = urlsplit(ORIGIN).netloc


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.assets = []
        self.home_links = []
        self.ids = set()
        self.math_count = 0
        self.display_math_count = 0
        self.math_errors = 0
        self.canonical = []
        self.refresh = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        self.math_count += "katex" in classes
        self.display_math_count += "katex-display" in classes
        self.math_errors += "katex-error" in classes
        for name in ("href", "src"):
            value = attrs.get(name)
            if value:
                self.urls.append(value)
                if tag != "a":
                    self.assets.append(value)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        if "myst-home-link" in classes:
            self.home_links.append(attrs.get("href"))
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href"))
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.refresh.append(attrs.get("content"))


def toc_files(entries):
    for entry in entries:
        if "file" in entry:
            yield entry["file"]
        yield from toc_files(entry.get("children", []))


def main():
    failures = []
    documents = {}
    old_routes = redirects()
    page_count = 0
    math_count = 0
    shared_css = (REPO / "assets/styles/math.css").read_text().strip()

    def document(path):
        if path not in documents:
            source = path.read_text(encoding="utf-8")
            parser = Links()
            parser.feed(source)
            documents[path] = (source, parser)
        return documents[path]

    def target_for(path):
        target = HTML / path.removeprefix(f"{BASE}/")
        return target if target.is_file() else target / "index.html"

    def check_links(url, parser, site=None):
        styles = set()
        for link in parser.urls:
            parsed = urlsplit(urljoin(f"https://{HOST}{url}", link))
            if parsed.scheme not in {"http", "https"} or parsed.netloc != HOST:
                continue
            path = unquote(parsed.path)
            # Package docs are a separate artifact; never require or copy them.
            if path.startswith("/normix/") and urlsplit(link).netloc:
                continue
            if path == BASE:
                path += "/"
            if not path.startswith(f"{BASE}/"):
                failures.append(f"{url}: URL outside {BASE}/: {link}")
                continue
            if site and link in parser.assets and not path.startswith(f"{site.base}/"):
                failures.append(f"{url}: asset outside its subsite: {link}")
            if site and path.rstrip("/") + "/" in old_routes:
                failures.append(f"{url}: link still uses an old flat route: {link}")
            target = target_for(path)
            if not target.is_file():
                failures.append(f"{url}: missing local target: {link}")
                continue
            if parsed.fragment and target.suffix == ".html":
                _, target_parser = document(target)
                if unquote(parsed.fragment) not in target_parser.ids:
                    failures.append(f"{url}: missing local fragment: {link}")
            if target.suffix == ".css":
                styles.add(target)
        return styles

    for site in SITES:
        directory = HTML / site.key
        sitemap = directory / "sitemap.xml"
        if not sitemap.is_file():
            failures.append(f"{site.base}/: missing sitemap")
        else:
            locations = {node.text for node in ET.parse(sitemap).iter(
                "{http://www.sitemaps.org/schemas/sitemap/0.9}loc"
            )}
            expected_urls = {
                ORIGIN + included.url(page)
                for included in (SITES if not site.key else (site,))
                for page in included.pages
            }
            if locations != expected_urls:
                failures.append(f"{site.base}/: incorrect public sitemap URLs")
        robots = directory / "robots.txt"
        if (not robots.is_file()
                or f"Sitemap: {ORIGIN}{site.base}/sitemap.xml" not in robots.read_text()):
            failures.append(f"{site.base}/: incorrect sitemap discovery URL")
        search = directory / "myst.search.json"
        if not search.is_file():
            failures.append(f"{site.base}/: missing search data")
        else:
            search_paths = {
                urlsplit(record["url"]).path.rstrip("/")
                for record in json.loads(search.read_text()).get("records", [])
            }
            expected_paths = {"", *(f"/{page.stem}" for page in site.notes)}
            if search_paths != expected_paths:
                failures.append(f"{site.base}/: search data does not match this track")
        config_path = directory / "config.json"
        if not config_path.is_file():
            failures.append(f"missing subsite config: {config_path}")
        else:
            config = json.loads(config_path.read_text())
            projects = config.get("projects", [])
            if (config.get("title") != site.title
                    or config.get("options", {}).get("logo_text") != site.title
                    or len(projects) != 1 or projects[0].get("title") != site.title):
                failures.append(f"{site.base}/: incorrect independent branding/project")
            else:
                expected = {str(page.relative_to(REPO)) for page in site.pages}
                if set(toc_files(projects[0].get("toc", []))) != expected:
                    failures.append(f"{site.base}/: TOC does not match this track's sources")
                if projects[0].get("index") != "index":
                    failures.append(f"{site.base}/: hub is not the project index")
                slugs = {page["slug"] for page in projects[0].get("pages", []) if "slug" in page}
                if slugs != {page.stem for page in site.notes}:
                    failures.append(f"{site.base}/: exported pages differ from this track")
            if not site.key:
                for option in ("hide_toc", "hide_outline", "hide_footer_links", "hide_search"):
                    if config.get("options", {}).get(option) is not True:
                        failures.append(f"landing: {option} must be enabled")

        for page in site.pages:
            page_count += 1
            url = site.url(page)
            target = target_for(url)
            if not target.is_file():
                failures.append(f"missing page: {url}")
                continue
            source, parser = document(target)
            if parser.refresh:
                failures.append(f"{url}: content was overwritten by a redirect")
            if url not in NO_MATH:
                math_count += 1
                if not parser.math_count or not parser.display_math_count:
                    failures.append(f"missing rendered display math: {url}")
            if parser.math_errors:
                failures.append(f"KaTeX rendering error: {url}")
            if parser.home_links != [f"{site.base}/"]:
                failures.append(f"{url}: logo does not link to its subsite home")
            styles = check_links(url, parser, site)
            if not any(shared_css in style.read_text() for style in styles):
                failures.append(f"{url}: shared math.css not found in linked styles")
            if "incerto-wiki/blob/" in source or "Technical-Incerto-Python" in source:
                failures.append(f"{url}: stale private source link")
            if not site.key:
                for track in SITES[1:]:
                    if not any(urlsplit(link).path == f"{track.base}/" for link in parser.urls):
                        failures.append(f"landing: missing link to {track.title}")
            elif (directory / site.old_hub / "index.html").exists():
                failures.append(f"{site.base}/: duplicate nested hub route")

    for old, new in old_routes.items():
        target = target_for(old)
        if not target.is_file():
            failures.append(f"missing redirect: {old}")
            continue
        source, parser = document(target)
        if parser.canonical != [f"https://{HOST}{new}"] or parser.refresh != [f"0; url={new}"]:
            failures.append(f"{old}: incorrect redirect or canonical destination")
        if new not in parser.urls:
            failures.append(f"{old}: missing visible destination link")
        if "window.location.search + window.location.hash" not in source:
            failures.append(f"{old}: redirect does not preserve queries/fragments")
        check_links(old, parser)

    if failures:
        raise SystemExit("\n".join(sorted(set(failures))))
    print(
        f"Checked {page_count} pages across four sites, {len(old_routes)} redirects, "
        f"{math_count} pages with display math, independent branding/TOCs, "
        "nested /math prefixes, local links/assets/fragments, sitemaps, and shared math.css."
    )


if __name__ == "__main__":
    main()
