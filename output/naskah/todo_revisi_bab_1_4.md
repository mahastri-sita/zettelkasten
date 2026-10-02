# TODO Revisi Naskah Bab 1–4

> **Objek:** `latex/tga_pwk_jakarta_bab_1_4_final.tex`. Rujukan baris `tex:NNN` mengacu ke versi 27 September 2026 dan akan bergeser setelah edit pertama. Kerjakan dari bawah ke atas, atau cari ulang dengan kata kunci.
> **Dasar:** `output/naskah/evaluasi_substansi_dan_eksekusi_bab_1_4_draf.md`. Kode dalam kurung (B1, C6, D, …) merujuk ke butir evaluasi itu.
> **Status:** daftar kerja. Belum ada perubahan pada `.tex`.

Penanda: 📥 = butuh berkas yang belum diunduh; ❓ = butuh keputusan pengguna.

## 0. Prasyarat

### 0.1 Unduhan manual BPS (situs BPS menolak unduhan otomatis)

Simpan di `source/official-document/`. Catatan sumber dapat dibuat agen setelah berkasnya ada.

- [ ] *Statistik Komuter Jabodetabek 2023*: https://www.bps.go.id/id/publication/2024/03/28/33b6bef825944e576e7ea3ba/statistik-komuter-jabodetabek-hasil-survei-komuter-jabodetabek-2023.html
- [ ] *Statistik Komuter Jabodetabek 2019*: https://www.bps.go.id/assets/publication/2019/12/04/eab87d14d99459f4016bb057/statistik-komuter-jabodetabek-2019.html
- [ ] *Statistik Komuter Jabodetabek 2014*: https://www.bps.go.id/id/publication/2014/03/17/c0deaf751b807b56681a9860/statistik-komuter-jabodetabek--hasil-survei-komuter-jabodetabek-2014-.html
- [ ] *Wilayah Statistik Metropolitan Indonesia 2024*: https://www.bps.go.id/id/publication/2026/05/29/61f2317887bfbf98ce596e5c/wilayah-statistik-metropolitan-indonesia-2024.html
- [ ] *Statistik Potensi Desa/Kelurahan 2024* untuk delapan kab/kota Bodetabek. Cari "Statistik Potensi Desa 2024" di masing-masing situs BPS kab/kota:
  - [ ] Kabupaten Bogor: https://bogorkab.bps.go.id/id/publication/2024/12/24/1066acf5488fadafaa98eb72/statistik-potensi-desa-kabupaten-bogor.html
  - [ ] Kota Bogor: https://bogorkota.bps.go.id/en/publication/2024/12/31/88486e40df9103aefbc1763b/publikasi-statistik-potensi-desa-kota--bogor-2024.html
  - [ ] Kota Depok (depokkota.bps.go.id)
  - [ ] Kabupaten Bekasi (bekasikab.bps.go.id)
  - [ ] Kota Bekasi (bekasikota.bps.go.id)
  - [ ] Kabupaten Tangerang (tangerangkab.bps.go.id)
  - [ ] Kota Tangerang (tangerangkota.bps.go.id)
  - [ ] Kota Tangerang Selatan (tangselkota.bps.go.id)
  - [ ] Opsional: edisi 2021/2018 untuk memeriksa keterbandingan seri (C4)
- [ ] *Provinsi DKI Jakarta Dalam Angka 2025*, *Jawa Barat Dalam Angka 2025*, dan *Banten Dalam Angka 2025*: penduduk, luas, dan kepadatan kab/kota.
- [ ] *Dalam Angka* kedelapan kab/kota: penduduk per kecamatan 2024. Termasuk *Kota Depok Dalam Angka 2025* dan *Kota Tangerang Dalam Angka 2024*, yang menjadi sumber Tabel 4.1 saat ini.
- [ ] *PDRB Kabupaten/Kota di Indonesia 2020–2024*: https://www.bps.go.id/id/publication/2025/06/10/ca543e942579ced46afd603b/produk-domestik-regional-bruto-kabupaten-kota-di-indonesia-2020-2024.html
- [ ] Tabel penduduk bekerja per kab/kota 2023 (publikasi angkatan kerja provinsi) dan tabel upah rata-rata pekerja formal per kab/kota, bila ada.

