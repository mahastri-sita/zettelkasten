# Audit substansi dan metode — TGA Jabodetabek, versi 3 Oktober 2026

## Dasar dan batas audit

- Objek: `tga_pwk_jakarta_bab_1_4_2026_10_03.pdf`, 70 halaman PDF, Bab 1–4 dan daftar pustaka.
- Tanggal audit: 3 Oktober 2026. Mode: **self**, sebagai masukan untuk penulis.
- Rubrik: pertanyaan penelitian dan keputusan pengguna yang tercatat, *Panduan TGA* SPWK FT UGM, *Template TGA Penelitian 2026*, validitas konstruk, koherensi inferensi, keterlacakan bukti, dan kelayakan skripsi S1. Standar kontribusi jurnal Q1 tidak dijadikan kewajiban.
- Nomor halaman berikut mengikuti **nomor tercetak**; halaman PDF = nomor tercetak + 1. Contoh: hlm. 43 adalah halaman PDF 44.
- Naskah dibaca dari awal sampai daftar pustaka melalui ekstraksi teks. Sampel halaman diagram, tabel, dan peta diperiksa secara visual. Rumus dibandingkan dengan sumber `.tex`; prosedur zonal Bab 4 diperiksa pada skrip yang tersedia, tanpa menjalankan ulang pengolahan spasial.
- Sekitar **19.300 kata** pada tubuh Bab 1–4, termasuk teks tabel dan keterangan gambar yang terbaca. Ini perkiraan ekstraksi PDF setelah menyambung kata yang terpotong di akhir baris, bukan hitungan resmi. Teks di dalam gambar raster dapat tidak terhitung.
- Audit menghasilkan usulan; tidak mengubah PDF, `.tex`, Argument, keputusan pengguna, atau catatan perjalanan kontradiksi.

## Penilaian utama

Naskah mempunyai pertanyaan yang bernilai dan arsitektur penelitian yang dapat dipertahankan untuk S1. Kelemahannya bukan kekurangan teori atau kekurangan metode. Kelemahan terbesarnya adalah **beberapa operasi yang belum cocok dengan makna kesimpulan yang hendak ditarik**: integrasi khusus DKI, regresi dua tahap, penggunaan beban sebagai gerbang diagnosis, serta penerjemahan stok bangunan dan jumlah fasilitas menjadi fungsi metropolitan.

Bab 1–4 cukup lengkap sebagai bahan pembimbingan pra-TA. Namun, rancangan belum aman dieksekusi sebagaimana tertulis tanpa memperbaiki masalah tersebut. Ketiadaan hasil Bab 5 tidak dihitung sebagai kesalahan: dokumen konteks menyatakan bahwa tahap pra-TA hanya memerlukan Bab 1–4.

Gagasan yang lebih kuat adalah menempatkan **kesesuaian atau perbedaan antara keterhubungan metropolitan dan fungsi yang berlokasi di pusat sekunder** sebagai masalah empiris utama. Borrowed size dan shadow tetap menjadi lensa interpretasi setelah hasil diperiksa. Kekuatan skripsinya terletak pada membedakan keadaan yang tampak serupa, bukan pada menghasilkan sebanyak mungkin label.

## Keputusan yang tetap dihormati

Audit membaca keputusan terkunci dan D1–D8 pada `output/naskah/todo_revisi_bab_1_4.md`, terutama §9.2. Usulan berikut tetap mempertahankan:

1. Jabodetabek sebagai cakupan; Cianjur tidak ditambahkan.
2. DKI Jakarta sebagai inti penelitian dan konteks kewenangan; WSM sebagai salah satu sumber.
3. Dua tingkat analisis: kecamatan dan kabupaten/kota.
4. Dua domain utama: layanan dan pekerjaan, dengan batas proksi pekerjaan yang jelas.
5. Inferensi Q3 melalui kemiringan residu terhadap integrasi.
6. Penandaan pusat melalui massa; P75 penduduk atau volume hunian.
7. Satu indikator satu peran; manfaat, beban, dan ketergantungan tetap terpisah.
8. NRES di luar kawasan industri sebagai spesifikasi utama; NRES total sebagai pembanding.
9. Label shadow hanya dari layanan; kawasan hunian tetap dapat menjadi kasus yang perlu diperiksa.
10. Web GIS dan what-if tetap tersedia sebagai keluaran; CCTV bersifat opsional sesuai rekaman, dan SUMO hanya relevan bila terkait CCTV.

Karena ini audit, menemukan kelemahan pada keputusan yang telah disahkan tidak berarti membatalkannya. Di bawah ini dibedakan koreksi matematis, penyempurnaan pengukuran, dan usulan interpretasi.

## Kekuatan yang perlu dipertahankan

- **Pertanyaan tidak menganggap ekspansi Jakarta pasti baik atau buruk.** Latar belakang dan tujuan memberi ruang hasil positif, negatif, dan campuran.
- **Dua tingkat mengikuti resolusi sumber.** Larangan menurunkan angka kabupaten/kota menjadi observasi kecamatan merupakan pilihan yang tepat.
- **Fungsi dipisahkan dari produktivitas dan kesejahteraan.** Pembatasan ini sudah kuat, meskipun belum konsisten pada seluruh istilah.
- **Tolok ukur internal disebut relatif.** DKI tidak digunakan sebagai standar yang otomatis harus ditiru seluruh kecamatan.
- **Bukti tandingan hadir.** Teori tidak hanya dipakai untuk membenarkan dugaan shadow.
- **Sumber yang belum tersedia dinyatakan belum diambil.** Ini lebih dapat dipertanggungjawabkan daripada menyajikan semua lapisan sebagai data yang sudah siap.
- **Bab 4 memiliki angka, sumber, dan peta yang relevan.** Perbedaan jaringan eksisting dan usulan JUTPI 3 juga sudah jelas.

