---
source_type: dataset
title: "Authoritative Administrative Boundary for Gerbangkertosusila"
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
spatial_coverage: "Gerbangkertosusila: Gresik, Bangkalan, Mojokerto, Kota Mojokerto, Kota Surabaya, Sidoarjo, dan Lamongan"
temporal_coverage: null
unit_of_observation: "administrative boundary feature"
data_format: "GeoJSON and QGIS metadata"
raw_files:
  - "source/dataset/UC-info-adm-GKS.geojson"
  - "source/dataset/UC-info-adm-GKS.qmd"
checksum: null
---

# Authoritative Administrative Boundary for Gerbangkertosusila

## Dataset Description

Delineasi administrasi Gerbangkertosusila yang diidentifikasi pengguna sebagai boundary authoritative untuk corpus UC/GKS. Dataset mencakup Gresik, Bangkalan, Mojokerto, Kota Mojokerto, Kota Surabaya, Sidoarjo, dan Lamongan.

## Variables or Schema

GeoJSON properties yang terlihat mencakup nama administrasi, kode wilayah, metadata, luas, dan atribut provenance yang tersedia pada feature. Detail schema lengkap belum diaudit.

## Coverage and Unit of Observation

- Cakupan spasial: Gerbangkertosusila.
- Unit observasi: feature batas administrasi.
- GeoJSON menyatakan EPSG:32749.
- Companion QGIS metadata menyatakan EPSG:4326.

## Collection or Production Method

Authority dan cakupan corpus berasal dari konfirmasi pengguna. Creator, institusi penerbit, tanggal, versi, serta prosedur delineasi tidak tercatat secara cukup dalam legacy metadata. File GeoJSON memuat sebagian field seperti `METADATA`, `UUPP`, dan `SRS_ID`, tetapi itu belum menjadi pengganti provenance lengkap.

## Known Limitations

- CRS GeoJSON dan CRS `.qmd` berbeda; tidak diselesaikan dalam migrasi.
- `.qmd` memiliki extent kosong/tidak valid dan metadata identitas yang kosong.
- GeoJSON memuat path lokal pada sebagian properties; path tersebut bukan stable source URL.
- Boundary ini tidak digabung dengan varian `EC-info-adm-gks*` atau boundary corpus EC/Solok.
- Tidak ada perubahan geometry atau reprojection yang dilakukan.

## Raw File Inventory

- `source/dataset/UC-info-adm-GKS.geojson`
  - Legacy source: `Porto-City-Cannibalism/info/UC-info-adm-GKS.geojson`
  - SHA-256: `c2240d1f3dc3adeeffcfd5cfb1fc06e38e343eac31927e17d88dc1472dd4f565`
- `source/dataset/UC-info-adm-GKS.qmd`
  - Legacy source: `Porto-City-Cannibalism/info/UC-info-adm-GKS.qmd`
  - SHA-256: `ba8b25d41b5024b3c02ecfbeb34d943c5fa5e64b3b4b1edfb2eb8ff04969bb76`

## Provenance Notes

- Authority and corpus scope are based on user confirmation.
- The `EC-info-adm-gks.geojson` file is intentionally excluded because its prefix/content relationship requires a separate corpus audit.
