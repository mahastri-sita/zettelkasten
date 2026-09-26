# Gravity-Based Urban Center Classification

## Purpose and Information Produced

Metode ini mengubah distribusi POI dan fasilitas sosial serta waktu tempuh jaringan jalan menjadi ukuran massa ekonomi, massa sosial, external pull, local strength, Cannibalism Index, dan tipologi pusat pada unit hexagon. Hasil metode adalah klasifikasi spasial, bukan interpretasi otomatis tentang knowledge-based city atau kualitas perencanaan.

## Input Data and Provenance

- Unit spasial hexagon dan centroid.
- POI primer untuk jasa profesional dan POI sekunder untuk fasilitas sosial.
- Kategori, jumlah, dan bobot setiap POI.
- Waktu tempuh antarcentroid melalui jaringan jalan.
- Parameter decay `beta`.
- User's paper and legacy method specification: `03-Work/MBA-Drafts/Latex-Cannibalism.md`.
- Canonical POI input: [[openstreetmap_poi_gks_april_2026|OpenStreetMap - POI GKS - April 2026]].
- Canonical railway input: [[openstreetmap_railway_gks_april_2026|OpenStreetMap - Railway GKS - April 2026]].
- Canonical road input: [[kemenhub_and_openstreetmap_road_network_gks_april_2026|Kemenhub and OpenStreetMap - Road Network GKS - April 2026]].
- Canonical boundary input: [[gks_administrative_boundary|GKS - Administrative Boundary]].
- Legacy procedure references: `Porto-City-Cannibalism/info/_build_gravity_v2.py` dan `EC-info-code-gravity-model.ipynb`.
- Legacy processed POI input: `Porto-City-Cannibalism/info/UC-info-GM-poi-v3.geojson`.
- Legacy OD input: `Porto-City-Cannibalism/info/IC-info-OD-matrix.csv`.
- Legacy calculated outputs: `UC-info-gravity-model.geojson`, `UC-info-gravity-model-v2.geojson`, dan file terkait di `Porto-City-Cannibalism/info/`.

Companion untuk input terolah, prosedur, dan output terhitung tidak dipertahankan di target. Material tersebut tetap tersedia melalui path legacy yang dicatat di atas; output v2 tetap menjadi lineage legacy terpilih, bukan hasil yang telah direvalidasi secara independen.

Dataset POI, jaringan, dan boundary sudah memiliki snapshot serta provenance record di target. Query OSM, pemisahan kontribusi Kemenhub/OSM, unit hexagon, versi jaringan, dan provenance bobot masih belum lengkap. Script legacy memiliki path hardcoded dan tidak disalin atau dijalankan dalam migrasi ini.

Pengguna mengidentifikasi `03-Work/MBA-Drafts/Latex-Cannibalism.md` sebagai paper pengguna tentang Urban Cannibalism GKS. Paper tersebut dipakai di sini untuk memperjelas spesifikasi Calculation. Paper belum dipindahkan atau dipromosikan ke `argument/synthesis-product/` dalam putaran ini; promosi tersebut menjadi pekerjaan terpisah.

## Version Lineage

### Version 1: Notebook and Earlier Output

- `Porto-City-Cannibalism/info/EC-info-code-gravity-model.ipynb` menyimpan prosedur awal dan beberapa blok kode yang dikomentari.
- Pada blok Phase 4 yang tersimpan, `pext_raw` menggunakan `li_raw` dari `m_econ` saja. Ini berbeda dari spesifikasi v2 yang memakai massa total sebagai massa penarik.
- Blok visualisasi awal menggunakan `qcut`, sedangkan spesifikasi v2 menggunakan normalisasi, transformasi `log(1+x)` untuk external pull, dan Jenks natural breaks.
- `Porto-City-Cannibalism/info/UC-info-gravity-model.geojson` adalah output lama dengan 149 feature dan field seperti `total_poi`, `li_norm`, `pext_norm`, `ci_index`, serta kelas tipologi.
- Output v1 tidak boleh dicampur dengan output v2 ketika menafsirkan distribusi kelas atau nilai `P_ext`.

### Version 2: Canonical Legacy Procedure

- `Porto-City-Cannibalism/info/_build_gravity_v2.py` membaca geometri dasar dari `UC-info-gravity-model.geojson` dan POI terolah dari `UC-info-GM-poi-v3.geojson`.
- POI diklasifikasikan melalui nama dan atribut OSM ke kategori ekonomi dan sosial, lalu dijumlahkan per hexagon.
- `M_econ` memakai bobot POI primer dan Shannon Entropy. `M_social` memakai bobot fasilitas sekunder.
- Massa penarik v2 adalah `M_total = M_econ + M_social`.
- `P_ext` dihitung dari matriks waktu tempuh dengan `beta = 2`; `L_i = M_econ`; dan `CI_i = P_ext / (L_i + 1)`.
- `P_ext` ditransformasi dengan `log(1+x)` sebelum normalisasi dan Jenks natural breaks untuk klasifikasi tiga kelas.
- Script menulis `Porto-City-Cannibalism/info/UC-info-gravity-model-v2.geojson`, yang berisi 149 feature dalam CRS GeoJSON `OGC:CRS84`.

