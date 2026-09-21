# Arsip Kecukupan dan Sumber Approach Proksi Skripsi PWK Jakarta

> **Tanggal keputusan:** 19 September 2026  
> **Status:** arsip keputusan rancangan; bukan hasil audit empiris ketersediaan data.  
> **Rujukan aktif:** [[output/naskah/bab_1/bab_1_pendahuluan_draf|Bab 1]], [[output/naskah/bab_3/bab_3_metode_penelitian_draf_rancangan_kerja|Bab 3]], dan [[output/panduan/roadmap_skripsi_tga_borrowed_size_dan_agglomeration_shadow_jakarta|roadmap]].

## Putusan kecukupan

Rancangan ini **sudah cukup untuk skripsi tingkat sarjana PWK di Indonesia** apabila tujuan penelitian dibatasi pada diagnosis spasial-relasional, fungsi relatif per domain, perubahan pada seri yang sebanding, dan pola yang konsisten dengan *borrowed size* atau *agglomeration shadow*. Rancangan tidak perlu menunggu sensus usaha lengkap, matriks OD mikro, data pajak, atau data administratif tertutup untuk menjadi layak.

Kecukupan tersebut bergantung pada disiplin berikut:

1. Tidak semua teknik yang tersedia harus dipakai. Skripsi memilih satu jalur minimum yang dapat selesai dan menyimpan teknik lain sebagai penguatan.
2. Setiap konstruk inti memiliki satu proksi utama, satu pemeriksaan independen bila memungkinkan, periode yang jelas, dan label observasi/agregat/estimasi/proksi.
3. Hasil disajikan sebagai pola, asosiasi, perbandingan relatif, atau perubahan pada seri yang sebanding; bukan klaim kausal atau sensus resmi.
4. Angka estimasi memiliki asumsi, rentang, dan pemeriksaan kewajaran. Ketidaktersediaan suatu sumber tidak boleh ditutup dengan angka rekaan.
5. Ruang lingkup berhenti setelah pertanyaan penelitian terjawab. Penambahan sumber hanya layak jika memperbaiki pengukuran, validasi, atau interpretasi.

## Paket minimum yang cukup

| Konstruk | Paket minimum | Pemeriksaan yang diperlukan |
|---|---|---|
| Massa lokal | Penduduk, bangunan, luas terbangun, atau aktivitas ekonomi pada unit yang sah | Periksa kesesuaian tahun, unit, dan definisi |
| Fungsi lokal | POI/usaha, fasilitas, kelas layanan, struktur sektor, atau pekerjaan terestimasi per domain | Deduplikasi, audit sampel, dan rentang koefisien |
| Relasi metropolitan | Transportasi, waktu tempuh, publikasi komuter, operator, atau kendala OD terbuka | Bedakan arus aktual, kapasitas, aksesibilitas, dan OD sintetis |
| Perubahan | Sedikitnya dua pengamatan yang benar-benar sebanding | Periksa perubahan pencatatan, kategori, batas, dan cakupan |
| Interpretasi | Residual fungsi–ukuran, relasi terarah, dan pemisahan manfaat–beban | Uji spesifikasi, leave-one-source-out, dan ketidakpastian |

Untuk tingkat S1, tiga konstruk pertama sudah cukup. CCTV, SUMO, estimasi OD rinci, dan klasifikasi fungsi tingkat lanjut adalah penguatan, bukan syarat kelulusan desain.

## Urutan prioritas kerja

Urutan berikut adalah urutan **pengerjaan**, bukan ranking ontologis bahwa satu jenis sumber selalu lebih benar daripada jenis lain.

### Prioritas 1 — wajib agar skripsi dapat berjalan

1. Bekukan unit analisis, wilayah pusat sekunder, daftar konstruk, dan periode per modul.
2. Bangun ID entitas dan deduplikasi POI/usaha/fasilitas dari OSM, Overture, direktori, Google Maps yang dapat digunakan secara sah, dan sumber pemda.
3. Padankan entitas dengan bangunan, jaringan, batas wilayah, dan atribut fungsi.
4. Siapkan massa lokal dari BPS, statistik daerah, penduduk, bangunan, luas terbangun, atau indikator aktivitas yang unitnya sah.
5. Siapkan satu jalur relasi metropolitan dari jaringan transportasi, waktu tempuh, laporan operator, atau publikasi komuter terbuka.
6. Buat manifest sumber yang mencatat tanggal akses, periode observasi, unit, definisi, lisensi, metode pembentukan, dan status observasi/estimasi/proksi.
7. Lakukan audit sampel dan uji rentang asumsi sebelum membentuk klasifikasi atau residual.

### Prioritas 2 — penguatan bernilai tinggi