### 0.2 Sudah diunduh agen (27 September 2026)

- [x] UU 2/2024, Perpres 60/2020 (batang tubuh), laporan BPTJ 2024, peta kawasan industri Kemenperin, GTFS TransJakarta, GHSL GHS-BUILT-V 2020 (total dan NRES).
- [ ] Opsional: pulihkan PDF JUTPI 3 dari git untuk mencatat halaman peta jaringan (Gambar 4.3): `git show "HEAD:source/official-document/JICA JUTPI 3 - 2025 - Project Completion Report.pdf" > /tmp/jutpi3.pdf`

### 0.3 Verifikasi setelah unduhan

- [ ] Hitung jumlah kecamatan non-DKI dari publikasi Podes/Dalam Angka; perkiraan saat ini sekitar 140 (C6).
- [ ] Baca definisi "inti" dan anomali ambang 15% vs 7% di WSM 2024 (C2).
- [ ] Periksa apakah publikasi komuter memuat tabel asal–tujuan 13×13 dan durasi/biaya per kab/kota asal (C1).
- [ ] Periksa tabel upah per kab/kota (C1).
- [ ] ❓ **Nama wilayah inti:** data Kemenperin 2025 sudah memakai "Daerah Khusus Jakarta". Pastikan status resmi per 2026, "DKI Jakarta" atau "Provinsi Daerah Khusus Jakarta", lalu seragamkan istilah di seluruh naskah.

## 1. Keputusan global (berlaku di semua bab)

- [ ] **Judul:** "… Pusat-Pusat Sekunder **Jabodetabek**" (`tex:21-22`) (C8). Rumusan final dari pengguna.
- [ ] **Dua tingkat:** kecamatan (utama; Q2–Q3) dan kab/kota (pendalaman; Q1–Q2) (C3).
- [ ] **Dua domain utama:** layanan dan pekerjaan (C10), menggantikan "pekerjaan utama, layanan kedua apabila lolos audit".
- [ ] **Inferensi Q3:** kemiringan residu terhadap integrasi di dalam Jabodetabek; tipologi hanya ringkasan (B1).
- [ ] **Pemilihan pusat:** berdasarkan massa (penduduk, luas terbangun), bukan fungsi (B2).
- [ ] **Satu indikator satu peran:** beban tidak memakai orientasi atau ketidakseimbangan arus (B4).
- [ ] **Kawasan hunian:** dapat menjadi korban *shadow*, dengan domain layanan sebagai pembeda (B3).
- [ ] **Penyebutan alat:** CCTV (*screenline* batas DKI), Web GIS, dan *what-if* cukup dijelaskan sekali di Bab 3. SUMO keluar, kecuali dikombinasikan dengan CCTV (C5).
- [ ] **Tipologi seragam:** satu daftar kelas yang sama di Tabel 2.2, tabel Bab 3, Gambar 1.1, dan Gambar 2.1 (D).
- [ ] ❓ **OD sintetis** (gravitasi/radiasi/IPF, `tex:1004-1010`, `tex:1470-1481`): rantai inti kini memakai OD kab/kota teramati dan WSM. Turunkan menjadi opsional atau hapus?
- [ ] **Satu sumber kebenaran:** file per-bab (`bab_1_…_final.tex` s.d. `bab_4_…_final.tex`) menduplikasi isi file gabungan, dan Bab 4 per-bab sudah berbeda caption. Putuskan: file gabungan sebagai sumber, file per-bab dihapus atau dibuat ulang.

## 2. Bab 1 Pendahuluan

