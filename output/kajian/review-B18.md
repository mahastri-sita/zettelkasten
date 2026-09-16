# Review B18

**Sumber yang direview:** Chris Jacobs-Crisioni, Mert Kompil, dan Lewis Dijkstra (2023), *Big in the neighbourhood: Identifying local and regional centres through their network position*, *Papers in Regional Science*, 102, 421-457, DOI 10.1111/pirs.12727.

## Summarized Abstract

**Laporan sumber:** Artikel menyatakan bahwa peringkat kota pada tingkat nasional tidak cukup menggambarkan relevansi lokal dan regional suatu settlement. Penulis memperkenalkan metode untuk memeringkat centrality settlement berdasarkan waktu tempuh dan ukuran settlement, kemudian menguji hubungan antara ukuran settlement, peran sebagai pusat lokal atau regional, dan endowment layanan. Untuk EU27 dan UK, pendekatan tersebut dilaporkan dapat menjelaskan endowment layanan per kapita dengan baik dan menambahkan nuansa yang tidak ditangkap peringkat nasional. Artikel juga mengidentifikasi preferensi skala spasial beberapa jenis layanan. Hasilnya menyiratkan bahwa endowment layanan dapat terkonsentrasi ulang karena koneksi jalan yang lebih cepat, terutama di area yang lebih terkoneksi. [Abstract, pp. 421-422]

**Interpretasi penulis:** Penulis memosisikan metode tersebut sebagai heuristic pragmatis untuk menangkap hierarki Christallerian pusat-pusat layanan, bukan sebagai pengganti pengamatan lapangan atau definisi functional urban area. [Section 1, pp. 422-423; Section 5, pp. 445-446]

## Problem Statement

**Laporan sumber:** Sebagian besar kajian urbanisme dan geografi ekonomi berfokus pada kota terbesar, padahal artikel melaporkan bahwa 63% penduduk EU dan UK tidak tinggal di urban centre dan sekitar 38% penduduk EU tinggal di wilayah di luar functional urban areas. Settlement kecil, town, dan village dapat menjadi hub layanan bagi hinterland meskipun perannya dalam pasar tenaga kerja terbatas. Penyediaan layanan sosial dan ekonomi menghadapi biaya lebih tinggi di wilayah berpenduduk kecil dan tersebar, sementara informasi yang komprehensif dan harmonis tentang layanan publik serta privat di seluruh Eropa belum tersedia. [Section 1, pp. 421-422]

**Laporan sumber:** Metode berbasis ukuran nasional, distribusi ukuran kota, jaringan kota global, atau ketergantungan pasar tenaga kerja tidak memadai untuk menjelaskan fungsi penyedia layanan bagi hinterland terdekat, khususnya pada settlement kecil. Data interaksi dan point of interest yang tersedia juga memiliki keterbatasan cakupan, variasi kualitas, serta potensi bias klasifikasi, commission, dan omission. [Section 2, pp. 423-425]

**Interpretasi penulis:** Masalah inti yang hendak diatasi adalah ketidakselarasan antara ukuran penduduk sebuah settlement dan peran layanan yang sebenarnya dijalankannya dalam konteks jaringan tetangga serta waktu tempuh.

**Inferensi pengolahan:** Unit persoalan artikel bukan sekadar lokasi layanan individual, melainkan cara mengidentifikasi settlement yang berfungsi sebagai pusat pada skala waktu tertentu ketika ukuran nasional saja menyembunyikan peran lokal atau regional.

## Objectives

**Laporan sumber:** Artikel menetapkan tiga tujuan utama: (1) memperkenalkan metode berbasis waktu tempuh jalan dan jumlah penduduk settlement untuk menginferensikan klasifikasi hierarki centrality serta menyajikan hasilnya untuk EU27 dan UK; (2) memvalidasi kegunaan hierarki dengan menguji seberapa baik hierarki tersebut menjelaskan endowment lokasi layanan; dan (3) memeriksa apakah perbedaan efisiensi jaringan transportasi berhubungan dengan peringkat centrality dan endowment layanan. Layanan yang dipertimbangkan mencakup layanan ekonomi dan sosial untuk kepentingan umum. [Section 1, pp. 422-423]

**Interpretasi penulis:** Pendekatan dimaksudkan sebagai heuristic yang hanya memerlukan ukuran settlement dan konektivitas jaringan jalan, sehingga menurut penulis pada prinsipnya dapat diterapkan secara global, walaupun validasi empiris artikel dilakukan pada EU27 dan UK. [Section 1, p. 423]

## Literature Survey

