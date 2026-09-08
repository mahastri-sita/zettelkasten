# Connectivity Review: Tier 1 (19 TXT sources)

> This document records the baseline connectivity audit before the evidence-backed manual patch. Current reviewed counts are in `graphify-out/structural-audit.json`, `coverage.json`, and `structural-audit.md`; the patch is reproducible from `manual-edge-patch.json`.

## Scope and basis

This review audits only these five artifacts:

- `graphify-out/graph.json`
- `graphify-out/graph-directed.json`
- `graphify-out/structural-audit.json`
- `coverage.json`
- `provenance-audit.md`

The primary connectivity result is the simple undirected graph in `graph.json`. Its ordinary links are used for degree and connected-component calculations. Hyperedges are reported separately and are not treated as ordinary graph links in the structural counts. The directed graph is used only to explain the 10 same-endpoint pairs that are preserved directionally but collapsed by the undirected simple-graph projection.

The audit definitions are:

- orphan: degree `== 0`
- weak: degree `<= 1`, therefore including all 54 orphans
- super-hub: degree `>= 10` in this run
- source component count: the number of distinct undirected components containing at least one node owned by that source

These are graph-degree classifications, not semantic judgments. A node can be isolated from ordinary links without being unsupported by its source, and hyperedge membership is reported separately from ordinary-link degree.

The `source_file` values in the representative tables reproduce the node metadata in `graph.json`. The source codes and full staging paths are recorded in `coverage.json`.

## Bottom line

The observed graph is fragmented, but the artifacts do not show a general structural corruption. The dominant pattern is a sparse, source-local extraction:

- `1,407` nodes form `163` undirected connected components.
- `54` components are single-node components, exactly matching the `54` orphan nodes.
- `754` nodes are weak by the audit definition: `54` degree-zero nodes plus `700` degree-one nodes.
- `1,384` of the `1,403` retained undirected links are within a single source. Only `19` retained links are cross-source, spanning `10` source pairs.
- All `19/19` source sets have at least one connected node, but only `2/19` source-owned node sets are entirely contained in one component: `M08` and `T14`.

Thus, disconnectedness is not evidence by itself that a node is wrong or that a relation is missing. It mainly records that the extracted relation graph contains many source-internal subgraphs and few cross-source bridges. A disconnected node should be classified as an extraction problem only after checking its source evidence at the recorded locator.

## Global counts

| Metric | Count | Reading |
|---|---:|---|
| Nodes | 1,407 | All node IDs are unique. |
| Raw/directed links | 1,413 | Preserved in `graph-directed.json`. |
| Retained undirected links | 1,403 | Ten same-endpoint pairs collapse in the simple undirected projection. |
| Hyperedges | 30 | Their node lists resolve, but they are counted separately from ordinary links. |
| Undirected components | 163 | Includes 54 singleton components. |
| Orphans | 54 | Degree `== 0`; each is its own component. |
| Weak nodes | 754 | Degree `<= 1`; 700 are degree-one nodes. |
| Super-hubs | 17 | Degree `>= 10`; this is an operational threshold, not a claim of corpus-wide importance. |
| Sources with at least one connected node | 19/19 | This is the weaker `graph_connected` condition. |
| Sources wholly within one component | 2/19 | `M08` and `T14` only. |

The component-size pattern is also sparse: 54 components have size 1; 61 have size 2-4; 26 have size 5-10; 3 have size 11-20; 14 have size 21-50; and 5 have at least 51 nodes. The five largest component sizes are `57`, `69`, `74`, `138`, and `214`. This is consistent with many small source-local relation clusters rather than one integrated corpus graph.

## Exact per-source counts

`Raw edges` is the source-owned `edge_count` in `coverage.json` and sums to the 1,413 directed/raw links. `Undirected links` is counted from `graph.json` and sums to 1,403. The difference is the projection collapse, not an assertion that source evidence was invalid.

