# TODO Revisi Pascaaudit Bab 1–4

> **Objek:** `latex/tga_pwk_jakarta_bab_1_4_final.tex` (versi `5ba3747`, PDF 3 Oktober 2026).
> **Dasar:** `latex/audit-report-tga_pwk_jakarta_bab_1_4_2026_10_03.md` (audit GPT) dan penilaian validitasnya (sesi 3 Oktober 2026). Kode C1–C7, I1–I10, dan F1–F6 merujuk audit itu.
> **Status:** belum dikerjakan. Keputusan D9 dan D10 disetujui pengguna 3 Oktober 2026 (semua mengikuti rekomendasi).
> **Hubungan dengan TODO lama:** `todo_revisi_bab_1_4.md` §9 (putaran 7) sudah selesai. File ini adalah putaran 8 dan berdiri sendiri.

Penanda: ✏️ = menyunting naskah; 🧮 = mengubah skrip atau perhitungan; 📄 = dokumentasi atau catatan sumber; ❓ = butuh keputusan pengguna.
Nomor baris `tex:NNN` mengacu ke versi `5ba3747` dan bisa bergeser setelah suntingan pertama; cari juga dengan kata kunci yang dikutip.

## Cara memakai

1. Kerjakan berurutan: **K1 → K2 → K3 → K4 → K5**. K1 dan K2 mengoreksi kesalahan, K3 mengubah desain, K4 merapikan sisa temuan, K5 menyesuaikan format.
2. Setiap butir punya **kriteria selesai**. Centang hanya bila kriteria terpenuhi dan sudah dicek di PDF.
3. Setelah tiap kelompok: kompilasi (XeLaTeX + Biber), pastikan 0 galat dan 0 rujukan tak terdefinisi, lalu commit terpisah.
4. Jangan menambah klaim baru yang tidak ada di butir. Bila menemukan masalah baru, catat di §8 dulu.

## 0. Keputusan yang dikunci untuk putaran ini

| Kode | Keputusan | Status |
|---|---|---|
| D9 | Layanan utama = **RS + PT** ("layanan orde tinggi"). Bank umum dilaporkan sebagai **domain layanan keuangan terpisah**. Label *shadow* hanya dari RS + PT. Hasil per jenis (RS, PT, bank) tetap dilaporkan. Mengubah D7. | Disetujui 3 Okt 2026 |
| D10 | Kemiringan $\theta$ diestimasi dengan **model satu tahap** (fungsi terhadap massa, X, I, Z, moderator). Residu *leave-one-out* hanya untuk profil kecamatan dan tipologi. Regresi residu terhadap $I$ menjadi pemeriksa. Ketidakpastian $\theta$ lewat *bootstrap* per kab/kota. Mengubah cara estimasi pada keputusan terkunci "inferensi Q3 lewat kemiringan residu"; prinsip "dibaca dari kemiringan, bukan dari tanda residu" tetap. | Disetujui 3 Okt 2026 |
| — | Semua keputusan terkunci lain dan D1–D8 (`todo_revisi_bab_1_4.md` §9.2) tetap berlaku kecuali yang diubah D9–D10. | — |

## 1. Kelompok 1 — Kesalahan yang membuat eksekusi gagal atau melanggar aturan

- [ ] **1.1 (I3) Volume nonhunian nol.** 🧮✏️
  - Fakta: 6 kecamatan bervolume NRES **tepat 0** (antara lain Tenjolaya, Cijeruk, Cariu); $\ln F_P$ dengan $c_P=0$ tidak terdefinisi (`tex:1364`).
  - Tindakan: ganti model pekerjaan menjadi model yang menerima nol (misalnya Poisson kuasi-*likelihood* pada volume, sejalan dengan D10), atau tetapkan $c_P$ berpijak pada satuan (misalnya 1 sel × volume minimum) dan uji sensitivitasnya. Tetapkan juga target prediksi balik (rata-rata vs median geometrik).
  - Jangan mengeluarkan kecamatan nol diam-diam.
  - **Selesai bila:** rumus Langkah 4 terdefinisi untuk seluruh 141 kecamatan, alasan pemilihan tertulis, dan daftar 6 kecamatan nol disebut di Bab 3 atau catatan sumber GHSL.

