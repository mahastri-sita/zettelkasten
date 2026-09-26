# Todo

> **Status eksekusi (9 September 2026):** paket source, query Graphify, audit provenance, dan dokumen kandidat sudah selesai. Checkbox yang tersisa pada bagian question bank berfungsi sebagai pertanyaan reusable atau gate peninjauan pengguna, bukan indikasi bahwa 19 sumber belum dibaca.

## Tujuan Fase

- [x] Menyusun question bank teoritis dan definisional untuk 19 sumber Tier 1.
- [x] Memperlakukan 19 sumber sebagai fondasi teori, mekanisme, konsep, model, dan lensa analitis; bukan sebagai 19 penelitian terdahulu.
- [x] Menghasilkan peta konvergensi, komplementaritas, ketegangan, dan ketidaksetaraan level antarteori.
- [x] Menyediakan dasar evidence-based untuk Bab 2.1 dan Bab 2.3.
- [x] Menjaga corpus 73 penelitian terdahulu sebagai jalur terpisah untuk Bab 2.2.
- [x] Tidak mengedit Argument, Synthesis Product, Contradiction Journey, Calculation, atau Output selama fase question bank ini.

## Batas Epistemik

- [x] Gunakan 19 kode canonical berikut tanpa menambah atau mengurangi sumber: `T01`, `T03`, `T05`, `T06`, `T07`, `T08`, `T09`, `T14`, `T16`, `T17`, `M07`, `M08`, `M13`, `M14`, `M16`, `M17`, `Z01`, `Z03`, `P02`.
- [x] Cocokkan kode, metadata, tipe sumber, dan path dengan `output/kajian/database_sitasi_dasar_teori.md`.
- [x] Pertahankan pemisahan kerja: 19 sumber Tier 1 untuk teori; 73 sumber dalam `output/kajian/kajian_penelitian_terdahulu_borrowed_size_dan_agglomeration_shadow_jakarta_bahan_bab_2_2.md` untuk penelitian terdahulu.
- [x] Jangan menanyakan unit analisis, data, metode, lokasi studi, atau temuan empiris sebagai pertanyaan wajib kepada 19 sumber.
- [x] Ganti pertanyaan `unit analisis` dengan objek penjelasan, level teorisasi, relasi, mekanisme, asumsi, dan batas cakupan.
- [x] Pisahkan selalu `source evidence`, `calculation`, `user position`, `AI inference`, dan `speculation`.
- [x] Bedakan definisi penulis, definisi kerja pengguna, definisi operasional, dan proposisi kandidat.
- [x] Jangan mengubah teori sumber menjadi klaim tentang Jakarta tanpa jembatan analitis dan bukti empiris yang sesuai.
- [x] Jangan menggunakan graph path, degree, community, atau hub status sebagai bukti kausal, bukti historis, atau bukti bahwa dua konsep ekuivalen.

## Graphify Baseline

- [x] Bekukan reviewed run sebagai baseline; jangan menjalankan ulang ekstraksi penuh.
- [x] Gunakan reviewed artifacts di `graphify-lab/runs/tier1-19-txt/graphify-out/`.
- [x] Jadikan `graph-directed.json` rujukan untuk arah relasi dan multiplicity.
- [x] Jadikan `graph.json` rujukan navigasi struktural/undirected.
- [x] Pertahankan raw fragments, base extraction, reviewed extraction, dan `manual-edge-patch.json` sebagai lapisan terpisah.
- [x] Catat baseline: 1,407 nodes, 1,417 directed edges, 1,407 undirected edges, 30 hyperedges, 159 components, 50 binary orphans, dan 754 weak nodes.
- [x] Catat confidence baseline: 1,372 `EXTRACTED`, 43 `INFERRED`, dan 2 `AMBIGUOUS` edges.
- [x] Catat bahwa 196 community berlaku pada reviewed proposal/report; `community-labels.md` yang menyebut 200/200 dianggap metadata stale sampai direkonsiliasi.
- [x] Perlakukan community labels sebagai label navigasi provisional, bukan taksonomi teori final.
- [x] Jangan menggabungkan duplicate labels lintas sumber hanya karena case-folded label sama.
- [x] Jangan menambah edge hanya untuk mengurangi orphan, component, weak node, atau fragmentation.
- [x] Jangan mempromosikan `INFERRED` atau `AMBIGUOUS` menjadi evidence tanpa verifikasi teks sumber.
- [x] Pertahankan anomali provenance `T03`, `Z01`, dan `Z03` seperti tercatat di handoff/audit.
- [x] Catat bahwa token metadata Graphify tidak tersedia dan angka `0/0` bukan bukti tidak ada biaya ekstraksi.
- [x] Catat perbedaan 20 kata antara manifest dan detector sebagai metadata discrepancy, bukan sebagai alasan mengubah corpus.

