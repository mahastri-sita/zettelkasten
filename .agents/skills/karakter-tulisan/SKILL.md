---
name: karakter-tulisan
description: Menilai atau menyunting prosa riset berbahasa Indonesia agar keputusan intelektual dan karakter penulis terasa, sambil menjaga ketepatan bukti. Gunakan untuk permintaan tentang suara penulis, tulisan yang terlalu steril, atau ketidaksempurnaan prosa yang bermakna; bukan untuk koreksi bahasa rutin atau naskah akademik berbahasa Inggris.
---

# Karakter tulisan

Tujuan skill ini adalah mempertahankan jejak penalaran seseorang dalam prosa riset berbahasa Indonesia. Tulisan yang terasa manusiawi menunjukkan apa yang penulis pilih untuk bedakan, ragukan, tekankan, dan biarkan terbuka. Jangan menanam salah ketik, kekeliruan gramatikal, fakta rekaan, anekdot fiktif, atau ketidakteraturan acak demi kesan manusia.

## Batas kerja

- Berlaku untuk tulisan berbahasa Indonesia dalam vault ini, terutama kajian, review, argumen, dan sintesis. Ikuti `AGENTS.md` dari akar hingga folder sasaran. Permintaan menilai atau menganalisis tidak mengizinkan penyuntingan file Output atau Argument; ubah file hanya saat pengguna memang meminta penyuntingan sesuai aturan folder.
- Bedakan suara yang tampak dalam teks dari identitas atau proses penulisnya. Tier list menilai kualitas review, bukan membuktikan siapa yang menulisnya atau bagaimana proses penulisannya.
- Saat memakai `output/kajian/tier-list-kepenulisan-kajian-pendahuluan.md`, gunakan kode review hanya untuk menemukan TXT asal yang berkode sama di `source/`. Baca prosa pada TXT sumber sebelum mengambil pelajaran gaya. Tier S pada review tidak otomatis berarti tulisan sumbernya teladan. Catat bahasa asli dan akses yang sungguh tersedia; jangan menganggap review Bahasa Indonesia sebagai contoh kalimat penulis artikel berbahasa Inggris.
- TXT hasil ekstraksi PDF dapat memuat pemenggalan baris, sambungan kolom, karakter rusak, atau salah baca OCR. Jangan menirunya sebagai “ketidaksempurnaan manusia” dan jangan menyimpulkan pilihan penulis dari artefak ekstraksi.
- Preferensi yang dinyatakan pengguna saat skill dibuat: **diagnostik tenang**, tajam membedakan konsep dan batas bukti. Terapkan ini sebagai suara default sampai pengguna meminta karakter lain. Belum ada sampel tulisan pribadi pengguna; review dalam tier list adalah korpus pembanding, bukan bukti gaya asli pengguna. Bila sampel pribadi kelak tersedia, kalibrasikan kembali tanpa menganggap preferensi awal sebagai aturan tetap.
- Pertahankan bahasa file, tujuan genre, istilah teknis yang perlu, kutipan, angka, sitasi, lokator, dan batas klaim. Jangan mengubah inferensi AI menjadi posisi pengguna atau menyamarkan konflik bukti.

## Pembacaan sebelum menyunting

1. Tentukan tugasnya: diagnosis saja, revisi bagian tertentu, atau penulisan baru. Tetapkan pembaca dan tingkat formalitas dari permintaan serta teks.
2. Temukan keputusan penulis yang sudah ada: pembedaan konsep, pilihan kasus atau angka, kritik terhadap sumber, keraguan yang beralasan, dan tesis yang terus kembali. Identifikasi kalimat yang membawa keputusan itu, bukan sekadar istilah yang terdengar akademis.
3. Pilah setiap gesekan prosa menurut akibatnya:
   - **Perbaiki:** salah fakta atau atribusi, loncatan bukti-ke-klaim, batas kausal kabur, ambiguitas yang mengubah makna, terjemahan teknis kaku, repetisi lintas bagian tanpa fungsi baru, dan susunan yang menyembunyikan tesis.
   - **Pertimbangkan untuk dipertahankan:** variasi panjang kalimat, transisi yang tidak selalu eksplisit, pengulangan istilah inti yang menjaga referen, paragraf yang lebih padat saat bukti memang berat, keberatan yang belum tuntas, atau koreksi diri yang benar-benar menunjukkan perubahan penilaian.
   - **Jangan buat-buat:** kekacauan sengaja, kelakar yang tidak sesuai genre, kata-kata ragu tanpa alasan, kalimat patah untuk drama, pengakuan orang pertama yang tidak berasal dari pengguna, atau larangan mekanis atas tanda baca dan kosakata.
4. Uji satu per satu: apakah bagian yang kurang mulus itu membantu pembaca mengikuti pikiran penulis? Jika tidak, rapikan. Jika ya, jangan poles hanya untuk menyamakan ritme.

## Cara membangun karakter

- Dahulukan satu pembedaan atau diagnosis yang mengubah cara pembaca memahami bahan. Tunjukkan kaitannya dengan bukti dan batasnya. Ketajaman lahir dari keputusan ini, bukan dari kata sifat yang kuat.
- Untuk suara default, sampaikan diagnosis tanpa gestur retoris yang membesar-besarkan. Letakkan batas bukti dekat dengan klaim yang dibatasinya; jangan menimbun seluruh caveat di penutup. Biarkan tesis terlihat lebih kuat daripada inventaris angka, tetapi jangan membuatnya lebih pasti daripada sumbernya.
- Pilih kedalaman yang tidak rata secara sadar. Beri ruang lebih pada temuan yang mengubah argumen; padatkan angka dan caveat yang hanya mengulang fungsi sebelumnya. Ketidaksimetrian harus mengikuti bobot intelektual.
- Biarkan istilah teknis berulang bila referennya sama. Hindari pergantian sinonim hanya untuk variasi. Campuran bahasa Indonesia dan istilah Inggris boleh bila istilah itu kerja konseptual, bukan akibat terjemahan setengah jadi.
- Gunakan keberatan atau kalimat bersyarat pada titik yang memang belum diputuskan bukti. Bila tabel dan narasi sumber bertentangan, tampilkan pertentangannya; jangan menciptakan rekonsiliasi yang tidak didukung.
- Sesuaikan register dengan genre. Review boleh lebih forensik; Argument pribadi dapat lebih eksploratif jika penulisnya demikian; Output akademik perlu lebih rapat dan dapat ditelusuri. Jangan mengimpor gaya satu genre ke semua file.

## Pemeriksaan akhir dan respons

- Bandingkan hasil dengan teks asal: klaim, sumber, angka, ketidakpastian, dan posisi penulis tetap utuh atau perubahan substantifnya ditandai untuk keputusan pengguna.
- Periksa apakah revisi hanya menghapus tanda yang dianggap “AI”. Jika iya, cari kembali pilihan intelektual yang seharusnya menjadi pusat kalimat. Jangan mengklaim dapat menentukan atau menjamin tulisan “terlihat manusia”.
- Untuk diagnosis, tunjukkan beberapa petikan pendek dengan alasan spesifik dan bedakan masalah substantif dari selera gaya. Untuk revisi yang diizinkan, berikan teks hasil dan catatan singkat tentang keputusan penting, terutama yang menyangkut bukti atau makna.

Baca [pembacaan TXT sumber](references/pembacaan-korpus.md) ketika perlu contoh konkret dari sumber yang dikodekan dalam tier list atau penjelasan mengapa pedoman humanizer umum tidak cukup untuk tulisan riset Indonesia.
