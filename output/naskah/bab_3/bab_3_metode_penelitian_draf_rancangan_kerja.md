# BAB 3 METODE PENELITIAN

> **Arsip draf:** arahan metodologis dalam berkas ini telah digantikan oleh `latex/Bab 3 - Metode Penelitian - final.tex` pada 21 September 2026. Naskah aktif memakai tiga pertanyaan penelitian, istilah Web GIS interaktif, dan rancangan penghitungan objek dari rekaman CCTV dengan deteksi YOLO serta pelacakan objek. Berkas ini dipertahankan sebagai rekaman penyusunan.

> **Arah pada draf, 18 September 2026:** proksi dan sumber terbuka sebagai fondasi utama; multitemporal sesuai bukti. Draf ini tidak menyatakan bahwa semua sumber telah diperoleh atau divalidasi.

## 3.1 Pendekatan penelitian

### 3.1.1 Pilihan pendekatan

Penelitian ini menggunakan **pendekatan kuantitatif (deduktif) dengan analisis spasial-relasional**. Konstruk integrasi metropolitan, fungsi relatif, manfaat, beban, serta gerbang penggunaan label *borrowed size* dan *agglomeration shadow* diturunkan dari kerangka konseptual Bab 2 sebelum klasifikasi dilakukan. Pendekatan ini dipilih karena pertanyaan penelitian menuntut pengukuran hubungan antara pusat sekunder dan Jakarta, perbandingan fungsi aktual dengan fungsi yang diharapkan dari ukuran lokal, serta pengujian stabilitas hasil pada variasi asumsi.

Pendekatan ini tidak berarti semua konstruk harus direduksi menjadi satu angka. Integrasi, fungsi relatif, manfaat, ketergantungan, dan beban dipertahankan sebagai dimensi yang dapat dibaca bersama. Statistik deskriptif, pemetaan, analisis jaringan, tolok ukur, residual, dan uji sensitivitas digunakan sesuai jenis bukti yang tersedia.

Audit dokumen dan audit asal-usul data merupakan prosedur penjaminan mutu. Prosedur ini digunakan untuk memeriksa definisi, tahun, unit, cakupan, cara pembentukan, nilai hilang, dan batas penggunaan data. Pemeriksaan dokumen tersebut tidak menjadikan penelitian ini penelitian campuran karena dokumen tidak dianalisis sebagai data untuk menjawab pertanyaan substantif Angka dalam laporan publik dapat diekstrak sebagai data sekunder apabila tabel atau pernyataan sumber, unit, dan periodenya dapat ditelusuri. Kekosongan angka tidak diisi dengan dugaan yang disamarkan sebagai pengamatan.

### 3.1.2 Alasan kesesuaian dengan pertanyaan penelitian

Kesesuaian pendekatan dengan pertanyaan penelitian diringkas sebagai berikut.

| Kode | Fokus pertanyaan | Alasan menggunakan pendekatan kuantitatif-spasial |
|---|---|---|
| Q1 | Arah, intensitas, dan asimetri hubungan metropolitan | Pengamatan dan estimasi relasi dari sumber terbuka dibandingkan pada unit yang sah. |
| Q2 | Fungsi per domain relatif terhadap massa lokal dan perubahannya pada seri sebanding | Pengukuran atau estimasi fungsi dibandingkan dengan tolok ukur, disertai ketidakpastian. |
| Q3 | Asosiasi relasi metropolitan dengan surplus atau defisit fungsi | Konstruk bersama, sirkularitas, dan penjelasan alternatif diperiksa sebelum interpretasi. |
| Q4 | Heterogenitas hubungan, manfaat, beban, dan fungsi antarpusat | Spesialisasi, hierarki, status administratif, posisi jaringan, dan kondisi lokal digunakan untuk membaca perbedaan. |

Sensitivitas menjadi pemeriksaan lintas keempat pertanyaan, bukan pertanyaan substantif tersendiri.

Pendekatan ini tidak cukup untuk menyatakan dampak kausal pembangunan jalan, perluasan wilayah, atau kebijakan tertentu tanpa strategi identifikasi tambahan. Karena itu, istilah yang dipakai dalam Bab 3 adalah *asosiasi*, *pola*, *surplus atau defisit relatif*, *ketergantungan yang konsisten dengan data*, dan *ketahanan klasifikasi*, bukan “dampak kausal” kecuali desain kelak benar-benar diperkuat.

### 3.1.3 Fondasi pengukuran

Penelitian ini sepenuhnya bertumpu pada proksi dan sumber terbuka, tanpa ketergantungan pada permohonan data tertutup. Data pemerintah yang terbuka tetap dapat digunakan. Pemilihan sumber mengikuti kesesuaian konstruk, cakupan spasial dan temporal, keterulangan pengolahan, serta biaya pemerolehan; status resmi tidak menjadi ukuran mutu dengan sendirinya. Sumber alternatif dapat lebih sesuai daripada data resmi agregat yang tersedia, tetapi keunggulan tersebut diuji per konstruk dan tidak diasumsikan berlaku universal.

## 3.2 Desain penelitian

### 3.2.1 Bentuk desain

Desain penelitian adalah **studi kasus tunggal kuantitatif-spasial dengan desain multitemporal sesuai bukti, diagnosis relasional, dan analisis sensitivitas**. Kasus tunggal dipilih agar pusat-pusat sekunder dapat dibandingkan di dalam satu sistem metropolitan tanpa memperlakukan perbedaan antarmetropolitan sebagai variasi yang setara. Sabuk pembanding fungsional hanya digunakan untuk memperluas tolok ukur apabila definisi, unit, dan periodenya kompatibel.

Desain memiliki tiga lapisan:

1. **Lapisan pengukuran:** observasi langsung atau agregat, proksi, serta hasil estimasi yang dibedakan secara eksplisit pada unit dan periode yang tercantum dalam manifest.
2. **Lapisan diagnosis:** pengukuran integrasi, fungsi relatif, manfaat, beban, dan tipologi dari satu konfigurasi bukti yang dibekukan.
3. **Lapisan ketahanan dan eksplorasi:** perubahan konfigurasi bukti, spesifikasi model, atau nilai skenario yang dibatasi dan selalu dilaporkan terhadap garis dasar tanpa menimpa data observasi.

### 3.2.2 Urutan kerja penelitian

Urutan penelitian sementara adalah sebagai berikut.

