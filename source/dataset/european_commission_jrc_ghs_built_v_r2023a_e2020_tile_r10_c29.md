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

## Derived Summary per Kecamatan (dihitung agen, 3 Oktober 2026)

Jumlah zonal raster GHS-BUILT-V total dan NRES (epoch 2020, m³ per sel 3 detik busur, EPSG:4326) di dalam poligon kecamatan COD-AB HDX (batas April 2020; seluruh 141 kode cocok dengan kode BPS 2024 di WSM). Sel dihitung bila pusatnya jatuh di dalam poligon (`rasterio.mask`, `all_touched=False`). Volume hunian = total − NRES. "Nonhunian di luar KI" = NRES di luar union poligon Kemenperin 2025 (30 rekaman Jabodetabek). "KI di/sekitar" = kecamatan yang berpotongan atau bersinggungan dengan poligon kawasan industri (20 kecamatan). Skrip disimpan di `latex/figures/scripts/` (bukan objek `calculation/`).

- Total 141 kecamatan: 4.818,6 juta m³; NRES 561,0 juta m³ (11,6%); NRES di luar kawasan industri 437,1 juta m³ (kawasan industri memuat 22,1% NRES).
- Ambang P75 volume hunian: 44.576.052 m³ (P66 34.628.213; P80 47.281.100). Ambang P75 penduduk: 193.899 jiwa.
- Penanda pusat sekunder P75 (penduduk **atau** volume hunian): 43 kecamatan (P+V 29, P saja 7, V saja 7). Korelasi penduduk–volume hunian 0,86.
- Batas: epoch 2020 adalah interpolasi (observasi terdekat 2018); batas kecamatan 2020 dipakai untuk unit 2024 tanpa koreksi pemekaran karena kodenya identik.

