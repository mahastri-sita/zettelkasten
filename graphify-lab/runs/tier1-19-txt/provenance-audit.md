# Graphify Tier 1 Provenance Audit

## Automated Checks

- All `1,407` node IDs are unique and match the lowercase `[a-z0-9_]+` rule.
- All `1,417` reviewed edge endpoints resolve globally; no fiktif node was added.
- All `30` hyperedge node lists resolve globally.
- `2,246` reviewed node/edge line-locator fields were checked against the corresponding TXT line counts; `0` ranges exceed their source file.
- Edge confidence distribution: `1,372` `EXTRACTED`, `43` `INFERRED`, and `2` `AMBIGUOUS`.
- The two `AMBIGUOUS` edges remain at confidence `0.2` and were not promoted.
- No duplicate node IDs, node conflicts, exact duplicate edges, self-loops, or missing endpoints were found.

## Manual Chunk 09 Samples

- Z03 `core_regions`/`peripheral_regions` and `authority_dependency_relations` are supported by lines `694-713`, which define core and periphery, dependency, and authority-dependency integration.
- T09 `agglomeration_shadow`, `locational_orphaning`, `spatial_separation`, and `gravitational_region` are supported by lines `570-598`, which describe neighboring locations being shut out and dynamically orphaned.
- M14 `strategic_work` is supported by lines `179-188`, which define strategic work as integrative, direction-changing, and transformative governance work.
- M16 `urban_governance_transformation` is supported by lines `98-113`, which connect governance transformation to actors, networks, discourses, practices, and cultural assumptions.
- M14 `strategic_frame` is supported by lines `658-728`; M16 `framing_ideas` is supported by lines `328-342`. Their cross-source similarity remains `INFERRED`, not evidence.
- The Z03 `core_regions` to T09 `lock_in` and T09 `agglomeration_shadow` to Z03 `dominance_effect` links are also `INFERRED`, with source-side locators retained.

## Structural Limitations

- Undirected construction collapses `10` same-endpoint edge pairs (`1,417` reviewed raw edges to `1,407` graph edges). Directed construction preserves all `1,417` reviewed edges.
- Only `2/19` source-owned node sets are contained in one undirected connected component. All `19/19` sources have at least one connected node, so these statuses must not be conflated.
- Community labels are provisional navigation labels, not user-approved substantive interpretations; the base proposal and reviewed proposal are preserved in `community-label-proposals.json` and `community-label-proposals-reviewed.json`.
- Fragment token metadata remains `0/0`; actual agent usage was not available in the returned results.
- TXT extraction preserves line-based locators, but original PDF page/figure structure and OCR/layout fidelity are not uniform across the corpus.
- The fixed ten-chunk partition and host-agent runtime are part of this run's provenance; earlier agent retries included transient `Connection reset by server` failures before final fragments were accepted.
- The four reviewed edges are not silently folded into raw fragments: they are reproducible through `manual-edge-patch.json` and `apply_manual_edge_patch.py`, producing `.graphify_extract_reviewed.json` from the base extraction.