1. Menetapkan pertanyaan, konstruk, definisi kerja, dan aturan klaim sebelum melihat hasil klasifikasi.
2. Menginventarisasi berkas dan mencatat asal-usul data setiap modul.
3. Mengaudit tahun, unit, cakupan, definisi, nilai hilang, reliabilitas, dan batas publikasi.
4. Mengharmonisasi geometri dan tabel korespondensi tanpa melakukan disagregasi semu.
5. Menetapkan kandidat pusat sekunder dan wilayah tangkapan fungsional berdasarkan bukti fungsi atau hubungan yang tersedia.
6. Mengukur atau mengestimasi relasi terarah; pisahkan aksesibilitas potensial, estimasi arus, dan arus teramati.
7. Mengukur atau mengestimasi fungsi lokal per domain dan membentuk residual fungsi–ukuran.
8. Memisahkan profil manfaat atau *functional upgrading* dari profil beban atau ketergantungan.
9. Menguji asosiasi relasi–fungsi, heterogenitas antarpusat, dan perubahan pada seri sebanding sebelum menyusun gradien serta kelas.
10. Menjalankan diagnostik spasial dan uji sensitivitas.
11. Menerjemahkan model yang sama ke WebGL dengan garis dasar, skenario, selisih, dan peta ketahanan.
12. Mengunci manifest, tabel indikator, parameter, dan batas klaim untuk reproduksi.

### 3.2.3 Kelebihan dan keterbatasan desain

Desain memungkinkan pengukuran spasial terperinci dan pengamatan beberapa periode dari sumber yang dapat diperiksa tanpa menunggu akses kelembagaan. Keterbatasan data administratif maupun nonpemerintah dinilai secara simetris. Ketersediaan koordinat, panjang seri, dan banyaknya sumber merupakan keunggulan hanya sejauh membantu mengukur konstruk yang dituju.

Galat klasifikasi usaha, duplikasi, cakupan yang berbeda antardaerah, perubahan pencatatan, dan asumsi model dapat memengaruhi hasil. Pemeriksaan independen, harmonisasi, serta propagasi ketidakpastian digunakan untuk mengukur pengaruhnya. Data multitemporal tidak dengan sendirinya mengidentifikasi sebab-akibat.

### 3.2.4 Perbedaan diagnosis dan skenario

Nilai *status quo* dibekukan sebagai garis dasar. Perubahan penggeser atau parameter tidak boleh menimpa nilai observasi, mengubah batas administratif, atau disajikan sebagai prediksi. Setiap skenario menyimpan konfigurasi indikator, bobot, ambang, nilai yang diubah, dan alasan substantif perubahan.

Perubahan karena sumber data diperoleh, hilang, atau turun mutu dicatat sebagai **skenario bukti**. Perubahan bobot, ambang, atau spesifikasi dalam konfigurasi bukti yang sama dicatat sebagai **skenario parameter**. Perubahan nilai indikator untuk pertanyaan *what-if* merupakan eksplorasi kondisional tambahan. Ketiganya tidak boleh ditampilkan sebagai jenis perubahan yang sama.

## 3.3 Ruang lingkup penelitian

### 3.3.1 Ruang lingkup spasial

Kasus utama adalah Jabodetabek sebagai kawasan utama penelitian, dengan sabuk Wilayah Statistik Metropolitan sebagai pembanding fungsional apabila datanya kompatibel. Kasus ini dipilih karena memungkinkan hubungan antara satu inti dan kandidat pusat sekunder lintas batas administratif diperiksa di dalam sistem metropolitan yang sama. DKI Jakarta diperlakukan sebagai satu inti untuk hubungan eksternal, dengan batas administratif tetap. Data rinci di dalam DKI tetap dapat digunakan untuk pemeriksaan internal, tetapi tidak mengubah keputusan bahwa DKI diperlakukan sebagai satu inti dalam klasifikasi eksternal.

Wilayah di luar DKI tidak disebut sebagai “wilayah Jakarta” hanya karena masuk dalam gradien analisis. Istilah yang digunakan adalah **jejak fungsional Jakarta**, **zona analitis keterkaitan metropolitan**, atau **gradien integrasi-ketergantungan metropolitan**. Istilah tersebut bukan zonasi legal RTRW dan tidak mengubah kewenangan pemerintah daerah.

Seluruh wilayah administratif di sekitar Jakarta tidak diasumsikan otomatis menjadi unit analisis yang tepat. Delineasi akhir harus menjelaskan sumber, tahun, definisi, dan alasan memasukkan atau mengeluarkan setiap unit.

### 3.3.2 Ruang lingkup temporal

Desain penelitian bersifat multitemporal sesuai bukti: perubahan dianalisis pada indikator dengan seri yang sebanding, sedangkan indikator lain dianalisis pada periode yang tersedia. Tahun dasar dan rentang analisis ditetapkan per modul setelah audit; panel lengkap dan satu tahun jangkar untuk semua sumber tidak diasumsikan.

Setiap modul menyimpan tahun observasi, tanggal ekstraksi, waktu publikasi, dan periode berlakunya atribut. Analisis perubahan mensyaratkan sedikitnya dua pengamatan yang sebanding; dua titik tidak disebut tren tahunan. Riwayat suntingan OSM dan tanggal kemunculan dalam direktori bukan otomatis tanggal berdiri atau tutup usaha. Data mutakhir tidak diproyeksikan ke masa lalu tanpa model dan bukti. Seri tidak sebanding dianalisis terpisah; interpolasi, jika digunakan, diberi label estimasi dan tidak menambah jumlah observasi independen.

### 3.3.3 Ruang lingkup substantif

Penelitian mencakup:

- integrasi atau eksposur metropolitan;
- fungsi lokal dan fungsi relatif terhadap ukuran serta karakteristik lokal;
- manfaat akses, *functional upgrading*, dan potensi retensi manfaat;
- beban komuter, ketergantungan, kebocoran nilai, dan defisit fungsi;
- tipologi *borrowed size*, campuran/transisional, *agglomeration shadow*, relatif independen, dan periferi lemah;
- sensitivitas indikator, bobot, ambang, unit, dan status mutu bukti; serta
- penyajian hasil dalam atlas, tabel, peta, dan WebGL.

Penelitian tidak mencakup penetapan radius geometris Jakarta, rekomendasi perubahan batas administrasi, pembuktian kausal seluruh kebijakan metropolitan, atau klaim produktivitas penuh jika fungsi ekonomi pada unit yang sesuai tidak tersedia.