| Code | Nodes | Raw edges | Undirected links | Hyperedges | Source components | All in one? | Orphans | Degree 1 | Weak total | Hubs |
|---|---:|---:|---:|---:|---:|:---:|---:|---:|---:|---:|
| T01 | 47 | 23 | 23 | 0 | 24 | No | 17 | 19 | 36 | 0 |
| T03 | 40 | 47 | 44 | 1 | 4 | No | 3 | 16 | 19 | 1 |
| T05 | 129 | 130 | 129 | 3 | 10 | No | 1 | 79 | 80 | 1 |
| T06 | 26 | 29 | 29 | 1 | 3 | No | 2 | 9 | 11 | 0 |
| T07 | 49 | 39 | 39 | 1 | 11 | No | 5 | 29 | 34 | 1 |
| T08 | 79 | 96 | 95 | 3 | 5 | No | 3 | 21 | 24 | 2 |
| T09 | 45 | 40 | 40 | 1 | 8 | No | 0 | 27 | 27 | 0 |
| T14 | 74 | 104 | 104 | 3 | 1 | Yes | 0 | 23 | 23 | 3 |
| T16 | 155 | 137 | 136 | 3 | 23 | No | 1 | 95 | 96 | 1 |
| T17 | 26 | 28 | 28 | 1 | 3 | No | 1 | 11 | 12 | 0 |
| M07 | 171 | 182 | 179 | 3 | 19 | No | 12 | 69 | 81 | 3 |
| M08 | 57 | 87 | 86 | 3 | 1 | Yes | 0 | 8 | 8 | 1 |
| M13 | 56 | 50 | 50 | 1 | 7 | No | 3 | 30 | 33 | 0 |
| M14 | 53 | 46 | 46 | 0 | 11 | No | 1 | 32 | 33 | 0 |
| M16 | 67 | 56 | 56 | 1 | 12 | No | 0 | 42 | 42 | 0 |
| M17 | 62 | 58 | 58 | 1 | 4 | No | 1 | 42 | 43 | 1 |
| Z01 | 140 | 131 | 131 | 3 | 13 | No | 2 | 76 | 78 | 0 |
| Z03 | 81 | 79 | 79 | 1 | 10 | No | 0 | 44 | 44 | 2 |
| P02 | 50 | 51 | 51 | 0 | 4 | No | 2 | 28 | 30 | 1 |
| **Total** | **1,407** | **1,413** | **1,403** | **30** |  |  | **54** | **700** | **754** | **17** |

The source component counts are not additive to 163 because one cross-source component can be counted once for every source represented in it. The two complete source sets are `M08` (57 nodes, 1 component) and `T14` (74 nodes, 1 component). The most internally fragmented source sets by this measure are `T01` (24 components), `T16` (23), and `M07` (19).

## Why 163 components is plausible here

The link ownership is strongly source-local. The 19 cross-source undirected links are distributed as follows, using source codes:

| Source pair | Retained links |
|---|---:|
| T03-T06 | 5 |
| T03-T17 | 3 |
| M14-M16 | 2 |
| T06-T17 | 2 |
| T09-Z03 | 2 |
| M13-M14 | 1 |
| T05-T09 | 1 |
| T09-T17 | 1 |
| T16-Z03 | 1 |
| T17-Z03 | 1 |

Most source pairs have no extracted bridge at all. This means a large number of components is an expected consequence of the current extraction boundary: concepts are usually related only to other concepts extracted from the same TXT source. The two source sets that are wholly connected are not evidence that every other source should also be one component; they simply have enough extracted internal links to form one component under this graph construction.

The 17 super-hubs are similarly local rather than a single corpus-wide backbone. Their source distribution is:

