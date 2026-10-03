---
source_type: dataset
title: "2025 Peta Kawasan Industri Eksisting Skala 1:50.000 — Data Dukung Kawasan Industri 125 KI"
creators: ["Kementerian Perindustrian, Direktorat Perwilayahan Industri"]
year: 2025
identifier: "satudata.kemenperin.go.id dataset bc2efe8c-1103-446a-8c68-99db09dd1018"
url: "https://satudata.kemenperin.go.id/dataset/2025-peta-kawasan-industri-eksisting-skala-1-50-000"
date_accessed: 2026-09-27
access_basis: raw-data
publisher: "Kementerian Perindustrian (Satu Data Kemenperin)"
version: null
release_date: null
license: null
spatial_coverage: "Indonesia; 125 kawasan industri, 31 record di unit Jabodetabek"
temporal_coverage: "2025 (menurut judul dataset)"
unit_of_observation: "Poligon kawasan industri; satu kawasan dapat terdiri atas beberapa record"
data_format: "ESRI Shapefile (dalam ZIP); XLSX metadata"
raw_files:
  - "data_dukung_kawasan_industri_125_ki.zip"
  - "1743.xlsx"
checksum: "sha256 zip bf4085c8ee8afbd8e57672203d178c8b3ecc01447d3599afe8d6f06917d5c22e; sha256 xlsx 1fa861195b2614d3e4e95aba1a198938e524d388b6f08631b713299da29b7cb7"
---

# Peta Kawasan Industri Eksisting 2025 — Data Dukung 125 KI

## Dataset Description

Poligon kawasan industri dari Satu Data Kemenperin. Isi ZIP adalah `Data Dukung Kawasan Industri - 125 KI/Data_Kawasan_Industri_125KI.shp` beserta `.dbf`, `.prj`, `.shx`, `.cpg`, `.sbn`, dan `.sbx` (berstempel 2026-04-20). `1743.xlsx` berisi lembar metadata indikator: produsen "Direktorat Perwilayahan Industri", jenis "peta", skala "1:50.000", dengan rujukan regulasi "Permenko Ekon 3/2024; SK KaBIG 16/2023; Kepka BIG 130/2025".

## Variables or Schema

Kolom DBF (hasil baca agen):

| Kolom | Isi | Catatan |
|---|---|---|
| `ID_KI` | Nomor kawasan | Bisa berupa rentang, misalnya "20 - 22" |
| `FCODE` | Kode fitur | Misalnya `GC03050020` |
| `NAMOBJ` | Nama kawasan | |
| `PENGELOLA` | Nama pengelola | |
| `Kab_Kota` | Kabupaten/kota | |
| `Provinsi` | Provinsi | Tertulis "Daerah Khusus Jakarta" untuk DKI |
| `Luas_IUKI` | Luas | Desimal koma; **satuan tidak didokumentasikan**, kemungkinan hektare |

## Coverage and Unit of Observation

- 153 record untuk 125 kawasan.
- 31 record memuat nama unit Jabodetabek. Satu di antaranya harus dikeluarkan: Kawasan Industri Cikembar di Kabupaten Sukabumi, yang cocok hanya karena nama pengelolanya memuat "Bogor".
- Contoh kawasan di Jabodetabek: Pulogadung, KBN Cakung, MM2100, Jababeka, GIIC, Lippo Cikarang, EJIP, Millennium, Cikupamas, dan Taman Tekno BSD.
- CRS menurut `.prj`: GCS WGS 1984.

- **Ringkasan Jabodetabek (dihitung agen 2 Oktober 2026 dari DBF; Cikembar dikeluarkan):** 30 record dengan 21 nama kawasan unik. Kabupaten Bekasi 19 record (10 nama; jumlah `Luas_IUKI` 6.419,6); Kabupaten Tangerang 6 (6; 1.724,3); Kabupaten Bogor 2 (2; 316,7); Kota Jakarta Timur 1 (433,0); Kota Jakarta Utara 1 (177,0); Kota Tangerang Selatan 1 (160,0). Tidak ada record untuk Kota Bogor, Kota Depok, Kota Bekasi, dan Kota Tangerang. Satuan luas tidak didokumentasikan (kemungkinan hektare), dan record berganda per kawasan dijumlahkan apa adanya.

- **Satuan `Luas_IUKI` (diperiksa 3 Oktober 2026).** Luas poligon dihitung agen dari geometri `.shp` (pendekatan planar lokal pada WGS84) lalu dibandingkan dengan `Luas_IUKI`. Kawasan berpoligon tunggal cocok dalam hektare: KBN Cakung 177 vs 176,4 ha; Cibinong Center 96,68 vs 95,3 ha; EJIP 320 vs 332,0 ha; Taman Industri Busan 29,47 vs 29,4 ha; kawasan di Tangerang Selatan 160 vs 156,5 ha. Jadi `Luas_IUKI` **kemungkinan besar dalam hektare** dan mencerminkan luas izin usaha kawasan industri (IUKI). Untuk kawasan besar, poligon jauh lebih luas daripada izin (Jababeka 1.285,97 vs ±4.463 ha; Lippo Cikarang 390 vs ±2.616 ha; MM2100 BFIE 829 vs ±3.001 ha). Untuk masker volume nonhunian di luar kawasan industri (keputusan D3), yang dipakai adalah **poligon**, bukan `Luas_IUKI`.
- **Hitungan baku untuk naskah:** 30 record untuk 21 kawasan unik di Jabodetabek; 19 kawasan di luar DKI (Kabupaten Bekasi 10, Kabupaten Tangerang 6, Kabupaten Bogor 2, Kota Tangerang Selatan 1).

## Collection or Production Method

Tidak didokumentasikan dalam berkas yang diperiksa. Judul dataset menyebut skala 1:50.000.

## Known Limitations

- Hanya memuat kawasan industri formal yang terdaftar (125 KI). Kawasan industri lain atau zona industri di luar KI tidak tercakup.
- Satu kawasan dapat terpecah menjadi beberapa record.
- Tidak memuat tenant, tenaga kerja, atau okupansi.
- Lisensi pakai ulang tidak tercantum pada berkas.

## Raw File Inventory

- `data_dukung_kawasan_industri_125_ki.zip` (731.294 byte)
- `1743.xlsx` (24.518 byte)

## Provenance Notes

- **Tautan unduh** (diakses 2026-09-27): `…/resource/88ec537e-60ac-4a66-bed5-2b04c9758219/download/data_dukung_kawasan_industri_125_ki.zip` dan `…/resource/1a16c565-8d24-4b86-98d3-1fd306891ce5/download/1743.xlsx`.
- **Peran dalam TA:** komponen pembeda proksi pekerjaan dan kontrol $Z$ (C6/C10 evaluasi).
