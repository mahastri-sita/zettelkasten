import json
import math
from collections import Counter, defaultdict
from pathlib import Path

import networkx as nx

from graphify.build import build_from_json
from graphify.diagnostics import diagnose_extraction


RUN = Path(__file__).parent
OUT = RUN / "graphify-out"
EXTRACTION = OUT / ".graphify_extract_reviewed.json"


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8")


def graph_audit(graph, directed):
    if directed:
        components = list(nx.weakly_connected_components(graph))
    else:
        components = list(nx.connected_components(graph))
    component_by_node = {
        node: index for index, component in enumerate(components) for node in component
    }
    degrees = dict(graph.degree())
    ordered = sorted(degrees.items(), key=lambda item: (-item[1], str(item[0])))
    threshold_index = max(0, math.ceil(len(degrees) * 0.95) - 1)
    sorted_degrees = sorted(degrees.values())
    threshold = max(10, sorted_degrees[threshold_index])

    duplicate_groups = defaultdict(list)
    for node, data in graph.nodes(data=True):
        duplicate_groups[str(data.get("label", node)).casefold()].append(
            {
                "id": node,
                "label": data.get("label", node),
                "source_file": data.get("source_file"),
            }
        )
    duplicate_groups = {
        label: entries
        for label, entries in duplicate_groups.items()
        if len(entries) > 1
    }

    return {
        "graph_file": "graph-directed.json" if directed else "graph.json",
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
        "connected_components": len(components),
        "orphan_definition": "degree == 0",
        "weak_definition": "degree <= 1",
        "super_hub_definition": "degree >= max(10, 95th-percentile degree threshold)",
        "orphan_count": sum(degree == 0 for degree in degrees.values()),
        "weak_count": sum(degree <= 1 for degree in degrees.values()),
        "super_hub_threshold": threshold,
        "super_hub_count": sum(degree >= threshold for degree in degrees.values()),
        "top_nodes": [
            {
                "id": node,
                "degree": degree,
                "label": graph.nodes[node].get("label", node),
            }
            for node, degree in ordered[:20]
        ],
        "duplicate_label_group_count": len(duplicate_groups),
        "duplicate_label_groups": dict(duplicate_groups),
        "citation_edge_count": sum(
            data.get("relation") == "cites" for _, _, data in graph.edges(data=True)
        ),
    }, component_by_node


def structural_markdown(audits):
    undirected = audits["undirected"]
    directed = audits["directed"]
    lines = [
        "# Reviewed Structural Audit",
        "",
        "This audit uses `.graphify_extract_reviewed.json` and the four-edge evidence patch.",
        "",
        "## Summary",
        "",
        "| Graph | Nodes | Edges | Components | Orphans | Weak | Super-hubs | Citation edges |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
        f"| Undirected | {undirected['nodes']} | {undirected['edges']} | {undirected['connected_components']} | {undirected['orphan_count']} | {undirected['weak_count']} | {undirected['super_hub_count']} | {undirected['citation_edge_count']} |",
        f"| Directed | {directed['nodes']} | {directed['edges']} | {directed['connected_components']} | {directed['orphan_count']} | {directed['weak_count']} | {directed['super_hub_count']} | {directed['citation_edge_count']} |",
        "",
        "Definitions: orphan = degree 0; weak = degree <= 1; super-hub threshold is the reported max(10, 95th-percentile threshold).",
        "",
        "## Top Nodes",
        "",
        "| Graph | Degree | Label | ID |",
        "|---|---:|---|---|",
    ]
    for graph_name, audit in (("Undirected", undirected), ("Directed", directed)):
        for node in audit["top_nodes"][:20]:
            lines.append(
                f"| {graph_name} | {node['degree']} | {node['label']} | `{node['id']}` |"
            )
    lines.extend(
        [
            "",
            "## Duplicate Labels",
            "",
            f"The reviewed graph contains {undirected['duplicate_label_group_count']} case-folded duplicate-label groups. These are retained when provenance differs.",
            "",
            "## Interpretation",
            "",
            "The four added edges remove four binary orphans and reduce the undirected component count by four. M07 remains represented through its existing hyperedge, while T03 remains intentionally unlinked because its candidate targets are ambiguous.",
            "",
        ]
    )
    return "\n".join(lines)


extraction = json.loads(EXTRACTION.read_text(encoding="utf-8"))
original_coverage = json.loads((RUN / "coverage.json").read_text(encoding="utf-8"))
patch = json.loads((RUN / "manual-edge-patch.json").read_text(encoding="utf-8"))
undirected = build_from_json(extraction, root=str(RUN), directed=False)
directed = build_from_json(extraction, root=str(RUN), directed=True)

