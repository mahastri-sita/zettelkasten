# TODO Revisi Naskah Bab 1–4

> **Objek:** `latex/tga_pwk_jakarta_bab_1_4_final.tex`. Rujukan baris `tex:NNN` mengacu ke versi 27 September 2026 dan akan bergeser setelah edit pertama. Kerjakan dari bawah ke atas, atau cari ulang dengan kata kunci.
> **Dasar:** `output/naskah/evaluasi_substansi_dan_eksekusi_bab_1_4_draf.md`. Kode dalam kurung (B1, C6, D, …) merujuk ke butir evaluasi itu.
> **Status:** peta kerja, bukan kontrak. Belum ada perubahan pada `.tex`.

Penanda: 📥 = butuh berkas yang belum diunduh; ❓ = butuh keputusan pengguna.

## Cara memakai daftar ini

Daftar ini disusun **sebelum** isi data dan publikasi dibaca. Fungsinya menjaga konteks dan arah, bukan mengunci langkah.

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
- Dua butir yang ditolak pengguna tidak diangkat lagi: kritik "skala" *borrowed size* dan perluasan ke Cianjur.

**Lentur (usulan awal; boleh berubah setelah data dibaca dan didiskusikan):**
- indikator spesifik, sumber per indikator, dan isi tabel operasionalisasi;
- bentuk model statistik dan daftar sensitivitas;
- isi dan jumlah subbab Bab 4;
- daftar gambar dan pembagian pembuatnya;
- urutan pengerjaan dan rujukan baris `tex:NNN`.

**Mode kerja yang diharapkan:**
1. Jelajahi dulu data dan publikasi yang relevan di `source/`.
2. Laporkan apa yang ditemukan dan apa artinya bagi rencana ini.
3. Diskusikan dengan pengguna; bertanya itu diharapkan, bukan dihindari.
4. Baru setelah itu mengedit, per bagian.

Jika data bertentangan dengan suatu butir di daftar ini, angkat ke pengguna dan sesuaikan daftarnya. Jangan memaksakan butirnya, dan jangan diam-diam menyimpang.

**Membaca tabel publikasi.** Banyak tabel BPS berupa gambar. Alat OCR dan aturan verifikasi angkanya ada di `HANDOFF.md` bagian "Cloud environment". Angka hasil OCR dicocokkan dengan baris total sebelum dipakai.

**Status data per commit `34af8cf` (2 Oktober 2026).** Data dari laptop lain sudah di-push dan sudah dicocokkan dengan §0.1.
- Publikasi BPS ada di **dua tempat** dengan isi identik: `source/official-document/` (nama "Institusi - Tahun - Judul", dengan catatan sumber) dan `source/dataset/` (nama snake_case, tanpa catatan). Pakai salinan `official-document/` sampai duplikatnya dirapikan (§0.5).
- Yang masih kurang: 12 *Kecamatan Dalam Angka* Kota Bekasi, dan tabel upah formal Banten (tidak tersedia).

## 0. Prasyarat

### 0.1 Unduhan manual BPS (situs BPS menolak unduhan otomatis)

Simpan di `source/official-document/`. Catatan sumber dapat dibuat agen setelah berkasnya ada.

