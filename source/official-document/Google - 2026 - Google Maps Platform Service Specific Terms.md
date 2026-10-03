---
source_type: official-document
title: "Google Maps Platform Service Specific Terms"
creators:
  - "Google"
year: 2026
identifier: null
url: "https://cloud.google.com/maps-platform/terms/maps-service-terms?hl=en"
date_accessed: 2026-10-03
access_basis: full-text
institution: "Google LLC"
jurisdiction: null
publication_date: "2026-06-10"
document_number: null
---

# Google Maps Platform Service Specific Terms

## AI-Processed Digest

### Core Claims or Contents

- Versi yang diarsipkan bertanda "Last modified June 10, 2026".
- **§3 Google ID Caching:** pelanggan boleh menyimpan nilai ID Google, misalnya `place_id` dari Places API, Directions API, Geolocation API, dan Routes API, sesuai dokumentasi.
- **§14 Places API (Legacy and New):** 14.1 konten boleh dipakai tanpa peta Google; **14.2 konten Places tidak boleh dipakai bersama peta non-Google**; 14.3 lintang/bujur boleh di-*cache* paling lama 30 hari kalender berturut-turut.
- **§19 Routes API:** 19.1 konten boleh dipakai tanpa peta Google; **19.2 konten Routes tidak boleh dipakai bersama peta non-Google**; 19.3 lintang/bujur boleh di-*cache* paling lama 30 hari.

### Evidence and Method

Halaman diunduh agen sebagai HTML pada 3 Oktober 2026 dan dibaca dari teks hasil pembersihan tag. Ketentuan umum Google Maps Platform Terms of Service (dokumen terpisah) belum dibaca.

### Scope and Limitations

- Dokumen ini tidak menyebut secara eksplisit apakah nilai turunan (misalnya waktu tempuh yang sudah diagregasikan atau jumlah tempat per kecamatan) masih tergolong "Google Maps Content". Status tersebut tetap wilayah abu-abu.
- Akibat bagi penelitian (inferensi agen): lapisan turunan Google sebaiknya tidak ditampilkan di Web GIS berpeta dasar OSM atau peta non-Google lain; nilai tersebut cukup dilaporkan dalam tabel dan analisis statistik.

## Faithful Source Text or Excerpts

> "Customer may cache the Google ID values from the Services that return such field and allow caching, in accordance with its Documentation. For example, Customer may cache (a) place_id from Places API, Directions API, Geolocation API and Routes API ..." (§3)

> "No use with a non-Google map. Customer must not use Google Maps Content from the Places API in conjunction with a non-Google map." (§14.2)

> "No use with a non-Google map. Customer must not use Google Maps Content from the Routes API in conjunction with a non-Google map." (§19.2)

> "Customer may temporarily cache latitude (lat) and longitude (lng) values from the Routes API for up to 30 consecutive calendar days, after which Customer must delete the cached latitude and longitude values." (§19.3)

## Provenance Notes

- Source attachment: [[Google - 2026 - Google Maps Platform Service Specific Terms.html]] (SHA-256 `4bffa512495ca172ed36abcb382b30eb70b311312e74cda7ffdb35a8e3579be6`).
- Dirujuk naskah sebagai `googlemaps2026terms`; entri bib bertanggal akses 27 September 2026, sedangkan salinan arsip ini diambil 3 Oktober 2026.
