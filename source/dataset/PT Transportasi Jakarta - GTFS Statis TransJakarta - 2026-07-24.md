---
source_type: dataset
title: "GTFS statis TransJakarta"
creators: ["PT Transportasi Jakarta"]
year: 2026
identifier: null
url: "https://gtfs.transjakarta.co.id/files/file_gtfs.zip"
date_accessed: 2026-09-27
access_basis: raw-data
publisher: "PT Transportasi Jakarta"
version: "Berkas di dalam ZIP berstempel 2026-07-24"
release_date: null
license: null
spatial_coverage: "Jaringan layanan TransJakarta"
temporal_coverage: "Jadwal yang berlaku pada versi feed; periode kalender belum dibaca"
unit_of_observation: "Halte, rute, perjalanan, dan waktu henti terjadwal"
data_format: "GTFS (ZIP berisi berkas teks CSV)"
raw_files:
  - "transjakarta_file_gtfs_2026-09-27.zip"
checksum: "sha256 63b4fb14d9afa7fd21737fee57991366b3f61746af12479725cc17d0cf64fb22"
---

# GTFS statis TransJakarta

## Dataset Description

Feed GTFS statis resmi TransJakarta, berisi jadwal dan jaringan layanan terjadwal.

## Variables or Schema

- **Berkas dalam ZIP:** `agency.txt`, `calendar.txt`, `fare_attributes.txt`, `fare_rules.txt`, `frequencies.txt`, `routes.txt`, `shapes.txt`, `stops.txt`, `stop_times.txt`, `ticketing_deep_links.txt`, `ticketing_identifiers.txt`, `transfers.txt`, `trips.txt`.
- Isi kolom belum dibaca. Struktur mengikuti spesifikasi GTFS, tetapi kolom tambahan belum diperiksa.

## Coverage and Unit of Observation

Hanya layanan TransJakarta. Tidak mencakup KRL, MRT, LRT Jabodebek, maupun angkutan Bodetabek lain.

## Collection or Production Method

Tidak didokumentasikan dalam berkas.

## Known Limitations

- Jadwal, bukan transaksi, jumlah penumpang, atau arus asal-tujuan.
- Waktu tempuh terjadwal tidak mencerminkan kemacetan aktual.
- Lisensi pakai ulang belum dikonfirmasi; catatan audit 24 Agustus 2026 juga menyatakan demikian.

## Raw File Inventory

`transjakarta_file_gtfs_2026-09-27.zip` (2.497.332 byte). Nama asli berkas adalah `file_gtfs.zip`, diganti dengan menambahkan operator dan tanggal unduh agar tidak ambigu.

## Provenance Notes

- Diunduh 2026-09-27.
- **Peran dalam TA:** aksesibilitas angkutan umum terjadwal (manfaat dan beban potensial) dan peta jaringan eksisting Bab 4.