- [ ] `tex:72` Tambah paragraf konteks kebijakan: Jabodetabek sebagai inti Kawasan Aglomerasi (UU 2/2024 Pasal 51) (C8).
- [ ] `tex:82` Turunkan janji "menunjukkan penerima manfaat dan penanggung beban" menjadi profil manfaat/beban per kecamatan dan per kab/kota asal (C1).
- [ ] `tex:84-90` Pertahankan klaim celah. Sesuaikan kalimat kontribusi dengan desain dua tingkat.
- [ ] `tex:94-99` Gambar 1.1: lihat §7 (F).
- [ ] `tex:105-111` RQ2: rinci "seri sebanding" menjadi komuter 2014/2019/2023 di sisi relasi (C4). Fungsi pekerjaan GHSL tidak dipakai untuk perubahan.
- [ ] `tex:129` Batasan: tambah kalimat Cianjur beserta alasannya (C8); tolok ukur internal dengan inferensi kemiringan (B1).
- [ ] `tex:131` Unit: tulis dua tingkat secara eksplisit (C3).
- [ ] `tex:137` Domain: layanan dan pekerjaan sama-sama utama; sebut proksi utama (C10).
- [ ] `tex:139` Hapus detail CCTV/YOLO/SUMO/Web GIS; cukup rujuk Bab 3 (C5). Tulis ulang rantai minimum sesuai dua tingkat.
- [ ] `tex:143-153` Ringkas subbab Metode supaya tidak mengulang Bab 3 (D).
- [ ] `tex:165-167` Manfaat praktis: Dewan/Kawasan Aglomerasi; perlakuan kawasan hunian (B3).

## 3. Bab 2 Kajian Pustaka

- [ ] `tex:199` Definisi pusat sekunder: kandidat ditetapkan dari massa, bukan fungsi (B2).
- [ ] `tex:223` Residu: tambah bahwa inferensi *shadow* dibaca dari kemiringan, bukan tanda residu per unit (B1).
- [ ] `tex:227` Sitasi asal-usul konsep: Alonso (1973) (E).
- [ ] `tex:235-237` *Agglomeration shadow*: tambahkan kawasan hunian sebagai kemungkinan korban, dengan mekanisme kebocoran permintaan layanan (B3).
- [ ] `tex:284-316` Tabel 2.1: tambahkan Sadewo dkk. 2021 dan 2023 (D).
- [ ] `tex:327-332` Gambar 2.1: lihat §7 (F).
- [ ] `tex:355` Model konseptual: catat bahwa $R$ dibaca melalui hubungannya dengan $I$ (kemiringan).
- [ ] `tex:359-377` Tabel 2.2: seragamkan kelas dan definisi "relatif independen" dengan Bab 3 (D).
- [ ] `tex:381-392` Proposisi: ganti dengan P1–P4 berarah, masing-masing dengan hasil yang membantah (evaluasi §10; B6).
- [ ] `tex:394-411` Gerbang label: tegaskan beban independen dari integrasi, bukan hanya dari residu (B4). Tambahkan daftar penjelasan alternatif bernama (evaluasi §10).

## 4. Bab 3 Metode Penelitian

- [ ] **Pengulangan:** "Fondasi pengukuran" (`tex:498-507`) sama dengan "Prinsip pengumpulan data" (`tex:820-828`); sisakan satu (D).
- [ ] **Keterlacakan pertanyaan:** perbarui tabel alasan pendekatan (`tex:458-485`) dan tabel keterlacakan (`tex:1431-1461`) sesuai pemetaan Q1–Q3 di evaluasi C6.
- [ ] `tex:543-581` Urutan kerja dan Gambar 3.1: sesuaikan dengan dua tingkat; lihat §7 (F).
- [ ] `tex:583-599` Rancangan minimum: tulis ulang menjadi rantai dua tingkat; hapus CCTV/SUMO/Web GIS dari sini (C3, C5).
- [ ] `tex:637-640` Definisikan atau hapus "Sabuk Wilayah Statistik Metropolitan" dan singkatan WSM (D).
- [ ] `tex:720-742` Unit amatan: kecamatan (tingkat 1) dan kab/kota (tingkat 2) (C3).
- [ ] `tex:744-763` Unit analisis: aturan pemilihan pusat berdasarkan massa, dengan ambang yang ditetapkan sebelum fungsi dihitung (B2).
- [ ] `tex:793-816` Populasi dan *leave-one-out*: pertahankan; N ≈ 140 kecamatan non-DKI (📥 hitung).
- [ ] `tex:840-892` Tabel sumber: ganti dengan sumber yang benar-benar dipakai, yaitu Podes 2024, WSM 2024, Statistik Komuter 2014/2019/2023, GHSL R2023A, Kemenperin 2025, Google Places, SIRS/PDDikti, OSM/Overture, GTFS, BPTJ, tabel Sakernas, dan CCTV (C6). 📥
- [ ] **Sisipkan tabel operasionalisasi variabel** dari evaluasi C6, dalam dua tabel: tingkat 1 dan tingkat 2, plus baris ketahanan. Letakkan di subbab pengumpulan data atau sebelum Langkah 1.
- [ ] `tex:993-1002` Estimasi pekerjaan: ganti koefisien POI dengan indeks volume nonhunian GHSL (epoch 2020, interpolasi dari observasi 2018). Kalibrasi ke pekerjaan menurut tempat kerja kab/kota diberi label S (C10).
- [ ] `tex:1004-1010` OD sintetis: ikuti keputusan ❓ di §1.
- [ ] `tex:1018-1035` CCTV: fokuskan pada *screenline* terarah di batas DKI, validasi manual, dan batas tafsir (bukan OD). SUMO hanya bila dikombinasikan dengan CCTV (C5).
- [ ] `tex:1043-1052` Etika dan lisensi: tambahkan desain kepatuhan Google (hanya *place ID*, kode kecamatan, dan kategori yang disimpan; koordinat dan nama tidak), lisensi GHSL (CC BY 4.0), dan status lisensi GTFS/Kemenperin yang belum jelas (C9).
- [ ] `tex:1070-1087` Langkah 2: delineasi berdasarkan massa (B2).
- [ ] `tex:1089-1173` Langkah 3:
  - tingkat 1: integrasi = % komuter ke inti (WSM);
  - tingkat 2: metrik OD kab/kota;
  - aksesibilitas (perutean OSM/GTFS) tetap terpisah (C3, C6).
