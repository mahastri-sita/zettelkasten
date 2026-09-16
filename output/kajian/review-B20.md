# Review B20

**Identitas sumber**

- Kode: B20.
- Judul: *Grid and shake: spatial aggregation and the robustness of regionally estimated elasticities*.
- Penulis: Gábor Békés dan Péter Harasztosi.
- Jenis yang tercantum dalam TXT: `ORIGINAL PAPER`. Status peer-review tidak diverifikasi secara terpisah.
- Jurnal: *The Annals of Regional Science* atau singkatan yang tercetak, *Ann Reg Sci*, volume 60, halaman 143-170, tahun 2018. Nomor isu tidak disebutkan dalam file TXT.
- DOI: `10.1007/s00168-017-0849-y`; URL yang tercantum: `https://doi.org/10.1007/s00168-017-0849-y`.
- Riwayat naskah: diterima 29 Juli 2016, diterima untuk publikasi 26 September 2017, dan dipublikasikan secara daring 7 Oktober 2017.
- Klasifikasi JEL: R12, R30, C15.
- Afiliasi yang tercantum: Institute of Economics of CERS-HAS and CEPR, Central European University, Budapest, untuk Békés; dan Joint Research Centre, Ispra, Italy, untuk Harasztosi.
- Bahan yang ditinjau adalah file `/Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/source/journal/B20-bekes-harastosi-2018-grid-and-shake-spatial-aggregation-and-the-robustness-of-regionally-estimated-elasticities-10.1007-s00168-017-0849-y.txt`. Metadata TXT menyatakan sumber PDF terdiri atas 28 halaman dan teks diekstraksi dengan `pdftotext -layout` pada 31 Agustus 2026.

## Summarized Abstract

**Laporan sumber.** Artikel mengusulkan metode yang sederhana dan transparan untuk mengukur robustnes spasial koefisien yang diestimasi secara regional. Fokusnya adalah peran distrik administratif dan ukuran wilayah, terutama ketika variabel dibandingkan pada unit spasial yang telah diagregasi. Penulis menyatakan bahwa prosedur tersebut memperbaiki metode yang ada, khususnya ketika unit spasial bersifat heterogen. Ilustrasi empiris menggunakan data Hungaria untuk membandingkan estimasi eksternalitas aglomerasi pada beberapa tingkat agregasi. Kesimpulan abstraknya adalah bahwa cara agregasi spasial tampak sama pentingnya dengan spesifikasi model ekonometrik (TXT, hlm. 143, abstrak, baris 50-60).

**Interpretasi penulis.** Kontribusi utama yang diklaim bukan estimator baru untuk elastisitas aglomerasi, melainkan prosedur untuk menghasilkan distribusi koefisien dari berbagai realisasi unit spasial buatan. Distribusi tersebut memungkinkan perbandingan antara unit administratif, unit buatan dengan ukuran serupa, dan ukuran grid yang berbeda (TXT, hlm. 143-145, baris 93-146 dan 158-163).

**Inferensi review.** Abstrak mendukung pembacaan bahwa objek utama artikel adalah sensitivitas hasil terhadap pilihan unit spasial. Ia tidak dengan sendirinya membuktikan besar atau arah kausal eksternalitas aglomerasi; angka elastisitas tetap bergantung pada data Hungaria, model yang dipakai, dan aturan pembentukan grid yang dijelaskan dalam artikel.

## Problem Statement

**Laporan sumber.** Penulis memulai dari masalah bahwa studi regional sering memilih kota, kabupaten, atau wilayah secara arbitrer. Estimasi kemudian dapat berubah karena karakteristik unit spasial, ukuran wilayah, letak batas administratif, serta jarak tempat berlangsungnya eksternalitas. Ketidakcocokan antara unit observasi dan jangkauan spasial fenomena dapat menghasilkan kesalahan pengukuran spasial dan korelasi spasial pada galat di lokasi yang berdekatan (TXT, hlm. 144-147, baris 88-121 dan 224-248).

Penulis juga menekankan bahwa ukuran unit tidak hanya tidak seragam, tetapi distribusinya tidak acak. Unit kecil atau besar dapat mengelompok karena geografi fisik, sejarah, urbanisasi, pertanian, akses pasar, dan institusi. Karena faktor-faktor tersebut juga berhubungan dengan kepadatan, upah, atau produktivitas, hasil estimasi dapat mencerminkan pola spasial unit administratif, bukan hanya hubungan substantif yang hendak diukur (TXT, hlm. 147-148, baris 255-312).

Batas administratif memiliki persoalan tambahan karena dapat menampung kebijakan pasar kerja, pajak, subsidi, dan regulasi. Karena itu, perbedaan antara estimasi pada wilayah administratif dan wilayah buatan dengan ukuran rata-rata yang sama dapat digunakan untuk memeriksa apakah batas administratif berkaitan dengan hasil estimasi (TXT, hlm. 148-149, baris 315-348).

**Interpretasi penulis.** Masalah tersebut dirumuskan sebagai kebutuhan untuk membandingkan estimasi antarunit spasial secara statistik, bukan sekadar menjalankan satu uji robustnes dengan unit alternatif. Prosedur yang dibutuhkan harus dapat diskalakan menurut ukuran unit, memperhitungkan pengelompokan unit kecil dan besar, membandingkan unit administratif dengan unit buatan, serta menghasilkan dasar untuk menguji signifikansi perbedaan elastisitas (TXT, hlm. 146-149, baris 249-252, 310-312, 340-364).

**Inferensi review.** Problem statement artikel terutama merupakan problem komparabilitas dan sensitivitas pengukuran. Ia belum sama dengan problem identifikasi kausal. OLS dan Poisson dalam artikel digunakan untuk melihat bagaimana koefisien berubah ketika unit spasial diubah; perubahan tersebut tidak secara otomatis dapat ditafsirkan sebagai perubahan kausal pada eksternalitas atau sebagai efek kebijakan.

## Objectives

**Laporan sumber.** Tujuan yang dinyatakan atau dijalankan dalam artikel meliputi:

