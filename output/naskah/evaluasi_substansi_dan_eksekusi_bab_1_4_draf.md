# Evaluasi Substansi dan Eksekusi Naskah Bab 1–4 (draf)

> **Status:** draf kerja, bukan keputusan pembimbing.
> **Tanggal:** 27 September 2026; diperbarui 2 Oktober 2026 (§15: verifikasi data dan revisi `.tex`).
> **Objek:** `latex/tga_pwk_jakarta_bab_1_4_final.tex` (Bab 1–4, pra-TA).
> **Penyusun:** evaluasi AI (Claude) yang ditanggapi pengguna pada tanggal yang sama, dalam dua putaran tanggapan.
> **Catatan kerja induk:** [[skripsi_s1_borrowed_size_dan_agglomeration_shadow_jakarta]]

## 0. Cara membaca

Dokumen ini memisahkan empat jenis isi:

- **Temuan evaluasi**: hasil pembacaan AI atas naskah, dengan rujukan baris `tex:NNN`.
- **Tanggapan/keputusan pengguna**: posisi pengguna pada 27 September 2026. Ini posisi pengguna, bukan inferensi AI.
- **Usulan**: rekomendasi AI yang belum diputuskan.
- **Perlu dicek**: klaim yang belum diverifikasi ke sumber.

Status setiap poin:

| Status | Arti |
|---|---|
| Disepakati | Pengguna setuju; masuk revisi |
| Diubah | Pengguna setuju dengan koreksi arah |
| Ditolak | Pengguna tidak setuju; tidak ditindaklanjuti |
| Terbuka | Belum diputuskan |

## 1. Ringkasan

Ide penelitian kuat dan matang untuk S1. Pertanyaannya tidak biner, dan naskah membedakan dengan tegas ukuran, fungsi, dan kinerja; aksesibilitas dan integrasi yang terealisasi; serta morfologi dan relasi. Gerbang bukti sebelum label *borrowed size* atau *agglomeration shadow* adalah kekuatan utama.

Kelemahan utama ada pada perumusan desain. Bab 3 masih berupa kumpulan aturan bersyarat tanpa spesifikasi utama yang dikunci. Empat masalah struktural perlu diperbaiki sebelum eksekusi:

1. Tolok ukur internal membuat tanda residu menjadi mekanis (B1).
2. Kandidat pusat dipilih dari variabel hasil (B2).
3. Integrasi dan beban memakai indikator yang sama (B4).
4. Unit relasi teramati tidak cocok dengan unit analisis (C1).

**Koreksi atas evaluasi awal:** tahap pra-TA hanya mewajibkan Bab 1–4 tanpa eksekusi. Karena itu, belum adanya data atau kalkulasi Jakarta di vault **bukan** masalah naskah.

## 2. Keputusan pengguna (27 September 2026)

**Sikap data:**
- Penelitian sepenuhnya bertumpu pada sumber terbuka dan proksi, terutama OSM.
- Data formal/resmi bersifat opsional, bukan kewajiban. Data resmi tetap dipakai apabila terbuka.
- Pengguna menilai jalur sumber terbuka lebih unggul.

**Pengadaan data:**
- Tidak membeli data BPS (termasuk mikrodata SILASTIK).
- Tidak bergantung pada pengajuan data. Pengajuan mungkin dicoba kelak, tetapi bukan syarat desain.

**Relasi dan observasi:**
- CCTV dipakai.
- Pengamatan langsung dilakukan jika diperlukan.

**Data yang dipakai:**
- Podes dan semua data terbuka lain.
- Publikasi Survei Komuter Jabodetabek yang bebas diakses.
- Jarak dan perjalanan dihitung langsung, lalu dicek terhadap rute yang ada.

**Lingkup wilayah:** Kabupaten Cianjur tidak ditambahkan (lihat C8).

**Putaran 2 (27 September 2026):**
- **Fasilitas:** dikumpulkan dengan Google Maps Platform (Places API). Pengguna tidak keberatan membayar karena pengambilan dilakukan sekali (statis). Syarat layanannya dibahas di C9.
- **Domain utama:** layanan **dan** pekerjaan, dengan proksi kreatif (C10).
- **Cakupan data kecamatan:** Jabodetabek saja. Ini interpretasi AI atas "jabodetabek aja" dan menjawab §13 no. 3: tanpa pembanding eksternal.
- **SUMO:** dikeluarkan, kecuali dikombinasikan dengan CCTV.
- **Web GIS dan *what-if*:** tetap masuk; yang dikurangi hanya frekuensi penyebutannya.
- **Peran CCTV:** *screenline* terarah di batas DKI (usulan C1) disetujui.
- **Judul:** "Jabodetabek", dengan syarat pilihan ini tidak membawa konsekuensi substantif. Menurut evaluasi, syarat ini terpenuhi (C8).
- **Contoh data kecamatan:** pengguna menambahkan `source/official-document/statistik-potensi-kelurahan-kota-jakarta-utara.pdf` sebagai contoh data Podes tingkat kecamatan (C2).

**Putaran 3 (27 September 2026):**
- **Unit:** desain dua tingkat disetujui (C3).
- **Google:** data Google hanya dipakai untuk menghitung, nama tempat tidak disimpan. Menurut pengguna, Google tetap dipatuhi, tetapi seluruh kebutuhan penelitian harus terpenuhi (C9).
- **Proksi pekerjaan:** pengguna meminta rekomendasi AI (C10).

## 3. Status per poin

| Poin | Pokok | Status |
|---|---|---|
| B1 | Tolok ukur internal membuat tanda residu mekanis | Disepakati |
| B2 | Kandidat pusat dipilih dari variabel hasil | Disepakati (perubahan perspektif) |
| B3 | Domain pekerjaan × komuter keluar | Diubah |
| B4 | Integrasi dan beban memakai indikator sama | Disepakati |
| B5 | Ketidakcocokan skala teori | Ditolak |
| B6 | Proposisi tidak dapat difalsifikasi; penjelasan alternatif tidak dinamai | Disepakati |
| C1 | Unit dan jumlah amatan | Diubah (tanpa mikrodata) |
| C2 | Sumber tingkat kecamatan belum dipakai | Disepakati; publikasi Podes per kecamatan yang terbuka ditemukan |
| C3 | Desain dua tingkat | Diputuskan (putaran 3) |
| C4 | Dimensi waktu | Disepakati |
| C5 | Cakupan melebar | Diubah: SUMO keluar (kecuali dengan CCTV); Web GIS dan *what-if* tetap, penyebutan dikurangi |
| C6 | Kunci desain dan tabel operasionalisasi | Disepakati; diterapkan di Bab 3 (2 Oktober 2026, §15) |
| C7 | Bab 4 tipis sebagai gambaran umum | Disepakati; unduh berkas dulu |
| C8 | Judul vs Kabupaten Cianjur | Diputuskan: judul memakai "Jabodetabek"; Cianjur tidak dicakup |
| C9 | Google Maps Platform untuk fasilitas | Diputuskan pengguna; perlu desain kepatuhan |
| C10 | Proksi untuk dua domain utama | Disepakati (putaran 4) |
| D | Inkonsistensi internal | Disepakati |
| E | Bibliografi | Disepakati |
| F | Touch-up figure | Disepakati |

## 4. Bagian A — Kekuatan yang dipertahankan

- Konstruk dipisahkan dengan jelas: ukuran lokal, fungsi, dan kinerja; aksesibilitas dan integrasi yang terealisasi; polisentrisitas morfologis dan fungsional.
- Kesadaran sirkularitas: indikator pembentuk relasi tidak dipakai lagi sebagai hasil, dan OD sintetis tidak diuji terhadap massa tujuannya (`tex:153`, `tex:1470-1474`).
- Label *shadow* mensyaratkan bukti beban yang terpisah. Tanpa bukti itu, kelasnya "terintegrasi tetapi tertinggal" (`tex:405-409`).
- Prosedur *leave-one-out*, dan DKI dikeluarkan dari garis ekspektasi.
- Klaim celah dibatasi pada korpus yang ditelusuri. Pencarian cepat 27 September juga tidak menemukan studi *borrowed size* atau *shadow* untuk Indonesia (bukan penelusuran sistematis).

## 5. Bagian B — Masalah pada tingkat ide

### B1. Tolok ukur internal membuat tanda residu mekanis — Disepakati

**Temuan** (`tex:129`, `tex:223`, `tex:1215-1225`):
- Ekspektasi dibentuk hanya dari pusat sekunder Jabodetabek, sehingga residu berpusat di nol karena cara hitungnya. Kira-kira separuh unit pasti bertanda negatif.
- Akibatnya, kelas "integrasi tinggi + residu negatif" pada Tabel 2.2 sebagian terisi otomatis.
- *Shadow* adalah defisit pada tingkat sistem. Jika seluruh pinggiran sama-sama tertekan, tolok ukur internal tidak dapat menangkapnya.
- Literatur rujukan (Burger dkk. 2015; Meijers dkk. 2016) membaca *shadow* dari **koefisien** kedekatan atau jaringan terhadap fungsi, bukan dari tanda residu per unit.

**Tindak lanjut:**
- Inferensi utama Q3 menjadi **kemiringan hubungan residu terhadap integrasi**. Tipologi hanya ringkasan akhir.
- Implementasi (putaran 2): kemiringan di dalam Jabodetabek saja, tanpa pembanding eksternal. Ini interpretasi AI atas "jabodetabek aja" (lihat §13).

### B2. Kandidat pusat dipilih dari variabel hasil — Disepakati (perubahan perspektif)

**Penjelasan.** Masalahnya bukan Jakarta sebagai kandidat, melainkan **cara memilih kandidat pusat sekunder**.
- Bab 3 memilih kandidat dari "konsentrasi aktivitas dan fungsi" (pekerjaan, layanan, kawasan industri) (`tex:755-763`, `tex:1074-1079`).
- Padahal fungsi adalah hal yang kemudian diukur sebagai hasil, yaitu residu fungsi.
- Akibatnya, hanya tempat yang fungsinya sudah menonjol yang masuk daftar. Tempat berpenduduk besar tetapi berfungsi sedikit, yang justru kandidat terkuat korban *shadow*, tidak pernah masuk analisis.
- Analogi: meneliti apakah suatu kondisi membuat tanaman kerdil, tetapi sampel hanya diambil dari tanaman yang sudah tinggi.
- Uji mengeluarkan satu indikator (`tex:760-763`) tidak menyelesaikan masalah ini. Penyaringannya terjadi sebelum pengukuran.