- [ ] `tex:1175-1225` Langkah 4:
  - layanan: model binomial negatif (nilai nol tetap ikut);
  - pekerjaan: model log-linear;
  - keduanya dengan *leave-one-out* dan residu per domain; inferensi kemiringan (B1, C6).
- [ ] `tex:1227-1248` Langkah 5: manfaat = akses kumulatif (tingkat 1) dan upah (tingkat 2); beban = waktu tempuh ke inti (tingkat 1) dan durasi/biaya (tingkat 2). Tidak memakai orientasi arus (B4).
- [ ] `tex:1250-1356` Langkah 6: seragamkan tipologi (D); ambang ditetapkan sebelum klasifikasi.
- [ ] `tex:1358-1382` Langkah 7: daftar sensitivitas sesuai baris ketahanan C6, termasuk masker fasilitas layanan pada GHSL dan analisis tanpa Google. Hapus "S-1" (`tex:1374`) (D).
- [ ] `tex:1384-1426` Langkah 8: Web GIS dan *what-if* tetap, lebih ringkas; Web GIS hanya menampilkan agregat Google (C5, C9).
- [ ] `tex:1483-1507` Multitemporal: komuter 2014/2019/2023; Podes 2018/2021/2024 bila sebanding (📥); GHSL tidak dipakai untuk perubahan (C4, koreksi C10).
- [ ] **Caption:** beri nomor dan judul pada enam tabel `\LTcaptype{none}` (D).

## 5. Bab 4 Gambaran Umum

- [ ] `tex:1601-1607` Tambah konteks kebijakan: UU 2/2024 (Kawasan Aglomerasi, termasuk Cianjur) dan Perpres 60/2020 (C7, C8). Berkasnya sudah ada.
- [ ] `tex:1611-1631` Satukan dua peta batas administratif; lihat §7 (F).
- [ ] `tex:1639-1667` Demografi: tambah baris DKI, luas, dan kepadatan; putuskan tahun 2024 (sejajar Podes/WSM) atau 2023 (sejajar komuter) (C7). 📥
- [ ] **Subbab baru, struktur ekonomi:** PDRB per sektor per kab/kota (C7). 📥
- [ ] **Subbab baru, pola komuter:** angka 2023 (sekitar 3,6 juta komuter; asal terbanyak Kabupaten Bogor) dan perbandingan 2014/2019 (C4, C7). 📥
- [ ] `tex:1669-1675` Morfologi: peta volume terbangun dan nonhunian dari GHSL, dengan label epoch 2020 hasil interpolasi. Berkasnya sudah ada.
- [ ] `tex:1677-1684` Jaringan: peta jaringan eksisting dari OSM dan GTFS; JUTPI 2045 sebagai lapisan rencana. Hapus kalimat CCTV/SUMO (C5, F).
- [ ] `tex:1686-1692` Industri: peta kawasan industri Kemenperin (berkas sudah ada) dan kota baru skala besar.
- [ ] `tex:1694-1709` Kandidat: ganti dengan aturan massa (B2); hapus penggabungan Tangerang–Tangsel; pindahkan paragraf CCTV/SUMO (`tex:1709`) ke Bab 3 (C5).
- [ ] `tex:1715-1745` Tabel audit sumber: perbarui dengan sumber aktual beserta tahun dan statusnya (C7).
- [ ] Tambah peta persentase komuter ke inti per kecamatan dari WSM (F). 📥