- Memperkenalkan prosedur “grid and shake” yang menempatkan grid pada peta, menggeser posisinya secara acak, menggabungkan unit dasar ke dalam kotak, lalu mengulang regresi untuk memperoleh distribusi koefisien (TXT, hlm. 145 dan 149-153, baris 122-146 dan 367-380).
- Menguji bagaimana ukuran unit spasial memengaruhi elastisitas aglomerasi pada beberapa ukuran grid buatan (15 x 15 km, 26 x 26 km, dan 39 x 39 km) (TXT, hlm. 150-152, baris 425-470).
- Membandingkan unit administratif Hungaria, yaitu munisipalitas dan mikro-wilayah, dengan unit buatan yang memiliki ukuran atau jumlah unit yang dapat dibandingkan (TXT, hlm. 145-146 dan 157-163, baris 164-183 dan 751-755).
- Menggunakan dua contoh empiris, yaitu hubungan kepadatan dengan upah dan hubungan kepadatan dengan pembentukan perusahaan baru (TXT, hlm. 153-157, baris 538-547 dan 583-721).
- Menilai apakah perbedaan estimasi antarukuran grid, serta antara unit administratif dan buatan, berbeda secara statistik (TXT, hlm. 151-153 dan 157-161, baris 499-535 dan 806-931).
- Membandingkan prosedur tersebut dengan agregasi berbasis lingkaran, spatial atau distributed lags, dan metode dots-to-boxes Briant et al. (2010) (TXT, hlm. 162-163, baris 934-1020).

**Interpretasi penulis.** Tujuan akhirnya adalah menyediakan cara yang transparan untuk mengevaluasi apakah hasil regional merupakan konsekuensi dari ukuran unit, realisasi batas, atau peran batas administratif, sambil tetap memungkinkan perbandingan lintas dataset dan lintas negara (TXT, hlm. 144-146 dan 163-164, baris 93-98, 175-183, dan 1070-1076).

## Literature Survey

**Laporan sumber.** Literatur yang dipakai penulis berangkat dari ekonomi geografi dan eksternalitas aglomerasi. Artikel merujuk pada Marshall untuk eksternalitas, Ciccone dan Hall untuk hubungan kepadatan dengan produktivitas, Ács dan Armington untuk pembentukan perusahaan, serta Melo et al. untuk meta-analisis estimasi ekonomi aglomerasi. Penulis menyatakan bahwa literatur tersebut umumnya menemukan produktivitas yang lebih tinggi pada wilayah yang lebih padat dan menghubungkannya dengan upah lokal (TXT, hlm. 153-154, baris 583-596; daftar referensi baris 1187-1245).

Argumen tentang skala dan jarak dibangun dengan merujuk pada Fotheringham dan Wong mengenai *modifiable areal unit problem* atau MAUP, Dewhurst dan McCann mengenai ukuran wilayah dan spesialisasi, Burger et al. mengenai tingkat geografis eksternalitas, serta Larsson mengenai peluruhan elastisitas kepadatan-upah menurut resolusi spasial. Penulis juga memberi ilustrasi korelasi kepadatan penduduk dan PDB per kapita di sejumlah negara Eropa: 0,74 pada NUTS1 dan 0,54 pada NUTS3. Data ilustratif itu disebut berasal dari Eurostat, dengan PDB per kapita tahun 2007 dan kepadatan penduduk rata-rata 2006-2008 pada delapan negara (TXT, hlm. 146-147, baris 238-276).

Untuk pendekatan metodologis, artikel membahas regresi spasial dan spatial lag, agregasi berbasis seed dan tetangga oleh Amrhein dan Flowerdew, dots-to-boxes oleh Briant et al., simulasi Menon, agregasi berbasis lingkaran, serta spatial dynamic atau distributed lags. Masing-masing dibahas menurut kemampuan menangani jarak, ukuran unit, bentuk wilayah, pengelompokan unit dasar, dan pengujian perbedaan koefisien (TXT, hlm. 145 dan 162-163, baris 147-157 dan 949-1020).

**Interpretasi penulis.** Penulis menempatkan grid and shake sebagai pelengkap atau alternatif bagi pendekatan tersebut. Klaim pembeda utamanya adalah kemampuan membentuk unit dengan ukuran yang dikendalikan, mengulang realisasi batas, menangani unit dasar yang heterogen dan tidak acak, menghitung semua unit dasar satu kali, serta membangun distribusi untuk inferensi (TXT, hlm. 145, 162-164, baris 158-163 dan 1023-1069).

**Inferensi review.** Survei ini berbentuk tinjauan naratif yang dipilih untuk membangun motivasi metode, bukan tinjauan sistematis. TXT tidak memuat protokol pencarian, kriteria inklusi, basis data pencarian, atau penilaian kualitas korpus literatur. Oleh karena itu, literatur yang disebut dapat dibaca sebagai landasan yang dipilih penulis, bukan sebagai inventaris lengkap penelitian tentang MAUP, agregasi spasial, atau elastisitas aglomerasi.

## Method Used

**Laporan sumber: pembentukan unit spasial.** Penulis mendigitalkan peta Hungaria dengan marker yang disusun seperti raster pada unit dasar munisipalitas. Marker ditempatkan pada jarak sekitar 800 meter; 153.113 marker digunakan untuk wilayah Hungaria seluas 93.030 km2. Marker dicocokkan dengan poligon munisipalitas sehingga dapat menjadi dasar pengelompokan ke unit yang lebih besar. Sistem koordinat yang disebut adalah proyeksi Mercator WGS84 EPSG:41001 (TXT, hlm. 150, baris 391-402 dan catatan kaki 10-11).

Grid persegi berukuran sisi L diletakkan di atas marker. Setiap marker diberi indeks kotak dengan `gx = int(x/L) + 1` dan `gy = int(y/L) + 1`. Jika satu munisipalitas memotong beberapa kotak, munisipalitas dimasukkan ke kotak yang memuat mayoritas markernya, yang dianggap mewakili bagian wilayah terbesar (TXT, hlm. 150, baris 403-418).

Tiga ukuran grid digunakan. Grid 15 x 15 km menghasilkan sekitar 440 unit dan dimaksudkan meniru unit yang seukuran kota besar. Grid 26 x 26 km dipilih untuk mendekati 150 mikro-wilayah, sedangkan grid 39 x 39 km menghasilkan sekitar 75 unit dan dimaksudkan untuk mensimulasikan ukuran rata-rata lima mikro-wilayah terbesar (TXT, hlm. 150-151, baris 425-458; ringkasan area pada Tabel 3, hlm. 164, baris 1083-1094).

Untuk mengurangi efek batas negara yang bergerigi, unit hasil grid yang luasnya kurang dari ambang 10 persen dari luas L x L km digabungkan dengan wilayah tetangga yang dipilih secara acak. Penulis mengakui bahwa persoalan ini lebih penting pada negara kecil, ukuran grid besar, dan garis batas yang tidak horizontal atau vertikal (TXT, hlm. 152, baris 489-496).

**Laporan sumber: pengacakan dan inferensi.** Titik awal grid digeser dengan menambahkan dua angka acak independen, xi dan zeta, yang masing-masing seragam pada interval 0 sampai L. Setiap posisi menghasilkan pengelompokan munisipalitas yang dapat berbeda. Penulis menjelaskan bahwa koefisien regresi dihimpun dari realisasi tersebut untuk membentuk distribusi dan dibandingkan dengan koefisien unit administratif atau distribusi dari ukuran lain (TXT, hlm. 152-153, baris 499-535).

