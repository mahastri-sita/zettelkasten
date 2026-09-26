---
source_type: dataset
title: "POI Gerbangkertosusila extracted from OpenStreetMap, April 2026"
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
unit_of_observation: "OSM feature"
data_format: "GeoJSON, projected and WGS84 variants"
raw_files:
  - "source/dataset/UC-info-poi-industry.geojson"
  - "source/dataset/UC-info-poi-industry-wgs84.geojson"
checksum: null
---

# POI Gerbangkertosusila extracted from OpenStreetMap, April 2026

## Dataset Description

Snapshot POI Gerbangkertosusila yang diidentifikasi pengguna sebagai ekstraksi OpenStreetMap pada April 2026. Dua file merupakan varian CRS dari corpus yang sama dan disimpan tanpa normalisasi.

## Variables or Schema

Properties yang terlihat mencakup `element`, `id`, `amenity`, `office`, dan `shop`. Struktur lengkap dapat berbeda antarvarian dan belum diaudit per feature.

## Coverage and Unit of Observation

- Cakupan spasial: Gerbangkertosusila.
- Unit observasi: feature POI OpenStreetMap.
- Varian projected menggunakan EPSG:32749; varian lain menggunakan CRS84/WGS84.

## Collection or Production Method

Pengguna mengidentifikasi data sebagai ekstraksi OpenStreetMap pada April 2026. Query, daftar tags, endpoint, aturan filtering, dan prosedur deduplikasi tidak tercatat.

## Known Limitations

- Kedua file adalah varian CRS dan tidak boleh diperlakukan sebagai dua kali jumlah POI.
- Tanggal ekstraksi diketahui pada tingkat bulan, tetapi timestamp dan snapshot source tidak tersedia.
- Kategori POI belum diaudit terhadap kategori primary/secondary dalam Gravity Calculation.
- Lisensi dan URL snapshot tidak tercatat dalam legacy metadata.
- Raw files tetap immutable; perubahan atau recapture memerlukan record versi baru.

## Raw File Inventory

- `source/dataset/UC-info-poi-industry.geojson`
  - Legacy source: `Porto-City-Cannibalism/info/UC-info-poi-industry.geojson`
  - SHA-256: `6396ec59e524f433cd214391f99f06ed37b296060910630486cf72411f47a884`
- `source/dataset/UC-info-poi-industry-wgs84.geojson`
  - Legacy source: `Porto-City-Cannibalism/info/UC-info-poi-industry-wgs84.geojson`
  - SHA-256: `281250613d745a8897777139aeade7a88a466c5da59e52e9a9457ca2d4531991`

## Provenance Notes

- Source and extraction month are based on user confirmation.
- This record does not assert that the POI file is an unmodified direct API response; filtering and reprojection history remain open.
