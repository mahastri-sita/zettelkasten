# Sectoral Competitiveness Correlation by Era

## Purpose and Information Produced

Metode ini mengukur kemiripan struktur daya saing sektoral antarwilayah pada setiap era. Ukuran yang dipakai adalah korelasi Pearson antarvektor `Dij` untuk 17 sektor, bukan korelasi deret waktu Nilai PDRB. Hasilnya membantu membandingkan apakah wilayah memiliki pola daya saing sektoral yang searah atau berlawanan.

Metode ini tidak membuktikan pertukaran barang, komuter, layanan, bypass, atau hubungan kausal. Interpretasi substantif tetap berada di Argument.

## Input Data and Provenance

- Input turunan legacy: `Porto-Enclave-City/info/EC-info-pdrb.md`.
- Kolom yang dipakai: `Wilayah`, `Era_COVID`, `Kategori`, dan `Dij`.
- Implementasi legacy yang menjadi spesifikasi prosedur: `03-Work/MBA-Drafts/charts-enclave-v3/charts/gambar-correlation.ts`.
- Loader legacy: `03-Work/MBA-Drafts/charts-enclave-v3/lib/data.ts`.
- Tabel hasil dan penjelasan metode: `03-Work/MBA-Drafts/Revized-Viz-Chart-Enclave-City.md`.
- Dataset PDRB yang menjadi dependency provenance: [[BPS - PDRB ADHK Regional - 2014-2024]].
- `EC-info-pdrb.md` adalah tabel terolah legacy, bukan raw canonical dataset. Prosedur ini tidak mengubah atau menyalin tabel tersebut ke target.

## Assumptions and Scope Conditions

- Setiap kombinasi wilayah-era memiliki satu nilai `Dij` untuk masing-masing 17 kategori sektor.
- Urutan kategori harus sama ketika dua vektor dibandingkan.
- Pasangan wilayah harus berada dalam klaster yang sama dan memakai era yang sama.
- Pearson correlation mengukur kemiripan pola relatif antar sektor, bukan besaran absolut atau perubahan sepanjang waktu.
- Label `before`, `during`, dan `after` dipakai sebagaimana tersedia dalam tabel legacy.

## Method Specification

Untuk wilayah `w` dan era `e`, bentuk vektor:

```text
D(w,e) = [Dij_1, Dij_2, ..., Dij_17]
```

Untuk dua wilayah `a` dan `b` dalam era yang sama, hitung:

```text
r(a,b,e) = sum((Dij_a,i - mean_a) * (Dij_b,i - mean_b))
           / sqrt(sum((Dij_a,i - mean_a)^2) * sum((Dij_b,i - mean_b)^2))
```

Nilai mendekati `+1` menunjukkan pola sektoral yang searah; nilai mendekati `-1` menunjukkan pola yang berlawanan. Nilai tersebut tidak menunjukkan arah pengaruh.

## Reproduction Procedure

1. Baca `EC-info-pdrb.md` setelah frontmatter dikeluarkan.
2. Filter tiga wilayah dalam satu klaster dan satu nilai `Era_COVID`.
3. Ambil 17 kategori `Dij` dalam urutan kategori yang sama untuk setiap wilayah.
4. Hitung korelasi Pearson untuk setiap pasangan wilayah.
5. Ulangi untuk era `before`, `during`, dan `after`.
6. Bulatkan hasil hanya pada tahap penyajian, bukan ketika menghitung.

Pasangan wilayah yang dipakai:

- MJK: Kota Mojokerto, Kabupaten Mojokerto, dan Surabaya.
- SLK: Kota Solok, Kabupaten Solok, dan Padang.

## Output Definition

- Pearson correlation between the 17-sector `Dij` profiles for each region pair and COVID-era label.
- A three-era comparison table for the MJK and SLK clusters.
- The result describes structural similarity of sectoral competitiveness; it does not measure annual co-movement, exchange, or causality.

## Calculated Result

Hasil reproduksi read-only dari 306 baris input, 17 kategori, dan enam pasangan wilayah adalah:

| Klaster | Pasangan | before | during | after |
|---|---|---:|---:|---:|
| MJK | Kota Mojokerto - Kab. Mojokerto | 0.371709 | 0.255219 | -0.672767 |
| MJK | Kab. Mojokerto - Surabaya | 0.389947 | 0.646687 | 0.079101 |
| MJK | Kota Mojokerto - Surabaya | 0.903195 | 0.578750 | 0.112235 |
| SLK | Kota Solok - Kab. Solok | 0.674037 | 0.855356 | 0.837120 |
| SLK | Kab. Solok - Padang | 0.496928 | 0.869315 | 0.763120 |
| SLK | Kota Solok - Padang | 0.262767 | 0.922218 | 0.864016 |

Hasil ini adalah basis metode korelasi v3 yang dipakai untuk membaca struktur sektoral per era. Hasil ini tidak boleh dibaca sebagai korelasi co-movement Nilai PDRB tahunan.

## Validation and Diagnostic Checks

- Reproduksi aritmetika read-only terhadap `EC-info-pdrb.md` menghasilkan 17 observasi untuk setiap wilayah-era dan mencocokkan tabel hasil pada `Revized-Viz-Chart-Enclave-City.md`.
- Pemeriksaan ini memvalidasi reproduksi terhadap tabel turunan yang tersedia, bukan perhitungan ulang upstream `Dij` dari raw PDRB.
- Ada discrepancy yang belum terselesaikan pada metode yearly-total. `handoff-EC-charts.md` melaporkan MJK `-0.65/-0.76/+0.44` dan SLK `+0.41/+0.05/+0.09`, sedangkan rerun persis logika v2/v3 terhadap `EC-info-econ.md` menghasilkan MJK `-0.622830/+0.568766/-0.247128` dan SLK `-0.265339/+0.286368/-0.071382`.
- Karena discrepancy tersebut, yearly-total tidak dipakai sebagai hasil kanonik dalam Calculation ini.

## Limitations and Known Failure Modes

- `n=17` per korelasi kecil dan sensitif terhadap sektor tertentu.
- Era COVID dapat mengubah struktur sektoral secara serentak; korelasi tinggi selama atau sesudah COVID tidak otomatis menunjukkan integrasi fungsional.
- `Dij` bergantung pada wilayah referensi, periode, definisi sektor, satuan, dan prosedur upstream yang belum sepenuhnya terdokumentasi di target.
- `EC-info-pdrb.md` merupakan hasil turunan legacy dengan provenance upstream terbatas.
- Korelasi tidak mengidentifikasi mekanisme kausal atau arus pertukaran.
- Perbedaan hasil yearly-total tetap menjadi pertanyaan terbuka dan tidak boleh diselesaikan dengan memilih angka yang paling mendukung narasi.

## Legacy Provenance

- `Porto-Enclave-City/info/EC-info-pdrb.md`
- `Porto-Enclave-City/info/EC-info-econ.md`
- `03-Work/MBA-Drafts/charts-enclave-v3/lib/data.ts`
- `03-Work/MBA-Drafts/charts-enclave-v3/charts/gambar-correlation.ts`
- `03-Work/MBA-Drafts/handoff-EC-charts.md`
- `03-Work/MBA-Drafts/Revized-Viz-Chart-Enclave-City.md`
