"""Canonical subsite paths shared by assembly, redirects, and HTML checks."""

from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BASE = "/math"
ORIGIN = "https://xshi19.github.io"
HTML = REPO / "_build" / "html"


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
    def pages(self):
        return [self.index, *self.notes]

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
