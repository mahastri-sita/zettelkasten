# Audit bahasa dan humanizer oleh GPT Sol

- Auditor: **GPT Sol (GPT-6.1 Sol, OpenAI)**.
- Tanggal: 3 Oktober 2026.
- Objek: `latex/tga_pwk_jakarta_bab_1_4_final.tex`, bukan PDF atau naskah bertanggal dari versi sebelumnya.
- Cakupan: Bab 1 sampai Bab 4, termasuk teks tabel, keterangan gambar, dan lampiran dalam berkas tersebut.
- Identitas sumber: 2.055 baris; 169.991 byte; waktu modifikasi 3 Oktober 2026, 10:35:30 WIB.
- SHA-256 sumber: `a95438123f2c52c3b3288da3a5a269bf445076be3f2117040f918f3a6e847488`.
- Bentuk pekerjaan: audit dan usulan penyuntingan. Berkas `.tex` tidak diubah.

Audit ini dibuat langsung dari `.tex` final. Audit bahasa lama, `latex/audit-bahasa-tga_pwk_jakarta_bab_1_4_2026_10_03.md`, dihapus atas instruksi pengguna. Audit substansi dan audit dari model lain tidak diubah atau digunakan sebagai dasar temuan.

## 1. Kesimpulan

Naskah tidak terasa seperti terjemahan Inggris secara keseluruhan. Sebagian besar uraian empiris, terutama Bab 4, sudah cukup alami. Masalah terkonsentrasi pada penjelasan teori di Bab 2 dan aturan analisis di Bab 3.

Ada dua masalah yang perlu dibedakan:

1. Ungkapan yang terasa seperti padanan harfiah atau susunan Inggris: "manfaat dapat ditahan", "fungsi yang disandang", "membuka arah perlakuan", "tanda yang berbeda", dan "menjadi sensitivitas".
2. Tulisan yang terasa terlalu dirakit: penumpukan istilah seperti "konfigurasi bukti", "cadangan bernama", "gerbang bukti", "manifest", "dibekukan", dan "rantai dikunci". Masing-masing bisa dijelaskan, tetapi pemakaiannya secara berdekatan membuat metode terasa seperti petunjuk kerja sistem, bukan penjelasan penelitian kepada pembaca.

Perbaikan utama bukan mengganti semua istilah teknis dengan kata sehari-hari. Yang perlu diperjelas adalah pelaku, tindakan, objek yang diukur, dan alasan suatu aturan digunakan. Bahasa akhirnya tetap harus formal dan cocok untuk tugas akhir PWK.

Audit humanizer ini adalah penilaian editorial, bukan pendeteksian penulis AI. Kemiripan pola tidak membuktikan bahwa suatu kalimat berasal dari AI atau diterjemahkan dari teks Inggris. Tidak diberikan persentase "AI", persentase "terjemahan", atau skor keseluruhan yang tidak mempunyai dasar pengukuran.

### Ringkasan per bab

| Bagian | Penilaian bahasa | Fokus perbaikan |
|---|---|---|
| Bab 1 | Umumnya jelas; beberapa kalimat kontribusi dan manfaat terlalu abstrak. | Perjelas tindakan penelitian dan hilangkan ungkapan kebijakan yang kabur. |
| Bab 2 | Kesan padanan harfiah paling tampak dalam penjelasan mekanisme. | Jelaskan makna retensi manfaat, arah hubungan, dan ketergantungan dengan kalimat Indonesia yang langsung. |
| Bab 3 | Paling padat jargon prosedural dan pengulangan batas klaim. | Ganti metafora prosedural dengan aturan yang bisa dipahami; bedakan perbaikan bahasa dari keputusan metodologis. |
| Bab 4 | Relatif paling luwes karena banyak objek, angka, dan lokasi konkret. | Perjelas rasio dan pembanding; pecah paragraf penandaan pusat yang terlalu padat. |
| Lampiran | Tabelnya berguna, tetapi sejumlah judul dan frasa masih mengikuti bahasa alur kerja. | Selaraskan istilah dengan isi bab dan perjelas status data. |

## 2. Cara membaca audit

Semua lokasi di bawah adalah nomor baris pada `.tex` dengan identitas sumber di atas, bukan halaman PDF. Satu baris LaTeX dapat memuat satu paragraf panjang. Nomor baris akan berubah jika sumber disunting.

Kutipan berupa potongan teks asli; perintah LaTeX seperti `\emph{...}` dan pergantian baris dihilangkan bila tidak memengaruhi kata-katanya. Daftar temuan menggabungkan pengulangan yang memiliki masalah sama. Daftar ini bukan perintah untuk mengganti setiap kemunculan secara otomatis.

Prioritas "utama" berarti ungkapan mengganggu pemahaman atau dapat menggeser tafsir. "Menengah" berarti maknanya masih terbaca, tetapi bentuknya kaku, padat, atau berulang. "Rendah" berarti pilihan gaya yang tidak mendesak.

Pemeriksaan menggunakan `humanizer` dan `humanizer-academic-id`, dengan kalibrasi untuk tulisan akademik Indonesia. Kaidah ejaan diperiksa secara terpisah melalui rujukan EYD V lokal pada skill `indonesia-eyd-writing-skill`. Pedoman humanizer tidak diperlakukan sebagai larangan mutlak atas kata teknis, bentuk pasif, atau kalimat pembatas inferensi.

## 3. Audit bahasa yang terasa seperti terjemahan

### 3.1 Bab 1

