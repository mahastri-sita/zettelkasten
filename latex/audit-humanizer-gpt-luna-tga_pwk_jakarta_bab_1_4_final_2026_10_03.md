# Audit bahasa dan humanizer

## GPT Luna

**Berkas yang diaudit:** `latex/tga_pwk_jakarta_bab_1_4_final.tex`  
**Tanggal audit:** 3 Oktober 2026  
**Mode:** audit editorial, tanpa mengubah berkas `.tex`  
**Cakupan:** kesan bahasa Inggris yang diterjemahkan ke bahasa Indonesia, pola humanizer, keluwesan kalimat akademik, dan beberapa catatan EYD yang langsung berkaitan dengan temuan tersebut.

## Putusan singkat

Naskah ini **tidak secara keseluruhan terasa seperti terjemahan mesin dari bahasa Inggris**. Banyak bagian, terutama uraian angka dan konteks pada Bab 4, sudah jelas, spesifik, dan terdengar seperti tulisan akademik Indonesia. Naskah juga memuat detail yang sulit disebut generik: nama kecamatan, angka, sumber, batas unit, pengecualian Kota Bekasi, perbedaan periode, serta batas inferensi.

Namun, kesan alih bahasa muncul cukup kuat pada bagian tertentu, terutama Bab 2 dan Bab 3. Sumber masalahnya bukan terutama istilah Inggris, melainkan:

1. padanan kata yang terlalu harfiah, seperti `fungsi keputusan`, `ditahan`, `menjadi sensitivitas`, dan `beban diambil dari`;
2. rangkaian kata benda abstrak yang menggantikan tindakan penelitian;
3. metafora prosedural yang dipakai terlalu sering, seperti `gerbang bukti`, `cadangan bernama`, `spesifikasi kembar`, `konfigurasi bukti`, dan `rantai penelitian`;
4. pengulangan kata kerja analitis `dibaca` untuk berbagai tindakan yang sebenarnya berbeda;
5. pengulangan batas klaim dalam bentuk yang sangat terstruktur sehingga sebagian paragraf terasa seperti dokumentasi sistem, bukan prosa skripsi.

Temuan ini adalah **penilaian terhadap kesan bahasa**, bukan bukti bahwa naskah diterjemahkan dari bahasa Inggris dan bukan bukti tentang penggunaan AI. Bahasa akademik yang padat, istilah teknis, dan kalimat pasif dalam metode tidak otomatis merupakan tanda AI.

### Peta per bab

- **Bab 1:** sedang. Gagasan utama cukup jelas, tetapi kontribusi dan batasan penelitian beberapa kali dipadatkan menjadi `konfigurasi`, `perangkaian`, `spesifikasi`, dan `gerbang`.
- **Bab 2:** paling terasa seperti alih bahasa pada bagian konsep. Kolokasi `penduduk besar`, `fungsi keputusan`, `ditahan`, `korban shadow`, dan `diadaptasi secara terbuka` perlu diprioritaskan.
- **Bab 3:** paling kuat menunjukkan pola humanizer. Banyak istilah prosedural, kalimat pasif, dan kata kerja `dibaca`, `dibekukan`, `diterapkan`, serta `dipakai` membuatnya menyerupai dokumentasi protokol.
- **Bab 4:** relatif luwes dan konkret. Perbaikan terutama menyangkut `locator`, perbandingan rasio, `jalur produksi yang diuji`, dan predikat yang hilang pada daftar pusat berbasis massa.

## Ringkasan hasil humanizer

