---
session_id: 2026-10-02-01
parent_session_id: null
branch: main
commits_since_parent: 0
date: 2026-10-02T19:53:42+07:00
---

# Handoff: Revisi Naskah TGA Bab 1–4 (Jabodetabek)

> Baca file ini lebih dulu, lalu `AGENTS.md` di root. Sesi cloud **tidak** membawa memori lokal; semua konteks ada di file dalam repo ini.
>
> **Sifat dokumen ini:** penjaga konteks, bukan naskah perintah. Rencana di sini disusun sebelum isi data dibaca. Jelajahi datanya, bertanyalah kepada pengguna, dan usulkan perubahan rencana bila perlu.

## Active goal

Merevisi naskah pra-TA `latex/tga_pwk_jakarta_bab_1_4_final.tex` (Bab 1–4; *Borrowed Size atau Agglomeration Shadow?*) berdasarkan evaluasi 27 September – 2 Oktober 2026.

Pra-TA hanya mewajibkan Bab 1–4 tanpa eksekusi analisis. Targetnya naskah yang desainnya jelas dan dapat dipertahankan, bukan hasil perhitungan.

## Where we left off

- [x] Evaluasi substansi dan eksekusi selesai: `output/naskah/evaluasi_substansi_dan_eksekusi_bab_1_4_draf.md` (§2 keputusan pengguna, §3 status per butir, C6 draf tabel operasionalisasi, §13 keputusan).
- [x] Peta kerja revisi tersusun: `output/naskah/todo_revisi_bab_1_4.md`.
- [x] Sumber non-BPS diunduh dan diberi catatan sumber (UU 2/2024, Perpres 60/2020, BPTJ 2024, Kemenperin, GTFS, GHSL).
- [x] Sumber BPS ada di repo (commit `14fccdd` dan `34af8cf`): Komuter 2014/2019/2023, WSM 2024, PDRB, Dalam Angka provinsi dan delapan kab/kota, Statistik Potensi Desa 2024/2025 untuk tujuh kab/kota, Keadaan Angkatan Kerja 2023, serta data upah (DKI, Jawa Barat, dan sebagian Banten).
- [x] Data dari laptop lain sudah di-push (`34af8cf`) dan sudah dicocokkan dengan TODO §0.1.
- [ ] **Masih kurang:**
  - 12 *Kecamatan Dalam Angka* Kota Bekasi, sebagai pengganti publikasi Podes yang tidak ada;
  - tabel upah formal Banten (tidak tersedia);
  - batas kecamatan (HDX), yang sengaja tidak di-commit karena ukurannya.
- [ ] **Repo perlu dirapikan** (TODO §0.5): 38 PDF BPS terduplikasi antara `source/dataset/` dan `source/official-document/`. Pakai salinan `official-document/`, yang punya catatan sumber.
- [ ] **Belum ada satu pun perubahan pada `.tex`.**

## Working mode

Pengguna menginginkan sesi yang eksploratif dan dialogis:

1. **Jelajahi dulu.** Isi publikasi dan data belum pernah dibaca agen: tabel apa yang tersedia, pada unit apa, untuk tahun berapa. Banyak butir rencana bergantung pada jawabannya.
2. **Laporkan dan diskusikan.** Sampaikan temuan dan artinya bagi desain. Bertanya kepada pengguna itu diharapkan (pakai alat tanya bila ada).
3. **Edit per bagian**, setelah arahnya disepakati.
4. **Jaga konteks.** Jika rencana berubah, perbarui TODO dan file evaluasi supaya sesi berikutnya tidak kehilangan jejak.

**Terkunci (keputusan pengguna; jangan diubah tanpa bertanya):** lihat daftar "Terkunci" di awal TODO dan evaluasi §13.

**Lentur:** indikator dan sumber spesifik, isi tabel operasionalisasi, bentuk model, isi Bab 4, daftar gambar, dan urutan kerja.

## Next concrete action