## Paket Kerja Subagent

### Aturan Umum Subagent

- [x] Jalankan paket source-local secara paralel jika kapasitas memungkinkan.
- [x] Jangan meminta subagent menulis ke canonical graph, Argument, Output, atau Synthesis Product.
- [x] Minta setiap subagent mengembalikan evidence packet terstruktur, bukan opini sintesis bebas.
- [x] Gunakan satu coordinator untuk deduplikasi, klasifikasi evidence, dan merge.
- [x] Jangan melakukan cross-source synthesis secara independen di setiap subagent.
- [x] Jika subagent tidak memiliki locator yang dapat diverifikasi, tandai `verification_needed` dan jangan menganggap tugas selesai.
- [x] Jika subagent menemukan konflik, pertahankan kedua pembacaan dan kirim ke human review; jangan mengambil rata-rata interpretasi.

### Source Packets S01-S19

- [x] `S01`: audit teori, definisi, mekanisme, dan batas `T01`; periksa hubungan ukuran, distribusi, dan kompensasi.
- [x] `S02`: audit `T03`; periksa sharing, matching, learning, heterogeneity, specialization, dan hubungan antar-mikrofoundasi.
- [x] `S03`: audit `T05`; periksa circular/cumulative causation, spread, backwash, dan regional inequality.
- [x] `S04`: audit `T06`; periksa external economies, urban economics, public finance, dan Henry George Theorem.
- [x] `S05`: audit `T07`; periksa increasing returns, elasticity of substitution, transport costs, dan core-periphery.
- [x] `S06`: audit `T08`; periksa agglomeration shadow, lock-in, city-size distribution, dan fungsi pusat.
- [x] `S07`: audit `T09`; periksa bounded agglomeration, congestion, path dependence, dan mekanisme aglomerasi.
- [x] `S08`: audit `T14`; periksa central place, central goods, threshold, range, economic distance, dan centrality.
- [x] `S09`: audit `T16`; periksa ability to invest, complementarity effect, induced investment, dan low-level equilibrium trap.
- [x] `S10`: audit `T17`; periksa growth poles, key/motor industry, territorial agglomeration, dan unbalanced growth.
- [x] `S11`: audit `M07`; periksa mobility, proximity, connectivity, accessibility, derived demand, measurement, dan equity.
- [x] `S12`: audit `M08`; periksa urban systems, network relations, flows, hierarchy, dan cross-source bridges.
- [x] `S13`: audit `M13`; periksa strategic versus comprehensive/traditional planning dan batas penggunaan sebagai lensa teori.
- [x] `S14`: audit `M14`; periksa strategic work, strategic frame, framing ideas, dan strategic spatial planning.
- [x] `S15`: audit `M16`; periksa governance episodes, institutional capacity, collective actor capacity, dan functional territories.
- [x] `S16`: audit `M17`; periksa Type I/Type II multilevel governance, functional/administrative boundaries, dan coordination.
- [x] `S17`: audit `Z01`; periksa urban economics, location equilibrium, households, firms, externalities, land use, housing, dan public finance.
- [x] `S18`: audit `Z03`; periksa core regions, peripheral regions, dependency, authority, dan lock-in.
- [x] `S19`: audit `P02`; periksa polycentricity, complementarity, cooperation, network externalities, synergy, dan Network Cities.

### Large-Source Specialist Passes

