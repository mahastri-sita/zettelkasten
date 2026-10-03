---
session_id: 2026-10-03-01-local
parent_session_id: 2026-10-02-02-cloud
branch: main
date: 2026-10-03
---

# Handoff: Revisi Naskah TGA Bab 1–4 (Jabodetabek)

> Baca file ini lebih dulu, lalu `AGENTS.md` di root.
>
> **Sifat dokumen ini:** penjaga konteks, bukan naskah perintah.

## Active goal

Menyelesaikan naskah pra-TA `latex/tga_pwk_jakarta_bab_1_4_final.tex` (*Borrowed Size atau Agglomeration Shadow? … Pusat-Pusat Sekunder Jabodetabek*). Pra-TA hanya mewajibkan Bab 1–4 tanpa eksekusi analisis.

## Where we left off

Putaran 7 (3 Oktober 2026, lokal) selesai. Rinciannya ada di evaluasi §16 dan TODO §9.

- [x] Bundle cloud (`a488635`) di-*fast-forward* ke `main`.
- [x] Perbandingan naskah lokal dan bundle menghasilkan regresi R1–R6 (TODO §9.1). Pengguna menyetujui keputusan D1–D8 (TODO §9.2).
- [x] **Verifikasi data:**
  - makna % WSM pada kecamatan inti;
  - basis penduduk Banten (P75 dibekukan: 193.899 jiwa, 36 kecamatan);
  - total RS/PT/bank Podes 2024 (tabel bank Tangsel tidak tercetak, sehingga dibuat cadangan K9);
  - asimetri dan rasio masuk/keluar 2014/2019/2023;
  - bibliografi lewat Crossref dan rekaman UTwente;
  - kawasan industri (30 rekaman/21 kawasan/19 non-DKI; `Luas_IUKI` ≈ hektare luas izin);
  - syarat Google Maps Platform (larangan pemakaian bersama peta non-Google).
- [x] **Naskah Bab 1–4 disunting:**
  - integrasi diberi nama ulang + interaksi status inti + $I^{DKI}$ kembar;
  - label *shadow* hanya dari layanan;
  - $F_P$ di luar kawasan industri (kawasan industri jadi moderator);
  - beban Google Routes jam sibuk (K6 = OSM);
  - gerbang memakai beban **atau** ketergantungan;
  - Tabel 3.7 bentuk bukti relasi;
  - subbab Pusat pelayanan + Tabel 4.3;
  - kolom asimetri di tabel komuter.
- [x] Empat diagram `.mmd` diperbarui dan dirender ulang di lokal (mermaid-cli 12.0.0 di scratchpad).
- [x] Kompilasi lokal XeLaTeX + Biber dengan Times New Roman: 66 halaman, tanpa galat, tanpa rujukan tak terdefinisi. PDF: `latex/tga_pwk_jakarta_bab_1_4_2026_10_03.pdf`.
- [x] Catatan sumber diperbarui: WSM, tujuh Podes 2024, Podes Tangsel 2025, Kemenperin. Catatan baru: syarat Google Maps Platform.

## Next concrete action

1. 🖐 **Pengguna:** unduh 12 *Kecamatan Dalam Angka* Kota Bekasi (tautan di TODO §0.1) dan batas kecamatan COD-AB HDX (TODO §0.4; jangan di-commit).
2. 🖐 **Pengguna:** buat peta G4.1–G4.8 (TODO §7.2). Prioritas: G4.2, G4.4, G4.8.
3. **Agen, setelah batas kecamatan ada:** hitung volume hunian dan nonhunian GHSL per kecamatan (kriteria massa kedua; masker kawasan industri berbasis poligon).
4. **Bahasa:** jalankan `humanizer-academic-id` + EYD pada naskah (TODO §9 F7).

## Open questions

- ❓ `argument/argument/skripsi_s1_…md` masih menyebut file `.tex` per bab sebagai "rujukan operasional aktif". Memperbaruinya butuh izin eksplisit untuk mengedit Argument.
- ❓ J21/J26 (Henderson dkk.): PDF identik, tahun J26 salah. Dibiarkan.
- Pembimbing: naskah menulis Rendy Bayu Aditya; konfirmasinya belum tercatat di vault.
- Biaya Google Routes/Places belum diuji. Ketentuan umum Google Maps Platform (di luar syarat khusus layanan) belum dibaca.

## Decisions made (kumulatif)

- **Terkunci oleh pengguna:** lihat awal TODO serta D1–D8 (TODO §9.2, evaluasi §16.1).
- **Keputusan agen yang sudah disahkan:** evaluasi §15.2 (lewat D7).

## Dragons

- **Makna % WSM pada kecamatan inti** adalah inferensi dari nilai DKI (23,6–49,7%). BPS tidak menyatakannya eksplisit. Jangan menulisnya sebagai fakta publikasi.
- **Penyebut arus keluar** di Bab 3 dan Bab 4 memasukkan arus ke luar Jabodetabek. Hitungan ulang harus memakai definisi yang sama, sebab pangsa ke DKI berbeda sekitar 1–2 poin bila penyebutnya diganti.
- **Bank Tangsel** berasal dari edisi 2025 (K9), sedangkan infografis Podes 2024 labelnya diragukan (BPR 94 vs 18 pada 2025).
- **Kota Bogor:** tabel RS mencetak 22, narasinya 20. **Tangsel:** tabel PT 5+23, narasinya 1+28. Naskah memakai angka tabel.
- **Font:** preamble jatuh ke Courier New bila Consolas tidak ada. Di Mac ini Consolas tidak terpasang.
- **Tabel BPS berupa gambar atau berlapisan teks rusak.** Baca visual (pdftoppm 90–150 dpi) dan cocokkan dengan total.
- **Situs BPS menolak `curl` (HTTP 403).** Unduhan BPS dilakukan pengguna.

## References

- **Peta kerja:** `output/naskah/todo_revisi_bab_1_4.md` (§9 = putaran 7).
- **Keputusan dan alasan:** `output/naskah/evaluasi_substansi_dan_eksekusi_bab_1_4_draf.md` (§15 cloud; §16 putaran 7).
- **Naskah:** `latex/tga_pwk_jakarta_bab_1_4_final.tex`, `latex/references.bib`, `latex/tga-preamble.tex`, `latex/figures/`.
- **Data terverifikasi:** catatan sumber di `source/official-document/` dan `source/dataset/`.
- **Catatan kerja induk** (jangan diedit tanpa izin): `argument/argument/skripsi_s1_borrowed_size_dan_agglomeration_shadow_jakarta.md`.