Jumlah replikasi yang muncul secara konsisten dalam uraian metode, gambar, Tabel 1, Tabel 2, dan penjelasan aplikasi adalah 300. Namun, langkah prosedur pada bagian 3.4 menyebut bahwa penggeseran grid diulang “a thousand times”. TXT tidak menjelaskan apakah ini perubahan desain, kesalahan penyalinan, atau langkah berbeda. Review ini mempertahankan kedua informasi tersebut dan menggunakan angka 300 ketika merujuk pada tabel dan hasil utama (TXT, hlm. 145, 152-153, 154-159, baris 141-146, 506-535, 643-651, 699-707, dan 724-735).

Untuk pemeriksaan distribusi yang memasukkan ketidakpastian estimasi, penulis mengambil 50 angka acak dari distribusi normal di sekitar setiap koefisien dan standard error pada masing-masing dari 300 realisasi. Distribusi perluasan tersebut terdiri atas 50 x 300 angka dan dibandingkan dengan distribusi yang terkait dengan batas administratif menggunakan uji Kolmogorov-Smirnov dua sisi (TXT, hlm. 161, baris 896-918; Appendix, Gambar 12, baris 1133-1137).

**Laporan sumber: model empiris.** Model pertama adalah regresi OLS penampang lintang tahun 1999:

`Wage_i = beta_1 DENSITY_i + beta_2 EDUC_i + nu_i`

Wage adalah upah rata-rata pekerja pada unit spasial; DENSITY adalah kepadatan penduduk usia kerja; EDUC adalah proksi pendidikan. Teks menyatakan bahwa seluruh variabel digunakan dalam logaritma. Standard error yang ditampilkan adalah robust. Variabel dan koefisien dihitung ulang pada setiap tingkat agregasi; rata-rata tahun sekolah diagregasi dengan pembobot frekuensi berdasarkan jumlah individu (TXT, hlm. 153-155, baris 597-625 dan Tabel 1 baris 631-651).

Model kedua menggunakan Poisson untuk jumlah perusahaan baru, dengan kepadatan penduduk dan upah sebagai penjelas:

`Pr(y_i = N) = f(lambda_i)`

`lambda_i = beta_1 DENSITY_i + beta_2 Wage_i`

Artikel tidak menjelaskan lebih lanjut dalam TXT bentuk lengkap fungsi link, prosedur penanganan dispersi, atau definisi operasional rinci jumlah perusahaan baru. Tabel 2 menyatakan semua variabel dalam logaritma dan menampilkan robust standard error untuk unit administratif serta rata-rata standard error dan simpangan baku koefisien untuk 300 replikasi grid (TXT, hlm. 155-156, baris 660-721 dan Tabel 2 baris 687-707).

**Inferensi review.** Randomisasi artikel mengubah pembagian ruang dengan mempertahankan data dasar dan model regresi. Dengan demikian, distribusi koefisien terutama menggambarkan sensitivitas terhadap realisasi agregasi yang dihasilkan oleh aturan grid, bukan ketidakpastian sampling baru atas perusahaan atau munisipalitas. Kesimpulan robustnes karenanya bersyarat pada proyeksi, kerapatan marker, ukuran grid, ambang koreksi batas, jumlah replikasi, dan spesifikasi model yang dipilih.

## Dataset

**Laporan sumber.** Data utama berasal dari data neraca perusahaan tingkat perusahaan milik Central Statistical Office Hungaria. Cakupannya adalah perusahaan manufaktur dengan pembukuan ganda dan sedikitnya lima karyawan. Informasi tahun 1999 digunakan untuk penampang lintang OLS, sedangkan informasi tahun 1998 juga tersedia untuk membentuk variabel pembentukan perusahaan baru. Data keuangan perusahaan dicocokkan dengan lokasi pada tingkat munisipalitas, kemudian dipasangkan dengan informasi ukuran dan penduduk munisipalitas dari basis data T-STAR (TXT, hlm. 153, baris 550-558).

Upah dihitung dari total biaya upah dan informasi pekerja penuh waktu. Proksi modal manusia berasal dari Hungarian Labor Force Survey, yang memuat sampel pekerja sektor manufaktur dan tingkat pendidikan tertinggi. Data survei dapat dihubungkan ke munisipalitas, tetapi pemberi kerja aktual tidak diidentifikasi, sehingga informasi pekerja tidak dapat dihubungkan langsung ke data perusahaan. Rata-rata tahun sekolah pada tingkat munisipalitas digunakan sebagai proksi kualitas tenaga kerja dan disebut bervariasi antara 7 dan 14 tahun (TXT, hlm. 153-154, baris 559-580).

Unit spasial dasar terdiri atas 3.125 munisipalitas. Struktur administratif yang disebut juga mencakup 150 mikro-wilayah atau kistérség, 20 wilayah NUTS3, dan tujuh wilayah NUTS2. Untuk analisis, grid buatan memiliki sekitar 440 unit pada ukuran 15 km, 150 unit pada ukuran 26 km, dan 75 unit pada ukuran 39 km. Angka luas minimum, rata-rata, dan maksimum tiap jenis unit dirangkum pada Tabel 3; angka untuk grid adalah rata-rata 300 replikasi (TXT, hlm. 145 dan 164, baris 164-173 dan 1083-1094).

Artikel juga menyebut data Eurostat untuk ilustrasi hubungan kepadatan dan PDB per kapita pada delapan negara Eropa. Data tersebut berfungsi sebagai motivasi mengenai perbedaan korelasi menurut NUTS1 dan NUTS3, bukan sebagai dataset utama untuk estimasi grid and shake dalam dua aplikasi Hungaria (TXT, hlm. 146-147, baris 238-270).

**Informasi yang tidak tersedia.** TXT tidak menyebut jumlah perusahaan yang masuk sebelum agregasi, ukuran sampel numerik Hungarian Labor Force Survey, skema sampling survei secara rinci, nama berkas data mentah, atau tautan akses data. TXT juga tidak memberi definisi lengkap pembentukan perusahaan baru selain keterkaitannya dengan informasi tahun 1998 dan 1999.

## Population / Sample

**Laporan sumber.** Populasi empiris yang didefinisikan penulis adalah perusahaan manufaktur di Hungaria yang melakukan pembukuan ganda dan mempunyai sedikitnya lima karyawan. Namun, unit observasi regresi bukan lagi perusahaan individual, melainkan unit spasial yang berisi informasi perusahaan, penduduk, luas wilayah, upah, dan pendidikan setelah agregasi (TXT, hlm. 153-155, baris 552-568 dan 597-606).