**Perbaikan:**
- Pilih unit berdasarkan **massa saja** (penduduk dan luas terbangun), bukan fungsi.
- Alternatif lain: analisis semua kecamatan, lalu tandai "pusat sekunder" sebagai subkelompok berdasarkan ambang massa yang ditetapkan sebelum fungsi dihitung.
- Daftar lima kandidat di Gambar 4.4 diganti mengikuti aturan ini.

### B3. Domain pekerjaan × komuter keluar — Diubah

**Temuan awal.** Kawasan hunian otomatis punya residu pekerjaan negatif sekaligus arus keluar tinggi ke DKI, sehingga pasangan ini berisiko tautologis (`tex:151`, `tex:1470`).

**Tanggapan pengguna.** Kawasan hunian dan *shadow* tidak saling meniadakan. Kawasan hunian justru dapat menjadi korban *shadow*, dan penelitian dapat membuka gagasan tentang cara memperlakukan kawasan hunian dengan lebih baik.

**Rekonsiliasi.** Tanggapan pengguna benar: kawasan hunian tidak otomatis dikecualikan dari *shadow*. Evaluasi awal keliru jika dibaca sebagai "hunian bukan *shadow*". Yang tersisa adalah **persoalan pengukuran**:
- Pada domain pekerjaan, kawasan hunian karena memang direncanakan sebagai kota tidur dan kawasan hunian karena tertekan *shadow* memberi sinyal yang sama: residu pekerjaan negatif dan arus keluar tinggi.
- Agar klaim *shadow* pada kawasan hunian dapat dipertahankan, dibutuhkan indikator pembeda.

**Tindak lanjut.** Kawasan hunian dimasukkan sebagai kemungkinan korban *shadow*, dengan salah satu syarat pembeda berikut:
1. **Domain layanan.** Penduduk yang besar menciptakan permintaan layanan lokal. Jika layanan tetap defisit sementara orientasi ke inti tinggi, itu tanda kebocoran permintaan ke inti, yaitu mekanisme *shadow* yang lebih jelas daripada defisit pekerjaan.
2. **Pembanding sejenis.** Bandingkan kecamatan hunian bermassa serupa pada tingkat integrasi yang berbeda (gradien).
3. **Kontrol karakter hunian.** Misalnya rasio luas terbangun nonhunian terhadap total terbangun (GHSL).

Gagasan pengguna tentang cara memperlakukan kawasan hunian dengan lebih baik dapat menjadi arah **manfaat praktis dan rekomendasi** Bab 6.

### B4. Integrasi dan beban memakai indikator yang sama — Disepakati

**Temuan:**
- Langkah 3 memakai orientasi menuju DKI dan rasio arus masuk-keluar sebagai **integrasi** (`tex:1164-1168`).
- Langkah 5 memakai orientasi yang sangat bergantung pada inti dan ketidakseimbangan arus sebagai **beban** (`tex:1236-1238`).
- Aturan yang ada hanya memisahkan beban dari residu, bukan dari integrasi. Syarat "integrasi tinggi + beban tinggi" untuk label *shadow* menjadi sebagian tautologis.

**Tindak lanjut:**
- Setiap indikator hanya boleh memegang satu peran.
- Beban diambil dari durasi, jarak, dan biaya perjalanan, bukan dari orientasi arus.
- Aturan yang sama berlaku untuk waktu tempuh hasil perutean: tidak boleh sekaligus menjadi aksesibilitas dan beban (lihat C1).

### B5. Ketidakcocokan skala teori — Ditolak

**Temuan awal.** *Borrowed size* berasal dari kota kecil di wilayah polisentris Eropa, sedangkan unit Jabodetabek berpenduduk 1–5,7 juta.

**Tanggapan pengguna.** *Borrowed size* bukan soal skala absolut. Konsep ini menyangkut makna relatif: fungsi yang disandang suatu tempat dibandingkan dengan ukurannya ketika tempat itu disebut kota.

**Tindak lanjut.** Tidak ada. Satu-satunya unsur yang tetap berlaku adalah sitasi asal-usul konsep (Alonso 1973), yang sudah masuk Bagian E.

### B6. Proposisi tidak dapat difalsifikasi — Disepakati

**Temuan:**
- Semua proposisi (`tex:383-392`) berbentuk "dapat … tetapi tidak harus", sehingga semua hasil kompatibel.
- "Penjelasan alternatif" di Q3 tidak pernah disebut satu per satu.

**Tindak lanjut.** Draf proposisi berarah dan daftar penjelasan alternatif ada di §10.

## 6. Bagian C — Masalah pada tingkat eksekusi

### C1. Unit dan jumlah amatan — Diubah (tanpa mikrodata)

**Temuan:**
- Definisi komuter BPS adalah pekerja yang melintasi batas **kabupaten/kota**.
- Menurut halaman produk SILASTIK yang tersimpan di `source/dataset/bps_silastik_survei_komuter_jabodetabek_2023_detail_produk.html`:
  - tempat kerja hanya tercatat pada tingkat kabupaten (`B4R412A_KA`);
  - Level Penyajian: Kabupaten.
- Akibatnya:
  - Relasi terarah yang teramati hanya tersedia sebagai matriks kab/kota, dengan 8 unit non-DKI.
  - Cikarang tidak dapat dipisahkan dari Kabupaten Bekasi.
  - Penggabungan "Tangerang–Tangsel" pada Gambar 4.4 bertentangan dengan unit data, yang memisahkan keduanya.
  - Regresi Q3 atau *leave-one-out* dengan 5–8 titik tidak bermakna.

**Keputusan pengguna:**
- Mikrodata SILASTIK tidak dipakai.
- Relasi kab/kota diambil dari publikasi Survei Komuter yang bebas diakses.
- CCTV dan pengamatan langsung dipakai.

**Konsekuensi.** Janji Bab 1 untuk menunjukkan penerima manfaat dan penanggung beban (`tex:82`) harus diturunkan ke apa yang ditabulasikan publikasi, yaitu profil per kab/kota asal. Tanpa mikrodata, analisis menurut karakteristik individu (upah, biaya per orang) tidak tersedia kecuali publikasi menabulasikannya. **Perlu dicek** isi tabel publikasi 2023.

**Pertanyaan pengguna — apakah data upah ada?**
- **Tingkat kab/kota:**
  - Beberapa BPS provinsi menerbitkan tabel terbuka "Rata-rata Upah/Gaji Bersih Sebulan Pekerja Formal menurut Kabupaten/Kota". Tabel ini terlihat untuk Jawa Tengah, NTT, dan Sumatera Barat. Untuk Jawa Barat, Banten, dan DKI **belum dipastikan**.
  - UMK terbuka (misalnya di opendata Jawa Barat), tetapi itu upah minimum regulatif, bukan upah aktual.
  - Upah Sakernas tercatat menurut tempat tinggal pekerja, bukan tempat kerja.
- **Tingkat kecamatan:** tidak ditemukan data terbuka.
- **Implikasi:** upah hanya dapat masuk profil manfaat di tingkat kab/kota, dengan status A dan N kecil.

**Pertanyaan pengguna — jarak dan perjalanan dihitung langsung:**
- Dapat dilakukan. Perutean jaringan OSM (misalnya OSRM atau r5) memberi jarak dan waktu tempuh arus bebas, dan GTFS TransJakarta memberi waktu terjadwal.
- Statusnya **aksesibilitas atau beban potensial (P)**, bukan waktu tempuh yang dialami. Kemacetan tidak terekam dalam OSM.
- Pemeriksa independen: durasi dan biaya rata-rata per kab/kota dalam publikasi Statistik Komuter 2023.
- Mengikuti B4, waktu tempuh hasil perutean dipakai sebagai aksesibilitas **atau** beban, tidak keduanya. Jika keduanya diperlukan, konstruksinya harus dibedakan dan dinyatakan.

**CCTV — peran (disetujui pengguna pada putaran 2):**
- **Hitungan terarah di titik penyeberangan batas DKI** (*screenline/cordon*) pada koridor utama, pagi dan sore.
  - Hasil: arah dan asimetri volume per koridor, yang mendukung Q1.
  - Hasil yang sama dapat dipakai untuk memeriksa estimasi relasi.
- **Batas:**
  - Hitungan kendaraan di satu ruas bukan pasangan asal-tujuan.
  - Lalu lintas tembus ikut terhitung.
  - Konversi kendaraan ke orang memerlukan asumsi okupansi, dan sepeda motor dominan.
- Rekaman CCTV **belum ada di vault**. Sumber rekaman, izin, dan cakupan waktunya perlu dicatat sebelum modul ini dijanjikan di Bab 3.
- **Pengamatan langsung:**
  - sampel hitung manual untuk memvalidasi hitungan YOLO;
  - verifikasi lapangan fasilitas pada sampel terarah.

### C2. Sumber terbuka tingkat kecamatan — Disepakati dengan catatan Podes

**Temuan.** Audit data 24 Agustus sudah menemukan sumber tingkat kecamatan, tetapi naskah hampir tidak memakainya. WSM disebut 1 kali, Podes 0 kali, dan tabel audit Bab 4 tidak memuat keduanya.
- **WSM 2024 (BPS, publikasi terbuka):** persentase komuter per kecamatan menuju inti, berbasis data posisi ponsel Agustus 2024.
  - Ada anomali ambang 15% vs 7% yang harus dicatat.
  - Kelas inti/periferi WSM tidak boleh menjadi kebenaran dasar.
  - **Perlu dicek** definisi "inti" dalam WSM Jabodetabek.
