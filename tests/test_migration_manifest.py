"""Account for every tracked Incerto source path without a source checkout."""
import csv
from fnmatch import fnmatchcase
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "9717c9cf83aee18b47f423a14bce2f0d14bb8bcb"


def test_pinned_source_manifest_is_complete_and_unambiguous():
    paths = (ROOT / "docs/records/incerto-wiki/source-paths.txt").read_text().splitlines()
    assert len(paths) == len(set(paths)) == 252
    rows = [r for r in csv.DictReader((ROOT / "docs/plan/migration-manifest.csv").open())
            if r["source_repository"] == "xshi19/incerto-wiki"]
    assert len({r["source_id"] for r in rows}) == len(rows)
    for path in paths:
        matches = [r for r in rows if fnmatchcase(path, r["source_path"])]
        assert len(matches) == 1, (path, matches)
        row = matches[0]
        assert row["source_revision"] == PIN
        assert row["disposition"] in {"imported", "exclude", "stay"}
        assert row["reason"] and row["target_path"] and row["license"]
        assert (ROOT / row["target_path"]).exists(), row
    assert all(any(fnmatchcase(p, r["source_path"]) for p in paths) for r in rows)
    stubs = [r for r in rows if r["disposition"] == "stay"]
    assert {Path(r["source_path"]).stem for r in stubs} == {"ch5", "ch6", "ch7"}
    assert all("Planned" in r["reason"] for r in stubs)