Tabel 1 dan Tabel 2 melaporkan 2.872 observasi pada tingkat munisipalitas, 149 pada tingkat mikro-wilayah, 437 pada grid 15 km, 150 pada grid 26 km, dan 73 pada grid 39 km. Jumlah unit administratif awal yang disebut adalah 3.125 munisipalitas dan 150 mikro-wilayah. Penulis menjelaskan bahwa sebagian munisipalitas tidak memiliki aktivitas manufaktur yang dapat diidentifikasi, sehingga tidak semuanya masuk dalam regresi (TXT, hlm. 155-156, Tabel 1 dan Tabel 2, baris 631-651 dan 687-707).

Terdapat perbedaan internal pada jumlah observasi munisipalitas. Tabel 1 dan Tabel 2 menulis 2.872, tetapi paragraf penjelas setelah Tabel 1 menyatakan 2.873. TXT tidak memberikan rekonsiliasi. Sampel pekerja dari Hungarian Labor Force Survey disebutkan secara substantif, tetapi ukuran numerik dan rincian pemilihannya tidak disebutkan dalam file (TXT, hlm. 155, baris 655-659; hlm. 153-154, baris 560-568).

**Inferensi review.** Angka 2.872 atau 2.873 harus dibaca sebagai jumlah unit spasial yang tersedia untuk regresi tingkat munisipalitas, bukan jumlah perusahaan atau jumlah individu. Replikasi 300 pada grid juga bukan 300 sampel independen; itu adalah 300 realisasi pembagian wilayah yang diterapkan pada basis data yang sama. Perbedaan jumlah observasi dan tidak tersedianya ukuran sampel HLFS membatasi audit eksternal atas komposisi sampel.

## Dependent Variables

**Laporan sumber.** Pada Model 1, variabel dependen adalah upah rata-rata pekerja pada unit spasial. Upah dihitung dari total biaya upah dan informasi pekerja penuh waktu, lalu digunakan dalam logaritma. Koefisien kepadatan ditafsirkan penulis sebagai elastisitas aglomerasi upah. Kepadatan penduduk usia kerja per km2 adalah variabel penjelas utama, sedangkan rata-rata tahun sekolah adalah kontrol (TXT, hlm. 153-155, baris 559-580 dan 597-606).

Pada Model 2, variabel dependen adalah jumlah perusahaan baru atau pembentukan perusahaan baru di unit spasial. Modelnya adalah Poisson; kepadatan menjadi variabel penjelas utama dan upah menjadi proksi kondisi pasar tenaga kerja. Data tahun 1998 digunakan bersama data tahun 1999 untuk membangun variabel pembentukan perusahaan baru, tetapi rumus atau aturan klasifikasi perusahaan baru tidak dijelaskan lebih rinci (TXT, hlm. 153 dan 155-156, baris 552-558 dan 660-721).

**Informasi yang tidak tersedia.** TXT tidak menyebut mata uang atau periode pembayaran upah secara rinci, tidak memberikan definisi formal jumlah perusahaan baru, dan tidak menjelaskan penanganan nilai nol atau transformasi variabel dependen pada Model 2. Catatan tabel menyatakan semua variabel dalam logaritma, tetapi rincian implementasi logaritma untuk jumlah perusahaan pada model Poisson tidak dijabarkan. Karena itu, review tidak mengasumsikan bentuk transformasi di luar pernyataan tersebut.

## Results

**Laporan sumber: regresi upah.** Tabel 1 melaporkan koefisien kepadatan pada model upah sebesar 0,055 dengan standard error 0,007 untuk munisipalitas dan 0,128 dengan standard error 0,021 untuk mikro-wilayah. Untuk grid buatan, rata-rata koefisien dari 300 replikasi adalah 0,082 pada grid 15 km, 0,116 pada grid 26 km, dan 0,137 pada grid 39 km. Rata-rata standard error masing-masing adalah 0,011, 0,019, dan 0,026, sedangkan simpangan baku koefisien lintas replikasi masing-masing adalah 0,006, 0,008, dan 0,015 (TXT, hlm. 154-155, Tabel 1, baris 631-651).

Koefisien kontrol tahun sekolah pada kolom munisipalitas dan mikro-wilayah adalah 0,966 dan 0,820. Pada grid 15 km, 26 km, dan 39 km, rata-ratanya adalah 1,098, 1,123, dan 0,979; simpangan baku koefisiennya adalah 0,121, 0,219, dan 0,510. R-squared berturut-turut untuk munisipalitas, mikro-wilayah, serta grid 15, 26, dan 39 km adalah 0,244, 0,383, 0,240, 0,361, dan 0,393. Tabel melaporkan jumlah observasi 2.872, 149, 437, 150, dan 73 (TXT, hlm. 154-155, Tabel 1, baris 637-651).

Narasi penulis menyebut urutan koefisien kepadatan sebagai 5,5 persen pada munisipalitas, 7,7 persen pada unit buatan kecil, 11,8 persen pada mikro-wilayah, dan 12,7 persen pada unit buatan sedang. Angka ini tidak sepenuhnya sama dengan angka Tabel 1, yang masing-masing menunjukkan 0,055, 0,082, 0,128, dan 0,116. TXT tidak menjelaskan perbedaan antara angka narasi dan tabel; keduanya dicatat terpisah di sini, bukan diselaraskan secara dugaan (TXT, hlm. 154, baris 612-619; Tabel 1, baris 637-645).

**Laporan sumber: regresi pembentukan perusahaan.** Pada Tabel 2, koefisien kepadatan adalah 1,377 dengan standard error 0,079 pada munisipalitas dan 0,917 dengan standard error 0,172 pada mikro-wilayah. Rata-rata koefisien dari grid 15, 26, dan 39 km adalah 1,321, 1,257, dan 1,146; rata-rata standard errornya adalah 0,074, 0,096, dan 0,219; simpangan baku koefisien lintas 300 replikasi adalah 0,027, 0,039, dan 0,085. Koefisien upah adalah 0,608 dengan standard error 0,200 pada munisipalitas, 0,554 dengan standard error 0,716 pada mikro-wilayah, serta rata-rata 0,526, 0,392, dan 1,664 pada grid 15, 26, dan 39 km. Simpangan baku koefisien upah pada grid tersebut adalah 0,110, 0,152, dan 0,358 (TXT, hlm. 155-156, Tabel 2, baris 687-707).

