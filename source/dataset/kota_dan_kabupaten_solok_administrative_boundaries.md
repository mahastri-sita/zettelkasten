---
source_type: dataset
title: "Administrative Boundaries for Kota and Kabupaten Solok"
creators: []
year: null
identifier: null
url: null
date_accessed: null
access_basis: raw-data
publisher: null
version: null
release_date: null
license: null
spatial_coverage: "Kota Solok dan Kabupaten Solok, Sumatera Barat"
temporal_coverage: null
unit_of_observation: "administrative boundary feature"
data_format: "GeoJSON and QGIS metadata, projected and lon/lat variants"
raw_files:
  - "source/dataset/ec_info_adm_kota_slk.geojson"
  - "source/dataset/ec_info_adm_kota_slk.qmd"
  - "source/dataset/ec_info_adm_kab_slk.geojson"
  - "source/dataset/ec_info_adm_kab_slk.qmd"
  - "source/dataset/ec_info_adm_kota_slk_wgs84.geojson"
  - "source/dataset/ec_info_adm_kab_slk_wgs84.geojson"
checksum: null
---

# Administrative Boundaries for Kota and Kabupaten Solok

## Dataset Description

Boundary administrasi Kota Solok dan Kabupaten Solok untuk corpus EC. Dataset memiliki varian projected dan varian lon/lat yang dipertahankan sebagai raw files terpisah.

## Variables or Schema

- Varian projected memuat properties administrasi seperti `NAMOBJ`, `WADMKK`, `WADMPR`, `LCODE`, `SHAPE_Leng`, dan `SHAPE_Area`.
- Varian lon/lat memuat properties sederhana `name`.
- File `.qmd` menyimpan metadata CRS QGIS, dengan kelengkapan berbeda antarfile.

## Coverage and Unit of Observation

- Cakupan spasial: Kota Solok dan Kabupaten Solok, Sumatera Barat.
- Unit observasi: feature batas administrasi.
- Projected GeoJSON menyatakan EPSG:32747.
- Varian dengan suffix `wgs84` memuat koordinat lon/lat tetapi tidak mendeklarasikan CRS pada GeoJSON.

## Collection or Production Method

Pengguna mengidentifikasi boundary EC/Solok sebagai authoritative untuk corpus tersebut. Institusi penerbit, tanggal, versi, sumber boundary, dan prosedur delineasi tidak tercatat lengkap dalam legacy metadata. Tidak ada reprojection atau merge yang dilakukan dalam migrasi.

## Known Limitations

- Dua varian `wgs84` tidak memiliki deklarasi CRS eksplisit; suffix filename dan bentuk koordinat menjadi petunjuk, bukan verifikasi formal.
- `ec_info_adm_kota_slk.qmd` menyatakan EPSG:32747 tetapi metadata identitas dan extent kosong.
- `ec_info_adm_kab_slk.qmd` tidak memiliki CRS yang terisi.
- Varian projected dan lon/lat tidak boleh diperlakukan sebagai dua boundary berbeda tanpa pemeriksaan geometri.
- Boundary Mojokerto, GKS, dan land-cover Solok tidak termasuk dalam record ini.

## Raw File Inventory

- `source/dataset/ec_info_adm_kota_slk.geojson`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kota_slk.geojson`
  - SHA-256: `6897284b6dd040ff2d5800a4c4559e0d1b4bd86f2e8c62109306f3fd4d9f8eec`
- `source/dataset/ec_info_adm_kota_slk.qmd`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kota_slk.qmd`
  - SHA-256: `0eab8a229b8bfc7b3d6a054bc1863305c33bc0a33a6994b4315a78f827d11986`
- `source/dataset/ec_info_adm_kab_slk.geojson`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kab_slk.geojson`
  - SHA-256: `a47ecabb72874e86d2a66bc1e86f3b69042d850de2cf3c6f858664d9509dc912`
- `source/dataset/ec_info_adm_kab_slk.qmd`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kab_slk.qmd`
  - SHA-256: `61d70b15a81dee393825e72641cf4490bd60c754386e40d4dbb204bbef66518a`
- `source/dataset/ec_info_adm_kota_slk_wgs84.geojson`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kota_slk_wgs84.geojson`
  - SHA-256: `02da838d81cb73e43877e4f5c2cbe93b57d029824bf4ce93d2bc6a23547f36a6`
- `source/dataset/ec_info_adm_kab_slk_wgs84.geojson`
  - Legacy source: `Porto-Enclave-City/info/ec_info_adm_kab_slk_wgs84.geojson`
  - SHA-256: `e802357c5bc417b2cd7f83294e5cab3b0308179a45201157a80701022b08b5e8`

## Provenance Notes

- Authority and corpus scope are based on user confirmation.
- Raw snapshots are preserved without reprojection or geometry edits.
- Changes to legacy files require checksum review and an explicit update of the target snapshot.
