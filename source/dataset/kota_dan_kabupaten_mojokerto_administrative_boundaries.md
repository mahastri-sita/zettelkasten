---
source_type: dataset
title: "Administrative Boundaries for Kota and Kabupaten Mojokerto"
creators: []
year: null
identifier: null
url: null
date_accessed: "2026-08-23"
access_basis: raw-data
publisher: null
version: null
release_date: null
license: null
spatial_coverage: "Kota Mojokerto dan Kabupaten Mojokerto, Jawa Timur"
temporal_coverage: null
unit_of_observation: "administrative boundary feature"
data_format: "GeoJSON and QGIS metadata, projected and lon/lat variants"
raw_files:
  - "source/dataset/ec_info_adm_kota_mjk.geojson"
  - "source/dataset/ec_info_adm_kota_mjk_wgs84.geojson"
  - "source/dataset/ec_info_adm_kota_mjk.qmd"
  - "source/dataset/ec_info_adm_kab_mjk.geojson"
  - "source/dataset/ec_info_adm_kab_mjk_wgs84.geojson"
  - "source/dataset/ec_info_adm_kab_mjk.qmd"
checksum: null
---

# Administrative Boundaries for Kota and Kabupaten Mojokerto

## Dataset Description

Snapshot boundary administrasi Kota Mojokerto dan Kabupaten Mojokerto dari corpus Enclave City. Varian projected, varian lon/lat, dan metadata QGIS dipertahankan sebagai file terpisah.

## Variables or Schema

- GeoJSON memuat feature boundary dan properties administrasi sesuai file legacy.
- File `.qmd` memuat metadata CRS QGIS.

## Coverage and Unit of Observation

- Cakupan spasial: Kota Mojokerto dan Kabupaten Mojokerto, Jawa Timur.
- Unit observasi: feature batas administrasi.
- Metadata QGIS Kota Mojokerto menyatakan EPSG:32749.
- Metadata QGIS Kabupaten Mojokerto menyatakan EPSG:4326.
- Varian dengan suffix `wgs84` dipertahankan tanpa reprojection atau asumsi tambahan tentang deklarasi CRS.

## Collection or Production Method

File diidentifikasi sebagai boundary administrasi dalam corpus pengguna. Institusi penerbit, tanggal, versi, sumber boundary, dan prosedur delineasi tidak tercatat lengkap dalam metadata legacy.

## Known Limitations

- Kesetaraan geometri antara varian projected dan `wgs84` belum diperiksa secara independen.
- Metadata CRS antarfile tidak seragam dan tidak boleh dinormalisasi tanpa pemeriksaan geometri.
- Tidak ada klaim bahwa boundary ini merupakan boundary resmi terbaru.

## Raw File Inventory

- `source/dataset/ec_info_adm_kota_mjk.geojson`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kota_mjk.geojson`
  - SHA-256: `b715a0ddbe8123c23033393df35548bdfc34d609c715d03eff379c073ff46e3f`
- `source/dataset/ec_info_adm_kota_mjk_wgs84.geojson`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kota_mjk_wgs84.geojson`
  - SHA-256: `6d48f8445efb2271a151e21b52f49c53a575b3f790fded5f75194886dc2ac935`
- `source/dataset/ec_info_adm_kota_mjk.qmd`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kota_mjk.qmd`
  - SHA-256: `b50b48274a47df0e03838fecb42eb8f384bd3bd5b94e9c45adc0e20da0edbc5e`
- `source/dataset/ec_info_adm_kab_mjk.geojson`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kab_mjk.geojson`
  - SHA-256: `f1539f62a77f23780456f1196457e64e9bdc345b27846edd1fc423eb291fd036`
- `source/dataset/ec_info_adm_kab_mjk_wgs84.geojson`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kab_mjk_wgs84.geojson`
  - SHA-256: `82a19110139c51205df432ef0b13d031ab54c328401167073b19b7d670032232`
- `source/dataset/ec_info_adm_kab_mjk.qmd`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kab_mjk.qmd`
  - SHA-256: `955ef5f2f4850a7e5af5a5fadc57140ad5c37d7c2fd043707ce86e0f067fb673`

## Provenance Notes

- Raw snapshots were copied without geometry edits, reprojection, or merge.
- The legacy files remain preserved at their original paths.
- Any later change to the legacy boundary files requires checksum review and an explicit target update.