- [x] Jalankan pass terpisah untuk `M07`, `M08`, `T08`, `T16`, `T14`, dan `Z01` agar review hyperedge, low-connectivity node, dan cross-source bridge tidak tercampur dalam satu pembacaan.
- [x] Pastikan specialist pass tidak mengulang seluruh isi sumber jika evidence packet sudah memiliki locator yang memadai.
- [x] Prioritaskan hyperedges `Regional cumulative inequality system`, `Growth Inducement Architecture`, `Three Micro-foundations of Urban Agglomeration`, `Accessibility Measurement Chain`, `Four-Track Strategic Planning Approach`, `Governance Transformation Dynamics`, `Nested and Cross-Cutting Territorial Governance`, `Core-Periphery Cumulative Process`, `Path-Dependent Agglomeration Mechanism`, dan `Polarized Development Mechanism`.

### Graph Query Workers Q01-Q08

- [x] `Q01`: telusuri `borrowed size and agglomeration shadow`; pisahkan T08, T01, T09, dan Z01 berdasarkan confidence dan locator.
- [x] `Q02`: telusuri `polarized development core periphery`; bandingkan `Z03`, `T07`, `T08`, `T09`, `T16`, dan `T17` tanpa menyamakan mekanisme.
- [x] `Q03`: telusuri `agglomeration functional specialisation`; periksa `T03`, `T06`, `T07`, `T09`, dan `Z01`.
- [x] `Q04`: telusuri `cumulative causation growth poles low level equilibrium`; pisahkan circular causation, growth pole, dan low-level equilibrium trap.
- [x] `Q05`: telusuri `polycentricity network externalities`; periksa apakah hubungan P02/Z01 dengan M07/T14 eksplisit atau hanya thematic proximity.
- [x] `Q06`: telusuri `accessibility land use transport equity`; gunakan M07 hyperedges sebelum membuat relasi binary tambahan.
- [x] `Q07`: telusuri `strategic spatial planning multilevel governance`; periksa M13, M14, M16, M17, dan P02 sebagai register governance/planning.
- [x] `Q08`: telusuri `central place central goods range`; periksa T14 dan hubungan yang dapat diverifikasi dengan P02/M07.
- [x] Untuk setiap query, simpan query literal, vocabulary expansion, traversal mode, budget, nodes, edges, confidence, locator, dan negative findings.
- [x] Tandai hasil query yang terpotong oleh budget; jangan menyebut node yang tampil sebagai keseluruhan graph.

### Audit Workers A01-A04

- [x] `A01`: audit provenance; pastikan setiap kandidat memiliki source ID, source path, locator, confidence, dan relation type.
- [x] `A02`: audit representation; bandingkan directed/undirected graph dan jelaskan 10 same-endpoint collapses.
- [x] `A03`: audit community metadata; rekonsiliasi 196 versus 200 tanpa mengubah label secara diam-diam.
- [x] `A04`: audit manual patch; pastikan empat edge patch tetap terpisah dari raw extraction dan dapat dilacak ke locator.

## Question Bank Teoritis

### Pertanyaan Inti Untuk Setiap Sumber

- [x] Apa masalah atau fenomena yang hendak dijelaskan sumber?
- [x] Apa objek penjelasan teoretisnya?
- [x] Apa konstruk dan definisi eksplisitnya?
- [x] Relasi apa yang diasumsikan ada antara konstruk tersebut?
- [x] Mekanisme apa yang menghubungkan konstruk-konstruk tersebut?
- [x] Apa asumsi spasial, temporal, institusional, atau ekonominya?
- [x] Pada level atau skala teorisasi apa mekanisme bekerja?
- [x] Apa kondisi yang memungkinkan mekanisme berlaku?
- [x] Apa mekanisme tandingan, efek negatif, atau batas cakupannya?
- [x] Apa yang tidak dapat disimpulkan tentang Jakarta?
- [x] Apakah bagian yang dibaca benar-benar teori, ilustrasi empiris, kritik, atau rekomendasi normatif?
- [x] Apa fungsi sumber bagi skripsi: konsep, mekanisme, asumsi, batasan, counterpoint, atau konteks?

### Pertanyaan Definisional

