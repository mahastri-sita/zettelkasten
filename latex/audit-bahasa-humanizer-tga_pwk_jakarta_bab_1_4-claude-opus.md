# Audit bahasa: terjemahan dan pola tulisan AI — TGA Jabodetabek Bab 1–4

> **Auditor: Claude Opus 5.5 (Anthropic)** — model `claude-opus-5-5`, dijalankan lewat Claude Code.
> **Tanggal:** 3 Oktober 2026.
> **Objek:** `latex/tga_pwk_jakarta_bab_1_4_final.tex`, commit `113d7af` (Bab 1–4; lampiran dan daftar pustaka tidak diaudit).
> **Mode:** audit saja. **Naskah tidak direvisi.** Laporan ini disimpan untuk dibandingkan dengan audit model lain sebelum ada keputusan revisi.

## 0. Cara membaca

- Nomor `L…` adalah nomor baris di file `.tex` pada commit `113d7af`. Nomor bisa bergeser setelah revisi apa pun; cari juga dengan kutipan.
- Setiap temuan memuat kutipan, alasan mengapa terasa seperti terjemahan atau pola AI, dan **arah** perbaikan. Arah bukan teks pengganti final.
- Dua lensa dipakai:
  1. **Terjemahan (*translationese*)**: kalimat yang struktur, kolokasi, atau istilahnya mengikuti bahasa Inggris sehingga terasa diterjemahkan.
  2. **Humanizer**: pola tulisan AI menurut skill `humanizer` (berbasis *Wikipedia: Signs of AI writing*) dan lapisan `humanizer-academic-id`.
- Tingkat keparahan: **T** = tinggi (terasa jelas, dekat pembaca, atau mengaburkan makna); **S** = sedang; **R** = rendah (gaya, boleh dibiarkan).

## 1. Penilaian umum

Naskah **bersih dari penanda AI yang paling kasar**:
- tidak ada kosakata AI khas (*menyoroti, krusial, lanskap, signifikan, menggarisbawahi, berfungsi sebagai, memainkan peran*);
- tidak ada pembuka klise ("Di era globalisasi…"), tidak ada kesimpulan berbunga;
- tidak ada em dash, kutip melengkung, atau emoji.

Masalah utamanya ada di **lapisan terjemahan**. Banyak kalimat dibangun dengan logika bahasa Inggris akademik: kata kerja *read as* menjadi "dibaca sebagai", *baseline* menjadi "garis dasar", *robust to* menjadi "ketahanan terhadap", *consistent with* menjadi "konsisten dengan", *it* menjadi "Ia". Hasilnya benar secara tata bahasa, tetapi terasa kaku dan "diterjemahkan", terutama di **Bab 3**.

Pola AI yang tersisa bersifat **struktural**, bukan leksikal:
1. penolakan di ekor kalimat (", bukan …") masih 42 kali;
2. daftar tiga unsur atau lebih yang padat, terutama di Bab 1 (±18 per 1.000 kata);
3. ritme kalimat yang sangat seragam di Bab 1, 2, dan 4 (rata-rata ±17 kata, simpangan baku ±7);
4. pengulangan pernyataan batas klaim yang defensif di banyak tempat.

**Per bab (penilaian kualitatif):**

| Bab | Rasa terjemahan | Pola AI | Catatan |
|---|---|---|---|
| 1 | Sedang | Sedang | Latar belakang sudah ringkas; kalimat penutup paragraf sering berupa daftar paralel |
| 2 | Sedang–tinggi | Sedang | Banyak kalke konseptual ("pembacaan", "Ia", "menangkap", "menikmati surplus") |
| 3 | **Tinggi** | Sedang | Jargon metodologi hasil terjemahan langsung; kepadatan istilah tertinggi |
| 4 | Rendah | Rendah | Paling alami: angka konkret, nama tempat, kalimat deskriptif |

## 2. Metrik pendukung