**Laporan sumber:** Artikel menempatkan kajian dalam Central Place Theory (CPT) Christaller dan Losch. CPT dipakai untuk memahami sistem berulang dari cluster retail dan layanan dengan tingkat kompleksitas, spesialisasi, dan frekuensi spasial yang berbeda. Artikel membahas tiga mekanisme: preferensi konsumen atas jarak yang lebih dekat versus pilihan yang lebih kaya; keputusan penyedia layanan yang menimbang kedekatan pengguna, pesaing, critical mass, economies of scale, dan agglomeration benefits; serta pertimbangan equity dan akses dalam layanan sosial. [Section 2, pp. 423-424]

**Laporan sumber:** Kajian terdahulu yang diringkas mencakup hierarki berdasarkan ukuran kota nasional atau global, jaringan kota kontinental, data commuting untuk mengidentifikasi ketergantungan fungsional, pemodelan dinamis kemunculan hierarki, dan penggunaan ukuran penduduk sebagai proksi ukuran pasar. Artikel menyatakan bahwa commuting tidak sepenuhnya merepresentasikan seluruh fungsi layanan, data layanan yang harmonis sulit diperoleh, model hierarki sektoral sangat kompleks, dan ukuran pasar statis mengabaikan dinamika agglomeration serta biaya perjalanan. Konteks lingkungan juga membuat settlement berukuran sama dapat mempunyai peran berbeda; artikel menghubungkannya dengan gagasan bahwa kota dapat meminjam ukuran dari kota yang terkoneksi. [Sections 2.1-2.4, pp. 423-425]

**Interpretasi penulis:** Literatur tersebut mendukung pemakaian kombinasi ukuran lokal dan konteks jaringan, bukan peringkat nasional tunggal, untuk membaca hierarki pusat layanan sampai ke settlement terkecil. Metode artikel diposisikan sebagai pelengkap definisi berbasis aglomerasi pasar tenaga kerja. [Sections 2.4 and 5, pp. 425 and 445-446]

## Method Used

**Laporan sumber:** Centrality dihitung dari ukuran relatif settlement dalam radius waktu tempuh yang telah ditentukan. Untuk settlement asal i dan ambang waktu t, nilai `L(t)_i` menjadi 1 jika settlement i memiliki penduduk setidaknya sebesar setiap settlement tujuan j yang dapat dicapai dalam `T_ij < t`; jika ada settlement yang lebih besar dalam radius tersebut, nilainya 0. Ambang diuji dari 5 sampai 120 menit dengan kenaikan 5 menit. Hierarki visual settlement ditentukan dari ambang tertinggi ketika kriteria tersebut masih benar. [Section 3, pp. 425-426; Equation (1); Figures 1 and 3; Tables 1-3]

**Laporan sumber:** Settlement dibentuk dari cluster populasi berbasis grid 1 x 1 km dan digeneralisasi menjadi polygon. Matriks waktu tempuh dihitung terpisah untuk setiap negara, menggunakan topologi jaringan dan kecepatan maksimum untuk navigasi mobil, dari centroid berbobot penduduk ke centroid berbobot penduduk settlement lain yang berada dalam jangkauan dua jam berkendara. Ukuran penduduk yang dipakai dalam analisis berasal dari agregasi grid JRC-GeoStat 2018. [Section 3.1, pp. 426-427]

**Laporan sumber:** Lokasi layanan diatribusikan ke settlement melalui jarak Euclidean ke grid cell terdekat yang berada di dalam settlement. Lokasi yang berjarak lebih dari 2,5 km dari settlement terdekat tidak dihitung. Endowment diuji dengan ANOVA dan perbandingan Tukey pada tingkat kepercayaan 95% menurut tipe settlement dan kelas ukuran. [Sections 4 and 4.1-4.2, pp. 430-435; Tables 4-5 and Appendix B]

**Laporan sumber:** Regresi OLS pada Equation (2) dijalankan terpisah untuk tiap jenis layanan. Variabel terikatnya adalah `ln(Y_i + 0.01)`, dengan `Y_i` jumlah lokasi layanan; prediktornya mencakup dummy negara, `ln(P_i + 0.01)`, dummy settlement dalam 10 km dari perbatasan nasional, dummy jaringan terisolasi, dan dummy `L(t)` pada beberapa ambang waktu secara simultan. Equation (3) menambahkan normalized effective speed dan jumlah destinasi yang dapat dicapai dalam 120 menit. Settlement dengan effective speed sedikitnya 11% di atas atau di bawah rata-rata nasional juga dibandingkan. [Sections 4.3-4.4, pp. 436-445; Equations (2)-(3); Tables 7-9]

**Laporan sumber:** Klasifikasi dihitung dengan GeoDMS dan algoritme shortest-path; analisis statistik dilakukan dengan SPSS dan R. [Section 1, p. 423]

**Inferensi pengolahan:** Desain ini merupakan analisis observasional berbasis perbandingan spasial, bukan eksperimen atau evaluasi before-after. `L(t)` adalah proksi centrality yang diturunkan dari populasi dan waktu tempuh, bukan observasi langsung atas pilihan konsumen atau keputusan setiap penyedia layanan.