- **Bangkitan dan tarikan perjalanan 182 kecamatan (BPTJ):** tabel marginal hasil *sketch planning*, berstatus S. Bukan arus teramati.

**Catatan Podes (diperbarui putaran 2):**
- Mikrodata Podes desa di SILASTIK berbayar (Rp 4.140.165 untuk 2024, menurut halaman produk di vault), sehingga tidak dipakai.
- **Temuan putaran 2:** BPS kab/kota menerbitkan secara terbuka *Statistik Potensi Desa/Kelurahan 2024* dari hasil Podes 2024. Contoh yang diperiksa adalah *Statistik Potensi Kelurahan Kota Jakarta Utara 2024* (BPS Kota Jakarta Utara, Desember 2024; 275 halaman PDF). Isinya:
  - **Bab III "Statistik Infrastruktur" (Tabel 19–21)** memuat **jumlah fasilitas per kecamatan**: SD sampai SMK, akademi/perguruan tinggi, rumah sakit dan rumah sakit bersalin, puskesmas, poliklinik dan apotek, kelompok pertokoan dan pasar, sarana perdagangan, akomodasi, bank, dan koperasi. Contoh Tabel 20.1 (hlm. 214): Penjaringan 6 rumah sakit, Tanjung Priok 9, total Jakarta Utara 25.
  - **Bab I** (misalnya Tabel 4.4, hlm. 62) memuat **banyaknya kelurahan yang memiliki fasilitas** per kecamatan. Ini ukuran keberadaan, bukan jumlah fasilitas.
  - Tabelnya berupa gambar tanpa lapisan teks, sehingga perlu OCR (`ocrmypdf`) atau entri manual. Halaman isi p berada di halaman PDF p + 22.
- **Ketersediaan:**
  - Publikasi serupa tahun 2024 terverifikasi ada untuk Kabupaten Bogor (40 kecamatan) dan Kota Bogor.
  - **Pembaruan 2 Oktober 2026:** edisi 2024 dan 2025 sudah diunduh pengguna untuk tujuh kab/kota (Kabupaten dan Kota Bogor, Depok, Kabupaten Bekasi, Kabupaten dan Kota Tangerang, Tangerang Selatan).
  - **Kota Bekasi:** publikasi Podes tidak ditemukan. Penggantinya *Kecamatan Dalam Angka 2025* untuk 12 kecamatan (data 2024) dan Tabel 4.2.3 *Kota Bekasi Dalam Angka 2025* (rumah sakit dan puskesmas per kecamatan). Keterbandingan definisinya dengan Tabel 19–21 kab/kota lain **perlu dicek**.
- **Seri waktu:** kata pengantar menyebut seri ini terbit tiga kali dalam sepuluh tahun (siklus Podes). **Pembaruan 2 Oktober 2026:** edisi 2018 dan 2021 tingkat kab/kota tidak ditemukan lewat pencarian di kedelapan situs BPS; yang ada hanya edisi 2024 dan 2025. Karena itu, seri ini **tidak mendukung** analisis perubahan fungsi layanan, dan C4 tetap bertumpu pada data komuter 2014/2019/2023.
- **Konsekuensi:**
  - Jumlah fasilitas Podes per kecamatan menjadi sumber **fungsi layanan dasar sampai menengah** yang bersifat sensus dan terbuka.
  - Google Places dan OSM/Overture melengkapi fungsi yang tidak dicakup Podes (layanan bisnis, klinik spesialis, perkantoran) sekaligus menjadi pemeriksa silang.

**Risiko baru akibat sikap OSM-first:**
- Kelengkapan pemetaan OSM cenderung lebih tinggi di kawasan yang lebih urban dan lebih dekat ke Jakarta.
- Bias cakupan ini dapat menciptakan asosiasi semu positif antara integrasi dan fungsi, sehingga pola tampak seperti *borrowed size*.
- Wajib ada pemeriksaan kelengkapan OSM per kecamatan terhadap Overture dan agregat Podes/Kecamatan Dalam Angka sebelum residu dihitung.

### C3. Desain dua tingkat — Diputuskan (putaran 3)

| Tingkat | Unit dan N | Massa S | Fungsi F | Integrasi I | Beban/manfaat | Menjawab |
|---|---|---|---|---|---|---|
| Utama | Kecamatan non-DKI, sekitar 140 (**perlu dihitung**) | Penduduk (WSM 2024 / Kecamatan Dalam Angka); luas terbangun (GHSL) | Layanan: jumlah fasilitas Podes 2024 per kecamatan, Google Places untuk layanan bisnis/spesialis, SIRS/PDDikti untuk kelas. Pekerjaan: proksi C10 | % komuter ke inti (WSM 2024). Tarikan BPTJ dipindahkan menjadi pemeriksa proksi pekerjaan (C10) agar tidak berperan ganda | Beban potensial: waktu tempuh hasil perutean OSM (P) | Q2 dan Q3: kemiringan residu terhadap integrasi |
| Pendalaman | Kab/kota, 13×13 | Penduduk kab/kota | Pekerjaan (estimasi POI, S), deskriptif | Matriks komuter publikasi 2014/2019/2023; hitungan CCTV per koridor | Durasi/biaya rata-rata (publikasi); upah kab/kota jika tersedia | Q1: arah, asimetri, arus antarpinggiran, dan perubahan antarperiode |

Keputusan putaran 2: layanan **dan** pekerjaan sama-sama menjadi domain utama. Proksi pekerjaan tingkat kecamatan dibahas di C10. Pada tingkat pendalaman kab/kota, estimasi pekerjaan tetap deskriptif.

### C4. Dimensi waktu — Disepakati

- Satu-satunya seri yang benar-benar sebanding adalah publikasi **Survei Komuter Jabodetabek 2014, 2019, dan 2023**. Bab 4 hanya menyebut edisi 2023.
- Gunakan seri tersebut untuk "perubahan" pada Q2 (sisi relasi), atau hapus kata "perubahan" dari Q2.
- Kesetaraan desain sampel dan definisi antaredisi harus diperiksa.
- Fungsi berbasis OSM tidak memiliki riwayat yang andal, sehingga perubahan fungsi tidak diklaim.

### C5. Cakupan melebar — Disepakati; CCTV dipertahankan dengan peran terbatas

**Temuan.** CCTV disebut 13 kali, Web GIS 10 kali, SUMO 8 kali, dan YOLO 4 kali. Tidak satu pun menjawab ketiga pertanyaan penelitian secara langsung. Rumpun skenario EV-/P- dan *what-if* juga melebar.

**Tindak lanjut:**
**Keputusan putaran 2:**
- **CCTV:** dipertahankan dengan peran C1, yaitu *screenline* terarah di batas DKI. Disetujui pengguna.
- **SUMO:** dikeluarkan dari lingkup, kecuali dikombinasikan dengan CCTV.
  - Jika dipakai, SUMO dapat membentuk rute dari hitungan ruas untuk simulasi koridor pada skenario *what-if* (misalnya dengan alat `routeSampler` atau `flowrouter` bawaan SUMO; **perlu dicek** kecocokannya).
  - Statusnya penguatan opsional, bukan rantai inti.
- **Web GIS dan *what-if*:** tetap masuk lingkup sebagai media komunikasi dan eksplorasi kondisional, dengan label yang sudah ada di Bab 3. Batas tampilan konten Google dibahas di C9.
- **Penyebutan:** hapus pengulangan CCTV, SUMO, dan Web GIS di Bab 1 (`tex:139`) dan Bab 4 (`tex:1684`, `tex:1709`). Cukup dijelaskan sekali di Bab 3.

### C6. Kunci desain — Disepakati

- Tulis ulang Bab 3 menjadi satu **spesifikasi utama** dan **cadangan bernama** beserta pemicunya, bukan menu bersyarat.
- Tambahkan **tabel operasionalisasi variabel**. Versi putaran 5 di bawah menggantikan kerangka awal dan disusun dari keputusan C1–C10. Statusnya draf; unsur yang ditandai **perlu dicek** belum diaudit. Status D/A/S/P dibaca relatif terhadap unit pada tingkat masing-masing.

**Tingkat 1 — kecamatan non-DKI Jabodetabek** (analisis utama; Q2 dan Q3; N ≈ 140, **perlu dihitung**):

| Konstruk | Indikator (definisi operasional) | Sumber | Periode | Status | Peran |
|---|---|---|---|---|---|
| Massa lokal $S$ | Jumlah penduduk | Tabel kecamatan dalam *Kabupaten/Kota Dalam Angka* atau WSM 2024 | 2024 | D | Garis dasar ekspektasi; kriteria pemilihan pusat (B2) |
| | Luas terbangun total | GHSL GHS-BUILT-S | Epoch observasi terdekat | P | Garis dasar alternatif (sensitivitas) |
| Karakteristik lokal $X$ | Kepadatan penduduk; status kota/kabupaten; lereng rata-rata | Turunan $S$ dan luas wilayah BPS; DEM terbuka | — | D/P | Kovariat ekspektasi, jumlahnya dibatasi |
| Penjelasan alternatif $Z$ | Luas kawasan industri; keberadaan kota baru skala besar; tahun pembentukan daerah otonom | Kemenperin 2025; OSM *landuse* dan literatur; regulasi pembentukan | 2025; — | D/P | Kontrol dan pemeriksaan Q3 (B6) |
| Integrasi $I$ | Persentase pekerja komuter yang menuju inti | WSM 2024 (data posisi ponsel) | Agustus 2024 | A | Variabel penjelas utama Q3 |
| Fungsi layanan $F_L$ | Jumlah RS, perguruan tinggi, bank, akomodasi, pertokoan/pasar | *Statistik Potensi Desa/Kelurahan 2024* (Tabel 19–21) | Podes 2024 | D | Hasil, domain layanan |
| | RS kelas A/B dan tempat tidur; perguruan tinggi terakreditasi | SIRS; PDDikti | Tangkapan 2026 | D | Pembobot orde layanan |
| | Jumlah layanan bisnis dan klinik spesialis | Google Places, hanya jumlah per kecamatan (C9) | Tangkapan 2026 | D (direktori) / P | Hasil; orde tinggi yang tidak tercakup Podes |
| Fungsi pekerjaan $F_P$ | Volume terbangun nonhunian (satuan dicek dari metadata) | GHSL GHS-BUILT-V R2023A NRES | Epoch 2020, interpolasi dari observasi 2018 | P | Hasil, domain pekerjaan |
| | Pangsa volume nonhunian di dalam kawasan industri | GHSL × Kemenperin 2025 | — | P | Pembeda manufaktur/nonmanufaktur (P2, P3) |
| | Jumlah tempat kerja Google; tarikan perjalanan BPTJ | Google Places; laporan BPTJ/Kemenhub | 2026; kajian 2023 | D/S | **Pemeriksa** $F_P$, bukan hasil |
| Fungsi harapan dan residu | $\hat F_{ik}$ dari $S_i$ dan $X_i$ dengan prediksi *leave-one-out* di antara kecamatan non-DKI; residu $R_{ik}$ = selisih log teramati terhadap harapan | Perhitungan | — | S | Hasil Q2; variabel terikat Q3 |
| Manfaat $A$ | Akses kumulatif ke volume nonhunian dalam ambang waktu tempuh jaringan | OSM + perutean (OSRM/r5) + GHSL | Tangkapan 2026 | P | Profil manfaat |
| Beban $D$ | Waktu tempuh jaringan arus bebas ke inti DKI | OSM + perutean | Tangkapan 2026 | P | Profil beban; gerbang *shadow* |

