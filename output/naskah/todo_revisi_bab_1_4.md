# TODO Revisi Naskah Bab 1–4

> **Objek:** `latex/tga_pwk_jakarta_bab_1_4_final.tex` (satu-satunya sumber naskah; file `.tex` per bab dihapus 2 Oktober 2026).
> **Dasar:** `output/naskah/evaluasi_substansi_dan_eksekusi_bab_1_4_draf.md`. Kode dalam kurung (B1, C6, D, …) merujuk ke butir evaluasi itu.
> **Status (2 Oktober 2026, sesi cloud):** revisi `.tex` §1–§6 selesai. Diagram §7 dirender, sedangkan peta GIS masih placeholder. Rincian pemeriksaan data ada di evaluasi §15. Rujukan baris `tex:NNN` lama sudah tidak berlaku; cari dengan kata kunci.

Penanda: 📥 = butuh berkas yang belum diunduh; ❓ = butuh keputusan pengguna; 🖐 = dikerjakan pengguna di lokal.

## Cara memakai daftar ini

**Terkunci (keputusan pengguna; jangan diubah tanpa bertanya):**
- Sikap data: sumber terbuka dan OSM lebih dulu; tidak membeli data BPS; tidak bergantung pada pengajuan.
- Judul memakai "Jabodetabek"; Cianjur tidak dicakup.
- Desain dua tingkat (kecamatan dan kab/kota) dengan dua domain utama (layanan dan pekerjaan).
- Inferensi Q3 lewat kemiringan residu terhadap integrasi, bukan tanda residu.
- Pusat dipilih berdasarkan massa.
- Satu indikator satu peran.
- Kawasan hunian dapat menjadi korban *shadow*.
- CCTV untuk *screenline*; SUMO keluar kecuali dikombinasikan dengan CCTV; Web GIS dan *what-if* tetap.
- Data Google hanya untuk menghitung.
- **Inti penelitian tetap DKI Jakarta; WSM hanya salah satu sumber** (pengguna, 2 Oktober 2026).
- Dua butir yang ditolak pengguna tidak diangkat lagi: kritik "skala" *borrowed size* dan perluasan ke Cianjur.

**Keputusan agen 2 Oktober 2026 (atas mandat "ambil keputusan terbaik"; boleh dikoreksi pengguna):** lihat evaluasi §15.2. Ringkasnya:
- OD sintetis dihapus dari rantai.
- Nama wilayah: "DKI Jakarta" dengan catatan kaki tentang UU 2/2024.
- File `.tex` per bab dihapus.
- "Perubahan" dipindah dari Q2 ke Q1.
- Pusat sekunder ditandai dengan kuartil teratas penduduk atau volume hunian.
- Layanan utama: RS + perguruan tinggi + bank umum.
- Duplikat PDF dihapus.

## 0. Prasyarat data

### 0.1 Unduhan manual BPS