## Dataset

**Laporan sumber:** Dataset settlement menggunakan grid populasi sensus EU 2011 untuk delineasi derajat urbanisasi dan grid populasi JRC-GeoStat 2018 untuk jumlah penduduk settlement. Settlement yang masuk adalah cluster city, town, dan village yang terpisah secara fisik, kontinu secara spasial, serta memenuhi ambang massa dan kepadatan penduduk; area yang terlalu jarang atau tidak berpenghuni tidak dimasukkan. Data jaringan jalan dan kecepatan berasal dari database TomTom 2018. [Section 3.1, pp. 426-427]

**Laporan sumber:** Sepuluh jenis layanan dan jumlah lokasi yang tersedia serta berhasil dihubungkan ke settlement adalah: retail 189.836 dan 164.459 (86,6%); primary schools 150.633 dan 125.455 (83,3%); banks 89.546 dan 82.604 (92,2%); pharmacies 86.789 dan 79.985 (92,2%); doctors 47.822 dan 39.872 (83,4%); secondary schools 37.464 dan 35.168 (93,9%); train stations 31.156 dan 23.524 (75,5%); hospitals 10.032 dan 9.496 (94,7%); cinemas 7.800 dan 7.375 (94,6%); universities 3.958 dan 3.677 (92,9%). Angka pertama adalah total lokasi di wilayah analisis dan angka kedua adalah lokasi yang diperhitungkan setelah linkage. [Table 4, p. 432]

**Laporan sumber:** Sumber utama lokasi layanan adalah PROFECY/ESPON dan sebagian besar datanya berasal dari OpenStreetMap. Data rumah sakit ditambah dari negara anggota melalui EUROSTAT-GISCO; stasiun kereta berasal dari basis data Poelman dan Dijkstra yang diperbarui; lokasi universitas berasal dari European Tertiary Education Register. [Section 4, pp. 430-432]

## Population / Sample

**Laporan sumber:** Populasi analisis mencakup 49.470 settlement di EU27 dan UK. Tabel 2 melaporkan klasifikasi per negara; total settlement yang menjadi pusat pada 15 menit adalah 8.796, pada 45 menit 840, dan pada 90 menit 254. Pada Appendix B, komposisi tipe settlement yang dianalisis adalah 823 urban centres, 8.817 towns, dan 39.790 villages, dengan total 49.430 observasi untuk analisis layanan per 100.000 penduduk. [Table 2, p. 428; Table 3, p. 430; Appendix B, Table A1, pp. 451-452]

**Laporan sumber:** Regresi Equation (2) menggunakan `n = 49.470`; Equation (3) menggunakan `n = 49.459` karena effective speed tidak dapat dihitung untuk seluruh settlement. Analisis kelas ukuran hanya mempertahankan settlement dengan sedikitnya 25.000 penduduk dan membaginya menjadi 25.000-50.000, 50.000-100.000, 100.000-250.000, dan lebih dari 250.000 penduduk, dengan total `n = 1.675`. Perbandingan effective speed memakai 7.269 settlement berkecepatan relatif rendah dan 6.647 berkecepatan relatif tinggi. [Table 7, p. 439; Tables 8-9, pp. 443-444; Appendix B, pp. 452-454]

**Inferensi pengolahan:** Cakupan yang dilaporkan lebih menyerupai universe settlement yang berhasil diidentifikasi melalui prosedur harmonisasi daripada sampel survei. Rancangan sampling probabilistik dan tingkat respons: Tidak disebutkan dalam file.

## Dependent Variables

**Laporan sumber:** Pada Equation (2) dan Equation (3), variabel terikat `Y_i` adalah jumlah lokasi dari satu jenis layanan yang diatribusikan ke settlement i. Regresi dijalankan terpisah untuk retail, primary schools, pharmacies, banks, train stations, doctors, secondary schools, hospitals, cinemas, dan universities. Jumlah tersebut ditransformasi menjadi `ln(Y_i + 0.01)` untuk mengurangi skewness dan menghindari log dari nol. [Sections 4.3-4.4, pp. 436-445; Tables 7-8]

**Laporan sumber:** Dalam pengujian ANOVA, variabel terikat adalah jumlah lokasi layanan per 100.000 penduduk. Tipe settlement dan kelas ukuran dipakai sebagai kelompok pembanding. `L(t)` bukan variabel terikat pada regresi; ia adalah variabel penjelas berbentuk dummy yang merepresentasikan centrality pada beberapa ambang waktu. [Section 4.2, pp. 434-435; Appendix B, Tables A1 and A3]

**Inferensi pengolahan:** Artikel tidak mengukur outcome kesejahteraan, akses aktual pengguna, atau performa ekonomi secara langsung. Outcome empiris utamanya adalah endowment atau jumlah lokasi layanan yang teramati dalam data POI.