- [ ] **1.2 (C7) Penyimpanan turunan Google dapat dibalik.** ✏️
  - Fakta: $F_i=e^{R_i}(\hat F_i+c)-c$; $\hat F_i$ dapat dibentuk ulang dari data publik, sehingga residu per kecamatan memungkinkan deduksi jumlah POI (bertentangan dengan §13.1 syarat khusus Places Aggregate API). Lokasi: `tex:1184` ("dalam 30 hari, jumlah tersebut diubah menjadi residu").
  - Tindakan: simpan **hanya statistik agregat** (kemiringan, korelasi pemeriksa, selang). Tidak ada nilai per kecamatan yang disimpan. Nyatakan bahwa lapisan Google tidak menghasilkan profil kecamatan. Podes tetap inti; K3 tetap jalur tanpa Google.
  - **Selesai bila:** desain kepatuhan Bab 3, Tabel 3.4 (baris Google), dan subbab etika tidak lagi menyebut penyimpanan nilai per kecamatan.

- [ ] **1.3 (I10) Prosedur raster tidak sesuai teks.** ✏️🧮
  - Fakta: `tex:1090` menulis GHSL "diproyeksikan ke UTM 48S… dengan bobot luas sel". Skrip `latex/figures/scripts/zonal.py` menjumlahkan sel EPSG:4326 dengan aturan pusat sel (`all_touched=False`).
  - Tindakan: pilih salah satu. (a) Tulis ulang teks sesuai prosedur nyata dan sebut sebagai pendekatan, atau (b) ubah skrip ke agregasi berbobot pecahan luas sel yang menjaga total. Rekomendasi: (a) untuk naskah pra-TA, ditambah uji sensitivitas `all_touched=True` pada beberapa kecamatan kecil.
  - **Selesai bila:** teks Bab 3, catatan dataset GHSL, dan skrip menyatakan prosedur yang sama.

- [ ] **1.4 (I10) Batas kecamatan: kode cocok ≠ garis cocok.** ✏️📄
  - Lokasi: `tex:924`, `tex:1707` ("K2 tidak terpicu").
  - Tindakan: ubah klaim menjadi "kode cocok; kesesuaian garis batas 2020 dengan batas 2024 belum diperiksa". Tambahkan pemeriksaan ringan: bandingkan luas poligon HDX dengan luas kecamatan pada WSM Lampiran 3, lalu tandai selisih besar.
  - **Selesai bila:** klaim K2 tidak lagi melebihi bukti, dan hasil perbandingan luas tercatat di catatan dataset GHSL.

## 2. Kelompok 2 — Klaim yang berlebihan

- [ ] **2.1 (C1) $I^{DKI}$ bukan persentase komuter ke DKI.** ✏️
  - Lokasi: `tex:1292`, `tex:1295`, `tex:1543`, serta Bab 1 dan Tabel 3.4/3.7.
  - Tindakan: ganti nama menjadi **"indeks WSM berbobot orientasi DKI kabupaten/kota"**. Jelaskan perbedaan penyebut: $O_k$ adalah pangsa di antara komuter lintas kab/kota termasuk ke luar Jabodetabek, sedangkan WSM memuat perjalanan antarkecamatan di dalam kab/kota. Tetap spesifikasi kembar (D1), tetapi kesimpulannya dibatasi: menguji pembobotan konteks DKI, bukan mengukur tujuan DKI per kecamatan.
  - **Selesai bila:** pencarian "integrasi khusus DKI" tidak lagi menemukan klaim persentase ke DKI.

- [ ] **2.2 (C3) Residu tidak dijamin berpusat nol dan terbelah dua.** ✏️
  - Lokasi: `tex:133`, `tex:221`.
  - Tindakan: hapus "kira-kira separuh unit pasti bertanda negatif" dan "berpusat di sekitar nol menurut konstruksinya". Pertahankan pesan bahwa tanda residu satu unit bukan bukti *shadow* atau *borrowed size*, karena tolok ukurnya relatif. Rencanakan pelaporan distribusi residu yang sebenarnya.
  - **Selesai bila:** tidak ada lagi klaim matematis tentang pemusatan atau pembagian tanda residu.

- [ ] **2.3 (C4) "Bocor ke inti" dan "arah sebaliknya tidak menghasilkan tanda positif".** ✏️
  - Lokasi: `tex:235` (bocor), `tex:1450` (tanda positif).
  - Tindakan:
    - `tex:235`: ganti "permintaan itu bocor ke inti" dengan pernyataan bersyarat. Data komuter kerja/sekolah tidak mengamati perjalanan berobat atau transaksi layanan, sehingga kebocoran permintaan adalah tafsir yang belum teramati.
    - `tex:1450`: hapus klaim bahwa tanda positif kebal kausalitas terbalik. Tanda positif tetap asosiasional (kota baru, jaringan, dan seleksi lokasi dapat menghasilkannya).
    - Tambahkan bahwa penyebut WSM memuat pelajar, sehingga kurangnya PT lokal dapat menaikkan $I$. Domain layanan juga tidak bebas kausalitas terbalik.
  - **Selesai bila:** Bab 2 dan Langkah 6 tidak menyiratkan identifikasi arah sebab.