- `M07`: 3 (`Accessibility`, degree 21; `Public-Transport Accessibility`, 13; `Derived-Demand Framework`, 12)
- `M08`: 1 (`The New Science of Cities`, 17)
- `M17`: 1 (`Multi-Level (Territorial) Governance: Three Criticisms`, 23)
- `P02`: 1 (`Polycentric Urban Regions and the Quest for Synergy: Is a Network of Cities More than the Sum of the Parts?`, 14)
- `T03`: 1 (`Micro-foundations of Urban Agglomeration Economies`, 13)
- `T05`: 1 (`Economic Theory and Under-Developed Regions`, 35)
- `T07`: 1 (`Increasing Returns and Economic Geography`, 13)
- `T08`: 2 (`Agglomeration`, 12; `The Spatial Economy: Cities, Regions, and International Trade`, 10)
- `T14`: 3 (`Central Places in Southern Germany`, 15; `Central-Place Types`, 12; `Range of Central Goods`, 10)
- `T16`: 1 (`The Strategy of Economic Development`, 25)
- `Z03`: 2 (`Core Regions`, 13; `Innovation`, 10)

The remaining eight sources have no node at the degree-10 threshold. A high degree here means that the extracted node is a local connector under the current relation set; it does not establish that the node is substantively central to the literature.

## Extraction and provenance assessment

### Checks that passed

The provenance audit reports:

- all 1,407 node IDs are unique and satisfy the ID rule;
- all 1,413 raw edge endpoints resolve globally;
- all 30 hyperedge node lists resolve;
- 2,242 node/edge locator fields were checked, with zero ranges beyond the corresponding TXT file;
- no duplicate node IDs, node conflicts, exact duplicate edges, self-loops, or missing endpoints were found.

These checks do not show a graph serialization failure, dangling relation, or fabricated endpoint. They also do not prove that every possible source-supported relation was extracted.

### Issues that affect interpretation

- The raw edge confidence distribution is `1,368 EXTRACTED`, `43 INFERRED`, and `2 AMBIGUOUS`. The two ambiguous edges remain at confidence `0.2` and were not promoted.
- Of the 19 retained cross-source links, 6 are `EXTRACTED` and 13 are `INFERRED`. Cross-source integration should therefore be reviewed separately from ordinary source-local connectivity.
- The undirected simple graph collapses 10 same-endpoint pairs, reducing 1,413 raw/directed links to 1,403 retained links. These pairs include distinct relation labels or distinct source locations in several cases. This is a representation/projection issue, not automatically an extraction error. Use `graph-directed.json` when relation multiplicity or direction matters.
- `coverage.json` records unavailable agent token metadata (`0` in the fragment fields). This limits run-cost and extraction-effort auditing but does not explain the component structure.
- The provenance audit retains a local-path anomaly for `T03` and manifest provenance anomalies for `Z01` and `Z03`. These should be resolved before comparing future runs, but the artifacts provide no basis for treating those sources' disconnected nodes as invalid.
- Community labels are now provisional navigation labels backed by `community-label-proposals.json`; they are not user-approved substantive categories. The provenance audit also notes uneven preservation of original PDF page, figure, and OCR/layout structure. These are interpretive limitations, not demonstrated causes of the 163 components.

The directed audit also reports 163 components and preserves all 1,413 links, while its degree-based weak count is 750 and its hub count is 18. The requested headline values are the undirected values because undirected degree is the basis for the 54, 754, and 17 figures in `structural-audit.json`.

## Representative low-connectivity nodes

The examples below are not an error list. They show what the degree classifications look like while preserving the graph's recorded provenance. An orphan can be a valid standalone extraction; a degree-one node can be correctly linked only once. The per-source table above is the exhaustive count summary.

### Orphans (degree 0)