## Results

**Laporan sumber:** Klasifikasi menghasilkan 49.470 settlement. Sebanyak 8.796 settlement diklasifikasikan sebagai centre pada ambang 15 menit, 840 pada 45 menit, dan 254 pada 90 menit, masing-masing sekitar 17,8%, 1,7%, dan 0,5% dari total. Settlement berukuran besar lebih sering menjadi settlement terbesar dalam neighbourhood. Artikel menyebut lima settlement dengan penduduk kurang dari 1.000 tetap menjadi yang terbesar dalam jangkauan 120 menit; semuanya merupakan komunitas pulau yang terisolasi atau memiliki koneksi daratan yang lambat. [Section 3.2, pp. 427-430; Tables 2-3]

**Inferensi pengolahan:** Table 3 yang diekstrak menampilkan angka 6 pada baris `L(120)` untuk kelas `<1k`, sedangkan narasi Section 3.2 menyebut lima. Review mempertahankan kedua informasi tersebut sebagai ketidakkonsistenan internal dan tidak memilih salah satunya tanpa sumber tambahan.

**Laporan sumber:** Contoh Belgia memperlihatkan perbedaan antara ukuran nasional dan posisi jaringan. Antwerp berada dalam 30 menit berkendara dari Brussels yang jauh lebih besar, sedangkan Arlon yang kecil mempunyai peran layanan hinterland yang diinferensikan lebih besar. Dalam Table 6, nilai `Max L(t)` adalah 70 untuk Arlon town cluster, 120 untuk Brussels, dan 25 untuk Antwerp. Per kapita endowment Arlon town cluster lebih tinggi daripada Brussels dan Antwerp untuk banyak layanan, tetapi penulis memperingatkan bahwa hitungan penduduk Arlon town cluster hanya mencakup 12.714 penduduk, dibanding 32.093 untuk munisipalitas Arlon. [Section 3.2 and Section 4.3, pp. 428 and 436; Figure 3; Table 6]

**Laporan sumber:** Kehadiran setidaknya satu layanan meningkat seiring ukuran settlement. Sebagai contoh, primary school terdapat pada 37,2% settlement berpenduduk kurang dari 1.000 dan 99,3% settlement berpenduduk lebih dari 250.000; university masing-masing terdapat pada 0,3% dan 97,8% kelompok tersebut. [Section 4.1, pp. 434-435; Table 5]

**Laporan sumber:** ANOVA menunjukkan perbedaan yang signifikan pada endowment per 100.000 penduduk antara urban centres, towns, dan villages untuk jenis layanan yang diuji. Rata-rata per kapita lebih tinggi di villages untuk retail, banks, pharmacies, primary schools, dan doctors; towns lebih tinggi untuk secondary schools, hospitals, dan cinemas; urban centres hanya lebih tinggi untuk universities. Tukey HSD menunjukkan bahwa sebagian besar pasangan kelompok berbeda signifikan, dengan beberapa pengecualian yang dirinci di Table A2. [Appendix B, pp. 451-453; Tables A1-A2]

**Laporan sumber:** Untuk perbandingan kelas ukuran settlement dengan sedikitnya 25.000 penduduk, teks Appendix B menyatakan perbedaan signifikan untuk retail, banks, pharmacies, primary schools, secondary schools, hospitals, dan cinemas, sementara doctors dan universities tidak berbeda signifikan. [Appendix B, pp. 452-454]

**Inferensi pengolahan:** Ringkasan teks Appendix B tidak sepenuhnya cocok dengan Table A3: nilai `Sig.` banks yang terbaca adalah 0,07, train stations memiliki 0,000 tetapi tidak disebut dalam ringkasan teks, dan doctors 0,081 serta universities 0,273. Perbedaan tersebut dibiarkan terlihat, bukan direkonsiliasi secara spekulatif.

**Laporan sumber:** Pada regresi Equation (2), ukuran settlement tetap positif dan signifikan untuk semua sepuluh layanan setelah kontrol lain dimasukkan. Centrality `L(t)` menambah daya jelaskan di luar ukuran penduduk. Primary schools, retail, dan pharmacies terutama berasosiasi dengan settlement yang dominan pada ambang waktu rendah; secondary schools, banks, dan hospitals menunjukkan preferensi supralokal; cinemas dan universities lebih terkait dengan ambang tinggi. Adjusted R2 model berkisar dari 0,56 untuk primary schools sampai 0,98 untuk universities. [Section 4.3, pp. 436-441; Table 7; Figure 8]