**Di lokal, sebelum membuka sesi cloud:**
1. Commit dan push `HANDOFF.md`, `output/naskah/todo_revisi_bab_1_4.md`, dan `output/naskah/evaluasi_substansi_dan_eksekusi_bab_1_4_draf.md`. Ketiganya belum ada di GitHub.
2. Pasang setup script OCR di pengaturan environment cloud (lihat "Cloud environment").
3. Opsional: unduh 12 *Kecamatan Dalam Angka* Kota Bekasi (tautan di TODO §0.1), dan putuskan perapian duplikat (TODO §0.5).

**Di sesi cloud, usulan langkah pertama (bukan urutan wajib):**
1. Baca `HANDOFF.md`, `AGENTS.md`, lalu bagian awal `output/naskah/todo_revisi_bab_1_4.md`.
2. Inventarisasi apa yang benar-benar ada di `source/` dan baca publikasi kuncinya. Pertanyaan yang perlu dijawab:
   - Berapa jumlah kecamatan non-DKI?
   - Bagaimana WSM 2024 mendefinisikan "inti", dan tabel apa yang tersedia per kecamatan?
   - Apakah *Statistik Komuter* memuat tabel asal–tujuan kab/kota serta durasi dan biaya?
   - Tabel fasilitas apa yang ada di *Statistik Potensi Desa*, dan apakah sebanding antar kab/kota?
3. Laporkan temuannya kepada pengguna, dan usulkan penyesuaian tabel operasionalisasi (evaluasi C6) bila perlu.
4. Setelah disepakati, mulai revisi. Bab 3 disarankan lebih dulu karena Bab 1, 2, dan 4 mengacu ke desainnya.
5. **Figure:** agen hanya mengedit diagram `.mmd`. Peta GIS dibuat manual oleh pengguna; agen memasang `\GambarPlaceholder` dengan caption dan label final (TODO §7).

**Prompt pembuka yang disarankan untuk sesi cloud:**

> Baca `HANDOFF.md` dan `AGENTS.md`. Kita akan merevisi `latex/tga_pwk_jakarta_bab_1_4_final.tex`. Mulailah dengan menjelajahi data dan publikasi di `source/` yang relevan, lalu laporkan apa yang kamu temukan dan apa artinya bagi rencana di `output/naskah/todo_revisi_bab_1_4.md`. Diskusikan dengan saya sebelum mengedit, dan silakan bertanya kapan saja. Saya memberi izin mengedit `.tex` dan `latex/references.bib` per bagian setelah arahnya kita sepakati. Jangan ubah keputusan yang ditandai terkunci tanpa bertanya; selebihnya boleh kamu usulkan perubahannya.

## Cloud environment

Menurut dokumentasi Claude Code (dicek 2 Oktober 2026), sesi cloud berjalan di VM Ubuntu 24.04 x86_64 dengan 4 vCPU, 16 GB RAM, dan 30 GB disk. `pdftotext`, Tesseract, `ocrmypdf`, dan LaTeX **tidak** terpasang bawaan, tetapi dapat dipasang.

**Setup script.** Pengguna mengisinya di pengaturan environment di claude.ai/code. Skrip berjalan sebagai root sebelum sesi dimulai, dan hasilnya di-*cache* bila selesai dalam sekitar 5 menit:

```bash
#!/bin/bash
apt update && apt install -y poppler-utils tesseract-ocr tesseract-ocr-ind ocrmypdf || true
pip install pymupdf pdfplumber pandas openpyxl || true
```

- Akses jaringan bawaan ("Trusted") sudah mengizinkan arsip Ubuntu dan PyPI, jadi skrip di atas berjalan tanpa pengaturan tambahan.
- Jika setup script belum dipasang, agen boleh menjalankan perintah yang sama di tengah sesi. Hasilnya tidak terbawa ke sesi berikutnya.
- Agen sebaiknya memeriksa dulu dengan `which pdftotext tesseract ocrmypdf` dan `check-tools`.