Dihitung dari sumber `.tex` (prosa saja; tabel, gambar, dan rumus dikeluarkan).

| Bab | Kalimat | Rata-rata kata/kalimat | Simpangan baku | Kalimat >35 kata | Kalimat <8 kata | Kata ber-awalan *di-* per 100 kata | Daftar 3+ unsur per 1.000 kata |
|---|---|---|---|---|---|---|---|
| 1 | 101 | 17,9 | 7,9 | 1 | 15 | 3,9 | 17,7 |
| 2 | 175 | 17,2 | 7,8 | 3 | 14 | 3,8 | 16,6 |
| 3 | 357 | 17,0 | 12,8 | 13 | 48 | 5,2 | 10,8 |
| 4 | 132 | 17,4 | 6,5 | 2 | 4 | 1,8 | 14,8 |

Frekuensi penanda terjemahan di seluruh Bab 1–4:

| Penanda | Jumlah | Padanan Inggris yang ditiru |
|---|---|---|
| ", bukan …" di ekor kalimat | 42 | *…, not …* |
| "dibaca sebagai/dibaca dari/membaca" (metaforis) | 16+ | *read as / read from* |
| "konsisten dengan" | 13 | *consistent with* |
| "garis dasar" | 9 | *baseline* |
| "gerbang (bukti/penggunaan label)" | 13 | *(evidence) gate* |
| "spesifikasi (utama/kembar)" | 20 | *(main/twin) specification* |
| "pemeriksa" sebagai kata benda | 7 | *checker* |
| "menjadi" sebagai pengganti kopula | 50 | *serves as / becomes* |
| "tersebut" | 65 | *the/that* |
| "Ia" untuk konsep abstrak | 3 | *it* |

Catatan: angka-angka ini indikator, bukan vonis. "Tersebut" dan "menjadi" wajar dalam bahasa Indonesia akademik; yang dinilai adalah kepadatannya dalam satu paragraf.

## 3. Temuan: rasa terjemahan

### 3.1 Verba metaforis "membaca / dibaca sebagai" (*read as*) — T

Bahasa Indonesia akademik jarang "membaca" data; biasanya "menafsirkan", "memperlakukan", "melihat", atau "menyimpulkan".

| Baris | Kutipan | Arah |
|---|---|---|
| L116 | "Bukti tersebut dibaca dari kemiringan hubungan fungsi dengan integrasi" | "Bukti tersebut diambil dari / disimpulkan dari kemiringan…" |
| L134, L1257 | "Residu dipakai untuk membaca posisi setiap kecamatan" | "untuk menunjukkan / menentukan posisi…" |
| L175 | "teori aglomerasi menjadi garis dasar untuk membaca hubungan ukuran dan fungsi" | "menjadi acuan untuk menafsirkan…" |
| L199 | "mencegah waktu tempuh singkat dibaca sebagai integrasi aktual" | "mencegah waktu tempuh singkat dianggap sebagai…" |
| L211 | "literatur rujukan membacanya dari koefisien" | "literatur rujukan menyimpulkannya dari koefisien" |
| L239, L675 | "jejak fungsional … tidak boleh dibaca sebagai perluasan wilayah" | "tidak boleh ditafsirkan sebagai…" |
| L243, L1505 | "membaca konsekuensi kondisional" | "menelusuri konsekuensi bersyarat" |
| L771 | "Fungsinya adalah membaca apakah kemiringan…" | "Tujuannya adalah memeriksa apakah…" |
| L1207, L1369, L1797, L1840 | "dibaca sebagai arah dan asimetri koridor", "dibaca sebagai profil, bukan regresi", "dibaca sebagai arah perubahan", "Peta dibaca sebagai skenario kebijakan" | variasikan: "diperlakukan sebagai", "ditafsirkan sebagai", "disajikan sebagai" |

### 3.2 Kalke istilah metodologi — T (terutama Bab 3)

