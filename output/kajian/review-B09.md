## Summarized Abstract
**Temuan sumber:** Artikel ini memperkenalkan metode untuk mengidentifikasi sub-pusat metropolitan berdasarkan pendekatan interaksi yang menggunakan arus komuter. Hasilnya dibandingkan dengan pendekatan berbasis kepadatan pekerjaan dan/atau ambang ukuran pekerjaan. Metode diterapkan pada kawasan metropolitan (MA) Roma dan Milan; menurut hasil artikel, metode yang diajukan memiliki kesesuaian yang lebih baik daripada pendekatan berbasis kepadatan pekerjaan. Hasil identifikasi sangat sensitif terhadap metode dan, sampai tingkat tertentu, terhadap konsep pusat yang digunakan. [Abstrak, hlm. 177]

**Interpretasi penulis:** Identifikasi sub-pusat perlu memperhatikan dimensi fungsional, bukan hanya konsentrasi morfologis pekerjaan. [Abstrak; Introduction, hlm. 177]

## Problem Statement
**Temuan sumber:** Struktur spasial kawasan metropolitan semakin kompleks; pekerjaan tersebar ke seluruh wilayah, sementara eksternalitas aglomerasi melampaui satu inti perkotaan. Identifikasi sub-pusat disebut sebagai langkah awal untuk memahami organisasi spasial metropolitan, tetapi riset empiris terutama masih menggunakan kepadatan pekerjaan, meskipun perhatian terhadap polisentrisitas fungsional meningkat. Penulis juga menyatakan bahwa pengukuran dampak polisentrisitas terhadap kinerja ekonomi metropolitan masih kurang diteliti secara empiris. [Introduction, hlm. 177]

**Interpretasi penulis:** Masalah metodologisnya adalah kurangnya alat identifikasi sentralitas metropolitan yang menggunakan ukuran interaksi untuk melengkapi atau menggantikan ukuran berbasis kepadatan. Perbandingan langsung antara pendekatan interaksi dan kepadatan juga dinilai masih kurang. [Introduction, hlm. 177]

## Objectives
**Temuan sumber:** Tujuan artikel adalah mengusulkan pendekatan metodologis untuk mengidentifikasi sub-pusat metropolitan, menerapkannya pada MA Roma dan Milan, serta membandingkan hasilnya dengan dua metode lain yang berbasis kepadatan dan ukuran pekerjaan. [Introduction, hlm. 177]

**Interpretasi penulis:** Pendekatan tersebut dimaksudkan untuk mengisi kesenjangan dalam deskripsi struktur perkotaan dengan mengidentifikasi sentralitas melalui relasi fungsional antarnode. [Introduction, hlm. 177]

## Literature Survey
**Temuan sumber:** Tinjauan membedakan metodologi statis/morfologis dari metodologi interaksi. Metode morfologis yang dibahas meliputi ambang pekerjaan dan kepadatan Giuliano dan Small, rasio pekerjaan terhadap pekerja penduduk (E/R) Shearmur dan Coffey, puncak kepadatan lokal, residu model ekonometrik kepadatan, kernel density, serta Local Indicators of Spatial Autocorrelation (LISA). Literatur interaksi menggunakan data arus, terutama arus komuter, untuk membaca hubungan dan posisi node dalam jaringan metropolitan. [Literature review, hlm. 178–180]

**Temuan sumber:** Kerangka teoretis artikel terutama terkait teori central place, yang menekankan hierarki fungsi antarnode. Literatur network of cities yang menekankan relasi horizontal dan spesialisasi antarpusat juga dibahas, tetapi penulis menilai teori central place tetap relevan untuk satu MA. Pendekatan morfologis dan fungsional tidak selalu bertentangan; studi ESPON yang dirujuk menggabungkan ukuran, lokasi, dan konektivitas. [Literature review, hlm. 179–180]

**Interpretasi penulis:** Perbedaan metode berakar pada perbedaan konsep pusat: kepadatan dan ukuran pekerjaan menangkap nodalitas absolut, sedangkan penyediaan fungsi dan pekerjaan melebihi permintaan penduduk menangkap sentralitas relatif terhadap wilayah sekitar. [Literature review, hlm. 179–180]

## Method Used
**Temuan sumber:** Unit analisis yang dipilih adalah tingkat perkotaan; sub-pusat dipilih dari seluruh munisipalitas yang berada dalam MA. Italia belum memiliki definisi resmi MA, sehingga batas MA diambil dari Boix dan Veneri (2009), yang menggunakan algoritme yang terinspirasi metodologi US Federal Register 1990. [Methods and data, hlm. 180]