| Node label | Code | `source_file` | `source_location` |
|---|---|---|---|
| `Connectivity` | M07 | `M07-levine-grengs-merlin-2019-from-mobility-to-accessibility-transforming-urban-transportation-and-land-use-planning-no-doi.txt` | `Introduction, lines 476-479` |
| `Comprehensive Planning` | M13 | `M13-albrechts-2004-strategic-spatial-planning-reexamined-10.1068-b3065.txt` | `lines 59-82, 172-187` |
| `Network Cities` | P02 | `P02-meijers-2005-polycentric-urban-regions-and-the-quest-for-synergy-is-a-network-of-cities-more-than-the-sum-of-the-parts-10.1080-00420980500060384.txt` | `lines 97-123, 131-160` |
| `Compensatory Payments` | T01 | `T01-alonso-1973-urban-zero-population-growth-no-doi.txt` | `lines 267-280` |
| `Heterogeneity of Workers and Firms` | T03 | `T03-duranton-puga-2004-micro-foundations-of-urban-agglomeration-economies-10.1016-S1574-0080-04-80005-1.txt` | `Section 5; lines 2309-2323` |
| `Henry George Theorem` | T06 | `T06-duranton-puga-2005-from-sectoral-to-functional-urban-specialisation-10.1016-j.jue.2004.12.002.txt` | `Section 3; lines 889-911` |
| `Elasticity of Substitution` | T07 | `T07-krugman-1991-increasing-returns-and-economic-geography-10.1086-261763.txt` | `lines 282-300, 387-391, 575-578` |
| `City-size distribution` | T08 | `T08-fujita-krugman-venables-1999-the-spatial-economy-cities-regions-and-international-trade-no-doi.txt` | `Chapter 12, §§12.1-12.4, pp. 215-225` |
| `Low-Level Equilibrium Trap` | T16 | `T16-hirschman-1958-the-strategy-of-economic-development-no-doi.txt` | `Chapter 2, lines 1270-1287` |
| `Backyard production` | Z01 | `Z01-o'sullivan-1996-urban-eonomics.txt` | `lines 1571-1611` |

Sources with zero orphan nodes in this audit are `M08`, `M16`, `T09`, `T14`, and `Z03`. Zero orphans does not mean those source sets are wholly connected; for example, `M16` touches 12 components and `Z03` touches 10.

### Weak non-orphans (degree 1)

| Node label | Code | `source_file` | `source_location` |
|---|---|---|---|
| `413 East Huron` | M07 | `M07-levine-grengs-merlin-2019-from-mobility-to-accessibility-transforming-urban-transportation-and-land-use-planning-no-doi.txt` | `Chapter 3, lines 2583-2588` |
| `Bipartite interest-control graph` | M08 | `M08-batty-2013-the-new-science-of-cities-no-doi.txt` | `Chapter 12, pp. 368-369; Chapter 13, pp. 414-415` |
| `Accountability` | M13 | `M13-albrechts-2004-strategic-spatial-planning-reexamined-10.1068-b3065.txt` | `lines 44-56, 436-481` |
| `Agency Field` | M14 | `M14-healey-2009-in-search-of-the-strategic-in-spatial-strategy-making-10.1080-14649350903417191.txt` | `lines 482-493` |
| `Agency Power` | M16 | `M16-healey-2006-transforming-governance-challenges-of-institutional-adaptation-and-a-new-politics-of-space-10.1080-09654310500420792.txt` | `lines 334-342` |
| `Agnew 1994, The Territorial Trap` | M17 | `M17-faludi-2012-multi-level-territorial-governance-three-criticisms-10.1080-14649357.2012.677578.txt` | `lines 164-169, 493-498, 728-730` |
| `Amsterdam` | P02 | `P02-meijers-2005-polycentric-urban-regions-and-the-quest-for-synergy-is-a-network-of-cities-more-than-the-sum-of-the-parts-10.1080-00420980500060384.txt` | `lines 446-448, 731-780` |
| `Borrowed Size` | T01 | `T01-alonso-1973-urban-zero-population-growth-no-doi.txt` | `lines 756-808` |
| `Agglomeration Mitigates Hold-up` | T03 | `T03-duranton-puga-2004-micro-foundations-of-urban-agglomeration-economies-10.1016-S1574-0080-04-80005-1.txt` | `Section 3.3; lines 1629-1745` |
| `Absence of a World State` | T05 | `T05-myrdal-1957-economic-theory-and-under-developed-regions-no-doi.txt` | `Chapter 5, pp. 63-65` |
| `Agricultural Periphery` | T07 | `T07-krugman-1991-increasing-returns-and-economic-geography-10.1086-261763.txt` | `lines 39-46, 160-173` |
| `Arthur (1994), Increasing Returns and Path Dependence in the Economy` | T08 | `T08-fujita-krugman-venables-1999-the-spatial-economy-cities-regions-and-international-trade-no-doi.txt` | `References, p. 351` |
| `Agglomeration Benefits` | T09 | `T09-arthur-1990-silicon-valley-locational-clusters-when-do-increasing-returns-imply-monopoly-10.1016-0165-4896-90-90064-E.txt` | `lines 134-149` |
| `Augsburg` | T14 | `T14-christaller-1966-central-places-in-southern-germany-no-doi.txt` | `lines 4351-4384; 4537-4569` |
| `Abortive Development` | T16 | `T16-hirschman-1958-the-strategy-of-economic-development-no-doi.txt` | `Chapter 2, lines 1254-1313` |
| `Active and Passive Economic Sets` | T17 | `T17-perroux-1955-note-sur-la-notion-de-pole-de-croissance-10.3406-ecoap.1955.2522.txt` | `Growth of poles and national economies; lines 695-704` |
| `Agricultural surplus` | Z01 | `Z01-o'sullivan-1996-urban-eonomics.txt` | `lines 1040-1060` |
| `Borrowing and Imitation` | Z03 | `Z03-friedmann-1967-a-generalized-theory-of-polarized-development.txt` | `lines 323-327` |