Jumlah observasi pada Tabel 2 sama dengan Tabel 1. Pseudo-R-squared yang tercantum adalah 0,467 dan 0,379 untuk dua unit administratif, serta 0,605, 0,615, dan 0,614 untuk grid 15, 26, dan 39 km. Penulis menyatakan bahwa koefisien kepadatan lebih besar dari satu pada seluruh estimasi dan menganggapnya sebagai hubungan bersih yang positif antara penduduk dan pembentukan perusahaan. Pernyataan naratif ini tidak sepenuhnya selaras dengan koefisien kepadatan 0,917 pada baris mikro-wilayah di Tabel 2; TXT tidak memberi penjelasan atas perbedaannya (TXT, hlm. 155-156, baris 711-721 dan Tabel 2, baris 693-707).

**Laporan sumber: perbandingan fragmentasi.** Untuk OLS upah dan Poisson pembentukan perusahaan, penulis menyatakan bahwa elastisitas pada tingkat munisipalitas lebih rendah daripada 95 persen elastisitas yang dihitung dari unit buatan. Untuk regresi upah, teks menyebut koefisien munisipalitas sebesar 5,2 persen, lebih rendah daripada batas bawah 95 persen sebesar 6,6 persen pada grid 15 km. Nilai tersebut divisualisasikan pada Gambar 4 dan Gambar 6 (TXT, hlm. 157-159, baris 751-802).

**Laporan sumber: perbandingan ukuran grid.** Untuk upah, penulis menemukan perbedaan elastisitas kepadatan antara grid 15 km dan 26 km, tetapi tidak menemukan perbedaan lanjutan yang signifikan di luar perbandingan tersebut. Hubungan dengan tahun sekolah disebut berubah antara grid 26 km dan 39 km. Untuk pembentukan perusahaan, estimasi titik pada grid 39 km tampak berbeda dari dua grid lain, tetapi perbedaannya tidak signifikan secara statistik karena variasi estimasinya lebih besar. Penulis juga menyatakan bahwa elastisitas upah terhadap pembentukan perusahaan pada grid besar berbeda secara statistik (TXT, hlm. 158-160, baris 806-837).

**Laporan sumber: perbandingan batas administratif dan unit buatan.** Pada Model 1, koefisien mikro-wilayah sebesar 12,7 persen dibandingkan dengan rata-rata 11,8 persen pada grid 26 km. Berdasarkan distribusi pada Gambar 4, perbedaan itu tidak signifikan; hipotesis nol bahwa efek unit administratif mikro-wilayah relatif terhadap unit buatan berukuran rata-rata sama dengan nol tidak dapat ditolak. Pada Model 2, penulis menyatakan bahwa koefisien kepadatan yang dibandingkan lebih besar dari satu dan kesamaan koefisien ditolak pada tingkat kepercayaan 5 persen, yang berarti terdapat perbedaan kecil tetapi signifikan antara unit administratif dan unit buatan. Angka 0,917 pada Tabel 2 tetap merupakan pengecualian yang tidak direkonsiliasi dalam TXT (TXT, hlm. 159-160, baris 839-859; Tabel 2, baris 693-695).

**Laporan sumber: distribusi perluasan dan validitas luar.** Untuk menguji perbandingan distribusi secara lebih luas, penulis menggabungkan 300 replikasi dengan 50 pengambilan acak dari distribusi normal di sekitar setiap estimasi. Uji Kolmogorov-Smirnov dua sisi tidak menolak hipotesis nol kesamaan antara distribusi yang terkait dengan batas administratif dan distribusi yang mencakup seluruh permutasi. Dengan distribusi perluasan tersebut, estimasi administratif dan buatan tidak dapat dibedakan baik pada mikro-wilayah maupun munisipalitas, dan perbedaan antara dua ukuran grid buatan juga tidak signifikan. Penulis menyimpulkan bahwa temuan khusus mengenai ukuran wilayah bersifat indikatif bila dibawa ke negara lain. Nilai statistik KS tidak dicantumkan dan disebut tersedia atas permintaan (TXT, hlm. 161, baris 896-931 dan catatan kaki 18 baris 941).

**Laporan sumber: perbandingan dengan metode lain.** Agregasi berbasis lingkaran dengan radius 14 km dipilih agar luasnya mendekati rata-rata mikro-wilayah dan grid 26 km. Di Hungaria, munisipalitas yang lebih kaya cenderung dihitung lebih sedikit oleh lingkaran, sedangkan munisipalitas yang lebih miskin dihitung lebih sering; penulis menganggap hal ini dapat membiasakan estimasi. Unit grid yang saling terpisah tidak mengalami penghitungan berulang tersebut (TXT, hlm. 162, baris 949-967).

Pada metode dots-to-boxes dengan 150 seed, artikel melaporkan bahwa unit buatan lebih kecil di barat daya dan lebih besar di tengah-timur karena heterogenitas ukuran munisipalitas. Grid menghasilkan 93 unit di sebelah barat Danube, sedangkan dots-to-boxes menghasilkan 57 unit. Distribusi koefisien dots-to-boxes memiliki median yang agak lebih rendah dan simpangan baku yang lebih tinggi, yaitu 0,7 dibandingkan 1,4 persen. Estimasi dari metode lingkaran lebih kecil daripada estimasi titik mikro-wilayah, tetapi keduanya berada dalam interval kepercayaan estimasi inti (TXT, hlm. 162-163, baris 974-1020; Appendix, Gambar 14-15, baris 1163-1182).

## Findings

**Interpretasi penulis.** Temuan substantif yang ditarik penulis adalah sebagai berikut:

- Ukuran unit spasial dapat mengubah elastisitas aglomerasi. Pada contoh upah, koefisien meningkat dari unit yang lebih kecil ke unit yang lebih besar, tetapi bukti perbedaan statistik terutama terlihat antara grid 15 km dan 26 km.
- Fragmentasi munisipalitas Hungaria berkaitan dengan elastisitas kepadatan-upah yang lebih rendah daripada estimasi pada unit buatan yang kurang terfragmentasi dan berukuran serupa. Penulis memperingatkan bahwa perbandingan lintas negara pada nomenklatur administratif yang sama dapat membandingkan unit dengan ukuran nyata yang berbeda.
- Batas administratif mikro-wilayah tidak menunjukkan perbedaan yang signifikan untuk elastisitas upah ketika dibandingkan dengan grid 26 km yang berukuran rata-rata sama. Sebaliknya, perbedaan pada model pembentukan perusahaan ditolak pada tingkat 5 persen.
- Pengujian dengan distribusi perluasan melemahkan pembacaan bahwa perbedaan ukuran grid atau batas administratif dapat digeneralisasi dengan mudah ke negara lain.
- Grid and shake dipandang lebih sesuai daripada dots-to-boxes ketika unit dasar sangat heterogen dan ukuran unit berkorelasi secara nonacak dengan kondisi sosial-ekonomi. Dibandingkan metode lingkaran, keunggulan yang ditekankan adalah setiap unit dasar dihitung satu kali.

