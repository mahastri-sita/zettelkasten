---
session_id: 2026-10-02-02-cloud
parent_session_id: 2026-10-02-01
branch: claude/quirky-maxwell-s334gn
commits_since_parent: 1
date: 2026-10-02T23:50:00+07:00
---

# Handoff: Revisi Naskah TGA Bab 1–4 (Jabodetabek)

> Baca file ini lebih dulu, lalu `AGENTS.md` di root. Sesi cloud tidak membawa memori lokal; semua konteks ada di file dalam repo ini.
>
> **Sifat dokumen ini:** penjaga konteks, bukan naskah perintah.

## Active goal

Menyelesaikan naskah pra-TA `latex/tga_pwk_jakarta_bab_1_4_final.tex` (*Borrowed Size atau Agglomeration Shadow? … Pusat-Pusat Sekunder Jabodetabek*). Pra-TA hanya mewajibkan Bab 1–4 tanpa eksekusi analisis.

## Where we left off

Sesi cloud 2 Oktober 2026 mengerjakan seluruh rencana di `output/naskah/todo_revisi_bab_1_4.md`. Rincian dan alasannya ada di evaluasi §15.

- [x] **Verifikasi data:**
  - 141 kecamatan non-DKI;
  - definisi inti WSM (morfologis, lebih luas dari DKI);
  - matriks asal–tujuan komuter 2014/2019/2023 (ditranskripsi dan dicocokkan dengan total);
  - durasi dan biaya berupa distribusi kelas;
  - penghasilan komuter (Tabel 51);
  - keterbandingan Podes;
  - PDRB, penduduk, dan kepadatan 2024.
- [x] **Catatan sumber diperbarui** dengan locator dan transkripsi tabel: Komuter 2014/2019/2023, WSM (Lampiran 3 dan 13, 141 kecamatan berkode BPS), Podes, *Dalam Angka*, PDRB, UU 2/2024, dan Kemenperin.
- [x] **Repo dirapikan:** 36 duplikat PDF dan berkas sampah dihapus; tiga publikasi dipindah ke `official-document/`; empat CSV upah diberi catatan sumber.
- [x] **Naskah direvisi:**
  - Bab 3 ditulis ulang (spesifikasi utama dua tingkat dan cadangan K1–K8);
  - Bab 4 diisi angka terverifikasi;
  - Bab 1–2 diselaraskan;
  - bibliografi diperbaiki dan dilengkapi;
  - makro `\GambarPlaceholder` ditambahkan.
- [x] **Diagram** `.mmd` (Gambar 1.1, 2.1, 3.1, 3.2) ditulis ulang dan dirender ke PNG.
- [x] **Uji kompilasi** di cloud dengan font pengganti: 62 halaman, tanpa galat, tanpa rujukan atau sitasi yang tidak terdefinisi.
- [x] File `.tex` per bab dihapus (satu sumber kebenaran); berkas isu per bab ditandai historis.

## Next concrete action (untuk pengguna)

1. **Tinjau keputusan agen** di evaluasi §15.2. Yang paling perlu dikonfirmasi:
   - ambang massa P75;
   - titik acuan beban di Bundaran HI;
   - komposisi layanan RS + perguruan tinggi + bank;
   - pemindahan "perubahan" dari Q2 ke Q1;
   - penghapusan OD sintetis.
2. **Kompilasi lokal** dengan Times New Roman (XeLaTeX + Biber), lalu periksa PDF per halaman.
3. **Unduh** 12 *Kecamatan Dalam Angka* Kota Bekasi (tautan di TODO §0.1) dan batas kecamatan COD-AB HDX (jangan di-commit).
4. **Buat peta manual** G4.1–G4.8 (TODO §7.2). Data kecamatan siap-*join* ada di catatan sumber WSM (`source/official-document/BPS - 2026 - Wilayah Statistik Metropolitan Indonesia 2024.md`), dan matriks komuter di catatan sumber Komuter 2023.
5. **Cek basis penduduk kecamatan Banten** di WSM Lampiran 3 (selisih 2–3% dari proyeksi kab/kota).

## Open questions

