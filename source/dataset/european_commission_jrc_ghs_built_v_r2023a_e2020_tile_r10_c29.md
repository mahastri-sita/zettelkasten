---
source_type: dataset
title: "GHS-BUILT-V R2023A — built-up volume, total dan non-residential (NRES), epoch 2020, 3 arcsec WGS84, tile R10_C29"
creators: ["European Commission, Joint Research Centre (JRC)"]
year: 2023
identifier: "GHS_BUILT_V_E2020_GLOBE_R2023A_4326_3ss_V1_0; GHS_BUILT_V_NRES_E2020_GLOBE_R2023A_4326_3ss_V1_0"
url: "https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_BUILT_V_GLOBE_R2023A/"
date_accessed: 2026-09-27
access_basis: raw-data
publisher: "European Commission, Joint Research Centre"
version: "R2023A V1-0"
release_date: null
license: "CC BY 4.0 (copyright.txt pada direktori produk)"
spatial_coverage: "Tile R10_C29: bujur 99.992–109.992, lintang -0.900 sampai -10.900 (mencakup seluruh Jabodetabek)"
temporal_coverage: "Epoch 2020, hasil interpolasi spasial-temporal; lihat Known Limitations"
unit_of_observation: "Sel raster 3 arcsec (sekitar 90 m)"
data_format: "GeoTIFF (BigTIFF) dalam ZIP, 12000 × 12000 piksel"
raw_files:
  - "ghs_built_v_nres_e2020_globe_r2023a_4326_3ss_v1_0_r10_c29.zip"
  - "ghs_built_v_e2020_globe_r2023a_4326_3ss_v1_0_r10_c29.zip"
checksum: "sha256 NRES 4452df9a295c2042b82c7439da1000116847640c65fb4d0ae6114ae8207d1a98; sha256 total 87c86b6619edc06f99709c54ecce7806c139cc1bd156be5cce20aa17d4464091"
---

# GHS-BUILT-V R2023A, epoch 2020, tile R10_C29

## Dataset Description

Raster volume terbangun Global Human Settlement Layer: volume total dan volume yang dialokasikan ke penggunaan dominan nonhunian (NRES). Setiap ZIP berisi satu GeoTIFF dan `GHSL_Data_Package_2023_light.pdf`.

## Variables or Schema

- Satu band nilai volume terbangun per sel.
- **Satuan dan nilai kosong belum dibaca** dari metadata TIFF maupun dokumen paket data, sehingga belum diasumsikan.

## Coverage and Unit of Observation

- **Georeferensi** (dibaca agen dari tag GeoTIFF): ukuran piksel 0,000833°, 12000 × 12000 piksel, bujur 99,992–109,992, lintang −0,900 sampai −10,900.
- **CRS** menurut nama produk: EPSG:4326.

## Collection or Production Method

Menurut *GHSL Data Package 2023* (bagian Products, GHS-BUILT-S dan GHS-BUILT-V), data 1975–2030 per 5 tahun dibuat melalui **interpolasi spasial-temporal** dari lima koleksi citra teramati:
- Landsat untuk epoch 1975, 1990, 2000, dan 2014;
- komposit Sentinel-2 untuk epoch 2018.

Pembedaan hunian (RES) dan nonhunian (NRES) diturunkan dari klasifikasi citra Sentinel-2.

## Known Limitations

- **Epoch 2020 bukan observasi langsung.** Nilainya hasil interpolasi, dengan observasi terdekat tahun 2018. Epoch 2025 dan 2030 juga turunan model.
- Karena komponen NRES berbasis Sentinel-2 2018, **perubahan NRES antarepoch tidak dapat dibaca sebagai perubahan teramati**.
- Kelas NRES mencakup semua bangunan nonhunian, termasuk rumah sakit, kampus, dan mal, bukan hanya tempat kerja.
- Salah klasifikasi mungkin terjadi di kawasan padat informal.

## Raw File Inventory

- `ghs_built_v_nres_e2020_globe_r2023a_4326_3ss_v1_0_r10_c29.zip` (2.056.942 byte)
- `ghs_built_v_e2020_globe_r2023a_4326_3ss_v1_0_r10_c29.zip` (15.745.765 byte)

## Provenance Notes

- **Asal unduhan** (2026-09-27): subdirektori `GHS_BUILT_V_NRES_E2020_GLOBE_R2023A_4326_3ss/V1-0/tiles/` dan `GHS_BUILT_V_E2020_GLOBE_R2023A_4326_3ss/V1-0/tiles/`. Unduhan tile total sempat terputus dan dilanjutkan dengan `curl -C -`; checksum dihitung setelah selesai.
- **Paket rilis:** direktori `GHS_BUILT_S_GLOBE_R2023A` memuat `GHS_BUILT_S_E2018_GLOBE_R2023A_54009_10` dan `GHS_BUILT_S_NRES_E2018_GLOBE_R2023A_54009_10`, yaitu luas terbangun epoch 2018 resolusi 10 m dalam Mollweide (terverifikasi dari daftar direktori 2026-09-27).
  - Produk ini berupa luas, bukan volume, dan belum diunduh.
  - Dapat dipakai sebagai sensitivitas yang paling dekat dengan observasi.
- **Peran dalam TA:** proksi utama domain pekerjaan (C10 evaluasi) dan massa alternatif (luas atau volume total).