| Pola | Tingkat perhatian | Temuan | Tindakan |
|---|---|---|---|
| Padanan atau kolokasi harfiah | Tinggi | Beberapa pasangan kata dapat dipahami, tetapi tidak lazim dalam prosa Indonesia. | Ubah pada kemunculan yang memikul argumen utama. |
| Jargon prosedural buatan naskah | Tinggi | Istilah internal terlalu sering muncul dalam kalimat biasa. | Definisikan sekali, lalu gunakan padanan tindakan dalam prosa. |
| Penumpukan nomina abstrak | Tinggi di Bab 1-3 | `konfigurasi`, `perangkaian`, `ketahanan`, `pembentukan`, dan `pengukuran` bertumpuk sebelum objek terlihat. | Kembalikan subjek, kata kerja, dan objek konkret. |
| Metafora `dibaca` | Sedang | Pencarian teks menemukan 33 kemunculan `dibaca`, termasuk tabel dan keterangan. | Ganti secara selektif dengan `dianalisis`, `ditafsirkan`, `digunakan`, atau `ditampilkan`. |
| `berbasis` | Rendah sampai sedang | Muncul 11 kali. Sebagian merupakan nama konstruk yang sah, seperti `pusat sekunder berbasis massa`. | Pertahankan sebagai label; gunakan `berdasarkan` dalam prosa jika tidak mengubah makna. |
| `gerbang bukti` | Sedang sampai tinggi | Muncul 10 kali dan menjadi metafora utama aturan klasifikasi. | Pada prosa, utamakan `syarat penggunaan label` atau `syarat bukti`. |
| `cadangan bernama` | Sedang sampai tinggi | Muncul 7 kali. Dapat terdengar seperti terjemahan `named fallback`. | Gunakan `rancangan alternatif berkode` atau `alternatif yang telah ditetapkan`. |
| `konfigurasi` | Sedang | Muncul 9 kali dengan beberapa arti yang berbeda. | Bedakan `susunan sumber dan metode`, `spesifikasi`, dan `hasil`. |
| `dibekukan` | Sedang | Muncul 8 kali dalam konteks ambang, garis dasar, dan konfigurasi bukti. | Gunakan `ditetapkan sebelum analisis` bila pembekuan bukan istilah metodologis yang sengaja dipertahankan. |
| `belum terselesaikan` | Sedang | Muncul 6 kali sebagai nama kategori hasil. | Jika bukan nama kategori, gunakan `belum dapat disimpulkan` atau `belum stabil`. |
| Kosakata AI/promosi | Rendah | Tidak tampak klaster `menyoroti`, `lanskap`, `krusial`, `vital`, `signifikan`, atau bahasa promosi sejenis. | Tidak perlu pembersihan massal. |
| Negasi paralel | Rendah | Konstruksi `bukan ... melainkan ...` hanya tampak pada beberapa lokasi dan umumnya logis. | Pertahankan ketika membatasi klaim; jangan menambah pola serupa. |
| Suara pasif | Rendah sampai sedang | Wajar dalam metode, tetapi beberapa kalimat menyembunyikan tindakan yang dilakukan. | Aktifkan kalimat bila pelaku atau tindakan perlu dibuat jelas. |
| Tanda pisah em/en | Rendah | Tidak ditemukan karakter Unicode em dash atau en dash. `--` di LaTeX terutama dipakai untuk rentang angka atau tanda baca LaTeX. | Tidak ada tindakan khusus. |

## Lokasi yang paling terasa seperti alih bahasa

### 1. Padanan harfiah dan kolokasi yang kurang alami

