> Historical record from `incerto-wiki` at `9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`.
> Source: `content/releases/releases.md`. Statements and commands below describe that repository
> at the recorded date, not current xshi-math verification. MIT; copyright (c) 2023 xshi19.

# Releases

Incerto Wiki uses versioned releases for stable chapter cycles.  A release is
not a promise that the whole wiki is complete; it is a named, reproducible
state of a coherent slice of the project.

## Current Releases

| Version | Scope | Status |
| ------- | ----- | ------ |
| v0.1.0 (`v0-1-0.md` in the source tree) | Chapter 3 seed: first concept cycle, notation, Python package, reading guide | Release ledger established |

## Release Gates

A stable chapter-cycle release should pass these checks before a Git tag is
cut:

- `python -m pytest`
- `jupyter-book build --html --execute`
- `python scripts/provenance_footer.py --check`
- browser smoke checks on representative concept, reading-guide, and table
  pages
- print smoke checks on representative pages when CSS or page structure
  changed

## Version Scheme

Use semantic-looking `vMAJOR.MINOR.PATCH` tags, with conservative meanings:

- `MAJOR`: incompatible site or package structure;
- `MINOR`: a stable chapter cycle or substantial concept-family release;
- `PATCH`: corrections that do not change the cycle scope.

The package version in `pyproject.toml`, the release page, and the Git tag
should agree when a release is published.

The tag workflow at `.github/workflows/release.yml` enforces that agreement for
`v*.*.*` tags and uploads the built static site as a release artifact.

## Release Notes

Each release note should record:

- scope and exclusions;
- verification commands;
- important source or data caveats;
- known gaps that remain intentionally open.
