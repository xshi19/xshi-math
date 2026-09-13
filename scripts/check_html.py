"""Check the six-page foundation artifact built with BASE_URL=/math.

Run after ``npm run build``. This checks files and URLs, not browser behavior.
"""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "_build" / "html"
BASE = "/math"
PAGES = (
    "index.html",
    "incerto/index.html",
    "incerto-counting-exceedances/index.html",
    "information-geometry/index.html",
    "normix-theory/index.html",
    "normix-conditioning-a-mixture/index.html",
)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.urls.append(value)


def main() -> None:
    failures = []
    styles = set()
    for name in PAGES:
        page = ROOT / name
        if not page.is_file():
            failures.append(f"missing page: {name}")
            continue
        source = page.read_text()
        if "-exceedances/" in name or "-mixture/" in name:
            if "katex" not in source:
                failures.append(f"missing rendered sample math: {name}")
        parser = Links()
        parser.feed(source)
        for url in parser.urls:
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc or url.startswith("#"):
                continue
            path = unquote(urlsplit(urljoin(f"{BASE}/{name}", url)).path)
            if path == BASE:
                path += "/"
            if not path.startswith(f"{BASE}/"):
                failures.append(f"{name}: URL outside {BASE}/: {url}")
                continue
            target = ROOT / path.removeprefix(f"{BASE}/")
            if not target.is_file() and not (target / "index.html").is_file():
                failures.append(f"{name}: missing local target: {url}")
            if target.suffix == ".css" and target.is_file():
                styles.add(target)
        if "incerto-wiki/blob/" in source or "Technical-Incerto-Python" in source:
            failures.append(f"{name}: stale private source link")
    if not any("text-underline-offset" in path.read_text() for path in styles):
        failures.append("shared math.css not found among linked stylesheets")
    if failures:
        raise SystemExit("\n".join(sorted(set(failures))))
    print(f"Checked {len(PAGES)} pages, local links/assets, /math prefix, and sample math.")


if __name__ == "__main__":
    main()