| Baris | Kutipan | Masalah dan arah perbaikan | Prioritas |
|---|---|---|---|
| 76 | "dengan saat berlaku yang dikaitkan" | Susunannya tidak luwes. Usulan: "yang mulai berlakunya dikaitkan dengan Keputusan Presiden mengenai pemindahan ibu kota". Ini hanya usulan bahasa; ketentuan hukumnya tidak diperiksa ulang dalam audit ini. | Menengah |
| 80 | "membuat pusat sekunder tetap di bawah fungsi yang diharapkan" | Yang berada di bawah nilai harapan adalah fungsi pusat, bukan pusatnya. Usulan: "membuat fungsi pusat sekunder lebih rendah daripada yang diharapkan". Pertahankan atribusi teori dan jangan memperluasnya menjadi kesimpulan kausal penelitian. | Utama |
| 84 | "perangkaian pengukuran relasi" | Nominalisasi membuat kontribusi lebih sulit dibayangkan. Gunakan verba: penelitian "menggabungkan pengukuran relasi, tolok ukur fungsi berdasarkan massa, dan pengujian hubungan per domain". Pertahankan komponen lain dalam daftar asli. | Menengah |
| 88 | "Masalah penelitian terletak pada konfigurasi hubungan dan fungsi relatif" | Objek pertanyaan tertutup oleh kata abstrak. Lebih langsung: "Penelitian ini mengkaji bagaimana hubungan metropolitan berkaitan dengan fungsi relatif wilayah Jabodetabek di luar DKI." Jangan mengubah asosiasi menjadi pengaruh. | Menengah |
| 95, 109 | "hasil yang belum terselesaikan" | Terasa seperti penerjemahan label hasil analisis ke bahasa penyelesaian pekerjaan. Dalam pertanyaan penelitian, dapat ditulis "hasil dalam kategori tidak terselesaikan", lalu jelaskan kategorinya. Penetapan nama akhir perlu konsisten dengan tabel tipologi; lihat Bagian 5. | Menengah |
| 118 | "Penelitian memakai dua tingkat unit" | Lebih alami dan lebih sesuai uraian berikutnya: "Penelitian menggunakan dua tingkat analisis." Kecamatan dan kabupaten/kota tetap disebut sebagai unit pada masing-masing tingkat. | Menengah |
| 120; 548; 880; 1175 | "spesifikasi kembar" | Istilah pasangan model belum langsung menjelaskan penggunaannya. Usulan: "spesifikasi pembanding yang selalu dilaporkan bersama spesifikasi utama". Jangan menjadikannya pemeriksaan opsional atau menyebut indeks berbobot itu sebagai persentase komuter menuju DKI. | Utama |
| 151 | "seluruh sumber yang dipakai bersifat terbuka sehingga dapat diulang" | Rujukan "diulang" tidak jelas: sumber atau analisis? Usulan: "Keterbukaan sumber dan dokumentasi pengolahan memungkinkan analisis diulang, sejauh ketentuan penggunaan datanya mengizinkan." Keterbukaan sumber sendiri bukan jaminan reproduksi penuh. | Utama |
| 155 | "dapat membuka arah perlakuan yang lebih baik" | Kolokasi tidak lazim dan manfaatnya terlalu kabur. Usulan: "dapat membantu merumuskan penanganan yang lebih sesuai" bagi kawasan hunian yang dimaksud. Tetap sebut hasilnya diagnostik, bukan bukti efektivitas kebijakan. | Utama |

### 3.2 Bab 2

