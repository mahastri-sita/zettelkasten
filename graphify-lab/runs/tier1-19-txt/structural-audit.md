# Reviewed Structural Audit

This audit uses `.graphify_extract_reviewed.json` and the four-edge evidence patch.

## Summary

| Graph | Nodes | Edges | Components | Orphans | Weak | Super-hubs | Citation edges |
|---|---:|---:|---:|---:|---:|---:|---:|
| Undirected | 1407 | 1407 | 159 | 50 | 754 | 17 | 146 |
| Directed | 1407 | 1417 | 159 | 50 | 750 | 18 | 146 |

Definitions: orphan = degree 0; weak = degree <= 1; super-hub threshold is the reported max(10, 95th-percentile threshold).

## Top Nodes

| Graph | Degree | Label | ID |
|---|---:|---|---|
| Undirected | 35 | Economic Theory and Under-Developed Regions | `t05_myrdal_1957_economic_theory_and_under_developed_regions_no_doi_economic_theory_and_under_developed_regions` |
| Undirected | 26 | The Strategy of Economic Development | `graphify_lab_full_corpus_txt_t16_hirschman_1958_the_strategy_of_economic_development_no_doi_the_strategy_of_economic_development` |
| Undirected | 23 | Multi-Level (Territorial) Governance: Three Criticisms | `graphify_lab_full_corpus_txt_m17_faludi_2012_multi_level_territorial_governance_three_criticisms_10_1080_14649357_2012_677578_multi_level_territorial_governance_three_criticisms` |
| Undirected | 21 | Accessibility | `graphify_lab_full_corpus_txt_m07_levine_grengs_merlin_2019_from_mobility_to_accessibility_transforming_urban_transportation_and_land_use_planning_no_doi_accessibility` |
| Undirected | 17 | The New Science of Cities | `graphify_lab_full_corpus_txt_m08_batty_2013_the_new_science_of_cities_no_doi_book` |
| Undirected | 15 | Central Places in Southern Germany | `graphify_lab_full_corpus_txt_t14_christaller_1966_central_places_in_southern_germany_no_doi_central_places_in_southern_germany` |
| Undirected | 14 | Polycentric Urban Regions and the Quest for Synergy: Is a Network of Cities More than the Sum of the Parts? | `graphify_lab_full_corpus_txt_p02_meijers_2005_polycentric_urban_regions_and_the_quest_for_synergy_is_a_network_of_cities_more_than_the_sum_of_the_parts_10_1080_00420980500060384_polycentric_urban_regions_and_the_quest_for_synergy_is_a_network_of_cities_more_than_the_sum_of_the_parts` |
| Undirected | 13 | Public-Transport Accessibility | `graphify_lab_full_corpus_txt_m07_levine_grengs_merlin_2019_from_mobility_to_accessibility_transforming_urban_transportation_and_land_use_planning_no_doi_public_transport_accessibility` |
| Undirected | 13 | Micro-foundations of Urban Agglomeration Economies | `graphify_lab_full_corpus_txt_t03_duranton_puga_2004_micro_foundations_of_urban_agglomeration_economies_10_1016_s1574_0080_04_80005_1_paper` |
| Undirected | 13 | Increasing Returns and Economic Geography | `graphify_lab_full_corpus_txt_t07_krugman_1991_increasing_returns_and_economic_geography_10_1086_261763_increasing_returns_and_economic_geography` |
| Undirected | 13 | Core Regions | `graphify_lab_full_corpus_txt_z03_friedmann_1967_a_generalized_theory_of_polarized_development_core_regions` |
| Undirected | 12 | Derived-Demand Framework | `graphify_lab_full_corpus_txt_m07_levine_grengs_merlin_2019_from_mobility_to_accessibility_transforming_urban_transportation_and_land_use_planning_no_doi_derived_demand_framework` |
| Undirected | 12 | Central-Place Types | `graphify_lab_full_corpus_txt_t14_christaller_1966_central_places_in_southern_germany_no_doi_central_place_types` |
| Undirected | 12 | Agglomeration | `t08_fujita_krugman_venables_1999_the_spatial_economy_cities_regions_and_international_trade_no_doi_agglomeration` |
| Undirected | 10 | Range of Central Goods | `graphify_lab_full_corpus_txt_t14_christaller_1966_central_places_in_southern_germany_no_doi_range_of_central_goods` |
| Undirected | 10 | Innovation | `graphify_lab_full_corpus_txt_z03_friedmann_1967_a_generalized_theory_of_polarized_development_innovation` |
| Undirected | 10 | The Spatial Economy: Cities, Regions, and International Trade | `t08_fujita_krugman_venables_1999_the_spatial_economy_cities_regions_and_international_trade_no_doi_the_spatial_economy` |
| Undirected | 9 | Land exchange model | `graphify_lab_full_corpus_txt_m08_batty_2013_the_new_science_of_cities_no_doi_land_exchange_model` |
| Undirected | 9 | Strategic (Spatial) Planning Reexamined | `graphify_lab_full_corpus_txt_m13_albrechts_2004_strategic_spatial_planning_reexamined_10_1068_b3065_strategic_spatial_planning_reexamined` |
| Undirected | 9 | From Sectoral to Functional Urban Specialisation | `graphify_lab_full_corpus_txt_t06_duranton_puga_2005_from_sectoral_to_functional_urban_specialisation_10_1016_j_jue_2004_12_002_paper` |
| Directed | 35 | Economic Theory and Under-Developed Regions | `t05_myrdal_1957_economic_theory_and_under_developed_regions_no_doi_economic_theory_and_under_developed_regions` |
| Directed | 26 | The Strategy of Economic Development | `graphify_lab_full_corpus_txt_t16_hirschman_1958_the_strategy_of_economic_development_no_doi_the_strategy_of_economic_development` |
| Directed | 23 | Multi-Level (Territorial) Governance: Three Criticisms | `graphify_lab_full_corpus_txt_m17_faludi_2012_multi_level_territorial_governance_three_criticisms_10_1080_14649357_2012_677578_multi_level_territorial_governance_three_criticisms` |
| Directed | 21 | Accessibility | `graphify_lab_full_corpus_txt_m07_levine_grengs_merlin_2019_from_mobility_to_accessibility_transforming_urban_transportation_and_land_use_planning_no_doi_accessibility` |
| Directed | 17 | The New Science of Cities | `graphify_lab_full_corpus_txt_m08_batty_2013_the_new_science_of_cities_no_doi_book` |
| Directed | 15 | Central Places in Southern Germany | `graphify_lab_full_corpus_txt_t14_christaller_1966_central_places_in_southern_germany_no_doi_central_places_in_southern_germany` |
| Directed | 14 | Polycentric Urban Regions and the Quest for Synergy: Is a Network of Cities More than the Sum of the Parts? | `graphify_lab_full_corpus_txt_p02_meijers_2005_polycentric_urban_regions_and_the_quest_for_synergy_is_a_network_of_cities_more_than_the_sum_of_the_parts_10_1080_00420980500060384_polycentric_urban_regions_and_the_quest_for_synergy_is_a_network_of_cities_more_than_the_sum_of_the_parts` |
| Directed | 13 | Public-Transport Accessibility | `graphify_lab_full_corpus_txt_m07_levine_grengs_merlin_2019_from_mobility_to_accessibility_transforming_urban_transportation_and_land_use_planning_no_doi_public_transport_accessibility` |
| Directed | 13 | Micro-foundations of Urban Agglomeration Economies | `graphify_lab_full_corpus_txt_t03_duranton_puga_2004_micro_foundations_of_urban_agglomeration_economies_10_1016_s1574_0080_04_80005_1_paper` |
| Directed | 13 | Increasing Returns and Economic Geography | `graphify_lab_full_corpus_txt_t07_krugman_1991_increasing_returns_and_economic_geography_10_1086_261763_increasing_returns_and_economic_geography` |
| Directed | 13 | Core Regions | `graphify_lab_full_corpus_txt_z03_friedmann_1967_a_generalized_theory_of_polarized_development_core_regions` |
| Directed | 12 | Derived-Demand Framework | `graphify_lab_full_corpus_txt_m07_levine_grengs_merlin_2019_from_mobility_to_accessibility_transforming_urban_transportation_and_land_use_planning_no_doi_derived_demand_framework` |
| Directed | 12 | Central-Place Types | `graphify_lab_full_corpus_txt_t14_christaller_1966_central_places_in_southern_germany_no_doi_central_place_types` |
| Directed | 12 | Agglomeration | `t08_fujita_krugman_venables_1999_the_spatial_economy_cities_regions_and_international_trade_no_doi_agglomeration` |
| Directed | 10 | Range of Central Goods | `graphify_lab_full_corpus_txt_t14_christaller_1966_central_places_in_southern_germany_no_doi_range_of_central_goods` |
| Directed | 10 | Ability to Invest | `graphify_lab_full_corpus_txt_t16_hirschman_1958_the_strategy_of_economic_development_no_doi_ability_to_invest` |
| Directed | 10 | Innovation | `graphify_lab_full_corpus_txt_z03_friedmann_1967_a_generalized_theory_of_polarized_development_innovation` |
| Directed | 10 | The Spatial Economy: Cities, Regions, and International Trade | `t08_fujita_krugman_venables_1999_the_spatial_economy_cities_regions_and_international_trade_no_doi_the_spatial_economy` |
| Directed | 9 | Land exchange model | `graphify_lab_full_corpus_txt_m08_batty_2013_the_new_science_of_cities_no_doi_land_exchange_model` |
| Directed | 9 | Strategic (Spatial) Planning Reexamined | `graphify_lab_full_corpus_txt_m13_albrechts_2004_strategic_spatial_planning_reexamined_10_1068_b3065_strategic_spatial_planning_reexamined` |

## Duplicate Labels

The reviewed graph contains 32 case-folded duplicate-label groups. These are retained when provenance differs.

## Interpretation

The four added edges remove four binary orphans and reduce the undirected component count by four. M07 remains represented through its existing hyperedge, while T03 remains intentionally unlinked because its candidate targets are ambiguous.