**Tingkat 2 — kab/kota Jabodetabek, 13 unit** (pendalaman; Q1 dan Q2):

| Konstruk | Indikator (definisi operasional) | Sumber | Periode | Status | Peran |
|---|---|---|---|---|---|
| Relasi terarah $I$ | Arus komuter $F_{ij}$ dan turunannya: intensitas (komuter keluar per penduduk bekerja), orientasi ke DKI $O_i$, pangsa arus antarpinggiran, rasio masuk/keluar, asimetri pasangan $(F_{ij}-F_{ji})/(F_{ij}+F_{ji})$ | Publikasi *Statistik Komuter Jabodetabek* (**perlu dicek** tersedianya tabel asal-tujuan) | 2014, 2019, 2023 | D | Q1; perubahan antarperiode (C4) |
| Arah dan asimetri koridor | Volume kendaraan terarah per jam di titik batas DKI, pagi dan sore, per kelas kendaraan | Rekaman CCTV + deteksi YOLO dan pelacakan; sampel hitung manual | Sesuai rekaman | S | Q1 tingkat koridor; validasi |
| Beban $D$ | Durasi dan biaya perjalanan rata-rata komuter menurut kab/kota asal | *Statistik Komuter* 2023 | 2023 | D | Profil beban; pemeriksa beban potensial tingkat 1 |
| Manfaat $A$ | Upah rata-rata pekerja formal (jika tersedia); UMK sebagai konteks | Tabel BPS provinsi (**perlu dicek**); penetapan UMK | 2023/2024 | A | Profil manfaat |
| Pekerjaan menurut tempat kerja | Penduduk bekerja − komuter keluar + komuter masuk | Tabel terbuka Sakernas + *Statistik Komuter* | 2023 | S | Kalibrasi/validasi $F_P$; **tidak** dipasangkan dengan relasi komuter |
| Fungsi dan residu agregat | Agregasi $F$ dan $R$ tingkat 1 ke kab/kota | Perhitungan | — | S | Membaca profil kab/kota bersama relasi |

**Lintas tingkat — ketahanan $Q$** (status S; mendukung gerbang 4). Variasi yang diuji:
- garis dasar massa: penduduk atau luas terbangun;
- pembanding: prediksi *leave-one-out* atau tetangga ukuran terdekat;
- bentuk residu;
- masker fasilitas layanan (OSM) pada GHSL;
- ambang tipologi;
- analisis tanpa lapisan Google.

**Pemetaan pertanyaan penelitian ke analisis:**