| Baris | Kutipan | Masalah dan arah perbaikan | Prioritas |
|---|---|---|---|
| 169 | "mempunyai penduduk besar" | Besar menerangkan jumlah, bukan penduduknya. Usulan: "mempunyai jumlah penduduk yang besar" atau "berpenduduk banyak". | Menengah |
| 169 | "peminjaman ukuran atau bayangan aglomerasi" | Padanan harfiah tidak langsung menerangkan konsep. Pada kalimat ini, pertahankan *borrowed size* dan *agglomeration shadow* yang memang didefinisikan sesudahnya. Padanan Indonesia boleh dipakai jika dijelaskan, bukan sebagai pengganti otomatis. | Utama |
| 173 | "berdekatan dengan banyak orang, pekerja, pemasok, pengetahuan, infrastruktur, dan amenitas" | Satu predikat kedekatan diterapkan pada orang dan objek abstrak. Susun ulang menjadi manfaat dari konsentrasi penduduk, tenaga kerja, pemasok, pengetahuan, infrastruktur, dan amenitas. Jangan menghapus mekanisme berbagi, mencocokkan, dan belajar yang dirujuk. | Menengah |
| 173 | "manfaat dan biaya bergerak bersama dengan cara yang berbeda" | Makna "bergerak" dan "cara yang berbeda" tidak dijelaskan. Nyatakan hubungan yang dimaksud: aglomerasi menimbulkan manfaat sekaligus biaya, sehingga tidak selalu memberi keuntungan bersih. Tidak perlu menggandakan "keuntungan" dengan "selalu positif". | Menengah |
| 181; 223; 233; 253; 296; 316 | "fungsi keputusan" | Terasa sebagai pemendekan dari fungsi pengambilan keputusan. Usulan: "fungsi pengambilan keputusan". Pada baris 181, susun menjadi "besar secara demografis, tetapi fungsi pengambilan keputusannya masih terbatas" agar tidak terbaca sebagai hanya menjalankan fungsi tersebut. | Menengah |
| 187; 757 sampai 759; 774 sampai 775 | "berfungsi sedikit"; "korban shadow" | Yang terbatas adalah fungsi lokal yang terukur. Sebutan korban juga menyiratkan kerugian dan sebab yang belum dibuktikan. Usulan: "berpenduduk besar tetapi memiliki fungsi lokal terbatas, sehingga tetap perlu diperiksa sebagai kandidat pola shadow". Pertahankan sifat kandidat. | Utama |
| 199 | "arah perubahan harus dipisahkan dari keberadaan infrastruktur itu sendiri" | Memisahkan objek abstrak tidak menjelaskan langkah penilaian. Usulan: "Arah perubahan struktur perlu dinilai tersendiri; keberadaan infrastruktur saja tidak menunjukkannya." Jangan menyatakan kausalitas baru dari keberadaan jaringan. | Menengah |
| 211 | "tanpa berarti apa pun tentang Jakarta" | Negasinya terlalu menyeluruh dan terdengar seperti bantahan percakapan. Usulan: "tanpa dengan sendirinya menunjukkan hubungan dengan Jakarta". Maksud bahwa tanda residu bukan bukti *shadow* tetap dipertahankan. | Utama |
| 215 | "fungsi yang disandang suatu tempat" | Metafora menyandang terasa seperti padanan harfiah. Usulan: "fungsi yang dijalankan suatu tempat". Perbandingan dengan ukuran lokal tetap perlu dinyatakan. | Menengah |
| 217; 253; 316 | "manfaat akses dapat ditahan"; "manfaat ekonomi telah tertahan"; "manfaat dapat ditahan di pusat sekunder" | Retensi manfaat belum diterangkan dalam bahasa Indonesia yang konkret. Pada baris 217, dapat ditulis "manfaat akses dapat tetap dinikmati di pusat sekunder dan dimanfaatkan untuk mengembangkan fungsi lokal". Jangan mengganti retensi manfaat dengan akses semata. | Utama |
| 227 | "Bukti empiris memperlihatkan tanda yang berbeda" | "Tanda" tidak jelas tanpa rujukan koefisien. Usulan: "Bukti empiris menunjukkan arah hubungan yang berbeda" menurut fungsi, skala, ukuran pusat, dan posisi jaringan. Jika yang dimaksud memang tanda koefisien, sebut koefisiennya. | Utama |
| 233 | "kepentingan timbal baliknya tidak seimbang" | Pembaca harus menebak siapa bergantung kepada siapa. Usulan: "hubungan tersebut lebih penting bagi pusat sekunder daripada bagi inti". Pertahankan perbedaan ketergantungan dan manfaat akses. | Utama |
| 239 | "harus diadaptasi secara terbuka terhadap data Indonesia" | Transparansi dan penyesuaian data tercampur. Usulan: "Penyesuaian definisi dan unit terhadap data Indonesia perlu dijelaskan secara terbuka." | Menengah |
| 249 | "Dari dormitori menuju pusat kegiatan pinggiran" | "Dormitori" kurang membantu pembaca memahami kawasan hunian yang bergantung pada pusat kerja lain. Usulan judul: "Dari kota tidur menuju pusat kegiatan pinggiran". Judul sumber berbahasa Inggris dalam tabel tidak ikut diubah. | Menengah |
| 253 | "menangkap pertumbuhan pekerjaan" | Terasa seperti ungkapan *capture growth*. Lebih konkret: "Pertumbuhan pekerjaan berlangsung di kawasan industri pinggiran dan membentuk spesialisasi baru." Gunakan hanya sejauh sesuai temuan sumber yang sudah dikutip. | Menengah |
| 271 | "meneruskan estafet tersebut" | Metafora umum menutupi hubungan dengan kajian sebelumnya. Usulan: "Penelitian ini melanjutkan kajian tersebut melalui tiga langkah." Tiga langkah tetap dipertahankan karena memang berbeda. | Rendah |
| 318 | "menanggung beban perjalanan pada dimensi ketiga" | Urutan dimensi memaksa pembaca kembali ke daftar sebelumnya dan dapat tertukar dengan empat lapisan mekanisme. Usulan: "sekaligus menanggung beban perjalanan". Tidak perlu menambah keterangan "tinggi" yang tidak ada dalam kalimat asal. | Menengah |
| 348 | "Persamaan ini bukan komitmen pada model kausal"; "manfaat dan beban sebagai pengukuran sejajar" | Ungkapan pertama terasa seperti *commitment to a model*; ungkapan kedua belum menjelaskan arti sejajar. Usulan: "Persamaan ini tidak dimaksudkan untuk mengidentifikasi hubungan kausal" dan "manfaat serta beban diukur secara terpisah". Jangan menghapus pembatas kausalitas. | Utama |
| 352 | "setelah inferensi kemiringan dan gerbang bukti" | Dua tahap analisis disingkat menjadi jargon. Usulan: "setelah kemiringan hubungan diestimasi dan syarat penggunaan label diperiksa". Ini perubahan bahasa, bukan penghapusan tahap pemeriksaan. | Utama |
| 379 | "Proposisi berikut berarah" | Terasa seperti padanan singkat *directional propositions*. Usulan: "Proposisi berikut menyatakan arah hubungan yang diharapkan dan hasil yang dapat membantahnya." | Menengah |

### 3.3 Bab 3