Istilah teknis memang perlu konsisten, tetapi sebagian istilah di bawah adalah terjemahan harfiah yang tidak lazim dalam literatur perencanaan berbahasa Indonesia. Pembaca (penguji) harus menerjemahkannya balik ke bahasa Inggris untuk paham.

| Istilah di naskah | Asal | Contoh baris | Arah |
|---|---|---|---|
| garis dasar | *baseline* | L175, L530, L641, L1111 | "acuan", "kondisi awal", atau "nilai acuan" |
| dibekukan / pembekuan | *frozen / freeze* | L530, L1111, L1121, L1616 | "ditetapkan sebelum…", "dikunci" (cukup satu istilah) |
| menimpa nilai observasi | *overwrite* | L530, L641 | "mengubah nilai observasi" |
| gerbang bukti, gerbang penggunaan label | *evidence gate, label gate* | L398, L1402 | "syarat pelabelan", "syarat bukti" |
| label ketat | *strict label* | L1402 | "label penuh", atau cukup "label" |
| spesifikasi kembar | *twin specification* | L120, L542, L1181 | "spesifikasi pendamping" |
| cadangan bernama | *named fallback* | L536, L572 | "alternatif cadangan (K1–K9)" |
| rantai inti … dikunci | *core chain locked* | L538 | "rangkaian analisis utama ditetapkan sebagai…" |
| kebenaran dasar | *ground truth* | L1163 | "acuan kebenaran" atau hapus |
| registri asal-usul data | *provenance registry* | L947, L1608 | "catatan asal-usul data" |
| manifest (mutu bukti/keluaran) | *manifest* | L947, L1121, L1500, L1608 | "daftar", "catatan konfigurasi" |
| paket reproduksi | *replication package* | L1608 | "berkas replikasi" |
| interpretasi aman | *safe interpretation* | L361 (judul kolom Tabel 2.2) | "tafsiran yang dapat dipertanggungjawabkan" / "batas tafsiran" |
| pemeriksa (kata benda) | *checker* | L927, L1094, L1345 | "pembanding", "alat pemeriksaan" |
| penguatan (modul) | *enhancement* | L128, L1089, L1453 | "pelengkap", "tambahan opsional" |
| skenario bukti, konfigurasi bukti | *evidence scenario/configuration* | L641, L1616 | "skenario sumber data", "kombinasi sumber" |
| tingkat tempat | *place level* | L1559 | "tingkat kecamatan" |
| jejak fungsional | *functional footprint* | L239, L675 | "jangkauan fungsional" |
| hasil (sebagai *outcome*) | *outcome* | L1229 dst. ("tiga hasil", "hasil layanan utama", "hasil pekerjaan") | ambigu dengan "hasil penelitian"; pakai "variabel terikat" atau "luaran" |
| ketahanan … terhadap keputusan analitis/teknis | *robustness to analytical choices* | L102, L219 | "kestabilan hasil terhadap pilihan analisis" |
| estimand | *estimand* | L1345, L1464 | boleh dipertahankan sebagai istilah statistik, tetapi beri padanan sekali ("besaran yang diestimasi") |

### 3.3 Kolokasi dan preposisi Inggris — S