- [ ] **2.4 (I10) Satuan `Luas_IUKI` ditulis sebagai fakta.** ✏️
  - Lokasi: `tex:1893`, `tex:1947`.
  - Tindakan: tulis "kemungkinan besar hektare (disimpulkan dari luas poligon; tidak didokumentasikan)".
  - **Selesai bila:** Bab 4 dan Tabel audit Bab 4 menandai satuan ini sebagai inferensi.

## 3. Kelompok 3 — Perubahan desain (D9, D10, I4, I6)

- [ ] **3.1 (I1, D9) Komposisi layanan.** ✏️
  - Fakta: bank = 1.295 dari 1.846 fasilitas (70%) di tujuh kab/kota.
  - Tindakan:
    - Bab 1–3: layanan utama = RS + PT ("layanan orde tinggi"); bank = domain layanan keuangan, dilaporkan terpisah. Lokasi utama: `tex:962` (Tabel 3.4), `tex:1122` (konstruksi proksi), Bab 1 §1.4, Tabel 2.2, P1.
    - Label *shadow* hanya dari RS + PT; kemiringan negatif yang hanya muncul pada bank dibaca sebagai pola layanan keuangan.
    - Hasil per jenis (RS, PT, bank) tetap dilaporkan; catat bahwa jumlah per kecamatan kecil dan banyak nol (siapkan K4).
    - K9 (bank Tangsel dari edisi 2025) kini hanya memengaruhi domain bank; sesuaikan Tabel 3.2.
    - Bab 4 Tabel 4.3: tambahkan kolom RS + PT atau catatan komposisi.
  - **Selesai bila:** tidak ada lagi "RS + PT + bank" sebagai layanan utama di Bab 1–4, dan gerbang *shadow* menyebut RS + PT.

- [ ] **3.2 (C2, D10) Estimasi kemiringan satu tahap.** ✏️
  - Lokasi: `tex:357` (model konseptual Bab 2), Langkah 4 dan 6 Bab 3, Tabel 3.7 keterlacakan, Gambar 2.1 dan 3.2.
  - Tindakan:
    - Tulis persamaan utama: $\ln \mathrm{E}[F_i] = \alpha + \beta \ln S_i + \gamma^\top X_i + \theta I_i + \lambda\,\mathrm{Inti}_i + \phi(I_i\times\mathrm{Inti}_i) + \delta^\top Z_i$ (binomial negatif untuk layanan; untuk pekerjaan mengikuti butir 1.1), dengan suku interaksi kawasan industri pada domain pekerjaan.
    - Residu *leave-one-out* hanya untuk profil kecamatan dan tipologi.
    - Regresi residu terhadap $I$ menjadi pemeriksa, dan bila dipakai harus memuat $S$ dan $X$ pada tahap kedua.
    - Ketidakpastian $\theta$: *bootstrap* per kab/kota; sebut bahwa galat baku *robust* heteroskedastisitas tidak kebal korelasi spasial (I8).
    - Hapus klaim bahwa kemiringan residu sudah mengendalikan $S$ dan $X$ (`tex:357`).
  - **Selesai bila:** Bab 2 dan Bab 3 konsisten bahwa $\theta$ berasal dari model satu tahap, dan Tabel 2.2 serta gerbang tetap membaca kemiringan, bukan tanda residu.

- [ ] **3.3 (I4) Sampel layanan 129 kecamatan.** ✏️
  - Lokasi: `tex:598` (K1), Bab 1 batasan, Langkah 6, Bab 4 subbab pusat berbasis massa.
  - Tindakan:
    - Model layanan memakai 129 kecamatan; model pekerjaan tetap 141.
    - Semua perbandingan antardomain (P3, kategori campuran) memakai 129 kecamatan yang sama.
    - Model pekerjaan dijalankan juga pada 129 kecamatan sebagai pemeriksaan pengaruh sampel.
    - K1 diubah: **tidak ada** profil layanan pengganti dari Google/OSM untuk Kota Bekasi. Kota Bekasi dideskripsikan dari tabel "banyaknya kelurahan yang memiliki".
    - Bab 4: sebut bahwa 8 dari 36 pusat berpenduduk P75 berada di Kota Bekasi dan tidak masuk analisis layanan.
  - **Selesai bila:** setiap klaim layanan menyebut cakupan 129, dan K1 di Tabel 3.2 serta Gambar 3.1 sesuai.