### OD Matrix

`Porto-City-Cannibalism/info/IC-info-OD-matrix.csv` berisi matriks 149 x 149 waktu tempuh, dengan satu baris dan satu kolom header tambahan pada file CSV. Kode notebook yang tersimpan membangun matriks dengan kondisi berikut:

- Graph jalan diambil melalui OSMnx untuk tujuh lokus GKS.
- Kecepatan diimputasi menurut tipe jalan; fallback adalah 20 km/jam.
- Centroid hexagon dipetakan ke node jalan terdekat.
- Shortest path memakai `travel_time` dan Dijkstra.
- Self-distance atau waktu di bawah 2 menit diberi floor 2 menit.
- Node yang tidak terhubung diberi default 3.600 detik atau 60 menit.

Matriks ini adalah derived calculation input, bukan raw dataset. Kesamaan graph OSMnx saat pembentukan matriks dengan snapshot jaringan canonical di target belum diverifikasi.

## Assumptions and Scope Conditions

- Massa ekonomi dan massa sosial dipisahkan.
- Local strength mengukur ekosistem jasa profesional dan tidak memasukkan massa sosial.
- External pull memakai waktu tempuh, bukan jarak Euclidean, bila jaringan dan waktu tempuh memang tersedia.
- `beta = 2` adalah benchmark legacy, bukan parameter yang telah dikalibrasi.
- Kategori POI dan bobot Christaller adalah keputusan pemodelan yang perlu sensitivity analysis.
- Klasifikasi tidak membuktikan bahwa suatu pusat memiliki karakter knowledge.

## Method Specification

### Massa Ekonomi dan Entropy

```text
M_econ_i = (sum over primary categories of Count_k * Weight_k) * (1 + E_i)
E_i = - sum over p of P_p * ln(P_p)
P_p = Count_p / sum of primary POI counts
```

Legacy weights untuk massa ekonomi adalah 3 bagi pengacara, konsultan, dan akuntan; 2 bagi IT, telekomunikasi, dan periklanan; serta 1.5 bagi bank dan asuransi.

### Massa Sosial

```text
M_social_i = sum over secondary categories of Count_m * Weight_m
```

Legacy weights untuk massa sosial adalah 4 bagi rumah sakit, 3 bagi universitas, dan 2 bagi mall atau department store.

### External Pull

```text
P_ext_i = sum over j != i of M_j / d_ij^beta
M_j = M_econ_j + M_social_j
```

Legacy specification menggunakan waktu tempuh jaringan jalan yang diekstrak melalui OSMnx dan `beta = 2`.

### Local Strength

```text
L_i = M_econ_i
```

Massa sosial tidak masuk ke `L_i`, tetapi tetap masuk ke massa total `M_j` yang menarik unit lain.

### Cannibalism Index

```text
CI_i = P_ext_i / (L_i + 1)
```

Konstanta `+1` mencegah pembagian dengan nol. CI tinggi berarti tekanan eksternal relatif tinggi terhadap kekuatan lokal dalam spesifikasi ini; interpretasi tersebut tidak otomatis berarti terjadi cannibalism secara kausal.

### Klasifikasi Tipologi

Legacy method menormalisasi `L_i` dan `P_ext_i`, memakai transformasi `log(1+x)` untuk external pull, lalu menggunakan Jenks natural breaks dengan tiga kelas rendah, sedang, dan tinggi. Matriks 3 x 3 menghasilkan sembilan label: Agglomeration Core, Semi AC, Independent Hub, Semi SZ, Neutral, Semi IH, Shadow Zone, Semi T, dan Terpencil.

## Reproduction Procedure

1. Tetapkan unit hexagon, periode, sumber POI, kategori, dan aturan deduplikasi.
2. Pilih lineage v2 sebagai prosedur canonical dan jangan mencampur hasil v1 dengan v2.
3. Hitung massa ekonomi dan entropy per hexagon.
4. Hitung massa sosial per hexagon.
5. Bangun atau akses matriks waktu tempuh jaringan dan tetapkan `beta`.
6. Hitung external pull, local strength, dan CI.
7. Terapkan transformasi serta Jenks sesuai parameter yang didokumentasikan.
8. Ekspor hasil dengan field input, parameter, dan klasifikasi yang dapat ditelusuri.
9. Jalankan diagnostik dan sensitivity analysis sebelum memakai hasil untuk Argument.

Tidak ada script atau notebook legacy yang dijalankan. Audit di bawah menggunakan pembacaan read-only terhadap output dan matriks yang sudah ada. Hasil ini belum dinyatakan tervalidasi secara penuh.

## Output Definition