| Baris | Kutipan | Masalah | Arah |
|---|---|---|---|
| L76 | "dengan saat berlaku yang dikaitkan dengan Keputusan Presiden" | *with its entry into force tied to* | "yang mulai berlakunya bergantung pada Keputusan Presiden" |
| L193 | "Bukti Indonesia menunjukkan" | *Indonesian evidence shows* | "Studi di Indonesia menunjukkan" |
| L217 | "Studi pada jaringan kota" | *studies on city networks* | "Studi tentang jaringan kota" |
| L217, L253 | "manfaat akses dapat ditahan", "manfaat ekonomi telah tertahan" | *retained* | "tetap berada di pusat sekunder", "dinikmati di lokasi yang sama" |
| L253 | "Kawasan industri di pinggiran menangkap pertumbuhan pekerjaan" | *capture job growth* | "menyerap / menampung pertumbuhan pekerjaan" |
| L211 | "tolok ukur internal tidak menangkapnya" | *does not capture it* | "tidak dapat mendeteksinya" |
| L225 | "memberi sinyal yang sama" | *give the same signal* | "menunjukkan gejala yang sama" |
| L237 | "pusat menikmati surplus" | *enjoys a surplus* | "pusat mempunyai surplus" |
| L237 | "ditempatkan sebagai ketidakstabilan hasil" | *treated as* | "dianggap sebagai ketidakstabilan hasil" |
| L231, L825, L1453 | "belum dengan sendirinya membuktikan", "tidak menjadi ukuran mutu dengan sendirinya" | *by itself* | "belum cukup untuk membuktikan" |
| L191 | "tidak otomatis kuat" | *not automatically strong* | "belum tentu kuat" |
| L1047 | "akan muncul hampir secara otomatis" | *almost automatically* | "hampir pasti muncul" |
| L1381 | "tidak kebal terhadap penjelasan lain" | *not immune to* | "masih dapat dijelaskan oleh faktor lain" |
| L624–625 | "dinilai secara simetris" | *assessed symmetrically* | "dinilai dengan ukuran yang sama" |
| L1248 | "tanpa harus mengambil logaritma hasil" | *take the log* | "tanpa melogaritmakan variabel terikat" |
| L1018 | "pusatnya jatuh di dalam poligon" | *falls within* | "pusatnya terletak di dalam poligon" |
| L1643 | "Secara kebijakan, Jabodetabek menjadi inti…" | *policy-wise* | "Dalam kebijakan nasional, …" |
| L257 | "Yudhistira dan kolega", "Pratama dan kolega" | *and colleagues* | "Yudhistira dkk." (sejalan dengan gaya sitasi yang kini memakai "dkk.") |
| L215 | "biasanya diasosiasikan dengan kota yang lebih besar" | *associated with* | "biasanya dimiliki kota yang lebih besar" |
| 13 tempat | "konsisten dengan *borrowed size*" | *consistent with* | pertahankan di definisi tipologi (istilah teknis), tetapi variasikan di prosa: "sejalan dengan", "sesuai dengan" |

### 3.4 Kata ganti "Ia" untuk konsep abstrak — S

Bahasa Indonesia baku memakai "ia" untuk orang. Untuk konsep, penulis Indonesia mengulang nomina atau memakai "istilah ini", "persamaan ini".

- L203: "Ia tidak menjadi ukuran langsung kesejahteraan…" (subjek: kematangan fungsi lokal)
- L233: "Ia dapat tampak dalam dominasi tujuan komuter…" (subjek: ketergantungan asimetris)
- L348: "Ia menunjukkan objek yang dipisahkan…" (subjek: persamaan)

Arah: "Istilah ini…", "Ketergantungan seperti ini…", "Persamaan tersebut…".

### 3.5 Struktur kalimat bahasa Inggris — T untuk yang mengaburkan makna