**Cara membaca tabel yang berupa gambar** (banyak publikasi BPS):
1. Coba `pdftotext -layout` lebih dulu. Sebagian tabel punya lapisan teks, misalnya Tabel 7.1 BPTJ dan *Kota Bekasi Dalam Angka*.
2. Bila tidak ada teks, jalankan OCR: `ocrmypdf -l ind+eng --sidecar hasil.txt masuk.pdf keluar.pdf`. PDF asli tidak boleh ditimpa; tulis turunannya sebagai berkas terpisah (`source/AGENTS.md`).
3. Alat baca PDF milik agen (per halaman, visual) dapat membaca tabel gambar secara langsung. Ini cara yang paling andal untuk tabel kecil, dan dipakai untuk memeriksa hasil OCR.
4. **Angka hasil OCR wajib diverifikasi.** Cocokkan jumlah per kolom dengan baris total pada tabel (misalnya baris "KOTA JAKARTA UTARA"), dan periksa sampel secara visual. Angka yang belum lolos pemeriksaan tidak boleh masuk naskah.
5. Catat halaman PDF dan halaman isi untuk setiap tabel yang diambil.

**Yang tidak ikut ke cloud:**
- Pengaturan tingkat pengguna di `~/.claude/` (memori, skill pribadi seperti `handoff` dan `graphify`, hook) tidak terbawa. Yang terbawa hanya isi repo, termasuk `AGENTS.md`.
- Domain di luar daftar bawaan (misalnya `data.humdata.org` dan server GHSL) perlu ditambahkan lewat akses jaringan "Custom" atau "Full". Situs BPS tetap menolak unduhan otomatis.
- LaTeX dapat dipasang (`texlive-xetex`, `biber`), tetapi ukurannya besar sehingga berisiko melewati batas 5 menit, dan font Times New Roman tidak tersedia. Rencana aman tetap: kompilasi di lokal.

## Open questions

- **OD sintetis** (gravitasi/IPF; `tex:1004-1010`, `tex:1470-1481`): opsional atau dihapus? Rantai inti kini memakai OD kab/kota teramati dan WSM.
- **Nama wilayah inti:** "DKI Jakarta" atau "Daerah Khusus Jakarta"? Data Kemenperin 2025 sudah memakai nama baru.
- **Satu sumber kebenaran:** file `.tex` per-bab menduplikasi file gabungan dan sudah tidak sinkron. Dihapus atau dibuat ulang?
- **Kota Bekasi:** publikasi Podes tidak ditemukan. Penggantinya (*Kecamatan Dalam Angka 2025*; Tabel 4.2.3 *Kota Bekasi Dalam Angka 2025*) belum dicek keterbandingannya.
- **Tabel siap-*join* untuk QGIS:** bolehkah agen membuat CSV per kecamatan di `calculation/`? Perlu izin eksplisit.
- **Pembimbing:** konfirmasi Rendy Bayu Aditya belum tercatat di vault.
- **Duplikat PDF** di `source/dataset/` dan `source/official-document/`: salinan mana yang dihapus? (TODO §0.5)
- **Isi publikasi** belum pernah dibaca agen, kecuali cuplikan yang tercatat di catatan sumber. Temuannya mungkin mengubah sebagian rencana.

## Decisions made this session

Rinciannya ada di evaluasi §2–§3 dan §13.

- **Sikap data:** sumber terbuka dan OSM lebih dulu. Data resmi dipakai bila terbuka. Tidak membeli data BPS dan tidak bergantung pada pengajuan.
- **Judul** memakai "Jabodetabek". Kabupaten Cianjur tidak dicakup; konteks Kawasan Aglomerasi (UU 2/2024 Pasal 51) ditempatkan di Bab 1.
- **Desain dua tingkat:** kecamatan non-DKI (utama; Q2–Q3) dan kab/kota (pendalaman; Q1–Q2).
- **Dua domain utama:** layanan dan pekerjaan. Usulan proksi saat ini (lentur):
  - layanan: jumlah fasilitas Podes 2024, Google Places, dan SIRS/PDDikti;
  - pekerjaan: volume nonhunian GHSL R2023A (epoch 2020, interpolasi dari observasi 2018), dengan pangsa kawasan industri sebagai pembeda.
