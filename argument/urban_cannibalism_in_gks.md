# Urban Cannibalism in GKS

## Status and Provenance

Ini adalah Argument aktif mengenai hubungan pusat-pinggiran di Gerbangkertosusila. File ini dibuat sebagai lapisan antara paper pengguna dan kemungkinan Synthesis Product; ia belum merupakan Synthesis Product atau Output.

Posisi utama diturunkan dari blok jawaban pengguna bertanda `-->` dalam:

- `Porto-City-Cannibalism/insight/UC-claude.insight.md`
- `03-Work/MBA-answer-prompt-2.md`

Pengguna mengidentifikasi `03-Work/MBA-Drafts/Latex-Cannibalism.md` sebagai paper pengguna mengenai Urban Cannibalism GKS. File tersebut menjadi provenance paper dan spesifikasi metode, tetapi tidak diubah atau dipindahkan dalam pembuatan Argument ini. `substance-paper-cannibalism.md` dan `paper-draft-cannibalism.md` adalah material proses paper; keduanya tidak diperlakukan otomatis sebagai posisi pengguna di luar bagian yang telah dikonfirmasi.

## Working Question

Mengapa dekonsentrasi spasial di Gerbangkertosusila tidak otomatis menghasilkan dekonsentrasi fungsional, dan dalam kondisi apa konektivitas justru memperkuat ketergantungan pinggiran pada Surabaya?

## User Position

### Cannibalism as a Proposed Concept

Pengguna mengusulkan istilah *cannibalism* untuk menamai dimensi aktif dari proses penyerapan ekonomi yang difasilitasi oleh infrastruktur konektivitas. Istilah ini dibangun dari literatur *agglomeration shadow*, *backwash effect*, dan *core-periphery*, tetapi bukan istilah disipliner yang sudah mapan.

Dalam posisi ini, *agglomeration shadow* menjelaskan kondisi pinggiran yang tumbuh lebih lambat di bawah tarikan pusat. *Cannibalism* menambahkan klaim bahwa shadow dapat menjadi mekanisme ekstraktif ketika konektivitas mengurangi *friction of distance*, sementara kekuatan fungsional lokal dan dekonsentrasi fungsional tidak berkembang.

### Diagnosis GKS

Gerbangkertosusila dipahami sebagai *polynuclear monocentric region in arrested transition*: secara morfologis terdapat industri dan infrastruktur di pinggiran, tetapi fungsi urbanized yang menopang kemandirian pusat masih terkonsentrasi di Surabaya. Diagnosis ini menolak penyamaan otomatis antara *morphological polycentricity* dan *functional polycentricity*.

Istilah *arrested transition* memuat asumsi normatif bahwa dekonsentrasi spasial semestinya dapat berlanjut menuju dekonsentrasi fungsional. Asumsi ini harus tetap terlihat ketika Argument dipakai dalam synthesis.

## AI-Organized Mechanism Candidate

Formulasi tiga kondisi berikut adalah abstraksi analitis dari posisi pengguna yang telah dikonfirmasi, bukan posisi baru yang sudah dikonfirmasi secara terpisah. Ia menjadi hipotesis kerja yang perlu diuji dan dapat direvisi sebelum promosi ke Synthesis Product.

Mekanisme kerja yang diajukan terdiri dari tiga kondisi:

1. Konektivitas mengurangi biaya atau waktu interaksi dengan pusat utama.
2. *Local strength* di wilayah pinggiran tidak cukup untuk menahan atau mengolah tarikan eksternal.
3. Dekonsentrasi fungsional tidak menyertai dekonsentrasi industri, hunian, atau infrastruktur.

Interaksi ketiganya menghasilkan tekanan ekstraktif potensial: wilayah pinggiran dapat menerima penduduk, hunian, industri, atau infrastruktur tanpa membangun ekosistem jasa profesional dan fungsi pengambilan keputusan yang setara. Model belum membuktikan aliran tenaga kerja, konsumsi, modal, atau keuntungan secara langsung.

## Evidence and Calculation

### Gravity Model v2

[[gravity_based_urban_center_classification|Gravity-Based Urban Center Classification]] adalah Calculation canonical untuk model gravity versi v2. Model menggunakan POI berbobot, Shannon Entropy, unit H3 resolusi 7, matriks waktu tempuh, `beta = 2`, dan:

```text
M_total = M_econ + M_social
P_ext_i = sum over j != i of M_total_j / d_ij^beta
L_i = M_econ_i
CI_i = P_ext_i / (L_i + 1)
```

Output legacy v2 `Porto-City-Cannibalism/info/UC-info-gravity-model-v2.geojson` memiliki 149 hexagon. Distribusi kelas yang terbaca dari output v2 adalah:

