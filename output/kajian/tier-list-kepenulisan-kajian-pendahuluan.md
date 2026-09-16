# Tier List Kepenulisan Kajian Pendahuluan

**Status:** sintesis kerja

## Cakupan

- Dokumen ini menilai kualitas **tulisan review**, bukan kualitas artikel sumber yang direview.
- Korpus terdiri dari 70 file `review-<kode>.md`: 16 kode J, 28 kode A, 25 kode B, dan C02.
- Semua file terbaca sebagai review yang dominan berbahasa Indonesia. Judul, heading, dan istilah teknis berbahasa Inggris tidak dihukum sebagai kegagalan bahasa.
- Tautan pada setiap kode membuka review yang menjadi dasar penilaian.

## Rubrik

Penilaian menggabungkan lima dimensi:

1. **Teknik prosa:** kejelasan, diksi, kohesi, struktur paragraf, kepadatan, dan kelancaran.
2. **Arsitektur argumen:** hubungan antara laporan sumber, interpretasi, inferensi, bukti, dan klaim.
3. **Karakter penulis:** kehadiran suara, sikap intelektual, dan cara kritik disampaikan.
4. **Keunikan sintesis:** kemampuan menghasilkan hubungan, kategori, atau diagnosis yang tidak berhenti pada parafrasa.
5. **Kontrol epistemik:** kalibrasi opini, pengakuan ketidakpastian, dan pencegahan overclaim.

### Arti tier

- **S:** tulisan exemplar. Kuat lintas dimensi, memiliki suara atau sintesis yang mudah dikenali, dan dapat dipakai sebagai model.
- **A:** tulisan sangat kuat dengan satu atau lebih keterbatasan material, biasanya repetisi, kepadatan teknis, atau sintesis yang belum maksimal.
- **B:** tulisan berguna dan cukup dapat dipercaya, tetapi lebih inventarisatif, paraphrastik, template-driven, atau kurang khas.
- **C:** tulisan lemah atau hanya dapat digunakan secara terbatas karena masalah besar pada kejelasan, struktur, atau hubungan bukti-klaim.
- **D:** tulisan tidak memadai atau tidak cukup tersedia untuk dinilai.

Tier tidak menggunakan kuota. Tidak adanya C dan D berarti seluruh korpus memiliki struktur minimum yang dapat dinilai; itu bukan klaim bahwa semua review sama kuatnya.

## Metode Penilaian

- Sepuluh subagent baru bertipe `general` membaca seluruh korpus dalam sepuluh batch, masing-masing tujuh file.
- Setiap subagent memberi penilaian provisional, ciri suara, keunikan, kelemahan, dan kandidat borderline.
- Hasil kemudian dikalibrasi lintas batch agar S tidak diberikan hanya karena sebuah review menjadi yang terbaik dalam batch kecil.
- Penilaian ini tetap berbasis teks review yang tersedia. Artikel sumber, PDF asli, data mentah, dan proses penulisan awal tidak diverifikasi ulang untuk menyusun tier kepenulisan.

## Pola Korpus

- Kekuatan paling konsisten adalah pelabelan sumber, interpretasi, dan inferensi; banyak review juga cukup disiplin dalam menahan klaim kausal.
- Kelemahan paling berulang adalah repetisi antara `Results`, `Findings`, `Conclusions`, dan `Provenance Notes`.
- Sebagian review memiliki suara audit-forensik yang kuat, tetapi terlalu sering berubah menjadi inventaris angka dan caveat.
- Review dengan karakter paling mudah dikenali cenderung mengubah detail teknis menjadi diagnosis konseptual, bukan hanya meringkas isi artikel.
- Penggunaan heading dan istilah teknis Inggris bukan masalah utama; pembeda tier terutama adalah kualitas sintesis, pacing, dan kehadiran suara penulis.

## S