## 3.4 Unit amatan dan unit analisis

### 3.4.1 Unit amatan

Unit amatan adalah satuan tempat setiap observasi dicatat pada sumber. Satuan tersebut dapat berupa desa/kelurahan, kecamatan, kabupaten/kota, zona asal-tujuan, titik fasilitas, atau sel raster. Kecamatan menjadi sasaran unit amatan utama untuk modul yang memiliki bukti relasional dan fungsi yang kompatibel karena cukup rinci untuk membedakan kandidat pusat sekunder dan wilayah sekitarnya.

Kecamatan tidak dipaksakan ketika data kritis hanya tersedia pada kabupaten/kota atau zona model. Dalam keadaan tersebut, perhitungan dilakukan pada unit sumber atau sebagai analisis paralel multiresolusi. Alokasi nilai kabupaten/kota ke kecamatan, kisi, atau titik hanya dilakukan dengan model eksplisit berbasis informasi lokal, pemeriksaan independen, dan ketidakpastian; hasil tetap merupakan estimasi, bukan observasi rinci.

Kisi atau heksagon hanya digunakan untuk data yang berasal dari raster atau titik, misalnya cahaya malam, morfologi terbangun, atau titik minat. Kisi dapat menjadi unit perhitungan utama bagi modul yang didukung titik atau raster. Resolusi keluaran mengikuti kemampuan pengukuran; koordinat rinci tidak otomatis menjamin ketepatan nilai atribut.

### 3.4.2 Unit analisis substantif

Unit analisis substantif adalah kandidat pusat sekunder beserta wilayah tangkapan fungsionalnya. Secara operasional, satu pusat dapat direpresentasikan oleh satu kecamatan, beberapa unit yang bersebelahan, atau zona sumber selama aturan pembentukannya dibekukan dan dapat direproduksi. Kabupaten/kota tetap menjadi lapisan agregasi kebijakan, layanan, APBD, dan tanggung jawab pemerintahan, tetapi tidak otomatis menjadi pusat sekunder.

Daftar kandidat awal dibentuk dari konsentrasi aktivitas dan fungsi dalam sumber terbuka, serta dibandingkan dengan pusat yang dikenali dalam dokumen perencanaan. Penetapannya menggunakan bukti kepadatan aktivitas, fungsi layanan, pekerjaan, kawasan industri, posisi jaringan, atau arus yang tersedia. Variabel untuk delineasi dipisahkan dari variabel hasil sejauh data memungkinkan. Jika indikator yang sama harus digunakan pada kedua tahap, ketahanan klasifikasi diuji kembali dengan mengeluarkan indikator tersebut agar penetapan pusat tidak menjadi pembuktian sirkular.

### 3.4.3 Aturan keterbandingan unit

Setiap indikator dicatat dengan unit asli, unit perhitungan, unit pelaporan, dan operasi transformasinya. Satu klasifikasi hanya dihitung jika bukti relasional dan bukti fungsi dapat dipadankan pada unit, wilayah tangkapan, dan periode yang sebanding atau dapat diagregasikan secara sah. Harmonisasi mengikuti aturan:

1. gunakan unit asli untuk perhitungan awal;
2. gunakan tabel korespondensi resmi jika tersedia;
3. agregasikan unit rinci ke unit lebih kasar bila operasi tersebut sah;
4. jalankan analisis paralel bila unit tidak dapat disetarakan;
5. keluarkan modul jika keterbandingan tidak dapat dipertanggungjawabkan; dan
6. jangan membandingkan skor lintas konfigurasi bukti sebagai perubahan kondisi tanpa menyatakan perbedaan sumber dan unitnya.

### 3.4.4 Populasi, cakupan, dan validasi manual

Populasi analisis adalah seluruh kandidat pusat dan wilayah tangkapan yang masuk dalam delineasi akhir serta mempunyai bukti yang memenuhi aturan modul. Jika sumber merupakan sensus atau inventaris seluruh unit, penelitian tidak mengambil sampel statistik tambahan. Pemeriksaan manual dilakukan secara purposif pada tiga sampai lima pusat sekunder prioritas untuk memeriksa lokasi kampus dan rumah sakit; usaha dan titik minat lain diperiksa pada sampel terarah yang mencakup variasi sektor, koridor, dan tingkat ketercakupan. Audit silang memeriksa asal-usul sumber agar dua salinan data yang sama tidak dianggap dua bukti independen. Kriteria pemilihan pusat validasi dicatat sebelum pemeriksaan. Validasi terbatas tersebut bukan sampel inferensial dan tidak digeneralisasikan sebagai sensus seluruh kawasan.

## 3.5 Metode pengumpulan data

### 3.5.1 Prinsip pengumpulan data

Penelitian ini sepenuhnya bertumpu pada proksi dan sumber terbuka, tanpa ketergantungan pada permohonan data tertutup. Data pemerintah yang terbuka tetap dapat digunakan. Pemilihan sumber mengikuti kesesuaian konstruk, cakupan spasial dan temporal, keterulangan pengolahan, serta biaya pemerolehan; status resmi tidak menjadi ukuran mutu dengan sendirinya.

Akuisisi mengikuti sumber yang benar-benar dapat digunakan: unduhan, layanan data, direktori publik, laporan operator, publikasi statistik, serta ekstraksi dokumen dengan locator tabel atau halaman. Metode pengambilan OSM dan Google Maps ditetapkan setelah audit kemampuan akses; penelitian tidak menganggap satu endpoint pencarian sebagai satu-satunya cara akuisisi atau hasil pencarian sebagai sensus lengkap. Terlihat publik tidak otomatis berarti tersedia sebagai unduhan terbuka atau dapat dibagikan ulang; kemampuan akuisisi dan reproduksi dicatat per sumber.

### 3.5.2 Kelompok sumber dan konstruksi data

Tabel berikut adalah rancangan sumber yang perlu diperiksa. Penyebutan sumber tidak menyatakan bahwa seri, atribut, atau cakupan seluruh Jabodetabek telah tersedia.