**Temuan sumber:** MA dimodelkan sebagai jaringan dengan munisipalitas sebagai node dan arus komuter sebagai link. Untuk setiap munisipalitas dihitung flow-centrality ratio (FCi), yaitu perbandingan in-degree terhadap out-degree, dan directional dominance index (DIIi), yaitu ukuran keterlibatan node yang membandingkan perjalanan masuk dengan rata-rata perjalanan masuk dalam MA. Munisipalitas dengan FCi dan DIIi lebih besar dari 1 diperlakukan sebagai kandidat sub-pusat tingkat kedua. [Methods and data, hlm. 180–181]

**Temuan sumber:** Selanjutnya dihitung productive completeness (PCi), yaitu rasio jumlah sektor lima digit dengan sedikitnya satu pekerjaan pada 2001 di suatu munisipalitas terhadap rata-rata jumlah sektor lima digit dalam MA. Munisipalitas dengan FCi > 1, DIIi > 1, dan PCi > 1 dipilih sebagai sub-pusat metropolitan tingkat pertama. Node yang terpilih dan bersebelahan digabungkan berdasarkan kontiguitas dan interaksi; agregatnya harus memiliki self-containment arus komuter sekurang-kurangnya 15%. [Methods and data, hlm. 180–181; catatan kaki 4, hlm. 181]

**Temuan sumber:** Hasil tersebut dibandingkan dengan metode Giuliano–Small (GS), yang memakai sedikitnya 10.000 pekerjaan dan kepadatan sedikitnya 10 pekerjaan per acre, serta metode Shearmur–Coffey (SC), yang memakai rasio E/R > 1 dan sedikitnya 5.000 pekerjaan. Evaluasi kesesuaian dilakukan dengan mengestimasi fungsi kepadatan pekerjaan polisentris: bentuk eksponensial negatif logaritmik dan model gravitasi logaritmik, kemudian membandingkan adjusted R2. [Empirical findings, hlm. 181–183; Evaluation of methods, hlm. 183–184]

## Dataset
**Temuan sumber:** Data arus komuter antarmunisipalitas berasal dari Istituto Nazionale di Statistica (Istat) dan menggunakan data 2001. Untuk setiap MA tersedia matriks yang memuat jumlah komuter dari setiap munisipalitas ke semua munisipalitas lain dalam MA. PCi menggunakan data Sensus Istat dengan klasifikasi sektoral NACE, pada tingkat sektor lima digit dan tahun 2001. [Methods and data, hlm. 180–181]

**Temuan sumber:** Evaluasi kepadatan menggunakan kepadatan pekerjaan bruto per kilometer persegi pada setiap munisipalitas serta jarak dari CBD dan sub-pusat terkonsolidasi; sumber tidak memberikan uraian dataset terpisah untuk setiap variabel evaluasi tersebut. Nama sumber dan periode tambahan untuk variabel evaluasi: Tidak disebutkan dalam file. [Evaluation of methods, hlm. 183–184]

## Population / Sample
**Temuan sumber:** Populasi analisis adalah seluruh munisipalitas dalam dua MA yang dipilih. Tabel 1 mencatat 200 observasi untuk Roma dan 597 observasi untuk Milan pada masing-masing indikator FCi, DIIi, dan PCi. [Table 1, hlm. 181]

**Temuan sumber:** Desain sampel probabilistik, responden individu, atau survei sampel: Tidak disebutkan dalam file. Unit observasinya adalah munisipalitas dan arus di antara munisipalitas. [Methods and data, hlm. 180–181]

## Dependent Variables
**Temuan sumber:** Variabel dependen tunggal konvensional pada tahap identifikasi: Tidak disebutkan dalam file. FCi, DIIi, dan PCi adalah indikator seleksi sub-pusat. Pada tahap evaluasi, variabel yang dijelaskan dalam persamaan adalah D, yaitu kepadatan pekerjaan bruto per kilometer persegi di setiap munisipalitas; jarak dari CBD dan sub-pusat digunakan dalam fungsi kepadatan eksponensial dan gravitasi. [Methods and data, hlm. 180–181; Evaluation of methods, hlm. 183]

**Interpretasi pengolahan:** Dengan demikian, keluaran utama tahap identifikasi adalah status/kumpulan sub-pusat, sedangkan adjusted R2 pada tahap evaluasi dipakai untuk membandingkan seberapa besar metode identifikasi menjelaskan variasi kepadatan pekerjaan. Ini adalah pembacaan struktur analisis dari persamaan dan uraian sumber, bukan istilah variabel dependen yang dipakai sebagai judul analisis oleh penulis. [Evaluation of methods, hlm. 183–184]