| Baris | Kutipan | Masalah | Arah |
|---|---|---|---|
| L120 | "pada kecamatan yang sendiri berada di dalam kawasan inti" | *which itself lies within*; "sendiri" janggal | "pada kecamatan yang termasuk kawasan inti" |
| L187 | "tempat berpenduduk besar tetapi berfungsi sedikit, yang justru kandidat korban *shadow*" | aposisi tanpa kopula; "berfungsi sedikit" janggal | "tempat berpenduduk besar dengan fungsi sedikit, yang justru merupakan kandidat korban *shadow*" |
| L211 | "sebagian unit akan tetap bertanda negatif tanpa berarti apa pun tentang Jakarta" | *without meaning anything about Jakarta* | "…bertanda negatif tanpa mengatakan apa pun tentang pengaruh Jakarta" |
| L225 | "Penduduk yang besar menciptakan permintaan…" | *a large population*; penduduk tidak "besar" | "Jumlah penduduk yang besar menciptakan…" |
| L233 | "hubungan penting bagi pusat sekunder, sementara kepentingan timbal baliknya tidak seimbang" | *reciprocal importance* | "pusat sekunder sangat bergantung pada hubungan itu, sedangkan Jakarta tidak" |
| L348 | "Persamaan ini bukan komitmen pada model kausal." | *not a commitment to a causal model* | "Persamaan ini tidak dimaksudkan sebagai model sebab-akibat." |
| L833 | "Terlihat publik tidak berarti boleh disimpan atau dibagikan ulang." | *publicly visible ≠ …*; tanpa subjek | "Data yang dapat dilihat publik belum tentu boleh disimpan atau dibagikan ulang." |
| L1029 | "Variabel dari tahun berbeda tidak dinormalisasi ulang untuk menyembunyikan selisih tahun." | dapat terbaca "tidak dinormalisasi *agar* menyembunyikan" | "Variabel dari tahun berbeda tidak dinormalisasi ulang, sehingga selisih tahun tetap terlihat." |
| L1056 | "Hasil layanan utama menjumlahkan rumah sakit…" | subjek tidak bisa "menjumlahkan" (*the main outcome sums*) | "Variabel layanan utama adalah jumlah rumah sakit dan…" |
| L1079 | "Model deteksi objek pralatih … pelacak objek mempertahankan identitas antarbingkai" | neologisme harfiah (*pretrained, across frames*) | "model deteksi objek yang sudah dilatih … pelacak objek mengikuti kendaraan yang sama dari satu bingkai ke bingkai berikutnya" |
| L1089 | "Statusnya penguatan opsional." | fragmen tanpa kopula | "Modul ini bersifat tambahan opsional." |
| L1389 | "Tiga objek ketidakpastian dibedakan." | *three objects of uncertainty* | "Ketidakpastian dihitung untuk tiga hal yang berbeda." |
| L1870 | "satu baris tidak dipakai untuk menyiratkan seri waktu" | *a row is not used to imply* | "setiap baris tidak menyiratkan seri waktu" |
| L786–796 | daftar imperatif "gunakan…", "agregasikan…", "jangan membandingkan…" | gaya pedoman Inggris (*use…, do not…*) | ubah ke kalimat deklaratif: "Perhitungan awal memakai unit asli…" |

### 3.6 Nominalisasi berat — S

Bahasa Inggris akademik suka nomina abstrak; bahasa Indonesia lebih luwes dengan verba.

- L80, L193: "pembacaan yang berlawanan / berbeda" → "tafsiran yang berlawanan", atau "kedua konsep menjelaskan hal yang berlawanan".
- L84, L271: "perangkaian pengukuran…", "Kebaruannya terletak pada perangkaian ketiga langkah" — "perangkaian" jarang dipakai; "menggabungkan / merangkai … dalam satu rancangan".
- L84: "Objek yang diestimasi adalah kemiringan hubungan antara integrasi metropolitan … dan fungsi lokal setelah massa serta karakteristik lokal diperhitungkan." — tiga lapis nomina; lebih alami: "Penelitian ini mengukur seberapa kuat integrasi metropolitan berhubungan dengan fungsi lokal setelah massa dan karakteristik lokal diperhitungkan."
- L88: "Masalah penelitian terletak pada konfigurasi hubungan dan fungsi relatif yang teramati" — abstrak; sebutkan masalah konkretnya.

### 3.7 Istilah Inggris yang punya padanan — R–S

- "locator" (L833, L1637) → "nomor halaman/tabel".
- "tenant" (L1846) → "penyewa/perusahaan penghuni".
- "manifest" (lihat 3.2).
- Istilah yang **wajar dipertahankan** (dicetak miring, konsisten): *borrowed size, agglomeration shadow, leave-one-out, what-if, screenline, contested, wild cluster bootstrap, point-in-polygon*.