**Laporan sumber:** Dampak perbatasan berbeda menurut layanan. Retail dan banks lebih banyak hadir dekat perbatasan, sedangkan beberapa layanan sosial lebih sedikit hadir di sana. Ketika settlement dekat perbatasan dikeluarkan, hasil variabel `L(t)` disebut tetap serupa, sehingga perbatasan memengaruhi jumlah layanan tetapi tidak tampak mengubah hierarki yang diinferensikan. [Section 4.3, pp. 438-439; Table 7 and footnote 2]

**Laporan sumber:** Train stations hampir tidak dipengaruhi peringkat lokal. Korelasi Pearson antara jumlah train stations dan layanan lain hanya 0,24-0,32. Penulis mengaitkan hal ini dengan pertimbangan jalur jaringan dan permintaan perjalanan, bukan semata-mata ukuran atau centrality settlement. [Section 4.3, pp. 438-439]

**Laporan sumber:** Pada Equation (3), effective speed yang lebih tinggi umumnya berasosiasi dengan lebih sedikit lokasi layanan, dengan pengecualian utama primary schools, train stations, dan universities yang menunjukkan koefisien positif signifikan. Efek negatif signifikan terlihat untuk banks, doctors, secondary schools, hospitals, dan cinemas; retail serta pharmacies tidak menunjukkan koefisien effective speed yang signifikan dalam Table 8. Jumlah destinasi yang terjangkau dalam 120 menit berasosiasi negatif dengan sebagian besar layanan dan positif dengan primary schools. [Section 4.4, pp. 441-445; Table 8]

**Laporan sumber:** Probabilitas menjadi local centre pada ambang 10 atau 20 menit menurun ketika effective speed lebih tinggi. Perbandingan settlement dengan effective speed sedikitnya 11% di bawah atau di atas rata-rata nasional menghasilkan pola yang campuran: secondary schools dan cinemas mempunyai ambang waktu yang relatif sama, sedangkan primary schools, retail, dan pharmacies lebih kurang sensitif terhadap ambang waktu dan tampak lebih mungkin terorganisasi menurut jarak. [Section 4.4, pp. 443-445; Table 9]

**Laporan sumber:** Pada subset settlement berpenduduk kurang dari 25.000, sebagian layanan berorde lebih tinggi, termasuk secondary schools dan cinemas, tidak lagi menunjukkan efek signifikan pada `L(t)` yang lebih tinggi. Artikel menyebut ukuran subset yang terbatas sebagai kemungkinan penjelasan. Peringkat populasi nasional sangat berkorelasi dengan ukuran penduduk dan tidak memberi daya jelas tambahan dalam model utama. [Sections 4.3-4.4, pp. 440-445; Figure 9]

**Inferensi pengolahan:** Hasil regresi mendukung hubungan asosiasional antara posisi jaringan dan jumlah layanan setelah ukuran penduduk dikontrol, tetapi tidak dengan sendirinya mengidentifikasi arah kausal antara peningkatan kecepatan jalan dan perpindahan layanan.

## Findings

**Laporan sumber:** Penulis menyimpulkan bahwa settlement yang diinferensikan memiliki peran pusat lokal atau regional memiliki lokasi layanan yang secara signifikan lebih banyak daripada settlement lain dengan ukuran sama. Hierarki yang diusulkan dinilai bermakna untuk menjelaskan service provision dan memperluas gagasan bahwa kinerja settlement bergantung pada ukuran lokal serta neighbourhood yang terkoneksi hingga settlement terkecil di EU27 dan UK. [Section 5, pp. 445-446]

**Interpretasi penulis:** Layanan beroperasi pada skala spasial yang berbeda. Dalam ringkasan Section 4.3, layanan lokal terutama mencakup primary schools, retail, dan pharmacies; layanan subregional mencakup secondary schools, banks, dan hospitals; layanan regional mencakup cinemas dan universities. Temuan ini dibaca sebagai dukungan terhadap ekspektasi CPT tentang hierarki pusat layanan. [Section 4.3, pp. 438-439; Section 5, p. 446]

**Interpretasi penulis:** Jaringan yang lebih cepat dapat menyebabkan hierarki neighbourhood menjadi lebih jarang dan layanan terkonsentrasi di area yang lebih terkoneksi. Namun, hasil perbandingan settlement berkecepatan rendah dan tinggi tidak seragam untuk semua layanan, sehingga penulis tidak memperlakukan mekanisme tersebut sebagai pola universal. [Section 4.4, pp. 443-445; Section 5, pp. 446]

**Inferensi pengolahan:** Centrality dalam artikel paling tepat dibaca sebagai kapasitas relatif suatu settlement untuk menjadi pusat layanan pada skala waktu tertentu. Ia tidak identik dengan ukuran kota, status administratif, volume perjalanan, atau akses aktual seluruh penduduk.

## Conclusions

