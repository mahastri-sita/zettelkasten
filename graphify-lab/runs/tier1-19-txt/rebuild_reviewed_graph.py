import json
from collections import defaultdict
from pathlib import Path

from graphify.analyze import god_nodes, suggest_questions, surprising_connections
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.export import to_json
from graphify.report import generate


RUN = Path(__file__).parent
OUT = RUN / "graphify-out"
EXTRACTION = OUT / ".graphify_extract_reviewed.json"
DETECTION = OUT / ".graphify_detect.json"
OLD_ANALYSIS = OUT / ".graphify_analysis.json"
OLD_LABELS = OUT / ".graphify_labels.json"
OLD_PROPOSALS = RUN / "community-label-proposals.json"


def node_label(graph, node_id):
    return graph.nodes[node_id].get("label", node_id)


def build_proposals(graph, communities, old_analysis, old_labels, old_proposals):
    old_members = {int(cid): set(nodes) for cid, nodes in old_analysis["communities"].items()}
    new_proposals = {}
    merged_labels = {
        frozenset({3, 192}): "Economic Development and Equilibrium",
        frozenset({17, 187}): "Economic Geography Model Parameters",
        frozenset({21, 165}): "Local Distribution and Compensation",
        frozenset({85, 158}): "Comprehensive and Traditional Planning",
    }

    for community_id, members_list in sorted(communities.items()):
        members = set(members_list)
        overlaps = {
            old_id: len(members & old_nodes)
            for old_id, old_nodes in old_members.items()
            if members & old_nodes
        }
        old_ids = frozenset(overlaps)
        if len(old_ids) > 1:
            label = merged_labels.get(old_ids)
            if label is None:
                raise SystemExit(f"unmapped community merge: {sorted(old_ids)}")
            confidence = "medium"
            basis_note = (
                "New graph community formed after four evidence-backed manual edges; "
                f"it merges prior provisional communities {sorted(old_ids)}."
            )
        else:
            old_id = max(overlaps, key=overlaps.get)
            prior = old_proposals["communities"][str(old_id)]
            label = old_labels[str(old_id)]
            confidence = prior["confidence"]
            basis_note = (
                f"Inherited from prior provisional community {old_id}; "
                "membership changed only through the reviewed edge patch."
            )

        internal = graph.subgraph(members).number_of_edges()
        external = sum(
            1
            for source, target in graph.edges()
            if (source in members) != (target in members)
        )
        supporting_nodes = [
            node_label(graph, node_id)
            for node_id in sorted(
                members,
                key=lambda node_id: (-graph.degree(node_id), node_label(graph, node_id)),
            )[:5]
        ]
        new_proposals[str(community_id)] = {
            "proposed_label": label,
            "confidence": confidence,
            "node_count": len(members),
            "supporting_nodes": supporting_nodes,
            "connectivity": {
                "internal_edges": internal,
                "external_edges": external,
                "connected_nodes": len(members),
            },
            "basis_note": basis_note,
            "inherited_from": sorted(old_ids),
        }

    return new_proposals


def analysis_for(graph, communities, labels, directed):
    cohesion = score_all(graph, communities)
    questions = suggest_questions(graph, communities, labels)
    return {
        "communities": {str(key): value for key, value in communities.items()},
        "cohesion": {str(key): value for key, value in cohesion.items()},
        "gods": god_nodes(graph),
        "surprises": surprising_connections(graph, communities),
        "questions": questions,
        "directed": directed,
    }


extraction = json.loads(EXTRACTION.read_text(encoding="utf-8"))
detection = json.loads(DETECTION.read_text(encoding="utf-8"))
old_analysis = json.loads(OLD_ANALYSIS.read_text(encoding="utf-8"))
old_labels = json.loads(OLD_LABELS.read_text(encoding="utf-8"))
old_proposals = json.loads(OLD_PROPOSALS.read_text(encoding="utf-8"))

undirected = build_from_json(extraction, root=str(RUN), directed=False)
directed = build_from_json(extraction, root=str(RUN), directed=True)
communities = cluster(undirected)
proposals = build_proposals(
    undirected, communities, old_analysis, old_labels, old_proposals
)
labels = {int(cid): proposal["proposed_label"] for cid, proposal in proposals.items()}
tokens = {
    "input": extraction.get("input_tokens", 0),
    "output": extraction.get("output_tokens", 0),
}

if not to_json(undirected, communities, str(OUT / "graph.json"), community_labels=labels):
    raise SystemExit("undirected graph export refused")
if not to_json(directed, communities, str(OUT / "graph-directed.json"), community_labels=labels):
    raise SystemExit("directed graph export refused")

undirected_analysis = analysis_for(undirected, communities, labels, directed=False)
directed_analysis = analysis_for(directed, communities, labels, directed=True)
(OUT / ".graphify_analysis.json").write_text(
    json.dumps(undirected_analysis, indent=2, ensure_ascii=False), encoding="utf-8"
)
(OUT / ".graphify_analysis_directed.json").write_text(
    json.dumps(directed_analysis, indent=2, ensure_ascii=False), encoding="utf-8"
)
(OUT / ".graphify_labels.json").write_text(
    json.dumps({str(key): value for key, value in labels.items()}, indent=2, ensure_ascii=False),
    encoding="utf-8",
)

reviewed_proposals = {
    "basis": (
        "Inherited from community-label-proposals.json after the four-edge manual evidence patch. "
        "Four merged communities receive new provisional navigation labels."
    ),
    "community_id_range": [0, len(communities) - 1],
    "communities": proposals,
    "manual_edge_patch": "manual-edge-patch.json",
}
(RUN / "community-label-proposals-reviewed.json").write_text(
    json.dumps(reviewed_proposals, indent=2, ensure_ascii=False), encoding="utf-8"
)

report = generate(
    undirected,
    communities,
    {int(key): value for key, value in undirected_analysis["cohesion"].items()},
    labels,
    undirected_analysis["gods"],
    undirected_analysis["surprises"],
    detection,
    tokens,
    str(RUN),
    suggested_questions=undirected_analysis["questions"],
)
report = (
    "# Graph Report - reviewed extraction\n\n"
    "This report uses `.graphify_extract_reviewed.json`, which applies the four "
    "source-supported edges listed in `manual-edge-patch.json`. Community names "
    "remain provisional navigation labels, not user-approved theoretical categories.\n\n"
    + report.split("\n", 1)[1]
)
(OUT / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")

print(
    f"Reviewed graph: {undirected.number_of_nodes()} nodes, "
    f"{undirected.number_of_edges()} undirected edges, "
    f"{directed.number_of_edges()} directed edges, "
    f"{len(communities)} communities"
)