- [[review-J06|J06]] - Suara ekonometrik yang hati-hati; kuat dalam membedakan perubahan akses, stok jaringan, proksi cahaya malam, dan heterogenitas menurut moda serta zona. Kepadatan audit menjadi keterbatasan minor.
- [[review-J07|J07]] - Tegas-analitis dengan rantai sumber sampai inferensi yang sangat rapat; pembedaan sprawl dari pertambahan luas kota menjadi sintesis yang mudah diingat.
- [[review-J10|J10]] - Metodologis dan presisi; membedakan ketimpangan statistik dari ketidakadilan normatif serta pola deskriptif dari klaim kausal. Struktur masih cukup formulaik.
- [[review-J11|J11]] - Audit-analitis dan seimbang; menunjukkan bahwa dampak rata-rata yang nihil dapat hidup berdampingan dengan dampak lokal. Lengkap, meski berulang.
- [[review-J26|J26]] - Suara analitis-institusional; menghubungkan bentuk kota, transportasi, tanah, industri, dan distribusi sosial ke sintesis desentralisasi sekaligus konsentrasi ulang.
- [[review-A01|A01]] - Suara konseptual yang terkontrol; membedakan borrowed function, borrowed performance, dan eksternalitas jaringan dengan arsitektur argumen yang utuh.
- [[review-A02|A02]] - Tajam secara ekonometrik; merangkum hasil sebagai substitusi yang parsial dan bersyarat tanpa menyembunyikan masalah koefisien, heterogenitas, atau kausalitas terbalik.
- [[review-A09|A09]] - Kritis dan tenang; pembedaan efek rata-rata DID dari efek diferensial DDD menghasilkan sintesis yang matang tentang kekuatan administratif dan borrowed size.
- [[review-A11|A11]] - Konseptual dan terarah; merangkai polycentricity, spillover, dan produktivitas sebagai rantai kondisional, bukan sebagai manfaat otomatis.
- [[review-A12|A12]] - Ekonomis dan kohesif; sangat baik dalam membedakan tidak adanya bukti dari bukti bahwa suatu efek tidak ada.
- [[review-A14|A14]] - Suara diagnostik yang tenang; pembedaan broadband hunian, penetrasi tempat, borrowed functions, dan zona jarak menghasilkan pembacaan yang khas.
- [[review-A17|A17]] - Tajam dan contradiction-aware; mempertahankan konflik antara tabel dan prosa tanpa mengarang rekonsiliasi, dengan sintesis manfaat lokal versus tekanan antardaerah.
- [[review-A22|A22]] - Forensik dan kritis; detail indeks layanan, unit, dan sampel diubah menjadi batas validitas konstruk serta mekanisme secara jelas.
- [[review-A23|A23]] - Ringkas, konseptual, dan non-biner; membedakan borrowed functions, borrowed performance, dan borrowed size dengan ekonomi prosa yang kuat.
- [[review-A24|A24]] - Komparatif dan sadar mekanisme; perbatasan dibaca sebagai penghalang sekaligus pelindung tanpa mengubah interaksi potensial menjadi arus aktual.
- [[review-B02|B02]] - Sangat ekonomis dan jernih; hubungan morfologi-fungsi, hasil, dan inferensi tersusun rapat. Sesekali terlalu mengikuti rubrik.
- [[review-B03|B03]] - Kuat dalam alur lintas skala; membedakan desentralisasi dari integrasi penuh dan menahan ekstrapolasi yang tidak didukung.
- [[review-B04|B04]] - Diagnostik dan skeptis; logika pengujian dari klaim jaringan kota ke kondisi, model, hasil, dan kesimpulan sangat jelas.
- [[review-B08|B08]] - Integratif dan method-aware; menjelaskan bahwa integrasi metropolitan bukan sekadar penjumlahan populasi, melainkan kapasitas jaringan dan koordinasi.
- [[review-B09|B09]] - Metodologis dan efisien; menjelaskan perbedaan sentralitas fungsional dan kepadatan morfologis tanpa melompat ke klaim kausal.
- [[review-B18|B18]] - Pragmatik dan sadar metode; centrality dibaca sebagai kapasitas pusat layanan, bukan sekadar ukuran kota, dengan contoh konkret yang memperkuat suara.
- [[review-B22|B22]] - Ringkas, skeptis, dan konseptual; gagasan pergantian rezim shadow-access serta observational equivalence dirumuskan dengan padat.
- [[review-B24|B24]] - Forensik-mekanistik; membedakan gradien kepadatan monoton dari pola turun-naik yang lebih diagnostik dan menghubungkannya langsung dengan identifikasi.
- [[review-C02|C02]] - Paling khas secara konseptual; istilah urban cannibalism, function-extractive split, dan arrested transition dipakai sebagai diagnosis sambil tetap dikritik batasnya.

## A