- [ ] **3.4 (I6) Agregasi dan spesifikasi moderator.** ✏️
  - Lokasi: `tex:995` (agregasi tingkat 2), Langkah 6, Tabel 3.4.
  - Tindakan:
    - Agregasi kab/kota: $R_k=\ln(\sum F + c)-\ln(\sum \hat F + c)$ (rasio jumlah), bukan rata-rata residu kecamatan.
    - Setiap interaksi ditulis bersama efek utamanya.
    - Batasi parameter ≤ ±10. X: kepadatan, lereng, status kota/kabupaten. Z: kota baru, pangsa lahan terbangun. Moderator: status inti; kawasan industri hanya untuk pekerjaan. **Keluarkan tahun pembentukan daerah otonom** (praktis hanya membedakan Tangerang Selatan); sesuaikan Tabel 2.4 dan Tabel 3.4.
    - Spesifikasi efek tetap kab/kota: tulis bahwa status kota/kabupaten gugur karena kolinear.
    - P4 (spline) hanya dijalankan bila sebaran $I$ memadai; bila tidak, dilaporkan tidak dapat diuji.
  - **Selesai bila:** persamaan lengkap tertulis, daftar kovariat final ada di satu tempat, dan aturan agregasi tingkat 2 tertulis.

## 4. Kelompok 4 — Temuan audit lain yang belum masuk K1–K3

- [ ] **4.1 (C5) Gerbang *shadow* lintas tingkat.** ✏️
  - Tindakan: tegaskan bahwa waktu tempuh arus bebas ke Bundaran HI adalah hambatan potensial menuju satu titik. Kecocokan urutan dengan beban tingkat 2 hanya pemeriksaan agregat dan tidak memvalidasi kecamatan. Ketergantungan kab/kota adalah konteks dan tidak boleh sendirian meloloskan label *shadow* untuk setiap kecamatan di kab/kota tersebut. Bila syarat unit gagal, gunakan "terintegrasi tetapi tertinggal" atau "tidak terselesaikan".
  - **Selesai bila:** gerbang di Bab 2 dan Langkah 6 memuat aturan ini.

- [ ] **4.2 (C6) Definisi selang ketidakpastian.** ✏️
  - Tindakan: tetapkan objek selang (selang prediksi per unit untuk tipologi; selang *bootstrap* untuk $\theta$), tingkat kepercayaan (misalnya 90%), dan cara hitung. Lunakkan kalimat "banyak unit diperkirakan tidak terselesaikan" (`tex:1503`) menjadi kemungkinan, bukan ekspektasi. Bedakan unit tidak terselesaikan karena ketidakpastian dari unit dengan data hilang.
  - **Selesai bila:** satu paragraf definisi selang ada di Langkah 6, dan Tabel 2.2 merujuknya.