- ❓ Keputusan agen pada evaluasi §15.2 (lihat di atas).
- ❓ `argument/argument/skripsi_s1_…md` masih menyebut file `.tex` per bab sebagai "rujukan operasional aktif". Memperbaruinya butuh izin eksplisit untuk mengedit Argument.
- ❓ J21/J26 (Henderson dkk.) berisi PDF identik dengan tahun J26 salah. Rapikan kode korpus atau biarkan?
- ❓ Pembimbing: naskah menulis Rendy Bayu Aditya; konfirmasinya belum tercatat di vault.
- Metadata yang belum diverifikasi: volume dan halaman `sadewoetal2021` dan `volgmannrusche2020`; judul buku `andani2021`; satuan luas Kemenperin.

## Decisions made (kumulatif)

- **Terkunci oleh pengguna:** lihat awal TODO. Tambahan 2 Oktober 2026: inti penelitian tetap DKI Jakarta, dan WSM hanya salah satu sumber.
- **Diambil agen atas mandat pengguna:** lihat evaluasi §15.2. Semua dapat dikoreksi.

## Dragons

- **Izin edit.** `AGENTS.md` melarang mengedit Argument, Output, dan Calculation tanpa niat edit eksplisit. Sesi ini bekerja di bawah mandat "kerjakan semuanya seperti yang sudah direncanakan". Mandat itu tidak mencakup mengedit catatan Argument.
- **Penomoran gambar.** Diagram keputusan cadangan muncul lebih dulu sehingga menjadi Gambar 3.1, dan alur analisis menjadi Gambar 3.2. ID di TODO (G3.1/G3.2) adalah ID kerja, bukan nomor PDF.
- **Tabel BPS berupa gambar.** Banyak tabel tidak punya lapisan teks yang benar; pada Komuter 2023, misalnya, pengodean font nama wilayah rusak. Baca secara visual, lalu cocokkan dengan baris atau kolom total. Tabel 13.1.3 *DKI Dalam Angka 2025* memuat baris yang bergeser; pakai edisi 2026.
- **Angka Bab 4 bersifat deskriptif.** Analisis Q1–Q3 belum dijalankan. Ambang P75 (36 kecamatan) masih sementara.
- **Kompilasi LaTeX.** Naskah memakai Times New Roman, yang tidak ada di cloud. Uji cloud memakai TeX Gyre Termes pada salinan di scratchpad; berkas repo tidak diubah fontnya.
- **Situs BPS menolak `curl` (HTTP 403).** Unduhan BPS dilakukan pengguna.

## Cloud environment (yang berhasil di sesi ini)

- `apt-get install tesseract-ocr tesseract-ocr-ind poppler-utils` dan `pip install pymupdf pdfplumber pandas openpyxl` berjalan tanpa pengaturan tambahan.
- XeLaTeX dan Biber dapat dipasang: `apt-get install texlive-xetex texlive-latex-extra texlive-bibtex-extra biber texlive-lang-other texlive-lang-european fonts-texgyre` (sekitar 10 menit, di latar belakang).
- Mermaid CLI dapat dipasang dengan `npm install @mermaid-js/mermaid-cli`. Render memakai `-p` berisi `{"executablePath":"/opt/pw-browsers/chromium","args":["--no-sandbox"]}`.
- Tabel gambar paling andal dibaca dengan render halaman (pymupdf, 110–150 dpi) dan pembacaan visual, lalu dicocokkan dengan total.

## References

- **Peta kerja:** `output/naskah/todo_revisi_bab_1_4.md`.
- **Keputusan dan alasan:** `output/naskah/evaluasi_substansi_dan_eksekusi_bab_1_4_draf.md` (§13 keputusan awal; §15 verifikasi dan keputusan 2 Oktober 2026).
- **Naskah:** `latex/tga_pwk_jakarta_bab_1_4_final.tex`, `latex/references.bib`, `latex/tga-preamble.tex`, `latex/figures/` (`.mmd` dan PNG).
- **Data terverifikasi:** catatan sumber di `source/official-document/`, terutama Komuter 2014/2019/2023, WSM 2024, dan *Dalam Angka* serta PDRB.
- **Catatan kerja induk** (jangan diedit tanpa izin): `argument/argument/skripsi_s1_borrowed_size_dan_agglomeration_shadow_jakarta.md`.
- **Commit induk:** `8926ba6 docs(naskah): add revision handoff and update evaluation and todo`.