| Lokasi | Cuplikan | Masalah | Usulan penyuntingan |
|---|---|---|---|
| L84 | `Objek yang diestimasi adalah kemiringan hubungan ...` | Struktur nominal membuat tindakan penelitian kurang langsung. | `Penelitian ini mengestimasi kemiringan hubungan antara integrasi metropolitan dan fungsi lokal setelah memperhitungkan massa serta karakteristik lokal.` |
| L155 | `dapat membuka arah perlakuan yang lebih baik` | `Arah perlakuan` terdengar seperti padanan harfiah dan tidak menyebut tindakan perencanaan. | `dapat membantu menentukan penanganan kawasan hunian berpenduduk besar yang layanannya tertinggal dari permintaan lokal` |
| L169 | `mempunyai penduduk besar ... arus keluar yang kuat` | Besaran penduduk dan arus lebih alami jika disebut sebagai jumlah atau volume. | `memiliki jumlah penduduk yang besar ... dan arus komuter keluar yang besar` |
| L173 | `manfaat dan biaya bergerak bersama dengan cara yang berbeda` | Hubungan perubahan tidak jelas. | `manfaat dan biaya tidak selalu berubah searah` |
| L173 | `berbagi, mencocokkan, dan belajar ... memperoleh pembelajaran` | `Mencocokkan` dan `memperoleh pembelajaran` terasa sebagai terjemahan kata demi kata. | `berbagi, mencocokkan kebutuhan, dan belajar dari interaksi yang berulang` atau `berbagi, pencocokan, dan pembelajaran` |
| L181 | `terbatas pada fungsi keputusan` | `Fungsi keputusan` terlalu padat. | `terbatas pada fungsi pengambilan keputusan` |
| L187 | `berpenduduk besar tetapi berfungsi sedikit` | `Berfungsi sedikit` tidak lazim untuk wilayah. | `memiliki jumlah penduduk besar tetapi fungsi lokal yang terbatas` |
| L187 | `kandidat korban shadow` | Konsep `shadow` diperlakukan seperti pelaku yang menghasilkan korban. | `kasus yang perlu diperiksa sebagai kemungkinan agglomeration shadow` |
| L199 | `arah perubahan harus dipisahkan dari keberadaan infrastruktur` | Maksudnya adalah membedakan efek atau perubahan yang diamati dari sekadar keberadaan jaringan. | `perubahan yang diamati perlu dibedakan dari sekadar keberadaan infrastruktur` |
| L211 | `Residu bukan bukti sebab` | `Bukti sebab` terlalu terpotong. | `Residu bukan bukti hubungan sebab akibat` |
| L217 | `manfaat dapat ditahan dan diubah menjadi fungsi lokal` | `Ditahan` membuat manfaat seolah-olah benda fisik. | `pusat sekunder dapat mempertahankan manfaat akses dan mengubahnya menjadi fungsi lokal` |
| L225 | `kawasan hunian yang tertekan shadow` | Bentuknya harfiah dan terlalu dekat dengan bahasa sebab akibat. | `kawasan hunian yang diduga mengalami agglomeration shadow` |
| L227 | `Bukti empiris memperlihatkan tanda yang berbeda` | `Tanda` tidak langsung menyebut arah hubungan. | `Temuan empiris menunjukkan arah hubungan yang berbeda` |
| L239 | `diadaptasi secara terbuka terhadap data Indonesia` | `Secara terbuka` tidak menjelaskan tindakan transparansi yang dimaksud. | `penyesuaian definisi dan unit dengan data Indonesia perlu dijelaskan` |
| L253 dan L316 | `fungsi keputusan` | Istilah yang sama berulang dalam pembahasan teori. | `fungsi pengambilan keputusan` |
| L271 | `meneruskan estafet tersebut` | Metafora ini terdengar retoris dan kurang perlu dalam kajian pustaka. | `Penelitian ini melanjutkan kajian tersebut dengan tiga langkah` |
| L271 | `perangkaian ketiga langkah tersebut` | `Perangkaian` memberi kesan proses mekanis. | `penggabungan ketiga langkah tersebut` |
| L271 dan L352 | `hasil yang belum terselesaikan` | Jika bukan nama kategori formal, hasil tidak benar-benar "terselesaikan". | `pola yang belum dapat disimpulkan` atau `hasil yang belum stabil` |
| L318 | `menanggung beban perjalanan` | Masih dapat diterima, tetapi perlu dibedakan dari `menanggung waktu`. | Pertahankan untuk biaya atau beban; gunakan `menghabiskan waktu perjalanan` bila waktu juga disebut. |
| L409 | `Beban diambil dari waktu tempuh jaringan` | `Diambil dari` terdengar seperti padanan `taken from`, bukan penjelasan pengukuran. | `Beban diukur berdasarkan waktu tempuh jaringan, durasi, atau biaya perjalanan` |
| L1301 | `peluang yang secara potensial terjangkau` | `Peluang` dan `potensial` mengulang arti. | `peluang yang secara teoritis dapat dijangkau` |
| L1308-L1309 | `menjadi sensitivitas` dan `dipakai sebagai pemeriksa moda` | Objek pengukuran seolah berubah menjadi metode atau pelaku pemeriksaan. | `Uji sensitivitas menggunakan waktu tempuh ke kecamatan DKI terdekat. Waktu tempuh terjadwal GTFS TransJakarta digunakan sebagai pembanding untuk moda angkutan umum.` |
| L1332-L1333 | `tidak disimpulkan dari tanda mentah` | `Tanda mentah` terlalu ringkas bagi pembaca yang belum akrab dengan polaritas. | `Polaritas ditentukan berdasarkan konstruk yang diukur, bukan hanya berdasarkan nilai mentah positif atau negatif.` |
| L1735 | `memiliki rumah sakit per penduduk setara dengan kota` | Kata `jumlah` atau `rasio` hilang. | `memiliki rasio jumlah rumah sakit terhadap penduduk yang setara dengan rasio di wilayah kota` |
| L1848 | `kawasan industri diperlakukan sebagai jalur produksi yang diuji` | `Jalur produksi` dapat berarti mekanisme, kelompok, atau moderator. | `kawasan industri diperlakukan sebagai jalur produksi yang dianalisis sebagai penjelasan alternatif` |
| L1859 | `7 hanya ambang penduduk` dan `7 hanya ambang volume hunian` | Predikat `melampaui` hilang dari daftar. | `7 hanya melampaui ambang penduduk` dan `7 hanya melampaui ambang volume hunian` |