- [x] Apa definisi eksplisit konsep dalam sumber?
- [x] Konsep ini berfungsi sebagai kondisi, proses, mekanisme, hasil, relasi, atau lensa analitis?
- [x] Apa atribut minimal konsep tersebut?
- [x] Apa konsep pembanding, lawan, atau konsep yang berdekatan?
- [x] Istilah apa yang tampak sinonim tetapi sebenarnya memiliki fungsi berbeda?
- [x] Apa yang dapat dan tidak dapat disimpulkan dari konsep tersebut?
- [x] Apa contoh non-instance yang membantu menetapkan batas konsep?
- [x] Bagaimana konsep ini menempati arsitektur teori: premis, mekanisme, moderator, outcome, atau interpretive lens?
- [x] Apakah definisi ini dapat digunakan untuk `borrowed size`, `agglomeration shadow`, integrasi metropolitan, atau pusat sekunder tanpa perluasan yang tidak sahih?
- [x] Bagian mana yang masih merupakan definisi kerja pengguna, bukan definisi sumber?

### Modul A: Aglomerasi Dan Disekonomi

- [x] Bagaimana `sharing`, `matching`, dan `learning` menghasilkan manfaat aglomerasi?
- [x] Bagaimana ukuran, kepadatan, biaya transportasi, dan increasing returns berhubungan?
- [x] Kapan aglomerasi menghasilkan congestion, harga lahan, polusi, atau eksklusi?
- [x] Apakah sumber membedakan ukuran lokal, fungsi metropolitan, produktivitas, dan kesejahteraan?
- [x] Apakah sumber memberi mekanisme atau hanya alasan konseptual untuk mengharapkan fungsi tertentu?

### Modul B: Spread, Backwash, Dan Polarisasi

- [x] Melalui mekanisme apa pertumbuhan pusat menyebar ke wilayah sekitar?
- [x] Melalui mekanisme apa pusat menarik tenaga kerja, modal, fungsi, atau permintaan?
- [x] Dalam kondisi apa spread dan backwash dapat hadir bersamaan?
- [x] Apa perbedaan penggunaan `growth pole`, `trickle-down`, `backwash`, `spread`, dan `cumulative causation`?
- [x] Apa batas penggunaan teori ini agar tidak berubah menjadi klaim bahwa Jakarta pasti menaungi pusat sekitarnya?

### Modul C: Hierarki, Pusat Sekunder, Dan Spesialisasi

- [x] Bagaimana threshold, range, dan hierarki menjelaskan fungsi berorde tinggi?
- [x] Apa dasar teoretis untuk membedakan pusat sekunder dari unit administratif biasa?
- [x] Apakah pertumbuhan sektor tertentu berarti kematangan fungsi lokal?
- [x] Bagaimana spesialisasi sektoral berbeda dari spesialisasi fungsional?
- [x] Apa keterbatasan asumsi ruang seragam dalam central-place theory?

### Modul D: Jaringan, Aksesibilitas, Dan Polisentrisitas

- [x] Apa perbedaan accessibility, connectivity, mobility, proximity, dan integrasi aktual?
- [x] Kapan jaringan menghasilkan complementarity atau synergy?
- [x] Apakah banyak pusat otomatis berarti jaringan fungsional yang kohesif?
- [x] Apa peran arus, posisi jaringan, massa lokal, dan hubungan lintas pusat?
- [x] Bukti apa yang dibutuhkan sebelum hubungan dengan Jakarta disebut relasional?

### Modul E: Governance Dan Geografi Fungsional

- [x] Bagaimana institusi dan koordinasi lintas batas memoderasi manfaat jaringan?
- [x] Apa perbedaan wilayah fungsional dan yurisdiksi administratif?
- [x] Apakah sumber memberi mekanisme yang dapat diukur atau hanya lensa perencanaan?
- [x] Bagaimana strategi spasial membentuk perhatian dan pilihan tindakan tanpa menjadi bukti kausal?
- [x] Apa yang boleh digunakan sebagai konteks interpretatif tetapi tidak boleh dimasukkan sebagai indikator?

### Modul Integrasi Borrowed Size-Agglomeration Shadow