- Agglomeration Core: 7
- Semi AC: 0
- Independent Hub: 0
- Semi SZ: 7
- Neutral: 9
- Semi IH: 0
- Shadow Zone: 16
- Semi T: 57
- Terpencil: 53

Hasil ini menggantikan distribusi output v1 dalam Argument ini. Output v1 dan v2 tidak boleh digabungkan karena prosedur external pull dan klasifikasinya berbeda.

Interpretasi pengguna adalah bahwa konsentrasi *Agglomeration Core* di Surabaya dan kemunculan *Shadow Zone* di sekitar inti serta koridor Suramadu mendukung diagnosis monocentric. Namun, *Shadow Zone* tetap merupakan klasifikasi tekanan potensial, bukan bukti kerugian aktual atau aliran ekstraksi.

### Sectoral Mojokerto Evidence

Calculation [[location_quotient_shift_share_and_klassen_typology|Location Quotient, Shift-Share, and Klassen Typology]] serta derived output legacy `Porto-City-Cannibalism/info/UC-info-econ-analysis.csv` digunakan untuk membaca pembagian fungsi Kota dan Kabupaten Mojokerto.

Pembacaan pengguna adalah:

- Kota Mojokerto lebih kuat pada sejumlah jasa perkotaan, sementara industri pengolahan lebih kuat di Kabupaten Mojokerto.
- Keberadaan basis industri di kabupaten tidak dengan sendirinya menghasilkan ekosistem jasa profesional yang mandiri.
- Konfigurasi ini diajukan sebagai *function-extractive split*: industri dan logistik dapat berada di Mojokerto, sedangkan sebagian fungsi profesional dan pengambilan keputusan tetap berorientasi ke Surabaya.

Derived output sektoral belum dinyatakan tervalidasi secara independen. Klaim mengenai mekanisme kausal atau arah aliran tetap merupakan inferensi Argument, bukan hasil langsung dari SLQ atau Shift-Share.

### Connectivity and Bangkalan

Bangkalan digunakan sebagai kasus untuk menguji kemungkinan *connectivity-induced cannibalism*. Posisi pengguna menghubungkan kedekatan dan konektivitas Suramadu dengan potensi tekanan eksternal, lalu membandingkannya dengan kapasitas fungsional lokal dan kondisi fiskal.

[[Effendi - 2014 - Dampak Pembangunan Jembatan Suramadu]] sekarang menjadi Source canonical untuk studi eksternal yang dikutip dalam paper. PDF tersebut melaporkan hal-hal berikut:

- Tabel PDRB harga konstan 2000 untuk empat kabupaten di Madura pada 2007-2011, dengan pertumbuhan 2011 sebesar 6,29 persen untuk Bangkalan, 6,13 persen untuk Sampang, 6,69 persen untuk Pamekasan, dan 6,36 persen untuk Sumenep (p. 3).
- Jumlah kendaraan yang melintasi Suramadu sebesar 3.231.748 pada 2009, 6.020.965 pada 2010, dan 7.291.611 pada 2011, berdasarkan data yang diatribusikan kepada PT Jasa Marga (p. 6).
- Penelitian kualitatif-deskriptif dengan 30 sampel purposif dari masyarakat umum, pemerintahan, dan kalangan pebisnis (pp. 4-5).
- Klaim dari KPPT Bangkalan bahwa terdapat delapan pengembang real estate yang telah memperoleh izin setelah peresmian jembatan (p. 6). Klaim ini belum diverifikasi terhadap sumber KPPT atau Radar Madura yang dirujuk artikel.

Studi tersebut membingkai Suramadu sebagai infrastruktur dengan *multiplier effect* yang menghemat waktu dan biaya, mendorong mobilitas, permukiman, pusat belanja, serta usaha baru, sambil menyatakan bahwa dampaknya dapat positif dan negatif (pp. 1, 5-7, 11). Sumber ini mendukung klaim tentang konektivitas, mobilitas, dan tekanan pembangunan; sumber ini tidak mengukur aliran jasa profesional, pengambilan keputusan, modal, atau keuntungan ke Surabaya. Karena itu, hubungan dari temuan tersebut menuju *cannibalism* tetap merupakan inferensi Argument yang harus diuji, bukan temuan langsung Source.

Citation dalam paper legacy tertulis `Efendi (2013)`, sedangkan halaman judul PDF mencantumkan `Mohammad Effendi` dan tahun 2014. Argument ini mengikuti metadata PDF dan mempertahankan perbedaan tersebut sebagai catatan provenance.

## Counterevidence and Alternative Readings