| Modul | Kandidat sumber terbuka | Konstruksi pengukuran dan pemeriksaan |
|---|---|---|
| Batas dan massa lokal | BIG, publikasi BPS, sumber pemda, raster penduduk | Geometri, penduduk, dan karakteristik lokal; samakan definisi, tahun, serta batas. |
| Usaha dan pekerjaan | OSM, Overture, Google Maps yang dapat digunakan, direktori usaha, bangunan, publikasi sektoral | Deduplicasi dan padankan lokasi serta kategori; estimasikan pekerjaan dari koefisien beralasan, skala bangunan, dan informasi usaha. |
| Fungsi layanan | Direktori fasilitas, PDDikti, SIRS, sumber kelas atau akreditasi publik | Padankan lokasi fisik, kelas, spesialisasi, kapasitas, dan akreditasi beserta masa berlakunya; jumlah fasilitas dan mutu tidak disamakan. |
| Jaringan dan layanan angkutan | OSM, GTFS yang tersedia, laporan TransJakarta, MRT, LRT, KRL, dan publikasi transportasi | Pisahkan rute, frekuensi, armada, kapasitas, penumpang, serta waktu; cakupan operator tidak dianggap mewakili semua moda. |
| Relasi terarah | Tabulasi komuter publik, WSM, laporan BPTJ/JUTPI yang terbuka, informasi operator | Gunakan observasi pada resolusi sumber atau kendala bagi estimasi OD; marginal dan kapasitas bukan pasangan arus aktual. |
| Ekonomi dan morfologi | PDRB publik, direktori kawasan industri, GHSL, WorldPop, VIIRS, citra terbuka | Konteks sektor, keterbangunan, dan aktivitas; produktivitas hanya diestimasi apabila pembilang dan penyebut kompatibel. |
| Pemeriksaan tambahan | Sumber terbuka independen, dokumentasi lokasi, CCTV yang dapat digunakan | Periksa cakupan waktu dan lokasi; CCTV/SUMO merupakan opsi yang memerlukan audit, bukan syarat terlaksananya penelitian. |

Apabila definisi atau ambang suatu publikasi bertentangan, simpan versi dan locator yang relevan, gunakan hanya variabel yang dapat ditafsirkan, dan uji alternatif yang masuk akal. Penelitian tidak menunggu jawaban instansi untuk menggunakan modul lain yang sudah dapat dipertanggungjawabkan.

### 3.5.3 Instrumen pengumpulan dan dokumentasi data

Karena penelitian menggunakan data sekunder, instrumen pengumpulan bukan kuesioner atau panduan wawancara. Instrumen kerja terdiri atas:

1. log akses untuk mencatat alamat sumber, tanggal akses, dan syarat penggunaan;
2. formulir audit berkas dan registri asal-usul data;
3. kamus data yang memuat definisi variabel, unit, tahun, nilai hilang, dan polaritas;
4. tabel korespondensi kode serta geometri antarversi;
5. manifest konfigurasi bukti dan parameter; serta
6. lembar pemeriksaan manual untuk kampus dan rumah sakit pada pusat prioritas.

Skrip akuisisi, pembersihan, transformasi, dan analisis diperlakukan sebagai bagian dari instrumen yang dapat direproduksi. Nama perangkat lunak, versi, parameter, dan tanggal pengolahan dicatat setelah perangkat benar-benar digunakan; Bab 3 tidak mengunci perangkat yang belum dipakai.

### 3.5.4 Audit dan status mutu bukti

Setiap berkas dicatat dalam registri asal-usul data sekurang-kurangnya menurut sumber, nama/versi berkas, tanggal akses, tahun observasi, unit, cakupan, definisi, metode pembentukan, nilai hilang, reliabilitas, lisensi, dan pembatasan publikasi.

| Status | Nama | Aturan penggunaan |
|---|---|---|
| D | Langsung | Konstruk teramati pada unit dan periode sasaran dengan mutu memadai. |
| A | Agregat | Konstruk teramati, tetapi unit, waktu, kategori, atau cakupan lebih kasar. |
| S | Sintetis | Nilai diestimasi dari data lain; asumsi, kalibrasi, dan ketidakpastian wajib ditampilkan. |
| P | Proksi | Mengukur gejala terkait, bukan konstruk yang hendak diklaim secara langsung. |
| ∅ | Dikeluarkan | Tidak tersedia, tidak sebanding, tidak reliabel, atau tidak dapat dipertanggungjawabkan. |

Status tersebut menjelaskan cara pengukuran, bukan urutan mutu sumber. Data resmi maupun nonpemerintah dapat mengandung galat. Pengamatan langsung pada unit publikasi tidak otomatis merupakan pengamatan langsung pada unit penelitian. Misalnya, survei kabupaten/kota dapat berstatus A untuk penelitian berkecamatan; jaringan dapat berstatus P untuk integrasi aktual; dan tabel bangkitan-tarikan dapat berstatus S atau A jika tidak memuat pasangan arus teramati.

### 3.5.5 Harmonisasi spasial dan temporal

Harmonisasi dilakukan setelah audit, bukan sebelum audit. Tahun dasar dan rentang perbandingan ditetapkan per modul setelah audit kesebandingan. Variabel dari 2023 atau 2025 tidak dinormalisasi ulang untuk menyembunyikan perbedaan tahun. Setiap peta, tabel, dan skor menyimpan tahun sumber dan status perbandingannya.

Untuk data spasial, geometri unit asli dipertahankan dalam arsip kerja. Tabel korespondensi resmi digunakan bila tersedia. Agregasi dari desa ke kecamatan dapat dilakukan bila definisi, kode, dan cakupan mendukung. Disagregasi nilai kabupaten/kota ke kecamatan dilarang kecuali ada model eksplisit, asumsi terlihat, validasi, dan pelabelan sintetis.

### 3.5.6 Konstruksi proksi dan estimasi

Pekerjaan dapat diestimasi dari jenis dan skala usaha, bangunan yang dipadankan, serta koefisien tenaga kerja dengan sumber yang dapat diperiksa. Dasar koefisien, variasi sektor, usaha informal, duplikasi cabang, tingkat hunian, dan lokasi kerja dibedakan. Koefisien dari wilayah atau periode lain diuji rentangnya; angka tidak dibuat sekadar untuk melengkapi tabel. Jika koefisien belum memiliki dasar, keluaran sementara tetap berupa fungsi atau skala usaha.

Relasi asal–tujuan dapat diestimasi dengan model gravitasi atau radiasi. Penyeimbangan IPF/Furness digunakan hanya jika marginal asal dan tujuan kompatibel dan totalnya konsisten atau penyesuaiannya beralasan. Ketidakpastian fungsi hambatan, massa tujuan, pilihan moda, dan arus internal diperiksa. Data yang digunakan untuk kalibrasi tidak dilaporkan sebagai validasi independen. Kecocokan marginal tidak membuktikan keunikan matriks OD.