| Pertanyaan | Analisis |
|---|---|
| Q1 | Peta alir dan indeks asimetri OD 13×13 kab/kota (2014/2019/2023); peta persentase komuter ke inti per kecamatan; volume koridor CCTV |
| Q2 | Model hitungan binomial negatif untuk layanan (nilai nol ditangani model, bukan dihapus) dan model log-linear untuk volume nonhunian, terhadap $S$ dan $X$, dengan prediksi *leave-one-out*, menghasilkan residu per domain; profil manfaat dan beban pada kedua tingkat |
| Q3 | Regresi residu terhadap $I$ dengan kontrol $Z$ pada tingkat 1 (jumlah parameter dibatasi); uji autokorelasi spasial residu (Moran's I), dengan model spasial hanya sebagai penguatan; tipologi sebagai ringkasan setelah gerbang bukti. Tingkat 2 dibaca sebagai profil, bukan regresi |

**Pemeriksaan independensi (B4 dan aturan sirkularitas):**
- $I$ (WSM) tidak dipakai dalam $F$.
- Tarikan BPTJ dan pekerjaan menurut tempat kerja hanya menjadi pemeriksa.
- Pekerjaan hasil turunan data komuter tidak dipasangkan dengan relasi komuter.
- Beban (waktu tempuh ke inti) berbeda konstruksi dari integrasi (pangsa arus) dan dari manfaat (akses kumulatif ke peluang).

**Perlu dicek sebelum tabel dikunci:**
- jumlah kecamatan;
- definisi "inti" dalam WSM;
- ketersediaan publikasi Podes untuk enam kab/kota;
- ~~versi dan epoch GHSL~~ — **terjawab (putaran 5):** R2023A; epoch 2020 adalah hasil interpolasi dengan observasi terdekat 2018, sehingga selisihnya sekitar 6 tahun dari Podes/WSM 2024. Luas NRES 2018 resolusi 10 m tersedia sebagai sensitivitas;
- tabel asal-tujuan dalam publikasi komuter;
- tabel upah per kab/kota.

- Kurangi pengulangan kalimat pengaman. Frasa "tidak otomatis" muncul 10 kali, dan pernyataan non-kausal diulang di setiap bab.

### C7. Bab 4 sebagai gambaran umum — Disepakati; unduh berkas sebelum revisi

**Yang belum ada:**
- penduduk DKI (Tabel 4.1 hanya memuat 8 unit non-DKI; `tex:1643-1663`), luas, dan kepadatan;
- struktur PDRB per sektor;
- angka komuter (sekitar 3,6 juta komuter pada Oktober 2023; tempat tinggal terbanyak di Kabupaten Bogor, sekitar 459 ribu);
- jaringan transportasi yang **sudah beroperasi** (Gambar 4.3 hanya rencana 2045);
- kawasan industri dan kota baru;
- konteks kebijakan: UU 2/2024 dan Kawasan Aglomerasi, Dewan Kawasan Aglomerasi, Perpres 60/2020.

**Ketidakcocokan tahun:** penduduk 2024 dipasangkan dengan data komuter 2023. Pertimbangkan memakai penduduk 2023.

**Daftar unduhan:** §12.

### C8. Judul vs Kabupaten Cianjur — Ditolak perluasan wilayah

**Temuan.** UU 2/2024 Pasal 51(2) memasukkan Kabupaten Cianjur ke Kawasan Aglomerasi. Judul memakai istilah "Kawasan Aglomerasi Jakarta", sedangkan wilayah studi hanya sembilan unit Jabodetabek. Kata "Cianjur" muncul 0 kali di naskah.

**Keputusan pengguna.** Cianjur tidak ditambahkan. Alasannya:
- Cianjur berada pada lapisan kedua.
- Pola yang berlaku di Jabodetabek diperkirakan berlaku juga di Cianjur dengan efek lebih kecil.
- Menambahkannya mempersulit penelitian tanpa manfaat berarti.

**Pertanyaan pengguna (putaran 2): apakah pilihan judul punya konsekuensi substantif?**
- **Terhadap analisis: tidak ada.** Unit, data, dan metode sama saja karena wilayah kerja tetap sembilan unit Jabodetabek.
- **Terhadap pembingkaian:**
  - "Kawasan Aglomerasi Jakarta" adalah istilah hukum (UU 2/2024) yang mencakup Cianjur. Memakainya di judul mengundang pertanyaan penguji mengapa Cianjur tidak diteliti, dan temuan secara implisit diklaim berlaku untuk seluruh kawasan hukum itu.
  - "Jabodetabek" cocok dengan wilayah data (Survei Komuter Jabodetabek, BPTJ, WSM), sehingga tidak ada celah antara judul dan cakupan.
- **Terhadap dampak:** relevansi kebijakan tidak hilang. Kaitan ke kebijakan dipertahankan di latar belakang dan manfaat praktis dengan menyatakan Jabodetabek sebagai inti Kawasan Aglomerasi menurut UU 2/2024. Dengan begitu, hasil penelitian tetap berbicara kepada Dewan Kawasan Aglomerasi.

**Keputusan:** judul memakai "Jabodetabek". Syarat pengguna, yaitu tidak ada konsekuensi substantif, terpenuhi menurut evaluasi ini. Kaitan dengan Kawasan Aglomerasi ditempatkan di Bab 1.

**Tindak lanjut:**
- Ganti frasa judul menjadi "… Pusat-Pusat Sekunder Jabodetabek". Rumusan akhir diserahkan kepada pengguna.
- Tambahkan satu kalimat di Batasan Penelitian: Kabupaten Cianjur, yang termasuk Kawasan Aglomerasi, tidak dicakup, beserta alasannya.
- Perkiraan "berlaku dengan efek lebih kecil" ditulis sebagai **alasan pembatasan lingkup**, bukan klaim empiris.

### C9. Google Maps Platform untuk fasilitas — Diputuskan pengguna; perlu desain kepatuhan

**Keputusan pengguna:** fasilitas dikumpulkan dengan Google Maps / Places API. Biaya bukan masalah karena pengambilan dilakukan sekali (statis).

**Catatan evaluasi.** Hambatan utamanya bukan biaya, melainkan syarat layanan. Menurut *Google Maps Platform Service Specific Terms* bagian Places API (diakses 27 September 2026):
- *place ID* boleh disimpan tanpa batas waktu;
- koordinat lintang-bujur hanya boleh di-*cache* paling lama 30 hari berturut-turut, lalu dihapus;
- atribut lain (nama, alamat, rating, jam buka, dan sebagainya) tidak boleh disimpan sebagai basis data;
- konten Places tidak boleh ditampilkan bersama peta non-Google.

Akibatnya, "ambil sekali lalu simpan sebagai dataset statis" justru bertentangan dengan syarat tersebut. Pengambilan di luar API (*scraping* laman Google Maps) juga dilarang.

**Desain kepatuhan yang diusulkan:**
1. Kumpulkan melalui Places API. Dalam jendela 30 hari, hitung agregat per kecamatan dan per jenis fasilitas.
2. Simpan hanya *place ID* dan tabel agregat per kecamatan. Hapus koordinat dan atribut setelah 30 hari; catat tanggal pengambilan dan penghapusan di log akses.
3. Web GIS hanya menampilkan agregat per kecamatan, bukan titik Google, kecuali memakai peta dasar Google.
4. Reproduksi: *place ID* memungkinkan pengambilan ulang, tetapi hasilnya dapat berubah. Catat ini sebagai batas reproduktibilitas.
5. Posisi agregat turunan (jumlah per kecamatan) terhadap syarat layanan adalah wilayah abu-abu. Nyatakan secara terbuka di subbab etika dan lisensi Bab 3.

**Catatan teknis dan biaya:**
- Satu permintaan pencarian di Places API (New) mengembalikan jumlah hasil terbatas, paling banyak sekitar 20 per permintaan (**perlu dicek** pada dokumentasi terbaru). Cakupan penuh karena itu memerlukan pembagian area bertingkat.
- Yang menentukan biaya adalah **jumlah panggilan**, bukan tarif per panggilan. Uji coba pada satu kab/kota untuk mengukurnya sebelum menjalankan seluruh Jabodetabek.

**Peran dalam desain:**
- Jumlah fasilitas Podes (C2) menjadi dasar layanan dasar sampai menengah.
- Google Places mengisi fungsi yang tidak dicakup Podes (layanan bisnis, klinik spesialis, perkantoran) dan memeriksa silang cakupan OSM/Overture.
- Tiga sumber dengan jalur pencatatan berbeda (sensus BPS, Google, OSM/Overture) sekaligus menjawab risiko bias cakupan OSM di C2.

**Tanggapan pengguna (putaran 3).** Nama tempat tidak disimpan; Google hanya dipakai untuk menghitung. Google tetap dipatuhi, tetapi seluruh kebutuhan penelitian harus terpenuhi.

**Penjelasan.** Menghitung memang diperbolehkan, dan itulah inti desain di atas. Yang dibatasi hanya penyimpanan data mentah dalam jangka panjang: koordinat lebih dari 30 hari dan atribut. Pemetaan kebutuhan penelitian terhadap batas tersebut:

| Kebutuhan penelitian | Terpenuhi? | Cara |
|---|---|---|
| Jumlah fasilitas per kecamatan per kategori | Ya | Titik ditumpangkan ke poligon kecamatan dalam proses yang sama, langsung setelah pengambilan (jauh di bawah 30 hari) |
| Deduplikasi antarpotongan area pencarian | Ya | Memakai *place ID*, yang boleh disimpan |
| Klasifikasi kategori | Ya | *types* Google dipakai sesaat untuk memetakan ke kategori milik penelitian; yang disimpan hanya label kategori sendiri |
| Keterulangan hitungan | Ya | Simpan tabel `place_id \| kode_kecamatan \| kategori_penelitian`, skrip, tanggal pengambilan, dan daftar jenis yang dicari. Koordinat, nama, dan alamat tidak disimpan |
| Pemeriksaan manual pada sampel | Ya | Dilakukan dalam 30 hari; setelahnya, buka ulang lewat *place ID* bila perlu |
| Peta agregat di Web GIS | Ya | Koroplet per kecamatan |
| Titik Google di Web GIS berbasis OSM | Tidak | Pakai titik OSM/Overture, atau peta dasar Google khusus untuk lapisan itu |
| Berbagi dataset titik mentah | Tidak | Bagikan tabel agregat dan daftar *place ID* |

**Batas:**
- Menyimpan pasangan *place ID* dengan kode kecamatan dan kategori buatan sendiri adalah wilayah abu-abu. Praktik ini lazim dalam riset dan sebaiknya dinyatakan terbuka di subbab etika dan lisensi.
- Evaluasi ini bukan nasihat hukum.

### C10. Proksi untuk dua domain utama — Usulan

Keputusan pengguna: layanan dan pekerjaan sama-sama menjadi domain utama, dengan proksi kreatif. Usulan awal di bawah ini belum diaudit.

**Pekerjaan (kecamatan):**

| Proksi | Sumber | Catatan |
|---|---|---|
| Volume bangunan nonhunian | GHSL (luas terbangun nonresidensial × tinggi bangunan) | Kapasitas tempat kerja, bukan jumlah pekerja; terbuka dan multitemporal |
| Jejak bangunan bertipe kerja | Overture Buildings / OSM (tag industri, komersial, kantor) | Kelengkapan tag tidak merata; uji terhadap GHSL |
| Kawasan industri × kepadatan pekerja per hektare | Kemenperin 2025 + koefisien dari laporan atau literatur | Estimasi (S); rentang koefisien diuji |
| Tempat kerja formal | Google Places (kantor, pabrik, gudang) | Terikat syarat C9 |
| Sumber penghasilan utama penduduk; industri mikro-kecil | Publikasi Podes (Bab I dan Bab 9) | Konteks struktur ekonomi, bukan jumlah pekerjaan |

**Layanan berorde tinggi (kecamatan):**

| Proksi | Sumber | Catatan |
|---|---|---|
| Jumlah RS, perguruan tinggi, bank, akomodasi, pertokoan/pasar | Publikasi Podes 2024 (Tabel 19–21) | Sensus dan terbuka; jumlah, bukan kapasitas |
| Kelas dan kapasitas RS (tempat tidur) | SIRS Kemenkes (publik) | Membedakan orde layanan |
| Akreditasi dan skala perguruan tinggi | PDDikti (publik) | Alamat badan hukum belum tentu lokasi kampus fisik |
| Layanan bisnis dan spesialis | Google Places (jenis tempat) | Terikat syarat C9 |
| Intensitas pemakaian (jumlah ulasan) | Google Places | Tidak boleh disimpan (C9); sebaiknya tidak dipakai sampai posisi kepatuhan jelas |

Aturan independensi tetap berlaku: proksi yang dipakai untuk membentuk relasi tidak dipakai lagi sebagai fungsi.

**Rekomendasi proksi pekerjaan (putaran 3; disetujui pengguna pada putaran 4):**

| Peran | Proksi | Alasan |
|---|---|---|
| **Utama** | Volume terbangun **nonhunian** per kecamatan, GHSL GHS-BUILT-V R2023A NRES, epoch 2020 (terverifikasi dan sudah diunduh) | Diukur dari citra satelit, sehingga cakupannya seragam dan bebas dari bias kelengkapan pemetaan. Terbuka (CC BY 4.0). Independen dari WSM/komuter dan dari hitungan layanan Podes/Google. **Koreksi putaran 5:** epoch 5-tahunan GHSL adalah hasil interpolasi dari observasi 1975, 1990, 2000, 2014, dan 2018, sedangkan komponen NRES berasal dari Sentinel-2 2018. Karena itu, **proksi ini tidak mendukung analisis perubahan (C4) pada sisi pekerjaan** |
| Komponen pembeda | Pangsa volume nonhunian di dalam kawasan industri (Kemenperin 2025) | Memisahkan pekerjaan manufaktur dari nonmanufaktur; dibutuhkan untuk P2 dan P3 |
| Pemeriksa 1 | Jumlah tempat kerja Google Places (kantor, pabrik, gudang) | Jalur pencatatan berbeda; terikat syarat C9 |
| Pemeriksa 2 | Tarikan perjalanan BPTJ per kecamatan (182 kecamatan) | Pemeriksa eksternal. Karena itu tidak lagi dipakai sebagai indikator integrasi (C3) |
| Pemeriksa 3 (kab/kota) | Pekerjaan menurut tempat kerja ≈ penduduk bekerja − komuter keluar + komuter masuk, dari tabel terbuka Sakernas dan Statistik Komuter; 13 unit | Kalibrasi atau validasi agregat proksi. Tidak dipasangkan dengan relasi komuter pada Q3 di tingkat kab/kota, supaya tidak sirkular |

**Tidak disarankan sebagai proksi utama:**
- Hitungan Google, karena condong ke usaha yang melayani konsumen, sementara pabrik dan gudang kurang terwakili, dan terikat C9.
- Tag bangunan OSM, karena bias kelengkapan pemetaan.
- VIIRS, karena bercampur dengan cahaya permukiman.

**Batas proksi utama:**
- **Tumpang tindih dengan domain layanan.** Kelas nonhunian juga mencakup rumah sakit, kampus, dan mal. Uji sensitivitas: keluarkan poligon fasilitas layanan dari OSM (misalnya `amenity=hospital`, `amenity=university`, `shop=mall`), lalu laporkan korelasi antardomain untuk P3.
- **Salah klasifikasi** mungkin terjadi di kawasan padat informal.
- **Kapasitas bukan jumlah pekerja.** Laporkan sebagai indeks. Konversi ke jumlah pekerjaan hanya melalui kalibrasi Pemeriksa 3 dan diberi label estimasi (S).
- **Pembeda B3 pada domain pekerjaan** tidak lagi memakai rasio nonhunian sebagai kontrol, karena rasio itu kini menjadi proksi. Pembeda yang tersisa adalah perbandingan dengan domain layanan dan perbandingan pada gradien integrasi.

## 7. Bagian D — Inkonsistensi internal (Disepakati)

- [ ] **Jumlah domain:**
  - Gambar 1.1 menyebut "pekerjaan, layanan, bisnis".
  - Teks membatasi paling banyak dua domain.
  - Proposisi 3 menyebut lima, termasuk "kinerja", yang dikeluarkan dari definisi kematangan.
- [ ] **Tipologi tidak seragam:** Tabel 2.2 punya 6 kelas; tabel Bab 3 punya 7; Gambar 1.1 menampilkan 3 hasil; Gambar 2.1 menampilkan 4 dengan nama berbeda.
- [ ] Definisi "relatif independen" berbeda antara Bab 2 (`tex:372`) dan Bab 3 (`tex:1293-1295`).
- [ ] Gambar 2.1 menurunkan manfaat dan beban dari asosiasi, padahal teks mengukurnya terpisah.
- [ ] Gambar 1.1 memasukkan beban ke uji hubungan, padahal teks memakainya hanya di gerbang label *shadow*.
- [ ] Sadewo dkk. 2021 dan 2023 disitasi tetapi tidak masuk Tabel 2.1 (`tex:284-316`). Sadewo 2023 (regresi panel spasial komuter antarpinggiran 2008–2015) adalah preseden terdekat.
- [ ] Enam tabel Bab 3 tanpa nomor dan judul (`\LTcaptype{none}`, sisa konversi Pandoc).
- [ ] Istilah tak terdefinisi: "WSM" dan "Sabuk Wilayah Statistik Metropolitan" (`tex:639`). "S-1" (`tex:1374`) terbawa dari catatan kerja.
- [ ] Subbab "Metode penelitian" di Bab 1 (`tex:143-153`) mengulang Bab 3. Ringkas.
- [ ] Setelah B2: ganti daftar kandidat Bab 4 (`tex:1698-1705`) dan hapus penggabungan Tangerang–Tangsel.

## 8. Bagian E — Bibliografi (Disepakati)

Hasil pencocokan dengan teks sumber lokal (pemetaan Explore, 27 September):

- [ ] **`otsuka2025`:** judul dan jurnal salah. Yang benar: *A three-layer model of borrowed size: empirical insights from Japan*, *Regional Studies, Regional Science* 12(1): 975–995.
- [ ] **`sadewoetal2021`:** penulis yang benar Erie Sadewo dan Anzhelika Antipova. Terbit di *Asian Geographer* (online 12 Maret 2020); judul lengkap memuat "the case of Medan, Jakarta, and Denpasar".
- [ ] **`sadewoetal2023`:** penulis yang benar Erie Sadewo, Anzhelika Antipova, dan Long Cheng. *Urban Geography* 44(8): 1628–1653; online 2022.
- [ ] **`burgermeijers2016`:** seharusnya 95(1): 5–16.
- [ ] **`durantonpuga2004`:** bab *Handbook of Regional and Urban Economics*, bukan artikel.
- [ ] **`andani2021`:** metadata @misc tidak lengkap (bab 13, tol Cipularang).
- [ ] **`volgmannrusche2020`:** tahun perlu dicek (versi *early view* bertanggal Februari 2019).
- [ ] **`bpsdki2025`, `bpsjabar2025`, `bpsbanten2024`:** tidak ada salinan lokal. Unduh (§12).

**Tambahan literatur:**
- [ ] Alonso (1973), *Urban Zero Population Growth*, *Daedalus* (terverifikasi; nomor volume perlu dicek).
- [ ] Otsuka, *Borrowed Size and Regional Resilience: Lessons from Japan* (Springer, New Frontiers in Regional Science: Asian Perspectives vol. 86). Memuat bab *borrowed size vs agglomeration shadow* dengan ekonometrika spasial.
- [ ] Kandidat yang **belum diverifikasi** (dari ingatan AI): Meijers, Hoogerbrugge & Cardoso (2018); Cardoso & Meijers (2016); van Meeteren, Neal & Derudder (2016).

## 9. Bagian F — Touch-up figure (Disepakati)

| Gambar | Masalah | Touch-up |
|---|---|---|
| 1.1 Logika penelitian | Belah ketupat berukuran berlebihan; domain "bisnis"; panah beban masuk uji hubungan; hanya 3 hasil | Ganti dengan kotak pertanyaan biasa; maksimal 2 domain; beban langsung ke gerbang label; hasil mengikuti tipologi; ekspor vektor (PDF/SVG); simpan perintah render `mmdc` |
| 2.1 Kerangka konseptual | Label "F-hat" terpotong; manfaat/beban jadi turunan asosiasi; kotak "Biaya dan tekanan lokal" menggantung; panah akses → relasi terbaca kausal; judul "Landasan lokal" menabrak garis | Notasi $S, X, F, \hat F, R, I, Z$ sesuai persamaan; manfaat dan beban sebagai pengukuran sejajar; nama hasil sama dengan Tabel 2.2 |
| 3.1 Alur analisis | Tata letak zig-zag membuat baris kedua terbaca 8→5; panah kecil; campur bahasa (*provenance*, *baseline*); umpan balik penurunan klaim tidak tergambar | Diagram alir vertikal dengan belah ketupat gerbang dan cabang cadangan (kecamatan vs kab/kota) |
| 4.1 & 4.2 Admin/status | Hampir identik; label menabrak batas (Kota Bekasi, Tangerang Selatan); penamaan tidak konsisten ("Depok" vs "Kota Depok"); koordinat WGS84 geografis tetapi pakai skala batang km | Gabung jadi satu peta; proyeksikan ke UTM 48S (EPSG:32748); isi laut; kabupaten tetangga sebagai konteks; inset Jawa; catatan Kepulauan Seribu; koma desimal ("6,2° LS"); rapikan legenda; catat skrip SVG→PNG |
| 4.3 Jaringan JUTPI | Tangkapan layar raster; tanpa nomor halaman sumber; legenda Inggris; atribusi peta dasar terpotong; hanya rencana 2045 | Gambar ulang: jaringan eksisting garis penuh (KRL, MRT, LRT Jabodebek, TransJakarta, tol; dari OSM/GTFS), rencana garis putus; gaya sama dengan peta lain; cantumkan halaman sumber |
| 4.4 Kandidat | Tangerang–Tangsel digabung; Cikarang tidak dapat dipisah pada data komuter; garis relasi hanya radial, tanpa pasangan antarpinggiran; koordinat piksel ditulis manual di `render_bab4_candidates.py` | Titik diturunkan dari koordinat; setelah B2, ganti dengan peta kecamatan berdasarkan massa |
| Baru | Belum ada | Peta kepadatan kecamatan; peta % komuter ke inti (WSM 2024); peta arus kab/kota 2023; peta jaringan eksisting; peta kawasan industri (Kemenperin 2025) dan kota baru; diagram keputusan cadangan di Bab 3 |
| Umum | Gaya tidak seragam | Satu font dan palet; ekspor vektor; format caption "Judul. Sumber: … (hlm.)" |

## 10. Draf proposisi berarah dan penjelasan alternatif (untuk B6)

Draf usulan; perlu disetujui pengguna.

| Kode | Proposisi | Hasil yang membantah |
|---|---|---|
| P1 — layanan, kecamatan | Setelah massa dan karakteristik lokal diperhitungkan, orientasi komuter ke inti yang lebih tinggi berasosiasi dengan residu layanan berorde tinggi yang lebih rendah. Pola ini diharapkan paling jelas pada kecamatan dominan hunian (tanggapan pengguna pada B3). | Kemiringan nol atau positif yang stabil |
| P2 — pekerjaan, kab/kota/koridor | Unit dengan tarikan masuk dan arus antarpinggiran yang besar (koridor industri Bekasi–Cikarang, Tangerang) memiliki residu pekerjaan positif, sehingga konsisten dengan *borrowed size* pada domain produksi. | Residu pekerjaan negatif pada unit dengan tarikan masuk tertinggi |
| P3 — lintas domain | Unit yang sama dapat surplus pekerjaan tetapi defisit layanan (spesialisasi fungsional; Duranton & Puga 2005), sehingga masuk kelas campuran. | Tanda residu kedua domain selalu searah |
| P4 — gradien (opsional) | Hubungan integrasi–residu tidak linear sepanjang gradien aksesibilitas ke inti (hipotesis *non-linear metropolitan effect* di catatan induk). | Tidak ada perubahan kemiringan pada spesifikasi yang wajar |

**Penjelasan alternatif yang dinamai beserta cara memeriksanya:**

| Penjelasan alternatif | Cara memeriksa |
|---|---|
| Kawasan industri formal | Luas atau keberadaan kawasan industri (Kemenperin 2025) sebagai kontrol |
| Kota baru swasta skala besar (BSD, Lippo Karawaci, Jababeka, Summarecon Bekasi, Sentul) | Penanda keberadaan dari sumber terbuka dan literatur |
| Status administratif dan usia daerah otonom (misalnya pemekaran Tangerang Selatan 2008) | Kontrol kota/kabupaten dan tahun pembentukan |
| Ketersediaan lahan | Pangsa lahan terbangun (GHSL). Harga tanah tidak tersedia dalam bentuk unduhan massal |
| Aksesibilitas jaringan (tol dan rel) | Dipisahkan sebagai A, bukan I |
| Bias cakupan pemetaan OSM | Pemeriksaan kelengkapan terhadap Overture dan agregat Podes (C2) |
| Topografi (Kabupaten Bogor bagian selatan) | Kemiringan lereng rata-rata dari DEM terbuka |

## 11. Urutan revisi yang disarankan

1. Putuskan unit (C1/C3). Domain utama sudah diputuskan: layanan dan pekerjaan.
2. Terapkan B1: kemiringan residu terhadap integrasi di dalam Jabodetabek.
3. Terapkan B2: aturan pemilihan unit berdasarkan massa.
4. Susun tabel operasionalisasi (C6) dengan proksi C10, lalu tulis ulang Bab 3 menjadi spesifikasi terkunci. Terapkan juga B4, B6, dan desain kepatuhan Google (C9) di subbab etika dan lisensi.
5. Keluarkan SUMO (kecuali dikombinasikan dengan CCTV). Kurangi penyebutan Web GIS dan *what-if*. Tetapkan peran CCTV sebagai *screenline* (C5).
6. **Unduh berkas (§12)**, lalu isi Bab 4 dengan fakta deskriptif (C7) dan tambahkan kalimat batasan Cianjur (C8).
7. Rapikan konsistensi (D), bibliografi (E), dan figure (F).

## 12. Daftar unduhan sebelum revisi

Setiap berkas disimpan di `source/` dengan catatan pendamping sesuai `source/AGENTS.md`: tanggal akses, URL, checksum untuk dataset, dan lisensi.

**Status unduhan (putaran 5, 27 September 2026):**
- Situs BPS (bps.go.id dan subdomain kab/kota) menolak unduhan otomatis dengan HTTP 403, sehingga **semua berkas BPS diunduh manual oleh pengguna**.
- Berkas non-BPS yang sudah diunduh agen ditandai [x] di bawah; catatan sumbernya sudah ada.
- PDF JUTPI 3 tersimpan di git sebagai `source/official-document/JICA JUTPI 3 - 2025 - Project Completion Report.pdf` tetapi tidak ter-*checkout*.

**Untuk Bab 4 (gambaran umum):**
- [ ] BPS Provinsi DKI Jakarta, *Provinsi DKI Jakarta Dalam Angka 2025*: penduduk per kota administrasi, luas, kepadatan.
- [ ] *Jawa Barat Dalam Angka 2025* dan *Banten Dalam Angka 2025*, atau Dalam Angka tiap kab/kota: penduduk, luas, kepadatan. Utamakan tahun 2023 agar sejajar dengan data komuter.
- [ ] *Kota Depok Dalam Angka 2025* dan *Kota Tangerang Dalam Angka 2024*: sumber Tabel 4.1 saat ini, yang belum punya salinan lokal.
- [ ] BPS, *PDRB Kabupaten/Kota di Indonesia 2020–2024*: struktur sektor.
- [ ] BPS, *Statistik Komuter Jabodetabek* 2023, 2019, dan 2014 (PDF dan lampiran tabel bila ada). Periksa apakah matriks asal-tujuan 13×13 tersedia. Periksa juga publikasi komuter per kab/kota (misalnya *Statistik Komuter Kota Depok 2023*).
- [ ] BPS, *Wilayah Statistik Metropolitan Indonesia 2024*: tabel persentase komuter per kecamatan dan metodologi (anomali ambang).
- [x] Kementerian Perindustrian, *Peta Kawasan Industri Eksisting 2025*: shapefile 125 KI dan xlsx metadata, di `source/dataset/`.
- [x] Teks UU No. 2 Tahun 2024 (Pasal 51 di halaman PDF 35–36) dan batang tubuh Perpres No. 60 Tahun 2020, di `source/official-document/`. Lampiran Perpres belum diunduh.
- [ ] Laporan JUTPI 3 *Project Completion Report* (sudah ada di git, tetapi tidak ter-*checkout*: `git show HEAD:<path>`). Catat halaman peta jaringan 2045.

**Untuk rancangan Bab 3 (cukup contoh untuk audit, bukan eksekusi penuh):**
- [ ] Ekstrak OSM Jawa (Geofabrik) bertanggal dan rilis Overture Places bertanggal: satu kab/kota sebagai uji kelengkapan.
- [x] GTFS statis TransJakarta (berkas berstempel 2026-07-24), di `source/dataset/`.
- [ ] Satu atau dua contoh *Kecamatan Dalam Angka* per kab/kota, untuk memastikan tabel fasilitas bersumber Podes tersedia.
- [ ] *Statistik Potensi Desa/Kelurahan 2024* untuk kedelapan kab/kota Bodetabek: sumber jumlah fasilitas per kecamatan (C2).
  - Terverifikasi ada: Kabupaten Bogor dan Kota Bogor. Sisanya perlu dicek.
  - Jakarta Utara sudah diunduh. Lengkapi kota administrasi DKI lain bila konteks DKI diperlukan.
- [ ] Edisi 2021 (dan 2018) publikasi yang sama, untuk memeriksa keterbandingan seri (C4).
- [ ] Arsip PDF *Google Maps Platform Service Specific Terms* versi saat pengambilan, untuk lampiran etika dan lisensi (C9).
- [ ] Tabel upah rata-rata pekerja formal menurut kab/kota (BPS Jawa Barat, Banten, DKI), bila ada, serta UMK 2023/2024.
- [x] Laporan BPTJ/Kemenhub. Tabel 7.1 (halaman PDF 176–181) berisi bangkitan dan tarikan 182 kecamatan, bukan matriks pasangan, dan dapat diekstrak sebagai teks. Di `source/official-document/`.
- [x] GHSL GHS-BUILT-V R2023A epoch 2020, total dan NRES, tile R10_C29, di `source/dataset/`. Luas NRES 2018 resolusi 10 m (sensitivitas) belum diunduh.

## 13. Keputusan yang masih terbuka

1. **Unit — diputuskan (putaran 3):** desain dua tingkat, yaitu kecamatan dan kab/kota.
2. **Domain utama — diputuskan:** layanan dan pekerjaan (C10).
3. **Implementasi B1 — diputuskan (interpretasi):** kemiringan di dalam Jabodetabek saja, tanpa pembanding eksternal. Koreksi bila "jabodetabek aja" dimaksudkan untuk hal lain.
4. **SUMO, Web GIS, dan *what-if* — diputuskan:** SUMO keluar kecuali dikombinasikan dengan CCTV; Web GIS dan *what-if* tetap; penyebutannya dikurangi.
5. **Peran CCTV — diputuskan:** *screenline* terarah di batas DKI.
6. **Judul — diputuskan:** "Jabodetabek" (C8).
7. **Kepatuhan Google — arah disepakati (putaran 3).** Data hanya dipakai untuk menghitung; yang disimpan *place ID*, kode kecamatan, dan kategori milik penelitian. Tabel kebutuhan di C9 menunjukkan dua hal yang tidak dapat dipenuhi, yaitu titik Google di atas peta OSM dan berbagi titik mentah, beserta penggantinya.
8. **Proksi pekerjaan — diputuskan (putaran 4).** Isi keputusan mengikuti rekomendasi C10: volume nonhunian GHSL sebagai proksi utama, pangsa di kawasan industri sebagai komponen pembeda, serta Google, BPTJ, dan pekerjaan menurut tempat kerja di tingkat kab/kota sebagai pemeriksa.

## 14. Provenance dan batas evaluasi

**Dasar evaluasi:**
- Pembacaan penuh `latex/tga_pwk_jakarta_bab_1_4_final.tex` dan ketujuh figure.
- Pemetaan repo oleh subagen Explore.
- Catatan kerja induk (audit data 24 Agustus) dan berkas isu per bab di `output/naskah/bab_*/`.
- Halaman produk SILASTIK yang tersimpan di `source/dataset/`.

**Yang belum diperiksa:**
- 70 berkas `output/kajian/review-*.md` belum dibaca, sehingga klaim celah belum diuji terhadap korpus pengguna.
- Isi tabel publikasi Statistik Komuter 2023 belum diperiksa langsung (halaman BPS mengembalikan 403 saat diakses).
- Isi data WSM 2024 belum diperiksa.
- Jumlah kecamatan non-DKI (sekitar 140) belum dihitung.
- Ketersediaan tabel upah kab/kota untuk Jawa Barat, Banten, dan DKI belum dipastikan.

**Sumber web yang dipakai (diakses 27 September 2026):**
- [BPS — Statistik Komuter Jabodetabek 2023](https://www.bps.go.id/en/publication/2024/03/28/33b6bef825944e576e7ea3ba/commuter-statistics-of-jabodetabek-results-of-jabodetabek-commuter-surveys-2023.html)
- [Databoks — wilayah dengan pekerja komuter terbanyak 2023](https://databoks.katadata.co.id/ketenagakerjaan/statistik/1649dd34f81ed99/ini-wilayah-jabodetabek-dengan-pekerja-komuter-terbanyak)
- [Tribunnews — UU DKJ: Cianjur masuk Kawasan Aglomerasi](https://www.tribunnews.com/metropolitan/2024/03/29/uu-rkj-kabupaten-bogor-tangerang-hingga-cianjur-masuk-kawasan-aglomerasi-daerah-khusus-jakarta)
- [CNN Indonesia — Jabodetabekjur](https://www.cnnindonesia.com/nasional/20240319165011-32-1076254/jabodetabekjur-cianjur-masuk-kawasan-aglomerasi-jakarta-di-ruu-dkj)
- [Springer — Borrowed Size and Regional Resilience: Lessons from Japan](https://link.springer.com/book/10.1007/978-981-95-7016-4)
- [JSTOR — Alonso, Urban Zero Population Growth](https://www.jstor.org/stable/20024174)
- [SAGE — Meijers & Burger 2017, Stretching the concept of borrowed size](https://journals.sagepub.com/doi/abs/10.1177/0042098015597642)
- [Taylor & Francis — Sadewo dkk. 2023](https://www.tandfonline.com/doi/abs/10.1080/02723638.2022.2125649)
- [BPS Jawa Tengah — contoh tabel upah pekerja formal menurut kab/kota](https://jateng.bps.go.id/id/statistics-table/2/MjMxOSMy/rata-rata-upah-gaji-bersih-sebulan-pekerja-formal-menurut-kabupaten-kota-dan-lapangan-pekerjaan-utama-di-provinsi-jawa-tengah.html)
- [Open Data Jawa Barat — UMK](https://opendata.jabarprov.go.id/id/dataset/daftar-upah-minimum-kabupatenkota-di-daerah-provinsi-jawa-barat)
- [Google Maps Platform Service Specific Terms](https://cloud.google.com/maps-platform/terms/maps-service-terms) (putaran 2; ringkasan syarat caching Places diperoleh lewat hasil pencarian, bukan pembacaan penuh dokumen)
- [BPS Kabupaten Bogor — Statistik Potensi Desa Kabupaten Bogor 2024](https://bogorkab.bps.go.id/id/publication/2024/12/24/1066acf5488fadafaa98eb72/statistik-potensi-desa-kabupaten-bogor.html)
- [BPS Kota Bogor — Statistik Potensi Desa Kota Bogor 2024](https://bogorkota.bps.go.id/en/publication/2024/12/31/88486e40df9103aefbc1763b/publikasi-statistik-potensi-desa-kota--bogor-2024.html)

**PDF Jakarta Utara (putaran 2):** yang dibaca hanya halaman PDF 1–12 (sampul, kata pengantar, daftar isi, daftar tabel), 84–85 (Tabel 4.4), dan 234–237 (catatan teknis serta Tabel 20.1–20.2), ditambah ekstraksi lapisan teks yang hanya memuat narasi. Tabel lain belum diperiksa satu per satu. Catatan sumbernya ada di `source/official-document/`.


## 15. Putaran 6 — verifikasi data dan revisi naskah (2 Oktober 2026)

Sesi cloud. Pengguna mengonfirmasi bahwa **inti penelitian tetap DKI Jakarta dan WSM hanya salah satu sumber**, lalu meminta seluruh rencana dikerjakan dengan keputusan terbaik bila belum diputuskan. Semua angka di bawah dibaca dari PDF di `source/official-document/` dan dicatat locatornya di catatan sumber masing-masing.

### 15.1 Hasil verifikasi butir "perlu dicek"

| Butir | Hasil | Akibat bagi desain |
|---|---|---|
| Jumlah kecamatan non-DKI (C3, C6) | **141** (WSM 2024, Lampiran 13, kode BPS 2024) | N tingkat 1 = 141; 129 bila cadangan K1 berlaku |
| Definisi "inti" WSM (C2) | Kawasan inti perkotaan **morfologis** (grid ≥1.500 jiwa/km², SP2020). KIP 1 mencakup seluruh DKI, Kota Bekasi, Depok, Kota Tangerang, dan Tangsel, serta kecamatan padat di tiga kabupaten (hlm. 28–29, 60) | % WSM berstatus A, bukan "% ke DKI". Uji sensitivitas memakai $I^{DKI}$ = WSM × pangsa kab/kota ke DKI 2023 |
| Anomali ambang 15% vs 7% (C2) | Bukan anomali: 7% dipilih BPS dengan merujuk Bosker dkk. (2021), sedangkan 15% adalah praktik OECD/UE (hlm. 12, 33–34) | Nilai kontinu dipakai; kelas delineasi tidak dijadikan kebenaran dasar |
| Nilai WSM untuk kecamatan inti | Tersedia untuk semua 141 kecamatan (1,9–47,8%); 105 inti, 27 periferi, 9 bukan WSM | Integrasi kecamatan dapat dihitung untuk seluruh unit |
| Matriks asal–tujuan komuter (C1) | **Ada** di ketiga edisi (Tabel 2). 2023: matriks pergerakan harian 13×13 + luar Jabodetabek; 2014/2019: arus komuter antarkab/kota. Semua jumlah baris dan kolom cocok dengan total | Q1 dan perubahan antarperiode terjawab dengan data teramati; OD sintetis tidak diperlukan |
| Durasi dan biaya rata-rata (C1, C6) | Hanya **distribusi kelas** (Tabel 20 dan 35), bukan rata-rata | Beban T2 = pangsa ≥90 menit dan ≥Rp25.000 |
| Upah per kab/kota (C1) | Tabel 51 Komuter 2023: distribusi penghasilan komuter bekerja per kab/kota asal. Tabel upah provinsi hanya sebagian (formal Banten tidak ada) | Manfaat T2 = pangsa komuter berpenghasilan ≥Rp5 juta; tabel upah menjadi konteks |
| Total komuter 2023 (C7) | 4.414.974 komuter (14,9%), dengan 3.614.673 bekerja; Kabupaten Bogor 584.041 (459.775 bekerja). Angka "3,6 juta" di evaluasi awal adalah komuter **bekerja** | Bab 4 memakai kedua angka |
| Keterbandingan Podes (C2) | Tabel jumlah fasilitas per kecamatan setara di tujuh kab/kota (edisi 2024). Kota Bekasi tidak punya Podes, dan Tabel 4.2.1 *Dalam Angka*-nya hanya memuat **banyaknya kelurahan yang memiliki** fasilitas | Cadangan K1 |
| Edisi 2025 *Statistik Potensi Desa* | Bersumber dari Pemutakhiran Data Perkembangan Desa 2025; definisi sebagian tabel berubah | Hanya pemeriksa stabilitas, bukan seri |
| Seri komuter (C4) | Definisi 2023 dirumuskan ulang; bulan (Mei 2014, April 2019, Oktober 2023) dan kerangka sampel berbeda | Perubahan dibaca sebagai arah estimasi survei |
| Penduduk kecamatan | WSM Lampiran 3 (sumber: *Daerah Dalam Angka 2024*): lima unit Jawa Barat persis sama dengan proyeksi 2024; tiga unit Banten berselisih 2–3% | ❓ Cek basis Banten sebelum ambang massa dibekukan |
| PDRB sektor (C7) | Publikasi PDRB kab/kota hanya memuat total. Pangsa sektor diambil dari Tabel 12.3 *Dalam Angka* kab/kota. Tabel 13.1.3 DKI edisi 2025 rusak (baris bergeser), sehingga dipakai edisi 2026 | Tabel 4.2 |
| Nama wilayah inti | BPS sampai 2026 masih memakai "Provinsi DKI Jakarta"; UU 2/2024 Pasal 73 mengaitkan saat berlakunya dengan Keppres pemindahan ibu kota | "DKI Jakarta" dengan catatan kaki |

Pola deskriptif yang muncul (hanya konteks Bab 4, bukan hasil): pangsa komuter Bodetabek yang menuju DKI turun dari 61,1% (2014) ke 58,0% (2019) dan 53,0% (2023), sedangkan pangsa antarpinggiran naik dari 36,1% ke 39,4% dan 44,6%. Pembacaannya dibatasi oleh perbedaan definisi antaredisi.

### 15.2 Keputusan agen atas mandat pengguna

Keputusan berikut diambil agen karena pengguna meminta "ambil keputusan terbaik". Semuanya boleh dikoreksi.

| Butir terbuka | Keputusan | Alasan |
|---|---|---|
| OD sintetis | Dihapus dari rantai | Matriks teramati tersedia untuk tiga edisi; OD sintetis hanya menambah risiko sirkular |
| Nama wilayah inti | "DKI Jakarta" dengan catatan kaki UU 2/2024 | Konsisten dengan seluruh data; status hukum nama baru bergantung pada Keppres |
| Satu sumber kebenaran | File `.tex` per bab dihapus | File gabungan sudah menjadi target revisi; file per bab sudah tidak sinkron |
| Letak "perubahan" | Dipindah dari Q2 ke Q1 | Perubahan hanya tersedia pada relasi; C4 mengizinkan kedua opsi |
| Aturan massa | Kuartil teratas penduduk **atau** volume terbangun hunian (GHSL total − NRES); P66/P80 sebagai sensitivitas. Semua 141 kecamatan tetap dianalisis | Volume hunian tidak tumpang tindih dengan proksi pekerjaan (NRES). Analisis seluruh unit menghindari seleksi |
| Komposisi layanan utama | RS + perguruan tinggi + bank umum (Podes 2024); pertokoan, pasar, dan akomodasi menjadi sensitivitas | Mewakili layanan antarkecamatan; akomodasi condong ke kawasan wisata (Puncak) |
| Residu | $R = \ln(F + c) - \ln(\hat F_{(-i)} + c)$, dengan $c = 0{,}5$ untuk hitungan | Tetap terdefinisi saat $F = 0$ |
| Titik acuan beban T1 | Bundaran HI; kecamatan DKI terdekat sebagai sensitivitas | Pusat CBD yang lazim; perlu konfirmasi |
| Ambang akses | 60 menit (45 dan 90 sebagai sensitivitas) | Kisaran komuter dominan (Tabel 20: 30–59 menit terbanyak) |
| Gerbang *shadow* | "Beban tinggi" dinilai di antara unit dengan integrasi serupa | Waktu tempuh ke inti berkorelasi negatif dengan integrasi |
| Tipologi | Tujuh kategori; residu bertanda hanya bila selang tidak memuat nol | Memasukkan ketidakpastian dan menyeragamkan tabel |
| Tabel siap-*join* | Tidak dibuat di `calculation/`; tabel 141 kecamatan berkode BPS ditaruh di catatan sumber WSM | Catatan sumber boleh dikelola agen; tidak menambah objek *calculation* tanpa izin |
| Duplikat PDF | 36 salinan `dataset/` dihapus setelah checksum identik | Publikasi statistik termasuk `official-document`; riwayat git menyimpan salinan lama |
| J21/J26 | Dibiarkan | Kode korpus dirujuk berkas review |

### 15.3 Yang berubah di naskah

Rincian per bab ada di TODO §1–§7. Inti perubahannya:
- **Bab 3** ditulis ulang menjadi spesifikasi utama dua tingkat dengan cadangan K1–K8.
- **Bab 4** diisi angka terverifikasi (Tabel 4.1–4.4).
- **Bab 1–2** diselaraskan:
  - judul "Jabodetabek";
  - konteks Kawasan Aglomerasi;
  - proposisi P1–P4;
  - tipologi tujuh kategori;
  - penjelasan alternatif bernama.
- Bibliografi diperbaiki, dan diagram dirender ulang.

### 15.4 Batas putaran ini

- Angka Bab 4 adalah kutipan atau aritmetika sederhana dari tabel publikasi, belum analisis Bab 5.
- Ambang penduduk P75 (36 kecamatan) bersifat sementara.
- Kompilasi cloud memakai font pengganti; kompilasi final dilakukan di lokal.
- Isi publikasi selain tabel yang disebut belum dibaca penuh.