| Baris | Kutipan | Masalah dan arah perbaikan | Prioritas |
|---|---|---|---|
| 536; 572 sampai 576; 617 | "cadangan bernama"; "pemicunya ditetapkan" | Bahasa alur kerja belum menjelaskan bahwa alternatif sudah ditentukan sebelum analisis. Usulan istilah: "alternatif analisis berkode", dengan "syarat penggunaan" untuk pemicu. Kode K1 sampai K9, syarat masing-masing, dan kewajiban melaporkan perbedaan hasil tetap ada. | Utama |
| 538 | "Rantai inti penelitian dikunci" | Metafora penguncian membuat desain terdengar seperti instruksi internal. Usulan: "Spesifikasi utama penelitian ditetapkan sebagai berikut." Tetap jelaskan bahwa spesifikasi ditentukan sebelum pengolahan. | Menengah |
| 533; 641; 767; 1116; 1616 | "dibekukan" | Kata ini dapat digunakan untuk versi data, tetapi pemakaiannya berulang menambah kekakuan. Sesuaikan objek: ambang "ditetapkan sebelum klasifikasi"; nilai acuan "disimpan tanpa ditimpa"; sumber "dicatat menurut versi". Jangan menggantinya dengan "ditetapkan" saja jika aturan tidak boleh mengubah nilai ikut hilang. | Menengah |
| 626 sampai 627 | "Keterbatasan data resmi maupun nonpemerintah dinilai secara simetris" | Terasa seperti *assessed symmetrically*. Usulan: "Keterbatasan data pemerintah dan nonpemerintah dinilai dengan kriteria yang sama." Kriterianya dapat dirujuk ke daftar penilaian sumber. | Utama |
| 799; 959; 1616 | "konfigurasi bukti" | Pembaca harus menebak apakah ini susunan sumber, indikator, unit, atau status bukti. Jelaskan sekali sebagai "susunan sumber data, indikator, dan unit analisis yang digunakan", sesuai cakupan yang dimaksud penulis. Setelah itu istilah singkat boleh dipertahankan. | Utama |
| 833 sampai 839 | "Akuisisi mengikuti jalur"; "locator halaman"; "Terlihat publik" | Pilihan katanya terasa berasal dari bahasa pemerolehan data teknis. Usulan: "Data diperoleh melalui ...", "nomor halaman sumber", dan "Dapat diakses publik tidak berarti boleh disimpan atau dibagikan ulang". Jika halaman PDF dan halaman tercetak berbeda, catat keduanya. | Utama |
| 959; 1123 sampai 1124; 1500; 1611 | "manifest" | Istilah dokumentasi belum langsung membantu pembaca tugas akhir. Gunakan "daftar sumber dan parameter", "catatan penetapan ambang", atau "daftar berkas keluaran" sesuai objek. Jika manifest adalah nama berkas yang benar-benar digunakan, pertahankan namanya dan jelaskan isinya. | Menengah |
| 1084 sampai 1085 | "arah dan asimetri volume per koridor" | Volume apa dan bagaimana arah dibedakan belum jelas. Usulan: "volume kendaraan menurut arah perjalanan dan ketimpangan arus pada setiap koridor". Jangan mengubah hitungan kendaraan menjadi pasangan asal-tujuan atau jumlah orang. | Utama |
| 1163 sampai 1166 | "pasangan lokasi tempat tinggal dan tempat kegiatan tingkat kecamatan yang berbeda dan berulang sedikitnya dua minggu" | Yang berulang seharusnya kegiatan atau perjalanan, bukan lokasinya. Pisahkan penjelasan perbedaan kecamatan asal-tujuan dari kriteria pengulangan. Rumusan final perlu dicocokkan dengan definisi BPS yang sudah dirujuk, bukan ditebak. | Utama |
| 1229 sampai 1239 | "Fungsi diukur terpisah pada tiga hasil" | Terasa seperti pemakaian *outcomes* yang belum dijelaskan. Usulan: "Analisis memodelkan tiga variabel hasil secara terpisah: layanan orde tinggi, layanan keuangan, dan stok nonhunian." Jangan menyebutnya tiga domain utama; naskah menetapkan dua domain utama. | Menengah |
| 1301 | "peluang yang secara potensial terjangkau" | Potensial dan peluang mengulang makna. Usulan: "peluang yang dapat dijangkau menurut waktu tempuh model". Tetap nyatakan bahwa pekerjaan yang benar-benar diperoleh tidak teramati. | Menengah |
| 1303; 578; 1905 | "Waktu tempuh dengan lalu lintas" | Seolah ada waktu tempuh yang tidak melibatkan lalu lintas sama sekali. Usulan: "waktu tempuh yang memperhitungkan kondisi lalu lintas". Perbedaan dengan waktu tempuh arus bebas tetap dinyatakan. | Menengah |
| 1307 sampai 1310 | "menjadi sensitivitas"; "pemeriksa moda angkutan umum" | Nomina analisis menggantikan tindakan penelitian. Usulan: "dipakai dalam uji sensitivitas" untuk tujuan DKI terdekat, dan "dipakai sebagai pembanding untuk moda angkutan umum" untuk GTFS. Penamaan sensitivitas atau triangulasi harus mengikuti perbedaan konstruk; lihat Bagian 5. | Utama |
| 1332 sampai 1333 | "Polaritas ditetapkan per konstruk dan tidak disimpulkan dari tanda mentah" | Sangat padat dan tidak menjelaskan tanda apa yang dimaksud. Uraikan indikator mana yang nilainya menunjukkan beban lebih tinggi, ketergantungan lebih tinggi, atau integrasi lebih tinggi. Jangan mengasumsikan semua nilai besar bermakna baik atau buruk. | Utama |
| 1430 | "meloloskan setiap kecamatan" | Pemeriksaan bukti terdengar seperti proses administrasi seleksi. Usulan: "memenuhi syarat pemberian label pada setiap kecamatan". Pertahankan bahwa ketergantungan kabupaten/kota tidak cukup untuk memberi label pada seluruh kecamatan. | Menengah |
| 1509 sampai 1512 | "membaca konsekuensi kondisional" | Terasa seperti padanan *conditional consequences*. Usulan: "melihat perubahan hasil model ketika nilai indikator tertentu diubah". Tetap sebut ini eksplorasi model, bukan prediksi dampak kebijakan. | Menengah |
| 1560 sampai 1561 | "alasan labelnya didukung atau belum terselesaikan" | "Belum terselesaikan" tidak sejajar dengan "didukung" dan bisa menerangkan label atau alasan. Usulan: "beserta alasan suatu label didukung oleh bukti atau belum dapat ditetapkan". Nama kategori formal tetap diselaraskan. | Menengah |
| 1616 sampai 1619 | "Konfigurasi bukti yang lolos audit dibekukan"; "cadangan bernama diterapkan sesuai pemicunya, atau batas modul dilaporkan" | Jargon bertumpuk dan "batas modul" tidak jelas. Nyatakan sumber yang dipakai, penetapan versi, kapan alternatif digunakan, dan keterbatasan yang dilaporkan. Contoh utuh tersedia pada Bagian 6. | Utama |

### 3.4 Bab 4 dan lampiran