## Bounded follow-up recommendations

1. Spot-check the representative orphans and degree-one nodes at their recorded `source_location`, prioritizing `T01`, `M07`, `T16`, `T07`, `M13`, and `T03`, which have the largest orphan or weak counts. Add a relation only when the source passage explicitly supports it. Do not add relations merely to reduce the component count.
2. Review the 19 cross-source links separately, especially the 13 `INFERRED` links and the 2 globally `AMBIGUOUS` links. Keep their confidence status unless source evidence justifies a change.
3. Use `graph-directed.json` for relation-level review where direction, relation labels, or multiple source locations matter. Treat the 10 undirected endpoint collapses as a projection difference unless a source-level review shows an actual extraction duplication.
4. Normalize the recorded provenance anomalies for `T03`, `Z01`, and `Z03`, and restore agent token metadata in a future run if reproducibility of extraction effort is needed. These actions improve auditability; they are not justified as a way to force connectivity.
5. Re-run the same read-only audit after any evidence-backed extraction change and compare nodes, raw links, retained links, component counts, locators, and confidence classes. A lower component count is not, by itself, a success criterion.

## Conclusion

The artifacts support a diagnosis of sparse and mostly source-local relation coverage, with a small number of explicit or inferred cross-source bridges. They do not support a diagnosis that the 54 orphans, 754 weak nodes, or the 163 components are collectively extraction errors. Endpoint, ID, locator, and hyperedge-resolution checks passed; the remaining uncertainty is whether particular source passages warrant additional relations, which requires targeted source review rather than graph-shape assumptions.

## Reviewed Follow-Up

The six representative orphan nodes were checked against their exact source passages. Four explicit relations were added through `manual-edge-patch.json`: T01 `Compensatory Payments` to `Distribution Problem`; T16 document to `Low-Level Equilibrium Trap`; T07 `Elasticity of Substitution` to `Economies of Scale`; and M13 `Comprehensive Planning` to `Traditional Land-Use Planning`. M07 `Connectivity` remains represented by its existing hyperedge, and T03 `Heterogeneity of Workers and Firms` remains ambiguous.

The reviewed graph now has `1,407` nodes, `1,407` undirected edges, `1,417` directed edges, `159` undirected components, and `50` binary orphans. Raw fragments remain unchanged; `.graphify_extract_reviewed.json` is the reproducible reviewed extraction layer.
