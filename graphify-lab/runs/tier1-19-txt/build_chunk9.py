import json
from pathlib import Path


TARGET = Path("graphify-out/.graphify_chunk_09.json")
Z03 = "/Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/graphify-lab/full-corpus-txt/Z03-friedmann-1967-a-generalized-theory-of-polarized-development.txt"
M14 = "/Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/graphify-lab/full-corpus-txt/M14-healey-2009-in-search-of-the-strategic-in-spatial-strategy-making-10.1080-14649350903417191.txt"
M16 = "/Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/graphify-lab/full-corpus-txt/M16-healey-2006-transforming-governance-challenges-of-institutional-adaptation-and-a-new-politics-of-space-10.1080-09654310500420792.txt"
T09 = "/Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/graphify-lab/full-corpus-txt/T09-arthur-1990-silicon-valley-locational-clusters-when-do-increasing-returns-imply-monopoly-10.1016-0165-4896-90-90064-E.txt"

PZ = "graphify_lab_full_corpus_txt_z03_friedmann_1967_a_generalized_theory_of_polarized_development"
P14 = "graphify_lab_full_corpus_txt_m14_healey_2009_in_search_of_the_strategic_in_spatial_strategy_making_10_1080_14649350903417191"
P16 = "graphify_lab_full_corpus_txt_m16_healey_2006_transforming_governance_challenges_of_institutional_adaptation_and_a_new_politics_of_space_10_1080_09654310500420792"
P09 = "graphify_lab_full_corpus_txt_t09_arthur_1990_silicon_valley_locational_clusters_when_do_increasing_returns_imply_monopoly_10_1016_0165_4896_90_90064_e"

# These are citation targets already verified in other raw fragments.
EXT_T16 = "graphify_lab_full_corpus_txt_t16_hirschman_1958_the_strategy_of_economic_development_no_doi_the_strategy_of_economic_development"
EXT_T17 = "graphify_lab_full_corpus_txt_t17_perroux_1955_note_sur_la_notion_de_pole_de_croissance_10_3406_ecoap_1955_2522_paper"
EXT_T05 = "t05_myrdal_1957_economic_theory_and_under_developed_regions_no_doi_economic_theory_and_under_developed_regions"
EXT_M13 = "graphify_lab_full_corpus_txt_m13_albrechts_2004_strategic_spatial_planning_reexamined_10_1068_b3065_strategic_spatial_planning_reexamined"

nodes = []
edges = []
hyperedges = []
node_ids = set()


def add_node(prefix, source, slug, label, file_type, location, rationale=None):
    node_id = f"{prefix}_{slug}"
    assert node_id not in node_ids, node_id
    assert all(c.islower() or c.isdigit() or c == "_" for c in node_id), node_id
    node_ids.add(node_id)
    node = {
        "id": node_id,
        "label": label,
        "file_type": file_type,
        "source_file": source,
        "source_location": location,
        "source_url": None,
        "captured_at": None,
        "author": None,
        "contributor": None,
    }
    if rationale is not None:
        node["rationale"] = rationale
    nodes.append(node)
    return node_id


def add_edge(source, target, relation, confidence, score, origin, location, weight=1.0):
    assert source in node_ids, source
    assert target in node_ids or target in {EXT_T16, EXT_T17, EXT_T05, EXT_M13}, target
    assert relation in {
        "calls",
        "implements",
        "references",
        "cites",
        "conceptually_related_to",
        "shares_data_with",
        "semantically_similar_to",
        "rationale_for",
    }
    assert confidence == "EXTRACTED" and score == 1.0 or confidence == "INFERRED" and score in {0.95, 0.85, 0.75, 0.65, 0.55} or confidence == "AMBIGUOUS" and 0.1 <= score <= 0.3
    edges.append(
        {
            "source": source,
            "target": target,
            "relation": relation,
            "confidence": confidence,
            "confidence_score": score,
            "source_file": origin,
            "source_location": location,
            "weight": weight,
        }
    )