- [x] *Statistik Komuter Jabodetabek* 2014, 2019, 2023. Matriks asal–tujuan (Tabel 2) ada di ketiga edisi dan sudah ditranskripsi serta dicocokkan dengan total di catatan sumbernya.
- [x] *Wilayah Statistik Metropolitan Indonesia 2024*. Lampiran 3 (penduduk, luas, dan kepadatan) dan Lampiran 13 (% komuter ke inti dan delineasi) untuk 141 kecamatan sudah ditranskripsi ke catatan sumber, lengkap dengan kode BPS.
- [x] *Statistik Potensi Desa* 2024 dan 2025 untuk tujuh kab/kota. Tabel jumlah fasilitas per kecamatan setara antar-kab/kota (nomor tabel bergeser antara edisi kota dan kabupaten).
- [ ] 📥 **Kota Bekasi:** publikasi Podes tidak ada. Tabel 4.2.1 *Kota Bekasi Dalam Angka 2025* hanya memuat banyaknya kelurahan yang **memiliki** fasilitas, bukan jumlah fasilitas, sehingga tidak setara. Unduh 12 *Kecamatan Dalam Angka 2025* untuk dicek; jika tidak setara, cadangan K1 berlaku (model layanan dengan 129 kecamatan).
  - Edisi 2025 (data 2024):
    - Bekasi Barat: https://bekasikota.bps.go.id/en/publication/2025/09/26/988fa1683590a87f810c6d14/kecamatan-bekasi-barat-dalam-angka-2025.html
    - Bekasi Selatan: https://bekasikota.bps.go.id/en/publication/2025/09/26/84b7f19ce05eb31a59de0bd0/kecamatan-bekasi-selatan-dalam-angka-2025.html
    - Bekasi Timur: https://bekasikota.bps.go.id/en/publication/2025/09/26/88f5d7ea28ad538a191114d3/kecamatan-bekasi-timur-dalam-angka-2025.html
    - Rawalumbu: https://bekasikota.bps.go.id/id/publication/2025/09/26/de57d2a5e5ce577fb1844fb1/kecamatan-rawalumbu-dalam-angka-2025.html
    - Jatiasih: https://bekasikota.bps.go.id/en/publication/2025/09/26/b248aa1726d5b343daa68fe6/jatiasih-district-in-figures-2025.html
    - Jatisampurna: https://bekasikota.bps.go.id/en/publication/2025/09/26/f23690b309af303d9512d617/jatisampurna-district-in-figures-2025.html
    - Bantargebang: https://bekasikota.bps.go.id/en/publication/2025/09/26/d901ae5b51f62c976db8db12/bantargebang-district-in-figures-2025.html
    - Mustikajaya: https://bekasikota.bps.go.id/en/publication/2025/09/26/18d81764fd0548eba554196c/kecamatan-mustikajaya-dalam-angka-2025.html
    - Pondokmelati: https://bekasikota.bps.go.id/en/publication/2025/09/26/eb56ee0ccee33d134c232c12/kecamatan-pondokmelati-dalam-angka-2025.html
  - Edisi 2025 belum ditemukan; tautan edisi 2024:
    - Bekasi Utara: https://bekasikota.bps.go.id/en/publication/2024/09/26/554c33fc11a60bf7865f47fb/bekasi-utara-district-in-figures-2024.html
    - Medan Satria: https://bekasikota.bps.go.id/en/publication/2024/09/26/222d2ed041be6da0d1e212d3/medan-satria-district-in-figures-2024.html
    - Pondokgede: https://bekasikota.bps.go.id/en/publication/2024/09/26/c8909d6a52d96096bdcdfdb3/kecamatan-pondokgede-dalam-angka-2024.html
- [x] *Dalam Angka* provinsi 2025 dan kab/kota 2025 serta *PDRB Kabupaten/Kota 2020–2024*. Angka penduduk, kepadatan, PDRB, dan pangsa sektor 2024 sudah diambil dan dicatat locatornya di catatan sumber.
- [x] Tabel upah. **Keputusan:** manfaat tingkat 2 memakai Tabel 51 *Statistik Komuter 2023* (distribusi penghasilan komuter bekerja per kab/kota asal). Tabel upah provinsi dan UMK hanya menjadi konteks. Upah formal Banten tidak tersedia dan tidak lagi menjadi syarat.

### 0.2 Sumber non-BPS

- [x] UU 2/2024 (Pasal 51–55 dan 73 sudah dicatat), Perpres 60/2020, BPTJ 2024, Kemenperin 2025 (ringkasan Jabodetabek dihitung: 21 KI), GTFS TransJakarta, dan GHSL R2023A.
- [ ] Opsional: catat halaman peta jaringan 2045 di PDF JUTPI 3 (Gambar 4.6 sementara).
- [ ] 📥 Ekstrak OSM Jawa (Geofabrik) dan rilis Overture bertanggal, untuk perutean dan uji kelengkapan.
- [ ] 📥 SIRS dan PDDikti (pembobot orde layanan; sensitivitas).
- [ ] Arsip PDF *Google Maps Platform Service Specific Terms* pada tanggal pengambilan.

