# Medan Relasional Jakarta

> **Rekaman historis — arah metodologis digantikan pada 18 September 2026.** Isi berikut merekam eksplorasi atau penilaian atas rancangan lama. Rancangan aktif sepenuhnya memakai proksi dan sumber terbuka serta multitemporal sesuai bukti; lihat [[output/naskah/bab_1/bab_1_pendahuluan_draf|Bab 1]] dan [[output/naskah/bab_3/bab_3_metode_penelitian_draf_rancangan_kerja|Bab 3]]. Hierarki akses, kewajiban data tertutup, dan batas potong lintang dalam rekaman ini bukan arahan kerja aktif. Locator halaman lama tetap merujuk dokumen yang dahulu diaudit, bukan naskah terbaru.


Prototipe WebGL satu layar untuk memperkenalkan rancangan skripsi tentang integrasi metropolitan, residual fungsi, manfaat–beban, dan ketahanan diagnosis. Antarmuka dibuat sebagai instrumen presentasi, bukan sebagai dashboard hasil analisis.

> **Ilustrasi prototipe — bukan hasil penelitian.** Seluruh nilai titik, arus, klasifikasi, dan perubahan antarskenario adalah data sintetis untuk mendemonstrasikan logika metode.

## Membuka demo

Di macOS, klik dua kali `start_demo.command`. Demo akan menjalankan server lokal dan membuka browser secara otomatis. Terminal perlu dibiarkan terbuka selama presentasi; tekan `Control+C` setelah selesai.

Alternatif dari Terminal:

```bash
npm install
npm run build
npm run preview
```

Kode sumber berada di `src/`, aset lokal berada di `public/`, dan hasil siap presentasi berada di `dist/`.

## Cara menggunakan

- Seret peta untuk menggeser, seret dengan klik kanan untuk memutar, dan gunakan roda/trackpad untuk memperbesar.
- Klik pilar atau bidang nol pada `Pusat A–F` untuk membaca profil titik demo.
- Gunakan mode `Garis dasar`, `Skenario`, `Selisih`, dan `Ketahanan`, atau tombol angka `1–4`.
- Gunakan preset bukti `EV-OPEN`, `EV-MIN`, dan `EV-FULL`. Preset tersebut adalah simulasi konfigurasi bukti, bukan perubahan kondisi metropolitan.
- Buka `Sensitivitas` untuk mengubah ambang klasifikasi tanpa menimpa nilai garis dasar.
- Buka `Bukti` untuk melihat 11 modul manifest, status `D/A/S/P/∅`, tingkat `M/U`, dan gerbang label ketat.
- Tekan `R` untuk kembali ke kamera presentasi dan `Esc` untuk menutup panel.

## Cara membaca visual

- Bidang melayang menandai residual nol.
- Pilar teal naik untuk surplus fungsi relatif; pilar plum bergerak menuju permukaan untuk defisit.
- Halo menunjukkan beban, sedangkan busur dan jejak bergerak menunjukkan hubungan metropolitan.
- Jakarta ditampilkan sebagai inti tetap berwarna coral. Jejak fungsional tidak mengubah batas yurisdiksi.

Klasifikasi mengikuti aturan kerja rancangan: `borrowed size`, `agglomeration shadow`, campuran, relatif independen, periferi lemah, dan tidak terselesaikan. Kelas tidak boleh dibaca sebagai kesimpulan empiris ataupun hubungan kausal.

## Data dan provenance

- Titik `Pusat A–F`, seluruh metrik, dan seluruh arus dibuat khusus sebagai data demo. Nama kota pada basemap hanya membantu orientasi; titik tidak mengklaim delineasi pusat sekunder final.
- Batas administratif lokal menggunakan geoBoundaries `gbOpen` Indonesia ADM2, boundary ID `IDN-ADM2-22746128`, tahun representasi 2020, lisensi `CC BY 3.0 IGO`. Metadata lengkap tersimpan di `public/data/boundary_metadata.json`. Geometri hanya dipakai sebagai konteks kartografis.
- Basemap menggunakan gaya Positron dari OpenFreeMap, dengan data OpenStreetMap/OpenMapTiles dan atribusi tetap tersedia pada peta. Basemap memerlukan internet; bila tile gagal, batas lokal dan seluruh layer demo tetap ditampilkan.
- Rujukan substantif aktif adalah `../naskah/bab_1/bab_1_pendahuluan_draf.md` dan `../naskah/bab_3/bab_3_metode_penelitian_draf_rancangan_kerja.md`. Prototipe ini mempertahankan ilustrasi skenario lama sebagai rekaman eksplorasi.

## Teknologi dan batas performa

Prototipe menggunakan Vite, React, TypeScript, MapLibre GL JS melalui `react-map-gl`, dan deck.gl dalam mode interleaved. Rasio piksel dibatasi maksimum 1,5. Animasi berhenti saat tab tidak aktif dan dinonaktifkan bila sistem memilih reduced motion. Browser tanpa WebGL memperoleh fallback statis.

Build produksi terakhir dapat dibuat ulang dengan:

```bash
npm run build
```