## Results
**Temuan sumber:** Statistik deskriptif pada Tabel 1 mencatat hal berikut. Untuk Roma, FCi memiliki 200 observasi, minimum 0,02, maksimum 4,62, mean 0,38, dan simpangan baku 0,51; DIIi memiliki rentang 0,00–195,94, mean 1,49, dan simpangan baku 13,88; PCi memiliki rentang 0,02–2,02, mean 0,33, dan simpangan baku 0,31. Untuk Milan, FCi memiliki 597 observasi, rentang 0,00–4,63, mean 0,58, dan simpangan baku 0,47; DIIi memiliki rentang 0,00–235,07, mean 1,11, dan simpangan baku 9,71; PCi memiliki rentang 0,01–2,01, mean 0,37, dan simpangan baku 0,28. [Table 1, hlm. 181]

**Temuan sumber:** Pendekatan fungsional mengidentifikasi empat munisipalitas pusat di Roma dan mengonsolidasikannya menjadi tiga sub-pusat berdasarkan kontiguitas dan interaksi. Tabel A.1 mencantumkan Rome, Pomezia, Latina, dan Civitavecchia; Tabel 2 menampilkan hasil pusat terkonsolidasi sebagai Rome, Latina, dan Civitavecchia. Di Milan, 11 munisipalitas diidentifikasi dan diagregasikan menjadi sembilan sub-pusat terkonsolidasi. Tabel A.1 mencantumkan Milan, Como, Pavia, Crema, Lodi, Segrate, Saronno, Trezzano sul Naviglio, Cantù, Legnano, dan Monza; Tabel 2 menampilkan agregasi tersebut dengan Milan terdiri atas tiga munisipalitas dan pusat lain masing-masing satu. [Empirical findings, hlm. 181; Table 2, hlm. 181; Table A.1, hlm. 184]

**Temuan sumber:** Dengan metode SC, 35 munisipalitas di MA Milan dan enam munisipalitas di MA Roma memenuhi syarat awal, lalu diagregasikan masing-masing menjadi 15 dan tiga sub-pusat terkonsolidasi. Dengan metode GS, tidak ada sub-pusat yang teridentifikasi di Roma, sedangkan di Milan ditemukan satu sub-pusat yang terdiri atas tiga munisipalitas. [Evaluation of methods, hlm. 182–183; Table 2, hlm. 181; Table A.1, hlm. 184]

**Temuan sumber:** Adjusted R2 untuk bentuk log eksponensial di Roma adalah 0,525 dengan metode fungsional dan 0,393 dengan SC; di Milan nilainya 0,671 dengan metode fungsional, 0,674 dengan SC, dan 0,426 dengan GS. Untuk bentuk log gravitasi, nilainya di Roma adalah 0,546 dengan metode fungsional dan 0,396 dengan SC; di Milan 0,703 dengan metode fungsional, 0,711 dengan SC, dan 0,414 dengan GS. [Table 3, hlm. 183]

## Findings
**Temuan sumber:** Peta dan uraian artikel menggambarkan Milan sebagai struktur yang lebih polisentris, dengan beberapa node pusat mengelilingi munisipalitas pivot, sedangkan Roma memiliki lebih sedikit node pusat dan peran munisipalitas pivot yang lebih menonjol. [Empirical findings, hlm. 181; Fig. 1–2, hlm. 181–182]

**Interpretasi penulis:** Pendekatan fungsional lebih restriktif daripada SC karena mencari node dengan sentralitas neto positif dan kapasitas sebagai pemasok fungsi, bukan sekadar node berkepadatan pekerjaan tinggi di sekitar pivot. Untuk Roma, pendekatan fungsional menjelaskan varians kepadatan pekerjaan jauh lebih besar daripada SC; pada kedua spesifikasi, selisih adjusted R2 sekurang-kurangnya 13,2 poin persentase. Untuk Milan, metode fungsional dan SC menjelaskan bagian varians yang secara substantif serupa, sedangkan GS menghasilkan nilai yang lebih rendah. [Evaluation of methods, hlm. 182–183]

**Interpretasi penulis:** Hasil identifikasi sub-pusat bergantung kuat pada metode yang dipakai dan konsep pusat yang hendak diukur. Perbandingan adjusted R2 juga dapat dipengaruhi oleh struktur data, termasuk ukuran dan jumlah unit spasial, fungsi yang dipilih, serta struktur perkotaan aktual. [Evaluation of methods, hlm. 183–184]

