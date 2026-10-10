"""Canonical subsite paths shared by assembly, redirects, and HTML checks."""

from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parents[1]
BASE = "/math"
ORIGIN = "https://xshi19.github.io"
HTML = REPO / "_build" / "html"
LEGACY_BASE = "/incerto-wiki"
LEGACY_HTML = REPO / "_build" / "legacy" / "incerto-wiki"
URL_MAP = REPO / "docs" / "plan" / "url-map.csv"


def normalize_page_path(path):
    """Normalize directory URLs and literal index.html aliases safely."""
    if (not path.startswith("/") or "\\" in path
            or any(part in {".", ".."} for part in unquote(path).split("/"))
            or "//" in path or any(ord(char) < 32 for char in unquote(path))):
        raise ValueError(f"Invalid page path: {path!r}")
    if path.endswith("/index.html"):
        path = path.removesuffix("index.html")
    return path if path.endswith(".html") else path.rstrip("/") + "/"


def page_file(root, path, base):
    """Resolve a public page path inside one artifact, never a sibling tree."""
    path = normalize_page_path(path)
    if not path.startswith(base + "/"):
        raise ValueError(f"Page outside {base}/: {path}")
    relative = path.removeprefix(base + "/")
    return root / relative if relative.endswith(".html") else root / relative / "index.html"


@dataclass(frozen=True)
class Site:
    key: str
    title: str
    prefix: str
    old_hub: str

    @property
    def base(self):
        return f"{BASE}/{self.key}" if self.key else BASE

    @property
    def index(self):
        return REPO / "content" / self.key / "index.md"

    @property
    def notes(self):
        return sorted((REPO / "content").glob(f"{self.prefix}*.md")) if self.key else []

    @property
    def shared_pages(self):
        """Landing-owned pages shared by every track (single canon, no copies)."""
        if self.key:
            return []
        return [REPO / "content" / "notation.md"]

    @property
    def pages(self):
        return [self.index, *self.shared_pages, *self.notes]

    def url(self, page):
        return f"{self.base}/" if page == self.index else f"{self.base}/{page.stem}/"


SITES = (
    Site("", "Mathematical notes", "", "index"),
    Site("incerto", "Incerto", "incerto-", "incerto"),
    Site("ig", "Information Geometry", "information-geometry-", "information-geometry"),
    Site("normix-theory", "Normix theory", "normix-", "normix-theory"),
)


def redirects():
    """Old flat URLs that moved; never overwrite a home with a self-redirect."""
    result = {}
    for site in SITES[1:]:
        if site.old_hub != site.key:
            result[f"{BASE}/{site.old_hub}/"] = f"{site.base}/"
        result.update({f"{BASE}/{page.stem}/": site.url(page) for page in site.notes})
    return result