- [ ] **4.3 (I2) Nama domain pekerjaan.** ✏️
  - Tindakan: sebut indikatornya "stok bangunan nonhunian di luar kawasan industri formal" secara konsisten. Asumsi stok 2018/2020 berlaku hingga 2024 ditulis sebagai asumsi, terutama untuk kawasan yang tumbuh cepat. P2 dirumuskan sebagai stok nonhunian di sekitar kawasan industri yang melampaui tolok ukur, bukan dekonsentrasi pekerjaan manufaktur (gagasan audit #5).
  - **Selesai bila:** Bab 1, P2, dan Tabel 3.4 memakai nama yang sama.

- [ ] **4.4 (I5) Uji P3.** ✏️
  - Lokasi: `tex:1611`.
  - Tindakan: P3 diuji dengan diagram pencar residu dua domain pada 129 kecamatan beserta ketidakpastiannya, lalu identifikasi kasus berlawanan arah. Korelasi hanya ringkasan. Tetapkan lebih dulu apa yang dihitung sebagai "berlawanan arah".
  - **Selesai bila:** Tabel 3.7 dan paragraf P1–P4 diperbarui.

- [ ] **4.5 (I7) Pisahkan ketahanan, triangulasi, dan perubahan cakupan.** ✏️
  - Tindakan: daftar Langkah 7 dibagi tiga: ketahanan pada estimand yang sama (ambang, komposisi, model); triangulasi sumber (Podes 2025, GTFS); perubahan cakupan (NRES total vs di luar kawasan industri).
  - **Selesai bila:** daftar Langkah 7 tersusun dalam tiga kelompok itu.

- [ ] **4.6 (I8) Aturan keputusan yang dapat direproduksi.** ✏️
  - Tindakan: beri kriteria untuk "autokorelasi kuat" (misalnya Moran's I residu dengan p < 0,05 pada matriks *queen*), "diagnostik buruk", "salah klasifikasi besar" (K5), dan "urutan sejalan" (misalnya korelasi peringkat Spearman ≥ 0,5 pada 8 kab/kota). Sebut bahwa efek tetap kab/kota tidak menyelesaikan ketergantungan spasial.
  - **Selesai bila:** setiap pemicu K4, K5, K8, dan pemeriksaan beban punya angka atau aturan tertulis.

- [ ] **4.7 (I9) Profil penghasilan bukan manfaat integrasi.** ✏️
  - Lokasi: `tex:992`.
  - Tindakan: ubah nama menjadi "profil penghasilan komuter"; akses kumulatif disebut peluang potensial. Jangan menyebut keduanya manfaat yang diatribusikan ke Jakarta.
  - **Selesai bila:** Tabel 3.5 dan Langkah 5 memakai nama baru.

- [ ] **4.8 (gagasan audit #3) Fasilitas di kecamatan tetangga.** ✏️
  - Tindakan: tambahkan ke Tabel 2.4 penjelasan alternatif "fasilitas di kecamatan tetangga (wilayah layanan melintasi batas)". Cara memeriksa: pemeriksaan terbatas pada kecamatan defisit dan surplus besar, dengan melihat fasilitas Podes di kecamatan yang berbatasan. Tidak menjadi domain atau indeks baru.
  - **Selesai bila:** Tabel 2.4 dan Langkah 6 memuat penjelasan ini.

- [ ] **4.9 (gagasan audit #4, #6) Tingkat kesimpulan.** ✏️
  - Tindakan: tambahkan satu paragraf di Bab 3 tentang tiga tingkat kesimpulan: sistem (θ), tempat (profil kecamatan dan 43 pusat berbasis massa), dan kewenangan (ringkasan kab/kota). Koefisien sistem tidak membuktikan status tiap kecamatan.
  - **Selesai bila:** paragraf ada di subbab batas klaim Bab 3.

- [ ] **4.10 (F6) UU 151/2024.** ✏️📄
  - Tindakan: tambah entri bib UU 151/2024 (perubahan atas UU 2/2024; nomenklatur jabatan, Pasal 70A–70D). Lengkapi catatan kaki Bab 1 dan Bab 4 tanpa mengubah pemakaian nama "DKI Jakarta" sebagai nama wilayah statistik. Buat catatan sumber di `source/official-document/` bila teks UU diunduh.
  - **Selesai bila:** catatan kaki dan bibliografi memuat UU 151/2024.

## 5. Kelompok 5 — Format dan ruang naskah

- [ ] **5.1 (F5) Inkonsistensi kecil.** ✏️
  - Tabel 3.1 (`tex:497`): hapus "serta perubahan pada seri yang sebanding" pada Q2.
  - `tex:1498`: "tersier" → "tertil".
  - Gambar 3.1 (`bab3_keputusan_cadangan.mmd`): tampilkan K1 dan K6 sebagai jalur aktif; perbarui setelah 3.1 dan 3.3.
  - Gambar 2.1: perbesar teks atau ringkas kotak.
  - Peta arus G4.3: tambahkan di caption bahwa garis bukan rute perjalanan.
  - Istilah "relatif independen" dan "periferi lemah": batasi sesuai definisi operasional di Tabel 2.2.
  - **Selesai bila:** keenam butir dicek di PDF.

- [ ] **5.2 (F2) Huruf tabel ≥ 10 pt.** ✏️
  - Fakta: template mensyaratkan ≥10; tabel memakai `\footnotesize` (±9 pt).
  - Tindakan: naikkan ke ukuran ≥10 pt; ringkas isi atau ubah orientasi tabel panjang (Tabel 2.1, 3.2–3.5, tabel Bab 4).
  - **Selesai bila:** `pdffonts`/ekstraksi ukuran huruf pada sampel tabel menunjukkan ≥10 pt.

- [ ] **5.3 (F4) Tata letak template.** ✏️
  - Fakta: template DOCX memakai 12 pt dan spasi 1,5; naskah LaTeX 11 pt, spasi 1,18.
  - Tindakan: ubah kelas ke 12 pt dan spasi 1,5 (atau dokumentasikan arahan pembimbing bila tidak). Tambahkan daftar tabel dan daftar gambar.
  - **Selesai bila:** preamble sesuai template dan daftar tabel/gambar tampil.

- [ ] **5.4 (F1) Latar belakang ≤ 2 halaman.** ✏️
  - Fakta: kini sekitar 3 halaman (PDF hlm. 5–7).
  - Tindakan: pindahkan rincian operasi, tipologi, dan gerbang ke Bab 2–3; pertimbangkan memindahkan Gambar 1.1 ke subbab metode Bab 1.
  - **Selesai bila:** §1.1 ≤ 2 halaman setelah 5.3 diterapkan.

- [ ] **5.5 (F3) Ruang kata.** ✏️
  - Fakta: batas 20.000 kata (tanpa daftar pustaka dan lampiran); Bab 1–4 kini sekitar 19.400 kata termasuk tabel.
  - Tindakan: target Bab 1–4 sekitar 12.000–14.000 kata. Pindahkan ke lampiran: Tabel 2.1 versi panjang, tabel cadangan K1–K9, rincian kepatuhan Google, dan rincian status bukti. Kerjakan **setelah** K1–K4 agar tidak memangkas teks yang masih berubah.
  - **Selesai bila:** hitungan kata Bab 1–4 (tanpa lampiran) ≤ 14.000 dan alasan tiap pemindahan dicatat.

## 6. Matriks cakupan audit

Setiap kode audit harus muncul di sini dengan status akhir.

| Kode audit | Butir | Penilaian validitas | Status |
|---|---|---|---|
| C1 | 2.1 | Valid | [ ] |
| C2 | 3.2 | Valid (bobot diturunkan) | [ ] |
| C3 | 2.2 | Valid | [ ] |
| C4 | 2.3 | Valid | [ ] |
| C5 | 4.1 | Valid | [ ] |
| C6 | 4.2 | Valid sebagian | [ ] |
| C7 | 1.2 | Valid | [ ] |
| I1 | 3.1 | Valid | [ ] |
| I2 | 4.3 | Valid | [ ] |
| I3 | 1.1 | Valid (6 nol tepat) | [ ] |
| I4 | 3.3 | Valid | [ ] |
| I5 | 4.4 | Valid | [ ] |
| I6 | 3.4 | Valid | [ ] |
| I7 | 4.5 | Valid sebagian | [ ] |
| I8 | 4.6 | Valid | [ ] |
| I9 | 4.7 | Valid | [ ] |
| I10 | 1.3, 1.4, 2.4 | Valid | [ ] |
| F1 | 5.4 | Valid | [ ] |
| F2 | 5.2 | Valid | [ ] |
| F3 | 5.5 | Valid (cara hitung prodi belum pasti) | [ ] |
| F4 | 5.3 | Valid | [ ] |
| F5 | 5.1 | Valid | [ ] |
| F6 | 4.10 | Valid | [ ] |
| Gagasan #3 | 4.8 | Diterima | [ ] |
| Gagasan #4, #6 | 4.9 | Diterima | [ ] |
| Gagasan #5 | 4.3 | Diterima | [ ] |
| Gagasan #1, #2, #7 | — | Tidak ditindaklanjuti: #1 menulis ulang Q3; #2 dan #7 sudah tercakup desain | — |
| Perkiraan jam kerja | — | Diabaikan: tidak dapat diverifikasi | — |

## 7. Penutup putaran

- [ ] Kompilasi final: 0 galat, 0 rujukan/sitasi tak terdefinisi; periksa PDF per halaman.
- [ ] Gambar `.mmd` yang terdampak (2.1, 3.1, 3.2) dirender ulang.
- [ ] Evaluasi `evaluasi_substansi_dan_eksekusi_bab_1_4_draf.md` §18: D9–D10, ringkasan perubahan, batas.
- [ ] `HANDOFF.md` diperbarui.
- [ ] Commit per kelompok (K1, K2, K3, K4, K5, penutup).
- [ ] Bahasa: `humanizer-academic-id` + EYD pada bagian yang berubah.

## 8. Temuan baru selama putaran

(Catat di sini masalah yang muncul saat mengerjakan, beserta kelompok tujuannya.)
