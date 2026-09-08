# Low-Connectivity Evidence Review

## Scope and method

This is a read-only audit of the six orphan records listed in `connectivity-review.md`. I read the cited passages in `graphify-lab/full-corpus-txt/` and checked the node and link records in `graphify-lab/runs/tier1-19-txt/graphify-out/graph.json` and `.graphify_extract.json`.

The degree facts below use the ordinary binary `links` in `graph.json`, which is the definition used by the structural audit (`degree == 0`). Hyperedge membership is reported separately. No raw fragment, source TXT, graph JSON, `Todo.md`, or other artifact was modified.

## Summary

| Code | Node | Binary degree | Hyperedge membership | Classification |
|---|---|---:|---:|---|
| T01 | `Compensatory Payments` | 0 | 0 | likely-missing-explicit-edge |
| M07 | `Connectivity` | 0 | 1 | isolated-but-plausible; relation already represented by hyperedge |
| T16 | `Low-Level Equilibrium Trap` | 0 | 0 | likely-missing-explicit-edge |
| T07 | `Elasticity of Substitution` | 0 | 0 | likely-missing-explicit-edge |
| M13 | `Comprehensive Planning` | 0 | 0 | likely-missing-explicit-edge |
| T03 | `Heterogeneity of Workers and Firms` | 0 | 0 | ambiguous |

## Findings

### T01 - Compensatory Payments

Node ID: `graphify_lab_full_corpus_txt_t01_alonso_1973_urban_zero_population_growth_no_doi_compensatory_payments`

Evidence: The passage states that the distribution problem could be solved if residents of the excluding locality made "compensatory payments (a form of rent)" to the people they would exclude (TXT lines 274-276). This is an explicit relation between the orphan and the existing `Distribution Problem` node, not merely a shared topic.

Graph evidence: The node record is present in `graph.json` at lines 6190-6201 and has no binary incident link or hyperedge. `Distribution Problem` already receives `rationale_for` links from `Local Population Policies` and `Real City`, but none from `Compensatory Payments`.

Classification: **likely-missing-explicit-edge**.

Proposed edge, not written:

```json
{
  "source": "graphify_lab_full_corpus_txt_t01_alonso_1973_urban_zero_population_growth_no_doi_compensatory_payments",
  "target": "graphify_lab_full_corpus_txt_t01_alonso_1973_urban_zero_population_growth_no_doi_distribution_problem",
  "relation": "conceptually_related_to",
  "confidence": "EXTRACTED",
  "confidence_score": 1.0,
  "source_file": "/Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/graphify-lab/full-corpus-txt/T01-alonso-1973-urban-zero-population-growth-no-doi.txt",
  "source_location": "lines 267-280"
}
```

Recommendation: Queue this single edge for a future evidence-backed extraction update. Do not add a separate link to `Social Equity` solely because that node shares part of the locator; the cited passage explicitly names the distribution problem, not that graph abstraction.

### M07 - Connectivity

Node ID: `graphify_lab_full_corpus_txt_m07_levine_grengs_merlin_2019_from_mobility_to_accessibility_transforming_urban_transportation_and_land_use_planning_no_doi_connectivity`

Evidence: The passage says that mobility is one means to achieve accessibility, while proximity and connectivity are other possible pathways; it then defines connectivity as delivery of goods and services to a location, virtually or physically (TXT lines 476-479).

Graph evidence: The node record at `graph.json` lines 5329-5340 has zero binary incident links. It is, however, already included in the extracted hyperedge `m07_accessibility_logic`, together with `Accessibility`, `Mobility`, `Proximity`, `Derived-Demand Framework`, and `Potential for Interaction` (`graph.json` lines 140-154). Thus the ordinary degree-zero result is a binary-projection artifact, not evidence that the passage was wholly disconnected.

Classification: **isolated-but-plausible** in the binary graph, with the explicit relation already represented by a source-local hyperedge.

Recommendation: Retain the hyperedge and do not add a duplicate binary edge in this audit. A direct `Connectivity` to `Accessibility` edge would be a representation choice for a binary projection, not a necessary evidence repair. No additional edge is proposed.

### T16 - Low-Level Equilibrium Trap

Node ID: `graphify_lab_full_corpus_txt_t16_hirschman_1958_the_strategy_of_economic_development_no_doi_low_level_equilibrium_trap`

Evidence: Hirschman describes models in which an initial income increase produces a population increase that absorbs the income gain, and identifies the conditions under which a country is caught in or escapes a "low-level equilibrium trap" (TXT lines 1273-1276). The surrounding passage is explicitly part of *The Strategy of Economic Development*.

Graph evidence: The node record at `graph.json` lines 7420-7431 has no binary incident link or hyperedge. The existing book node already has citation links to Simon, Nelson, and Leibenstein at the cited footnote range, but it has no document-to-concept link to the extracted `Low-Level Equilibrium Trap` node.

Classification: **likely-missing-explicit-edge**.

Proposed edge, not written:

```json
{
  "source": "graphify_lab_full_corpus_txt_t16_hirschman_1958_the_strategy_of_economic_development_no_doi_the_strategy_of_economic_development",
  "target": "graphify_lab_full_corpus_txt_t16_hirschman_1958_the_strategy_of_economic_development_no_doi_low_level_equilibrium_trap",
  "relation": "references",
  "confidence": "EXTRACTED",
  "confidence_score": 1.0,
  "source_file": "/Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/graphify-lab/full-corpus-txt/T16-hirschman-1958-the-strategy-of-economic-development-no-doi.txt",
  "source_location": "Chapter 2, lines 1270-1287"
}
```

