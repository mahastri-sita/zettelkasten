# Location Quotient, Shift-Share, and Klassen Typology

## Purpose and Information Produced

Metode ini mengubah data PDRB sektoral menjadi informasi tentang spesialisasi, dinamika pertumbuhan, komponen pertumbuhan, dan posisi sektor dalam tipologi dua dimensi. Metode ini tidak menentukan makna substantif bagi Mojokerto tanpa Argument dan pemeriksaan terhadap data.

## Input Data and Provenance

- PDRB sektor `i` pada wilayah `r` dan wilayah referensi `N`.
- Periode awal `t0` dan akhir `t1` yang konsisten.
- Total PDRB wilayah dan total PDRB referensi.
- Legacy method specification: `03-Work/MBA-Drafts/Latex-Enclave.md`.
- Canonical dataset record: [[bps_pdrb_adhk_regional_2014_2024|BPS - PDRB ADHK Regional - 2014-2024]].
- Legacy raw variants: `Porto-Enclave-City/info/EC-info-bps-new.csv` dan `Porto-City-Cannibalism/info/UC-info-econ-pdrb.csv`.
- User-processed input: `Porto-Enclave-City/info/EC-info-econ.md`.
- Legacy derived outputs: `Porto-Enclave-City/info/EC-info-pdrb.md` dan `Porto-City-Cannibalism/info/UC-info-econ-analysis.csv`.
- Project data index: `03-Work/MBA-data.md`.
- Legacy chart handoff: `03-Work/MBA-Drafts/handoff-EC-charts.md`, yang melaporkan discrepancy pada kolom `Kategori` dan hasil korelasi lama. Handoff ini belum diaudit ulang secara independen.

Companion legacy-derived tidak dipertahankan di target. Varian raw, input terolah, dan output turunan tetap tersedia melalui path legacy yang dicatat di atas untuk provenance dan rekonsiliasi selanjutnya; material tersebut bukan data raw canonical atau hasil tervalidasi.

Record dataset sudah canonical untuk provenance file. Publikasi BPS, definisi satuan, versi, dan pemeriksaan angka masih belum tersedia atau belum dilakukan.

## Assumptions and Scope Conditions

- Wilayah referensi `N` harus dinyatakan eksplisit. Legacy specification menggunakan provinsi sebagai acuan utama dan nasional sebagai pembanding sekunder pada beberapa angka.
- Definisi sektor, harga, periode, dan unit harus konsisten antarwilayah.
- Nilai awal tidak boleh nol ketika dipakai sebagai penyebut pertumbuhan.
- Threshold klasifikasi adalah 1, tetapi batas tersebut tidak membuktikan kausalitas atau daya saing secara mandiri.

## Method Specification

### Static Location Quotient

```text
LQ_ir = (X_ir / X_r) / (X_iN / X_N)
```

`LQ > 1` menunjukkan spesialisasi relatif terhadap referensi; `LQ < 1` menunjukkan nonbasis relatif. `LQ = 1` menunjukkan proporsi yang sama dengan referensi.

### Dynamic Location Quotient

```text
DLQ_ir = (1 + g_ir) / (1 + g_iN)
g_ir = (X_ir^t1 - X_ir^t0) / X_ir^t0
g_iN = (X_iN^t1 - X_iN^t0) / X_iN^t0
```

`DLQ > 1` menunjukkan pertumbuhan spesialisasi yang lebih cepat daripada referensi. `DLQ < 1` menunjukkan pertumbuhan yang lebih lambat.

### Shift-Share

```text
Delta X_ir = N_ij + P_ij + D_ij
N_ij = X_ir^t0 * r_N
r_N = (X_N^t1 - X_N^t0) / X_N^t0
P_ij = X_ir^t0 * (r_iN - r_N)
r_iN = (X_iN^t1 - X_iN^t0) / X_iN^t0
D_ij = X_ir^t0 * (r_ir - r_iN)
r_ir = (X_ir^t1 - X_ir^t0) / X_ir^t0
```

`N_ij` adalah regional share, `P_ij` adalah proportional shift atau bauran industri, dan `D_ij` adalah differential shift. `D_ij > 0` hanya berarti pertumbuhan sektor wilayah lebih tinggi daripada pertumbuhan sektor referensi dalam spesifikasi ini; ia tidak sendirian membuktikan mekanisme penyebab.

### Tipologi Klassen Dua Dimensi

Tipologi menggunakan `SLQ` pada sumbu horizontal dan `DLQ` pada sumbu vertikal:

```text
Prima          : SLQ > 1, DLQ > 1
Berkembang     : SLQ < 1, DLQ > 1
Maju Tertekan  : SLQ > 1, DLQ < 1
Tertinggal     : SLQ < 1, DLQ < 1
```

## Reproduction Procedure

1. Validasi wilayah, sektor, periode, unit, dan referensi.
2. Hitung total PDRB dan laju pertumbuhan yang diperlukan.
3. Hitung LQ, DLQ, `N_ij`, `P_ij`, dan `D_ij` untuk setiap sektor-wilayah.
4. Terapkan klasifikasi Tipologi Klassen.
5. Simpan hasil sebagai calculated result yang terpisah dari data raw.
6. Periksa identitas shift-share dan bandingkan hasil dengan tabel sumber.

Tidak ada prosedur yang dijalankan dalam migrasi ini. Tidak ada hasil yang dinyatakan tervalidasi.

## Output Definition

- Tabel LQ dan DLQ per sektor-wilayah-periode.
- Tabel `N_ij`, `P_ij`, dan `D_ij`.
- Klasifikasi Tipologi Klassen.
- Catatan referensi wilayah, periode, dan unit yang dipakai.
- Legacy derived outputs: `Porto-Enclave-City/info/EC-info-pdrb.md` dan `Porto-City-Cannibalism/info/UC-info-econ-analysis.csv`.

## Validation and Diagnostic Checks

Belum dilakukan. Pemeriksaan yang diperlukan mencakup rekonsiliasi `Delta X_ir = N_ij + P_ij + D_ij`, pengecekan penyebut nol, konsistensi satuan, konsistensi acuan provinsi, serta sensitivitas terhadap periode COVID dan pemilihan referensi.

## Limitations

- Hasil bergantung pada wilayah referensi dan periode yang dipilih.
- Shift-share bersifat deskriptif dan tidak mengidentifikasi mekanisme kausal.
- Nilai positif `D_ij` tidak cukup untuk menyimpulkan bahwa suatu kebijakan atau sektor telah menjadi mesin pertumbuhan.
- Data legacy dan hasil turunan belum memiliki provenance lengkap di target.
- `ec_info_bps_new.csv` tetap dipertahankan sebagai snapshot raw, tetapi laporan masalah pada `Kategori` membuatnya tidak aman dipakai sebagai tabel kategori analitis tanpa rekonsiliasi. `EC-info-econ.md` adalah tabel terolah pengguna yang dipakai pipeline chart legacy, bukan raw canonical.

## Legacy Provenance

- `03-Work/MBA-Drafts/Latex-Enclave.md`
- `03-Work/MBA-data.md`
- `Porto-Enclave-City/info/EC-info-econ.md`
- `Porto-Enclave-City/info/EC-info-pdrb.md`
- `03-Work/MBA-Drafts/handoff-EC-charts.md`