## 6. Bibliografi (`latex/references.bib`) (E)

- [ ] **Perbaikan metadata:**
  - `otsuka2025`: *A three-layer model of borrowed size: empirical insights from Japan*, *Regional Studies, Regional Science* 12(1): 975–995.
  - `sadewoetal2021` dan `sadewoetal2023`: nama penulis Erie Sadewo, Anzhelika Antipova, dan Long Cheng; artikel 2021 terbit di *Asian Geographer*.
  - `burgermeijers2016`: 95(1): 5–16.
  - `durantonpuga2004`: entri bab *Handbook*, bukan artikel.
  - `andani2021`: lengkapi metadata.
  - `volgmannrusche2020`: cek tahun terbit.
- [ ] **Entri baru:**
  - Alonso (1973);
  - UU 2/2024; Perpres 60/2020;
  - BPTJ 2024;
  - Kemenperin 2025;
  - GHSL R2023A;
  - GTFS TransJakarta;
  - Statistik Potensi Desa 2024 (per kab/kota);
  - WSM 2024;
  - Statistik Komuter 2014/2019/2023.
- [ ] Opsional: Otsuka, *Borrowed Size and Regional Resilience: Lessons from Japan* (Springer). Kandidat lain (Meijers dkk. 2018; Cardoso & Meijers 2016; van Meeteren dkk. 2016) diverifikasi dulu.

## 7. Figure (F)

- [ ] **Gambar 1.1:** kotak pertanyaan biasa (bukan belah ketupat besar); maksimal 2 domain; beban langsung ke gerbang; kelas hasil sama dengan tipologi; ekspor vektor; simpan perintah `mmdc`.
- [ ] **Gambar 2.1:** notasi $S, X, F, \hat F, R, I, Z$; manfaat dan beban sebagai pengukuran sejajar; nama hasil mengikuti Tabel 2.2; perbaiki label "F-hat" yang terpotong.
- [ ] **Gambar 3.1:** diagram alir vertikal dengan gerbang dan cabang dua tingkat; istilah Indonesia.
- [ ] **Gambar 4.1 + 4.2:** satu peta dengan proyeksi UTM 48S, isi laut, kabupaten tetangga termasuk Cianjur, inset Jawa, catatan Kepulauan Seribu, koma desimal, label tidak menabrak batas; catat skrip SVG→PNG.
- [ ] **Gambar 4.3:** gambar ulang jaringan eksisting (garis penuh) dan rencana JUTPI (garis putus); cantumkan halaman sumber.
- [ ] **Gambar 4.4:** ganti dengan peta kecamatan berdasarkan massa; titik diturunkan dari koordinat, bukan piksel manual.
- [ ] **Peta baru:**
  - kepadatan per kecamatan;
  - % komuter ke inti (WSM);
  - arus OD kab/kota 2023;
  - volume nonhunian GHSL;
  - kawasan industri;
  - diagram keputusan cadangan di Bab 3.
- [ ] **Gaya seragam:** satu font dan palet; format caption "Judul. Sumber: … (hlm.)".

## 8. Penutup revisi

- [ ] Periksa konsistensi istilah: DKI/DK Jakarta, pusat sekunder, residu, dan nama kelas tipologi.
- [ ] Kurangi pengulangan kalimat pengaman ("tidak otomatis" muncul 10×).
- [ ] Kompilasi ulang (XeLaTeX + Biber) dan periksa PDF secara visual per halaman. Aturan vault: jalankan hanya atas permintaan pengguna.
- [ ] Perbarui file isu per bab di `output/naskah/bab_*/…_issues.md`, atau tandai sebagai historis.