| Baris | Kutipan | Masalah dan arah perbaikan | Prioritas |
|---|---|---|---|
| 1637 | "tahun dan locator yang disebutkan" | Istilah asing tidak perlu untuk maksud sederhana. Usulan: "tahun serta nomor halaman atau tabel sumber yang dicantumkan". Gunakan "bagian sumber" jika rujukannya bukan halaman atau tabel. | Utama |
| 1641 | "menampung perumahan, pekerjaan, industri, pendidikan, perdagangan" | Satu verba dipakai untuk bangunan, pekerjaan, sektor, dan kegiatan. Bisa disusun menjadi "Di Bogor, Depok, Tangerang, dan Bekasi berkembang kawasan hunian, industri, pusat pendidikan, perdagangan, dan kegiatan lain ...". Pertahankan informasi pekerjaan dan perbedaan kemandirian dalam kelanjutannya. | Rendah |
| 1691 | "fungsi dibandingkan terhadap massa" | Selain preposisinya kaku, fungsi dan massa bukan besaran yang langsung dibandingkan. Usulan: "fungsi aktual dibandingkan dengan fungsi yang diharapkan berdasarkan massa lokal". | Utama |
| 1735 | "rumah sakit per penduduk setara dengan kota"; "perguruan tinggi per penduduknya" | Pembanding kota tidak spesifik dan ungkapannya menyerupai *hospitals per population*. Gunakan "rasio rumah sakit per 100 ribu penduduk" dan sebut kota pembanding. Tabel naskah mencatat Kabupaten Bekasi 1,86 dan Kota Tangerang 1,88; jangan menyatakan setara dengan semua kota. | Utama |
| 1846 | "jumlah tenant" | Lebih jelas: "jumlah perusahaan yang menempati kawasan" jika itu isi atribut yang dimaksud. Jangan otomatis memakai "penyewa" karena status sewa perusahaan tidak diketahui. | Menengah |
| 1859 | "7 hanya ambang penduduk"; "7 hanya ambang volume hunian" | Predikat hilang. Usulan: "7 memenuhi hanya kriteria penduduk" dan "7 memenuhi hanya kriteria volume hunian". Selain itu, pisahkan uraian kriteria, sebaran lokasi, cakupan layanan, dan hubungan dua ukuran massa ke beberapa paragraf. Semua angka dan pengecualian tetap dipertahankan. | Utama |
| 1884; 1889; 1891; 1915 | "Cadangan bernama"; "Bagian rantai"; "Pemicu" | Selaraskan dengan istilah bab: "Alternatif analisis berkode", "Komponen analisis", dan "Syarat penggunaan". Struktur tabel serta kode K1 sampai K9 tetap diperlukan. | Menengah |
| 1945 sampai 1946; 1948 | "Tangkapan 2026"; "Tangkapan bertanggal" | Terasa seperti *snapshot*, tetapi tanggal dan jenis pengambilan belum jelas. Gunakan "pengambilan data 2026" atau "salinan data pada tanggal pengambilan" sesuai objek. Sumber yang belum diambil tetap diberi keterangan tersebut; jangan mengarang tanggal akses. | Menengah |
| 1995 sampai 1996 | "peta berpeta dasar non-Google" | Pengulangan kata peta membuat susunan janggal. Usulan: "peta yang menggunakan peta dasar non-Google". Syarat penggunaan sumber tetap dipertahankan. | Utama |
| 2002 sampai 2006 | "kebutuhan permintaan diperkirakan sekitar 850 permintaan" | Permintaan diulang dan objeknya tidak disebut. Usulan: "Dengan 141 kecamatan dan sekitar enam jenis tempat, diperlukan sekitar 850 permintaan API." Pertahankan sifat perkiraan, batas 5.000, rujukan harga, dan rencana uji coba. | Menengah |

## 4. Audit humanizer pada susunan tulisan

### 4.1 Jargon prosedural yang berdekatan

Masalah paling menonjol berada pada baris 530 sampai 578, 591 sampai 648, dan 1608 sampai 1631. Pembaca berulang kali menjumpai rantai, pembekuan, gerbang, konfigurasi, cadangan, pemicu, dan manifest. Ini bukan alasan menghapus prosedur. Istilah tersebut perlu dijelaskan melalui tindakan yang benar-benar dilakukan.

Pedoman penyuntingan yang disarankan:

| Istilah sekarang | Bentuk yang lebih langsung | Makna yang harus tetap ada |
|---|---|---|
| Gerbang bukti; gerbang penggunaan label | Syarat penggunaan label; pemeriksaan kelayakan interpretasi | Label hanya dipakai setelah bukti memenuhi syarat, bukan berdasarkan tanda residu saja. |
| Cadangan bernama | Alternatif analisis berkode | Alternatif sudah ditetapkan, mempunyai syarat penggunaan, dan tidak dipilih untuk memperoleh hasil menarik. |
| Dibekukan | Ditetapkan sebelum analisis; disimpan sebagai nilai acuan tanpa ditimpa | Keputusan tidak disesuaikan diam-diam setelah hasil diketahui. |
| Konfigurasi bukti | Susunan sumber, indikator, dan unit analisis | Perubahan sumber atau konstruk dibedakan dari perubahan keadaan wilayah. |
| Manifest | Daftar sumber dan parameter; catatan penetapan; daftar berkas keluaran | Asal-usul data, versi, dan keputusan tetap dapat ditelusuri. |
| Pengukuran sejajar | Pengukuran terpisah | Peluang, beban, dan ketergantungan tidak dilebur menjadi satu skor yang menutupi perbedaan. |

Pilihan padanan perlu disepakati sekali, kemudian dipakai konsisten. Jangan menciptakan sinonim berbeda hanya agar pengulangan hilang.

### 4.2 Nominalisasi yang mengaburkan tindakan

Baris 84, 88, 271, 348, 352, dan 1616 memuat rangkaian seperti "perangkaian", "konfigurasi", "inferensi", dan "pemeriksaan". Kata-kata itu tidak salah. Masalahnya muncul ketika beberapa kata abstrak menjadi satu-satunya penjelasan tentang apa yang dilakukan penelitian.

Gunakan verba ketika tindakan dapat disebut: mengukur arus, membentuk fungsi harapan, mengestimasi kemiringan, memeriksa syarat label, atau mencatat perubahan sumber. Istilah seperti estimand, residu, dan kemiringan tetap digunakan saat menunjuk objek statistik yang spesifik.

### 4.3 Pengulangan negasi dan batas klaim

Pembatas kausalitas, produktivitas, fungsi lokal, dan perluasan wilayah muncul antara lain pada baris 126 sampai 130, 203, 211, 219, 225, 348, 409, 494 sampai 498, 731 sampai 735, 1267 sampai 1275, 1369 sampai 1387, serta 1590 sampai 1631.

Sebagian besar pembatas tersebut penting dan bukan sekadar pengisi. Jangan menghapusnya demi meloloskan daftar humanizer. Namun, pada bagian yang berdekatan, rangkaian "bukan ...", "tidak ...", dan "hanya ..." membuat argumen terasa terus membantah pembaca.

Perbaikannya adalah mendahulukan pernyataan positif tentang apa yang diukur, lalu menempatkan batas inferensi yang relevan. Batas harus tetap hadir di titik pembaca mungkin salah menafsirkan hasil. Gunakan rujukan silang untuk rincian yang sudah dijelaskan, bukan menghapus perbedaan antara asosiasi dan kausalitas.

### 4.4 Uraian gap yang terlalu mengikuti pola tabel

Baris 294 sampai 306 berkali-kali menggunakan pola "belum/tidak ...; penelitian ini ..." pada kolom celah dan posisi penelitian. Pola itu masuk akal untuk tabel perbandingan, tetapi dapat terasa mekanis karena setiap penelitian diarahkan ke paket kontribusi yang sama.