Laporan tahunan dan berita dapat menyediakan informasi armada, perjalanan, kapasitas, atau penumpang; setiap angka harus memiliki periode, unit, dan rujukan yang jelas. Kapasitas kendaraan memerlukan asumsi frekuensi, operasi, serta keterisian untuk memperkirakan penggunaan. CCTV memerlukan audit akses rekaman, lokasi, jam, kelas kendaraan, serta cakupan pengamatan. SUMO dapat digunakan untuk simulasi terkalibrasi bila kebutuhan tersebut terpenuhi, tetapi simulasi tidak menciptakan pengamatan arus atau asal–tujuan yang belum tersedia.

Validasi menggunakan sumber terbuka dengan jalur pencatatan berbeda, pengamatan terarah, atau data yang disisihkan dari kalibrasi. Jika pemeriksaan independen belum tersedia, keluaran relasional dilaporkan sebagai estimasi eksploratif dengan rentang ketidakpastian; keterbatasan ini tidak menghentikan modul fungsi atau aksesibilitas yang valid.

### 3.5.7 Etika, lisensi, dan keamanan

Data yang dapat diakses publik tetap diperiksa syarat pemakaian, privasi, dan hak penyebarluasan turunannya. Pengamatan CCTV hanya menyimpan statistik yang diperlukan, bukan identitas individu. Keluaran WebGL mengikuti izin publikasi setiap sumber. Peta publik hanya memuat data yang boleh dipublikasikan, agregasi yang sah, atau proksi yang diberi label. Nilai penggeser tidak boleh mengungkap data mentah atau memungkinkan rekonstruksi unit sensitif.

## 3.6 Metode analisis data

### 3.6.1 Langkah 1: audit, dokumentasi, dan pembekuan garis dasar

Analisis dimulai dengan tabel audit yang menghubungkan konstruk, indikator, sumber, tahun, unit, polaritas, status bukti, aturan transformasi, dan batas klaim. Garis dasar dibekukan setelah tahap audit awal agar skenario tidak mengubah nilai observasi.

Pada tahap ini ditetapkan pula indikator yang dikeluarkan karena duplikasi, cakupan yang tidak memadai, proporsi nilai hilang yang mengganggu keterbandingan, ketidakcocokan unit, atau ketidakjelasan definisi. Pengeluaran indikator dicatat sebagai keputusan metodologis, bukan dihapus tanpa jejak.

### 3.6.2 Langkah 2: delineasi pusat sekunder dan wilayah tangkapan fungsional

Kandidat pusat sekunder berangkat dari daftar yang dikenali dalam sumber resmi, kemudian diuji dengan bukti fungsi dan hubungan yang tersedia. Bukti yang dapat digunakan meliputi kepadatan aktivitas, fasilitas, pekerjaan, kawasan industri, posisi jaringan, arus perjalanan, atau kombinasi yang ditetapkan sebelum pengukuran fungsi relatif dan klasifikasi.

Setiap kandidat diberi alasan masuk, sumber, unit, periode, dan tingkat ketidakpastian. Aturan pembentukan wilayah tangkapan fungsional dibekukan untuk setiap konfigurasi bukti sebelum hasil fungsi relatif dihitung. Wilayah tangkapan dapat berbeda antarkonfigurasi bukti, tetapi perubahan tersebut harus diberi versi dan tidak boleh ditampilkan sebagai perubahan kondisi metropolitan. Wilayah tangkapan merupakan konstruksi analitis, bukan batas administratif baru.

### 3.6.3 Langkah 3: pengukuran integrasi metropolitan

Relasi metropolitan diukur melalui tiga bentuk bukti yang tidak disusun sebagai hierarki sumber resmi dan nonresmi:

| Bentuk bukti | Konstruksi | Interpretasi |
|---|---|---|
| Pengamatan relasi | Pasangan arus atau orientasi dari sumber publik | Relasi teramati pada unit, moda, populasi, dan periode sumber. |
| Estimasi relasi | OD sintetis dengan massa, jaringan, kendala, serta pemeriksaan independen | Relasi terestimasi dan ketidakpastiannya; tidak disebut pengamatan langsung. |
| Aksesibilitas potensial | Kesempatan tujuan dan biaya jaringan | Potensi akses; tidak dengan sendirinya menunjukkan arus terealisasi. |

Tidak adanya OD rinci terbuka tidak menggugurkan rancangan estimasi. Kemampuan menjawab relasi dinilai dari validasi dan identifikasi modelnya.

Jika tersedia, arah arus dibedakan dari kedekatan. Waktu tempuh atau jarak jaringan saja hanya mengukur aksesibilitas potensial. Persentase komuter ke inti dapat mengukur orientasi pada unit sumber, tetapi tidak otomatis menjelaskan hubungan antarpusat sekunder.

Jika matriks asal-tujuan yang kompatibel tersedia, proporsi orientasi unit $i$ menuju inti Jakarta dihitung sebagai

$$
O_i = \frac{\sum_{j \in J} F_{ij}}{\sum_j F_{ij}},
$$

dengan $F_{ij}$ sebagai arus teramati atau terestimasi (status dilaporkan) dari unit $i$ menuju unit $j$ dan $J$ sebagai himpunan zona inti Jakarta yang ditetapkan sebelum perhitungan. Arus internal atau *self-containment* hanya dihitung sebagai $F_{ii}/\sum_j F_{ij}$ apabila definisi perjalanan, zona, dan populasi pembentuk matriks mendukung. Jika sumber hanya menerbitkan persentase orientasi, nilai sumber digunakan pada unit publikasinya tanpa merekonstruksi pasangan arus yang tidak tersedia.

Jika bukti yang tersedia hanya jaringan atau waktu tempuh, aksesibilitas potensial dapat dihitung dengan bentuk umum

$$
A_i = \sum_j W_j f(c_{ij}),
$$

dengan $W_j$ sebagai besaran kesempatan pada tujuan $j$, $c_{ij}$ sebagai biaya perjalanan jaringan, dan $f(\cdot)$ sebagai fungsi hambatan yang dinyatakan serta diuji sensitivitasnya. Nilai $A_i$ tidak disebut integrasi aktual karena tidak memuat arus yang teramati.

Profil integrasi tidak harus berupa satu indeks. Bila indeks ringkas digunakan, setiap komponen, polaritas, bobot, dan aturan normalisasi disimpan. Integrasi yang tinggi tidak otomatis berarti manfaat tinggi karena dapat berdampingan dengan beban dan ketergantungan.

