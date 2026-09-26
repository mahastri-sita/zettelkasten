---
source_type: dataset
title: "geoBoundaries Indonesia ADM2 simplified"
creators:
  - "William & Mary GeoLab"
year: 2023
identifier: "IDN-ADM2"
url: "https://github.com/wmgeolab/geoBoundaries/raw/9469f09/releaseData/gbOpen/IDN/ADM2/geoBoundaries-IDN-ADM2_simplified.geojson"
date_accessed: 2026-09-19
access_basis: raw-data
publisher: "William & Mary GeoLab; source organizations listed by geoBoundaries: BPS, WFP, and OCHA ROAP"
version: "gbOpen build 2023-12-12"
release_date: 2023-12-12
license: "Creative Commons Attribution 3.0 IGO"
spatial_coverage: "Indonesia, administrative level 2; Bab 4 selects Jabodetabek units"
temporal_coverage: "Boundary year represented: 2020"
unit_of_observation: "Administrative level 2 polygon"
data_format: "GeoJSON"
raw_files:
  - "geoBoundaries-IDN-ADM2_simplified.geojson"
checksum: "sha256: 146653d488331086ddc43d159a261b01ea6dd08c7ed422e34a9886c3c690430c"
---

# geoBoundaries Indonesia ADM2 simplified

## Dataset Description

Berkas GeoJSON ini berisi geometri administratif level 2 Indonesia yang disederhanakan. Dalam pekerjaan ini, berkas dipakai sebagai geometri konteks untuk peta Bab 4. Wilayah penelitian memilih DKI Jakarta, Kabupaten Bogor, Kota Bogor, Kota Depok, Kabupaten Tangerang, Kota Tangerang, Kota Tangerang Selatan, Kabupaten Bekasi, dan Kota Bekasi.

## Variables or Schema

Atribut yang tersedia pada fitur meliputi `shapeName`, `shapeISO`, `shapeID`, `shapeGroup`, dan `shapeType`. Geometri berupa `Polygon` atau `MultiPolygon` sesuai fitur sumber. Tidak ada variabel penduduk, pekerjaan, fungsi, atau arus perjalanan di dalam berkas ini.

## Coverage and Unit of Observation

Unit pengamatan adalah poligon ADM2. Metadata sumber menyatakan bahwa geometri merepresentasikan batas tahun 2020 dan build geoBoundaries bertanggal 12 Desember 2023. Bab 4 menggunakan geometri untuk konteks visual dan pelaporan batas administratif. Geometri tidak digunakan untuk menetapkan pusat sekunder, daerah tangkapan, atau batas fungsional.

## Collection or Production Method

Metode pembentukan mengikuti dokumentasi geoBoundaries. Catatan penelitian ini tidak menambahkan asumsi tentang cara pengumpulan batas di luar metadata yang tersedia. Berkas yang disimpan adalah salinan raw dari URL sumber pada 19 September 2026.

## Known Limitations

Geometri disederhanakan sehingga tidak boleh dipakai untuk pengukuran luas yang memerlukan ketelitian batas tinggi. Kesepadanan geometri dengan unit indikator pada tahun lain perlu diperiksa. Perbedaan nama, pemekaran, atau perubahan batas harus dicatat sebelum agregasi.

## Raw File Inventory

- `geoBoundaries-IDN-ADM2_simplified.geojson`: salinan raw GeoJSON yang diakses pada 19 September 2026.

## Provenance Notes

Sumber metadata lokal sebelumnya mencatat build 12 Desember 2023, batas yang direpresentasikan tahun 2020, lisensi CC BY 3.0 IGO, dan batas penggunaan sebagai geometri konteks. Berkas ini tidak dibersihkan atau dinormalisasi. Peta turunan disimpan terpisah di `latex/figures/` dan `output/naskah/bab_4/figures/`.
