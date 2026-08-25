---
source_type: dataset
title: "Railway Network in Gerbangkertosusila from OpenStreetMap, April 2026"
creators:
  - "OpenStreetMap"
year: 2026
identifier: null
url: null
date_accessed: null
access_basis: raw-data
publisher: "OpenStreetMap"
version: "April 2026 extraction"
release_date: null
license: null
spatial_coverage: "Gerbangkertosusila"
temporal_coverage: "April 2026 extraction"
unit_of_observation: "OSM railway feature"
data_format: "GeoJSON"
raw_files:
  - "source/dataset/UC-info-rel-ka.geojson"
checksum: "fd7d42bf8eebe3d33b034fe7d44ab7372509a58c904f39cb3e237a95aaa98e9a"
---

# Railway Network in Gerbangkertosusila from OpenStreetMap, April 2026

## Dataset Description

Snapshot jaringan rel Gerbangkertosusila yang diidentifikasi pengguna sebagai data OpenStreetMap dari April 2026.

## Variables or Schema

Properties yang terlihat mencakup `osm_id`, `code`, `fclass`, dan `name`. Geometry berupa `MultiLineString` dan CRS file adalah CRS84/WGS84.

## Coverage and Unit of Observation

- Cakupan spasial: Gerbangkertosusila.
- Unit observasi: feature jaringan rel OpenStreetMap.
- CRS: CRS84/WGS84 sesuai GeoJSON.

## Collection or Production Method

Pengguna mengidentifikasi data sebagai ekstraksi OpenStreetMap pada April 2026. Query, filter `fclass`, endpoint, dan aturan pemilihan segmen tidak tercatat.

## Known Limitations

- Tidak ada timestamp ekstraksi atau URL snapshot.
- Tidak ada pemeriksaan konektivitas, duplikasi, atau kelengkapan jaringan.
- Raw file tidak boleh dipakai untuk menyimpulkan kondisi operasional kereta api tanpa Source tambahan.

## Raw File Inventory

- `source/dataset/UC-info-rel-ka.geojson`
  - Legacy source: `Porto-City-Cannibalism/info/UC-info-rel-ka.geojson`
  - SHA-256: `fd7d42bf8eebe3d33b034fe7d44ab7372509a58c904f39cb3e237a95aaa98e9a`

## Provenance Notes

- Source and extraction month are based on user confirmation.
- This record preserves the raw snapshot; no network cleaning or reprojection was performed.
