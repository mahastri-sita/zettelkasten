# Handoff: Graphify Tier 1

**Tanggal:** 7 September 2026.
**Fokus sesi berikutnya:** bangun knowledge graph dari 19 sumber teori Tier 1 dengan 10 agent semantic paralel.

## Keputusan Pengguna

- Corpus final untuk Graphify adalah **19 sumber**, bukan 60.
- Gunakan Tier 1 saja. Jangan menghidupkan kembali Tier 2, studi empiris, studi kasus, atau ulasan sekunder.
- Angka kerja final adalah 19. Angka 17 adalah hitungan sementara untuk tulang punggung teori/kerangka dari subset A/B, bukan corpus final.
- `graphify-lab` lama sengaja dihapus agar sesi baru dimulai dari staging dan run yang bersih.

## Sumber Kebenaran

- `output/kajian/database_sitasi_dasar_teori.md` berisi hanya 19 karya dan path sumbernya.
- `Todo.md` berisi roadmap eksekusi yang harus diikuti.
- Extraction spec: `/Users/mac/.config/opencode/skills/graphify/references/extraction-spec.md`.

## 19 Kode Terkunci

`T01`, `T03`, `T05`, `T06`, `T07`, `T08`, `T09`, `T14`, `T16`, `T17`, `M07`, `M08`, `M13`, `M14`, `M16`, `M17`, `Z01`, `Z03`, `P02`.

## Keadaan Workspace

- Database telah ditulis ulang menjadi daftar Tier 1 saja.
- `Todo.md` lama telah dihapus dan ditulis ulang sebagai roadmap Graphify 19 sumber.
- Seluruh `graphify-lab` lama, termasuk input copy, manifest, control run, cache, fragment, dan graph, telah dihapus.
- Tidak ada semantic extraction full corpus yang berhasil dijalankan pada sesi ini.
- Berkas di `source/` tidak diubah.
- Ada banyak perubahan dan berkas tidak terkait di worktree; jangan menjalankan reset, checkout, clean global, atau mengubahnya.

## Langkah Sesi Berikutnya

1. Baca database dan `Todo.md`; jangan gunakan daftar 60 dari konteks lama.
2. Buat ulang `graphify-lab/full-corpus-txt/`, lalu salin tepat 19 TXT dari path sumber pada database. Jangan salin PDF.
3. Buat manifest baru dan deteksi Graphify. Target: tepat 19 file semantic dan 0 file review/PDF.
4. Buat run baru, misalnya `graphify-lab/runs/tier1-19-txt/`.
5. Bagi 19 TXT menjadi 10 chunk berdasarkan jumlah kata. Buku besar (`Z01`, `Z03`, `M07`, `M08`, `T05`, `T08`, `T14`, `T16`) perlu diberi ruang konteks; jangan sekadar membagi dua file per agent.
6. Dispatch 10 agent `general`/general-purpose secara paralel dalam satu batch. Jangan gunakan agent read-only/explore karena setiap agent harus menulis fragment.
7. Set `DEEP_MODE=true`, berikan extraction spec secara konsisten, dan tulis satu `.graphify_chunk_NN.json` per agent ke run baru.
8. Validasi 10 fragment, merge tanpa menghapus raw fragment, bangun graph undirected dan directed, jalankan health/community/query smoke tests, lalu audit provenance.

## Aturan Ekstraksi

- Input semantic hanya TXT canonical dari 19 karya.
- `source_file` pada setiap node, edge, dan hyperedge harus berupa path absolut yang diberikan kepada agent, verbatim.
- `EXTRACTED` hanya untuk relasi yang eksplisit di teks; `INFERRED` dan `AMBIGUOUS` tidak boleh dipromosikan menjadi evidence.
- Setiap edge wajib memiliki `confidence` dan `confidence_score` sesuai extraction spec.
- Jangan mengarang metadata, locator, sitasi, konsep, atau relasi.
- Catat kegagalan, timeout, truncation, OCR/TXT limitation, dan locator yang hilang.
- Host-agent OpenCode adalah route semantic yang dipilih; jangan menunggu `OPENAI_API_KEY` atau `ANTHROPIC_API_KEY`.

## Catatan Provenance

- `T03` adalah bab buku secara bibliografis, tetapi TXT lokal berada di `source/working-paper/`.
- `Z01` memakai label `1996` pada nama file, sedangkan title page menyebut edisi kedelapan International Edition dan copyright 2012.
- `Z03` adalah draft bertanggal Desember 1967.
- Kode dan path lokal harus dipertahankan; jangan menormalisasi nama file secara manual.

## Skill Berikutnya

- Gunakan skill `graphify` untuk pipeline, extraction schema, validation, merge, dan graph build.
- Gunakan skill `handoff` hanya bila sesi kembali perlu dipindahkan.