**Interpretasi penulis:** Metode yang diperkenalkan dipandang komplementer terhadap definisi fungsional yang bertumpu pada aglomerasi pasar tenaga kerja. Metode tersebut membantu menemukan settlement kecil yang "punch above their weight" dalam penyediaan layanan dan penting bagi konteks rural. [Section 5, pp. 445-446]

**Interpretasi penulis:** Penulis menyatakan bahwa peningkatan jaringan jalan berpotensi memperkuat konsentrasi layanan apabila layanan memang diatur oleh waktu tempuh, bahkan dapat memperkuat ketergantungan pada mobil pribadi. Kesimpulan ini tetap disertai kualifikasi bahwa sebagian layanan lebih dekat dengan logika jarak dan bahwa faktor struktur spasial yang tidak terukur mungkin menjelaskan pola campuran. [Section 5, pp. 446]

**Laporan sumber:** Artikel menegaskan bahwa klasifikasi ini adalah heuristic, bergantung pada data sekunder, dan hasilnya tidak boleh dianggap sebagai pengganti field work lokal. [Section 5, p. 446]

## Contributions

**Laporan sumber:** Kontribusi metodologis artikel adalah klasifikasi hierarki centrality settlement yang menggunakan ukuran penduduk relatif dalam neighbourhood berbasis waktu tempuh jalan. Klasifikasi tersebut dihitung untuk hampir 50.000 settlement di EU27 dan UK, bukan hanya kota besar. [Sections 1 and 3, pp. 422-430]

**Laporan sumber:** Artikel memvalidasi klasifikasi dengan sepuluh kategori layanan dan menunjukkan bahwa posisi jaringan menjelaskan variasi endowment setelah ukuran penduduk dikontrol. Artikel juga memberi karakterisasi empiris tentang skala spasial layanan serta menguji kaitan endowment dengan effective speed jaringan. [Sections 4.2-4.4, pp. 434-445]

**Interpretasi penulis:** Kontribusi substantifnya adalah memperluas pembacaan tentang ketergantungan settlement pada neighbourhood terkoneksi sampai ke town dan village, serta menyediakan informasi pelengkap bagi peringkat populasi nasional dan definisi functional urban area. Hasil klasifikasi disebut tersedia secara publik melalui tautan data yang dicantumkan pada artikel. [Sections 1 and 5, pp. 422-423 and 445-446]

**Inferensi pengolahan:** Nilai tambah utama artikel berada pada operasionalisasi peran pusat layanan secara harmonis pada banyak settlement, bukan pada pengukuran langsung kualitas, keterjangkauan, atau penggunaan layanan.

## Research Gap

**Laporan sumber:** Gap yang dinyatakan adalah belum tersedianya cara universal yang memuaskan untuk menangkap fungsi penyedia layanan settlement bagi hinterland langsung. Informasi yang komprehensif, harmonis, dan cukup rinci tentang semua layanan publik serta privat di seluruh wilayah Eropa juga dinyatakan belum tersedia. Karena itu, settlement kecil yang penting bagi service provision dapat terlewat jika klasifikasi hanya memakai ukuran penduduk nasional atau ketergantungan pasar tenaga kerja. [Sections 1 and 2.4, pp. 422 and 425]

**Laporan sumber:** Artikel masih menyisakan kebutuhan untuk memahami peran struktur spasial dan keputusan lokasi layanan dengan lebih baik, terutama karena respons terhadap travel time berbeda antara layanan dan antara settlement dengan effective speed rendah atau tinggi. [Section 5, p. 446]

**Inferensi pengolahan:** Karena analisis yang dilaporkan menggunakan perbandingan spasial dan cross-sectional differences, dampak kausal perubahan jaringan jalan terhadap relokasi layanan belum ditetapkan oleh artikel. Ini merupakan batas evidence untuk membaca dugaan "reshuffling", bukan temuan kausal baru.

## Limitations

**Laporan sumber:** Penulis menyebut metode sebagai heuristic dan mengakui bahwa metode tersebut tidak memasukkan banyak faktor relevan, termasuk historical inertia. Ukuran penduduk dan waktu tempuh jalan berasal dari data sekunder dan dapat menyimpang dari kondisi praktik. Validasi terutama bergantung pada data crowdsourced yang mungkin mengandung commission error, omission error, perbedaan klasifikasi, dan perbedaan eligibility antarnegara, zona bahasa, atau wilayah. [Section 4, pp. 430-432; Section 5, p. 446]

**Laporan sumber:** Settlement dianalisis sebagai cluster polygon, sehingga ukuran settlement tidak selalu sama dengan ukuran pasar atau populasi munisipalitas. Contoh Arlon menunjukkan bahwa 12.714 penduduk pada town cluster kurang dari setengah 32.093 penduduk munisipalitasnya, sedangkan batas Brussels dan Antwerp mencakup beberapa munisipalitas. [Section 4.3, p. 436; Table 6]