### 2. Jargon prosedural yang mengambil alih prosa

Istilah berikut dapat dipertahankan sebagai nama komponen pada tabel, diagram, atau manifest. Masalah muncul ketika istilah itu menjadi predikat utama dalam paragraf dan pembaca harus mengingat metaforanya sebelum memahami tindakan penelitian.

| Istilah | Lokasi penting | Bentuk yang lebih langsung |
|---|---|---|
| `gerbang bukti` | L139, L400-L411, L617, L1335-L1432, L1629 | `syarat penggunaan label`, `syarat bukti`, atau `aturan klasifikasi` |
| `cadangan bernama` | L536, L572-L578, L617, L1616-L1619, L1915 | `rancangan alternatif berkode` atau `alternatif yang hanya digunakan jika syaratnya terpenuhi` |
| `spesifikasi kembar` | L120, L548, L880, L1174-L1194 | `spesifikasi pembanding berorientasi DKI` |
| `konfigurasi hasil` | L95, L109, L490 | `pola hasil` atau `kombinasi hasil` |
| `konfigurasi bukti` | L645, L799, L959, L1616, L1631 | `susunan sumber dan metode` atau `spesifikasi dengan sumber tertentu` |
| `rantai inti penelitian` | L538, L572, L584 | `spesifikasi utama penelitian` |
| `garis dasar dibekukan` | L533-L534, L641, L1116 | `garis dasar ditetapkan sebelum klasifikasi` |
| `skenario bukti` | L644-L648, L1485-L1491 | `perubahan akibat sumber atau mutu data` |
| `skenario parameter` | L645-L648, L1512-L1514 | `perubahan bobot, ambang, atau spesifikasi` |
| `tingkat klaim` | L617 | `kekuatan klaim` atau `tingkat inferensi` |
| `membaca posisi` | L134, L1258-L1259 | `menentukan posisi relatif` atau `menafsirkan posisi relatif` |
| `dibaca sebagai profil` | L1150, L1384-L1387 | `dianalisis secara deskriptif, bukan melalui regresi` |