- [x] Apakah sumber Tier 1 benar-benar mendefinisikan `borrowed size`, atau hanya menyediakan fondasinya?
- [x] Periksa apakah `T01` memberi intuisi awal atau definisi yang dapat dipertahankan; jangan mengasumsikan tanpa teks.
- [x] Bedakan sumber yang menjelaskan manfaat jaringan dari sumber yang menjelaskan dominasi, eksklusi, atau shadow.
- [x] Bedakan own mass, external access, function, performance, welfare, dan resilience.
- [x] Identifikasi kondisi ketika borrowed size dan agglomeration shadow dapat muncul bersamaan.
- [x] Tandai mana teori sumber dan mana konstruksi kerja penelitian ini.
- [x] Pertahankan empat gerbang yang sudah ada jika masih didukung: bukti relasional, pembanding ukuran, kompatibilitas, dan ketahanan.
- [x] Tandai residual fungsi-ukuran, manfaat, beban, dan ketahanan sebagai konsep jembatan atau operasional jika belum menjadi konsep sumber.

## Evidence Packet Schema

- [x] Setiap packet memakai field berikut tanpa perlu membuat taxonomy baru:

```text
task_id:
source_code:
bibliographic_record:
bibliographic_type:
source_file:
access_basis:
identifier:
locator:
verbatim_excerpt:
source_claim:
theoretical_role:
epistemic_status: source evidence | AI inference | user working choice | candidate
assumptions_and_scope:
countermechanism_or_limitation:
not_supported_by_source:
target_section: 2.1 | 2.2-context | 2.3
relation_to_Jakarta: analytical relevance only | direct empirical evidence | unresolved
metadata_caveat:
verification_needed:
```

- [x] Kutipan mempertahankan bahasa asli dan locator yang tersedia.
- [x] Terjemahan diberi label terjemahan, bukan kutipan asli.
- [x] Metadata-only, abstract-only, excerpt-only, dan full-text dibedakan.
- [x] Identifier yang tidak tersedia tetap `null`; jangan ditebak.
- [x] Klaim yang tidak didukung sumber diberi `not_supported_by_source`.
- [x] Setiap packet menyebutkan counterevidence atau alasan mengapa sebuah relasi dibiarkan kosong.

## Graph Query And Evidence Cards

- [x] Buat evidence card untuk relasi `Core Regions` -> `Lock-In`; bedakan `INFERRED` dari bukti teks Z03.
- [x] Verifikasi edge `Core-periphery model` -> `Agglomeration` pada T08 dan catat lintasan community 36/26 sebagai navigasi, bukan kausalitas.
- [x] Verifikasi empat manual edges: T01 `Distribution Problem`, T16 `Low-Level Equilibrium Trap`, T07 `Elasticity of Substitution` -> `Economies of Scale`, dan M13 `Comprehensive Planning` -> `Traditional Land-Use Planning`.
- [x] Pertahankan negative finding `Core Regions` -> `Spatial Strategy Making` sebagai graph gap; jangan membuat bridge tanpa evidence baru.
- [x] Periksa M07 `Connectivity` melalui hyperedge `Accessibility Logic`; jangan menambah binary edge hanya karena node degree-zero.
- [x] Periksa T03 `Heterogeneity of Workers and Firms`; pertahankan ambiguous jika target relasinya tidak unik.
- [x] Review weak/orphan candidates `Network Cities`, `Henry George Theorem`, `City-size distribution`, `Backyard production`, dan T03 `Heterogeneity of Workers and Firms` hanya melalui teks sumber.
- [x] Simpan negative findings sebagai hasil audit, bukan sebagai bukti bahwa hubungan teoretis tidak ada.

## Perbandingan Antarteori

- [x] Bandingkan klaim, mekanisme, dan fungsi konsep; jangan membandingkan seluruh sumber sebagai unit penelitian.
- [x] Klasifikasikan relasi sebagai `convergence`, `complementarity`, `tension`, `different theoretical register`, `not comparable`, atau `silence`.
- [x] Bedakan konsep yang sama dengan fungsi berbeda dari konsep berbeda yang menjelaskan mekanisme serupa.
- [x] Bandingkan T03/T07/T08/T09/Z01 untuk ekonomi aglomerasi tanpa meratakan sharing, matching, learning, increasing returns, lock-in, dan congestion.
- [x] Bandingkan T05/T16/T17/Z03 untuk spread, backwash, growth pole, cumulative causation, core-periphery, dan dependency.
- [x] Bandingkan T14/P02/M08 untuk hierarki, central place, network, polycentricity, complementarity, dan synergy.
- [x] Tempatkan M07/M13/M14/M16/M17 sebagai register aksesibilitas, perencanaan, governance, dan geografi fungsional; jangan paksa semuanya menjadi mekanisme ekonomi.
- [x] Review 32 duplicate-label groups tanpa menghapus source provenance.
- [x] Catat konflik teori dan counterevidence sebelum menulis definisi kerja.