**Laporan sumber:** Lokasi layanan yang lebih dari 2,5 km dari settlement terdekat tidak diperhitungkan. Hanya 75,5% train stations yang berhasil dihubungkan menurut Table 4; artikel menjelaskan bahwa sebagian rail stops di lokasi terpencil mungkin melayani wilayah yang lebih luas. Data transportasi publik komprehensif berskala Eropa juga tidak tersedia dalam studi ini, sehingga train station hanya menjadi indikator kasar transportasi publik. [Sections 4 and 4.1-4.3, pp. 430-441; Table 4]

**Laporan sumber:** Matriks travel time dibuat terpisah per negara. Dengan demikian, peran settlement pusat terhadap service endowment lintas batas tidak dimasukkan ke dalam matriks utama, walaupun kedekatan ke perbatasan diuji sebagai variabel kontrol. [Section 3.1, pp. 426-427; Section 4.3, pp. 438-439]

**Laporan sumber:** Hasil pada subset settlement kecil kehilangan signifikansi untuk sebagian layanan berorde lebih tinggi; artikel mengaitkannya secara kemungkinan dengan ukuran subset yang terbatas. Hasil perbandingan effective speed juga campuran, sehingga tidak semua layanan dapat diperlakukan mengikuti travel time secara seragam. [Section 4.3-4.4, pp. 440-445]

**Inferensi pengolahan:** Outcome berbasis jumlah lokasi POI tidak cukup untuk menyimpulkan bahwa penduduk benar-benar memakai layanan tersebut, memperoleh akses yang setara, atau mengalami peningkatan kesejahteraan. Artikel juga tidak melaporkan observasi longitudinal before-after untuk perubahan jaringan jalan.

## Challenges

**Laporan sumber:** Tantangan identifikasi adalah menentukan settlement sebagai node tempat penyedia layanan secara masuk akal dapat berlokasi, ketika fasilitas sering berada di luar batas settlement. Penulis harus melakukan linkage ke grid cell terdekat, menetapkan batas 2,5 km, dan menangani lokasi terpencil seperti rail stops yang mungkin melayani hinterland lebih luas. [Sections 3.1 and 4.1, pp. 426-427 and 432-434]

**Laporan sumber:** Ketiadaan data konsumsi barang dan layanan yang komprehensif serta harmonis membuat fungsi settlement tidak dapat diidentifikasi langsung dari interaksi aktual. Pemodelan dinamis hierarki layanan juga dipandang terlalu kompleks untuk tujuan identifikasi yang mencakup banyak sektor dan distribusi penduduk Eropa yang tidak seragam. [Section 2.4, pp. 424-425]

**Laporan sumber:** Penulis menghadapi variasi lintas negara dalam kualitas dan cakupan POI, persoalan interaksi lintas batas, serta korelasi tinggi antara jarak dan waktu tempuh yang menyulitkan pembandingan kedua prinsip pengorganisasian layanan. Effective speed juga tidak dapat dihitung untuk seluruh settlement. [Sections 3.1 and 4.4, pp. 426-427 and 441-445]

**Inferensi pengolahan:** Tantangan analitis terbesar adalah memisahkan pengaruh ukuran penduduk, posisi jaringan, jarak, dan kualitas data POI ketika seluruhnya saling berkaitan secara spasial. Model kontrol mengurangi masalah tersebut, tetapi tidak menghapusnya.

## Practical Implications

**Interpretasi penulis:** Hasil dapat membantu mengarahkan investasi untuk territorial cohesion dan memprioritaskan settlement dalam rencana tata ruang strategis nasional maupun regional. Metode ini juga disebut dapat membantu zoning lokal dan regulasi lalu lintas dengan mengidentifikasi peran teritorial settlement, termasuk settlement kecil yang menjadi pusat layanan rural. [Section 5, pp. 445-446]

**Laporan sumber:** Penulis memperingatkan bahwa peningkatan kecepatan jaringan dapat mengurangi peran central settlement pada skala waktu rendah dan berpotensi memusatkan layanan di area yang lebih terkoneksi. Jika layanan memang terorganisasi menurut travel time, kebijakan mempercepat jaringan dapat memperkuat ketergantungan pada mobil pribadi; karena itu hasil tidak boleh dibaca sebagai alasan otomatis untuk mempercepat semua koneksi. [Sections 4.4 and 5, pp. 443-446]

**Inferensi pengolahan:** Untuk keputusan praktis, `L(t)` lebih aman digunakan sebagai alat screening awal untuk calon pusat layanan, lalu diverifikasi dengan kondisi lapangan, data layanan lokal, dan moda transportasi selain mobil.

## Applications