**Inferensi review.** Hasil paling kuat dalam artikel adalah demonstrasi bahwa satu hubungan dapat berubah menurut agregasi dan bahwa variasi tersebut dapat divisualisasikan serta diuji dengan distribusi koefisien. Namun, hasil antaroutcome tidak seragam: perbedaan batas administratif tidak signifikan pada model upah tetapi signifikan pada model pembentukan perusahaan. Karena itu, temuan tidak mendukung pernyataan universal bahwa batas administratif selalu penting atau selalu tidak penting. Pernyataan penulis bahwa mungkin ada kebijakan yang berperan pada model pembentukan perusahaan adalah interpretasi yang masuk akal dari perbedaan tersebut, tetapi bukan identifikasi efek kebijakan.

## Conclusions

**Laporan sumber.** Penulis menyimpulkan bahwa grid and shake adalah metode yang fleksibel, transparan, sederhana, dan relatif cepat untuk menguji robustnes penelitian empiris pada data yang diagregasi secara spasial. Dalam menghasilkan distribusi parameter, metode ini diposisikan sebagai alternatif bagi dots-to-boxes; dalam memperhitungkan jarak, ia diposisikan sebagai alternatif bagi spatial lags berbobot (TXT, hlm. 163-164, baris 1023-1029).

Metode dinilai sesuai bagi peneliti dan praktisi yang memiliki data pada tingkat administratif rendah seperti munisipalitas atau kode pos. Penulis menyebut empat kondisi penggunaan: variabel bermakna pada unit regional; proses yang dikaji tidak dibatasi pada satu unit dan memiliki spillover; wilayah tidak dipisahkan dari aliran transportasi atau pengetahuan oleh geografi pertama seperti laut atau gunung; serta unit dasar heterogen dan ukuran rata-ratanya berkorelasi dengan fitur tak teramati (TXT, hlm. 163-164, baris 1030-1057).

Penulis menyatakan bahwa unit buatan yang berukuran sama membantu menghindari bias dari struktur spasial yang endogen, menghitung semua unit dasar sekali, dan menggabungkan keunggulan sejumlah metode terdahulu. Keterbatasan yang diakui dalam perbandingan itu adalah fleksibilitas yang lebih rendah untuk memodelkan hubungan nonlinier di dalam unit. Dalam aplikasi Hungaria, penulis menyatakan bahwa ukuran grid memengaruhi pengukuran premi aglomerasi dan bahwa batas regional tidak berdampak pada elastisitas upah terhadap kepadatan (TXT, hlm. 164, baris 1058-1076).

**Inferensi review.** Kesimpulan tersebut sebaiknya dibaca sebagai klaim metodologis yang bersyarat, bukan validasi umum untuk seluruh jenis data regional. Uji validitas luar tidak menolak perbedaan distribusi, tetapi itu tidak membuktikan bahwa distribusi benar-benar identik. Selain itu, kesimpulan tentang kebijakan tidak dapat dinaikkan menjadi efek kausal karena desain yang dilaporkan berupa penampang lintang dan perbandingan agregasi.

## Contributions

**Laporan sumber.** Kontribusi metodologis yang diklaim artikel adalah prosedur yang dapat: membandingkan estimasi pada beberapa tingkat agregasi; memperlakukan distribusi ukuran unit yang tidak seragam dan tidak acak; membandingkan unit administratif dengan unit buatan; dan mengukur signifikansi statistik perbedaan (TXT, hlm. 145, baris 158-163).

Kontribusi empirisnya adalah penerapan prosedur pada dua hubungan di Hungaria, yaitu kepadatan dengan upah dan kepadatan dengan pembentukan perusahaan baru, serta pembandingan tiga ukuran grid dengan dua tingkat administratif. Artikel juga menempatkan hasil itu berdampingan dengan metode lingkaran, spatial lags, dan dots-to-boxes (TXT, hlm. 153-163, baris 538-547 dan 751-1020).

**Inferensi review.** Sumbangan utama artikel adalah membuat pilihan agregasi menjadi objek robustnes yang dapat diamati sebagai distribusi, bukan sekadar keputusan awal peneliti. Sumbangan itu bersifat prosedural dan diagnostik. TXT tidak menunjukkan bahwa artikel menyediakan dataset publik, kode replikasi, atau estimator kausal baru; keberadaan atau ketiadaan bahan tersebut di luar TXT tidak dapat dipastikan dari sumber yang digunakan.

## Research Gap

**Laporan sumber.** Artikel mengidentifikasi celah pada praktik estimasi regional yang menggunakan unit administratif tertentu tanpa cara statistik yang memadai untuk mengetahui apakah koefisien sensitif terhadap batas dan ukuran unit. Metode terdahulu dinilai hanya memenuhi sebagian kebutuhan: spatial lag menangani aspek spasial tetapi jumlah tetangga tidak ditentukan oleh ukuran unit; lingkaran sederhana dan fleksibel tetapi dapat mengulang atau mengoversampling wilayah padat; dots-to-boxes dapat menghasilkan ukuran dan bentuk yang tidak seragam ketika unit dasar heterogen; dan robustness check konvensional tidak selalu memberi distribusi pembanding atau uji signifikansi (TXT, hlm. 147-149 dan 162-163, baris 351-364 dan 949-1020).

Penulis terutama menempatkan konteks Hungaria sebagai kasus yang tidak cocok untuk metode yang mengandaikan unit dasar relatif sama besar, karena ukuran munisipalitas berbeda secara besar dan mengelompok secara spasial. Grid and shake diajukan untuk mengisi celah tersebut dengan menyamakan ukuran rata-rata unit buatan sambil mengacak letak batasnya (TXT, hlm. 147-148 dan 162-163, baris 285-312 dan 989-1008).

**Inferensi review.** Celah yang tersisa adalah pengujian lintas negara dan lintas waktu yang lebih luas, termasuk negara dengan geografi, sistem administratif, dan distribusi unit dasar yang berbeda. TXT juga belum memberi uji sensitivitas menyeluruh terhadap ukuran marker, ambang koreksi batas, jumlah replikasi, pilihan ukuran L, dan bentuk ketergantungan spasial. Ini adalah celah yang diinferensikan dari batas cakupan artikel, bukan agenda eksplisit yang dinyatakan penulis.

## Limitations

**Laporan sumber.** Artikel menyebut beberapa keterbatasan data dan prosedur secara langsung atau tersebar di dalam pembahasan:

