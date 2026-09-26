---
source_type: dataset
title: "Population of Solok and Mojokerto, 2010-2025"
creators:
  - "BPS"
year: null
identifier: null
url: null
date_accessed: null
access_basis: raw-data
publisher: "BPS"
version: null
release_date: null
license: null
spatial_coverage: "Kota Solok; Kabupaten Solok; Kota Mojokerto; Kabupaten Mojokerto"
temporal_coverage: "2010-2025"
unit_of_observation: "wilayah-tahun"
data_format: "Markdown table"
raw_files:
  - "source/dataset/EC-info-population.md"
checksum: "7b5f5167706ddc8cbfc8c9f9645d2abfff957c26ea644c24dc617f5f4d21e605"
---

# Population of Solok and Mojokerto, 2010-2025

## Dataset Description

Dataset populasi yang diidentifikasi pengguna sebagai data BPS untuk Kota/Kabupaten Solok dan Kota/Kabupaten Mojokerto. File memuat seri tahunan 2010-2025.

## Variables or Schema

- `Wilayah`
- `Tahun`
- `Populasi`

Nilai populasi ditulis sebagai angka dengan pemisah ribuan dalam string CSV-like pada tabel legacy.

## Coverage and Unit of Observation

- Cakupan waktu: 2010-2025.
- Cakupan wilayah: empat wilayah Solok dan Mojokerto.
- Unit observasi: satu wilayah pada satu tahun.

## Collection or Production Method

Pengguna mengidentifikasi file sebagai BPS. Publikasi, URL, versi rilis, definisi populasi, metode sensus atau proyeksi, satuan resmi, dan lisensi tidak tercatat dalam legacy metadata.

## Known Limitations

- Format angka belum dinormalisasi dan tidak boleh diubah dalam raw Source.
- Perubahan tajam antarperiode belum diperiksa terhadap publikasi asal.
- File raw disalin sebagai snapshot immutable ke `source/dataset/`; file legacy tetap dipertahankan sebagai provenance asal.

## Raw File Inventory

- `source/dataset/EC-info-population.md`
  - Legacy source: `Porto-Enclave-City/info/EC-info-population.md`
  - SHA-256: `7b5f5167706ddc8cbfc8c9f9645d2abfff957c26ea644c24dc617f5f4d21e605`

## Provenance Notes

- Provenance source: user confirmation bahwa file ini adalah data BPS.
- Legacy index `Porto-Enclave-City/info/EC-info-data.md` menyebut pasangan data populasi Solok dan Mojokerto sebagai `penduduk-slk-mjk`.
- Target copy adalah snapshot; perubahan pada legacy file memerlukan review checksum dan update eksplisit.