Pertahankan satu perbedaan yang paling relevan pada setiap baris: unit analisis, jenis fungsi, arah arus, pengukuran beban, atau ketahanan klasifikasi. Tidak perlu mengulang semua keunggulan rancangan pada setiap penelitian. Jangan memperbesar kelemahan sumber hanya untuk menguatkan kebaruan penelitian ini.

### 4.5 Kalimat penghubung yang belum membawa informasi

Kalimat tentang ojek daring pada baris 263 menyebutnya sebagai "bagian lain dari hubungan metropolitan" tanpa menjelaskan kaitannya dengan analisis berikutnya. Jika dipertahankan, nyatakan kaitannya dengan keragaman moda atau pembacaan arus antarpinggiran hanya sejauh didukung sumber. Jika tidak mempunyai peran dalam argumen, dapat dipangkas oleh penulis bersama rujukannya.

Sebaliknya, pembatas korpus pada baris 82 dan 269 bukan pengisi. Batas penelusuran itu mencegah klaim kebaruan universal dan perlu dipertahankan, meskipun dua kalimat pembatas yang berurutan bisa diringkas menjadi satu.

### 4.6 Paragraf padat yang memuat terlalu banyak tugas

Baris 1859 memuat aturan penandaan, ambang, jumlah kecamatan, distribusi kabupaten/kota, kehilangan data layanan, dua kriteria massa, contoh kecamatan, kota baru, dan korelasi dalam satu paragraf. Kepadatannya lebih mengganggu daripada pilihan satu-dua kata.

Pecah berdasarkan fungsi uraian: kriteria dan ambang; jumlah serta sebaran pusat; cakupan analisis layanan; hubungan penduduk dengan volume hunian. Pemecahan tidak boleh menghilangkan angka 36, 43, 28, 35, delapan pusat Kota Bekasi, komposisi 29 + 7 + 7, atau korelasi 0,86. Ini pemecahan paragraf, bukan pemecahan objek penelitian menjadi berkas baru.

### 4.7 Hal yang tidak perlu "dihumanisasi"

- Istilah *borrowed size*, *agglomeration shadow*, aglomerasi, polisentrisitas, residu, binomial negatif, Poisson kuasi-likelihood, *leave-one-out*, dan *wild cluster bootstrap* memiliki fungsi konseptual atau teknis. Konsistensinya lebih penting daripada variasi sinonim.
- Tiga mekanisme berbagi, mencocokkan, dan belajar pada baris 173 bukan "aturan tiga" yang dibuat untuk memperindah tulisan. Demikian pula tiga objek ketidakpastian pada baris 1389 sampai 1400 memang berbeda.
- Bentuk pasif tidak otomatis bermasalah. "Nilai hilang tidak diubah menjadi nol" justru ringkas dan jelas.
- Kata "berbasis", "signifikan", "urban", "konstruk", dan "estimand" tidak otomatis menandai AI. Makna statistik tidak boleh diganti dengan penilaian umum seperti "penting".
- Susunan bab, tabel, butir tujuan, rumus, dan format sitasi mengikuti kebutuhan tugas akhir. Struktur ini tidak perlu dibuat lebih informal.
- Angka rinci, nama kecamatan, pengecualian Kota Bekasi, perbedaan periode, dan ketidakpastian sumber perlu dipertahankan. Jangan menggantinya dengan generalisasi yang terasa lebih lancar tetapi kurang tepat.
- Bahasa ilmiah tidak perlu ditambah opini pribadi, humor, atau gaya percakapan untuk terasa manusiawi.

## 5. Kalimat yang tidak aman diperbaiki sebagai gaya saja

Bagian ini menandai ambiguitas yang terlihat saat membaca bahasa naskah. Ini bukan audit ulang seluruh metode. Perbaikannya perlu keputusan penulis atau pengecekan definisi sumber; tidak dilakukan otomatis.

