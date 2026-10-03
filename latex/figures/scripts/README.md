# Skrip peta Bab 4 dan zonal GHSL

Dibuat 3 Oktober 2026 (putaran 7b). Urutan:

1. `extract_adm.py <work> <idn_admin_boundaries.gdb>` — ambil batas COD-AB HDX (unduh dari https://data.humdata.org/dataset/cod-ab-idn; jangan di-commit) untuk wilayah studi.
2. `zonal.py <work> <work>/out/adm3_bodetabek.gpkg` — jumlah zonal GHSL total/NRES per kecamatan, masker kawasan industri Kemenperin, ambang P66/P75/P80. Membaca tabel WSM dari catatan sumber vault.
3. `maps.py <work> <outdir>` — delapan peta G4.1–G4.8. Membutuhkan `<work>/osm/net.json` (Overpass: `way[highway=motorway]` dan `way[railway~rail|subway|light_rail]`, bbox -6.85,106.35,-5.9,107.3), `<work>/osm/newtowns.json` (Nominatim), dan `<work>/out/od2023.json` (Tabel 2 Komuter 2023, DKI digabung).

Lingkungan: Python 3.11 dengan geopandas 1.2, rasterio 1.4, rasterstats, matplotlib, pyogrio (GDAL 3.12). Raster GHSL dan ZIP Kemenperin diekstrak dari `source/dataset/` ke `<work>/ghsl` dan `<work>/ki`.

`bps_link.js` (puppeteer) hanya mengambil tautan "Unduh Publikasi" dari halaman BPS; situs menolak akses beruntun.