- Nilai `M_econ`, `M_social`, `entropy`, `P_ext`, `L`, dan `CI` per hexagon.
- Kelas normalized `L` dan `P_ext`.
- Label tipologi spasial.
- Parameter bobot, beta, jaringan, periode, transformasi, dan metode breaks.
- Canonical legacy calculated output untuk lineage v2: `Porto-City-Cannibalism/info/UC-info-gravity-model-v2.geojson`.
- Superseded legacy calculated output untuk lineage v1: `Porto-City-Cannibalism/info/UC-info-gravity-model.geojson`.

## Validation and Diagnostic Checks

### Read-only Integrity Audit (2026-08-23)

Pemeriksaan struktural dan identitas numerik dilakukan tanpa menjalankan script atau notebook legacy:

- `UC-info-gravity-model-v2.geojson` berisi 149 feature Polygon dan 149 `h3_address` unik dalam CRS `OGC:CRS84`.
- Semua field v2 wajib (`m_econ`, `m_social`, `m_total`, `entropy_index`, `pext_raw`, `pext_log`, `pext_logn`, `pext_norm`, `li_norm`, `ci_index`, `li_class`, dan `pext_class`) tersedia dan tidak null.
- Identitas `m_total = m_econ + m_social`, `pext_log = log(1 + pext_raw)`, dan `ci_index = pext_raw / (m_econ + 1)` konsisten pada toleransi numerik floating-point di seluruh feature.
- Crosstab `li_class` x `pext_class` menghasilkan distribusi v2 yang dipakai dalam Output: `(0,0)=53`, `(0,1)=57`, `(1,1)=9`, `(1,2)=7`, `(0,2)=16`, `(2,2)=7`.
- `IC-info-OD-matrix.csv` berukuran 149 x 149; 149 ID baris unik, 149 ID kolom unik, urutan baris dan kolom sama, serta set ID sama dengan GeoJSON.
- Seluruh nilai OD finite dan non-negatif. Diagonal konsisten pada 2 menit, dan rentang nilai adalah 2 sampai 178,0356 menit.
- Matriks OD tidak simetris; selisih absolut maksimum adalah 99,0809 menit. Ini tidak otomatis dianggap error karena waktu tempuh dapat bersifat directional pada graph jalan, tetapi arah graph dan aturan routing belum diaudit secara independen.
- Reproduksi read-only `P_ext` pada `beta = 2` dari `m_total` dan OD menghasilkan error maksimum `3,55e-15` terhadap field `pext_raw` pada GeoJSON.
- Spot-check ranking CI pada `beta = 1`, `2`, dan `3` menghasilkan Spearman `1,0` terhadap ranking `beta = 2`. Overlap 10 unit teratas adalah `7/10` untuk `beta = 1` dan `8/10` untuk `beta = 3`. Jenks tidak diulang pada spot-check ini, sehingga robustness label sembilan kelas belum dapat disimpulkan.

Pemeriksaan ini mendukung integritas internal file, lineage, dan reproduksi formula dasar, tetapi bukan validasi substantif. Pemeriksaan POI ganda, unit kosong secara substantif, kesesuaian graph dengan snapshot target, sensitivity analysis pada label, bobot kategori, metode Jenks, skala hexagon, dan perubahan data POI antarperiode masih belum dilakukan.

Pemeriksaan lineage juga diperlukan: pastikan output yang dipakai memiliki field v2 (`m_total`, `pext_raw`, `pext_log`, dan `pext_logn`), tidak menggunakan output v1, serta cocok dengan 149 ID hexagon pada matriks OD.

## Limitations

- POI adalah proxy, bukan pengukuran langsung kapasitas ekonomi atau sosial.
- Bobot kategori adalah asumsi model.
- Waktu tempuh dan jaringan dapat berubah berdasarkan sumber, periode, dan kondisi perjalanan.
- Output v1 dan v2 menggunakan prosedur yang berbeda, terutama pada massa penarik dan klasifikasi; distribusi hasilnya tidak boleh dibandingkan tanpa menandai lineage.
- Matriks OD adalah derived input yang berasal dari graph dan aturan kecepatan legacy; provenance graph serta kesesuaiannya dengan snapshot jaringan target belum lengkap.
- Hasil gravity tidak menyediakan teori langsung untuk spesialisasi sektoral atau knowledge-based city. Legacy Argument secara eksplisit mengakui hubungan tersebut sebagai post-hoc rationalization.
- File `UC-info-dasymetric-mapping.csv` dan GeoJSON gravity adalah hasil turunan, bukan input raw, dan belum dipindahkan.

## Legacy Provenance

- `03-Work/MBA-Drafts/Latex-Cannibalism.md`
- `Porto-City-Cannibalism/info/_build_gravity_v2.py`
- `Porto-City-Cannibalism/info/EC-info-code-gravity-model.ipynb`
- `Porto-City-Cannibalism/info/UC-info-GM-poi-v3.geojson`
- `Porto-City-Cannibalism/info/IC-info-OD-matrix.csv`
- `Porto-City-Cannibalism/info/UC-info-gravity-model.geojson`
- `Porto-City-Cannibalism/info/UC-info-gravity-model-v2.geojson`