## Mapping Ke Bab 2

- [x] Audit `argument/argument/bab_2_dasar_teori_dan_konsep_kunci_borrowed_size_dan_agglomeration_shadow_jakarta.md` sebagai target mapping, bukan sebagai sumber evidence baru.
- [x] Untuk Bab 2.1, petakan definisi kerja agglomeration, agglomeration economies, agglomeration shadow, borrowed size, metropolitan integration, secondary centre, accessibility, network, dan polycentricity.
- [x] Untuk Bab 2.2, jangan memasukkan 19 sumber sebagai tabel penelitian empiris; gunakan corpus 73 penelitian terdahulu.
- [x] Untuk Bab 2.3, petakan mekanisme, moderator, batas klaim, dan proposisi kandidat.
- [x] Tandai setiap panah diagram sebagai `source-supported`, `candidate`, atau `unresolved`.
- [x] Jangan menyebut P1-P6 sebagai temuan; perlakukan sebagai proposisi/ekspektasi sampai diuji oleh desain penelitian.
- [x] Tandai bagian yang hanya memberi konteks interpretatif dan tidak boleh menjadi indikator.
- [x] Buat rute `2.1`, `2.2-context`, dan `2.3` untuk setiap evidence packet.

## Merge Dan Audit Gate

- [x] Coordinator deduplicate berdasarkan source ID, target ID, relation, source path, dan locator; jangan berdasarkan label saja.
- [x] Tolak packet tanpa endpoint, path sumber, locator, confidence, relation type, atau status epistemik.
- [x] Tolak locator yang out-of-range atau tidak dapat diverifikasi pada canonical TXT.
- [x] Pertahankan disagreement antar-subagent jika target atau relation belum unik.
- [x] Jangan memperbarui graph exports selama fase question bank kecuali ada kebutuhan integritas yang jelas dan disetujui.
- [x] Jika ada patch baru, simpan sebagai reviewed patch terpisah; jangan menimpa raw extraction.
- [x] Setelah merge, periksa unique IDs, resolved endpoints, valid locators, self-loops, duplicate edges, hyperedge members, dan confidence counts.
- [x] Bandingkan before/after nodes, edges, hyperedges, components, orphans, locators, dan confidence classes jika graph memang diperbarui.
- [x] Pastikan graph-shape improvement bukan kriteria keberhasilan substantif.

## Output Fase Ini

- [x] Register 19 sumber dengan metadata dan provenance yang cocok.
- [x] Evidence packet untuk setiap sumber yang benar-benar telah diverifikasi.
- [x] Question bank teoritis dan definisional yang tidak memaksa semua sumber menjawab pertanyaan yang sama.
- [x] Peta konsep dan mekanisme lintas sumber.
- [x] Peta konvergensi, komplementaritas, ketegangan, dan ketidaksetaraan level.
- [x] Matriks rute ke Bab 2.1, Bab 2.2-context, dan Bab 2.3.
- [x] Daftar definisi kerja kandidat, counterevidence, unresolved issues, dan verification needs.
- [x] Paket rekomendasi untuk user review; bukan Synthesis Product final.

## Keputusan Posisi Pengguna

