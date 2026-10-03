---
source_type: official-document
title: "Google Maps Platform Terms of Service"
creators:
  - "Google"
year: 2026
identifier: null
url: "https://cloud.google.com/maps-platform/terms?hl=en"
date_accessed: 2026-10-03
access_basis: full-text
institution: "Google LLC"
jurisdiction: null
publication_date: "2026-08-26"
document_number: null
---

# Google Maps Platform Terms of Service

## AI-Processed Digest

### Core Claims or Contents

- Versi yang diarsipkan bertanda "Last modified August 26, 2026".
- **§3.2.3 Restrictions Against Misusing the Services:**
  - (a) *No Scraping*: dilarang mengekspor atau mengekstrak konten Google untuk dipakai di luar layanan, termasuk menyimpan atau mengunduh massal hasil *directions*, *distance matrix*, dan informasi tempat, serta menyalin nama usaha dan alamat.
  - (b) *No Caching*: dilarang menyimpan konten Google kecuali yang diizinkan *Maps Service Specific Terms*.
  - (c) *No Creating Content From Google Maps Content*: contoh (iv) **melarang memakai lintang/bujur Places API sebagai masukan analisis point-in-polygon**.
  - (e) *No Use With Non-Google Maps*.

### Evidence and Method

Halaman diunduh agen sebagai HTML pada 3 Oktober 2026 dan dibaca dari teks hasil pembersihan tag, khususnya §3.2.3.

### Scope and Limitations

- Bagian lain (biaya, kewajiban, definisi lengkap "Google Maps Content") hanya dibaca sekilas.
- Akibat bagi penelitian (inferensi agen): desain lama yang menumpangkan titik Places ke poligon kecamatan melanggar §3.2.3(c)(iv). Menyimpan waktu tempuh Routes per kecamatan tidak diizinkan oleh §3.2.3(a)–(b) karena Routes hanya memberi izin *cache* untuk lintang/bujur selama 30 hari. Jalur yang tersisa adalah Places Aggregate API (syarat khusus §13).

## Faithful Source Text or Excerpts

> "No Scraping. Customer will not export, extract, or otherwise scrape Google Maps Content for use outside the Services. For example, Customer will not: (i) pre-fetch, index, store, reshare, or rehost Google Maps Content outside the services; (ii) bulk download Google Maps tiles, Street View images, geocodes, directions, distance matrix results, roads information, places information, elevation values, and time zone details; ..." (§3.2.3(a))

> "No Caching. Customer will not cache Google Maps Content except as expressly permitted under the Maps Service Specific Terms." (§3.2.3(b))

> "... (iv) use latitude/longitude values from the Places API as an input for point-in-polygon analysis; ..." (§3.2.3(c))

## Provenance Notes

- Source attachment: [[Google - 2026 - Google Maps Platform Terms of Service.html]] (SHA-256 `a4d810345b9c75553a646dc2d25f296e71229047f717177a640f48bd595916b5`).
- Dirujuk naskah sebagai `googlemaps2026tos`.