# Z03: Friedmann's general theory of polarized development.
z_paper = add_node(PZ, Z03, "a_general_theory_of_polarized_development", "A General Theory of Polarized Development", "paper", "lines 14-24")
z_author = add_node(PZ, Z03, "john_friedmann", "John Friedmann", "concept", "lines 19-24")
z_regional_planning = add_node(PZ, Z03, "regional_planning", "Regional Planning", "concept", "lines 42-54")
z_spatial_theory = add_node(PZ, Z03, "spatial_development_theory", "Theory of Development in Its Spatial Dimension", "rationale", "lines 130-141", "A theory for regional planning must link social change with territorial organization and treat space as an independent variable.")
z_territorial_org = add_node(PZ, Z03, "territorial_organization", "Territorial Organization", "concept", "lines 130-141")
z_spatial_system = add_node(PZ, Z03, "spatial_system", "Spatial System", "concept", "lines 358-368")
z_field_forces = add_node(PZ, Z03, "space_as_field_of_forces", "Space as a Field of Forces", "rationale", "lines 130-141", "Space is treated as a structured field of forces such as energy levels, decision-making power, and communications, rather than only physical distance.")
z_social_change = add_node(PZ, Z03, "social_change", "Social Change", "concept", "lines 143-163")
z_dahrendorf = add_node(PZ, Z03, "dahrendorf_conflict_model", "Dahrendorf Conflict Model", "concept", "lines 157-163")
z_location = add_node(PZ, Z03, "classical_location_theory", "Classical Location Theory", "concept", "lines 69-79")
z_growth_centers = add_node(PZ, Z03, "growth_centers", "Growth Centers", "concept", "lines 69-79")
z_spatial_org = add_node(PZ, Z03, "spatial_organization_theory", "Spatial Organization Theory", "concept", "lines 80-94")
z_general_equilibrium = add_node(PZ, Z03, "general_equilibrium_model", "General Equilibrium Model", "rationale", "lines 80-114", "Static equilibrium can describe point-location patterns but does not explain the historical path of transformation.")
z_regional_dev = add_node(PZ, Z03, "regional_development_theory", "Regional Development Theory", "concept", "lines 96-114")
z_interregional_flows = add_node(PZ, Z03, "interregional_flows", "Interregional Flows of Labor and Capital", "concept", "lines 102-114")
z_siebert = add_node(PZ, Z03, "siebert_regional_models", "Siebert Models of Regions", "concept", "lines 122-128")
z_technical_knowledge = add_node(PZ, Z03, "technical_knowledge", "Technical Knowledge", "concept", "lines 122-128")
z_diffusion = add_node(PZ, Z03, "diffusion_of_innovations", "Diffusion of Innovations", "concept", "lines 122-128")
z_communication = add_node(PZ, Z03, "communication", "Communication", "concept", "lines 130-141")
z_dev_innovation = add_node(PZ, Z03, "development_as_innovation", "Development as Innovation", "rationale", "lines 209-266", "Development is a discontinuous succession of innovations that gradually forms clusters and linked systems, producing structural transformation.")
z_epochal = add_node(PZ, Z03, "epochal_innovation", "Epochal Innovation", "concept", "lines 211-260")
z_paradigm = add_node(PZ, Z03, "sociocultural_paradigm", "Socio-Cultural Paradigm", "concept", "lines 211-234")
z_clusters = add_node(PZ, Z03, "innovation_clusters", "Innovation Clusters", "concept", "lines 262-275")
z_linked_innovations = add_node(PZ, Z03, "linked_systems_of_innovations", "Linked Systems of Innovations", "concept", "lines 262-275")
z_growth = add_node(PZ, Z03, "growth", "Growth", "concept", "lines 277-286")
z_structural_change = add_node(PZ, Z03, "structural_change", "Structural Change", "concept", "lines 277-286")
z_asynchronic = add_node(PZ, Z03, "asynchronous_development", "Asynchronous Development", "concept", "lines 287-312")
z_leading = add_node(PZ, Z03, "leading_forces", "Leading or Innovative Forces", "concept", "lines 287-312")
z_lagging = add_node(PZ, Z03, "lagging_forces", "Lagging or Traditional Forces", "concept", "lines 287-312")
z_traditional = add_node(PZ, Z03, "traditional_social_matrix", "Traditional Social Matrix", "concept", "lines 292-312")
z_invention = add_node(PZ, Z03, "invention", "Invention", "concept", "lines 314-319")
z_innovation = add_node(PZ, Z03, "innovation", "Innovation", "concept", "lines 320-342")
z_borrowing = add_node(PZ, Z03, "borrowing_and_imitation", "Borrowing and Imitation", "concept", "lines 323-327")
z_innovator = add_node(PZ, Z03, "innovator", "Innovator", "concept", "lines 339-342")
z_innovation_demand = add_node(PZ, Z03, "innovation_demand", "Demand for Innovation", "concept", "lines 344-351")
z_frame_confrontation = add_node(PZ, Z03, "mental_frame_confrontation", "Confrontation of Mental Frames", "concept", "lines 352-373")
z_comm_field = add_node(PZ, Z03, "communication_field", "Communication Field", "rationale", "lines 358-373", "A spatial system has a field in which the probability of information exchange varies across locations.")
z_info_exchange = add_node(PZ, Z03, "information_exchange", "Information Exchange", "concept", "lines 358-373")
z_type_i = add_node(PZ, Z03, "type_i_spatial_system", "Type I Spatial System", "rationale", "lines 378-380", "Rigid, hierarchical, centrally controlled systems tend to have low innovative capacity.")
z_type_ii = add_node(PZ, Z03, "type_ii_spatial_system", "Type II Spatial System", "rationale", "lines 382-393", "Fluid, non-hierarchical, multi-centric, horizontally integrated systems can generate innovation, but conflict may also produce deadlock.")
z_hybrid = add_node(PZ, Z03, "hybrid_social_system", "Hybrid Type I-Type II System", "rationale", "lines 399-405", "The proposed optimal arrangement superimposes leadership, central information, and conflict-resolution functions on a Type II system.")
z_personalities = add_node(PZ, Z03, "innovative_personalities", "Innovative Personalities", "concept", "lines 407-421")
z_large_city = add_node(PZ, Z03, "large_city_innovation_conditions", "Large City Innovation Conditions", "rationale", "lines 423-512", "Large cities combine problem pressure, information flows, cultural heterogeneity, diffuse power, resources, and rewards that can raise the probability of innovation.")
z_power = add_node(PZ, Z03, "power", "Power", "concept", "lines 516-529")
z_authority = add_node(PZ, Z03, "authority", "Authority", "concept", "lines 531-542")
z_institutionalized_power = add_node(PZ, Z03, "institutionalized_power", "Institutionalized Power", "rationale", "lines 531-536", "Power potential is fully extracted when its exercise is socially legitimate.")
z_authority_dependency = add_node(PZ, Z03, "authority_dependency_relations", "Authority-Dependency Relations", "rationale", "lines 563-580", "Spatial systems are integrated through authority-dependency relations maintained by legitimacy and coercion.")
z_counter_elites = add_node(PZ, Z03, "counter_elites", "Counter-Elites", "concept", "lines 549-561")
z_authority_conflict = add_node(PZ, Z03, "authority_conflict", "Conflict over Authority", "concept", "lines 574-618")
z_suppression = add_node(PZ, Z03, "suppression", "Suppression", "concept", "lines 582-593")
z_neutralization = add_node(PZ, Z03, "neutralization", "Neutralization", "concept", "lines 594-601")
z_cooptation = add_node(PZ, Z03, "cooptation", "Cooptation", "concept", "lines 602-604")
z_replacement = add_node(PZ, Z03, "replacement", "Replacement", "concept", "lines 605-606")
z_legitimate = add_node(PZ, Z03, "legitimate_conflict", "Legitimate Conflict", "concept", "lines 608-615")
z_illegitimate = add_node(PZ, Z03, "illegitimate_conflict", "Illegitimate Conflict", "concept", "lines 617-618")
z_integration = add_node(PZ, Z03, "social_integration", "Social Integration", "concept", "lines 568-580")
z_core = add_node(PZ, Z03, "core_regions", "Core Regions", "rationale", "lines 677-708", "Core regions are high-capacity centres of change; the periphery is defined through dependency on them.")
z_periphery = add_node(PZ, Z03, "peripheral_regions", "Peripheral Regions", "concept", "lines 694-703")
z_core_periphery = add_node(PZ, Z03, "core_periphery_spatial_system", "Core-Periphery Spatial System", "concept", "lines 702-708")
z_dependency = add_node(PZ, Z03, "dependency_relation", "Dependency Relation", "concept", "lines 699-700")
z_dominance = add_node(PZ, Z03, "dominance_effect", "Dominance Effect", "concept", "lines 773-780")
z_information_effect = add_node(PZ, Z03, "information_effect", "Information Effect", "concept", "lines 782-793")
z_psychological = add_node(PZ, Z03, "psychological_effect", "Psychological Effect", "concept", "lines 795-802")
z_modernization = add_node(PZ, Z03, "modernization_effect", "Modernization Effect", "concept", "lines 804-808")
z_linkage = add_node(PZ, Z03, "linkage_effects", "Linkage Effects", "concept", "lines 810-823")
z_production = add_node(PZ, Z03, "production_effects", "Production Effects", "concept", "lines 825-836")
z_spread = add_node(PZ, Z03, "spread_effects", "Spread Effects", "concept", "lines 875-905")
z_backwash = add_node(PZ, Z03, "backwash_effects", "Backwash Effects", "concept", "lines 1775-1802")
z_hierarchy = add_node(PZ, Z03, "core_region_hierarchy", "Hierarchy of Core Regions", "concept", "lines 976-1010")
z_transmission = add_node(PZ, Z03, "innovation_transmission", "Transmission of Innovation", "concept", "lines 1013-1049")
z_critical = add_node(PZ, Z03, "critical_point", "Critical Point of Core Development", "rationale", "lines 1051-1062", "Self-reinforcing core development becomes dysfunctional beyond a threshold unless spread effects accelerate and peripheral dependence is reduced.")
z_surface = add_node(PZ, Z03, "communication_surface_expansion", "Expansion of the Communication Surface", "concept", "lines 1068-1079")
z_modernizing = add_node(PZ, Z03, "modernizing_institutions", "Modernizing Institutions", "concept", "lines 1730-1754")
z_convergence = add_node(PZ, Z03, "cultural_convergence", "Core Region Cultural Convergence", "concept", "lines 1760-1773")
z_core_expansion = add_node(PZ, Z03, "core_region_expansion", "Core Region Expansion", "concept", "lines 1581-1624")
z_national_autonomy = add_node(PZ, Z03, "national_autonomy", "National Autonomy", "concept", "lines 1365-1414")
z_regional_autonomy = add_node(PZ, Z03, "regional_autonomy", "Regional Autonomy", "concept", "lines 1858-1869")
z_alliances = add_node(PZ, Z03, "political_alliances", "Political Alliances", "concept", "lines 1519-1551")
z_brazil = add_node(PZ, Z03, "brazilian_northeast", "Brazilian Northeast", "concept", "lines 1871-1900")
z_sudene = add_node(PZ, Z03, "sudene", "SUDENE", "concept", "lines 1902-1936")
z_ne_cores = add_node(PZ, Z03, "northeastern_core_regions", "Northeastern Core Regions", "concept", "lines 1929-1936")