## Conclusions
**Interpretasi penulis:** Penulis menyimpulkan bahwa metode fungsional yang diusulkan bekerja baik secara teoretis dan empiris serta memberikan kesesuaian yang lebih baik ketika fungsi kepadatan pekerjaan polisentris diestimasi. Pendekatan ini dinilai lebih tepat untuk pusat-pusat dalam MA Italia yang terbentuk melalui koalesensi, sedangkan ukuran kepadatan lebih dekat dengan gagasan desentralisasi pekerjaan dari CBD yang padat. [Concluding remarks, hlm. 183–184]

**Interpretasi penulis:** Metode GS dinilai tidak memadai dalam konteks metropolitan Italia, terutama ketika ambangnya tidak diperbarui berdasarkan pengetahuan lokal. Pilihan metode harus bergantung pada apakah analisis diarahkan pada polisentrisitas morfologis atau fungsional. [Concluding remarks, hlm. 184]

## Contributions
**Temuan sumber:** Artikel mengusulkan prosedur yang menggabungkan unsur interaksi dan fungsi: FCi serta DIIi untuk relasi dan dominasi arus, lalu PCi untuk kelengkapan struktur sektoral. Prosedur itu mengidentifikasi node tanpa menetapkan ambang absolut populasi atau pekerjaan. Penulis menyatakan bahwa karya ini berkontribusi pada literatur tentang pendekatan yang menilai sentralitas melalui fungsi dan pekerjaan yang disediakan melebihi jumlah yang diminta penduduk sekitar. [Methods and data, hlm. 180–181; Concluding remarks, hlm. 184]

**Interpretasi pengolahan:** Kontribusi metodologis yang dapat diidentifikasi dari TXT adalah menjadikan konsep pusat fungsional dapat dibandingkan secara eksplisit dengan dua prosedur berbasis ambang dalam dua MA Italia. [Introduction, hlm. 177; Empirical findings, hlm. 181–183]

## Research Gap
**Temuan sumber:** Penulis menyatakan bahwa perhatian terhadap relasi fungsional antarnode di dalam MA telah meningkat, tetapi jauh lebih sedikit penelitian yang mengidentifikasi sentralitas metropolitan memakai ukuran interaksi sebagai pengganti pendekatan berbasis kepadatan. Studi komparatif antara hasil kedua pendekatan tersebut juga disebut masih kurang. Selain itu, topik pengaruh polisentrisitas terhadap kinerja ekonomi metropolitan dinyatakan masih kurang diteliti secara empiris. [Introduction, hlm. 177]

**Inferensi pengolahan/batas klaim:** Ini adalah kesenjangan yang dirumuskan penulis dalam artikel; TXT tidak menyediakan tinjauan sistematis dengan protokol pencarian yang memungkinkan verifikasi independen atas kelengkapan klaim tersebut. [Introduction; Literature review, hlm. 177–180]

## Limitations
**Temuan sumber:** Penulis menyebut ketersediaan data sebagai batasan serius: data arus biasanya tidak seluas dan tidak sesering diperbarui seperti data stok. Masalah unit areal yang dapat dimodifikasi (MAUP) dapat muncul karena tingkat spasial analisis bergantung pada tingkat tempat data fungsional seperti komuter tersedia. [Concluding remarks, hlm. 184]

**Temuan sumber:** Jumlah sektor lima digit hanya merupakan pendekatan terhadap fungsi ekonomi yang disediakan pusat; hubungan antara klasifikasi NACE dan fungsi ekonomi perlu diteliti lebih lanjut, walaupun hal itu bukan tujuan artikel. Penulis juga mencatat bahwa metode berbasis ambang sulit diterapkan lintas konteks karena perbedaan struktur permukiman dan unit spasial yang tersedia. [Methods and data, hlm. 181; Concluding remarks, hlm. 184]

**Temuan sumber:** Arus komuter pekerjaan tidak mencakup seluruh pergerakan untuk konsumsi, studi, dan rekreasi. Karena itu, kandidat awal dari FCi dan DIIi disebut sub-pusat tingkat kedua, dan PCi diperlukan untuk menangkap seperangkat fungsi perkotaan yang lebih luas. [Methods and data, hlm. 180–181]

## Challenges
**Temuan sumber:** Tantangan metodologis yang dibahas dalam TXT meliputi pemilihan tingkat spasial ketika data arus hanya tersedia pada unit tertentu, penentuan ambang yang dapat bersifat diskresioner, serta penggabungan munisipalitas yang bersebelahan menjadi pusat terkonsolidasi dengan syarat interaksi dan self-containment minimal 15%. [Literature review, hlm. 178; Methods and data, hlm. 180–181]