1. Tambahkan sejarah OSM, arsip web, foto/ulasan bertanggal, dan citra terbuka untuk memeriksa perubahan temporal.
2. Tambahkan atribut kelas layanan dan kapasitas fasilitas pendidikan, kesehatan, kampus, serta layanan publik.
3. Tambahkan footprint bangunan, citra Sentinel/Landsat, GHSL, WorldPop, dan cahaya malam untuk memeriksa skala serta intensitas.
4. Gunakan capture–recapture dan tabel konflik sumber untuk mengukur kemungkinan usaha yang luput dan memprioritaskan audit.
5. Uji *leave-one-source-out*, perubahan bobot, dan perubahan koefisien untuk menguji stabilitas hasil.
6. Gunakan lowongan kerja, LPSE, proyek publik, atau struktur cabang sebagai penguat fungsi pekerjaan dan keputusan.
7. Gunakan open routing untuk membandingkan waktu tempuh, transfer, dan ketahanan jaringan.

### Prioritas 3 — opsional setelah inti stabil

1. Mapillary/KartaView/Wikimedia dan audit foto jalan.
2. Listing properti untuk tekanan sewa, kekosongan, dan perubahan fungsi.
3. Kalender acara untuk membaca lonjakan aktivitas sementara.
4. *Sentinel locations* untuk pemantauan berulang.
5. CCTV dan SUMO bila akses, cakupan, privasi, dan kalibrasi benar-benar memadai.
6. Machine learning atau klasifikasi otomatis yang lebih kompleks setelah tersedia sampel audit yang cukup.

Jika waktu terbatas, berhenti setelah Prioritas 1. Jika ada waktu tambahan, pilih paling banyak dua atau tiga item dari Prioritas 2. Prioritas 3 tidak boleh menunda analisis utama.

## Sumber dan pendekatan yang sudah tercatat

- OSM, Overture, Google Maps yang dapat digunakan secara sah, direktori usaha, dan data pemda untuk lokasi serta atribut usaha.
- OSM history, tanggal publikasi, foto/ulasan, situs resmi, berita, dan arsip web untuk perubahan temporal.
- Footprint bangunan, GHSL, WorldPop, Landsat, Sentinel, VIIRS/Black Marble, dan citra terbuka untuk morfologi serta intensitas aktivitas.
- PDDikti, data sekolah, SIRS/akreditasi kesehatan, fasilitas publik, pusat belanja, hotel, kantor, dan fasilitas orde tinggi.
- BPS, PDRB, statistik kecamatan/kabupaten, publikasi komuter, data sektoral, dan laporan operator.
- TransJakarta, MRT Jakarta, LRT Jabodebek, KRL/KAI Commuter, BPTJ, JUTPI, jaringan jalan, GTFS atau jadwal yang tersedia.
- Estimasi pekerjaan dari kategori usaha, bangunan, sektor, dan koefisien yang diuji rentangnya.
- Estimasi relasi melalui gravitasi, radiasi, IPF/Furness, dan kendala marginal yang kompatibel.
- CCTV dan SUMO sebagai opsi setelah audit akses, cakupan, kalibrasi, dan privasi.
- Capture–recapture, active learning, sentinel locations, peta konflik sumber, negative space, dan klasifikasi probabilistik.

## Tambahan yang layak memperkuat rancangan

### 1. Portal geospasial dan tata ruang terbuka

Audit Ina-Geoportal/BIG, RBI, RDTR digital, RTRW, SIMTARU daerah, serta portal geospasial kabupaten/kota. Sumber ini dapat membantu membedakan fungsi yang diizinkan, fungsi yang terbangun, dan fungsi yang benar-benar teridentifikasi. Peta rencana tidak boleh diperlakukan sebagai bukti penggunaan aktual.

### 2. Data perizinan dan pembangunan yang dapat dipublikasikan

Periksa portal PBG/SLF, data proyek, LPSE, pengadaan fasilitas, berita groundbreaking, dan publikasi DPMPTSP yang tersedia. Gunakan sebagai jejak ekspansi kapasitas, bukan sebagai jumlah usaha aktif. Status perizinan juga tidak menjamin kegiatan benar-benar berjalan.

### 3. Data sekolah dan kesehatan yang lebih kaya

Selain jumlah titik, gunakan akreditasi, kelas layanan, kapasitas tempat tidur, program studi, spesialisasi, jadwal layanan, dan jaringan cabang. Ini memperkuat pengukuran fungsi orde tinggi tanpa harus memperoleh data administrasi mikro.

### 4. KartaView, Mapillary, Wikimedia, dan foto jalan terbuka

Jejak foto jalan dapat digunakan untuk pemeriksaan keberadaan papan usaha, perubahan fasad, pembangunan, dan keterisian koridor. Gunakan hanya data dengan izin yang sesuai dan simpan hasil agregat, bukan identitas individu.

### 5. Lowongan kerja dan direktori profesional

Lokasi, sektor, tingkat keahlian, dan frekuensi lowongan dapat menjadi sensor permintaan tenaga kerja serta fungsi bisnis. Lowongan adalah sinyal perekrutan, bukan jumlah pekerja aktual; perlu dibandingkan dengan bangunan, POI, dan struktur sektor.

### 6. Tender, pengadaan, dan jejak proyek publik

