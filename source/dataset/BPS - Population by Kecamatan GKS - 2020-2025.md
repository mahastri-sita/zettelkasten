---
source_type: dataset
title: "Population by Kecamatan in Gerbangkertosusila, 2020-2025"
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
spatial_coverage: "Gerbangkertosusila, tingkat kecamatan sesuai file"
temporal_coverage: "2020, 2023, 2025"
unit_of_observation: "baris kecamatan dengan kolom populasi tahun 2020, 2023, dan 2025"
data_format: "CSV"
raw_files:
  - "source/dataset/UC-info-penduduk.csv"
checksum: "6d6a114701cbfe09abaf0fb305803d64f000f15c68f2e327780157810ee72b49"
---

# Population by Kecamatan in Gerbangkertosusila, 2020-2025

## Dataset Description

Dataset populasi tingkat kecamatan yang diidentifikasi pengguna sebagai data BPS. File berisi populasi untuk 2020, 2023, dan 2025 serta kolom `RRI` dan identitas administrasi.

## Variables or Schema

- `Wilayah`
- `WADMKC`
- `KAB_KOTA`
- `KECAMATAN`
- `RRI`
- `2020`
- `2023`
- `2025`

## Coverage and Unit of Observation

- Cakupan waktu: 2020, 2023, dan 2025.
- Cakupan wilayah: kecamatan dalam Gerbangkertosusila sesuai isi file.
- Unit observasi: satu baris kecamatan dengan tiga kolom populasi tahunan.

## Collection or Production Method

Pengguna mengidentifikasi file sebagai BPS. Publikasi, URL, versi rilis, definisi `RRI`, metode estimasi, satuan, dan lisensi tidak tercatat dalam legacy metadata.

## Known Limitations

- `RRI` disimpan sebagai persentase string, tetapi definisinya belum tersedia.
- Baris `Trowulan` tercatat di bawah `kabupaten_bangkalan`; ini ditandai sebagai anomali dan tidak diperbaiki.
- Nama wilayah dan angka belum divalidasi terhadap batas administrasi atau publikasi BPS.
- File raw disalin sebagai snapshot immutable ke `source/dataset/`; file legacy tetap dipertahankan sebagai provenance asal.

## Raw File Inventory

- `source/dataset/UC-info-penduduk.csv`
  - Legacy source: `Porto-City-Cannibalism/info/UC-info-penduduk.csv`
  - SHA-256: `6d6a114701cbfe09abaf0fb305803d64f000f15c68f2e327780157810ee72b49`

## Provenance Notes

- Provenance source: user confirmation bahwa file ini adalah data BPS.
- Legacy index `Porto-Enclave-City/info/EC-info-data.md` menyebut dataset populasi kecamatan ini sebagai `penduduk-bps`.
- Target copy adalah snapshot; perubahan pada legacy file memerlukan review checksum dan update eksplisit.