**Catatan:** jangan melakukan penggantian global. `Gerbang bukti`, misalnya, dapat berguna jika sudah diperkenalkan sebagai nama ringkas. Yang perlu dikurangi adalah pemakaian metafora tersebut ketika kalimat dapat langsung menyebut syarat atau tindakan.

### 3. Penumpukan abstraksi dan pengulangan batas klaim

Bab 1-3 sangat berhati-hati dalam membatasi inferensi. Itu merupakan kekuatan substantif, tetapi bentuk bahasanya berulang. Pembaca beberapa kali diberi tahu bahwa sesuatu bukan kausal, bukan produktivitas, bukan jumlah pekerjaan, bukan integrasi aktual, bukan bukti `shadow`, dan bukan prediksi kebijakan.

Batas tersebut perlu dipertahankan, tetapi sebaiknya dikelompokkan:

- jelaskan batas konstruk sekali pada Bab 2;
- jelaskan aturan pengukuran pada Bab 3;
- pada Bab 1 cukup pertahankan batas yang diperlukan untuk memahami pertanyaan penelitian;
- pada Bab 4 cukup pertahankan batas yang mencegah pembaca menganggap data deskriptif sebagai hasil diagnosis.

Lokasi yang dapat diringkas:

- L84, L95, L109: `konfigurasi` dan `hasil yang belum terselesaikan` muncul sebelum tipologi dijelaskan;
- L130 dan L139: batas penggunaan label dijelaskan berulang dalam latar belakang dan keterangan gambar;
- L211, L219, L225, L227: batas residu, layanan, dan `shadow` kembali dijelaskan dalam beberapa paragraf berdekatan;
- L348, L352, L375: model, residu, gerbang, dan tipologi dijelaskan lagi dengan pola yang hampir sama;
- L438, L494-L498, L1621-L1631: keterbatasan kausal dinyatakan kembali dalam prosa metode dan aturan keputusan.

Masalah ini bukan kesalahan logika. Ini terutama masalah ritme. Ketika setiap paragraf mengantisipasi semua kemungkinan salah tafsir, suara penulis menjadi seperti dokumentasi protokol otomatis.

## Audit pola humanizer

### Pola yang benar-benar tampak

1. **Bahasa prosedur yang terlalu sering.** `Dibekukan`, `ditetapkan`, `dilaporkan`, `dibaca`, `diperiksa`, dan `dipakai` sering hadir dalam satu rangkaian. Sebagian wajar dalam metode, tetapi beberapa kalimat kehilangan pelaku dan tujuan.
2. **Metafora yang diperlakukan sebagai tindakan.** `Gerbang`, `rantai`, `cadangan`, `jalur`, `lapisan`, dan `membaca` membuat metode terdengar seperti sistem perangkat lunak.
3. **Nominalisasi bertingkat.** Contoh paling jelas ialah `perangkaian pengukuran relasi`, `ketahanan hasil terhadap keputusan analitis`, `pembentukan ekspektasi`, dan `konfigurasi bukti yang lolos audit`.
4. **Daftar tiga atau lebih unsur yang berulang.** `arah, intensitas, dan asimetri`, `peluang, beban, dan ketergantungan`, serta `unit, periode, dan konstruk` memang sah secara metodologis, tetapi pengulangannya di setiap bab memberi ritme yang sangat teratur.
5. **Subjek yang hilang pada kalimat pasif.** Pada metode, bentuk pasif sering tepat. Namun, kalimat seperti `Waktu tempuh ... menjadi sensitivitas` dan `beban diambil dari ...` membutuhkan predikat aktif yang menyebut uji atau pengukuran.

### Pola yang tidak dominan dan tidak perlu dibersihkan secara paksa