- *Shadow Zone* dapat dibaca sebagai pembagian kerja regional atau spesialisasi yang efisien, bukan selalu sebagai proses merugikan. Pengguna memilih pembacaan negatif karena model mendefinisikan urbanized industry sebagai indikator kekuatan pusat; konsekuensi normatif ini perlu dipertahankan sebagai pilihan teori.
- Effendi dan Hendarto membingkai Suramadu terutama sebagai *multiplier effect* dengan manfaat waktu, biaya, mobilitas, usaha baru, dan pembangunan permukiman, serta menyatakan dampak positif dan negatif. Pembacaan ini menantang asumsi bahwa konektivitas secara inheren bersifat ekstraktif.
- Tidak adanya *Independent Hub* dapat menunjukkan lemahnya ekosistem jasa, tetapi tidak membuktikan bahwa Surabaya secara kausal mengekstraksi fungsi dari setiap hexagon.
- Model gravity adalah sistem tertutup pada batas GKS. Tarikan dari Jakarta, Malang, Bali, atau wilayah lain tidak dimasukkan.
- `beta = 2` dan bobot POI ditetapkan sebagai asumsi benchmark tanpa sensitivity analysis.
- POI OpenStreetMap dapat meng-underestimate ekonomi informal dan tidak membedakan seluruh hierarki kantor pusat, cabang, atau kapasitas institusi.
- Skala H3 sekitar 5 km2 menimbulkan risiko MAUP ketika hasil dipakai untuk fenomena berskala kabupaten.
- Analisis sektoral mendalam baru tersedia untuk Mojokerto. Generalisasi mekanisme ke Sidoarjo, Gresik, Lamongan, atau Bangkalan masih bersifat hipotetis.

## Scope Conditions and Open Questions

- Argument ini membahas tekanan fungsional potensial intra-metropolitan, bukan pengukuran flow aktual.
- Distribusi kelas yang digunakan harus selalu berasal dari output v2, bukan tabel paper lama.
- Apakah *cannibalism* adalah proses ekstraktif atau pembagian kerja yang efisien membutuhkan outcome data dan data flow yang belum tersedia.
- Apakah empat kondisi spasial yang disebut sebagai *function-extractive*, *connectivity-induced*, atau mode lain merupakan tipologi yang stabil masih terbuka.
- Apakah hexagon tertentu benar-benar berada di koridor Suramadu, Ngoro Industrial Park, atau pusat Kota Mojokerto membutuhkan pemeriksaan spasial terhadap output v2 dan boundary canonical.
- Provenance studi eksternal Bangkalan sudah tersedia sebagai Source canonical, tetapi validitas klaim turunannya dan kesesuaiannya sebagai evidence load-bearing masih harus diuji.
- Promosi ke `argument/synthesis-product/` ditunda sampai angka v2, provenance Bangkalan, dan batas inferensi direkonsiliasi.

## Linked Evidence

- [[gravity_based_urban_center_classification|Gravity-Based Urban Center Classification]] - metode gravity, lineage v1/v2, dan batas validasi.
- [[location_quotient_shift_share_and_klassen_typology|Location Quotient, Shift-Share, and Klassen Typology]] - metode analisis sektoral.
- [[openstreetmap_poi_gks_april_2026|OpenStreetMap - POI GKS - April 2026]] - raw POI snapshot canonical.
- [[kemenhub_and_openstreetmap_road_network_gks_april_2026|Kemenhub and OpenStreetMap - Road Network GKS - April 2026]] - raw road network snapshot canonical.
- [[gks_administrative_boundary|GKS - Administrative Boundary]] - boundary canonical corpus GKS.
- [[bps_pdrb_adhk_regional_2014_2024|BPS - PDRB ADHK Regional - 2014-2024]] - raw PDRB snapshot canonical.
- [[bps_population_by_kecamatan_gks_2020_2025|BPS - Population by Kecamatan GKS - 2020-2025]] - raw population snapshot canonical.
- [[Effendi - 2014 - Dampak Pembangunan Jembatan Suramadu]] - studi eksternal tentang dampak Suramadu di Bangkalan dan sumber counterevidence terhadap pembacaan ekstraktif otomatis.

## Legacy Provenance

- `03-Work/MBA-Drafts/Latex-Cannibalism.md`
- `Porto-City-Cannibalism/insight/UC-claude.insight.md`
- `03-Work/MBA-answer-prompt-2.md`
- `Porto-City-Cannibalism/substance-paper-cannibalism.md`
- `Porto-City-Cannibalism/paper-draft-cannibalism.md`
- `Porto-City-Cannibalism/info/UC-info-gravity-model-v2.geojson`
- `Porto-City-Cannibalism/info/UC-info-econ-analysis.csv`