| Kode | Kecamatan | Kab/kota | Total (juta m³) | Nonhunian | Hunian | Nonhunian di luar KI | KI di/sekitar | Pusat P75 |
|---|---|---|---|---|---|---|---|---|
| 3201010 | Nanggung | Kabupaten Bogor | 5,53 | 0,00 | 5,53 | 0,00 |  |  |
| 3201020 | Leuwiliang | Kabupaten Bogor | 10,15 | 0,00 | 10,15 | 0,00 |  |  |
| 3201021 | Leuwisadeng | Kabupaten Bogor | 5,65 | 0,09 | 5,56 | 0,09 |  |  |
| 3201030 | Pamijahan | Kabupaten Bogor | 9,75 | 0,01 | 9,74 | 0,01 |  |  |
| 3201040 | Cibungbulang | Kabupaten Bogor | 13,45 | 0,02 | 13,43 | 0,02 |  |  |
| 3201050 | Ciampea | Kabupaten Bogor | 22,13 | 0,07 | 22,06 | 0,07 |  |  |
| 3201051 | Tenjolaya | Kabupaten Bogor | 4,35 | 0,00 | 4,35 | 0,00 |  |  |
| 3201060 | Dramaga | Kabupaten Bogor | 16,64 | 0,09 | 16,55 | 0,09 |  |  |
| 3201070 | Ciomas | Kabupaten Bogor | 27,82 | 0,14 | 27,68 | 0,14 |  |  |
| 3201071 | Tamansari | Kabupaten Bogor | 16,19 | 0,02 | 16,16 | 0,02 |  |  |
| 3201080 | Cijeruk | Kabupaten Bogor | 9,04 | 0,00 | 9,04 | 0,00 |  |  |
| 3201081 | Cigombong | Kabupaten Bogor | 13,10 | 0,06 | 13,05 | 0,06 |  |  |
| 3201090 | Caringin | Kabupaten Bogor | 16,70 | 0,28 | 16,42 | 0,28 |  |  |
| 3201100 | Ciawi | Kabupaten Bogor | 22,02 | 0,57 | 21,44 | 0,57 |  |  |
| 3201110 | Cisarua | Kabupaten Bogor | 30,93 | 0,42 | 30,50 | 0,42 |  |  |
| 3201120 | Megamendung | Kabupaten Bogor | 17,79 | 0,01 | 17,77 | 0,01 |  |  |
| 3201130 | Sukaraja | Kabupaten Bogor | 42,02 | 0,27 | 41,75 | 0,27 |  | P |
| 3201140 | Babakan Madang | Kabupaten Bogor | 29,85 | 4,39 | 25,46 | 2,30 | ya |  |
| 3201150 | Sukamakmur | Kabupaten Bogor | 6,01 | 0,01 | 6,00 | 0,01 |  |  |
| 3201160 | Cariu | Kabupaten Bogor | 6,97 | 0,00 | 6,97 | 0,00 |  |  |
| 3201161 | Tanjungsari | Kabupaten Bogor | 5,60 | 0,00 | 5,60 | 0,00 |  |  |
| 3201170 | Jonggol | Kabupaten Bogor | 26,82 | 0,16 | 26,66 | 0,16 |  |  |
| 3201180 | Cileungsi | Kabupaten Bogor | 103,22 | 16,87 | 86,34 | 16,87 |  | P+V |
| 3201181 | Klapanunggal | Kabupaten Bogor | 41,76 | 7,48 | 34,28 | 7,29 | ya |  |
| 3201190 | Gunung Putri | Kabupaten Bogor | 127,76 | 10,61 | 117,15 | 10,61 |  | P+V |
| 3201200 | Citeureup | Kabupaten Bogor | 69,16 | 15,38 | 53,78 | 14,37 | ya | P+V |
| 3201210 | Cibinong | Kabupaten Bogor | 104,73 | 1,91 | 102,82 | 1,91 |  | P+V |
| 3201220 | Bojong Gede | Kabupaten Bogor | 65,65 | 0,13 | 65,52 | 0,13 |  | P+V |
| 3201221 | Tajur Halang | Kabupaten Bogor | 30,14 | 0,01 | 30,13 | 0,01 |  |  |
| 3201230 | Kemang | Kabupaten Bogor | 22,11 | 0,22 | 21,89 | 0,22 |  |  |
| 3201231 | Rancabungur | Kabupaten Bogor | 4,82 | 0,01 | 4,81 | 0,01 |  |  |
| 3201240 | Parung | Kabupaten Bogor | 27,20 | 0,66 | 26,55 | 0,66 |  |  |
| 3201241 | Ciseeng | Kabupaten Bogor | 17,34 | 0,00 | 17,34 | 0,00 |  |  |
| 3201250 | Gunung Sindur | Kabupaten Bogor | 38,10 | 2,94 | 35,16 | 2,94 |  |  |
| 3201260 | Rumpin | Kabupaten Bogor | 11,89 | 0,04 | 11,85 | 0,04 |  |  |
| 3201270 | Cigudeg | Kabupaten Bogor | 8,87 | 0,01 | 8,87 | 0,01 |  |  |
| 3201271 | Sukajaya | Kabupaten Bogor | 3,27 | 0,01 | 3,26 | 0,01 |  |  |
| 3201280 | Jasinga | Kabupaten Bogor | 6,61 | 0,01 | 6,60 | 0,01 |  |  |
| 3201290 | Tenjo | Kabupaten Bogor | 4,79 | 0,25 | 4,54 | 0,25 |  |  |
| 3201300 | Parung Panjang | Kabupaten Bogor | 18,48 | 0,00 | 18,48 | 0,00 |  |  |
| 3216010 | Setu | Kabupaten Bekasi | 40,21 | 0,14 | 40,07 | 0,14 | ya | P |
| 3216021 | Serang Baru | Kabupaten Bekasi | 34,23 | 1,80 | 32,43 | 0,23 | ya |  |
| 3216022 | Cikarang Pusat | Kabupaten Bekasi | 36,25 | 11,14 | 25,11 | 0,62 | ya |  |
| 3216023 | Cikarang Selatan | Kabupaten Bekasi | 120,24 | 47,30 | 72,94 | 7,54 | ya | V |
| 3216030 | Cibarusah | Kabupaten Bekasi | 15,79 | 0,05 | 15,74 | 0,05 |  |  |
| 3216031 | Bojongmangu | Kabupaten Bekasi | 5,45 | 0,11 | 5,34 | 0,03 | ya |  |
| 3216041 | Cikarang Timur | Kabupaten Bekasi | 26,54 | 4,85 | 21,69 | 3,59 | ya |  |
| 3216050 | Kedungwaringin | Kabupaten Bekasi | 12,26 | 1,56 | 10,70 | 1,56 |  |  |
| 3216061 | Cikarang Utara | Kabupaten Bekasi | 103,90 | 45,83 | 58,07 | 8,70 | ya | P+V |
| 3216062 | Karangbahagia | Kabupaten Bekasi | 18,63 | 0,10 | 18,53 | 0,10 |  |  |
| 3216070 | Cibitung | Kabupaten Bekasi | 44,56 | 0,93 | 43,62 | 0,93 | ya | P |
| 3216071 | Cikarang Barat | Kabupaten Bekasi | 138,20 | 46,93 | 91,27 | 29,93 | ya | P+V |
| 3216081 | Tambun Selatan | Kabupaten Bekasi | 101,99 | 6,04 | 95,95 | 6,04 |  | P+V |
| 3216082 | Tambun Utara | Kabupaten Bekasi | 31,81 | 0,11 | 31,70 | 0,11 |  | P |
| 3216090 | Babelan | Kabupaten Bekasi | 45,38 | 0,93 | 44,45 | 0,93 |  | P |
| 3216100 | Tarumajaya | Kabupaten Bekasi | 31,31 | 6,68 | 24,63 | 3,26 | ya |  |
| 3216110 | Tambelang | Kabupaten Bekasi | 4,98 | 0,02 | 4,96 | 0,02 |  |  |
| 3216111 | Sukawangi | Kabupaten Bekasi | 5,46 | 0,05 | 5,41 | 0,05 |  |  |
| 3216120 | Sukatani | Kabupaten Bekasi | 11,72 | 0,03 | 11,69 | 0,03 |  |  |
| 3216121 | Sukakarya | Kabupaten Bekasi | 5,80 | 0,01 | 5,79 | 0,01 |  |  |
| 3216130 | Pebayuran | Kabupaten Bekasi | 14,57 | 0,08 | 14,49 | 0,08 |  |  |
| 3216140 | Cabangbungin | Kabupaten Bekasi | 6,52 | 0,06 | 6,46 | 0,06 |  |  |
| 3216150 | Muara Gembong | Kabupaten Bekasi | 4,49 | 0,02 | 4,47 | 0,02 |  |  |
| 3271010 | Bogor Selatan | Kota Bogor | 48,21 | 1,63 | 46,58 | 1,63 |  | P+V |
| 3271020 | Bogor Timur | Kota Bogor | 25,84 | 2,96 | 22,88 | 2,96 |  |  |
| 3271030 | Bogor Utara | Kota Bogor | 46,83 | 2,38 | 44,45 | 2,38 |  |  |
| 3271040 | Bogor Tengah | Kota Bogor | 32,05 | 7,27 | 24,78 | 7,27 |  |  |
| 3271050 | Bogor Barat | Kota Bogor | 52,31 | 0,77 | 51,54 | 0,77 |  | P+V |
| 3271060 | Tanah Sareal | Kota Bogor | 50,11 | 1,38 | 48,73 | 1,38 |  | P+V |
| 3275010 | Pondokgede | Kota Bekasi | 60,85 | 3,44 | 57,41 | 3,44 |  | P+V |
| 3275011 | Jatisampurna | Kota Bekasi | 46,03 | 2,92 | 43,11 | 2,92 |  |  |
| 3275012 | Pondokmelati | Kota Bekasi | 34,89 | 1,55 | 33,34 | 1,55 |  |  |
| 3275020 | Jatiasih | Kota Bekasi | 64,14 | 2,52 | 61,62 | 2,52 |  | P+V |
| 3275030 | Bantargebang | Kota Bekasi | 44,56 | 12,76 | 31,80 | 12,76 |  |  |
| 3275031 | Mustikajaya | Kota Bekasi | 59,89 | 1,23 | 58,66 | 1,23 |  | P+V |
| 3275040 | Bekasi Timur | Kota Bekasi | 45,22 | 0,64 | 44,58 | 0,64 |  | P+V |
| 3275041 | Rawalumbu | Kota Bekasi | 54,44 | 7,16 | 47,28 | 7,16 |  | P+V |
| 3275050 | Bekasi Selatan | Kota Bekasi | 52,15 | 6,24 | 45,92 | 6,24 |  | P+V |
| 3275060 | Bekasi Barat | Kota Bekasi | 47,43 | 1,73 | 45,69 | 1,73 |  | P+V |
| 3275061 | Medan Satria | Kota Bekasi | 45,51 | 11,63 | 33,88 | 11,63 |  |  |
| 3275070 | Bekasi Utara | Kota Bekasi | 57,61 | 3,58 | 54,03 | 3,58 |  | P+V |
| 3276010 | Sawangan | Kota Depok | 53,94 | 1,04 | 52,90 | 1,04 |  | P+V |
| 3276011 | Bojongsari | Kota Depok | 40,64 | 2,23 | 38,41 | 2,23 |  |  |
| 3276020 | Pancoran Mas | Kota Depok | 56,14 | 2,91 | 53,22 | 2,91 |  | P+V |
| 3276021 | Cipayung | Kota Depok | 31,08 | 0,13 | 30,95 | 0,13 |  |  |
| 3276030 | Sukmajaya | Kota Depok | 51,85 | 1,21 | 50,64 | 1,21 |  | P+V |
| 3276031 | Cilodong | Kota Depok | 48,45 | 1,46 | 46,98 | 1,46 |  | V |
| 3276040 | Cimanggis | Kota Depok | 68,14 | 3,76 | 64,38 | 3,76 |  | P+V |
| 3276041 | Tapos | Kota Depok | 60,17 | 1,32 | 58,85 | 1,32 |  | P+V |
| 3276050 | Beji | Kota Depok | 46,39 | 3,12 | 43,27 | 3,12 |  |  |
| 3276060 | Limo | Kota Depok | 31,24 | 0,12 | 31,12 | 0,12 |  |  |
| 3276061 | Cinere | Kota Depok | 33,38 | 1,17 | 32,21 | 1,17 |  |  |
| 3603010 | Cisoka | Kabupaten Tangerang | 7,98 | 0,03 | 7,95 | 0,03 |  |  |
| 3603011 | Solear | Kabupaten Tangerang | 8,04 | 0,00 | 8,04 | 0,00 |  |  |
| 3603020 | Tigaraksa | Kabupaten Tangerang | 26,75 | 4,11 | 22,64 | 4,11 | ya |  |
| 3603021 | Jambe | Kabupaten Tangerang | 3,75 | 0,00 | 3,75 | 0,00 | ya |  |
| 3603030 | Cikupa | Kabupaten Tangerang | 88,05 | 25,15 | 62,90 | 20,71 | ya | P+V |
| 3603040 | Panongan | Kabupaten Tangerang | 29,73 | 2,79 | 26,94 | 2,79 | ya |  |
| 3603050 | Curug | Kabupaten Tangerang | 57,60 | 9,99 | 47,61 | 9,99 |  | V |
| 3603051 | Kelapa Dua | Kabupaten Tangerang | 56,43 | 6,95 | 49,48 | 6,95 |  | V |
| 3603060 | Legok | Kabupaten Tangerang | 25,21 | 0,98 | 24,23 | 0,98 |  |  |
| 3603070 | Pagedangan | Kabupaten Tangerang | 30,28 | 3,31 | 26,97 | 3,31 |  |  |
| 3603081 | Cisauk | Kabupaten Tangerang | 19,80 | 0,72 | 19,08 | 0,72 |  |  |
| 3603120 | Pasarkemis | Kabupaten Tangerang | 55,48 | 13,08 | 42,41 | 11,58 | ya | P |
| 3603121 | Sindang Jaya | Kabupaten Tangerang | 12,31 | 0,64 | 11,67 | 0,64 |  |  |
| 3603130 | Balaraja | Kabupaten Tangerang | 33,43 | 6,86 | 26,57 | 6,86 |  |  |
| 3603131 | Jayanti | Kabupaten Tangerang | 7,13 | 0,15 | 6,98 | 0,15 |  |  |
| 3603132 | Sukamulya | Kabupaten Tangerang | 5,90 | 0,22 | 5,67 | 0,22 |  |  |
| 3603140 | Kresek | Kabupaten Tangerang | 5,05 | 0,06 | 4,99 | 0,06 |  |  |
| 3603141 | Gunung Kaler | Kabupaten Tangerang | 3,84 | 0,02 | 3,82 | 0,02 |  |  |
| 3603150 | Kronjo | Kabupaten Tangerang | 4,81 | 0,03 | 4,78 | 0,03 |  |  |
| 3603151 | Mekar Baru | Kabupaten Tangerang | 3,30 | 0,02 | 3,28 | 0,02 |  |  |
| 3603160 | Mauk | Kabupaten Tangerang | 7,06 | 0,01 | 7,04 | 0,01 |  |  |
| 3603161 | Kemiri | Kabupaten Tangerang | 4,34 | 0,77 | 3,58 | 0,77 |  |  |
| 3603162 | Sukadiri | Kabupaten Tangerang | 7,55 | 0,06 | 7,49 | 0,06 |  |  |
| 3603170 | Rajeg | Kabupaten Tangerang | 18,13 | 0,37 | 17,76 | 0,37 |  | P |
| 3603180 | Sepatan | Kabupaten Tangerang | 23,21 | 5,88 | 17,33 | 5,88 |  |  |
| 3603181 | Sepatan Timur | Kabupaten Tangerang | 16,91 | 1,09 | 15,82 | 1,09 |  |  |
| 3603190 | Pakuhaji | Kabupaten Tangerang | 13,79 | 0,88 | 12,91 | 0,88 |  |  |
| 3603200 | Teluknaga | Kabupaten Tangerang | 21,83 | 2,12 | 19,71 | 2,12 |  |  |
| 3603210 | Kosambi | Kabupaten Tangerang | 44,02 | 20,68 | 23,34 | 20,68 |  |  |
| 3671010 | Ciledug | Kota Tangerang | 27,64 | 0,13 | 27,50 | 0,13 |  |  |
| 3671011 | Larangan | Kota Tangerang | 28,08 | 0,20 | 27,89 | 0,20 |  |  |
| 3671012 | Karang Tengah | Kota Tangerang | 27,62 | 0,35 | 27,27 | 0,35 |  |  |
| 3671020 | Cipondoh | Kota Tangerang | 48,56 | 2,26 | 46,29 | 2,26 |  | P+V |
| 3671021 | Pinang | Kota Tangerang | 40,31 | 4,06 | 36,25 | 4,06 |  |  |
| 3671030 | Tangerang | Kota Tangerang | 41,13 | 5,17 | 35,95 | 5,17 |  |  |
| 3671031 | Karawaci | Kota Tangerang | 39,13 | 10,71 | 28,42 | 10,71 |  |  |
| 3671040 | Jati Uwung | Kota Tangerang | 53,09 | 29,07 | 24,01 | 29,07 |  |  |
| 3671041 | Cibodas | Kota Tangerang | 28,22 | 7,06 | 21,16 | 7,06 |  |  |
| 3671042 | Periuk | Kota Tangerang | 26,27 | 7,27 | 19,00 | 7,27 |  |  |
| 3671050 | Batuceper | Kota Tangerang | 24,61 | 8,77 | 15,84 | 8,77 |  |  |
| 3671051 | Neglasari | Kota Tangerang | 22,85 | 6,24 | 16,61 | 6,24 |  |  |
| 3671060 | Benda | Kota Tangerang | 34,25 | 9,35 | 24,90 | 9,35 |  |  |
| 3674010 | Setu | Kota Tangerang Selatan | 35,24 | 6,35 | 28,89 | 2,49 | ya |  |
| 3674020 | Serpong | Kota Tangerang Selatan | 62,76 | 5,66 | 57,10 | 5,66 | ya | V |
| 3674030 | Pamulang | Kota Tangerang Selatan | 73,64 | 4,41 | 69,23 | 4,41 |  | P+V |
| 3674040 | Ciputat | Kota Tangerang Selatan | 57,84 | 4,69 | 53,15 | 4,69 |  | P+V |
| 3674050 | Ciputat Timur | Kota Tangerang Selatan | 55,70 | 2,53 | 53,18 | 2,53 |  | V |
| 3674060 | Pondok Aren | Kota Tangerang Selatan | 81,60 | 4,16 | 77,45 | 4,16 |  | P+V |
| 3674070 | Serpong Utara | Kota Tangerang Selatan | 54,19 | 7,32 | 46,86 | 7,32 |  | V |
