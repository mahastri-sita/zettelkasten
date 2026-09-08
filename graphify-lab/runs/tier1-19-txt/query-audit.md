# Graphify Tier 1 Query Audit

**Input:** `graphify-out/.graphify_extract_reviewed.json` via `manual-edge-patch.json`

**Graph outputs:**

- Undirected: `graphify-out/graph.json` (`1407` nodes, `1407` edges)
- Directed: `graphify-out/graph-directed.json` (`1407` nodes, `1417` edges)

## Query Smoke Tests

All queries were run with `graphify query ... --budget 700` against the undirected graph. The reported nodes included `source_file` and `source_location` provenance.

| Query | Nodes found | Displayed | Provenance sample |
|---|---:|---:|---|
| `borrowed size and agglomeration shadow` | 46 | 11 | T08, T01, T09, Z01 |
| `polycentricity and network externalities` | 27 | 10 | P02, Z01 |
| `accessibility and land use transport` | 62 | 9 | M07 |
| `polarized development core periphery` | 103 | 12 | Z03, T08, T07, T16, T17, T09 |
| `increasing returns and path dependence` | 5 | 5 | T09, T07, T01 |
| `strategic spatial planning and multilevel governance` | 45 | 12 | M13, M16, M14 |

Several queries were truncated by the `700`-token budget; truncation is reported by the CLI and is not treated as missing extraction.

## Path and Explain

- `graphify path "Core Regions" "Spatial Strategy Making"` found no directed path.
- `graphify path "Core Regions" "Spatial Strategy Making" --undirected` also found no path. This pair remains disconnected in the current graph.
- `graphify path "Core Regions" "Lock-In" --undirected` found a one-hop `semantically_similar_to` path marked `INFERRED`. The raw edge provenance is Z03, `lines 694-713`.
- `graphify path "Core-periphery model" "Agglomeration" --undirected` found a one-hop `conceptually_related_to` path marked `EXTRACTED`, crossing Community 36 to Community 26. Its T08 locator is `Chapter 5, §§5.3-5.6, pp. 65-77`.
- `graphify path "Compensatory Payments" "Distribution Problem" --undirected` found a one-hop `conceptually_related_to` path marked `EXTRACTED`; locator T01, `lines 267-280`.
- `graphify path "The Strategy of Economic Development" "Low-Level Equilibrium Trap" --undirected` found a one-hop `references` path marked `EXTRACTED`; locator T16, `Chapter 2, lines 1270-1287`.
- `graphify path "Elasticity of Substitution" "Economies of Scale" --undirected` found a one-hop `conceptually_related_to` path marked `EXTRACTED`; locator T07, `lines 387-391`.
- `graphify path "Comprehensive Planning" "Traditional Land-Use Planning" --undirected` found a one-hop `conceptually_related_to` path marked `EXTRACTED`; locator M13, `lines 172-187`.
- `graphify explain "Agglomeration Shadow"` resolved the node in T09 at `lines 563-598`, degree `4`, with three `EXTRACTED` rationale edges and one `INFERRED` similarity edge to `Dominance Effect`.

## Caveat

Community labels are provisional navigation labels derived from graph membership and supporting node labels. They are not user-approved substantive theory categories; the base and reviewed proposal bases are in `community-label-proposals.json` and `community-label-proposals-reviewed.json`.