## Masalah kritis

### C1. Rumus integrasi khusus DKI tidak mengestimasi persentase menuju DKI yang dinyatakan

**Lokasi:** hlm. 8, 27, 37, 42–43; terutama §3.6.3.

Rumusnya adalah:

\[
I_i^{DKI}=I_i\,O_{k(i)}^{2023}.
\]

WSM menggunakan proporsi perjalanan rutin menuju inti morfologis terhadap penduduk bekerja/sekolah asal. Sementara itu, \(O_k\) adalah pangsa tujuan DKI **di antara komuter yang melintasi batas kabupaten/kota**, termasuk tujuan luar Jabodetabek dalam penyebut. Inti WSM mencakup banyak tujuan di luar DKI dan perjalanan antarkecamatan dalam kabupaten/kota yang sama.

Perkalian probabilitas membutuhkan pangsa DKI **bersyarat pada perjalanan ke inti WSM**, dengan populasi, definisi perjalanan, dan periode yang kompatibel. Pangsa itu tidak tersedia dalam \(O_k\). Mengasumsikan semua kecamatan dalam kabupaten/kota mempunyai pangsa yang sama belum menyelesaikan perbedaan penyebut ini. Status S membuat asumsi terlihat, tetapi tidak membuat rumus tersebut menjadi estimator persentase yang sah.

**Arah perbaikan dalam D1:** spesifikasi kembar tetap dilaporkan, tetapi hasil perkalian disebut **indeks WSM yang dibobot orientasi DKI kabupaten/kota**, bukan estimasi persentase komuter kecamatan menuju DKI. Ia menguji pembobotan konteks DKI; ia tidak memvalidasi tujuan DKI pada kecamatan. Orientasi DKI teramati tetap dibaca pada tingkat kabupaten/kota. Jika yang dipertahankan adalah klaim persentase DKI, desain memerlukan data bersyarat yang sesuai dan belum tersedia pada bukti yang diperiksa.

### C2. Regresi residu belum otomatis mengendalikan massa dan karakteristik lokal

**Lokasi:** hlm. 22, 43–45; §2.3.2, §3.6.4, §3.6.6.

Naskah membentuk harapan dari \(S,X\), kemudian meregresikan residu terhadap \(I,Z\). Alasan bahwa \(S,X\) sudah digunakan pada tahap pertama tidak cukup untuk menyatakan bahwa kemiringan tahap kedua merupakan hubungan integrasi yang telah dikendalikan terhadap keduanya.

Dalam kasus linear paling sederhana, misalkan \(W\) memuat massa dan kontrol. Koefisien parsial adalah:

\[
\theta_{parsial}=\frac{I^TM_WY}{I^TM_WI},
\]