### 3.8 Inkonsistensi istilah (variasi sinonim) — S

Pola humanizer §11 (*elegant variation*) dan sekaligus masalah ketelitian.

| Konsep | Varian di naskah | Contoh baris | Arah |
|---|---|---|---|
| layanan orde tinggi | "berorde tinggi", "orde tinggi", "jasa tingkat tinggi" | L80, L130, L1641 | pilih satu ("layanan berorde tinggi") |
| kota tidur | "dormitori", "kota tidur" | L249 (judul subbab), L130 | "kota tidur" |
| *borrowed size / shadow* | "peminjaman ukuran", "bayangan aglomerasi" muncul sekali | L169 | pakai istilah Inggris miring secara konsisten, atau beri padanan sekali di definisi |
| harapan | "ekspektasi", "harapan", "garis ekspektasi" | L116, L211, L504 | "fungsi harapan" |
| manfaat vs peluang | "manfaat" (konsep) dan "peluang potensial" (operasional) bercampur | L94, L102, L108, L155, L159, L1590, L1799 | tetapkan: "manfaat" hanya di teori, "peluang/profil penghasilan" di operasional; L1799 ("profil beban dan manfaat") dan L1590 masih memakai istilah lama |
| relasi vs hubungan | dipakai bergantian | banyak | boleh, tetapi "relasi" untuk arus terarah, "hubungan" untuk asosiasi statistik |

## 4. Temuan: pola tulisan AI (humanizer)

### 4.1 Penolakan di ekor kalimat dan paralelisme negatif (§9, A3) — S

Masih **42 kali** ", bukan …". Sebagian sah sebagai batas klaim di sel tabel, tetapi di prosa menjadi tik gaya. Contoh yang paling terasa:

- L84: "Sumbangannya bukan konsep baru, melainkan perangkaian…" (paralelisme *not X but Y*).
- L98: "dilaporkan sebagai triangulasi, bukan sebagai sensitivitas model yang ekuivalen".
- L126: "kematangan fungsi lokal …, bukan kesejahteraan penduduk, mutu pelayanan…, ketahanan ekonomi, atau keberhasilan pembangunan" (penolakan sekaligus daftar empat unsur).
- L357/L348: "Kemiringan inilah yang membedakan…, bukan tanda residu per unit."
- L996: "menjelaskan cara pengukuran, bukan peringkat mutu sumber".
- L1876: "menjadi konteks bagi pengukuran, bukan hasil diagnosis".

Arah: pertahankan di definisi dan tabel; di prosa, ubah sebagian menjadi kalimat positif ("Istilah kematangan dibatasi pada…").

### 4.2 Daftar tiga unsur atau lebih yang padat (§10) — S

Bab 1 memuat ±18 daftar per 1.000 kata. Contoh:

- L82: empat klausa paralel berturut-turut ("mempertahankan…, membandingkan…, memisahkan…, dan menguji…") — pola *rule of three/four* paling jelas.
- L122: enam kriteria dalam satu kalimat ("kesesuaian konstruk, cakupan spasial dan temporal, keterulangan, biaya pemerolehan, lisensi, dan hasil pemeriksaan independen").
- L1111: sembilan unsur ("konstruk, indikator, sumber, tahun, unit, polaritas, status bukti, aturan transformasi, dan batas klaim").
- L316: empat "Lapisan pertama/kedua/ketiga/keempat adalah …: …" dengan pola titik dua yang identik.
- L1641: "perumahan, pekerjaan, industri, pendidikan, perdagangan, serta fasilitas".

Arah: pecah daftar panjang menjadi dua kalimat, atau pindahkan ke tabel; untuk L316, variasikan struktur keempat lapisan.