### 0.3 Verifikasi (selesai 2 Oktober 2026; rincian di evaluasi §15.1)

- [x] Jumlah kecamatan non-DKI: **141** (Kab. Bogor 40, Kab. Bekasi 23, Kota Bogor 6, Kota Bekasi 12, Depok 11, Kab. Tangerang 29, Kota Tangerang 13, Tangsel 7).
- [x] Definisi "inti" WSM: kawasan inti perkotaan **morfologis** (grid ≥1.500 jiwa/km² SP2020). Inti 1 mencakup seluruh DKI, Kota Bekasi, Depok, Kota Tangerang, dan Tangsel, serta kecamatan padat di tiga kabupaten. Ambang 7% adalah pilihan metodologis (Bosker dkk. 2021), bukan anomali. Nilai % tersedia untuk semua kecamatan, termasuk kecamatan inti.
- [x] Komuter: matriks asal–tujuan 13×13 tersedia (2014, 2019, 2023). Durasi (Tabel 20) dan biaya (Tabel 35) hanya berupa **distribusi kelas**, bukan rata-rata. Penghasilan komuter tersedia (Tabel 51).
- [x] Nama wilayah inti: publikasi BPS sampai 2026 masih memakai "Provinsi DKI Jakarta", dan UU 2/2024 Pasal 73 mengaitkan saat berlakunya dengan Keppres pemindahan ibu kota. Naskah memakai "DKI Jakarta" dengan catatan kaki.
- [ ] ❓ **Basis penduduk kecamatan Banten** di WSM Lampiran 3 berselisih 2–3% dari proyeksi kab/kota. Cocokkan dengan tabel kecamatan di *Dalam Angka* kab/kota Banten sebelum ambang massa dibekukan.
- [ ] Satuan `Luas_IUKI` Kemenperin (kemungkinan hektare) belum terdokumentasi.

### 0.4 Batas kecamatan