- [[review-J01|J01]] - Audit-forensik atas post-suburbanization dan konflik tabel-narasi; bukti sangat terlacak, tetapi prosa padat dan berulang.
- [[review-J03|J03]] - Sintesis konseptual tentang dekonsentrasi dan reaglomerasi kuat; hubungan menuju struktur hibrida jelas, meski terlalu panjang dan sarat angka.
- [[review-J05|J05]] - Suara paling kuat pada tata kelola dan distribusi kekuasaan; mudah diikuti, tetapi rantai buktinya tidak setajam review teknis teratas.
- [[review-J08|J08]] - Auditor statistik yang teliti dalam membaca odds ratio, pilihan moda, dan batas model; kelemahannya adalah gaya katalogis.
- [[review-J09|J09]] - Skeptis dan contradiction-aware; konflik usia, pendapatan, OR, dan sampel dipetakan baik, tetapi inventaris konflik berulang.
- [[review-J22|J22]] - Komparatif-historis; pembedaan polisentralitas morfologis dan fungsional sangat berguna, sementara mekanisme penyebab masih tersebar.
- [[review-J23|J23]] - Kritis dan model-literate; menunjukkan bahwa pertumbuhan pekerjaan manufaktur tidak otomatis berarti keseimbangan pekerjaan-perumahan. Kepadatan teknis mengurangi kelancaran.
- [[review-J27|J27]] - Kuat dalam membaca transformasi sosial-ekonomi dan segregasi sebagai proses bersamaan; lengkap, tetapi paling repetitif di kelompok J.
- [[review-A03|A03]] - Ringkas dan fokus; posisi hierarkis dibaca sebagai moderator manfaat massa eksternal, dengan beberapa generalisasi yang perlu tetap dikalibrasi.
- [[review-A04|A04]] - Diagnostik-metodologis; tipologi residual empat kuadran dan contoh Berlin-Frankfurt menjadi ciri utama, meski caveat berulang.
- [[review-A05|A05]] - Komparatif dan peka terhadap heterogenitas; tidak menyederhanakan jaringan sebagai selalu menguntungkan, tetapi register teknisnya agak kaku.
- [[review-A06|A06]] - Auditif dan evidence-checked; kuat pada angka, konstruk, proksi, serta arah koefisien, namun terasa seperti log pemeriksaan.
- [[review-A07|A07]] - Investigatif; sangat baik dalam mendeteksi ambiguitas internal tanpa menyelesaikannya dengan dugaan, tetapi terlalu cumbersome.
- [[review-A08|A08]] - Menyusun sintesis integrasi yang asimetris antara industri sekunder dan tersier; struktur kuat, tetapi detail dan caveat menumpuk.
- [[review-A10|A10]] - Ekonomis; menangkap ketegangan antara jaringan yang makin multisentra dan manfaat inovasi yang tetap terkonsentrasi. Pemisahan sumber dan interpretasi belum selalu konsisten.
- [[review-A13|A13]] - Audit-forensik dengan pemisahan laporan, interpretasi, dan inferensi yang sangat disiplin; terlalu panjang dan inventarisatif.
- [[review-A15|A15]] - Suara makroekonomi yang terukur; membedakan kontribusi jaringan dari perubahan disparitas total, tetapi daftar angka regional mengganggu ritme.
- [[review-A16|A16]] - Rigor teknis pada TFP, GMM, elastisitas, dan heterogenitas sektoral; struktur kuat, tetapi blok locator dan caveat berulang.
- [[review-A19|A19]] - Contradiction-aware; membedakan hasil pendapatan lahan dan GDP serta menahan klaim shadow, walau beberapa bagian katalogis.
- [[review-A20|A20]] - Audit kuantitatif yang sangat teliti terhadap angka, jumlah observasi, variabel, dan status kausal; kepadatan teknis menjadi beban.
- [[review-A21|A21]] - Dokumenter dan hati-hati; konflik regional dipertahankan tanpa spekulasi, tetapi suara sintesis kurang menonjol karena bentuknya katalog hasil.
- [[review-A25|A25]] - Kompak dan sistematik dalam meringkas banyak model serta indikator; gaya bullet telegraphic membatasi kedalaman hubungan antarbukti.
- [[review-A26|A26]] - Essayistik dan konseptual; model tiga lapisan dijembatani dengan implikasi kelembagaan, tetapi bukti empiris dan detail operasional lebih tipis.
- [[review-A27|A27]] - Audit-provenance dengan sintesis agensi kota sekunder yang khas; disiplin epistemiknya tinggi, tetapi sangat repetitif dan birokratis.
- [[review-A28|A28]] - Relasional dan relatif mengalir; menunjukkan bahwa fungsi lokal tidak identik untuk semua saluran, meski penandaan epistemiknya belum seragam.
- [[review-B01|B01]] - Audit-statistik yang tertib dalam memetakan tiga dimensi integrasi dan outcome proksi; bagian hasil cenderung menjadi katalog koefisien.
- [[review-B05|B05]] - Perspektif skala menjadi ciri utama dan berhasil menolak satu resep polycentricity; prosa report-like dan cukup berulang.
- [[review-B06|B06]] - Forensik dan sangat evidence-checked; stabilitas hasil lintas spesifikasi dibaca baik, tetapi metadata serta caveat terlalu padat.
- [[review-B07|B07]] - Audit-empiris yang kuat tentang perbedaan massa penduduk gabungan dan massa dukungan amenitas; ekstensif dan repetitif.
- [[review-B10|B10]] - Kritis dan adil saat membaca konflik EIM-ACT dan tabel hasil; masalah utamanya adalah pengulangan konflik yang sama.
- [[review-B11|B11]] - Suara kebijakan yang bersyarat; membedakan GDP deskriptif dari outcome ekonometrik, tetapi transisi antar-cakupan sampel kurang mulus.
- [[review-B13|B13]] - Forensik dan provenance-first; mempertahankan anomali sampel serta ambiguitas ekonometrik, dengan repetisi tinggi antarbagian.
- [[review-B14|B14]] - Sistematik dan diagnostik dalam membedakan studi, estimasi, elastisitas, dan heterogenitas; ritme bullet sangat formulaik.
- [[review-B15|B15]] - Teknis tetapi tetap interpretatif; alur hipotesis-metode-hasil-inferensi jelas dan mampu menahan klaim universal.
- [[review-B17|B17]] - Analitis dan non-biner; tidak memaksa aglomerasi dan jaringan menjadi pilihan eksklusif, walau istilah Inggris dan kalimat panjang dominan.
- [[review-B19|B19]] - Eksplanatoris dan kritis; tipologi kota kecil-menengah memberi identitas, tetapi uraiannya enumeratif dan panjang.
- [[review-B20|B20]] - Forensik dan sangat kuat mempertahankan kontradiksi angka; kepadatan serta repetisi mengurangi kelancaran.
- [[review-B21|B21]] - Analitis dan seimbang dalam menjelaskan efek jarak bertingkat serta nonlinearitas; tesis utama kadang tertutup daftar koefisien.
- [[review-B23|B23]] - Suara historis yang tenang; membedakan dominasi pusat dari pengosongan hinterland, tetapi daftar hasil wilayah terlalu data-heavy.
- [[review-B25|B25]] - Terapan dan diagnostik; hubungan morfologi-fungsi-arus manusia cukup khas, tetapi review masih terlalu mengikuti urutan artikel.