| Baris | Ambiguitas | Keputusan yang diperlukan |
|---|---|---|
| 489; 512 sampai 516; 624 sampai 627; 656 sampai 657 | Uraian menyebut cakupan 141 kecamatan atau sumber yang seragam untuk fungsi, sedangkan layanan secara eksplisit memakai 129 kecamatan pada baris 126, 550 sampai 553, dan 1236 sampai 1238. | Selaraskan cakupan: 141 untuk populasi utama dan pekerjaan, 129 untuk layanan. Jangan memperhalus kalimat "seluruh wilayah" sehingga pengecualian Kota Bekasi makin tidak terlihat. |
| 352; 369; 1394 sampai 1400; 1438 sampai 1440; 1550 sampai 1552 | Ada pergantian antara selang ketidakpastian residu dan selang prediksi fungsi. Frasa "residunya tidak keluar dari selang prediksi" mencampur objek. | Tentukan apakah yang dibandingkan adalah fungsi teramati dengan selang prediksi fungsi, atau residu dengan selang pada skala residu. Baris 1394 sampai 1397 menyatakan yang pertama. Usulan bahasa harus mengikuti prosedur yang benar-benar digunakan. |
| 95; 237; 352; 369; 409; 1445 sampai 1448 | "Belum terselesaikan", "tidak terselesaikan", dan "belum terklasifikasi" tidak selalu mempunyai lingkup sama. Tabel juga memasukkan komponen hilang, sementara uraian membedakannya dari ketidakpastian. | Sepakati nama kategori dan bedakan alasan masuknya: data hilang, ketidakpastian prediksi, atau ketidakstabilan spesifikasi. "Campuran" tetap berarti perbedaan substantif antardomain, bukan ketidakpastian. |
| 524 sampai 528; 1031 sampai 1032; 1181 sampai 1194 | Istilah disagregasi atau estimasi dapat membuat indeks WSM berbobot orientasi DKI terbaca sebagai estimasi persentase kecamatan ke DKI, padahal naskah melarang tafsir itu. | Jelaskan bahwa ini indeks berbobot dengan penyebut berbeda, bukan penurunan angka komuter DKI ke tingkat kecamatan. Jangan menyederhanakan sampai status indeks tersebut berubah. |
| 1307 sampai 1310; 1485 sampai 1491; 1947 | GTFS disebut pemeriksa dan sensitivitas, tetapi kelompok pemeriksaan kemudian menempatkannya sebagai triangulasi yang dapat mengubah konstruk. | Gunakan istilah yang sama untuk tujuan DKI terdekat, GTFS, pergantian sumber, dan perubahan cakupan hasil sesuai objek masing-masing. Jangan menyebut semuanya sensitivitas yang setara. |
| 936 sampai 937; 1345 sampai 1348 | Kawasan industri disebut "tidak dikontrol", tetapi model memuat efek utama dan interaksinya. | Jelaskan bahwa kawasan industri diuji sebagai moderator, bukan dihapus dari model. Perbaikan bahasa tidak boleh menghilangkan efek utama atau interaksi yang sudah ditetapkan. |
| 1037 sampai 1045 | "Indeks volume" dapat menyiratkan skor normalisasi, sedangkan hasil pekerjaan dijelaskan sebagai volume fisik dalam m³. | Pastikan apakah benar ada indeks, atau hanya volume nonhunian. Jangan mengubah satuan atau menambahkan normalisasi yang tidak dilakukan. |
| 1628 sampai 1631 | Sesudah syarat label dinyatakan gagal, teks masih mengizinkan istilah "pola yang konsisten atau tidak konsisten dengan konstruk tersebut". Ini dapat terasa sebagai jalan memutar untuk label yang dibatasi sebelumnya. | Tentukan tingkat klaim yang masih diizinkan ketika syarat gagal. Selaraskan dengan istilah deskriptif pada baris 409, bukan hanya membuat kalimat lebih lancar. |
| 1643 | "minimal sembilan unit Jabodetabek" tidak menjelaskan jenis satuan administratif. DKI pada uraian studi diperlakukan sebagai gabungan, tetapi unit matriks berbeda. | Jelaskan lingkup administratif dengan merujuk ketentuan yang dimaksud. Jangan menebak padanan hukum atau mengganti nomenklatur melalui penyuntingan gaya. |
| 1942 | "Pengganti layanan Kota Bekasi" terdengar seperti sumber pengganti telah diterima, padahal kelanjutannya menyatakan tabel tidak setara dan K1 berlaku. | Gunakan "sumber yang diperiksa sebagai calon pengganti" atau rumusan serupa jika itu status sebenarnya. Jangan memberi kesan jumlah fasilitas yang hilang sudah tersedia. |
| 1945; 1094; 1508 sampai 1509; 1982 sampai 1999 | Baris sumber Google menyebut jumlah per poligon disimpan paling lama 30 hari dan nilai turunan, sementara uraian utama menegaskan tidak ada nilai per kecamatan yang disimpan sebagai keluaran. | Bedakan penyimpanan sementara untuk pengolahan dari keluaran agregat yang dipertahankan. Jangan menyamakan "nilai turunan" dengan izin menyimpan residu kecamatan. Ketentuan layanan tidak diverifikasi ulang dalam audit ini. |

## 6. Contoh humanisasi dengan pemeriksaan ulang

Contoh berikut adalah usulan, belum dimasukkan ke `.tex`. Proses draf, pemeriksaan kekakuan yang tersisa, dan usulan akhir ditampilkan agar alasan penyuntingannya terlihat.

### 6.1 Manfaat praktis, baris 155

Kalimat yang paling perlu diperbaiki adalah:

> Penelitian juga dapat membuka arah perlakuan yang lebih baik bagi kawasan hunian berpenduduk besar yang layanannya tertinggal dari permintaan lokal.

Draf:

> Penelitian juga dapat memberi arah penanganan yang lebih baik bagi kawasan hunian berpenduduk besar yang penyediaan layanannya tertinggal dari permintaan lokal.

Yang masih kaku: "memberi arah" tetap abstrak, sedangkan "lebih baik" belum menjelaskan bentuk kegunaannya. Kalimat perlu menyatakan bahwa penelitian membantu perumusan penanganan, bukan memastikan keberhasilannya.

Usulan akhir untuk seluruh paragraf:

> Secara praktis, penelitian ini membantu pemerintah daerah, Dewan Kawasan Aglomerasi, dan penyusun rencana induk Kawasan Aglomerasi memahami posisi kecamatan serta kabupaten/kota di sekitar Jakarta. Profil relasi, fungsi relatif, manfaat, dan beban digunakan untuk membedakan kebutuhan penguatan fungsi lokal, hubungan antarpusat, pengurangan beban perjalanan, dan koordinasi lintas batas. Hasilnya juga dapat membantu merumuskan penanganan yang lebih sesuai bagi kawasan hunian berpenduduk besar yang penyediaan layanannya tertinggal dari permintaan lokal. Keluaran ini bersifat diagnostik. Penelitian tidak menetapkan perubahan batas administrasi, memilih bentuk kelembagaan tertentu, atau memprediksi dampak kebijakan tanpa analisis tambahan.

Dipertahankan: penerima manfaat, semua jenis kebutuhan, kawasan hunian yang dimaksud, sifat diagnostik, dan tiga batas penggunaan hasil.

### 6.2 Alternatif analisis, baris 572 sampai 576

Teks asal, dengan perintah rujukan silang tidak ditampilkan:

> Setiap penyimpangan dari rantai ini hanya boleh terjadi melalui cadangan bernama yang pemicunya ditetapkan sebelum data diolah. Cadangan tidak dipilih karena menghasilkan kelas yang lebih menarik. Jika cadangan dipakai, alasan dan perbedaan hasilnya terhadap spesifikasi utama dilaporkan.

Draf:

> Perubahan spesifikasi utama hanya dilakukan melalui alternatif berkode yang syarat penggunaannya ditetapkan sebelum data diolah. Alternatif tidak dipilih untuk menghasilkan kelas yang lebih menarik. Penggunaannya dilaporkan bersama alasan dan perbedaan hasil terhadap spesifikasi utama.

Yang masih kaku: "penggunaannya dilaporkan bersama alasan" tetap nominal dan belum membedakan penetapan syarat dari pemenuhan syarat tersebut.

Usulan akhir:

> Setiap perubahan dari spesifikasi utama harus mengikuti alternatif analisis berkode yang tercantum dalam lampiran dan diagram keputusan. Syarat penggunaan setiap alternatif ditetapkan sebelum data diolah; alternatif hanya digunakan apabila syarat tersebut terpenuhi. Pilihannya tidak didasarkan pada keinginan memperoleh kelas hasil yang lebih menarik. Jika alternatif digunakan, penelitian melaporkan alasan pemilihannya dan perbedaan hasil dibandingkan dengan spesifikasi utama.