- Tidak ada bahasa promosi seperti `vibran`, `luar biasa`, `menakjubkan`, atau klaim pentingnya penelitian yang berlebihan.
- Tidak ada pembukaan formulaik seperti `Di era globalisasi` atau `Seiring perkembangan zaman`.
- Tidak ada penutup generik seperti `masa depan terlihat cerah`.
- Tidak ada sapaan chatbot, ajakan berkomunikasi, emoji, atau bahasa pelayanan.
- Tidak ada penggunaan Unicode em dash atau en dash.
- Konstruksi `bukan ... melainkan ...` masih terbatas dan beberapa memang penting untuk membatasi klaim.
- Istilah Inggris pada judul artikel, nama API, nama data, dan konsep utama bukan masalah humanizer selama ditulis konsisten dan, jika perlu, dijelaskan pada kemunculan pertama.

### Sinyal manusia yang perlu dipertahankan

- penyebutan kecamatan dan kawasan secara spesifik;
- pengakuan bahwa Kota Bekasi tidak memiliki seri fasilitas yang setara;
- perbedaan definisi komuter 2014, 2019, dan 2023;
- pengakuan bahwa data komuter tidak mengamati perjalanan berobat atau transaksi layanan;
- pembedaan antara proksi stok bangunan dan jumlah pekerjaan;
- penyebutan nilai yang belum tersedia, sumber yang belum diambil, serta lisensi yang belum jelas;
- penolakan untuk menyimpulkan kausalitas dari hubungan observasional.

Detail-detail tersebut membuat naskah terdengar ditulis oleh peneliti yang memahami keterbatasan datanya. Jangan menghapusnya demi membuat prosa lebih pendek.

## Istilah Inggris dan istilah teknis yang sebaiknya diperlakukan berbeda

### Pertahankan

Istilah berikut tidak perlu diterjemahkan secara paksa:

- *borrowed size* dan *agglomeration shadow* sebagai nama konsep;
- *leave-one-out*, *wild cluster bootstrap*, *spline*, *screenline*, *point-in-polygon*, dan *location quotient* jika istilah tersebut memang digunakan dalam metode;
- WSM, GHSL, GTFS, API, OSM, Podes, SIRS, dan PDDikti;
- judul artikel atau laporan berbahasa Inggris pada tabel penelitian terdahulu;
- `residu`, `kemiringan`, `kovariat`, `konstruk`, `domain`, `proksi`, dan `reproduktibilitas`.

Menurut EYD V, istilah atau ungkapan asing yang belum diserap dapat ditulis dengan huruf miring. Penggunaan `\emph{borrowed size}` dan `\emph{agglomeration shadow}` sudah sejalan dengan kebutuhan tersebut. Yang perlu diperbaiki adalah kalimat Indonesia di sekeliling istilah, bukan istilah teknisnya.

### Jelaskan atau ganti pada prosa

| Istilah | Saran |
|---|---|
| `locator` | `nomor halaman, tabel, atau lampiran` pada L835 dan L1637. |
| `epoch` | Pertahankan dalam nama data, tetapi jelaskan sebagai `periode observasi` pada kemunculan pertama. |
| `grid` | `petak grid` atau `grid kepadatan` sesuai konteks pada L1645. |
| `screenline` | `garis penampang lalu lintas (screenline)` pada kemunculan pertama. |
| `what-if` | `eksplorasi skenario bersyarat` atau `eksplorasi what-if` setelah definisi singkat. |
| `status quo` | `kondisi awal` dalam prosa; pertahankan istilah asing hanya jika menjadi nama modul. |
| `contested` | `campuran` sudah cukup, kecuali ada alasan teori untuk mempertahankan istilah Inggris. |
| `masker` | `penyaringan poligon` atau `masking berbasis poligon`, karena `masker` dapat terdengar seperti benda, bukan operasi spasial. |
| `spesifikasi kembar` | Ganti dengan deskripsi fungsi spesifikasi, bukan metafora hubungan keluarga. |