### 3.6.4 Langkah 4: pengukuran fungsi lokal dan fungsi relatif

Fungsi lokal dibangun per domain dari titik usaha dan fasilitas, atribut skala dan mutu, bangunan, serta informasi sektoral. Kehadiran fasilitas dapat menjadi observasi langsung untuk keberadaan layanan dan sekaligus proksi untuk konstruk kematangan. Pekerjaan yang diestimasi tidak otomatis lebih rendah mutunya daripada tabulasi agregat; keduanya dibandingkan menurut kesesuaian unit, definisi, cakupan, dan hasil pemeriksaan.

Kesalahan pencocokan lokasi, koefisien pekerjaan, kapasitas fasilitas, dan cakupan usaha diteruskan ke rentang nilai fungsi. Produktivitas tidak disimpulkan hanya dari jumlah POI atau intensitas cahaya.

Fungsi relatif dihitung terpisah untuk setiap konstruk $k$, misalnya fungsi layanan atau pekerjaan, agar residual pada satu konstruk tidak diberi nama konstruk lain. Secara umum, tingkat fungsi yang diharapkan dapat dinyatakan sebagai

$$
g_k(Y_{ik}) = \alpha_k + \beta_k h(S_i) + \boldsymbol{\gamma}_k^{\mathsf T}\mathbf{X}_i + \varepsilon_{ik},
$$

dengan $Y_{ik}$ sebagai nilai fungsi yang diukur atau diestimasi pada konstruk $k$, $S_i$ sebagai ukuran lokal, $\mathbf{X}_i$ sebagai karakteristik lokal yang ditetapkan sebelum klasifikasi, serta $g_k(\cdot)$ dan $h(\cdot)$ sebagai transformasi yang dipilih berdasarkan skala pengukuran serta diagnostik data. Residual fungsi dihitung sebagai

$$
R_{ik}=g_k(Y_{ik})-\widehat{g_k(Y_{ik})}.
$$

Residual positif berarti surplus relatif dan residual negatif berarti defisit relatif pada konstruk $k$. Residual layanan tidak disebut surplus produktivitas; nilai titik minat tidak disebut pekerjaan; dan potret satu tahun tidak disebut *functional upgrading* temporal.

Pemilihan tolok ukur dilakukan sebelum tipologi dibentuk. Model fungsi-ukuran digunakan hanya jika jumlah unit efektif, bentuk distribusi, residual, dan pengaruh pencilan memadai untuk konstruk yang dimodelkan. Jika syarat tersebut tidak terpenuhi, tingkat yang diharapkan dibentuk melalui kelompok pembanding ukuran yang transparan atau ringkasan pembanding lain yang dapat direproduksi. Pilihan model, populasi pembanding, transformasi, prediksi, dan ketidakpastian dicatat. Jika tolok ukur hanya memakai pusat internal kawasan studi, hasil disebut relatif terhadap kawasan studi dan tidak digeneralisasikan sebagai ukuran universal.

### 3.6.5 Langkah 5: pemisahan manfaat, ketergantungan, dan beban

Manfaat dan beban tidak dipaksa masuk ke satu sumbu yang saling meniadakan. Profil manfaat dibentuk dari akses pekerjaan, surplus fungsi, produktivitas atau upah, keragaman fungsi, dan kemampuan memenuhi kebutuhan lokal hanya jika indikator tersebut benar-benar teramati atau memiliki proksi yang diberi label. Profil beban dibentuk dari orientasi yang sangat bergantung pada inti, durasi atau biaya perjalanan, dan defisit fungsi pada unit yang kompatibel. Kebocoran nilai, *upgrading*, atau spesialisasi subordinat tidak menjadi indikator operasional apabila data yang diperlukan tidak tersedia; istilah tersebut hanya dapat digunakan sebagai interpretasi terbatas yang ditopang bukti.

Komuter dapat berarti akses yang meningkat sekaligus beban perjalanan. Industrialisasi dapat berarti *upgrading* atau fungsi subordinat. Oleh karena itu, polaritas ditetapkan per konstruk dan tidak disimpulkan dari tanda positif atau negatif mentah.

### 3.6.6 Langkah 6: diagnosis tipologi dan gradien

Diagnosis dimulai dari vektor profil multidimensi, kemudian diringkas menjadi kategori jika diperlukan untuk komunikasi. Jika beberapa indikator digabung dalam satu dimensi $d$, skor ringkas hanya dihitung dalam satu konfigurasi bukti dengan himpunan indikator yang tetap:

$$
Z_{id}=\frac{\sum_{k \in K_d} w_k z_{ik}}{\sum_{k \in K_d} w_k}, \qquad w_k \geq 0.
$$

Nilai $z_{ik}$ adalah indikator yang telah ditransformasi dan diarahkan secara konsisten, sedangkan $w_k$ adalah bobot yang disimpan dalam manifest. Nilai hilang tidak diubah menjadi nol. Jika komponen wajib tidak tersedia pada satu unit, skor dimensi dan kelas unit tersebut dinyatakan tidak dapat dihitung dalam konfigurasi itu. Normalisasi dilakukan terhadap populasi pembanding garis dasar yang dibekukan agar perubahan skenario tidak mengubah titik acuan secara tersembunyi.

Logika kategori kerja ditetapkan sebagai berikut. Nilai ambang belum diberi angka sebelum distribusi data, dasar teoretis atau kebijakan, dan diagnostik diperiksa; ambang garis dasar yang dipilih harus dibekukan sebelum klasifikasi dan diuji sensitivitasnya.

| Kategori kerja | Konfigurasi minimum | Batas interpretasi |
|---|---|---|
| Relatif independen | hubungan dengan inti berada di bawah ambang integrasi, sedangkan fungsi lokal tidak menunjukkan defisit yang berarti | bukan bukti autarki atau tidak adanya hubungan metropolitan |
| Pola konsisten dengan *borrowed size* | bukti relasional berada di atas ambang dan residual fungsi pada konstruk yang diuji positif | istilah ketat hanya digunakan setelah empat gerbang bukti terpenuhi; “integrasi produktif” bukan sinonim otomatis |
| Campuran atau transisional | arah residual berbeda antarkonstruk, atau manfaat dan beban sama-sama tinggi | perbedaan dimensi harus tetap terlihat dan tidak dirata-ratakan menjadi label tunggal |
| Pola konsisten dengan *agglomeration shadow* | bukti relasional berada di atas ambang dan residual fungsi pada konstruk yang diuji negatif; bukti beban dapat memperkuat diagnosis | tidak membuktikan bahwa Jakarta menyebabkan defisit tersebut |
| Periferi lemah | hubungan dengan inti dan fungsi lokal sama-sama rendah | tidak disebut *shadow* Jakarta tanpa hubungan relasional yang memadai |
| Tidak terselesaikan | unit tidak kompatibel, komponen wajib hilang, atau kelas tidak stabil pada spesifikasi utama | ketidakpastian dilaporkan sebagai hasil, bukan dipaksa masuk ke kelas terdekat |

