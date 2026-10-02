---
source_type: dataset
title: "PDRB ADHK Regional Compilation, 2014-2024"
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
spatial_coverage: "Gerbangkertosusila; Kabupaten/Kota Solok; Kota Padang; Jawa Timur; Sumatera Barat; nasional"
temporal_coverage: "2014-2024"
unit_of_observation: "wilayah-tahun-sektor-kategori"
data_format: "CSV, dua varian legacy"
raw_files:
  - "source/dataset/ec_info_bps_new.csv"
  - "source/dataset/uc_info_econ_pdrb.csv"
checksum: null
---

# PDRB ADHK Regional Compilation, 2014-2024

## Dataset Description

Dataset PDRB yang diidentifikasi pengguna sebagai data BPS. Dua file mencakup seri PDRB ADHK sektoral dan total per wilayah untuk periode 2014-2024. Record ini canonical untuk provenance dataset, bukan hasil normalisasi angka.

## Variables or Schema

Kolom utama:

- `Tahun`
- `Wilayah`
- `Sektor`
- `Kategori`
- `Nilai_PDRB`

## Coverage and Unit of Observation

- Cakupan waktu: 2014-2024.
- Cakupan wilayah: Gerbangkertosusila, wilayah Solok, Kota Padang, Jawa Timur, Sumatera Barat, dan nasional sesuai isi file.
- Unit observasi: kombinasi wilayah, tahun, sektor, dan kategori.

## Collection or Production Method

Pengguna mengidentifikasi dataset ini sebagai BPS. Publikasi BPS, URL, versi rilis, satuan resmi, metode ekstraksi, dan lisensi tidak tercatat dalam legacy metadata. Tidak ada transformasi yang dilakukan pada raw file dalam migrasi ini.

## Known Limitations

- `ec_info_bps_new.csv` dan `uc_info_econ_pdrb.csv` diperlakukan sebagai dua varian raw BPS, bukan digabungkan.
- Pada baris total, salah satu varian menggunakan kategori kosong sedangkan varian lain menggunakan `komposit`.
- File `Porto-Enclave-City/info/EC-info-econ.md` adalah olahan pengguna dan tidak diperlakukan sebagai raw Source.
- Handoff legacy `03-Work/MBA-Drafts/handoff-EC-charts.md` melaporkan bahwa `ec_info_bps_new.csv` memiliki masalah pada kolom `Kategori`; laporan tersebut belum diaudit ulang secara independen dalam target. File tetap dipertahankan sebagai snapshot raw immutable, tetapi tidak diperlakukan sebagai tabel kategori yang aman untuk analisis tanpa rekonsiliasi.
- Nilai, satuan, definisi kategori, dan kesesuaian dengan publikasi BPS belum diverifikasi secara independen.
- Raw files disalin sebagai snapshot immutable ke `source/dataset/`; file legacy tetap dipertahankan sebagai provenance asal.

## Raw File Inventory

- `source/dataset/ec_info_bps_new.csv`
  - Legacy source: `Porto-Enclave-City/info/ec_info_bps_new.csv`
  - SHA-256: `e651a38dfb131da598900d76b9a2a063c005f7bf031e72fb1d9934106239e180`
- `source/dataset/uc_info_econ_pdrb.csv`
  - Legacy source: `Porto-City-Cannibalism/info/uc_info_econ_pdrb.csv`
  - SHA-256: `51266297f8914b4db9f7515428fcd247264f205c2d47bb469957c1af076a804d`

## Provenance Notes

- Provenance source: user confirmation that both files are BPS data.
- The legacy index `Porto-Enclave-City/info/EC-info-data.md` labels the underlying economic master sheet as `econ-mastersheet-bps`.
- Derived and user-processed files are intentionally not listed as raw files.
- Target copies are snapshots; later changes to legacy files require checksum review and an explicit update.