Dipertahankan: rujukan Lampiran A, tabel alternatif, dan diagram keputusan; penetapan sebelum pengolahan; larangan memilih berdasarkan hasil yang disukai; kewajiban melaporkan perbedaan. Perintah rujukan LaTeX asli perlu tetap ditempatkan pada kalimat pertama jika usulan diterapkan.

### 6.3 Aturan keputusan, baris 1616 sampai 1619

Teks asal:

> Konfigurasi bukti yang lolos audit dibekukan sebelum analisis, dan perubahan sumber atau model disimpan sebagai versi baru. Jika suatu modul gagal, cadangan bernama diterapkan sesuai pemicunya, atau batas modul dilaporkan tanpa mengubah nilai hilang menjadi nol.

Draf:

> Susunan bukti yang memenuhi audit ditetapkan sebelum analisis, dan perubahan sumber atau model dicatat sebagai versi baru. Jika modul gagal, alternatif berkode digunakan sesuai syaratnya, atau keterbatasannya dilaporkan. Nilai hilang tidak diubah menjadi nol.

Yang masih kaku: "susunan bukti" tetap kabur; satu kalimat menampung kegagalan, alternatif, dan pelaporan tanpa urutan keputusan yang jelas.

Usulan akhir:

> Sumber data yang memenuhi syarat audit ditetapkan sebelum analisis. Setiap perubahan sumber atau model dicatat sebagai versi baru. Jika suatu modul tidak dapat dijalankan, penelitian menggunakan alternatif yang telah ditetapkan hanya apabila syarat penggunaannya terpenuhi. Jika tidak ada alternatif yang sesuai, keterbatasan modul dilaporkan. Nilai hilang tetap dicatat sebagai nilai hilang, bukan nol.

Catatan penerapan: bila "konfigurasi bukti" juga mencakup indikator, unit, dan parameter, sebut komponen tersebut pada kalimat pertama. Pilihan ini memerlukan penetapan cakupan istilah, bukan sekadar penggantian kata.

## 7. Catatan EYD dan istilah asing

Masalah keluwesan bahasa di atas tidak semuanya kesalahan EYD. "Cadangan bernama", misalnya, adalah masalah pilihan istilah dan keterbacaan, bukan pelanggaran ejaan.

Pemeriksaan EYD terbatas pada hal berikut:

1. Kata atau ungkapan asing biasa ditulis miring jika dipertahankan. `locator` pada baris 835 dan 1637 serta `tenant` pada baris 1846 belum dibungkus perintah huruf miring. Padanan Indonesia lebih membantu pada ketiga lokasi tersebut. Rujukan: EYD V, Bab I bagian G angka 3.
2. Nama diri dan merek asing tidak otomatis ditulis miring. Jangan menerapkan koreksi yang sama kepada nama seperti Google Maps Platform, OpenStreetMap, atau TransJakarta. Rujukan: catatan pada bagian huruf miring EYD V.
3. Periksa koma sebelum anak kalimat pada baris 187, 348, dan 1044: masing-masing memuat koma sebelum "sehingga" atau "karena" setelah induk kalimat. Pada susunan tersebut koma dapat dihapus agar sesuai pola induk kalimat diikuti anak kalimat. Jangan menghapus koma sebelum "tetapi", "melainkan", atau "sedangkan" yang membentuk pertentangan. Rujukan: EYD V, Bab III bagian B angka 2 dan 4.
4. Istilah teknis asing yang sudah ditulis miring, misalnya *leave-one-out*, *screenline*, dan *what-if*, tidak perlu diganti semata-mata karena berasal dari bahasa Inggris. Jelaskan istilah jika diperlukan oleh pembaca.

Rujukan yang benar-benar dibaca: `references/eyd/eyd-edisi-v-2022.md` pada skill `indonesia-eyd-writing-skill`, bagian huruf miring dan tanda koma. Audit tidak memeriksa semua lema terhadap KBBI dan tidak mengklaim setiap saran padanan sebagai koreksi kata baku.

## 8. Urutan revisi yang disarankan

1. Dahulukan kalimat yang dapat mengubah tafsir: fungsi pusat pada baris 80, cakupan 141/129, selang prediksi, indeks berbobot DKI, dan aturan label ketika syarat gagal.
2. Perbaiki ungkapan paling janggal: "membuka arah perlakuan", "manfaat dapat ditahan", "tanda yang berbeda", "menjadi sensitivitas", "locator", dan "peta berpeta dasar".
3. Tetapkan padanan yang konsisten untuk gerbang, cadangan, pembekuan, konfigurasi, dan manifest. Pertahankan semua aturan analitis yang diwakilinya.
4. Kurangi pengulangan batas klaim yang benar-benar berdekatan; jangan menghapus pembatas yang diperlukan untuk menafsirkan rumus atau hasil.
5. Pecah paragraf baris 1859 dan rapikan kolom celah penelitian terdahulu tanpa kehilangan angka, sumber, atau pengecualian.
6. Baca ulang hasil penyuntingan dengan suara pelan. Jika pembaca masih harus menerjemahkan istilah prosedural menjadi tindakan, kalimatnya belum cukup jelas.

## 9. Batas audit

Audit ini berdasarkan pembacaan teks sumber `.tex`, bukan hasil render PDF. Teks di dalam berkas gambar, tata letak hasil kompilasi, entri daftar pustaka yang dihasilkan dari berkas lain, dan seluruh sumber eksternal tidak diaudit ulang. Tidak dilakukan kompilasi, penghitungan ulang data, atau verifikasi baru terhadap regulasi dan ketentuan layanan.

Nomor baris dan kutipan merujuk hanya pada versi dengan hash yang dicantumkan. Usulan penyuntingan merupakan penilaian **GPT Sol**, bukan posisi intelektual baru penulis. Perbedaan metode yang disebut pada Bagian 5 tetap memerlukan keputusan penulis. Tidak ada promosi sintesis, perubahan kerangka penelitian, atau penambahan catatan topik karena pekerjaan ini terbatas pada audit editorial.