Label ketat *borrowed size* atau *agglomeration shadow* hanya dapat dipakai bila empat gerbang berikut terpenuhi:

1. ada bukti relasional terhadap Jakarta dari pengamatan atau estimasi yang diperiksa secara independen, bukan hanya jarak atau waktu tempuh;
2. ada tolok ukur fungsi relatif yang mengukur konstruk substantif pada unit yang memadai;
3. bukti relasional dan fungsi dapat dihubungkan pada unit, wilayah tangkapan, dan periode yang sebanding; dan
4. label tidak runtuh pada uji sensitivitas utama atau tidak bergantung pada satu proksi bermasalah.

Jika satu gerbang gagal, istilah yang dipakai adalah **profil**, **surplus/defisit relatif**, atau **pola yang konsisten dengan** konstruk tertentu. Penurunan klaim menjadi bagian dari hasil metodologis.

### 3.6.7 Langkah 7: diagnostik spasial dan ketahanan hasil

Paket diagnostik minimum mencakup korelasi dan duplikasi indikator, pengeluaran satu indikator secara bergiliran (*leave-one-indicator-out*), variasi bobot dan ambang, serta perubahan unit ketika perbandingan multiresolusi dapat dilakukan secara sah. Pergantian observasi, agregat, estimasi, atau proksi dibandingkan sebagai konfigurasi bukti terpisah; status tersebut bukan tangga mutu otomatis. Perubahan definisi pusat atau wilayah tangkapan diuji apabila lebih dari satu delineasi dapat dipertanggungjawabkan.

Autokorelasi global dan pengelompokan lokal hanya dihitung apabila jumlah unit, geometri, dan matriks bobot spasial memadai. Definisi ketetanggaan atau jarak serta penanganan pulau spasial dinyatakan sebelum perhitungan dan diuji dengan spesifikasi alternatif yang wajar. Model regresi spasial bukan syarat desain minimum S-1; model tersebut hanya digunakan sebagai penguatan jika diagnostik menunjukkan kebutuhan dan asumsi model dapat dipenuhi.

Ketahanan tidak diringkas hanya sebagai persentase kelas yang sama. Peta perpindahan, rentang skor, unit tidak terselesaikan, dan alasan perubahan perlu ditampilkan. Kategori “tidak terselesaikan” adalah keluaran yang sah ketika spesifikasi menghasilkan kesimpulan berbeda secara substantif.

### 3.6.8 Langkah 8: skenario, sensitivitas, dan implementasi WebGL

Analisis membedakan tiga keluarga perubahan.

1. **Skenario bukti (`EV-*`)** menguji hasil ketika sumber atau status mutu bukti berubah. Setiap skenario menyimpan sumber, tahun, unit, status D/A/S/P/∅, indikator yang aktif, dan klaim yang diperbolehkan. Perbedaan kelas antarskenario bukti menunjukkan ketergantungan kesimpulan pada bukti, bukan perubahan kondisi metropolitan.
2. **Skenario parameter (`P-*`)** menguji bobot, ambang, normalisasi, indikator, atau spesifikasi lain dalam satu konfigurasi bukti yang sama. Skenario ini merupakan analisis sensitivitas model.
3. **Skenario nilai indikator** mengubah nilai dalam rentang terkalibrasi untuk pertanyaan *what-if*. Skenario ini merupakan eksplorasi kondisional, bukan bagian dari diagnosis *status quo* atau prediksi kausal kebijakan.

Garis dasar observasi, konfigurasi bukti, dan populasi pembanding dibekukan sebelum ketiga keluarga perubahan dijalankan. Setiap konfigurasi menyimpan nilai garis dasar, nilai skenario, selisih, kelas sebelum-sesudah, dan status kelayakan. Nilai yang tidak teramati tidak diberi tampilan seolah-olah merupakan observasi, dan kombinasi yang tidak masuk akal secara substantif ditolak oleh aturan validasi. Batas administratif DKI selalu terlihat sebagai lapisan tetap.

Keluaran empiris utama-tabel, profil, peta diagnosis, dan audit ketahanan-harus dapat dihasilkan tanpa WebGL. WebGL menerapkan model yang sama sebagai antarmuka keluaran kedua. Keluaran minimalnya adalah peta garis dasar, peta skenario, peta selisih, daftar unit yang berpindah kelas, dan peta ketahanan atau ketidakpastian. Penghitungan ulang serta visualisasi interaktif tidak disebut data waktu nyata atau prediksi masa depan.

### 3.6.9 Keterlacakan pertanyaan dan analisis asosiasi

| Pertanyaan | Bukti dan operasi | Keluaran |
|---|---|---|
| Q1: relasi terarah | Pengamatan atau estimasi relasi, arah, intensitas, dan asimetri; aksesibilitas disajikan terpisah | Profil relasi dengan status pengukuran dan ketidakpastian. |
| Q2: fungsi relatif dan perubahan | Fungsi terukur atau terestimasi, massa lokal, tolok ukur per domain, seri yang lolos harmonisasi | Residual per domain dan perubahan pada periode sebanding. |
| Q3: asosiasi relasi–fungsi | Hubungkan dimensi relasi dengan residual fungsi; periksa masukan bersama dan alternatif penjelasan | Arah, besaran, dan ketidakpastian asosiasi. |
| Q4: heterogenitas | Bandingkan spesialisasi, hierarki, status administratif, posisi jaringan, kondisi lokal, serta aktor | Profil manfaat, beban, dan konfigurasi antarpusat; tipologi jika stabil. |

Untuk Q3, residual fungsi per domain dianalisis terhadap dimensi relasi terarah, dengan kovariat lokal yang beralasan dan jumlah parameter yang sesuai jumlah unit efektif. Paparan relasional tidak dimasukkan ke tolok ukur utama fungsi–ukuran. Jika sampel tidak mendukung regresi, perbandingan profil atau kelompok digunakan dengan batas interpretasi eksplisit. Bentuk nonlinier dan heterogenitas diuji apabila dukungan data memadai.

