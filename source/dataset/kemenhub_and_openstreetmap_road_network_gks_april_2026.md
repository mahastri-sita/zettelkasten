---
source_type: dataset
title: "Road Network in Gerbangkertosusila from Kemenhub and OpenStreetMap, April 2026"
creators:
  - "Kementerian Perhubungan"
  - "OpenStreetMap"
year: 2026
identifier: null
url: null
date_accessed: null
access_basis: raw-data
publisher: "Kementerian Perhubungan and OpenStreetMap"
version: "April 2026 composite snapshot"
release_date: null
license: null
spatial_coverage: "Gerbangkertosusila"
temporal_coverage: "April 2026 composite snapshot"
unit_of_observation: "road geometry feature"
data_format: "GeoJSON, CRS84 and EPSG:32749 variants"
raw_files:
  - "source/dataset/uc_info_jalan_arteru.geojson"
  - "source/dataset/uc_info_jalan_mgl.geojson"
  - "source/dataset/uc_info_jalan_tol_gks.geojson"
checksum: null
---

# Road Network in Gerbangkertosusila from Kemenhub and OpenStreetMap, April 2026

## Dataset Description

Composite snapshot jaringan jalan Gerbangkertosusila yang menurut konfirmasi pengguna menggabungkan data resmi Kementerian Perhubungan dengan material yang ditambahkan dari OpenStreetMap.

## Variables or Schema

Ketiga file terutama memuat geometry `LineString` dan atribut `fid`. Atribut sumber, kelas jalan, dan identitas jaringan tidak konsisten antarfile.

## Coverage and Unit of Observation

- Cakupan spasial: Gerbangkertosusila.
- Unit observasi: geometry jalan per feature.
- `uc_info_jalan_arteru.geojson` dan `uc_info_jalan_mgl.geojson` menggunakan CRS84/WGS84; `uc_info_jalan_tol_gks.geojson` menggunakan EPSG:32749.

## Collection or Production Method

Pengguna mengidentifikasi dataset sebagai data resmi Kementerian Perhubungan yang telah diperkaya dengan material OpenStreetMap pada April 2026. Per feature, bagian mana berasal dari masing-masing sumber belum terdokumentasi.

## Known Limitations

- Ini adalah composite dataset, bukan satu sumber homogen.
- Tidak ada tanggal rilis Kementerian Perhubungan, URL, lisensi, atau aturan penambahan OSM.
- Perbedaan CRS dan atribut membuat ketiga file tidak boleh digabung tanpa prosedur eksplisit.
- Tidak ada validasi topologi, konektivitas, nama jalan, atau hierarki jalan.
- Raw files tetap immutable; proses harmonisasi harus dicatat dalam Calculation terpisah.

## Raw File Inventory

- `source/dataset/uc_info_jalan_arteru.geojson`
  - Legacy source: `Porto-City-Cannibalism/info/uc_info_jalan_arteru.geojson`
  - SHA-256: `528db44a14b6b3ed1dc58931a75542e7433eb6aaf984cc21ee8947b594e9f603`
- `source/dataset/uc_info_jalan_mgl.geojson`
  - Legacy source: `Porto-City-Cannibalism/info/uc_info_jalan_mgl.geojson`
  - SHA-256: `1997c0cd9b54178f2b6dc87f47cfde195547956d5ba90aaf1ebcb3b0e288f7a5`
- `source/dataset/uc_info_jalan_tol_gks.geojson`
  - Legacy source: `Porto-City-Cannibalism/info/uc_info_jalan_tol_gks.geojson`
  - SHA-256: `e2f7b02797fb75379f267c2320e1c4728ec235aa7e7aef998be7b37dc41783a4`

## Provenance Notes

- Composite provenance and extraction month are based on user confirmation.
- This record does not infer which feature came from Kementerian Perhubungan or OpenStreetMap.