- [x] Tambahkan section keputusan interaktif ke dokumen kandidat yang sama.
- [x] Catat pilihan `[U]` untuk equilibrium versus cumulative: sintesis bersyarat.
- [x] Catat pilihan `[U]` untuk hierarchy versus network: hierarki + jaringan.
- [x] Catat pilihan `[U]` untuk spread versus backwash: dual effect.
- [x] Catat pilihan `[U]` untuk accessibility versus integration: arus + akses.
- [x] Catat pilihan `[U]` untuk governance: moderator relasional.
- [x] Catat pilihan `[U]` untuk planning versus emergence: kombinasi bersyarat.
- [x] Catat pilihan `[U]` untuk borrowed size: multi-sumber kandidat.
- [x] Catat pilihan `[U]` untuk agglomeration shadow: diagnosis relasional ketat.
- [x] Pertahankan tim alternatif sebagai counterposition dan counterevidence.
- [ ] Tinjau ulang pilihan jika data, literatur tambahan, atau refleksi pengguna mengubah posisi.

## Definition Of Done

- [x] Semua 19 kode telah diperiksa pada level yang relevan; `not applicable` boleh digunakan dengan alasan.
- [x] Setiap pertanyaan penting memiliki locator atau ditandai sebagai unresolved.
- [x] Tidak ada klaim substantif yang hanya didukung community, degree, path, atau inferred edge.
- [x] Counterevidence, scope conditions, dan alternative mechanisms terlihat.
- [x] Tidak ada teori sumber yang salah dipresentasikan sebagai temuan empiris Jakarta.
- [x] Tidak ada klaim dari corpus 73 sumber yang dipindahkan ke corpus teori tanpa provenance.
- [x] Definisi penulis, definisi kerja pengguna, dan proposisi kandidat tidak tercampur.
- [x] Satu candidate synthesis dapat ditelusuri kembali ke Source, Calculation, atau user-confirmed position.
- [ ] User telah meninjau dan menyetujui posisi konseptual sebelum file Argument, Synthesis Product, Contradiction Journey, Calculation, atau Output diedit.

## Stop Conditions

> **Status:** semua stop condition diperiksa selama merge; tidak ada yang terpicu. Checkbox di bawah dipertahankan sebagai safeguard untuk fase berikutnya.

- [ ] Berhenti jika source scope bukan 19 canonical Tier 1 TXT.
- [ ] Berhenti jika lebih dari setengah packet subagent gagal, tidak memiliki locator, atau tidak dapat diverifikasi.
- [ ] Berhenti pada kandidat relasi yang hanya didukung label, community, degree, path, atau thematic similarity.
- [ ] Berhenti mempromosikan edge `INFERRED` atau `AMBIGUOUS` menjadi evidence.
- [ ] Berhenti jika graph audit menemukan dangling endpoint, missing locator, duplicate ID, atau unresolved hyperedge.
- [ ] Berhenti jika perbedaan 196/200 community belum direkonsiliasi dan label hendak digunakan sebagai kategori substantif.
- [ ] Berhenti jika sumber hanya tersedia sebagai metadata/abstrak tetapi klaim ditulis seolah-olah berasal dari full text.
- [ ] Berhenti sebelum menulis posisi personal pengguna tanpa konfirmasi eksplisit.
- [ ] Bekukan hasil sebagai candidate package jika sisa persoalan hanya berupa ambiguitas atau pilihan interpretasi pengguna.

## Referensi Operasional

- `output/kajian/database_sitasi_dasar_teori.md`
- `output/kajian/kajian_penelitian_terdahulu_borrowed_size_dan_agglomeration_shadow_jakarta_bahan_bab_2_2.md`
- `argument/argument/bab_2_dasar_teori_dan_konsep_kunci_borrowed_size_dan_agglomeration_shadow_jakarta.md`
- `graphify-lab/runs/tier1-19-txt/graphify-out/graph.json`
- `graphify-lab/runs/tier1-19-txt/graphify-out/graph-directed.json`
- `graphify-lab/runs/tier1-19-txt/graphify-out/GRAPH_REPORT.md`
- `graphify-lab/runs/tier1-19-txt/graphify-out/structural-audit.md`
- `graphify-lab/runs/tier1-19-txt/graphify-out/query-audit.md`
- `graphify-lab/runs/tier1-19-txt/graphify-out/provenance-audit.md`
- `graphify-lab/runs/tier1-19-txt/community-label-proposals-reviewed.json`
- `graphify-lab/runs/tier1-19-txt/manual-edge-patch.json`
- `handoff-graphify-tier1.md`
