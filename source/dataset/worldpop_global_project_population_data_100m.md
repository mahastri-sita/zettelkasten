---
source_type: dataset
title: "WorldPop Global Project Population Data: Estimated Residential Population per 100x100m Grid Square"
creators:
  - "WorldPop"
year: null
identifier: "WorldPop/GP/100m/pop"
url: "https://developers.google.com/earth-engine/datasets/catalog/WorldPop_GP_100m_pop"
date_accessed: 2026-08-24
access_basis: metadata-only
publisher: "WorldPop"
version: null
release_date: null
license: "Creative Commons Attribution 4.0 International"
spatial_coverage: "Global"
temporal_coverage: "2000-2021"
unit_of_observation: "100x100m grid cell; catalog pixel size 92.77 meters"
data_format: "Google Earth Engine ImageCollection"
raw_files: []
checksum: null
---

# WorldPop Global Project Population Data: Estimated Residential Population per 100x100m Grid Square

## Dataset Description

The Earth Engine catalog describes a global population-distribution dataset providing the estimated number of residents in each grid cell. The catalog identifies the collection as `WorldPop/GP/100m/pop` and lists availability from 2000 to 2021.

## Variables or Schema

- `population`: estimated number of people residing in each grid cell.
- Image properties: `country` and `year`.
- Catalog pixel size: 92.77 meters.

## Coverage and Unit of Observation

- Spatial coverage: global.
- Temporal coverage: 2000-2021 according to the catalog availability range.
- Unit of observation: raster grid cell.

## Collection or Production Method

The catalog states that census-based population counts are disaggregated to approximately 100x100m cells using machine-learning methods and a Random Forest-based dasymetric redistribution approach.

## Known Limitations

- This record is based on catalog metadata; the raster values were not accessed or downloaded.
- Values are estimated population counts, not direct observations of residents at the grid-cell level.
- A specific country, year, export, and processing version have not been verified for the project datasets.

## Raw File Inventory

No local raw file. The collection is remote and identified by the Earth Engine asset ID in `identifier`.

## Provenance Notes

- Catalog URL accessed on 2026-08-24.
- The canonical BibTeX key `tatem2017worldpop` now identifies this WorldPop dataset in the Enclave City and Urban Cannibalism reference files. The key is retained so existing `\citep` calls continue to resolve; it no longer identifies the Tatem (2017) article.