sedangkan regresi residu \(M_WY\) pada integrasi mentah memakai penyebut \(I^TI\), setelah pemusatan yang sesuai. Keduanya umumnya berbeda apabila integrasi berkaitan dengan massa/kontrol. Prinsip ini dijelaskan dalam materi regresi parsial [William Greene, Econometrics I, Part 4](https://people.stern.nyu.edu/wgreene/Econometrics/Econometrics-I-4.pdf), khususnya pembahasan Frisch–Waugh–Lovell.

Dalam naskah, persoalannya lebih kompleks karena prediksi leave-one-out, model binomial negatif, dan residu logaritmik tidak memenuhi identitas OLS tersebut begitu saja.

**Arah perbaikan tanpa mengganti Q3:** tetap gunakan kemiringan residu sebagai analisis utama, tetapi tentukan kontrol massa dan \(X\) pada tahap kedua, beserta efek utama status inti dan moderator industri. Bandingkan secara wajib dengan model satu tahap yang sesuai distribusi outcome. Nyatakan bahwa kemiringan residu adalah estimand operasional penelitian; jangan otomatis menyamakannya dengan koefisien fungsi yang telah dikendalikan. Ketidakpastian perlu mencakup pembentukan benchmark, bukan hanya galat baku tahap kedua.

### C3. Residu tidak pasti berpusat nol, dan tidak pasti separuh unit bertanda negatif

**Lokasi:** hlm. 8, 13, 23, 44.

Pernyataan paling jelas pada hlm. 13 adalah bahwa “kira-kira separuh unit pasti bertanda negatif”. Ini salah secara matematis. Bahkan residu OLS dalam sampel dengan intersep hanya memiliki jumlah nol; jumlah tanda positif dan negatif tidak harus seimbang. Pada residu logaritmik hasil prediksi leave-one-out dan model hitungan, jumlah residu nol juga tidak dijamin.

**Arah perbaikan:** pertahankan pesan bahwa tanda residu sendiri bukan bukti borrowed size atau shadow. Hapus jaminan pemusatan dan pembagian tanda; laporkan distribusi aktual. Tolok ukur internal memberikan posisi relatif terhadap pembanding internal, bukan bukti bahwa seluruh sistem memenuhi atau gagal memenuhi kebutuhan normatif.

### C4. Arus kerja/sekolah tidak membuktikan kebocoran permintaan layanan; tanda positif tidak meniadakan kausalitas terbalik

**Lokasi:** hlm. 14, 24, 45–46; §2.1.8 dan §3.6.6.

Pada hlm. 14, defisit layanan dan orientasi penduduk ke inti diikuti pernyataan bahwa permintaan “bocor ke inti”. Data komuter kerja/sekolah tidak mengamati perjalanan berobat, penggunaan bank, atau transaksi layanan. Rendahnya perguruan tinggi lokal juga dapat mendorong perjalanan sekolah ke luar; masalah arah sebaliknya tidak hilang hanya karena outcome dipindahkan dari pekerjaan ke layanan.

Pada hlm. 45, kemiringan positif pekerjaan dibenarkan untuk borrowed size karena “arah sebaliknya tidak menghasilkan tanda positif”. Pernyataan ini terlalu kuat. Pertumbuhan fungsi lokal, seleksi lokasi rumah tangga, jaringan transportasi, atau perkembangan kota baru dapat berkaitan dengan integrasi dan stok nonhunian secara bersamaan. Tidak ada dasar untuk membatasi seluruh alternatif itu pada satu tanda.

**Arah perbaikan dalam D2:** tetap hanya gunakan layanan untuk label shadow, tetapi akui bahwa layanan pun belum mengidentifikasi kebocoran permintaan. Hasil positif pekerjaan juga tetap asosiasional. “Konsisten dengan” berarti cocok dengan sebagian implikasi teori setelah alternatif diperiksa, bukan bahwa arah sebab-akibat sudah diketahui.

### C5. Gerbang shadow belum mempunyai bukti beban/ketergantungan pada unit yang diperlukan

**Lokasi:** hlm. 24, 38, 44–46; Tabel 3.4–3.5.

Waktu arus bebas dari titik berat penduduk ke Bundaran HI mengukur hambatan menuju **satu tujuan hipotetis**. Ia tidak mengukur perjalanan aktual tiap komuter. Membandingkan urutan agregatnya dengan pangsa perjalanan panjang pada delapan kabupaten/kota hanya memeriksa kecocokan pada skala agregat; hal itu tidak memvalidasi 141 kecamatan. Durasi survei juga mencakup perjalanan ke seluruh tujuan, bukan khusus Bundaran HI atau DKI.

Asimetri dan rasio masuk/keluar kabupaten/kota sudah tepat disebut konteks. Namun, apabila konteks itu meloloskan setiap kecamatan di kabupaten/kota untuk label shadow, terjadi atribusi lintas tingkat meskipun angka tidak disalin ke kolom kecamatan.

**Arah perbaikan dalam D4–D5:** Bundaran HI, perutean OSM, serta syarat beban **atau** ketergantungan tetap dipertahankan. Nyatakan waktu arus bebas sebagai hambatan potensial; status agregat yang mendukung atau melemahkan interpretasi tidak menjadi bukti individual kecamatan. Jika gerbang kompatibilitas unit gagal, gunakan keluaran “terintegrasi tetapi tertinggal” atau “tidak terselesaikan” yang sudah tersedia. Label yang lebih kuat hanya diberikan pada tingkat bukti yang mendukungnya.

### C6. Selang ketidakpastian belum didefinisikan, tetapi sudah menentukan hampir seluruh klasifikasi

**Lokasi:** hlm. 22, 44–46; Tabel 2.2.

Naskah berpindah antara “selang ketidakpastian residu” dan “selang prediksi leave-one-out”. Selang untuk **rata-rata fungsi harapan** menjawab pertanyaan berbeda dari selang prediksi untuk **realisasi fungsi sebuah unit**. Ketidakpastian koefisien Q3 merupakan objek ketiga. Leave-one-out sendiri hanya prosedur prediksi; ia tidak menentukan cara membangun ketiga selang tersebut.

**Arah perbaikan:** tetapkan terlebih dahulu objek selang, tingkat kepercayaan, dan cara menghitungnya. Untuk diagnosis unit, tentukan apakah yang dicari adalah penyimpangan dari rata-rata pembanding atau observasi yang tidak lazim terhadap distribusi prediksi. Untuk Q3, perhitungkan ulang kedua tahap dalam prosedur ketidakpastian yang dipilih dan pertimbangkan ketergantungan spasial. Jangan menetapkan bahwa banyak unit “diharapkan” tidak terselesaikan sebelum distribusi dan galat diperiksa. Unit tanpa bukti penyimpangan yang kuat juga perlu dibedakan alasannya dari unit yang datanya hilang.

### C7. Rencana menyimpan residu Google belum mengatasi keterbalikan jumlah mentah

**Lokasi:** hlm. 35, 37, 41, 47; §3.5.8.

Syarat Places Aggregate API membatasi penyimpanan jumlah mentah dan mensyaratkan nilai turunan yang tidak menggantikan atau memungkinkan deduksi POI Counts. Mengubah jumlah menjadi residu belum otomatis memenuhi syarat itu. [Google Maps Platform Service Specific Terms, §13](https://cloud.google.com/maps-platform/terms/maps-service-terms).

Secara matematis, untuk residu yang digunakan naskah:

\[
R_i=\ln(F_i+c)-\ln(\widehat F_i+c)
\quad\Rightarrow\quad
F_i=e^{R_i}(\widehat F_i+c)-c.
\]

Jika benchmark, konstanta, dan residu per kecamatan disimpan agar penelitian dapat direproduksi, jumlah fasilitas dapat direkonstruksi. Ini adalah masalah desain yang dapat diperlihatkan tanpa menafsirkan seluruh kontrak.

**Arah perbaikan dalam batas “Google hanya untuk menghitung”:** jangan menjanjikan penyimpanan residu per kecamatan sebagai desain yang sudah terbukti patuh. Pertahankan Podes sebagai inti dan K3 sebagai jalur tanpa Google. Lapisan Google hanya dijalankan bila bentuk keluaran yang dipertahankan benar-benar memenuhi syarat yang berlaku. Menghapus data mentah saja tidak menyelesaikan rekonstruksi melalui transformasi terbalik.

## Masalah penting

### I1. Komposit layanan dapat lebih banyak mengukur kantor bank daripada layanan berorde tinggi

**Lokasi:** hlm. 35, 37, 40, 54–55.

Menjumlahkan satu rumah sakit, satu perguruan tinggi, dan satu bank umum memberi bobot numerik sama pada fungsi yang berbeda. Bank jauh lebih banyak pada sebagian wilayah; kantor bank umum juga tidak otomatis merupakan fungsi keuangan strategis. Keberadaan rumah sakit atau kampus belum membuktikan jangkauan pelayanannya melampaui kecamatan.

**Arah perbaikan dalam D7:** RS + PT + bank tetap sebagai spesifikasi gabungan. Analisis per jenis fasilitas yang sudah diwajibkan harus menjadi hasil substantif utama untuk memeriksa apakah tanda gabungan dikendalikan bank. Jika domain berbeda arah, jelaskan perbedaannya. Pembobotan SIRS/PDDikti adalah pemeriksaan tambahan, bukan obat yang harus selalu ditambahkan.

### I2. Domain pekerjaan sebenarnya mengukur stok fisik nonhunian di luar kawasan industri

**Lokasi:** hlm. 8, 37, 40, 44–45, 58–59.

GHSL tidak mengamati pekerja, okupansi, jenis pekerjaan, atau tingkat keahlian. Setelah masker industri, outcome semakin khusus: stok nonhunian yang tersisa di luar poligon kawasan industri formal. Volume positif di sekitar industri dapat menunjukkan bangunan besar, bukan bukti pekerjaan jasa atau manfaat produksi yang tertahan lokal. Dokumentasi [GHSL Data Package 2023, §2.3](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC133256/JRC133256_01.pdf) menetapkan satuannya sebagai volume bangunan per sel, bukan jumlah pekerjaan.

**Arah perbaikan dalam D3:** pertahankan masker utama, tetapi gunakan nama indikator yang tepat dan batasi kesimpulannya. NRES total merupakan pembanding substantif atas stok seluruh kawasan; mengubah masker mengubah cakupan outcome, sehingga hasil di dalam dan di luar industri tidak dianggap selalu mengestimasi objek identik. Asumsi stok 2018/2020 berubah lambat sampai 2024 perlu diperlakukan sebagai asumsi, terutama pada kawasan yang tumbuh cepat.

### I3. Logaritma pekerjaan belum memiliki aturan untuk nilai nol dan prediksi balik

**Lokasi:** hlm. 44; §3.6.4.

Model memakai \(\ln F_P\) dan \(c_P=0\). Ia tidak terdefinisi bila volume nonhunian sebuah kecamatan nol. Tabel sumber turunan menampilkan beberapa nilai 0,00 juta m³; angka yang dibulatkan itu belum membuktikan nol tepat, sehingga nilai tak dibulatkan harus diperiksa.

Prediksi \(\exp(\widehat{\ln F})\) juga bukan otomatis rata-rata \(F\) pada skala asli. Naskah belum menetapkan apakah benchmark memakai median/geometric mean atau mean dengan koreksi transformasi balik.

**Arah perbaikan:** definisikan penanganan nol, unit konstanta bila transformasi dipakai, serta target prediksi balik sebelum model dijalankan. Hindari mengeluarkan kecamatan nol secara diam-diam karena dapat menyaring lokasi yang justru substantif.

### I4. Layanan efektifnya 129 kecamatan; gabungan dua domain tidak tersedia untuk seluruh 141

**Lokasi:** hlm. 27–28, 34–35, 40, 55.

K1 bukan lagi kemungkinan abstrak: naskah sendiri menyatakan sumber layanan Kota Bekasi belum setara. Dua belas kecamatan itu penting; delapan di antaranya lolos penanda massa penduduk pada Bab 4. Hilangnya satu kota dapat memengaruhi gradient layanan dan keterwakilan pusat bermassa besar.

**Arah perbaikan:** tulis populasi wilayah 141 dan sampel analitis layanan 129 sebagai keadaan sumber saat ini. Perbandingan antardomain dan kategori campuran memakai unit yang sama-sama mempunyai kedua outcome. Pekerjaan tetap dapat memakai 141. Kota Bekasi tidak diperlakukan nol atau dipasangkan ke model Podes menggunakan profil Google/OSM yang belum setara. Semua kesimpulan layanan harus menyebut cakupannya.

### I5. P3 tidak diuji secara memadai hanya dengan korelasi residu

**Lokasi:** hlm. 24, 47; Tabel 2.3.

Korelasi positif sekalipun dapat mengandung kecamatan dengan residu pekerjaan positif dan layanan negatif. Korelasi nol tidak otomatis berarti terdapat konfigurasi campuran yang kuat. P3 juga berupa kemungkinan (“dapat”), sehingga perlu target observasional yang lebih jelas.

**Arah perbaikan:** gunakan scatterplot residu dua domain pada sampel yang sama, tampilkan ketidakpastian, lalu identifikasi kasus yang benar-benar berlawanan arah. Korelasi menjadi ringkasan tambahan. Tentukan lebih dahulu apa yang dihitung sebagai perbedaan substantif. Kegagalan menemukan pola bukan bukti bahwa pola itu mustahil.

### I6. Agregasi residu dan moderator belum cukup operasional

**Lokasi:** hlm. 25, 38, 45–47.

Residu logaritmik tidak boleh dijumlahkan seolah-olah merupakan jumlah fasilitas atau pekerjaan. Naskah belum menetapkan bagaimana \(R_i\) menjadi residu kabupaten/kota untuk P2. Penjumlahan fungsi teramati dan harapan lalu penghitungan ulang rasio berbeda dari rata-rata residu kecamatan; keduanya perlu dibedakan.

Interaksi integrasi × status inti dan integrasi × kawasan industri juga memerlukan efek utama masing-masing moderator. Status kota/kabupaten dan tahun pembentukan daerah akan berpotensi kolinear dengan efek tetap kabupaten/kota pada spesifikasi pembanding.

**Arah perbaikan:** pilih satu aturan agregasi dan jelaskan unit serta cakupannya. Tulis persamaan lengkap dengan efek utama dan interaksi; pilih kovariat berdasarkan peran teoretis, bukan daftar sebanyak mungkin. Laporkan kontrol yang tidak dapat diestimasi pada spesifikasi efek tetap.

### I7. Sensitivitas, triangulasi, dan perubahan objek masih tercampur

**Lokasi:** hlm. 15, 32, 46–48.

Daftar ketahanan memasukkan penggantian Podes 2024 dengan 2025 yang definisinya diakui berubah, penggantian waktu arus bebas dengan moda terjadwal, serta pergantian NRES di luar industri menjadi seluruh NRES. Ketiganya bukan selalu perubahan parameter pada konstruk yang sama.

**Arah perbaikan:** sajikan hasil secara terpisah menurut tujuan pemeriksaannya: ketahanan estimand yang sama, kesesuaian sumber, dan perubahan cakupan/moda/periode. Tidak perlu membuat sistem kode baru. Perbedaan yang masuk akal antarobjek tidak otomatis menyebabkan hasil inti gagal.

### I8. Inferensi spasial dan pengujian alternatif mempunyai aturan keputusan yang terlalu longgar

**Lokasi:** hlm. 28, 45–46.

“Autokorelasi kuat”, “diagnostik buruk”, “salah klasifikasi besar”, dan “urutan sejalan” belum mempunyai kriteria yang dapat direproduksi. Efek tetap kabupaten/kota mengendalikan perbedaan kelompok, tetapi tidak otomatis mengatasi ketergantungan spasial dalam atau lintas kelompok. Galat baku tahan heteroskedastisitas juga tidak otomatis tahan korelasi antarwilayah.

**Arah perbaikan:** tetapkan pemeriksaan minimum dan konsekuensinya sebelum hasil dilihat. Batasi interaksi dan spline pada pertanyaan yang benar-benar perlu. Jika ketergantungan spasial belum tertangani secara layak, pertahankan hasil sebagai eksplorasi asosiasi dengan ketidakpastian yang dinyatakan. Tidak perlu menjadikan semua keluarga model spasial sebagai kewajiban S1.

### I9. Profil penghasilan belum menunjukkan manfaat tambahan akibat integrasi

**Lokasi:** hlm. 38, 44–45, 56.

Pangsa komuter berpenghasilan ≥Rp5 juta menggambarkan penghasilan kelompok komuter yang diamati. Tanpa pembanding penduduk yang sebanding, angka itu tidak mengukur premium integrasi. Ambang absolut juga belum memperhitungkan biaya perjalanan dan seleksi pekerjaan/pendidikan.

**Arah perbaikan:** pertahankan angka sebagai **profil penghasilan komuter**, salah satu konteks manfaat yang mungkin. Akses kumulatif adalah peluang potensial, bukan pekerjaan yang benar-benar didapat. Jangan menyebut salah satu indikator sebagai manfaat tambahan yang sudah diatribusikan pada Jakarta.

### I10. Kecocokan kode geometri dan prosedur raster belum sesuai dengan janji metode

**Lokasi:** hlm. 39–40, 51, 59, 65; `latex/figures/scripts/zonal.py`.

Metode menjanjikan reproyeksi GHSL ke UTM dan agregasi berbobot bagian luas sel. Skrip Bab 4 justru menjumlahkan sel raster asal yang pusatnya jatuh pada poligon, menggunakan `all_touched=False`. Ini perbedaan prosedur nyata, bukan semata gaya penulisan. Karena volume adalah besaran per sel, reproyeksi dan interpolasi perlu menjaga total; resampling biasa tidak otomatis melakukannya.

Seluruh kode 2020 cocok dengan kode 2024 tidak membuktikan garis batasnya tidak berubah. Pada data kawasan industri, luas poligon yang jauh melampaui luas izin juga menunjukkan bahwa makna batas perlu diperiksa sebelum dianggap tepat untuk mengecualikan bangunan.

**Arah perbaikan:** selaraskan uraian dengan prosedur yang benar-benar dipakai. Nyatakan agregasi pusat sel sebagai pendekatan bila dipertahankan; periksa sensitivitas batas pada beberapa kasus yang kritis. Jangan menegaskan ekuivalensi geometri dari kode saja. Kesimpulan satuan hektare dan luas izin pada Kemenperin tetap diberi penanda inferensi bila belum dikonfirmasi dokumentasi.

## Kepatuhan template dan perbaikan penyajian

### F1. Latar belakang melebihi batas dua halaman

**Lokasi:** §1.1, hlm. 4–6, termasuk Gambar 1.1.

Template TGA Penelitian 2026 menyebut: **“Latar belakang ditulis dalam maksimal 2 halaman.”** Versi ini menggunakan tiga halaman. Pangkas detail operasi, tipologi, dan gerbang dari latar belakang; bagian tersebut sudah dibahas pada Bab 2–3. Gambar alur metode dapat ditempatkan pada bagian metode yang sesuai. Fleksibilitas judul/subbab dalam template tidak dengan sendirinya mencabut batas tersebut; dispensasi pembimbing belum tercatat pada bahan yang diperiksa.

### F2. Beberapa tabel memakai ukuran huruf di bawah minimum 10 pt

**Lokasi:** Tabel 2.1 hlm. 17–20, Tabel 3.2 hlm. 28, bagian Tabel 3.3–3.5, dan beberapa tabel Bab 4.

Template menyebut: **“Ukuran huruf dalam tabel tidak boleh lebih kecil dari 10.”** Pemeriksaan teks PDF menemukan ukuran sekitar **8,97 pt** untuk isi tabel yang disampel. Ini bukan hanya kesan visual. Ringkas isi/kolom dan atur orientasi bila perlu; jangan mempertahankan isi panjang dengan mengecilkan huruf.

### F3. Ruang untuk Bab 5–6 hampir habis dalam batas kata skripsi

Panduan TGA bagian Format Penulisan, halaman PDF 11, menetapkan maksimum 20.000 kata, tidak termasuk daftar pustaka dan lampiran. Tubuh Bab 1–4 diperkirakan sudah sekitar 19.300 kata. Belum dinyatakan melanggar batas pada versi parsial ini, tetapi naskah lengkap berisiko jelas melampauinya.

**Arah perbaikan:** alokasikan ruang yang cukup bagi hasil, pembahasan, dan kesimpulan. Target kerja sementara sekitar 12.000–14.000 kata untuk Bab 1–4 dapat memberi ruang 6.000–8.000 kata untuk Bab 5–6; itu usulan editorial, bukan aturan baru. Pindahkan rincian operasional berulang dan tabel cadangan panjang ke lampiran bila tetap diperlukan, sementara logika desain inti tetap berada di tubuh Bab 3.

### F4. Tata letak belum sepenuhnya mengikuti pengaturan template

Sumber LaTeX memakai kelas 11 pt, spasi 1,18, dan margin kiri 30 mm. Pengaturan dasar DOCX memakai 12 pt, spasi 1,5, dan margin 1 inci. Panduan meminta ukuran huruf dan pengaturan paragraf mengikuti template. Perbedaan ini perlu diselaraskan atau didukung arahan pembimbing yang terdokumentasi. Ukuran tabel di bawah 10 pt adalah pelanggaran eksplisit yang lebih pasti daripada perbedaan teknis kecil antarformat.

Daftar tabel dan daftar gambar juga belum tampil. Ketiadaan halaman pengesahan, intisari, dan abstrak tidak diperlakukan sebagai kesalahan substantif Bab 1–4; bagian depan naskah final mengikuti tahap administrasi yang berlaku.

### F5. Beberapa ketidakkonsistenan kecil masih perlu dirapikan

- Tabel 3.1 hlm. 26 masih menyebut perubahan seri pada fokus Q2, sementara rumusan Q2 hlm. 7 sudah tidak memuat perubahan.
- Hlm. 46 memakai “tersier” untuk sensitivitas ambang; bila yang dimaksud pembagian tiga kelompok, istilahnya **tertil**.
- Gambar 3.1 menampilkan rantai lama berisi layanan 141 dan beban lalu lintas, meskipun K1/K6 sudah aktif. Gambar boleh memuat keputusan historis, tetapi keadaan yang benar-benar aktif harus tampak langsung.
- Gambar 2.1 hlm. 21 mempunyai teks internal sangat kecil pada ukuran cetak. Perbesar atau ringkas isi kotak.
- Tabel penelitian terdahulu panjang pada hlm. 17–20; narasi sintesisnya sudah lebih kuat daripada katalog. Ringkas kolom celah yang berulang dan pertahankan temuan yang benar-benar menentukan desain.
- Istilah “relatif independen” dan “periferi lemah” perlu terus dibatasi sesuai definisi operasional; integrasi DKI rendah tidak berarti hubungan dengan pusat lain lemah, dan residu negatif tidak berarti basis lokal absolut kecil.
- Peta arus memakai garis melengkung sebagai hubungan asal–tujuan. Tambahkan keterangan bahwa garis bukan rute perjalanan aktual jika peta dipakai di luar konteks bab.

### F6. Konteks hukum belum memuat perubahan UU Jakarta

**Lokasi:** catatan kaki hlm. 4, hlm. 49, daftar pustaka.

UU 2/2024 sudah mempunyai perubahan melalui UU 151/2024. Perubahan itu menambahkan pengaturan nomenklatur jabatan dan membedakan pemberlakuan ketentuan perubahan dari Keppres pemindahan ibu kota. Rujukan yang hanya memakai UU awal belum cukup untuk merangkum keadaan hukumnya. [UU 151 Tahun 2024, Pasal I–II](https://peraturan.bpk.go.id/Download/369854/UU%20Nomor%20151%20Tahun%202024.pdf).

Nama “DKI Jakarta” tetap dapat dipertahankan sebagai nama wilayah statistik mengikuti keputusan pengguna. Koreksinya adalah melengkapi dasar dan membatasi penjelasan hukum; audit ini tidak menyimpulkan bahwa seluruh ketentuan UU awal telah berlaku atau bahwa Pasal 73 dicabut.

## Gagasan substansi yang lebih kuat dalam kerangka yang sama

### 1. Jadikan perbedaan hubungan dan fungsi sebagai inti kontribusi

Pertanyaan besar pengguna adalah kapan hubungan dengan Jakarta layak difasilitasi dan kapan perlu dikoreksi. Skripsi S1 dengan data sekarang tidak dapat menetapkan manfaat sosial bersih atau radius optimal. Ia dapat menjawab bagian yang lebih terukur: **apakah wilayah dengan keterhubungan metropolitan lebih tinggi juga mempunyai fungsi lokal yang lebih kuat setelah massa diperhitungkan, dan pada domain apa kedua hal itu berbeda?**

Ini bukan konstruk baru atau indeks gabungan. Ini penajaman benang merah yang sudah tersedia melalui Q1–Q3. Dua domain tetap utama, tetapi masing-masing memperoleh kesimpulan sesuai bukti: layanan sebagai keberadaan fasilitas, pekerjaan sebagai proksi stok fisik nonhunian. Perbedaan keduanya menjadi temuan substantif, bukan gangguan yang harus ditutup dengan satu kelas.

Keunggulannya terhadap versi sekarang adalah hasil tetap informatif apabila borrowed size atau shadow belum dapat dibedakan secara kuat. Penelitian tidak gagal hanya karena banyak label tidak lolos gerbang.

### 2. Uji tiga pembacaan yang benar-benar bersaing

| Pembacaan | Pola yang perlu dicari | Hal yang belum boleh disimpulkan |
|---|---|---|
| Keterhubungan berjalan bersama fungsi lokal | Kemiringan layanan dan proksi nonhunian positif atau lebih kuat pada pusat bermassa besar | Jakarta secara kausal membentuk fungsi tersebut |
| Keterhubungan terutama memberi hubungan ke fungsi di tempat lain | Integrasi tinggi dengan fungsi yang berlokasi lokal relatif rendah; profil komuter memperlihatkan orientasi/asimetri yang relevan | Kebocoran permintaan, kerugian kesejahteraan, atau kegagalan kota tidur |
| Pembagian fungsi berbeda menurut domain | Layanan dan stok nonhunian berbeda arah; pola sekitar industri dan kota baru memberikan konteks | Semua bentuk spesialisasi merupakan ketidakmatangan |

Ketiganya memakai data dan operasi yang sudah direncanakan. Hasil nol atau tidak presisi juga sah: ia menunjukkan bahwa hubungan yang diasumsikan teori tidak terdeteksi kuat pada konstruk, unit, dan periode ini.

### 3. Bedakan fungsi berlokasi lokal dari layanan yang tersedia di dekat batas

Jumlah fasilitas rendah dalam suatu kecamatan dapat berarti kekurangan nyata, tetapi dapat pula berarti fasilitas berlokasi di kecamatan tetangga. Ini alternatif yang sangat relevan bagi PWK: **kekurangan lokasi fasilitas dalam batas administratif tidak selalu sama dengan kekurangan layanan yang dapat dijangkau penduduk.**

Tanpa mengubah unit atau cara pemilihan pusat, lakukan pemeriksaan terbatas pada beberapa kasus yang menentukan interpretasi: lokasi defisit layanan besar, lokasi surplus, serta pasangan kecamatan yang berbagi pusat pelayanan. Gunakan fasilitas/direktori yang sudah tersedia dan jaringan yang memang direncanakan. Ini pemeriksaan atas penjelasan alternatif, bukan domain ketiga atau kewajiban menyusun indeks akses layanan baru.

Jika fasilitas dekat batas menjelaskan defisit, implikasinya dapat berupa akses lintas batas atau koordinasi pelayanan. Jika fungsi memang rendah dan alternatif itu tidak memadai, penguatan fasilitas lokal menjadi isu yang lebih masuk akal untuk dibahas. Pilihan kebijakan tetap kondisional; biaya, kualitas, kapasitas, dan permintaan aktual belum dihitung.

### 4. Beri pusat bermassa besar peran yang jelas pada hasil

Judul dan penanda P75 sudah dipertahankan. Karena itu, pembahasan hasil perlu benar-benar menunjukkan apa yang terjadi pada 43 kandidat pusat berbasis massa, bukan berhenti pada satu kemiringan seluruh 141 kecamatan.

Laporkan hubungan seluruh sampel, lalu gunakan interaksi massa yang sudah direncanakan atau perbandingan profil untuk membaca subkelompok tersebut. Jangan menyatakan bahwa hasil seluruh kecamatan otomatis merupakan hasil pusat sekunder. Pada domain layanan, tampilkan pusat yang tidak dapat dibaca karena Kota Bekasi belum tercakup. Pemilihan berbasis massa dipertahankan sebagai aturan penandaan; ia bukan bukti bahwa fungsi pusat sudah terbentuk.

### 5. Buat P2 menilai apa yang benar-benar diukur

Dengan NRES industri dikeluarkan, P2 tidak langsung menguji dekonsentrasi pekerjaan manufaktur. Ia lebih tepat memeriksa **apakah konsentrasi industri hadir bersama stok nonhunian di sekitarnya yang melampaui benchmark massa**.

Outcome ini dapat menunjukkan lingkungan kegiatan pendukung, tetapi jenis dan pemanfaatannya harus diperiksa sebelum dibaca sebagai layanan bisnis, retensi nilai, atau pekerjaan berkualitas. Perbandingan NRES total dan NRES di luar industri membantu membedakan konsentrasi stok di dalam kawasan formal dari stok di sekitarnya. Ini memperkuat D3 tanpa mengubah spesifikasi utama.

### 6. Pisahkan kesimpulan sistem, profil tempat, dan implikasi pemerintah

- **Tingkat sistem:** arah dan besar kemiringan, ketidakpastian, heterogenitas inti/noninti, serta hasil masing-masing jenis layanan.
- **Tingkat tempat:** posisi relatif kecamatan dan pusat berbasis massa, dengan alasan mengapa suatu label didukung atau belum terselesaikan.
- **Tingkat kewenangan:** ringkasan kabupaten/kota yang dapat digunakan untuk membaca kebutuhan koordinasi.

Koefisien negatif sistem tidak membuktikan bahwa setiap kecamatan beresidu negatif merupakan korban Jakarta. Sebaliknya, koefisien rata-rata positif tidak menutup kemungkinan adanya lokasi tertinggal. Pemisahan tingkat kesimpulan ini membuat temuan lebih berguna dan mencegah klaim melompat dari asosiasi sistem ke rekomendasi tempat.

### 7. Pertahankan paket kerja yang dapat dijelaskan oleh mahasiswa S1

| Wajib untuk jawaban penelitian | Penguatan setelah inti dapat dipertanggungjawabkan |
|---|---|
| Profil OD 2014/2019/2023, dengan batas keterbandingan | CCTV dan SUMO terkait rekaman yang valid |
| WSM kontinu dan pemisahan status inti; spesifikasi kembar dengan nama yang benar | Spline bila bentuk data dan ukuran sampel mendukung |
| Benchmark dua domain; hasil layanan gabungan serta per jenis | Bobot kapasitas/orde SIRS dan PDDikti |
| Kemiringan residu yang dikontrol dengan jelas; model satu tahap sebagai pemeriksa | Lapisan Google bila keluaran memenuhi syarat penggunaan |
| Perbandingan domain pada sampel yang sama; diagnostik dan beberapa pemeriksaan ketahanan terarah | Tampilan Web GIS yang lebih rumit setelah keluaran inti selesai |
| Profil penghasilan, biaya, dan waktu pada tingkat sumbernya | Eksplorasi what-if dengan baseline tetap dan batas interpretasi |

Web GIS dan what-if tetap berada dalam kerangka yang disepakati. Urutan ini hanya memastikan implementasi media dan modul tambahan tidak mendahului kepastian metode inti. Tidak diperlukan pembelian mikrodata, panel fungsi lengkap, metropolitan pembanding baru, atau strategi kausal yang belum tersedia.

## Urutan perbaikan dan perkiraan usaha

1. **Koreksi makna estimand dan rumus:** C1–C4, sekitar 4–7 jam untuk keputusan metode dan penyelarasan teks.
2. **Kunci aturan ketidakpastian dan gerbang lintas tingkat:** C5–C6 serta I3–I8, sekitar 6–10 jam; dapat lebih lama bila diperlukan konsultasi statistik.
3. **Perjelas konstruksi domain dan status Google:** C7, I1–I2, I9–I10, sekitar 3–6 jam untuk rancangan dan dokumentasi, di luar akuisisi baru.
4. **Pangkas pengulangan dan patuhi template:** F1–F5, sekitar 5–9 jam termasuk pemeriksaan visual.

Total indikatif **18–32 jam revisi naskah dan rancangan**, bukan estimasi penyelesaian seluruh analisis Bab 5 atau jaminan waktu. Jangan menjalankan semua model lebih dulu kemudian memilih rancangan yang menghasilkan label paling menarik.

## Pola penulisan yang perlu diperbaiki

- **Data-Dumper:** terbatas pada Tabel 2.1 yang panjang; isi celah berulang lebih sering menambahkan katalog daripada memperjelas perdebatan.
- **Jargon-Hider:** tidak dominan pada narasi awal, tetapi tumpukan “gerbang”, “cadangan bernama”, “manifest”, “spesifikasi kembar”, dan skenario dapat menutupi tiga operasi utama: mengukur hubungan, mengukur fungsi relatif, dan menguji asosiasi.
- **Citation-Stuffer:** tidak menjadi masalah utama. Latar belakang justru perlu lebih ringkas dan sitasi yang menentukan keputusan metode perlu diberi peran jelas.
- **Passive-Voice Abuser:** tidak menjadi masalah prioritas. Tidak dilakukan penghitungan otomatis rasio kalimat pasif; audit tidak mengklaim angka gaya yang tidak diukur.

## Provenance dan ketidakpastian yang masih terbuka

- Panduan TGA yang tersimpan berasal dari dokumen dengan metadata pembuatan 2023; template bertajuk 2026. Ketentuan yang dibahas diverifikasi dari bahan lokal tersebut, bukan jaminan tidak ada edaran prodi yang lebih baru. Judul/subjudul tetap fleksibel menurut template dan arahan pembimbing.
- Makna proporsi WSM pada kecamatan inti tetap merupakan inferensi yang belum dijelaskan eksplisit oleh publikasi. Interaksi status inti membantu membaca perbedaan, tetapi tidak menyelesaikan validitas pengukuran dengan sendirinya.
- Catatan sumber WSM, Komuter 2023, GHSL, Kemenperin, dan keputusan metode dibaca secara terarah. Dokumentasi GHSL §2.3 diperiksa dari PDF yang terdapat dalam ZIP sumber. Bagian metode artikel Burger dkk. 2015 diperiksa dari teks sumber lokal; seluruh bibliografi dan seluruh tabel asli BPS tidak diverifikasi ulang pada audit ini.
- Bibliografi hukum dan syarat Google diperiksa pada sumber primer daring. Kritik keterbalikan residu dan perbedaan penyebut merupakan penalaran matematis audit, bukan pernyataan temuan empiris Jakarta.
- Jumlah 43 pusat berbasis massa dan ringkasan zonal dibaca dari Bab 4 serta catatan sumber/skrip. Tidak dilakukan penghitungan ulang seluruh raster atau estimasi Q3. Karena itu, audit tidak menyatakan besar, tanda, atau signifikansi hasil penelitian yang belum dihitung.
- Nilai 0,00 pada tabel volume yang dibulatkan belum diperlakukan sebagai nol tepat. Kesalahan rumus untuk nol tetap perlu dicegah sebelum eksekusi.
- Berkas `RTK.md` yang dirujuk instruksi tidak ditemukan pada lokasi vault dan lokasi konteks yang diperiksa; audit menerapkan AGENTS.md yang tersedia dan tidak mengarang isi RTK.
- Relevansi Topic Notes telah diperiksa. Router yang ada untuk Urban Cannibalism berfokus pada GKS dan tidak memerlukan perubahan untuk audit versi ini; tidak dibuat router atau taksonomi baru.
- Semua usulan substansi dalam laporan ini merupakan **usulan AI untuk dinilai penulis**, bukan posisi intelektual baru pengguna atau temuan yang telah terbukti.

## Bahan yang digunakan

- [PDF yang diaudit](</Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/latex/tga_pwk_jakarta_bab_1_4_2026_10_03.pdf>).
- [Keputusan pengguna dan batas rancangan](</Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/output/naskah/todo_revisi_bab_1_4.md>), bagian awal dan §9.2.
- [Panduan TGA](</Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/source/official-document/Panduan_TGA[1].pdf>), terutama Format Penulisan.
- [Template TGA Penelitian 2026](</Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten/source/official-document/Template TGA Penelitian 2026.docx>), §1.1, petunjuk tabel/gambar, serta pengaturan dokumen.
- Catatan sumber BPS WSM 2024, Komuter 2023, GHSL R2023A, dan Kemenperin 2025 di vault; skrip `latex/figures/scripts/zonal.py` dan `maps.py`.
