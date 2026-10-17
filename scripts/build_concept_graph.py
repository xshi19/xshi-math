"""Build the Incerto concept graph from the flat xshi-math notes."""

from __future__ import annotations

import argparse
import json
import html
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import networkx as nx
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "assets" / "data" / "concept-graph.json"
ALLOWED_TYPES = {
    "definition",
    "distribution",
    "theorem",
    "method",
    "empirical-example",
}
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+?\.md(?:#[^)]+)?)\)")


@dataclass(frozen=True)
class ConceptPage:
    """Parsed concept-page metadata."""

    concept_id: str
    concept_type: str
    title: str
    source_path: Path
    depends_on: tuple[str, ...]
    related: tuple[str, ...]
    tags: tuple[str, ...]
    status: str
    body: str
    proof_depends_on: tuple[str, ...] = ()
    special_case_of: tuple[str, ...] = ()
    applications: tuple[str, ...] = ()

    @property
    def relative_path(self) -> str:
        return "content/" + self.source_path.name

    @property
    def site_url(self) -> str:
        return "/math/incerto/" + self.source_path.stem + "/"


def _split_frontmatter(text: str, path: Path) -> tuple[dict[str, Any], str]:
    if not text.startswith("---"):
        return {}, text

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            frontmatter_text = "\n".join(lines[1:index])
            body = "\n".join(lines[index + 1 :])
            frontmatter = yaml.safe_load(frontmatter_text) or {}
            if not isinstance(frontmatter, dict):
                raise ValueError(f"{path}: frontmatter must be a mapping")
            return frontmatter, body

    raise ValueError(f"{path}: opening frontmatter fence has no closing fence")


def _first_heading(body: str, path: Path) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError(f"{path}: concept page has no level-1 heading")


def _as_string_tuple(value: object, *, field_name: str, path: Path) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        raise ValueError(f"{path}: concept.{field_name} must be a list")
    result: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise ValueError(f"{path}: concept.{field_name} entries must be strings")
        result.append(item)
    return tuple(result)


def load_concepts(root: Path = ROOT) -> list[ConceptPage]:
    """Load concept metadata from Markdown frontmatter."""

    concept_root = root / "content"
    concepts: list[ConceptPage] = []
    for path in sorted(concept_root.glob("incerto-*.md")):
        text = path.read_text(encoding="utf-8")
        frontmatter, body = _split_frontmatter(text, path)
        options = frontmatter.get("options", {})
        if options is None:
            options = {}
        if not isinstance(options, dict):
            raise ValueError(f"{path}: options frontmatter must be a mapping")
        concept = options.get("concept", frontmatter.get("concept"))
        if concept is None:
            continue  # Hubs and reading guides are not concept nodes.
        if not isinstance(concept, dict):
            raise ValueError(f"{path}: concept metadata must be a mapping")

        concept_id = concept.get("id")
        concept_type = concept.get("type")
        if not isinstance(concept_id, str) or not concept_id:
            raise ValueError(f"{path}: concept.id must be a non-empty string")
        if not ID_PATTERN.fullmatch(concept_id):
            raise ValueError(f"{path}: concept.id must be a lowercase slug")
        if not isinstance(concept_type, str) or concept_type not in ALLOWED_TYPES:
            allowed = ", ".join(sorted(ALLOWED_TYPES))
            raise ValueError(f"{path}: concept.type must be one of {allowed}")

        concepts.append(
            ConceptPage(
                concept_id=concept_id,
                concept_type=concept_type,
                title=frontmatter.get("title") or _first_heading(body, path),
                source_path=path,
                depends_on=_as_string_tuple(
                    concept.get("prerequisites", concept.get("depends_on", [])),
                    field_name="prerequisites", path=path
                ),
                related=_as_string_tuple(
                    concept.get("related", []), field_name="related", path=path
                ),
                tags=_as_string_tuple(
                    concept.get("tags", []), field_name="tags", path=path
                ),
                status=str(concept.get("status", "active")),
                body=body,
                proof_depends_on=_as_string_tuple(concept.get("proof_depends_on", []), field_name="proof_depends_on", path=path),
                special_case_of=_as_string_tuple(concept.get("special_case_of", []), field_name="special_case_of", path=path),
                applications=_as_string_tuple(concept.get("applications", []), field_name="applications", path=path),
            )
        )
    return concepts


def _validate_ids(concepts: list[ConceptPage]) -> dict[str, ConceptPage]:
    by_id: dict[str, ConceptPage] = {}
    for concept in concepts:
        existing = by_id.get(concept.concept_id)
        if existing is not None:
            raise ValueError(
                "duplicate concept.id "
                f"{concept.concept_id!r}: {existing.relative_path} and "
                f"{concept.relative_path}"
            )
        if concept.concept_id == "notation":
            raise ValueError(f"{concept.relative_path}: notation is not a concept node")
        by_id[concept.concept_id] = concept
    return by_id


def _dependency_graph(concepts: list[ConceptPage]) -> nx.DiGraph:
    by_id = _validate_ids(concepts)
    graph = nx.DiGraph()
    for concept in concepts:
        graph.add_node(concept.concept_id)
    for concept in concepts:
        for dependency in concept.depends_on:
            if dependency == "notation":
                raise ValueError(
                    f"{concept.relative_path}: notation must not be a graph dependency"
                )
            if dependency not in by_id:
                raise ValueError(
                    f"{concept.relative_path}: unknown dependency {dependency!r}"
                )
            graph.add_edge(dependency, concept.concept_id)

    if not nx.is_directed_acyclic_graph(graph):
        cycle = " -> ".join(edge[0] for edge in nx.find_cycle(graph))
        raise ValueError(f"concept dependency graph has a cycle: {cycle}")
    return graph


def _resolved_concept_links(concept: ConceptPage, path_to_id: dict[Path, str]) -> set[str]:
    links: set[str] = set()
    for match in MARKDOWN_LINK_PATTERN.finditer(concept.body):
        raw_target = match.group(1).split("#", 1)[0]
        if "://" in raw_target or raw_target.startswith("#"):
            continue
        target_path = (concept.source_path.parent / raw_target).resolve()
        target_id = path_to_id.get(target_path)
        if target_id is not None and target_id != concept.concept_id:
            links.add(target_id)
    return links


def _edge_id(kind: str, source: str, target: str) -> str:
    return f"{kind}:{source}->{target}"


def _build_edges(concepts: list[ConceptPage], graph: nx.DiGraph) -> list[dict[str, str]]:
    by_id = {concept.concept_id: concept for concept in concepts}
    dependency_pairs = set(graph.edges())
    edge_keys: set[tuple[str, str, str]] = set()
    edges: list[dict[str, str]] = []

    def add_edge(kind: str, source: str, target: str) -> None:
        if kind in {"reference", "related"}:
            source, target = sorted((source, target))
        key = (kind, source, target)
        if source == target or key in edge_keys:
            return
        if source not in by_id or target not in by_id:
            raise ValueError(f"unknown {kind} edge endpoint: {source!r}, {target!r}")
        edge_keys.add(key)
        edges.append(
            {
                "id": _edge_id(kind, source, target),
                "source": source,
                "target": target,
                "kind": kind,
            }
        )

    for source, target in sorted(dependency_pairs):
        add_edge("dependency", source, target)

    path_to_id = {
        concept.source_path.resolve(): concept.concept_id for concept in concepts
    }
    for concept in concepts:
        for target_id in _resolved_concept_links(concept, path_to_id):
            if (
                (target_id, concept.concept_id) in dependency_pairs
                or (concept.concept_id, target_id) in dependency_pairs
            ):
                continue
            add_edge("reference", concept.concept_id, target_id)
        for target_id in concept.related:
            add_edge("related", concept.concept_id, target_id)
        for source_id in concept.proof_depends_on:
            add_edge("proof-dependency", source_id, concept.concept_id)
        for target_id in concept.special_case_of:
            add_edge("generalization", concept.concept_id, target_id)
        for target_id in concept.applications:
            add_edge("application", concept.concept_id, target_id)

    return sorted(edges, key=lambda edge: (edge["kind"], edge["source"], edge["target"]))


def _dag_layout(concepts: list[ConceptPage], graph: nx.DiGraph) -> dict[str, Any]:
    by_id = {concept.concept_id: concept for concept in concepts}
    generations = [sorted(group, key=lambda item: by_id[item].title) for group in nx.topological_generations(graph)]
    max_generation = max((len(group) for group in generations), default=1)
    width = max(920, 180 + 150 * max(len(generations) - 1, 1))
    height = max(620, 100 + 90 * max_generation)
    positions: dict[str, dict[str, float]] = {}
    for level, group in enumerate(generations):
        x = 90 + level * 150
        y_step = height / (len(group) + 1)
        for row, concept_id in enumerate(group, start=1):
            positions[concept_id] = {"x": float(x), "y": float(row * y_step)}
    return {"width": width, "height": height, "nodes": positions}


def _scale_layout(raw_positions: dict[str, tuple[float, float]]) -> dict[str, dict[str, float]]:
    if not raw_positions:
        return {}
    xs = [position[0] for position in raw_positions.values()]
    ys = [position[1] for position in raw_positions.values()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    span_x = max(max_x - min_x, 1e-9)
    span_y = max(max_y - min_y, 1e-9)
    positions: dict[str, dict[str, float]] = {}
    for concept_id, (x, y) in raw_positions.items():
        positions[concept_id] = {
            "x": float(90 + ((x - min_x) / span_x) * 740),
            "y": float(90 + ((y - min_y) / span_y) * 500),
        }
    return positions


def _knowledge_layout(concepts: list[ConceptPage], edges: list[dict[str, str]]) -> dict[str, Any]:
    graph = nx.Graph()
    graph.add_nodes_from(concept.concept_id for concept in concepts)
    for edge in edges:
        graph.add_edge(edge["source"], edge["target"])
    raw_positions = nx.spring_layout(graph, seed=20260531, k=1.15, iterations=200)
    return {
        "width": 920,
        "height": 680,
        "nodes": _scale_layout(raw_positions),
    }


def build_graph_data(root: Path = ROOT) -> dict[str, Any]:
    """Build serializable graph data for the static visualization."""

    concepts = load_concepts(root)
    graph = _dependency_graph(concepts)
    edges = _build_edges(concepts, graph)
    nodes = [
        {
            "id": concept.concept_id,
            "title": concept.title,
            "type": concept.concept_type,
            "path": concept.relative_path,
            "url": concept.site_url,
            "tags": list(concept.tags),
            "status": concept.status,
        }
        for concept in sorted(concepts, key=lambda item: item.title)
    ]
    type_counts: dict[str, int] = {}
    for concept in concepts:
        type_counts[concept.concept_type] = type_counts.get(concept.concept_type, 0) + 1

    return {
        "schema_version": 2,
        "nodes": nodes,
        "edges": edges,
        "layouts": {
            "dag": _dag_layout(concepts, graph),
            "knowledge": _knowledge_layout(concepts, edges),
        },
        "topological_order": list(nx.topological_sort(graph)),
        "stats": {
            "node_count": len(nodes),
            "dependency_edge_count": graph.number_of_edges(),
            "reference_edge_count": sum(edge["kind"] == "reference" for edge in edges),
            "related_edge_count": sum(edge["kind"] == "related" for edge in edges),
            "type_counts": dict(sorted(type_counts.items())),
        },
    }


def write_graph_data(output_path: Path = DEFAULT_OUTPUT, root: Path = ROOT) -> dict[str, Any]:
    """Write graph JSON and the static concept list."""

    data = build_graph_data(root)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    # A static list remains usable without JavaScript or a successful fetch.
    list_path = output_path.parent.parent / "graphs" / "concept-list.html"
    list_path.parent.mkdir(parents=True, exist_ok=True)
    links = "\n".join(f'<li><a target="_parent" href="{html.escape(n["url"])}">'
                      f'{html.escape(n["title"])}</a></li>' for n in data["nodes"])
    list_path.write_text('<!doctype html><html lang="en"><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>Concept list</title><link rel="stylesheet" href="../css/concept-graph.css">'
        '<main class="concept-list"><h1>All concepts</h1><ul>' + links + '</ul></main></html>\n')
    return data


def stage_graph_assets(destination: Path, root: Path = ROOT) -> dict[str, Any]:
    """Copy graph UI and regenerate data inside one Incerto HTML export."""
    import shutil
    for relative in ("graphs/concept-graph.html", "js/concept-graph.js", "css/concept-graph.css"):
        target = destination / "assets" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / "assets" / relative, target)
    return write_graph_data(destination / "assets/data/concept-graph.json", root)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="path for the generated concept graph JSON",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate and print a summary without writing the JSON file",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data = build_graph_data(ROOT) if args.check else write_graph_data(args.output, ROOT)
    stats = data["stats"]
    print(
        "concept graph: "
        f"{stats['node_count']} nodes, "
        f"{stats['dependency_edge_count']} dependency edges, "
        f"{stats['reference_edge_count']} reference edges"
    )
    if args.check:
        print("concept graph validation passed")
    else:
        print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