- Data lokasi perusahaan hanya menunjukkan kantor pusat. Penulis merujuk bukti bahwa 7 persen perusahaan memiliki lebih dari satu lokasi dan rata-rata perusahaan tersebut memiliki 1,15 pabrik, lalu menilai potensi biasnya relatif kecil (TXT, hlm. 153, catatan kaki 14, baris 556-572).
- Pemberi kerja pekerja pada Hungarian Labor Force Survey tidak diketahui. Karena itu, informasi pekerja tidak dapat ditautkan langsung ke perusahaan dan hanya diringkas menjadi rata-rata pendidikan pada tingkat munisipalitas (TXT, hlm. 153-154, baris 559-580).
- Regresi munisipalitas tidak mencakup seluruh 3.125 munisipalitas karena ada unit tanpa aktivitas manufaktur yang dapat diidentifikasi. Perbandingan dengan grid 15 km juga dapat dipengaruhi oleh wilayah tanpa pekerjaan yang masuk ke penyebut kepadatan; penulis menyatakan arah biasnya ambigu dan persoalan itu menonjol di Hungaria bagian barat. Catatan kaki menyatakan bahwa persoalan tersebut tidak memengaruhi grid yang lebih besar, tetapi menulis ukuran “26 and 36 km”, sedangkan bagian lain menggunakan grid 39 km. Perbedaan ini tidak direkonsiliasi dalam TXT (TXT, hlm. 155, catatan kaki 16, baris 655-680).
- Koreksi batas hanya menangani unit yang lebih kecil dari 10 persen luas kotak dengan menggabungkannya ke tetangga. Penulis menyebutnya sebagai pengimbangan sebagian, bukan penghapusan seluruh efek batas (TXT, hlm. 152, baris 489-496).
- Penggunaan metode dibatasi oleh empat kondisi yang dicantumkan penulis, termasuk adanya spillover lintas unit, tidak adanya penghalang geografis yang relevan, dan korelasi antara heterogenitas ukuran unit dengan fitur tak teramati (TXT, hlm. 163-164, baris 1030-1057).

**Inferensi review.** Bukti empiris dibatasi pada satu negara, periode utama 1999 untuk upah dan informasi 1998-1999 untuk pembentukan perusahaan, serta perusahaan manufaktur yang memenuhi kriteria tertentu. Generalisasi ke wilayah lain tidak dapat diasumsikan. Pengacakan juga hanya menyapu pergeseran grid dalam aturan yang dipilih, bukan seluruh kemungkinan partisi spasial. Pemakaian distribusi normal untuk menggambar ketidakpastian koefisien dan penggunaan 300 replikasi merupakan keputusan pemodelan yang dapat memengaruhi interval dan uji perbandingan.

Desain penampang lintang yang dilaporkan tidak mengatasi endogenitas kepadatan, seleksi lokasi perusahaan, atau kemungkinan bahwa faktor tak teramati memengaruhi upah dan pembentukan perusahaan sekaligus. Dengan demikian, istilah “elasticity” dalam hasil tidak boleh dibaca sebagai bukti kausal tanpa asumsi tambahan yang tidak disediakan TXT. Detail yang tidak tersedia mengenai jumlah perusahaan, ukuran sampel survei, konstruksi perusahaan baru, kode, dan statistik KS juga membatasi pemeriksaan replikasi.

## Challenges

**Laporan sumber.** Tantangan implementasi yang dihadapi metode meliputi digitasi peta, penyediaan marker yang cukup rapat untuk mengenali wilayah munisipalitas kecil, pencocokan marker dengan poligon, pengelompokan munisipalitas yang memotong lebih dari satu kotak, serta pengurangan unit kecil di perbatasan (TXT, hlm. 150-152, baris 391-418 dan 489-519).

Penulis juga menghadapi tantangan substantif berupa distribusi ukuran munisipalitas yang tidak seimbang dan berkelompok. Tantangan analitis berikutnya adalah membangun distribusi koefisien dari banyak realisasi, membandingkannya dengan satu koefisien administratif, serta memasukkan standard error masing-masing realisasi ke dalam distribusi perluasan (TXT, hlm. 147-153 dan 161, baris 255-312, 499-535, dan 908-918).

Pencocokan data juga memiliki tantangan: data neraca perusahaan berada pada tingkat perusahaan, data populasi dan luas pada tingkat munisipalitas, dan data pendidikan berasal dari survei yang tidak mengidentifikasi pemberi kerja. Hasil akhirnya harus dibangun ulang pada setiap agregasi, termasuk dengan pembobotan frekuensi untuk rata-rata tahun sekolah (TXT, hlm. 153-155, baris 552-580 dan 621-625).

**Catatan audit review.** TXT memuat beberapa ketidakkonsistenan yang perlu diperlakukan sebagai tantangan dokumentasi, bukan dikoreksi dengan dugaan:

- Bagian 3.4 menyebut pengulangan seribu kali, sedangkan sebagian besar keterangan metode, tabel, dan gambar menyebut 300 replikasi (TXT, hlm. 145 dan 152-159, baris 141-146, 506-535, 643-651, 699-707, dan 724-735).
- Tabel 1 dan Tabel 2 mencantumkan 2.872 observasi munisipalitas, sedangkan paragraf sesudah Tabel 1 menyebut 2.873 (TXT, hlm. 155-156, baris 644-655 dan 699-701).
- Narasi hasil upah menyebut 7,7 persen untuk grid kecil, 11,8 persen untuk mikro-wilayah, dan 12,7 persen untuk grid sedang, sementara Tabel 1 mencantumkan 0,082, 0,128, dan 0,116 untuk kolom yang bersesuaian (TXT, hlm. 154-155, baris 612-619 dan 637-645).
- Narasi Model 2 menyatakan bahwa semua koefisien kepadatan lebih besar dari satu, tetapi Tabel 2 mencantumkan 0,917 pada mikro-wilayah (TXT, hlm. 155-156, baris 711-721 dan 693-695).
- Catatan kaki 16 menyebut grid 36 km, sedangkan metode dan tabel menggunakan grid 39 km. Tabel 2 juga mewarisi catatan “years of schooling” meskipun baris kovariatnya adalah Wage. TXT tidak memberi penjelasan atas perbedaan penulisan ini (TXT, hlm. 155-156, baris 676-680 dan 703-707).

**Inferensi review.** Ketidakkonsistenan tersebut tidak cukup untuk menyatakan hasil salah, tetapi cukup untuk mengharuskan pembaca memilih angka secara eksplisit dan menahan diri dari rekonstruksi yang tidak didukung. Audit metodologis atau replikasi memerlukan klarifikasi penulis, terutama mengenai jumlah replikasi dan jumlah observasi dasar.