- [x] *Statistik Komuter Jabodetabek 2023*: https://www.bps.go.id/id/publication/2024/03/28/33b6bef825944e576e7ea3ba/statistik-komuter-jabodetabek-hasil-survei-komuter-jabodetabek-2023.html
- [x] *Statistik Komuter Jabodetabek 2019*: https://www.bps.go.id/assets/publication/2019/12/04/eab87d14d99459f4016bb057/statistik-komuter-jabodetabek-2019.html
- [x] *Statistik Komuter Jabodetabek 2014*: https://www.bps.go.id/id/publication/2014/03/17/c0deaf751b807b56681a9860/statistik-komuter-jabodetabek--hasil-survei-komuter-jabodetabek-2014-.html
- [x] *Wilayah Statistik Metropolitan Indonesia 2024*: https://www.bps.go.id/id/publication/2026/05/29/61f2317887bfbf98ce596e5c/wilayah-statistik-metropolitan-indonesia-2024.html
- [ ] *Statistik Potensi Desa/Kelurahan 2024* untuk delapan kab/kota Bodetabek. Cari "Statistik Potensi Desa 2024" di masing-masing situs BPS kab/kota:
  - [x] Kabupaten Bogor: https://bogorkab.bps.go.id/id/publication/2024/12/24/1066acf5488fadafaa98eb72/statistik-potensi-desa-kabupaten-bogor.html
  - [x] Kota Bogor: https://bogorkota.bps.go.id/en/publication/2024/12/31/88486e40df9103aefbc1763b/publikasi-statistik-potensi-desa-kota--bogor-2024.html
  - [x] Kota Depok (depokkota.bps.go.id)
  - [x] Kabupaten Bekasi (bekasikab.bps.go.id)
  - [ ] Kota Bekasi (bekasikota.bps.go.id) — **publikasi Podes tidak ditemukan** (pencarian 2 Oktober 2026). Pengganti: *Kecamatan Dalam Angka 2025* untuk 12 kecamatan (data 2024), ditambah Tabel 4.2.3 *Kota Bekasi Dalam Angka 2025* (rumah sakit dan puskesmas per kecamatan).
    - Edisi 2025 (data 2024):
      - [ ] Bekasi Barat: https://bekasikota.bps.go.id/en/publication/2025/09/26/988fa1683590a87f810c6d14/kecamatan-bekasi-barat-dalam-angka-2025.html
      - [ ] Bekasi Selatan: https://bekasikota.bps.go.id/en/publication/2025/09/26/84b7f19ce05eb31a59de0bd0/kecamatan-bekasi-selatan-dalam-angka-2025.html
      - [ ] Bekasi Timur: https://bekasikota.bps.go.id/en/publication/2025/09/26/88f5d7ea28ad538a191114d3/kecamatan-bekasi-timur-dalam-angka-2025.html
      - [ ] Rawalumbu: https://bekasikota.bps.go.id/id/publication/2025/09/26/de57d2a5e5ce577fb1844fb1/kecamatan-rawalumbu-dalam-angka-2025.html
      - [ ] Jatiasih: https://bekasikota.bps.go.id/en/publication/2025/09/26/b248aa1726d5b343daa68fe6/jatiasih-district-in-figures-2025.html
      - [ ] Jatisampurna: https://bekasikota.bps.go.id/en/publication/2025/09/26/f23690b309af303d9512d617/jatisampurna-district-in-figures-2025.html
      - [ ] Bantargebang: https://bekasikota.bps.go.id/en/publication/2025/09/26/d901ae5b51f62c976db8db12/bantargebang-district-in-figures-2025.html
      - [ ] Mustikajaya: https://bekasikota.bps.go.id/en/publication/2025/09/26/18d81764fd0548eba554196c/kecamatan-mustikajaya-dalam-angka-2025.html
      - [ ] Pondokmelati: https://bekasikota.bps.go.id/en/publication/2025/09/26/eb56ee0ccee33d134c232c12/kecamatan-pondokmelati-dalam-angka-2025.html
    - Edisi 2025 belum ditemukan; tautan edisi 2024 (cek edisi 2025 di https://bekasikota.bps.go.id/id/publication):
      - [ ] Bekasi Utara: https://bekasikota.bps.go.id/en/publication/2024/09/26/554c33fc11a60bf7865f47fb/bekasi-utara-district-in-figures-2024.html
      - [ ] Medan Satria: https://bekasikota.bps.go.id/en/publication/2024/09/26/222d2ed041be6da0d1e212d3/medan-satria-district-in-figures-2024.html
      - [ ] Pondokgede: https://bekasikota.bps.go.id/en/publication/2024/09/26/c8909d6a52d96096bdcdfdb3/kecamatan-pondokgede-dalam-angka-2024.html
  - [x] Kabupaten Tangerang (tangerangkab.bps.go.id)
  - [x] Kota Tangerang (tangerangkota.bps.go.id)
  - [x] Kota Tangerang Selatan (tangselkota.bps.go.id)
  - [ ] Opsional: edisi 2021/2018 untuk memeriksa keterbandingan seri (C4) — **tidak ditemukan** untuk kedelapan kab/kota (pencarian 2 Oktober 2026). Seri tingkat kab/kota tampaknya baru ada sejak edisi 2024, sehingga perubahan fungsi layanan antarperiode tidak didukung seri ini.
- [x] *Provinsi DKI Jakarta Dalam Angka 2025*, *Jawa Barat Dalam Angka 2025*, dan *Banten Dalam Angka 2025*: penduduk, luas, dan kepadatan kab/kota.
- [x] *Dalam Angka* kedelapan kab/kota: penduduk per kecamatan 2024. Termasuk *Kota Depok Dalam Angka 2025* dan *Kota Tangerang Dalam Angka 2024*, yang menjadi sumber Tabel 4.1 saat ini.
- [x] *PDRB Kabupaten/Kota di Indonesia 2020–2024*: https://www.bps.go.id/id/publication/2025/06/10/ca543e942579ced46afd603b/produk-domestik-regional-bruto-kabupaten-kota-di-indonesia-2020-2024.html
- [x] *Keadaan Angkatan Kerja* Agustus 2023 untuk Jawa Barat, Banten, dan DKI (penduduk bekerja per kab/kota).
- [ ] Tabel upah per kab/kota: **sebagian besar sudah ada** di `source/dataset/` (commit `34af8cf`). Isi PDF belum diperiksa.
  - [x] DKI, upah pekerja formal per kota 2025 (CSV) dan pekerja informal 2024 (CSV).
  - [x] DKI, *Worker Profile of DKI Jakarta Province 2023* (PDF).
  - [x] Jawa Barat, *Pekerja Formal dan Informal* 2023 dan 2024 (PDF). Perlu dicek apakah memuat upah per kab/kota.
  - [x] Banten, pendapatan pekerja informal 2023 (CSV) dan UMK 2023 (CSV).
  - [ ] Banten, upah pekerja formal per kab/kota: tidak ditemukan. Pakai UMK sebagai konteks dan catat keterbatasannya.
  - Tautan asal:
  - [ ] Jawa Barat, *Pekerja Formal dan Informal 2024*: https://jabar.bps.go.id/en/publication/2025/06/23/7cf2d590c18b1d5d35749a64/pekerja-formal-dan-informal-provinsi-jawa-barat-2024.html
  - [ ] Jawa Barat, edisi 2023: https://jabar.bps.go.id/en/publication/2024/06/21/981d64e62ad058a22979ebfa/pekerja-formal-dan-informal-provinsi-jawa-barat-2023.html
  - [ ] DKI, *Profil Pekerja Provinsi DKI Jakarta 2023*: https://jakarta.bps.go.id/en/publication/2024/11/29/a29e22b34b24c47e608039a1/profil-pekerja-provinsi-dki-jakarta-2023.html
  - [ ] Banten, pendapatan pekerja informal per kab/kota 2023: https://banten.bps.go.id/en/statistics-table/1/ODYjMQ==/rata-rata-pendapatan-bersih-sebulan-pekerja-informal-menurut-kabupaten-kota-dan-lapangan-pekerjaan-utama-di-provinsi-banten-rupiah-2023.html
  - [ ] Banten, UMK per kab/kota: https://banten.bps.go.id/en/statistics-table/2/NDkxIzI=/upah-minimum-menurut-kabupaten-kota-di-provinsi-banten.html
  - Tabel upah formal per kab/kota untuk Banten tidak ditemukan.

### 0.2 Sudah diunduh agen (27 September 2026)

- [x] UU 2/2024, Perpres 60/2020 (batang tubuh), laporan BPTJ 2024, peta kawasan industri Kemenperin, GTFS TransJakarta, GHSL GHS-BUILT-V 2020 (total dan NRES).
- [ ] Opsional: pulihkan PDF JUTPI 3 dari git untuk mencatat halaman peta jaringan (Gambar 4.3): `git show "HEAD:source/official-document/JICA JUTPI 3 - 2025 - Project Completion Report.pdf" > /tmp/jutpi3.pdf`

### 0.3 Verifikasi setelah unduhan

- [ ] Hitung jumlah kecamatan non-DKI dari publikasi Podes/Dalam Angka; perkiraan saat ini sekitar 140 (C6).
- [ ] Baca definisi "inti" dan anomali ambang 15% vs 7% di WSM 2024 (C2).
- [ ] Periksa apakah publikasi komuter memuat tabel asal–tujuan 13×13 dan durasi/biaya per kab/kota asal (C1).
- [ ] Periksa tabel upah per kab/kota (C1).
- [ ] ❓ **Nama wilayah inti:** data Kemenperin 2025 sudah memakai "Daerah Khusus Jakarta". Pastikan status resmi per 2026, "DKI Jakarta" atau "Provinsi Daerah Khusus Jakarta", lalu seragamkan istilah di seluruh naskah.

### 0.4 Batas kecamatan (untuk peta dan analisis tingkat kecamatan)

geoBoundaries tidak menyediakan batas kecamatan (ADM3) untuk Indonesia; yang ada di vault hanya ADM2.

- [ ] Unduh *Indonesia - Subnational Administrative Boundaries* (COD-AB) dari HDX: https://data.humdata.org/dataset/cod-ab-idn
  - Sumber BPS; batas per April 2020; memuat Admin 3 (7.069 kecamatan); lisensi CC BY-IGO.
  - Ukuran 219 MB (GDB) sampai 498 MB (SHP). **Jangan di-commit**, karena melebihi batas 100 MB per berkas di GitHub. Simpan di lokal untuk QGIS; di vault cukup catatan sumber berisi URL dan versi.
  - Alternatif: layanan batas desa BIG (`geoservices.big.go.id/rbi/rest/services/BATASWILAYAH/Administrasi_AR_KelDesa_10K`), digabung ke kecamatan.
- [ ] Cocokkan daftar kecamatan pada batas 2020 dengan daftar kecamatan di publikasi 2024 (kemungkinan ada pemekaran atau perubahan nama).

### 0.5 Kebersihan repo (butuh keputusan pengguna; agen tidak menghapus berkas data)

- [ ] ❓ **38 PDF duplikat** (sekitar 600 MB): isi identik antara `source/dataset/*.pdf` dan `source/official-document/BPS … .pdf`. Menurut `source/AGENTS.md`, publikasi statistik resmi termasuk `official-document`. Usul: hapus salinan di `dataset/`.
- [ ] Tiga PDF baru yang hanya ada di `dataset/` (dua *Pekerja Formal dan Informal* Jawa Barat dan *Worker Profile* DKI) adalah publikasi. Usul: pindahkan ke `official-document/` dan buatkan catatan sumber.
- [ ] Empat CSV upah baru belum punya catatan sumber pendamping (URL, tanggal akses).
- [ ] Berkas sampah yang ikut ter-commit:
  - `source/dataset/statistik_potensi_desa_kabupaten_bogor_2025_qedoefda.pdf.part` (unduhan tidak selesai);
  - `source/official-document/Pembekalan-Kerja-Praktik-2025.pptx-1.pdf:Zone.Identifier`.
- [ ] Berkas kembar lain:
  - dua CSV upah formal Jawa Barat 2019 dengan isi sama;
  - J21 dan J26 (Henderson dkk. 1996) di `source/journal/`.

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

### 7.1 Aturan placeholder

Peta GIS dan gambar ulang jaringan dibuat **manual oleh pengguna** (QGIS atau perangkat lain). Agen tidak membuatnya. Agen memasang placeholder di `.tex` supaya penomoran, rujukan silang, dan tata letak tetap stabil.

- [ ] Tambahkan makro ke `latex/tga-preamble.tex`:

```latex
\newcommand{\GambarPlaceholder}[2][7cm]{%
  \fbox{\parbox[c][#1][c]{0.92\linewidth}{\centering\small
    \textbf{PLACEHOLDER GAMBAR}\\[0.6em]#2}}}
```

- [ ] Untuk setiap gambar manual, tulis caption dan label final sekarang; hanya isi gambarnya yang ditunda:

```latex
\begin{figure}[H]
  \centering
  \GambarPlaceholder{Peta kepadatan penduduk per kecamatan, 2024.\\
    Berkas target: \texttt{figures/bab4\_kepadatan\_kecamatan.pdf}}
  \caption{Kepadatan penduduk per kecamatan di Jabodetabek, 2024. Sumber: …}
  \label{fig:bab4-kepadatan}
\end{figure}
```

- Setelah gambar jadi: simpan di `latex/figures/` dengan nama berkas target, ganti `\GambarPlaceholder{…}` dengan `\includegraphics[width=\textwidth]{…}`, lalu centang di tabel 7.2.
- **Gambar lama yang isinya bertentangan dengan keputusan baru** (diagram 1.1, 2.1, 3.1 dan peta kandidat 4.4) langsung diganti placeholder.
- **Gambar lama yang isinya tidak salah** (peta administratif, peta JUTPI) tetap dipakai sementara dan ditandai "sementara" di tabel 7.2.

### 7.2 Daftar gambar

| ID | Berkas target (`latex/figures/`) | Isi | Pembuat | Data | Sementara di naskah | Selesai |
|---|---|---|---|---|---|---|
| G1.1 | `bab1_logika_penelitian` | Logika penelitian: kotak pertanyaan biasa; 2 domain; beban langsung ke gerbang; kelas hasil mengikuti tipologi | **Agen** mengedit `.mmd`; render dengan `mmdc` (di lokal bila cloud tidak bisa) | — | Placeholder sampai dirender | [ ] |
| G2.1 | `bab2_kerangka_konseptual` | Kerangka konseptual: notasi $S, X, F, \hat F, R, I, Z$; manfaat dan beban sejajar; nama hasil mengikuti Tabel 2.2 | **Agen** (`.mmd`) + render | — | Placeholder | [ ] |
| G3.1 | `bab3_alur_analisis` | Diagram alir vertikal dua tingkat dengan gerbang bukti; istilah Indonesia | **Agen** (`.mmd`) + render | — | Placeholder | [ ] |
| G3.2 | `bab3_keputusan_cadangan` (baru) | Diagram keputusan: spesifikasi utama → cadangan bernama → pemicunya | **Agen** (`.mmd`) + render | — | Placeholder | [ ] |
| G4.1 | `bab4_admin_status` | Batas dan status administratif (gabungan Gambar 4.1 dan 4.2) | **Manual** | `source/dataset/geoboundaries_idn_adm2_simplified.geojson` | Gambar lama `bab4_status_administratif.png`; `bab4_admin.png` dihapus dari naskah | [ ] |
| G4.2 | `bab4_kepadatan_kecamatan` (baru) | Kepadatan penduduk per kecamatan, 2024 | **Manual** | Batas kecamatan (lihat §0.4) + penduduk dan luas per kecamatan dari *Dalam Angka* kab/kota | Placeholder | [ ] |
| G4.3 | `bab4_komuter_od_2023` (baru) | Arus komuter antar kab/kota 2023 (peta alir atau diagram kord) | **Manual** | Tabel asal–tujuan *Statistik Komuter 2023* + batas ADM2 | Placeholder | [ ] |
| G4.4 | `bab4_komuter_ke_inti_kecamatan` (baru) | Persentase komuter ke inti per kecamatan | **Manual** | WSM 2024 + batas kecamatan | Placeholder | [ ] |
| G4.5 | `bab4_terbangun_nonhunian` (baru) | Volume terbangun total dan nonhunian (GHSL, epoch 2020 hasil interpolasi) | **Manual** | Dua ZIP `GHS_BUILT_V_*_R10_C29` di `source/dataset/` | Placeholder | [ ] |
| G4.6 | `bab4_jaringan_eksisting` | Jaringan eksisting (KRL, MRT, LRT Jabodebek, TransJakarta, tol) garis penuh; rencana JUTPI 2045 garis putus | **Manual** | OSM (rel dan tol), `transjakarta_file_gtfs_2026_09_27.zip`, PDF JUTPI 3 (catat halaman sumber) | Gambar lama `bab4_network_jutpi.png` | [ ] |
| G4.7 | `bab4_kawasan_industri` (baru) | Kawasan industri formal dan kota baru skala besar | **Manual** | `data_dukung_kawasan_industri_125_ki.zip` (keluarkan Cikembar, Sukabumi); kota baru didigitasi dari OSM/literatur | Placeholder | [ ] |
| G4.8 | `bab4_pusat_berdasarkan_massa` | Kecamatan kandidat pusat berdasarkan massa (pengganti peta kandidat lama) | **Manual** | Penduduk per kecamatan + luas terbangun GHSL + batas kecamatan; ambang massa dari Bab 3 | Placeholder; `bab4_candidates.png` dihapus dari naskah | [ ] |

**Spesifikasi untuk semua peta manual:**
- Proyeksi UTM 48S (EPSG:32748); *extent* sama untuk semua peta.
- Laut diisi warna; kabupaten tetangga (termasuk Cianjur) abu-abu sebagai konteks; inset Pulau Jawa; catatan Kepulauan Seribu.
- Skala batang dan arah utara; koordinat tepi memakai koma desimal ("6,2° LS").
- Label tidak menabrak garis batas; penamaan konsisten ("Kota Depok", "Kota Tangerang Selatan").
- Satu font dan satu palet untuk semua gambar.
- Ekspor PDF vektor, atau PNG minimal 300 dpi pada lebar 160 mm.
- Sumber dan tahun data ditulis di caption, bukan di dalam gambar.

**Dukungan agen untuk peta manual:**
- [ ] ❓ Menyiapkan tabel siap-*join* (CSV per kecamatan dan per kab/kota dengan kode wilayah) dari publikasi BPS, supaya pengguna tinggal menggabungkannya di QGIS. Ini transformasi data, jadi tempatnya di `calculation/` dan **perlu izin eksplisit** pengguna.
- [ ] Menuliskan caption, sumber, dan catatan batas tafsir untuk setiap gambar di `.tex`.

### 7.3 Gaya seragam

- [ ] Format caption: "Judul. Sumber: … (hlm.)".
- [ ] Catat perintah render diagram (`mmdc -i <berkas>.mmd -o <berkas>.pdf`) dan langkah ekspor peta, supaya dapat diulang.

## 8. Penutup revisi

- [ ] Periksa konsistensi istilah: DKI/DK Jakarta, pusat sekunder, residu, dan nama kelas tipologi.
- [ ] Kurangi pengulangan kalimat pengaman ("tidak otomatis" muncul 10×).
- [ ] Kompilasi ulang (XeLaTeX + Biber) dan periksa PDF secara visual per halaman. Aturan vault: jalankan hanya atas permintaan pengguna.
- [ ] Perbarui file isu per bab di `output/naskah/bab_*/…_issues.md`, atau tandai sebagai historis.
