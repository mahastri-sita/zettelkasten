# Graphify Tier 1 Coverage

Coverage separates `source_available`, `fragment_written`, `extraction_nonempty`, and `graph_connected`.
The reviewed graph applies the four evidence-backed edges in `manual-edge-patch.json`; raw fragments remain unchanged.

| Code | Chunk | Words | Nodes | Edges | Hyperedges | Located nodes/edges | Graph connected | One component | Patch edges | Warnings |
|---|---:|---:|---:|---:|---:|---:|---|---|---:|---|
| `T01` | 10 | 8295 | 47 | 24 | 0 | 47/24 | True | False (23) | 1 | actual agent token usage unavailable; fragment token fields remain 0; one evidence-backed edge added by manual review patch |
| `T03` | 08 | 27137 | 40 | 47 | 1 | 40/47 | True | False (4) | 0 | actual agent token usage unavailable; fragment token fields remain 0; manifest provenance: local source path is source/working-paper/ |
| `T05` | 07 | 62535 | 129 | 130 | 3 | 129/130 | True | False (10) | 0 | actual agent token usage unavailable; fragment token fields remain 0 |
| `T06` | 08 | 13816 | 26 | 29 | 1 | 26/29 | True | False (3) | 0 | actual agent token usage unavailable; fragment token fields remain 0 |
| `T07` | 10 | 6487 | 49 | 40 | 1 | 49/40 | True | False (10) | 1 | actual agent token usage unavailable; fragment token fields remain 0; one evidence-backed edge added by manual review patch |
| `T08` | 03 | 110652 | 79 | 96 | 3 | 79/96 | True | False (5) | 0 | actual agent token usage unavailable; fragment token fields remain 0 |
| `T09` | 09 | 7200 | 45 | 40 | 1 | 45/40 | True | False (8) | 0 | actual agent token usage unavailable; fragment token fields remain 0 |
| `T14` | 04 | 97141 | 74 | 104 | 3 | 74/104 | True | True | 0 | actual agent token usage unavailable; fragment token fields remain 0 |
| `T16` | 05 | 84814 | 155 | 138 | 3 | 155/138 | True | False (22) | 1 | actual agent token usage unavailable; fragment token fields remain 0; one evidence-backed edge added by manual review patch |
| `T17` | 08 | 5794 | 26 | 28 | 1 | 26/28 | True | False (3) | 0 | actual agent token usage unavailable; fragment token fields remain 0 |
| `M07` | 06 | 84062 | 171 | 182 | 3 | 171/182 | True | False (19) | 0 | actual agent token usage unavailable; fragment token fields remain 0 |
| `M08` | 02 | 186649 | 57 | 87 | 3 | 57/87 | True | True | 0 | actual agent token usage unavailable; fragment token fields remain 0 |
| `M13` | 10 | 8481 | 56 | 51 | 1 | 56/51 | True | False (6) | 1 | actual agent token usage unavailable; fragment token fields remain 0; one evidence-backed edge added by manual review patch |
| `M14` | 09 | 12450 | 53 | 46 | 0 | 53/46 | True | False (11) | 0 | actual agent token usage unavailable; fragment token fields remain 0 |
| `M16` | 09 | 12252 | 67 | 56 | 1 | 67/56 | True | False (12) | 0 | actual agent token usage unavailable; fragment token fields remain 0 |
| `M17` | 10 | 8955 | 62 | 58 | 1 | 62/58 | True | False (4) | 0 | actual agent token usage unavailable; fragment token fields remain 0 |
| `Z01` | 01 | 195344 | 140 | 131 | 3 | 140/131 | True | False (13) | 0 | actual agent token usage unavailable; fragment token fields remain 0; manifest provenance anomaly retained verbatim |
| `Z03` | 09 | 14718 | 81 | 79 | 1 | 81/79 | True | False (10) | 0 | actual agent token usage unavailable; fragment token fields remain 0; manifest provenance anomaly retained verbatim |
| `P02` | 10 | 9542 | 50 | 51 | 0 | 50/51 | True | False (4) | 0 | actual agent token usage unavailable; fragment token fields remain 0 |

All 19 sources are available, have a written fragment, and have non-empty extraction.

`graph_connected` means at least one source-owned node participates in an undirected edge. `One component` reports whether all nodes owned by that source share one component.