- [ ] 🖐 Unduh COD-AB HDX (https://data.humdata.org/dataset/cod-ab-idn; 219–498 MB; **jangan di-commit**). Cocokkan kode 2020 dengan kode BPS 2024 di WSM Lampiran 13; bila tidak cocok, cadangan K2 berlaku.
- [x] Tabel siap-*join* tidak dibuat di `calculation/`. Penggantinya adalah tabel 141 kecamatan **dengan kode BPS** (penduduk, luas, kepadatan, % komuter ke inti, dan delineasi) di catatan sumber WSM (`source/official-document/BPS - 2026 - Wilayah Statistik Metropolitan Indonesia 2024.md`). Tabel itu bisa disalin ke CSV untuk QGIS.

### 0.5 Kebersihan repo (selesai 2 Oktober 2026)

- [x] 36 PDF duplikat di `source/dataset/` dihapus setelah checksum SHA-256-nya terbukti identik dengan salinan `official-document/`.
- [x] Tiga publikasi dipindahkan ke `official-document/` dan diberi catatan sumber: Pekerja Formal dan Informal Jawa Barat 2023 dan 2024, serta Profil Pekerja DKI 2023.
- [x] Empat CSV upah diberi catatan sumber (`bps_upah_*`, `bps_pendapatan_*`).
- [x] Berkas sampah dihapus: `.pdf.part`, `:Zone.Identifier`, dan berkas kunci Word `~$mplate…docx`.
- [x] CSV upah Jawa Barat 2019 yang kembar dihapus (yang dipertahankan adalah berkas yang punya catatan sumber).
- [ ] ❓ J21/J26 (Henderson dkk.) berisi PDF identik, dan J26 salah tahun (2006). **Dibiarkan**, karena J26 dirujuk `output/kajian/review-J26.md`. Putuskan apakah kode korpus perlu dirapikan.

## 1. Keputusan global — selesai di `.tex`

- [x] Judul: "… Pusat-Pusat Sekunder Jabodetabek" (C8).
- [x] Dua tingkat (C3); dua domain utama (C10); inferensi kemiringan (B1); pusat berbasis massa (B2); satu indikator satu peran (B4); kawasan hunian sebagai kemungkinan korban (B3).
- [x] CCTV, SUMO, dan Web GIS hanya dijelaskan di Bab 3 (C5).
- [x] Tipologi seragam tujuh kategori di Tabel 2.2, Bab 3, Gambar 1.1, dan Gambar 2.1 (D).
- [x] OD sintetis **dihapus** dari rantai. Alasannya, relasi kab/kota sudah teramati dan integrasi kecamatan tersedia dari WSM.
- [x] Satu sumber kebenaran: file per bab dihapus. Berkas isu per bab ditandai historis.

## 2. Bab 1 — selesai

- [x] Paragraf Kawasan Aglomerasi (UU 2/2024 Pasal 51–55; Perpres 60/2020); catatan kaki nama DKI.
- [x] Janji "penerima manfaat dan penanggung beban" diturunkan menjadi profil per kecamatan dan per kab/kota asal.
- [x] Klaim celah dipertahankan; kontribusi ditulis dua tingkat.
- [x] Q1 kini memuat perubahan 2014/2019/2023 (sisi relasi). Kata "perubahan" dihapus dari Q2. Tujuan khusus diselaraskan.
- [x] Batasan: Cianjur, tolok ukur internal dan inferensi kemiringan, unit dua tingkat, dua domain beserta proksinya. Detail alat dihapus.
- [x] Subbab metode diringkas; manfaat praktis menyebut Dewan Kawasan Aglomerasi dan perlakuan kawasan hunian.
- [x] Sitasi Alonso (1973) (parafrase dicek terhadap teks sumber).

## 3. Bab 2 — selesai

- [x] Definisi pusat sekunder berbasis massa; residu dibaca lewat kemiringan; Alonso; kawasan hunian sebagai korban *shadow* (mekanisme kebocoran layanan).
- [x] Tabel 2.1: Sadewo dkk. 2021 dan 2023 ditambahkan (baris 12–13).
- [x] Model konseptual: $R$ dibaca melalui kemiringan terhadap $I$.
- [x] Tabel 2.2: tujuh kategori; residu bertanda hanya bila selangnya tidak memuat nol.
- [x] Proposisi P1–P4 berarah beserta hasil yang membantah (Tabel 2.3); gerbang: beban independen dari integrasi **dan** residu; penjelasan alternatif bernama (Tabel 2.4).

## 4. Bab 3 — selesai (ditulis ulang)

- [x] Spesifikasi utama dan **cadangan bernama K1–K8** beserta pemicunya (Tabel 3.2, Gambar 3.1).
- [x] Tabel sumber aktual (Tabel 3.3); operasionalisasi tingkat 1 dan 2 (Tabel 3.4–3.5); status D/A/S/P (Tabel 3.6); keterlacakan Q1–Q3 (Tabel 3.7). Semua tabel bernomor.
- [x] Pengulangan "Fondasi pengukuran" dihapus; WSM didefinisikan; "Sabuk" dan "S-1" dihapus.
- [x] Integrasi kecamatan = % komuter ke Inti 1 WSM (status A), dengan sensitivitas $I^{DKI}$ (estimasi S) = WSM × pangsa kab/kota ke DKI 2023.
- [x] Model binomial negatif (layanan) dan log-linear (volume NRES), prediksi *leave-one-out*, residu log.
- [x] Manfaat dan beban dua tingkat; beban T2 memakai pangsa ≥90 menit dan ≥Rp25.000; manfaat T2 memakai pangsa penghasilan ≥Rp5 juta.
- [x] Desain kepatuhan Google, lisensi GHSL/COD-AB, status lisensi GTFS/Kemenperin, dan privasi CCTV.
- [x] Daftar ketahanan sesuai C6, ditambah Podes 2025, $I^{DKI}$, dan efek tetap kab/kota.
- [ ] ❓ Ambang massa (P75, dengan P66/P80 sebagai sensitivitas), titik acuan beban (Bundaran HI), dan ambang akses 60 menit adalah **pilihan agen**. Konfirmasi atau ubah.

## 5. Bab 4 — selesai (ditulis ulang)

- [x] Konteks kebijakan (UU 2/2024, Perpres 60/2020) dan delineasi WSM.
- [x] Tabel 4.1: penduduk, kepadatan, dan jumlah kecamatan untuk sembilan unit (2024).
- [x] Subbab struktur ekonomi: Tabel 4.2 (PDRB, per kapita, pangsa C/G/H 2024).
- [x] Subbab pola komuter: Tabel 4.3 (arus 2023; orientasi ke DKI 2014/2019/2023), ringkasan beban, dan ringkasan WSM kecamatan.
- [x] Morfologi GHSL, jaringan eksisting vs rencana, kawasan industri (21 KI), dan kota baru (Firman 2004; Firman & Fahmi 2017).
- [x] Pusat berbasis massa: ambang penduduk P75 sekitar 194 ribu jiwa, 36 kecamatan (**sementara**, sebelum kriteria volume hunian dihitung).
- [x] Tabel audit sumber diperbarui; kalimat CCTV/SUMO, kandidat lama, dan penggabungan Tangerang–Tangsel dihapus.

## 6. Bibliografi — selesai

- [x] Diperbaiki dan dicek terhadap salinan lokal:
  - `otsuka2025` (RSRS 12(1): 975–995);
  - `sadewoetal2021` (Asian Geographer; penulis Erie Sadewo dkk.);
  - `sadewoetal2023` (penulis Erie Sadewo, Delik Hudalah, Anzhelika Antipova, Long Cheng, Ibnu Syabri; 44(8): 1628–1653 dari evaluasi);
  - `burgermeijers2016` (95(1): 5–16);
  - `durantonpuga2004` (`@incollection`);
  - `andani2021` dan `volgmannrusche2020` (catatan keterbatasan metadata).
- [x] `bpsjabar2025` kini merujuk *Provinsi Jawa Barat Dalam Angka 2025*; `bpsbanten2024` dihapus.
- [x] Entri baru: Alonso 1973, Firman 2004, UU 2/2024, Perpres 60/2020, BPTJ 2024, Kemenperin 2025, GHSL, GTFS, COD-AB HDX, syarat Google, Statistik Komuter 2014/2019/2023, WSM 2024, PDRB, Podes 2024 (tujuh entri), *Dalam Angka* kab/kota 2025 (delapan entri), *Dalam Angka* provinsi, dan KAK.
- [ ] Belum diverifikasi: volume dan halaman cetak `sadewoetal2021` dan `volgmannrusche2020`; judul buku `andani2021`.
- [ ] Opsional: Otsuka, *Borrowed Size and Regional Resilience* (Springer); kandidat Meijers dkk. 2018, Cardoso & Meijers 2016, dan van Meeteren dkk. 2016 diverifikasi dulu.

## 7. Figure

### 7.1 Aturan placeholder

- [x] Makro `\GambarPlaceholder` ada di `latex/tga-preamble.tex`.
- Setelah peta jadi: simpan di `latex/figures/` dengan nama berkas target, ganti `\GambarPlaceholder{…}` dengan `\includegraphics[width=\textwidth]{…}`, lalu centang di tabel 7.2.

### 7.2 Daftar gambar

Nomor gambar di PDF mengikuti urutan kemunculan: diagram keputusan cadangan menjadi Gambar 3.1 dan alur analisis menjadi Gambar 3.2.

| ID | Berkas (`latex/figures/`) | Isi | Pembuat | Status di naskah | Selesai |
|---|---|---|---|---|---|
| G1.1 | `bab1_logika_penelitian` | Logika penelitian | Agen (`.mmd`) | Dirender PNG | [x] |
| G2.1 | `bab2_kerangka_konseptual` | Kerangka konseptual $S, X, F, \hat F, R, I, Z$ | Agen (`.mmd`) | Dirender PNG | [x] |
| G3.1 | `bab3_alur_analisis` | Alur dua tingkat dengan gerbang | Agen (`.mmd`) | Dirender PNG (Gambar 3.2 di PDF) | [x] |
| G3.2 | `bab3_keputusan_cadangan` | Spesifikasi utama → K1–K8 | Agen (`.mmd`) | Dirender PNG (Gambar 3.1 di PDF) | [x] |
| G4.1 | `bab4_admin_status` | Batas dan status administratif | 🖐 Manual | **Sementara**: `bab4_status_administratif.png` | [ ] |
| G4.2 | `bab4_kepadatan_kecamatan.pdf` | Kepadatan per kecamatan 2024 | 🖐 Manual; data WSM Lampiran 3 | Placeholder | [ ] |
| G4.3 | `bab4_komuter_od_2023.pdf` | Arus komuter kab/kota 2023 | 🖐 Manual; data catatan sumber Komuter 2023 | Placeholder | [ ] |
| G4.4 | `bab4_komuter_ke_inti_kecamatan.pdf` | % komuter ke inti per kecamatan | 🖐 Manual; data WSM Lampiran 13 | Placeholder | [ ] |
| G4.5 | `bab4_terbangun_nonhunian.pdf` | Volume terbangun total dan nonhunian | 🖐 Manual; GHSL | Placeholder | [ ] |
| G4.6 | `bab4_jaringan_eksisting` | Jaringan eksisting dan rencana 2045 | 🖐 Manual | **Sementara**: `bab4_network_jutpi.png` | [ ] |
| G4.7 | `bab4_kawasan_industri.pdf` | Kawasan industri dan kota baru | 🖐 Manual | Placeholder | [ ] |
| G4.8 | `bab4_pusat_berdasarkan_massa.pdf` | Pusat berbasis massa | 🖐 Manual (setelah volume hunian dihitung) | Placeholder | [ ] |

**Spesifikasi peta manual** (tidak berubah):
- UTM 48S (EPSG:32748) dengan *extent* yang sama;
- laut diisi; kabupaten tetangga (termasuk Cianjur) abu-abu; inset Jawa; catatan Kepulauan Seribu;
- skala batang, arah utara, dan koma desimal;
- label tidak menabrak garis; satu font dan satu palet;
- PDF vektor atau PNG ≥300 dpi pada lebar 160 mm;
- sumber ditulis di caption.

### 7.3 Render diagram

- Perintah: `mmdc -i <berkas>.mmd -o <berkas>.png -s 3 -b white`. Di sesi cloud, perintah ini dijalankan dengan konfigurasi puppeteer `{"executablePath":"/opt/pw-browsers/chromium","args":["--no-sandbox"]}`.
- Diagram cloud dirender dengan font pengganti, karena Arial tidak tersedia. Render ulang di lokal untuk Arial, atau ekspor ke PDF bila ingin vektor.

## 8. Penutup revisi

- [x] Konsistensi istilah (DKI Jakarta, pusat sekunder, residu, tujuh kategori). Frasa "tidak otomatis" kini muncul 1×.
- [x] Uji kompilasi di cloud (XeLaTeX + Biber, font pengganti TeX Gyre Termes) berhasil: 62 halaman, tanpa galat, tanpa rujukan atau sitasi yang tidak terdefinisi, tiga *overfull box* <3 pt.
- [ ] 🖐 Kompilasi final di lokal dengan Times New Roman, lalu periksa PDF per halaman.
- [x] Berkas isu per bab ditandai historis.
- [ ] ❓ `argument/argument/skripsi_s1_…md` masih menyebut file `.tex` per bab sebagai "rujukan operasional aktif". Mengedit Argument perlu izin eksplisit.