write_json(
    OUT / "health.json",
    {
        "undirected": diagnose_extraction(extraction, directed=False, root=str(RUN)),
        "directed": diagnose_extraction(extraction, directed=True, root=str(RUN)),
    },
)

audits = {}
for name, graph, is_directed in (
    ("undirected", undirected, False),
    ("directed", directed, True),
):
    audits[name], _ = graph_audit(graph, is_directed)
write_json(OUT / "structural-audit.json", audits)
(RUN / "structural-audit.md").write_text(structural_markdown(audits), encoding="utf-8")

source_node_count = Counter(node.get("source_file") for node in extraction["nodes"])
source_edge_count = Counter(edge.get("source_file") for edge in extraction["edges"])
source_hyperedge_count = Counter(
    hyperedge.get("source_file") for hyperedge in extraction.get("hyperedges", [])
)
source_located_node_count = Counter(
    node.get("source_file")
    for node in extraction["nodes"]
    if node.get("source_location")
)
source_located_edge_count = Counter(
    edge.get("source_file")
    for edge in extraction["edges"]
    if edge.get("source_location")
)
source_patch_count = Counter(edge.get("source_file") for edge in patch["edges"])
components = list(nx.connected_components(undirected))
component_by_node = {
    node: index for index, component in enumerate(components) for node in component
}

rows = []
for original in original_coverage["rows"]:
    source_file = original["staging_file"]
    source_nodes = {
        node["id"]
        for node in extraction["nodes"]
        if node.get("source_file") == source_file
    }
    component_count = len({component_by_node[node] for node in source_nodes})
    row = dict(original)
    row.update(
        {
            "source_available": Path(source_file).is_file(),
            "extraction_nonempty": bool(source_nodes),
            "graph_connected": any(undirected.degree(node) > 0 for node in source_nodes),
            "all_source_nodes_in_one_component": component_count == 1,
            "source_component_count": component_count,
            "node_count": source_node_count[source_file],
            "edge_count": source_edge_count[source_file],
            "hyperedge_count": source_hyperedge_count[source_file],
            "located_node_count": source_located_node_count[source_file],
            "located_edge_count": source_located_edge_count[source_file],
            "reviewed_edge_patch_count": source_patch_count[source_file],
        }
    )
    if source_patch_count[source_file]:
        row["warnings"] = list(row.get("warnings", [])) + [
            "one evidence-backed edge added by manual review patch"
        ]
    rows.append(row)

coverage = dict(original_coverage)
coverage["rows"] = rows
coverage["reviewed_extraction"] = ".graphify_extract_reviewed.json"
coverage["manual_edge_patch"] = "manual-edge-patch.json"
write_json(RUN / "coverage.json", coverage)

coverage_lines = [
    "# Graphify Tier 1 Coverage",
    "",
    "Coverage separates `source_available`, `fragment_written`, `extraction_nonempty`, and `graph_connected`.",
    "The reviewed graph applies the four evidence-backed edges in `manual-edge-patch.json`; raw fragments remain unchanged.",
    "",
    "| Code | Chunk | Words | Nodes | Edges | Hyperedges | Located nodes/edges | Graph connected | One component | Patch edges | Warnings |",
    "|---|---:|---:|---:|---:|---:|---:|---|---|---:|---|",
]
for row in rows:
    one_component = "True" if row["all_source_nodes_in_one_component"] else f"False ({row['source_component_count']})"
    warnings = "; ".join(row.get("warnings", []))
    coverage_lines.append(
        f"| `{row['code']}` | {row['chunk']:02d} | {row['word_count']} | {row['node_count']} | {row['edge_count']} | {row['hyperedge_count']} | {row['located_node_count']}/{row['located_edge_count']} | {row['graph_connected']} | {one_component} | {row['reviewed_edge_patch_count']} | {warnings} |"
    )
coverage_lines.extend(
    [
        "",
        "All 19 sources are available, have a written fragment, and have non-empty extraction.",
        "",
        "`graph_connected` means at least one source-owned node participates in an undirected edge. `One component` reports whether all nodes owned by that source share one component.",
    ]
)
(RUN / "coverage.md").write_text("\n".join(coverage_lines) + "\n", encoding="utf-8")

print(
    f"Audited reviewed outputs: undirected={undirected.number_of_nodes()} nodes/"
    f"{undirected.number_of_edges()} edges; components={audits['undirected']['connected_components']}; "
    f"orphans={audits['undirected']['orphan_count']}"
)