add_edge(z_paper, z_author, "references", "EXTRACTED", 1.0, Z03, "lines 14-24")
add_edge(z_spatial_theory, z_regional_planning, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 130-141")
add_edge(z_spatial_theory, z_social_change, "references", "EXTRACTED", 1.0, Z03, "lines 130-163")
add_edge(z_spatial_theory, z_territorial_org, "references", "EXTRACTED", 1.0, Z03, "lines 130-141")
add_edge(z_spatial_theory, z_spatial_system, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 130-141")
add_edge(z_field_forces, z_spatial_system, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 130-141")
add_edge(z_dahrendorf, z_social_change, "references", "EXTRACTED", 1.0, Z03, "lines 157-163")
add_edge(z_location, z_growth_centers, "references", "EXTRACTED", 1.0, Z03, "lines 69-79")
add_edge(z_spatial_org, z_general_equilibrium, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 80-94")
add_edge(z_regional_dev, z_general_equilibrium, "references", "EXTRACTED", 1.0, Z03, "lines 96-114")
add_edge(z_interregional_flows, z_regional_dev, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 102-114")
add_edge(z_siebert, z_technical_knowledge, "references", "EXTRACTED", 1.0, Z03, "lines 122-128")
add_edge(z_siebert, z_diffusion, "references", "EXTRACTED", 1.0, Z03, "lines 122-128")
add_edge(z_siebert, z_communication, "references", "EXTRACTED", 1.0, Z03, "lines 122-128")
add_edge(z_dev_innovation, z_epochal, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 209-266")
add_edge(z_dev_innovation, z_clusters, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 262-266")
add_edge(z_dev_innovation, z_linked_innovations, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 262-266")
add_edge(z_epochal, z_paradigm, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 211-234")
add_edge(z_dev_innovation, z_structural_change, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 248-266")
add_edge(z_growth, z_structural_change, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 277-286")
add_edge(z_asynchronic, z_leading, "references", "EXTRACTED", 1.0, Z03, "lines 287-312")
add_edge(z_asynchronic, z_lagging, "references", "EXTRACTED", 1.0, Z03, "lines 287-312")
add_edge(z_leading, z_traditional, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 292-312")
add_edge(z_invention, z_innovation, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 314-327")
add_edge(z_borrowing, z_innovation, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 323-327")
add_edge(z_innovator, z_innovation, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 339-342")
add_edge(z_innovation_demand, z_innovation, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 344-351")
add_edge(z_frame_confrontation, z_info_exchange, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 352-373")
add_edge(z_comm_field, z_info_exchange, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 358-373")
add_edge(z_info_exchange, z_innovation, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 370-373")
add_edge(z_type_i, z_innovation, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 378-380")
add_edge(z_type_ii, z_innovation, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 382-393")
add_edge(z_hybrid, z_type_i, "references", "EXTRACTED", 1.0, Z03, "lines 399-405")
add_edge(z_hybrid, z_type_ii, "references", "EXTRACTED", 1.0, Z03, "lines 399-405")
add_edge(z_large_city, z_innovation, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 423-512")
add_edge(z_large_city, z_comm_field, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 448-465")
add_edge(z_large_city, z_personalities, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 467-481")
add_edge(z_power, z_authority, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 516-542")
add_edge(z_institutionalized_power, z_authority, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 531-542")
add_edge(z_authority, z_authority_dependency, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 563-580")
add_edge(z_counter_elites, z_authority_conflict, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 549-580")
add_edge(z_authority_conflict, z_suppression, "references", "EXTRACTED", 1.0, Z03, "lines 582-606")
add_edge(z_authority_conflict, z_neutralization, "references", "EXTRACTED", 1.0, Z03, "lines 582-606")
add_edge(z_authority_conflict, z_cooptation, "references", "EXTRACTED", 1.0, Z03, "lines 582-606")
add_edge(z_authority_conflict, z_replacement, "references", "EXTRACTED", 1.0, Z03, "lines 582-606")
add_edge(z_legitimate, z_authority_conflict, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 608-618")
add_edge(z_illegitimate, z_authority_conflict, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 608-618")
add_edge(z_authority_dependency, z_integration, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 568-580")
add_edge(z_core, z_periphery, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 694-703")
add_edge(z_periphery, z_dependency, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 699-700")
add_edge(z_core_periphery, z_authority_dependency, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 702-708")
add_edge(z_core, z_core_periphery, "references", "EXTRACTED", 1.0, Z03, "lines 694-708")
add_edge(z_dominance, z_core, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 773-780")
add_edge(z_information_effect, z_core, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 782-793")
add_edge(z_psychological, z_core, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 795-802")
add_edge(z_modernization, z_core, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 804-808")
add_edge(z_linkage, z_innovation, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 810-823")
add_edge(z_production, z_innovation, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 825-836")
add_edge(z_spread, z_core, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 875-905")
add_edge(z_backwash, z_core, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 1775-1802")
add_edge(z_hierarchy, z_core, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 976-1010")
add_edge(z_transmission, z_core, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 1013-1049")
add_edge(z_transmission, z_periphery, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 1013-1049")
add_edge(z_critical, z_spread, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 1051-1062")
add_edge(z_critical, z_backwash, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 1051-1062")
add_edge(z_surface, z_core_expansion, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 1068-1079")
add_edge(z_modernizing, z_transmission, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 1730-1754")
add_edge(z_modernizing, z_convergence, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 1760-1773")
add_edge(z_core_expansion, z_core, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 1581-1624")
add_edge(z_national_autonomy, z_dependency, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 1365-1414")
add_edge(z_alliances, z_national_autonomy, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 1519-1551")
add_edge(z_regional_autonomy, z_periphery, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 1858-1869")
add_edge(z_brazil, z_sudene, "references", "EXTRACTED", 1.0, Z03, "lines 1871-1900")
add_edge(z_sudene, z_regional_autonomy, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 1902-1925")
add_edge(z_sudene, z_ne_cores, "rationale_for", "EXTRACTED", 1.0, Z03, "lines 1925-1936")
add_edge(z_ne_cores, z_core, "conceptually_related_to", "EXTRACTED", 1.0, Z03, "lines 1929-1936")
add_edge(z_paper, EXT_T16, "cites", "EXTRACTED", 1.0, Z03, "lines 111-114; notes lines 2063-2066")
add_edge(z_paper, EXT_T17, "cites", "EXTRACTED", 1.0, Z03, "lines 69-79; notes lines 2002-2018")


# M14: Healey's account of strategic work and practical judgement.
m14_paper = add_node(P14, M14, "in_search_of_the_strategic_in_spatial_strategy_making", "In Search of the Strategic in Spatial Strategy Making", "paper", "lines 40-53")
m14_author = add_node(P14, M14, "patsy_healey", "Patsy Healey", "concept", "lines 40-47")
m14_strategy = add_node(P14, M14, "spatial_strategy_making", "Spatial Strategy Making", "concept", "lines 112-188")
m14_work = add_node(P14, M14, "strategic_work", "Strategic Work", "rationale", "lines 176-191", "Strategic work is integrative and aims to change direction, open possibilities, and move away from previous positions.")
m14_transformative = add_node(P14, M14, "transformative_governance_work", "Transformative Governance Work", "rationale", "lines 179-188", "Spatial strategy making responds to changing contexts and contributes to governance as enduring public infrastructure.")
m14_complex = add_node(P14, M14, "urban_complex", "Urban Complex", "concept", "lines 167-175")
m14_infrastructure = add_node(P14, M14, "governance_infrastructure", "Governance Infrastructure", "rationale", "lines 218-235", "Spatial strategies work by framing and focusing how actors involved in urban development think and act.")
m14_social_product = add_node(P14, M14, "social_product", "Spatial Strategy as Social Product", "concept", "lines 218-224")
m14_reference_frame = add_node(P14, M14, "reference_frame", "Reference Frame", "concept", "lines 224-235")
m14_orientation = add_node(P14, M14, "strategic_orientation", "Strategic Orientation", "concept", "lines 224-235")
m14_polity = add_node(P14, M14, "polity", "Polity", "concept", "lines 228-235")
m14_attention = add_node(P14, M14, "mobilise_attention", "Mobilising Attention", "concept", "lines 280-288")
m14_judgement = add_node(P14, M14, "integrative_practical_judgement", "Integrative Practical Judgement", "rationale", "lines 189-216", "Judgement combines technical expertise, political astuteness, analytical knowledge, moral considerations, breadth, and sensitivity to experience.")
m14_change_direction = add_node(P14, M14, "change_direction", "Changing Direction", "concept", "lines 176-188")
m14_structuring = add_node(P14, M14, "structuring_dimension", "Structuring Dimension", "concept", "lines 179-188")
m14_collective = add_node(P14, M14, "collective_governance_effort", "Collective Governance Effort", "concept", "lines 194-202")
m14_problems = add_node(P14, M14, "policy_problems", "Policy Problems", "concept", "lines 236-246")
m14_solutions = add_node(P14, M14, "policy_solutions", "Policy Solutions", "concept", "lines 236-246")
m14_policy_streams = add_node(P14, M14, "policy_streams", "Policy Streams", "concept", "lines 236-246")
m14_opportunity = add_node(P14, M14, "opportunity_structure", "Opportunity Structure", "rationale", "lines 324-360", "Opportunity structure is a shifting complex of relations that can expand through transformative energy or contract under doubt and challenge.")
m14_momentum = add_node(P14, M14, "momentum_for_change", "Momentum for Change", "concept", "lines 296-333")
m14_institutional_moment = add_node(P14, M14, "institutional_moment", "Institutional Moment", "concept", "lines 324-333")
m14_situating = add_node(P14, M14, "situating_and_scoping", "Situating and Scoping", "concept", "lines 427-493")
m14_strategy_makers = add_node(P14, M14, "strategy_makers", "Strategy Makers", "concept", "lines 427-461")
m14_identity = add_node(P14, M14, "institutional_identity", "Institutional Identity", "concept", "lines 447-481")
m14_audit = add_node(P14, M14, "institutional_audit", "Institutional Audit", "concept", "lines 482-493")
m14_agency_field = add_node(P14, M14, "agency_field", "Agency Field", "concept", "lines 482-493")
m14_levers = add_node(P14, M14, "levers_of_power", "Levers of Power", "concept", "lines 482-493")
m14_endogenous = add_node(P14, M14, "endogenous_trajectory", "Endogenous Trajectory", "concept", "lines 494-509")
m14_exogenous = add_node(P14, M14, "exogenous_trajectory", "Exogenous Trajectory", "concept", "lines 494-509")
m14_practical_politics = add_node(P14, M14, "practical_politics", "Practical Politics", "concept", "lines 521-538")
m14_knowledgeability = add_node(P14, M14, "knowledgeability", "Knowledgeability", "rationale", "lines 561-624", "Strategic work needs multiple knowledge traditions, experiential understanding, open-mindedness, and a systemic grasp of connections.")
m14_knowledge = add_node(P14, M14, "knowledge_resources", "Knowledge Resources", "concept", "lines 539-558")
m14_experiential = add_node(P14, M14, "experiential_knowledge", "Experiential Knowledge", "concept", "lines 575-597")
m14_systematised = add_node(P14, M14, "systematised_knowledge", "Systematised Knowledge", "concept", "lines 561-584")
m14_open = add_node(P14, M14, "open_mindedness", "Open-Mindedness", "concept", "lines 598-607")
m14_pluralism = add_node(P14, M14, "pluralistic_imagination", "Pluralistic Imagination", "concept", "lines 598-624")
m14_systemic = add_node(P14, M14, "systemic_qualities", "Systemic Qualities", "concept", "lines 608-624")
m14_inquiry = add_node(P14, M14, "community_of_inquiry", "Community of Inquiry", "concept", "lines 623-655")
m14_selective = add_node(P14, M14, "selective_framing", "Selective Framing", "concept", "lines 658-678")
m14_frame = add_node(P14, M14, "strategic_frame", "Strategic Frame", "rationale", "lines 658-728", "A strategic frame selects and names a meaningful direction, links problems to action, and helps actors position activity in a wider context.")
m14_framing_ideas = add_node(P14, M14, "framing_ideas", "Framing Ideas", "concept", "lines 658-678")
m14_front_back = add_node(P14, M14, "frontstage_backstage", "Frontstage and Backstage", "concept", "lines 670-678")
m14_simplification = add_node(P14, M14, "selective_simplification", "Selective Simplification", "rationale", "lines 679-693", "Framing simplifies urban dynamics and is therefore politically consequential and morally burdensome.")
m14_moral = add_node(P14, M14, "moral_responsibility", "Moral Responsibility", "concept", "lines 687-693")
m14_sense = add_node(P14, M14, "collective_sense_making", "Collective Sense Making", "concept", "lines 743-762")
m14_synthetic = add_node(P14, M14, "synthetic_imagination", "Synthetic Imagination", "concept", "lines 799-822")
m14_ethics = add_node(P14, M14, "ethical_reflexivity", "Ethical Reflexivity", "concept", "lines 799-822")
m14_transformative_strategy = add_node(P14, M14, "transformative_strategy_making", "Transformative Strategy Making", "concept", "lines 858-911")
m14_responsive_strategy = add_node(P14, M14, "responsive_strategy_making", "Responsive Strategy Making", "concept", "lines 870-911")
m14_institutionalization = add_node(P14, M14, "institutionalization", "Institutionalization", "concept", "lines 858-879")
m14_public_asset = add_node(P14, M14, "public_realm_asset", "Public Realm Asset", "concept", "lines 914-920")
m14_provisionality = add_node(P14, M14, "trajectory_provisionality", "Provisionality and Revisability", "concept", "lines 814-822")

add_edge(m14_paper, m14_author, "references", "EXTRACTED", 1.0, M14, "lines 40-53")
add_edge(m14_work, m14_strategy, "rationale_for", "EXTRACTED", 1.0, M14, "lines 176-188")
add_edge(m14_work, m14_change_direction, "rationale_for", "EXTRACTED", 1.0, M14, "lines 176-188")
add_edge(m14_strategy, m14_transformative, "rationale_for", "EXTRACTED", 1.0, M14, "lines 179-188")
add_edge(m14_social_product, m14_infrastructure, "rationale_for", "EXTRACTED", 1.0, M14, "lines 218-235")
add_edge(m14_strategy, m14_reference_frame, "rationale_for", "EXTRACTED", 1.0, M14, "lines 224-235")
add_edge(m14_reference_frame, m14_orientation, "conceptually_related_to", "EXTRACTED", 1.0, M14, "lines 224-235")
add_edge(m14_orientation, m14_polity, "rationale_for", "EXTRACTED", 1.0, M14, "lines 228-235")
add_edge(m14_attention, m14_complex, "rationale_for", "EXTRACTED", 1.0, M14, "lines 280-288")
add_edge(m14_judgement, m14_work, "rationale_for", "EXTRACTED", 1.0, M14, "lines 189-216")
add_edge(m14_collective, m14_strategy, "rationale_for", "EXTRACTED", 1.0, M14, "lines 194-202")
add_edge(m14_policy_streams, m14_problems, "references", "EXTRACTED", 1.0, M14, "lines 236-246")
add_edge(m14_policy_streams, m14_solutions, "references", "EXTRACTED", 1.0, M14, "lines 236-246")
add_edge(m14_problems, m14_solutions, "conceptually_related_to", "EXTRACTED", 1.0, M14, "lines 236-246")
add_edge(m14_opportunity, m14_momentum, "rationale_for", "EXTRACTED", 1.0, M14, "lines 324-360")
add_edge(m14_institutional_moment, m14_opportunity, "conceptually_related_to", "EXTRACTED", 1.0, M14, "lines 324-360")
add_edge(m14_situating, m14_strategy_makers, "rationale_for", "EXTRACTED", 1.0, M14, "lines 427-461")
add_edge(m14_strategy_makers, m14_identity, "rationale_for", "EXTRACTED", 1.0, M14, "lines 447-481")
add_edge(m14_audit, m14_agency_field, "rationale_for", "EXTRACTED", 1.0, M14, "lines 482-493")
add_edge(m14_audit, m14_levers, "rationale_for", "EXTRACTED", 1.0, M14, "lines 482-493")
add_edge(m14_endogenous, m14_situating, "references", "EXTRACTED", 1.0, M14, "lines 494-509")
add_edge(m14_exogenous, m14_situating, "references", "EXTRACTED", 1.0, M14, "lines 494-509")
add_edge(m14_practical_politics, m14_attention, "rationale_for", "EXTRACTED", 1.0, M14, "lines 521-538")
add_edge(m14_knowledgeability, m14_knowledge, "rationale_for", "EXTRACTED", 1.0, M14, "lines 539-558")
add_edge(m14_knowledgeability, m14_experiential, "rationale_for", "EXTRACTED", 1.0, M14, "lines 575-597")
add_edge(m14_knowledgeability, m14_systematised, "references", "EXTRACTED", 1.0, M14, "lines 561-584")
add_edge(m14_open, m14_pluralism, "rationale_for", "EXTRACTED", 1.0, M14, "lines 598-607")
add_edge(m14_open, m14_systemic, "rationale_for", "EXTRACTED", 1.0, M14, "lines 608-624")
add_edge(m14_inquiry, m14_knowledgeability, "rationale_for", "EXTRACTED", 1.0, M14, "lines 623-655")
add_edge(m14_selective, m14_frame, "rationale_for", "EXTRACTED", 1.0, M14, "lines 658-678")
add_edge(m14_frame, m14_framing_ideas, "conceptually_related_to", "EXTRACTED", 1.0, M14, "lines 658-678")
add_edge(m14_frame, m14_front_back, "rationale_for", "EXTRACTED", 1.0, M14, "lines 670-678")
add_edge(m14_simplification, m14_moral, "rationale_for", "EXTRACTED", 1.0, M14, "lines 679-693")
add_edge(m14_sense, m14_frame, "rationale_for", "EXTRACTED", 1.0, M14, "lines 743-762")
add_edge(m14_synthetic, m14_ethics, "conceptually_related_to", "EXTRACTED", 1.0, M14, "lines 799-822")
add_edge(m14_synthetic, m14_frame, "rationale_for", "EXTRACTED", 1.0, M14, "lines 799-822")
add_edge(m14_ethics, m14_provisionality, "rationale_for", "EXTRACTED", 1.0, M14, "lines 814-822")
add_edge(m14_transformative_strategy, m14_attention, "rationale_for", "EXTRACTED", 1.0, M14, "lines 893-911")
add_edge(m14_transformative_strategy, m14_knowledgeability, "rationale_for", "EXTRACTED", 1.0, M14, "lines 893-911")
add_edge(m14_transformative_strategy, m14_frame, "rationale_for", "EXTRACTED", 1.0, M14, "lines 908-911")
add_edge(m14_transformative_strategy, m14_institutionalization, "rationale_for", "EXTRACTED", 1.0, M14, "lines 858-879")
add_edge(m14_responsive_strategy, m14_transformative_strategy, "conceptually_related_to", "EXTRACTED", 1.0, M14, "lines 893-911")
add_edge(m14_institutionalization, m14_public_asset, "rationale_for", "EXTRACTED", 1.0, M14, "lines 858-920")
add_edge(m14_paper, EXT_M13, "cites", "EXTRACTED", 1.0, M14, "lines 156-162; references lines 1016-1018")


# M16: Healey's sociological institutionalist account and Newcastle cases.
m16_paper = add_node(P16, M16, "transforming_governance_challenges_of_institutional_adaptation_and_a_new_politics_of_space", "Transforming Governance: Challenges of Institutional Adaptation and a New Politics of Space", "paper", "lines 41-55")
m16_author = add_node(P16, M16, "patsy_healey", "Patsy Healey", "concept", "lines 41-49")
m16_transformation = add_node(P16, M16, "urban_governance_transformation", "Urban Governance Transformation", "rationale", "lines 98-113", "Governance transformation links actors, networks, discourses, practices, and cultural assumptions that confer authority and legitimacy.")
m16_changing = add_node(P16, M16, "changing_governance", "Changing Governance", "concept", "lines 117-143")
m16_rescaling = add_node(P16, M16, "rescaling_governance", "Re-Scaling of Governance Arenas and Networks", "concept", "lines 132-170")
m16_territorial = add_node(P16, M16, "territorial_focus", "Territorial Focus", "concept", "lines 138-143")
m16_politics = add_node(P16, M16, "new_politics_of_space", "New Politics of Space", "concept", "lines 141-170")
m16_progressive = add_node(P16, M16, "progressive_potential", "Progressive Potential", "concept", "lines 141-143")
m16_regressive = add_node(P16, M16, "regressive_potential", "Regressive Potential", "concept", "lines 141-143")
m16_fragmentation = add_node(P16, M16, "fragmentation", "Fragmentation", "rationale", "lines 171-216", "Fragmentation may be a new competitive reality, dis-integration, or a destabilization that creates opportunities for new territorial integration.")
m16_project = add_node(P16, M16, "project_driven_practice", "Project-Driven Practice", "concept", "lines 171-188")
m16_partnerships = add_node(P16, M16, "governance_partnerships", "Governance Partnerships", "concept", "lines 179-188")
m16_multilevel = add_node(P16, M16, "multilevel_governance_arenas", "Multi-Level Governance Arenas", "concept", "lines 183-188")
m16_institutionalist = add_node(P16, M16, "sociological_institutionalist_approach", "Sociological Institutionalist Approach", "rationale", "lines 217-241", "The approach provides intermediate tools between structural transformation and the situated experience of actors in places.")
m16_constructivism = add_node(P16, M16, "social_constructivism", "Social Constructivism", "concept", "lines 240-249")
m16_relational = add_node(P16, M16, "relational_social_action", "Relational Social Action", "concept", "lines 240-249")
m16_institutions = add_node(P16, M16, "institutions", "Institutions", "concept", "lines 242-249")
m16_norms = add_node(P16, M16, "norms_rules_practices", "Norms, Rules, and Practices", "concept", "lines 242-249")
m16_governance = add_node(P16, M16, "governance", "Governance", "rationale", "lines 250-283", "Governance encompasses regulation and mobilisation of social action and all forms of collective action focused on the public realm.")
m16_collective = add_node(P16, M16, "collective_action", "Collective Action", "concept", "lines 250-281")
m16_entrepreneurial = add_node(P16, M16, "entrepreneurial_governance", "Entrepreneurial Governance", "concept", "lines 261-267")
m16_landscape = add_node(P16, M16, "governance_landscape", "Governance Landscape", "concept", "lines 284-312")
m16_formal = add_node(P16, M16, "formal_government", "Formal Government", "concept", "lines 284-312")
m16_informal = add_node(P16, M16, "informal_networks", "Informal Networks", "concept", "lines 294-312")
m16_territorial_actor = add_node(P16, M16, "territorial_collective_actor", "Territorial Collective Actor", "concept", "lines 268-283")
m16_actor_capacity = add_node(P16, M16, "collective_actor_capacity", "Collective Actor Capacity", "concept", "lines 276-281")
m16_institutional_work = add_node(P16, M16, "institutional_work", "Institutional Work", "concept", "lines 261-267")
m16_binding = add_node(P16, M16, "binding_flows", "Binding Flows", "concept", "lines 313-342")
m16_structuration = add_node(P16, M16, "structuration_theory", "Structuration Theory", "concept", "lines 320-342")
m16_structure_agency = add_node(P16, M16, "structure_agency", "Structure and Agency", "rationale", "lines 320-342", "Governance transformation is shaped by the formative interaction between structuring pressures and actors-in-social-relations.")
m16_material = add_node(P16, M16, "material_resources", "Material Resources", "concept", "lines 323-331")
m16_authoritative = add_node(P16, M16, "authoritative_resources", "Authoritative Resources", "concept", "lines 325-331")
m16_frames = add_node(P16, M16, "framing_ideas", "Framing Ideas", "concept", "lines 328-342")
m16_structural_forces = add_node(P16, M16, "structural_forces", "Structural Forces", "concept", "lines 330-342")
m16_agency_power = add_node(P16, M16, "agency_power", "Agency Power", "concept", "lines 334-342")
m16_discourse = add_node(P16, M16, "discourse_structuration", "Discourse Structuration", "concept", "lines 353-379")
m16_discourse_inst = add_node(P16, M16, "discourse_institutionalization", "Discourse Institutionalization", "concept", "lines 353-379")
m16_levels = add_node(P16, M16, "levels_of_power", "Levels of Power", "concept", "lines 380-399")
m16_episodes = add_node(P16, M16, "governance_episodes", "Episodes of Governance", "concept", "lines 410-438")
m16_processes = add_node(P16, M16, "governance_processes", "Governance Processes", "concept", "lines 410-472")
m16_cultural = add_node(P16, M16, "cultural_assumptions", "Cultural Assumptions", "concept", "lines 429-472")
m16_innovation = add_node(P16, M16, "governance_innovation", "Governance Innovation", "concept", "lines 410-438")
m16_institutionalization = add_node(P16, M16, "institutionalization", "Institutionalization", "rationale", "lines 410-438", "Innovations endure when they move from explicit episodes into governance processes and become embedded in routine practices and cultural assumptions.")
m16_boundaries = add_node(P16, M16, "boundaries_and_resistance", "Boundaries and Resistance", "concept", "lines 417-438")
m16_capacity = add_node(P16, M16, "institutional_capacity", "Institutional Capacity", "rationale", "lines 495-522", "Enduring transformation requires social processes that build knowledge and relational resources capable of carrying ideas across governance arenas.")
m16_knowledge = add_node(P16, M16, "knowledge_resources", "Knowledge Resources", "concept", "lines 509-522")
m16_relational_resources = add_node(P16, M16, "relational_resources", "Relational Resources", "concept", "lines 509-522")
m16_capital = add_node(P16, M16, "intellectual_social_political_capital", "Intellectual, Social, and Political Capital", "concept", "lines 501-512")
m16_newcastle = add_node(P16, M16, "newcastle_governance_landscape", "Newcastle Governance Landscape", "concept", "lines 537-580")
m16_council = add_node(P16, M16, "newcastle_city_council", "Newcastle City Council", "concept", "lines 545-598")
m16_grainger = add_node(P16, M16, "grainger_town_partnership", "Grainger Town Partnership", "concept", "lines 613-679")
m16_grainger_funding = add_node(P16, M16, "national_funding", "National Government Funding", "concept", "lines 613-626")
m16_grainger_consult = add_node(P16, M16, "consultative_style", "Consultative Style", "concept", "lines 633-649")
m16_grainger_contained = add_node(P16, M16, "contained_temporary_arena", "Contained and Temporary Arena", "concept", "lines 644-679")
m16_going = add_node(P16, M16, "going_for_growth", "Going for Growth", "concept", "lines 687-789")
m16_population_decline = add_node(P16, M16, "population_decline", "Population Decline", "concept", "lines 707-722")
m16_citizen_protest = add_node(P16, M16, "citizen_protest", "Citizen Protest", "concept", "lines 723-747")
m16_area_committees = add_node(P16, M16, "area_committees", "Area Committees", "concept", "lines 775-789")
m16_local_partnerships = add_node(P16, M16, "local_strategic_partnerships", "Local Strategic Partnerships", "concept", "lines 775-789")
m16_ouseburn = add_node(P16, M16, "ouseburn_trust", "Ouseburn Trust", "concept", "lines 792-850")
m16_place_identity = add_node(P16, M16, "place_identity", "Place Identity", "concept", "lines 825-849")
m16_consultative_politics = add_node(P16, M16, "consultative_politics", "Consultative Politics", "concept", "lines 809-849")
m16_rescaling_focus = add_node(P16, M16, "rescaling_focus", "Re-Scaling Focus", "concept", "lines 866-888")
m16_central_local = add_node(P16, M16, "central_local_power_dynamic", "Central-Local Government Power Dynamic", "concept", "lines 956-968")
m16_people_places = add_node(P16, M16, "people_in_places", "People-in-Places", "concept", "lines 920-937")
m16_on_move = add_node(P16, M16, "governance_on_the_move", "Governance on the Move", "rationale", "lines 956-987", "The governance process is moving, but its trajectory remains uncertain and dependent on central-local power dynamics.")
m16_continual = add_node(P16, M16, "continual_transformation", "Continual Transformation", "concept", "lines 969-987")

add_edge(m16_paper, m16_author, "references", "EXTRACTED", 1.0, M16, "lines 41-55")
add_edge(m16_transformation, m16_changing, "rationale_for", "EXTRACTED", 1.0, M16, "lines 98-113")
add_edge(m16_changing, m16_rescaling, "references", "EXTRACTED", 1.0, M16, "lines 132-170")
add_edge(m16_changing, m16_territorial, "references", "EXTRACTED", 1.0, M16, "lines 138-143")
add_edge(m16_changing, m16_politics, "references", "EXTRACTED", 1.0, M16, "lines 141-170")
add_edge(m16_progressive, m16_transformation, "conceptually_related_to", "EXTRACTED", 1.0, M16, "lines 141-143")
add_edge(m16_regressive, m16_transformation, "conceptually_related_to", "EXTRACTED", 1.0, M16, "lines 141-143")
add_edge(m16_fragmentation, m16_transformation, "rationale_for", "EXTRACTED", 1.0, M16, "lines 171-226")
add_edge(m16_project, m16_fragmentation, "rationale_for", "EXTRACTED", 1.0, M16, "lines 171-188")
add_edge(m16_partnerships, m16_project, "references", "EXTRACTED", 1.0, M16, "lines 179-188")
add_edge(m16_multilevel, m16_landscape, "rationale_for", "EXTRACTED", 1.0, M16, "lines 183-188")
add_edge(m16_institutionalist, m16_transformation, "rationale_for", "EXTRACTED", 1.0, M16, "lines 217-241")
add_edge(m16_constructivism, m16_institutionalist, "references", "EXTRACTED", 1.0, M16, "lines 240-249")
add_edge(m16_relational, m16_institutionalist, "references", "EXTRACTED", 1.0, M16, "lines 240-249")
add_edge(m16_institutions, m16_norms, "rationale_for", "EXTRACTED", 1.0, M16, "lines 242-249")
add_edge(m16_governance, m16_collective, "rationale_for", "EXTRACTED", 1.0, M16, "lines 250-281")
add_edge(m16_governance, m16_institutional_work, "references", "EXTRACTED", 1.0, M16, "lines 261-267")
add_edge(m16_entrepreneurial, m16_governance, "conceptually_related_to", "EXTRACTED", 1.0, M16, "lines 261-267")
add_edge(m16_landscape, m16_formal, "references", "EXTRACTED", 1.0, M16, "lines 284-312")
add_edge(m16_landscape, m16_informal, "references", "EXTRACTED", 1.0, M16, "lines 294-312")
add_edge(m16_territorial_actor, m16_actor_capacity, "rationale_for", "EXTRACTED", 1.0, M16, "lines 268-281")
add_edge(m16_binding, m16_structure_agency, "rationale_for", "EXTRACTED", 1.0, M16, "lines 313-342")
add_edge(m16_structuration, m16_structure_agency, "rationale_for", "EXTRACTED", 1.0, M16, "lines 320-342")
add_edge(m16_material, m16_binding, "references", "EXTRACTED", 1.0, M16, "lines 323-331")
add_edge(m16_authoritative, m16_binding, "references", "EXTRACTED", 1.0, M16, "lines 325-331")
add_edge(m16_frames, m16_binding, "references", "EXTRACTED", 1.0, M16, "lines 328-342")
add_edge(m16_binding, m16_structural_forces, "rationale_for", "EXTRACTED", 1.0, M16, "lines 330-342")
add_edge(m16_structure_agency, m16_agency_power, "rationale_for", "EXTRACTED", 1.0, M16, "lines 334-342")
add_edge(m16_discourse, m16_discourse_inst, "rationale_for", "EXTRACTED", 1.0, M16, "lines 353-379")
add_edge(m16_discourse_inst, m16_processes, "rationale_for", "EXTRACTED", 1.0, M16, "lines 367-379")
add_edge(m16_levels, m16_episodes, "references", "EXTRACTED", 1.0, M16, "lines 380-399")
add_edge(m16_episodes, m16_processes, "rationale_for", "EXTRACTED", 1.0, M16, "lines 410-438")
add_edge(m16_processes, m16_cultural, "rationale_for", "EXTRACTED", 1.0, M16, "lines 410-472")
add_edge(m16_innovation, m16_episodes, "rationale_for", "EXTRACTED", 1.0, M16, "lines 410-438")
add_edge(m16_institutionalization, m16_innovation, "rationale_for", "EXTRACTED", 1.0, M16, "lines 410-438")
add_edge(m16_institutionalization, m16_processes, "rationale_for", "EXTRACTED", 1.0, M16, "lines 410-438")
add_edge(m16_boundaries, m16_innovation, "rationale_for", "EXTRACTED", 1.0, M16, "lines 417-438")
add_edge(m16_capacity, m16_knowledge, "rationale_for", "EXTRACTED", 1.0, M16, "lines 509-522")
add_edge(m16_capacity, m16_relational_resources, "rationale_for", "EXTRACTED", 1.0, M16, "lines 509-522")
add_edge(m16_capital, m16_capacity, "conceptually_related_to", "EXTRACTED", 1.0, M16, "lines 501-512")
add_edge(m16_newcastle, m16_council, "references", "EXTRACTED", 1.0, M16, "lines 537-598")
add_edge(m16_grainger, m16_grainger_funding, "rationale_for", "EXTRACTED", 1.0, M16, "lines 613-626")
add_edge(m16_grainger, m16_grainger_consult, "rationale_for", "EXTRACTED", 1.0, M16, "lines 633-649")
add_edge(m16_grainger, m16_grainger_contained, "rationale_for", "EXTRACTED", 1.0, M16, "lines 644-679")
add_edge(m16_grainger, m16_council, "references", "EXTRACTED", 1.0, M16, "lines 625-679")
add_edge(m16_going, m16_population_decline, "rationale_for", "EXTRACTED", 1.0, M16, "lines 707-722")
add_edge(m16_going, m16_citizen_protest, "rationale_for", "EXTRACTED", 1.0, M16, "lines 723-747")
add_edge(m16_citizen_protest, m16_consultative_politics, "rationale_for", "EXTRACTED", 1.0, M16, "lines 740-752")
add_edge(m16_going, m16_area_committees, "references", "EXTRACTED", 1.0, M16, "lines 775-789")
add_edge(m16_going, m16_local_partnerships, "references", "EXTRACTED", 1.0, M16, "lines 775-789")
add_edge(m16_ouseburn, m16_place_identity, "rationale_for", "EXTRACTED", 1.0, M16, "lines 825-849")
add_edge(m16_ouseburn, m16_consultative_politics, "rationale_for", "EXTRACTED", 1.0, M16, "lines 809-849")
add_edge(m16_rescaling_focus, m16_newcastle, "rationale_for", "EXTRACTED", 1.0, M16, "lines 866-888")
add_edge(m16_on_move, m16_central_local, "rationale_for", "EXTRACTED", 1.0, M16, "lines 956-987")
add_edge(m16_continual, m16_on_move, "rationale_for", "EXTRACTED", 1.0, M16, "lines 969-987")
add_edge(m16_people_places, m16_territorial, "conceptually_related_to", "EXTRACTED", 1.0, M16, "lines 920-937")


# T09: Arthur's path-dependent model of locational increasing returns.
t09_paper = add_node(P09, T09, "silicon_valley_locational_clusters_when_do_increasing_returns_imply_monopoly", "Silicon Valley Locational Clusters: When Do Increasing Returns Imply Monopoly?", "paper", "lines 33-64")
t09_author = add_node(P09, T09, "w_brian_arthur", "W. Brian Arthur", "concept", "lines 33-43")
t09_increasing = add_node(P09, T09, "increasing_returns", "Increasing Returns", "rationale", "lines 46-64", "Unbounded agglomeration returns can produce monopoly, but bounded returns do not guarantee a single dominant location.")
t09_network = add_node(P09, T09, "network_externalities", "Network Externalities", "concept", "lines 68-78")
t09_agglomeration = add_node(P09, T09, "agglomeration_economies", "Agglomeration Economies", "rationale", "lines 74-78", "Firms benefit from being close to other firms, so existing concentration can attract subsequent entrants.")
t09_benefits = add_node(P09, T09, "agglomeration_benefits", "Agglomeration Benefits", "concept", "lines 134-149")
t09_diseconomies = add_node(P09, T09, "diseconomies_of_agglomeration", "Diseconomies of Agglomeration", "concept", "lines 143-149")
t09_geography = add_node(P09, T09, "geographical_benefits", "Geographical Benefits", "concept", "lines 147-149")
t09_history = add_node(P09, T09, "historical_accident", "Historical Accident", "rationale", "lines 83-100", "Early entry order and heterogeneous firm types can select one of multiple possible locational patterns.")
t09_firms = add_node(P09, T09, "heterogeneous_firms", "Heterogeneous Firms", "concept", "lines 157-183")
t09_entry = add_node(P09, T09, "random_entry_order", "Random Entry Order", "concept", "lines 169-183")
t09_locations = add_node(P09, T09, "candidate_locations", "Candidate Locations", "concept", "lines 150-183")
t09_tastes = add_node(P09, T09, "locational_tastes", "Locational Tastes", "concept", "lines 157-183")
t09_distribution = add_node(P09, T09, "firm_type_distribution", "Distribution of Firm Types", "concept", "lines 169-183")
t09_probability = add_node(P09, T09, "locational_choice_probability", "Locational Choice Probability", "concept", "lines 188-203")
t09_shares = add_node(P09, T09, "locational_shares", "Locational Shares", "concept", "lines 217-228")
t09_stochastic = add_node(P09, T09, "stochastic_approximation", "Stochastic Approximation", "concept", "lines 229-247")
t09_expected = add_node(P09, T09, "expected_motion", "Expected Motion", "concept", "lines 248-263")
t09_perturbation = add_node(P09, T09, "perturbation_effect", "Perturbation Effect", "concept", "lines 257-263")
t09_fixed = add_node(P09, T09, "fixed_points", "Fixed Points", "concept", "lines 275-304")
t09_attractor = add_node(P09, T09, "attractor_points", "Attractor Points", "concept", "lines 275-304")
t09_repellor = add_node(P09, T09, "repellor_points", "Repellor Points", "concept", "lines 275-304")
t09_path = add_node(P09, T09, "path_dependent_process", "Path-Dependent Process", "rationale", "lines 285-308", "The limiting locational pattern depends on the sequence of past choices rather than only on a unique static equilibrium.")
t09_aek = add_node(P09, T09, "strong_law_aek", "Arthur-Ermoliev-Kaniovski Strong Law", "concept", "lines 285-308")
t09_pure = add_node(P09, T09, "pure_attractiveness", "Pure Attractiveness", "concept", "lines 319-336")
t09_unbounded = add_node(P09, T09, "unbounded_agglomeration", "Unbounded Agglomeration Economies", "concept", "lines 338-360")
t09_monopoly = add_node(P09, T09, "monopoly_outcome", "Monopoly Outcome", "concept", "lines 351-360")
t09_lockin = add_node(P09, T09, "lock_in", "Lock-In", "concept", "lines 357-382")
t09_bounded = add_node(P09, T09, "bounded_agglomeration", "Bounded Agglomeration Economies", "concept", "lines 430-448")
t09_upper = add_node(P09, T09, "agglomeration_upper_bound", "Agglomeration Upper Bound", "concept", "lines 430-448")
t09_heterogeneity = add_node(P09, T09, "heterogeneity_of_tastes", "Heterogeneity of Tastes", "concept", "lines 430-448")
t09_sharing = add_node(P09, T09, "regional_sharing", "Regional Sharing", "concept", "lines 430-448")
t09_potential_lockin = add_node(P09, T09, "potential_lock_in_set", "Potential Lock-In Set", "concept", "lines 449-467")
t09_dominant_set = add_node(P09, T09, "potentially_dominant_set", "Potentially Dominant Set", "concept", "lines 449-467")
t09_ceiling = add_node(P09, T09, "agglomeration_ceiling", "Agglomeration Ceiling", "concept", "lines 482-506")
t09_shadow = add_node(P09, T09, "agglomeration_shadow", "Agglomeration Shadow", "rationale", "lines 563-598", "A populated location can dynamically orphan nearby locations by making its geographical neighbours unable to overcome its agglomeration advantage.")
t09_orphaning = add_node(P09, T09, "locational_orphaning", "Locational Orphaning", "concept", "lines 563-598")
t09_gravity = add_node(P09, T09, "gravitational_region", "Gravitational Region", "concept", "lines 591-595")
t09_separation = add_node(P09, T09, "spatial_separation", "Spatial Separation", "concept", "lines 563-598")
t09_sequence_linkage = add_node(P09, T09, "sequence_linkage", "Sequence Linkage", "concept", "lines 641-652")
t09_relocation = add_node(P09, T09, "moving_and_relocation", "Moving and Relocation", "concept", "lines 632-640")
t09_expectations = add_node(P09, T09, "expectations", "Expectations", "concept", "lines 653-662")
t09_exclusion = add_node(P09, T09, "competitive_exclusion", "Competitive Exclusion", "concept", "lines 676-683")
t09_selection = add_node(P09, T09, "selectional_advantage", "Selectional Advantage", "concept", "lines 676-683")
t09_product_standard = add_node(P09, T09, "product_and_standard_network_effects", "Product and Standard Network Effects", "concept", "lines 684-695")

add_edge(t09_paper, t09_author, "references", "EXTRACTED", 1.0, T09, "lines 33-43")
add_edge(t09_increasing, t09_agglomeration, "references", "EXTRACTED", 1.0, T09, "lines 46-64")
add_edge(t09_network, t09_increasing, "conceptually_related_to", "EXTRACTED", 1.0, T09, "lines 68-78")
add_edge(t09_agglomeration, t09_benefits, "rationale_for", "EXTRACTED", 1.0, T09, "lines 134-149")
add_edge(t09_diseconomies, t09_agglomeration, "conceptually_related_to", "EXTRACTED", 1.0, T09, "lines 136-149")
add_edge(t09_geography, t09_locations, "rationale_for", "EXTRACTED", 1.0, T09, "lines 147-156")
add_edge(t09_history, t09_entry, "rationale_for", "EXTRACTED", 1.0, T09, "lines 169-183")
add_edge(t09_firms, t09_tastes, "rationale_for", "EXTRACTED", 1.0, T09, "lines 157-183")
add_edge(t09_distribution, t09_probability, "rationale_for", "EXTRACTED", 1.0, T09, "lines 169-203")
add_edge(t09_probability, t09_shares, "rationale_for", "EXTRACTED", 1.0, T09, "lines 188-228")
add_edge(t09_shares, t09_stochastic, "rationale_for", "EXTRACTED", 1.0, T09, "lines 217-247")
add_edge(t09_expected, t09_shares, "rationale_for", "EXTRACTED", 1.0, T09, "lines 248-263")
add_edge(t09_perturbation, t09_shares, "rationale_for", "EXTRACTED", 1.0, T09, "lines 257-263")
add_edge(t09_fixed, t09_attractor, "references", "EXTRACTED", 1.0, T09, "lines 275-304")
add_edge(t09_fixed, t09_repellor, "references", "EXTRACTED", 1.0, T09, "lines 275-304")
add_edge(t09_path, t09_history, "rationale_for", "EXTRACTED", 1.0, T09, "lines 285-308")
add_edge(t09_aek, t09_path, "rationale_for", "EXTRACTED", 1.0, T09, "lines 285-308")
add_edge(t09_pure, t09_geography, "rationale_for", "EXTRACTED", 1.0, T09, "lines 319-336")
add_edge(t09_pure, t09_agglomeration, "conceptually_related_to", "EXTRACTED", 1.0, T09, "lines 319-336")
add_edge(t09_unbounded, t09_monopoly, "rationale_for", "EXTRACTED", 1.0, T09, "lines 338-360")
add_edge(t09_unbounded, t09_lockin, "rationale_for", "EXTRACTED", 1.0, T09, "lines 357-382")
add_edge(t09_monopoly, t09_lockin, "rationale_for", "EXTRACTED", 1.0, T09, "lines 357-382")
add_edge(t09_bounded, t09_upper, "rationale_for", "EXTRACTED", 1.0, T09, "lines 430-448")
add_edge(t09_bounded, t09_heterogeneity, "rationale_for", "EXTRACTED", 1.0, T09, "lines 430-448")
add_edge(t09_bounded, t09_sharing, "rationale_for", "EXTRACTED", 1.0, T09, "lines 430-448")
add_edge(t09_potential_lockin, t09_dominant_set, "conceptually_related_to", "EXTRACTED", 1.0, T09, "lines 449-467")
add_edge(t09_dominant_set, t09_lockin, "rationale_for", "EXTRACTED", 1.0, T09, "lines 482-506")
add_edge(t09_ceiling, t09_sharing, "rationale_for", "EXTRACTED", 1.0, T09, "lines 490-506")
add_edge(t09_shadow, t09_orphaning, "rationale_for", "EXTRACTED", 1.0, T09, "lines 563-598")
add_edge(t09_shadow, t09_gravity, "rationale_for", "EXTRACTED", 1.0, T09, "lines 591-595")
add_edge(t09_shadow, t09_separation, "rationale_for", "EXTRACTED", 1.0, T09, "lines 570-598")
add_edge(t09_sequence_linkage, t09_path, "rationale_for", "EXTRACTED", 1.0, T09, "lines 641-652")
add_edge(t09_relocation, t09_path, "rationale_for", "EXTRACTED", 1.0, T09, "lines 632-640")
add_edge(t09_expectations, t09_monopoly, "rationale_for", "EXTRACTED", 1.0, T09, "lines 653-662")
add_edge(t09_exclusion, t09_lockin, "rationale_for", "EXTRACTED", 1.0, T09, "lines 676-683")
add_edge(t09_selection, t09_history, "rationale_for", "EXTRACTED", 1.0, T09, "lines 676-683")
add_edge(t09_product_standard, t09_network, "rationale_for", "EXTRACTED", 1.0, T09, "lines 684-695")
add_edge(t09_paper, EXT_T05, "cites", "EXTRACTED", 1.0, T09, "lines 117-125")
add_edge(t09_paper, EXT_T17, "cites", "EXTRACTED", 1.0, T09, "lines 117-125")


# Cross-source connections are limited to explicit citations or strong, reviewable
# semantic correspondences in this chunk. They remain INFERRED, not evidence.
add_edge(m14_work, m16_transformation, "semantically_similar_to", "INFERRED", 0.85, M14, "lines 179-188")
add_edge(m14_frame, m16_frames, "semantically_similar_to", "INFERRED", 0.85, M14, "lines 658-728")
add_edge(z_core, t09_lockin, "semantically_similar_to", "INFERRED", 0.65, Z03, "lines 694-713")
add_edge(t09_shadow, z_dominance, "semantically_similar_to", "INFERRED", 0.65, T09, "lines 570-598")


hyperedges.extend(
    [
        {
            "id": "z03_polarized_development_mechanism",
            "label": "Polarized Development Mechanism",
            "nodes": [z_dev_innovation, z_comm_field, z_core, z_periphery, z_authority_dependency],
            "relation": "form",
            "confidence": "EXTRACTED",
            "confidence_score": 1.0,
            "source_file": Z03,
        },
        {
            "id": "t09_path_dependent_agglomeration_mechanism",
            "label": "Path-Dependent Agglomeration Mechanism",
            "nodes": [t09_history, t09_agglomeration, t09_probability, t09_path, t09_lockin, t09_shadow],
            "relation": "form",
            "confidence": "EXTRACTED",
            "confidence_score": 1.0,
            "source_file": T09,
        },
        {
            "id": "m16_governance_transformation_dynamics",
            "label": "Governance Transformation Dynamics",
            "nodes": [m16_episodes, m16_processes, m16_cultural, m16_capacity, m16_actor_capacity],
            "relation": "form",
            "confidence": "EXTRACTED",
            "confidence_score": 1.0,
            "source_file": M16,
        },
    ]
)

fragment = {
    "nodes": nodes,
    "edges": edges,
    "hyperedges": hyperedges,
    "input_tokens": 0,
    "output_tokens": 0,
}
TARGET.write_text(json.dumps(fragment, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("chunk_09: {} nodes, {} edges, {} hyperedges".format(len(nodes), len(edges), len(hyperedges)))