**Laporan sumber:** Aplikasi yang ditunjukkan artikel adalah klasifikasi centre lokal dan regional; pemetaan peran service provider settlement; perbandingan endowment layanan menurut tipe, ukuran, dan posisi jaringan; serta analisis hubungan service provision dengan effective road speed. Penulis menyatakan pendekatan pada prinsipnya dapat diterapkan secara global, tetapi hasil empiris yang disajikan hanya untuk EU27 dan UK. [Sections 1, 3, and 4, pp. 422-445]

**Interpretasi penulis:** Klasifikasi dapat melengkapi functional urban area dalam penentuan prioritas investasi territorial cohesion, spatial planning, zoning, dan traffic regulation, terutama di luar aglomerasi metropolitan. [Section 5, pp. 445-446]

**Inferensi pengolahan:** Penggunaan untuk memproyeksikan konsekuensi suatu proyek jalan atau untuk menetapkan lokasi layanan secara final memerlukan data temporal dan validasi lokal yang tidak disediakan artikel; aplikasi semacam itu tidak dapat diperlakukan sebagai hasil langsung studi.

## Future Research (Optional)

**Laporan sumber:** Artikel menyebut perlunya case studies untuk menganalisis akses spasial publik terhadap layanan secara penuh karena data public transport komprehensif berskala Eropa belum tersedia. Artikel juga menyatakan bahwa diperlukan lebih banyak penelitian untuk memahami peran struktur spasial dan keputusan lokasi layanan ketika jaringan berubah. [Section 4.3, pp. 440-441; Section 5, p. 446]

**Inferensi pengolahan:** Tidak ada agenda future research lain yang ditambahkan di luar dua arah yang disebutkan sumber.

## Provenance Notes

**Laporan sumber:** File yang diverifikasi adalah tepat satu TXT dengan prefiks `B18` di bawah `source/`: `source/journal/B18-jacobs-crisioni-kompil-dijkstra-2023-big-in-the-neighbourhood-identifying-local-and-regional-centres-through-their-network-position-10.1111-pirs.12727.txt`. Header file menunjuk ke PDF yang bersesuaian, mencatat ekstraksi pada 2026-08-31 dengan `pdftotext -layout`, dan mencatat PDF 38 halaman. [PDF Metadata, lines 1-28]

**Laporan sumber:** Seluruh rentang teks bernomor 1-1572 dibaca, termasuk metadata PDF, artikel utama, references, Appendix A-C, Table A1-A5, catatan kaki, dan abstrak bahasa Spanyol serta Jepang. Artikel yang diidentifikasi dari byline adalah Jacobs-Crisioni, Kompil, dan Dijkstra; DOI, tanggal penerimaan, jurnal, volume, dan halaman diambil dari file TXT. [lines 30-32, 41-73, 1017-1162, 1167-1543, and 1548-1572]

**Interpretasi penulis:** Batas evidence yang dinyatakan artikel sendiri dipertahankan di review ini. Tidak ada sumber luar yang digunakan atau diakses; nama karya lain hanya disebut ketika artikel TXT menggunakannya dalam literature survey atau referensi.

**Inferensi pengolahan:** `wc -l` melaporkan 1.571 newline, sedangkan pembacaan file menandai 1.572 baris karena baris terakhir tidak menjadi newline terpisah; tidak ada rentang isi yang dilewati dalam pembacaan. Artefak ekstraksi meliputi mojibake pada metadata nama penulis (`Chris Jacobsâ€ Crisioni`), karakter kontrol pada sebagian tanda minus di tabel, form-feed penanda halaman, dan beberapa tata letak tabel yang terpecah. Nama penulis dalam review mengikuti byline artikel yang terbaca sebagai `Chris Jacobs-Crisioni`.

**Inferensi pengolahan:** Artikel menyebut sepuluh service types pada bagian utama dan Tables 4, 7, serta 8, sedangkan Appendix B pada satu kalimat menyebut "nine services" meskipun tabelnya memuat sepuluh kategori. Review melaporkan sepuluh kategori dan menandai ketidakkonsistenan tersebut, bukan mengoreksinya dengan sumber luar. Ringkasan skala layanan juga memakai "up to 30 minutes" pada Section 4.3 dan "20-minute range" pada Section 5; kedua locator dipertahankan pada bagian Results tanpa dipaksakan menjadi satu angka.

**Inferensi pengolahan:** Untuk perbandingan tipe settlement, narasi Appendix B menyebut rata-rata per kapita banks lebih tinggi di villages, sedangkan Table A1 yang terbaca menunjukkan mean towns 30,10 dan villages 29,74; Table A2 juga menunjukkan perbedaan towns-villages tidak signifikan. Pernyataan narasi dan angka tabel dipertahankan sebagai dua bukti yang tidak sepenuhnya konsisten.

**Status review:** Lengkap secara struktur dan evidence untuk TXT B18 yang tersedia. Review ini tidak mengubah TXT sumber maupun PDF, tidak menangani kode lain, dan tidak membuat dokumen induk.