LPSE, kontrak proyek, laporan tahunan, dan berita resmi dapat dipakai untuk melacak investasi fasilitas, jaringan, dan peningkatan kapasitas pusat. Pendekatan ini membantu membaca fungsi kelembagaan dan perubahan kapasitas yang tidak tampak dari POI.

### 7. Struktur cabang dan jaringan organisasi

Situs bank, rumah sakit, kampus, hotel, ritel, dan perusahaan dapat digunakan untuk membedakan kantor pusat, kantor regional, cabang, dan titik layanan. Ini membuka dimensi relasi keputusan dan fungsi bisnis, bukan hanya jumlah lokasi.

### 8. Harga sewa dan listing properti sebagai tekanan bayangan

Listing properti publik dapat digunakan sebagai sampel tekanan lahan, kekosongan, dan perubahan fungsi. Sampel harus dicatat menurut tanggal, tipe properti, dan metode deduplikasi. Harga listing bukan transaksi dan tidak boleh disebut nilai pasar tanpa pemeriksaan tambahan.

### 9. Data acara dan kalender publik

Kalender konferensi, pameran, pertandingan, acara kampus, dan agenda ruang publik dapat menjadi indikator daya tarik sementara. Data ini cocok untuk membaca temporalitas dan konsentrasi aktivitas, bukan menggantikan pekerjaan atau penduduk.

### 10. Open routing dan analisis jaringan yang dapat diulang

OSRM, Valhalla, OpenTripPlanner, atau jaringan OSM dapat digunakan untuk menghitung waktu tempuh, transfer, rute alternatif, dan ketahanan konektivitas. Hasilnya tetap aksesibilitas potensial kecuali ada bukti penggunaan aktual.

### 11. Analisis *source disagreement*

Buat tabel konflik antarsumber untuk setiap entitas: ada/tidak ada, kategori, waktu, dan tingkat keyakinan. Konflik menjadi dasar sampling audit manual dan bukan alasan untuk memilih sumber yang paling menguntungkan hipotesis.

### 12. Estimasi cakupan dengan capture–recapture

Irisan OSM, direktori, Google Maps yang sah, dan data pemda dapat digunakan untuk memperkirakan bagian usaha yang tidak tertangkap. Hasilnya harus dilaporkan sebagai estimasi cakupan, bukan koreksi pasti terhadap populasi sebenarnya.

### 13. *Leave-one-source-out* dan pengaruh indikator

Ulangi klasifikasi dengan mengeluarkan satu sumber atau satu indikator secara bergantian. Jika pusat berpindah kelas secara besar-besaran, kesimpulan harus diturunkan menjadi probabilistik atau belum terklasifikasi.

### 14. *Sentinel locations* dan audit berulang

Tetapkan beberapa lokasi tetap per pusat untuk diperiksa berkala. Sampel kecil tetapi konsisten dapat menjadi jangkar untuk membedakan perubahan fenomena dari perubahan keterlihatan digital.

## Yang tidak perlu ditambahkan sebagai syarat

Hal-hal berikut dapat memperkaya penelitian, tetapi terlalu berisiko menjadi beban wajib untuk skripsi S1:

- sensus lengkap semua usaha;
- matriks OD individu atau data ponsel tertutup;
- CCTV seluruh Jabodetabek;
- simulasi SUMO tanpa kalibrasi lapangan;
- machine learning kompleks tanpa validasi manual;
- pengumpulan semua portal dan semua tahun sekaligus;
- klaim bahwa satu sumber terbuka pasti lebih benar daripada semua sumber resmi.

## Gerbang keputusan sebelum analisis utama

Penelitian dapat dianggap siap masuk analisis utama jika:

- satu unit analisis dan wilayah kajian telah dibekukan;
- setiap indikator mencatat sumber, periode, unit, definisi, dan metode pembentukan;
- setiap konstruk inti memiliki proksi utama dan batas klaim;
- nilai kosong dibedakan dari nol;
- minimal sebagian entitas telah diaudit secara manual atau dibandingkan dengan sumber independen;
- estimasi memiliki rentang dan uji sensitivitas;
- periode yang dibandingkan benar-benar sebanding;
- hasil tidak runtuh ketika satu sumber atau indikator dikeluarkan;
- semua keluaran membedakan observasi, estimasi, proksi, dan simulasi.

## Keputusan akhir

Pendekatan yang ada sudah memadai untuk skripsi PWK tingkat sarjana. Tambahan yang paling bernilai bukan menambah kerumitan model, melainkan memperkuat **audit cakupan, sejarah temporal, struktur organisasi, jejak pembangunan, pemeriksaan konflik sumber, dan stabilitas klasifikasi**.

Dengan batas tersebut, skripsi dapat mempertahankan fokus *borrowed size–agglomeration shadow* tanpa bergantung pada permohonan data tertutup dan tanpa berpura-pura memiliki pengukuran resmi yang lengkap.

Rentang tahun, kelengkapan lintas Jabodetabek, ketersediaan atribut, koefisien pekerjaan, izin penggunaan data, serta validasi independen tetap merupakan pertanyaan empiris yang harus diperiksa sebelum setiap modul dibekukan.