### 4.3 Pengulangan batas klaim yang defensif (§24, hedging) — S

Gagasan "tanda residu satu kecamatan bukan bukti *shadow*; bukti dibaca dari kemiringan" diulang setidaknya di L116, L211, L348–357, L1265, L1345, dan catatan Tabel 2.2. Gagasan "penelitian observasional/asosiasional, tidak kausal" diulang di L130, L494, L1369, L1621. Pengulangan ini terasa seperti teks yang ditulis ulang berkali-kali untuk menangkis kritik.

Arah: nyatakan sekali dengan tegas di Bab 2 (definisi) dan sekali di Bab 3 (aturan); bagian lain cukup merujuk.

### 4.4 Ritme kalimat seragam (§ ritme, A13) — S

Bab 1, 2, dan 4: rata-rata ±17 kata per kalimat dengan simpangan baku hanya 6,5–7,9. Hampir tidak ada kalimat sangat pendek yang tegas atau kalimat panjang yang mengalir. Bab 3 lebih bervariasi (simpangan baku 12,8), tetapi variasinya berasal dari fragmen administratif ("Statusnya penguatan opsional.") dan kalimat daftar yang sangat panjang, bukan dari ritme argumen.

Arah: di paragraf argumen (Bab 1 §1.1, Bab 2 §2.1.6–2.1.8), selipkan kalimat pendek yang menyatakan inti klaim, lalu kalimat panjang yang menjelaskannya.

### 4.5 Pembuka kalimat berulang — R

- "Penelitian ini …" (14 kali sebagai pembuka di Bab 1–3) dan "Dalam penelitian ini, …" (4 kali di Bab 2).
- "Pada tingkat …" (8 kali di Bab 3–4).
- "Bab ini …" sebagai pembuka (L1637, L1876).

### 4.6 Penunjuk arah dan pembuka subbab (§28, §29) — R

- L169: "Konsep dalam bab ini dipakai untuk membedakan objek yang sering tercampur…"
- L247: "Subbab ini membahas penelitian empiris… Di sini, penelitian terdahulu disusun sebagai…"
- L1637: "Bab ini menjelaskan wilayah yang menjadi konteks pengukuran. Uraian disusun untuk membantu pembaca…"
- L1876: "Bab ini menyediakan batas administratif untuk pemetaan…"

Arah: langsung masuk ke isi; kalimat pengantar boleh satu, bukan dua atau tiga.

### 4.7 Kopula diganti "menjadi" (§8, A2) — R

"menjadi" muncul 50 kali, sebagian sebagai pengganti "adalah": "menjadi garis dasar" (L175), "menjadi pemeriksa" (L927), "menjadi konteks" (L1323, L1876), "menjadi penguatan". Wajar dalam bahasa Indonesia, tetapi padat di Bab 3.

### 4.8 Kepala tebal di dalam paragraf (§16) — R

Bab 3 memakai `\textbf{Tingkat 1.}`, `\textbf{Ketidakpastian.}`, `\textbf{Gerbang bukti.}`, `\textbf{Google Maps Platform.}`, `\textbf{Fungsi pekerjaan.}`, dan seterusnya. Untuk bab metode ini masih lazim, tetapi jumlahnya banyak; pertimbangkan subsubbab biasa.

### 4.9 Yang tidak ditemukan

Tidak ditemukan: kosakata AI khas (A1), pembuka klise (A5), frasa promosi (A8), atribusi samar (§5), bagian "tantangan dan prospek" (§6), em dash di prosa, kutip melengkung, emoji, kesimpulan berbunga, atau sapaan gaya *chatbot*. Tanda `--` di naskah dipakai untuk rentang angka (2014--2023, Pasal 51--55), yang benar secara tipografi.

## 5. Yang sebaiknya dipertahankan (penanda tulisan manusia)