## Contoh audit humanizer: draf, pemeriksaan, dan versi akhir

Bagian ini bukan rewrite seluruh naskah. Ini contoh cara menerapkan humanizer pada tiga lokasi yang paling representatif.

### Contoh 1: posisi penelitian, L84

**Draf penyuntingan pertama:**

> Penelitian ini tidak menetapkan *borrowed size* atau *agglomeration shadow* sebagai jawaban awal. Penelitian ini mengestimasi hubungan antara integrasi metropolitan dan fungsi lokal setelah massa serta karakteristik lokal diperhitungkan. Layanan orde tinggi dan stok bangunan nonhunian dianalisis secara terpisah agar surplus pada satu domain tidak menutupi defisit pada domain lain.

**Apa yang masih terasa seperti tulisan AI:**

- dua kalimat berturut-turut dimulai dengan `Penelitian ini`;
- hubungan antarkalimat masih sangat rapi dan simetris;
- `jawaban awal` dan `domain` tetap abstrak jika tidak segera dikaitkan dengan tindakan analisis.

**Versi akhir yang lebih luwes:**

> Penelitian ini menguji apakah kecamatan yang lebih terhubung dengan kawasan inti memiliki fungsi lokal yang lebih tinggi atau lebih rendah daripada yang diperkirakan dari jumlah penduduk dan kondisi lokalnya. Layanan orde tinggi dan stok bangunan nonhunian dianalisis secara terpisah. Hasilnya baru ditafsirkan dengan konsep *borrowed size* atau *agglomeration shadow* setelah relasi metropolitan dan penjelasan alternatif diperiksa. Relasi terarah pada tingkat kabupaten/kota digunakan sebagai konteks tambahan.

### Contoh 2: spesifikasi dan alternatif, L572-L576

**Draf penyuntingan pertama:**

> Penelitian menggunakan satu rantai utama. Cadangan bernama hanya digunakan apabila pemicunya terpenuhi. Jika cadangan digunakan, alasan dan perbedaannya dari spesifikasi utama dilaporkan.

**Apa yang masih terasa seperti tulisan AI:**

- `rantai utama` dan `cadangan bernama` masih membawa metafora prosedural;
- tiga kalimat memakai pola syarat yang seragam.

**Versi akhir yang lebih luwes:**

> Penelitian menggunakan satu spesifikasi utama. Rancangan alternatif hanya dipakai jika kondisi yang telah ditetapkan sebelum pengolahan data terpenuhi. Setiap penggunaan alternatif, alasan pemilihannya, dan perbedaannya dari spesifikasi utama dilaporkan.

### Contoh 3: beban dan uji sensitivitas, L1301-L1310

**Draf penyuntingan pertama:**

> Ukuran ini menyatakan peluang yang dapat dijangkau secara potensial. Beban diukur dari waktu tempuh menuju Bundaran Hotel Indonesia. Waktu tempuh ke kecamatan DKI terdekat menjadi sensitivitas, sedangkan GTFS TransJakarta menjadi pemeriksa moda angkutan umum.

**Apa yang masih terasa seperti tulisan AI:**

- `menjadi sensitivitas` dan `menjadi pemeriksa` masih menjadikan indikator sebagai pelaku;
- tiga ukuran waktu tempuh diletakkan berurutan tanpa menjelaskan fungsi masing-masing.

**Versi akhir yang lebih luwes:**

> Ukuran ini menunjukkan peluang yang secara teoritis dapat dijangkau. Beban potensial dihitung dari waktu tempuh menuju Bundaran Hotel Indonesia. Sebagai uji sensitivitas, tujuan tersebut diganti dengan kecamatan DKI terdekat. Waktu tempuh terjadwal dari GTFS TransJakarta digunakan sebagai pembanding untuk angkutan umum.

## Prioritas revisi

### Prioritas 1: wajib diperbaiki sebelum naskah dibaca pembimbing