## Practical Implications

**Laporan sumber.** Penulis menyarankan agar peneliti tidak membandingkan koefisien regional hanya berdasarkan nomenklatur administratif. Ukuran aktual unit, distribusi ukuran, dan kemungkinan pengelompokan geografis perlu diperhitungkan. Grid and shake dapat digunakan untuk membandingkan estimasi pada unit berukuran rata-rata sama, menguji apakah unit administratif merupakan realisasi spasial yang khusus, dan membangun interval atau distribusi perbandingan (TXT, hlm. 144-149 dan 163-164, baris 118-121, 340-364, dan 1070-1076).

Untuk evaluasi kebijakan regional, penulis menyarankan perbandingan wilayah administratif dengan unit pseudo-administratif yang ukurannya sebanding. Jika perbedaannya terlihat, prosedur dapat membantu menilai apakah batas administratif berkaitan dengan hubungan yang diestimasi. Namun, hasil model upah dalam artikel tidak menunjukkan dampak batas regional, sementara model pembentukan perusahaan menunjukkan perbedaan kecil yang signifikan (TXT, hlm. 148-149 dan 159-164, baris 315-348, 839-890, dan 1070-1076).

**Inferensi review.** Implikasi praktis yang paling aman adalah menjadikan sensitivitas unit spasial sebagai bagian dari pelaporan utama, bukan catatan tambahan. Prosedur ini dapat memperingatkan pembaca ketika perbandingan lintas wilayah lebih banyak mencerminkan ukuran unit daripada perbedaan hubungan substantif. Ia tetap tidak menggantikan desain identifikasi kebijakan, pengendalian endogenitas, atau penilaian kualitas data.

## Applications

**Laporan sumber: aplikasi yang benar-benar dilakukan.** Artikel menerapkan metode pada dua model berbasis data Hungaria. Aplikasi pertama mengestimasi premi aglomerasi upah dari kepadatan dan pendidikan. Aplikasi kedua mengestimasi pembentukan perusahaan baru dari kepadatan dan upah. Keduanya dibandingkan pada tingkat munisipalitas, mikro-wilayah, serta grid 15 km, 26 km, dan 39 km (TXT, hlm. 153-160, baris 538-547, 583-721, dan 751-859).

Tiga pertanyaan aplikasi yang lebih spesifik adalah pengaruh fragmentasi munisipalitas, pengaruh ukuran unit spasial, dan peran pembagian politik-administratif. Artikel juga menerapkan atau mereplikasi perbandingan dengan agregasi lingkaran dan dots-to-boxes untuk melihat dampak penghitungan berulang serta heterogenitas ukuran dan bentuk unit (TXT, hlm. 157-163, baris 751-755 dan 934-1020).

**Laporan sumber: aplikasi yang disarankan.** Dalam kesimpulan, penulis menyebut contoh variabel yang dapat bermakna pada unit regional, seperti jumlah tempat tidur rumah sakit, dokter, dan kelas universitas, serta proses spillover seperti aliran pengetahuan. Kondisi itu disampaikan sebagai ruang penggunaan metode, bukan sebagai aplikasi empiris tambahan dalam artikel (TXT, hlm. 163-164, baris 1030-1057).

**Inferensi review.** Di luar Hungaria, TXT hanya memberi ilustrasi korelasi regional Eropa dan tidak melaporkan penerapan grid and shake pada negara lain. Karena itu, penggunaan artikel untuk konteks lain harus diperlakukan sebagai transfer metode yang perlu diuji, bukan sebagai bukti bahwa pola koefisiennya berlaku di tempat lain.

## Future Research (Optional)

**Laporan sumber.** Artikel tidak memiliki bagian agenda penelitian masa depan yang eksplisit. Penulis menyatakan bahwa metode dapat digunakan dalam pengaturan spasial lain dan berguna untuk membandingkan dataset dari berbagai bagian dunia, tetapi tidak merumuskan daftar studi lanjutan, desain baru, atau target data tertentu (TXT, hlm. 143-146 dan 163-164, baris 93-98, 164-183, dan 1070-1076).

**Inferensi review, bukan agenda yang dinyatakan penulis.** Penelitian lanjutan yang logis dapat menguji metode pada lebih banyak negara dan periode, membandingkan jenis unit dasar yang berbeda, serta melakukan analisis sensitivitas formal terhadap ukuran grid, kerapatan marker, ambang koreksi batas, jumlah replikasi, dan aturan tetangga. Penggabungan dengan panel, desain kuasi-eksperimental, atau model yang secara eksplisit menangani ketergantungan spasial juga dapat memisahkan sensitivitas agregasi dari masalah identifikasi kausal. Usulan ini tidak dianggap sebagai isi atau rekomendasi eksplisit artikel.

## Provenance Notes

- Seluruh review ini hanya menggunakan file TXT B20 yang ditentukan pengguna. Tidak ada informasi dari DOI, laman jurnal, artikel lain, atau pencarian eksternal yang ditambahkan.
- Seluruh teks yang tersedia dibaca, termasuk metadata ekstraksi pada baris 1-28, artikel pada baris 30-1182, appendix, dan daftar referensi pada baris 1187-1251.
- Locator utama menggunakan halaman cetak artikel, bagian, tabel, gambar, catatan kaki, dan rentang baris TXT. Nomor halaman PDF dan nomor halaman artikel dapat berdekatan tetapi tidak diasumsikan identik; halaman yang digunakan di review mengikuti nomor halaman artikel yang tercetak, seperti 143-170.
- Pernyataan dengan label **Laporan sumber** merangkum apa yang dinyatakan, ditampilkan, atau dilaporkan dalam TXT. Pernyataan dengan label **Interpretasi penulis** merangkum cara penulis memaknai hasil atau keunggulan metodenya. Pernyataan dengan label **Inferensi review** adalah analisis pengolahan ini dan bukan klaim yang dinyatakan penulis.
- Informasi yang tidak tersedia atau tidak dapat diverifikasi dari TXT meliputi nomor isu jurnal, jumlah perusahaan dan individu sebelum agregasi, ukuran numerik serta desain sampling HLFS, definisi rinci perusahaan baru, nilai statistik KS, kode replikasi, dan akses data mentah.
- Ketidakkonsistenan internal mengenai 300 versus seribu replikasi, 2.872 versus 2.873 observasi, angka narasi versus Tabel 1, klaim koefisien kepadatan Model 2 versus angka 0,917, serta penyebutan 36 versus 39 km dipertahankan sebagai catatan audit. Review tidak memilih salah satu angka dengan bantuan sumber di luar TXT.
- Tidak ada tabel yang digunakan dalam review ini.