- **Bab 4** paling alami: angka spesifik (Kosambi −12,5%, Benda +18,5%, 193.899 jiwa, 584 ribu komuter Kabupaten Bogor), nama tempat (Bojongmangu, Tambun Selatan, Cikarang Barat), dan pengakuan data yang tidak sempurna (selisih Banten, tabel bank Tangsel yang tidak tercetak). Jangan "dihaluskan".
- Kalimat yang mengakui keterbatasan secara konkret, misalnya L1029–L1033 dan L1265 ("sebarannya dilaporkan apa adanya").
- Istilah lokal yang hidup: "gugur karena kolinear" (L1357), "kota tidur", "ojek sepeda motor daring".

## 6. Temuan sampingan non-bahasa (dicatat, tidak diperbaiki)

Ditemukan saat membaca; bukan bagian audit bahasa, tetapi perlu diketahui sebelum revisi:

1. **L843** masih berbunyi "Tabel \ref{tab:bab3-sumber} memuat sumber yang dipakai beserta status ketersediaannya per Oktober 2026", padahal tabel tersebut sudah dipindah ke Lampiran B. Ringkasan sumber yang semestinya menggantikan kalimat ini tidak masuk saat pemindahan lampiran.
2. **L459** (§3.1.1) masih menyebut "model log-linear, regresi residu" sebagai teknik utama, padahal desain D10 memakai model satu tahap dan Poisson kuasi-*likelihood*; regresi residu kini hanya pemeriksa.
3. **L1733** menyatakan rumah sakit, perguruan tinggi, **dan bank umum** melayani lebih dari satu kecamatan, sedangkan L1056 menyatakan sebagian besar kantor bank melayani kebutuhan harian. Keduanya perlu diselaraskan.
4. **L448, L94, L102, L108, L155, L159, L1590, L1799** masih memakai "manfaat" pada konteks operasional yang sudah diganti menjadi "peluang potensial" dan "profil penghasilan" (lihat 3.8).
5. **L1859** menyebut 43 pusat berbasis massa dua kali dengan urutan yang membingungkan (hasil gabungan disebut sebelum ambang volume hunian diperkenalkan).

## 7. Prioritas untuk tahap revisi (setelah audit model lain dibandingkan)

1. **Bab 3**: ganti kalke metodologi utama (3.2) dengan istilah yang lazim di literatur perencanaan berbahasa Indonesia, dan pakai secara konsisten.
2. **Verba "membaca"** (3.1) dan **kolokasi Inggris** (3.3) di Bab 2 dan Bab 3.
3. **Kalimat yang mengaburkan makna** (3.5): L120, L187, L211, L225, L233, L1029, L1056.
4. **Konsistensi istilah** (3.8) dan temuan sampingan nomor 1–4.
5. **Pengulangan batas klaim** (4.3) dan **penolakan di ekor kalimat** (4.1).
6. **Ritme dan daftar** (4.2, 4.4) di Bab 1 §1.1 dan Bab 2 §2.1.
7. Sisanya (4.5–4.8, 3.7) bersifat rendah.

## 8. Batas audit

- Audit mencakup prosa, keterangan gambar, dan sebagian isi tabel Bab 1–4. Isi Tabel 2.1 (penelitian terdahulu) dan lampiran tidak diaudit baris per baris.
- Metrik dihitung otomatis dari sumber `.tex` dengan pembersihan perintah LaTeX sederhana; angkanya perkiraan.
- Penilaian "rasa terjemahan" bersifat kebahasaan dan subjektif. Arah perbaikan yang ditulis adalah usulan, bukan teks final, dan perlu dicocokkan dengan gaya pembimbing serta temuan model lain.
- Auditor yang sama (Claude Opus 5.5) menulis sebagian besar revisi naskah pada putaran 7–8. Bias penulis terhadap teksnya sendiri mungkin ada; karena itu audit dari model lain berguna sebagai pembanding.

— *Claude Opus 5.5 (Anthropic), 3 Oktober 2026*