**Temuan sumber:** Perbandingan antarhasil juga menghadapi persoalan bahwa ambang GS berasal dari struktur wilayah Los Angeles dan diterapkan pada unit yang berbeda dari munisipalitas Italia. SC dapat memilih munisipalitas di sabuk pertama dan kedua yang memiliki banyak pekerjaan karena kedekatannya dengan pivot, meskipun belum tentu merupakan pusat fungsional. [Empirical findings, hlm. 181–183]

## Practical Implications
**Interpretasi penulis:** Identifikasi sub-pusat memberi pengetahuan tentang organisasi spasial metropolitan yang diperlukan untuk kebijakan tata ruang. Hasil identifikasi juga dapat membantu mengenali tempat yang menjadi prioritas investasi publik dan tempat yang membentuk efek aglomerasi di dalam wilayah. [Introduction, hlm. 177]

**Interpretasi pengolahan:** Alat pengukuran struktur perkotaan yang lebih andal diperlukan untuk menguji efek polisentrisitas terhadap kinerja ekonomi metropolitan, tetapi artikel ini terutama mengusulkan dan mengevaluasi metode identifikasi, bukan mengestimasi efek kebijakan tersebut. [Introduction, hlm. 177; Concluding remarks, hlm. 184]

## Applications
**Temuan sumber:** Metode diterapkan pada seluruh munisipalitas dalam MA Roma dan Milan menggunakan arus komuter 2001, lalu hasilnya dibandingkan dengan GS dan SC. Aplikasi lain di luar dua MA tersebut tidak disebutkan dalam file. [Methods and data, hlm. 180–181; Empirical findings, hlm. 181–183]

## Future Research (Optional)
**Temuan sumber:** Penulis mengusulkan penelitian lanjutan untuk menguji apakah terdapat jenis sub-pusat yang berbeda menurut asal pembentukannya, yaitu desentralisasi atau koalesensi, dan apakah jenis tersebut menghasilkan dampak yang berbeda terhadap struktur metropolitan. Penulis juga mengusulkan pengkajian hubungan antarsub-pusat serta apakah fungsi mereka bersifat alternatif atau komplementer, dengan mengeksplorasi koneksi konsumsi, rekreasi, dan pertukaran antarperusahaan. [Concluding remarks, hlm. 184]

## Provenance Notes
**Catatan verifikasi:** Hanya satu TXT aktual berprefiks B09 ditemukan di bawah `source/`, yaitu `source/journal/B09-veneri-2013-the-identification-of-sub-centres-in-two-italian-metropolitan-areas-a-functional-approach-10.1016-j.cities.2012.04.006.txt`. Nama tersebut cocok dengan artikel Paolo Veneri, “The identification of sub-centres in two Italian metropolitan areas: A functional approach,” *Cities* 31 (2013), hlm. 177–185, DOI `10.1016/j.cities.2012.04.006`. [Metadata artikel dan halaman 177–185]

**Catatan ekstraksi:** TXT memuat seluruh teks yang tersedia dari 617 baris, termasuk blok `[PDF Metadata]`, teks artikel, Appendix A, dan References. Metadata menyebut PDF sumber `journal/B09-veneri-2013-the-identification-of-sub-centres-in-two-italian-metropolitan-areas-a-functional-approach-10.1016-j.cities.2012.04.006.pdf`, diekstrak pada 2026-08-31 dengan `pdftotext -layout`; PDF berjumlah 9 halaman, tidak terenkripsi, berukuran 595.276 x 793.701 pts, berukuran 617632 bytes, dan versi PDF 1.7. Metadata juga menyatakan Custom Metadata: no, Metadata Stream: yes, Tagged: no, UserProperties: no, Suspects: no, Form: none, JavaScript: no, dan Optimized: no. [PDF Metadata, baris 1–20]

**Batasan evidence:** Klaim review ini hanya diproses dari TXT B09 tersebut. Ekstraksi memiliki artefak kecil berupa ligatur/karakter rumus dan susunan dua kolom pada beberapa bagian, tetapi teks naratif, angka tabel, locator halaman, appendix, dan kesimpulan terbaca. TXT dan PDF sumber tidak diubah. Catatan kaki menyatakan pandangan yang disampaikan adalah pandangan penulis dan tidak selalu mencerminkan pandangan OECD. [PDF Metadata; catatan kaki, hlm. 177]