1. L155: `membuka arah perlakuan`.
2. L173: `bergerak bersama dengan cara yang berbeda`.
3. L181, L253, L316: `fungsi keputusan`.
4. L187, L758: `berfungsi sedikit`.
5. L187, L225, L774: `korban shadow` atau `tertekan shadow`.
6. L211: `bukti sebab`.
7. L217, L316: `manfaat dapat ditahan`.
8. L239: `diadaptasi secara terbuka terhadap data Indonesia`.
9. L409: `beban diambil dari`.
10. L1308-L1309: `menjadi sensitivitas` dan `dipakai sebagai pemeriksa`.
11. L1735: `rumah sakit per penduduk setara dengan kota`.
12. L1859: daftar `7 hanya ambang ...` tanpa predikat.

### Prioritas 2: perbaiki ketika subbab terkait direvisi

1. Jelaskan `gerbang bukti`, `cadangan bernama`, `spesifikasi kembar`, dan `konfigurasi bukti` pada kemunculan pertama.
2. Kurangi `dibaca` dengan memilih kata kerja sesuai tindakan: `dianalisis`, `ditafsirkan`, `digunakan`, `ditampilkan`, atau `dibandingkan`.
3. Ganti `locator` dengan jenis lokasi rujukan yang konkret.
4. Ganti `meneruskan estafet`, `perangkaian`, dan `hasil yang belum terselesaikan` pada kajian pustaka.
5. Ubah pembukaan Bab 2 dan Bab 4 agar langsung masuk ke persoalan, bukan mengumumkan isi bab.
6. Kelompokkan batas klaim yang berulang. Jangan menghapus batas inferensi, tetapi jangan mengulang seluruh daftar larangan di setiap subbab.

### Prioritas 3: pertahankan kecuali ada alasan substantif

- istilah Inggris sebagai nama konsep atau metode;
- kalimat pasif yang memang berfungsi mendahulukan objek pengukuran;
- daftar tiga unsur yang diperlukan untuk mendefinisikan konstruk;
- `berbasis massa` sebagai label operasional pusat sekunder;
- kata `konsisten dengan`, `berkaitan dengan`, `proksi`, dan `asosiasional`, karena kata-kata tersebut menjaga kejujuran inferensi.

## Kesimpulan audit GPT Luna

Naskah ini memiliki dasar bahasa Indonesia akademik yang kuat, tetapi keluwesannya tertutup oleh sistem istilah prosedural yang terlalu rapat. Jika hanya ada waktu untuk satu putaran penyuntingan, jangan menerjemahkan semua istilah Inggris dan jangan mengganti semua kata teknis. Dahulukan pemulihan predikat dan objek pada frasa yang terasa harfiah, lalu sederhanakan nama-nama prosedur dalam prosa.

Urutan yang paling aman adalah:

1. perbaiki kolokasi pada daftar Prioritas 1;
2. definisikan nama internal sekali dan gunakan bentuk deskriptif sesudahnya;
3. ubah kalimat Bab 3 menjadi uraian tindakan: siapa melakukan apa, pada data apa, dengan tujuan apa;
4. ringkas pengulangan batas klaim tanpa mengurangi batas inferensi;
5. lakukan pembacaan keras untuk mengecek apakah pembaca dapat menyebut objek dan tindakan setiap kalimat tanpa menerjemahkan ulang istilahnya.

**Penilaian akhir GPT Luna:** kesan English-to-Indonesian translation berada pada tingkat **sedang dan terkonsentrasi**, sedangkan risiko pola humanizer berada pada tingkat **sedang terutama karena jargon prosedural, nominalisasi, dan pengulangan arsitektur kalimat**. Bab 4 memerlukan penyuntingan ringan; Bab 2 dan Bab 3 memerlukan penyuntingan bahasa yang lebih terarah.

Audit ini adalah keluaran editorial **GPT Luna**. Berkas sumber `.tex` tidak diubah.