- **Inferensi Q3** adalah kemiringan residu terhadap integrasi di dalam Jabodetabek. Tipologi hanya ringkasan.
- **Pemilihan pusat** berdasarkan massa, bukan fungsi.
- **Satu indikator satu peran:** beban tidak memakai orientasi arus.
- **Kawasan hunian** dapat menjadi korban *shadow*; domain layanan menjadi pembedanya.
- **Alat:** CCTV untuk *screenline* terarah di batas DKI. SUMO keluar, kecuali dikombinasikan dengan CCTV. Web GIS dan *what-if* tetap, tetapi dijelaskan sekali saja di Bab 3.
- **Google Places** hanya untuk menghitung. Yang disimpan *place ID*, kode kecamatan, dan kategori sendiri.
- **Perubahan antarperiode** sejauh ini hanya didukung data komuter 2014/2019/2023. GHSL dan seri Podes tidak mendukungnya.
- **Ditolak pengguna (jangan diangkat lagi):** kritik "skala" *borrowed size*, dan perluasan wilayah ke Cianjur.
- **Preferensi kerja:** rencana tidak boleh mengekang. Eksplorasi dan diskusi diutamakan; yang penting konteks tidak hilang.

## Dragons

- **Izin edit.** `AGENTS.md` melarang mengedit naskah tanpa niat edit eksplisit. Prompt pembuka di atas sudah memuat izin itu, dengan syarat arah tiap bagian disepakati dulu.
- **Nomor baris bergeser.** Rujukan `tex:NNN` mengacu ke versi 27 September. Setelah edit pertama, cari dengan kata kunci.
- **Tabel BPS berupa gambar.** Banyak PDF BPS tidak punya lapisan teks pada tabelnya, sehingga `pdftotext` saja tidak cukup. Ikuti bagian "Cloud environment" di atas: pasang OCR, baca visual, dan verifikasi angka terhadap baris total.
- **Kompilasi LaTeX.** Naskah memakai XeLaTeX + Biber dan font Times New Roman, dan lingkungan cloud mungkin tidak punya keduanya. `AGENTS.md` juga melarang build tanpa permintaan. Rencana aman: edit di cloud, kompilasi di lokal.
- **Situs BPS menolak `curl` (HTTP 403).** Unduhan BPS dilakukan pengguna.
- **Sparse checkout lokal.** Di mesin lokal, PDF dan ZIP terlacak git tetapi tidak tampil di disk; ambil dengan `git show "HEAD:<path>" > berkas`. Klon cloud biasa memuat semuanya.
- **Batas kecamatan belum ada di vault.** geoBoundaries tidak punya ADM3 untuk Indonesia. Sumbernya HDX COD-AB (BPS, 2020), berukuran 219–498 MB, sehingga tidak boleh di-commit (TODO §0.4).
- **Bibliografi salah metadata.** `otsuka2025`, `sadewoetal2021`, `sadewoetal2023`, dan `burgermeijers2016` perlu diperbaiki (TODO §6).
- **Figure tanpa skrip.** PNG diagram dibuat dari `.mmd` tanpa perintah render tercatat, dan peta Bab 4 tidak punya skrip SVG→PNG.
- **Klaim yang belum diverifikasi** di evaluasi ditandai "perlu dicek". Jangan diperlakukan sebagai fakta.

## References

- **Peta kerja:** `output/naskah/todo_revisi_bab_1_4.md` (awal file: terkunci vs lentur; §0 data; §7 gambar dan placeholder).
- **Keputusan dan alasan:** `output/naskah/evaluasi_substansi_dan_eksekusi_bab_1_4_draf.md` (C6 draf tabel operasionalisasi; §10 draf proposisi P1–P4; §13 keputusan).
- **Naskah:** `latex/tga_pwk_jakarta_bab_1_4_final.tex`, `latex/references.bib`, `latex/tga-preamble.tex`, `latex/figures/`.
- **Catatan kerja induk** (jangan diedit tanpa izin): `argument/argument/skripsi_s1_borrowed_size_dan_agglomeration_shadow_jakarta.md`.
- **Sumber:** `source/official-document/` dan `source/dataset/`, masing-masing dengan catatan `.md` pendamping.
- **PLAN.md dan napkin.md:** tidak dipakai di vault ini. Fungsinya digantikan oleh file evaluasi dan peta kerja di atas.
- **Arsip `handoff/`:** tidak dibuat, karena `AGENTS.md` melarang menambah folder baru.
- **Commit terakhir saat handoff:** `34af8cf refactor: normalize dataset filenames`. Berkas di `source/dataset/` kini memakai snake_case.