## B

- [[review-J02|J02]] - Skeptis dan terukur dalam membedakan pola perjalanan dari dekonsentrasi pekerjaan; penulisannya cukup dapat dipercaya, tetapi mekanis dan kurang berkembang sebagai sintesis.
- [[review-J04|J04]] - Sangat unik secara konseptual dalam membaca kawasan industri sebagai post-suburb dan melampaui property; transisi bukti ke klaim masih longgar.
- [[review-J25|J25]] - Memiliki benang merah integrasi fungsional dan fragmentasi kelembagaan; terlalu difus, birokratis, dan mengulang tesis yang sama.
- [[review-A18|A18]] - Bersih dan teratur, dengan fokus borrowed performance, borrowed functions, dan salah alokasi; kritik independen serta karakter penulis lebih tipis.
- [[review-B12|B12]] - Moderat dan policy-oriented; tetap koheren serta tidak banyak overclaim, tetapi cenderung paraphrastik dan kurang memiliki sintesis unik.
- [[review-B16|B16]] - Kontekstual dan bersyarat dengan kontrol epistemik baik; register Indonesia paling tidak konsisten dan terasa paling dekat dengan terjemahan teknis.

## C

- Tidak ada review pada tier ini.

## D

- Tidak ada review pada tier ini.

## Catatan Batas

- Tier ini menilai bentuk penalaran yang tampak dalam review, bukan kepengarangan asli artikel yang diringkas.
- Kualitas review tidak membuktikan bahwa semua klaim review benar; verifikasi sumber tetap diperlukan untuk klaim substantif.
- Ketiadaan tier C/D tidak menghapus kelemahan lokal pada review tertentu. Ia hanya menunjukkan bahwa kelemahan tersebut masih kompatibel dengan penggunaan terbatas sebagai dokumen kerja.
