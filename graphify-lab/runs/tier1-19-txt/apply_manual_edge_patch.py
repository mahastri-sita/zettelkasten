import json
from pathlib import Path


RUN = Path(__file__).parent
GRAPHIFY_OUT = RUN / "graphify-out"
BASE = GRAPHIFY_OUT / ".graphify_extract.json"
PATCH = RUN / "manual-edge-patch.json"
OUTPUT = GRAPHIFY_OUT / ".graphify_extract_reviewed.json"


def edge_key(edge):
    return (
        edge["source"],
        edge["target"],
        edge["relation"],
        edge["source_file"],
        edge["source_location"],
    )


extraction = json.loads(BASE.read_text(encoding="utf-8"))
patch = json.loads(PATCH.read_text(encoding="utf-8"))
nodes = {node["id"]: node for node in extraction["nodes"]}
existing = {edge_key(edge) for edge in extraction["edges"]}

for edge in patch["edges"]:
    if edge["source"] not in nodes or edge["target"] not in nodes:
        raise SystemExit(f"missing endpoint: {edge['source']} -> {edge['target']}")
    if not Path(edge["source_file"]).is_file():
        raise SystemExit(f"missing provenance file: {edge['source_file']}")
    if edge["confidence"] != "EXTRACTED" or edge["confidence_score"] != 1.0:
        raise SystemExit("manual patch contains an invalid confidence value")
    key = edge_key(edge)
    if key in existing:
        raise SystemExit(f"patch edge already exists: {key}")
    existing.add(key)

reviewed = dict(extraction)
reviewed["edges"] = extraction["edges"] + patch["edges"]
reviewed["manual_edge_patch"] = patch["patch_id"]
OUTPUT.write_text(json.dumps(reviewed, indent=2, ensure_ascii=False), encoding="utf-8")
print(
    f"Applied {len(patch['edges'])} evidence-backed edges: "
    f"{len(extraction['edges'])} -> {len(reviewed['edges'])}"
)