Jika POI atau pekerjaan tujuan dipakai untuk membentuk OD sekaligus menjadi variabel hasil, lakukan spesifikasi yang mengeluarkan komponen bersama dan gunakan pemeriksaan relasi independen. Asosiasi yang terutama dihasilkan masukan model tidak dijadikan bukti pengaruh integrasi. Galat koefisien, pencocokan, cakupan, serta estimasi arus dipropagasikan melalui penghitungan ulang pada rentang asumsi yang beralasan.

### 3.6.10 Analisis multitemporal dan batas keterbandingan

Buat daftar cakupan pusat–indikator–tahun. Pilih jendela perbandingan per domain berdasarkan definisi, geometri, dan mekanisme pencatatan yang sebanding. Gunakan batas wilayah bersama atau korespondensi yang dapat diperiksa, tangani duplikasi serta perubahan kategori, dan bedakan waktu perekaman dari waktu kejadian. Kekosongan historis tidak diisi dengan nol atau inventaris masa kini.

Perubahan fungsi dan residual dihitung hanya untuk pasangan periode yang lolos audit. Pembanding fungsi–ukuran yang tetap digunakan untuk membaca perubahan terhadap acuan yang sama; tolok ukur per tahun, bila digunakan, diberi interpretasi posisi relatif pada masing-masing tahun. Keduanya tidak dicampur. Estimasi panel hanya dipilih jika jumlah pusat, periode, serta kesebandingan mendukungnya; rancangan tidak bergantung pada panel lengkap.

Perubahan ketercakupan peta diperiksa melalui jejak penyuntingan, sumber pembanding, dan sampel terarah. Jika perubahan fenomena tidak dapat dipisahkan dari perubahan pencatatan, hasil temporal pada indikator itu tidak disimpulkan; analisis periode yang valid tetap dapat digunakan. Perbandingan sumber yang mengubah konstruk dilaporkan sebagai triangulasi atau perubahan objek estimasi, bukan sensitivitas yang ekuivalen.

### 3.6.11 Validitas, reliabilitas, dan reproduktibilitas

**Validitas konstruk** dijaga dengan memisahkan ukuran lokal, hubungan relasional, aksesibilitas potensial, fungsi, kinerja, manfaat, dan beban. Titik minat, waktu tempuh, atau jumlah fasilitas tidak langsung diperlakukan sebagai produktivitas, integrasi aktual, atau kematangan ekonomi.

**Validitas analitis dan reliabilitas hasil** dijaga melalui aturan transformasi yang terdokumentasi, tolok ukur yang ditetapkan sebelum klasifikasi, pemeriksaan duplikasi indikator, pengeluaran satu indikator secara bergiliran, serta variasi bobot, ambang, unit, dan status bukti. Penghitungan dengan konfigurasi masukan serta parameter yang sama harus menghasilkan keluaran yang sama. Ketidaksesuaian antarsumber dilaporkan dan tidak diselesaikan dengan memilih sumber yang menghasilkan klasifikasi yang diinginkan.

**Validitas eksternal** dibatasi pada unit, tahun, dan kawasan yang benar-benar tercakup. Hasil kabupaten/kota tidak digeneralisasikan ke kecamatan; hasil pemeriksaan pada pusat terpilih tidak digeneralisasikan ke seluruh kawasan; dan pola dalam sistem Jakarta tidak otomatis berlaku untuk metropolitan lain.

Paket reproduksi minimal memuat:

1. kamus data, log akses, dan registri asal-usul data;
2. geometri serta tabel korespondensi versi analisis;
3. skrip atau langkah transformasi dan analisis;
4. nilai garis dasar dan parameter skenario;
5. tabel indikator, bobot, ambang, dan versi model;
6. daftar data yang dikeluarkan beserta alasannya; dan
7. manifest keluaran, sumber, dan syarat reproduksi atau penyebarluasan.

### 3.6.12 Aturan keputusan, keluaran, dan batas klaim

Setiap sumber terbuka diproses melalui pemeriksaan isi, metadata, unit, tahun, definisi, cakupan, serta cara pembentukan. Indikator dibentuk melalui observasi atau estimasi dengan asumsi yang terdokumentasi. Konfigurasi yang lolos pemeriksaan dibekukan sebelum analisis; perubahan sumber atau model disimpan sebagai versi baru.

Mutu dinilai melalui kemampuan menjawab konstruk, pemeriksaan independen, kesebandingan, dan ketidakpastian. Data resmi agregat dan proksi rinci sama-sama diperiksa; akses kelembagaan tidak menjadi syarat kelayakan. Jika suatu modul gagal, perbaiki konstruksi, ganti sumber terbuka yang sesuai, atau laporkan batasnya tanpa mengubah nilai hilang menjadi nol.

Keluaran utama penelitian adalah tabel audit dan manifest mutu bukti; peta serta profil hubungan metropolitan atau aksesibilitas; peta fungsi aktual dan fungsi relatif; profil manfaat serta beban; gradien atau tipologi *status quo*; tabel dan peta sensitivitas; serta penjelajah WebGL garis dasar-skenario-selisih-ketahanan. Hasil juga dilaporkan menurut lapisan administrasi untuk membantu interpretasi tanggung jawab tanpa mengubah batas kewenangan.

Dengan rancangan ini, penelitian dapat menyatakan pola hubungan atau aksesibilitas, fungsi lokal yang diukur atau diestimasi, perubahan pada seri yang sebanding, surplus atau defisit relatif pada konstruk yang diukur, tipologi deskriptif, gradien, dan stabilitas hasil terhadap asumsi yang diuji. Penelitian tidak dapat menyatakan bahwa Jakarta secara kausal menyebabkan ketergantungan, bahwa satu radius merupakan batas metropolitan yang benar, bahwa pusat sekunder pasti mengalami *upgrading*, atau bahwa perubahan nilai dalam WebGL memprediksi dampak kebijakan masa depan.

Klaim *borrowed size* dan *agglomeration shadow* digunakan secara ketat hanya setelah empat gerbang bukti terpenuhi. Jika tidak, hasil ditulis sebagai pola yang “konsisten dengan” atau “tidak konsisten dengan” konstruk tersebut pada unit, periode, dan konfigurasi bukti yang disebutkan.