Recommendation: Add only the document-to-concept reference in a later extraction revision. The existing citations to the named authors should not be duplicated or relabeled based on this passage.

### T07 - Elasticity of Substitution

Node ID: `graphify_lab_full_corpus_txt_t07_krugman_1991_increasing_returns_and_economic_geography_10_1086_261763_elasticity_of_substitution`

Evidence: Krugman identifies the elasticity of substitution among products as a parameter determining equilibrium (TXT lines 297-300). He then states that the parameter can be interpreted as an inverse index of equilibrium economies of scale (TXT lines 387-391). The latter is an explicit relation to the existing `Economies of Scale` node.

Graph evidence: The node record at `graph.json` lines 7095-7106 has no binary incident link or hyperedge. `Economies of Scale` exists and is already linked to `Increasing Returns to Scale` and `Manufacturing`, but not to this parameter node.

Classification: **likely-missing-explicit-edge**.

Proposed edge, not written:

```json
{
  "source": "graphify_lab_full_corpus_txt_t07_krugman_1991_increasing_returns_and_economic_geography_10_1086_261763_elasticity_of_substitution",
  "target": "graphify_lab_full_corpus_txt_t07_krugman_1991_increasing_returns_and_economic_geography_10_1086_261763_economies_of_scale",
  "relation": "conceptually_related_to",
  "confidence": "EXTRACTED",
  "confidence_score": 1.0,
  "source_file": "/Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/graphify-lab/full-corpus-txt/T07-krugman-1991-increasing-returns-and-economic-geography-10.1086-261763.txt",
  "source_location": "lines 387-391"
}
```

Recommendation: Queue this one relation. Do not add separate links to convergence or divergence from the cited ranges alone; the passage identifies a parameter of equilibrium, but does not assign a direction without relying on the surrounding model discussion.

### M13 - Comprehensive Planning

Node ID: `graphify_lab_full_corpus_txt_m13_albrechts_2004_strategic_spatial_planning_reexamined_10_1068_b3065_comprehensive_planning`

Evidence: The passage describes strategic spatial planning as having evolved toward comprehensive planning at different administrative levels (TXT lines 59-62). It later characterizes EU land-use plans as mainly comprehensive and discusses their limits (TXT lines 172-187). This explicitly maps the orphan to the existing `Traditional Land-Use Planning` node, whose source record covers the same land-use-planning discussion.

Graph evidence: The node record at `graph.json` lines 5791-5802 has no binary incident link or hyperedge. `Traditional Land-Use Planning` is already linked to `Legal Certainty and Rigidity` and `Land-Use Regulation`, but not to `Comprehensive Planning`.

Classification: **likely-missing-explicit-edge**.

Proposed edge, not written:

```json
{
  "source": "graphify_lab_full_corpus_txt_m13_albrechts_2004_strategic_spatial_planning_reexamined_10_1068_b3065_comprehensive_planning",
  "target": "graphify_lab_full_corpus_txt_m13_albrechts_2004_strategic_spatial_planning_reexamined_10_1068_b3065_traditional_land_use_planning",
  "relation": "conceptually_related_to",
  "confidence": "EXTRACTED",
  "confidence_score": 1.0,
  "source_file": "/Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/graphify-lab/full-corpus-txt/M13-albrechts-2004-strategic-spatial-planning-reexamined-10.1068-b3065.txt",
  "source_location": "lines 172-187"
}
```

Recommendation: Queue this relation. Do not infer a stronger causal edge from comprehensive planning to rigidity, limited resources, or stakeholder exclusion; the passage presents these as distinct features and criticisms of land-use plans.

### T03 - Heterogeneity of Workers and Firms

Node ID: `graphify_lab_full_corpus_txt_t03_duranton_puga_2004_micro_foundations_of_urban_agglomeration_economies_10_1016_s1574_0080_04_80005_1_heterogeneity_of_workers_and_firms`

Evidence: The passage says that worker and firm heterogeneity is at the root of "most if not all" mechanisms in the chapter, then asks whether the relevant heterogeneity is within an industry or across sectors. It also says that existing models treat heterogeneity thinly and that empirical work faces measurement difficulties (TXT lines 2309-2323).

Graph evidence: The node record at `graph.json` lines 7021-7033 has no binary incident link or hyperedge. The graph contains separate `Sharing Mechanisms`, `Matching Mechanisms`, and `Learning Mechanisms` nodes under the `Sharing, Matching, and Learning Taxonomy`, but the cited passage does not identify one unique target or specify which mechanisms receive the relation.

Classification: **ambiguous**.

Recommendation: Leave the node unlinked. A link to the taxonomy, or separate links to all three mechanism nodes, would be a plausible synthesis of the chapter but would exceed what this passage explicitly and uniquely supports. No edge is proposed.

## Overall recommendation

The six binary orphans were not a uniform extraction-error class. Four explicitly supported relations were applied through `manual-edge-patch.json`; M07's existing hyperedge was retained without duplication, and T03 remains ambiguous. Fragment count was not used as a reason to add any further edge.

## Post-Patch Resolution

The reviewed graph gives each of the four patched nodes one binary incident edge. M07 remains binary-degree zero but is covered by the existing `m07_accessibility_logic` hyperedge; T03 remains binary-degree zero and unlinked because the passage does not identify a unique target. Raw fragments and the base `.graphify_extract.json` remain unchanged.
