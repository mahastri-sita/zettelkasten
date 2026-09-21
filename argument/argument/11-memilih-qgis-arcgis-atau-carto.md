# you asked

> **Rekaman historis — arah metodologis digantikan pada 18 September 2026.** Isi berikut merekam eksplorasi atau penilaian atas rancangan lama. Rancangan aktif sepenuhnya memakai proksi dan sumber terbuka serta multitemporal sesuai bukti; lihat [[output/naskah/bab_1/bab_1_pendahuluan_draf|Bab 1]] dan [[output/naskah/bab_3/bab_3_metode_penelitian_draf_rancangan_kerja|Bab 3]]. Hierarki akses, kewajiban data tertutup, dan batas potong lintang dalam rekaman ini bukan arahan kerja aktif. Locator halaman lama tetap merujuk dokumen yang dahulu diaudit, bukan naskah terbaru.

apa pakai arcgis atau qgis? atau carto?

---

# chatgpt response

Kalau konteksnya **skripsi agglomeration shadow + signaling kuat + ada developer CS yang bisa membantu**, saya **tidak akan memilih salah satu secara eksklusif**. Mereka berada di layer yang berbeda.

Pilihan saya saat ini:

> **QGIS + Python/PostGIS untuk scientific workflow → MapLibre/deck.gl untuk visual product.**  
> **ArcGIS dipakai opsional. CARTO dipakai hanya kalau kebutuhan skala/cloud memang muncul.**

### Perbandingannya

| Tool | Saya pakai untuk | Kekuatan buat proyekmu | Kekurangan |
|---|---|---|---|
| **QGIS** | GIS desktop, eksplorasi data, QA, cartography, processing | Open-source, sangat bagus untuk melihat/mengecek hasil analisis dan membuat peta akademik; punya 3D Map View juga. ([QGIS](https://www.qgis.org/project/overview/?utm_source=chatgpt.com))| Bukan frontend WebGL custom yang ideal; QGIS Server terutama mengekspos layanan OGC seperti WMS/WFS/WMTS. ([QGIS](https://docs.qgis.org/3.44/en/docs/server_manual/services.html?utm_source=chatgpt.com))|
| **ArcGIS Pro + ArcGIS ecosystem** | GIS/3D institusional, WebScene, publikasi enterprise | 3D-nya sangat matang; ArcGIS Maps SDK punya `SceneView` untuk aplikasi web 3D dan WebScene bisa dipakai lintas Pro/Online/web. ([Esri Developer](https://developers.arcgis.com/javascript/latest/references/core/views/SceneView/?utm_source=chatgpt.com))| Ekosistem lebih proprietary; kalau ingin visualisasi custom yang sangat eksperimental, kalian mulai bermain di API Esri dan bahkan custom WebGL `RenderNode` masih ditandai experimental. ([Esri Developer](https://developers.arcgis.com/javascript/latest/references/core/views/3d/webgl/RenderNode/?utm_source=chatgpt.com))|
| **CARTO** | cloud spatial analytics + serving dataset besar | Sangat cocok dengan deck.gl; stack visualisasinya WebGL2/WebGPU dan dibuat untuk dataset geospasial skala besar. ([CARTO Docs](https://docs.carto.com/carto-for-developers/key-concepts/carto-for-deck.gl?utm_source=chatgpt.com))| Untuk satu skripsi bisa jadi overkill; nilai utamanya terasa ketika data sudah hidup di warehouse/cloud dan perlu serving/scalability. ([CARTO Docs](https://docs.carto.com/carto-for-developers/overview?utm_source=chatgpt.com))|
| **MapLibre + deck.gl** | **aplikasi final/interaktif** | Paling bebas untuk extrusion, hexbin, flow, animation, time slider, typology, custom interaction. CARTO sendiri memakai deck.gl dan mendukung MapLibre sebagai basemap. ([CARTO Docs](https://docs.carto.com/carto-for-developers/key-concepts/carto-for-deck.gl/basemaps?utm_source=chatgpt.com))| Perlu development sungguhan |
| **PostGIS + Python** | **mesin analitik** | Metodologi tetap auditable/reproducible; frontend hanya membaca hasil | Bukan visual layer |

## Jadi arsitektur yang saya pilih

```text
                 SCIENTIFIC WORK
─────────────────────────────────────────

 GEE / BPS / OSM / lainnya
             │
             ▼
          PYTHON
     GeoPandas / stats
     network analysis
             │
             ▼
          POSTGIS
             │
     ┌───────┴────────┐
     │                │
     ▼                ▼
   QGIS            notebooks
 QA / inspect      methodology
 cartography       validation


                 ↓ hasil final ↓


               VISUAL PRODUCT
─────────────────────────────────────────

             PostGIS
                │
                ▼
       tiles / GeoJSON / API
                │
                ▼
      MAPLIBRE + DECK.GL
                │
     ┌──────────┼───────────┐
     ▼          ▼           ▼
   3D map    flows       time slider
     │          │           │
     ├──────────┼───────────┤
     ▼          ▼           ▼
 typology     centres     shadow
 borrowed     hierarchy   analysis
 size
                │
                ▼
      INTERACTIVE RESEARCH ATLAS
```

Menurut saya ini lebih kuat daripada semuanya dikerjakan ArcGIS.

### Kenapa QGIS tetap saya pakai

Karena kamu **planner**, bukan frontend developer.

Kamu perlu tempat untuk membuka layer dan berpikir:

> “Ini hasilnya masuk akal nggak?”

> “Boundary-nya rusak nggak?”

> “Flow ini benar nggak?”

> “CRS-nya salah nggak?”

> “Klasifikasi borrowed-size ini secara spasial terlihat janggal nggak?”

QGIS sangat cocok menjadi **workbench-mu**. Ia gratis/open-source, punya processing dan cartographic workflow yang matang. ([QGIS](https://www.qgis.org/project/overview/?utm_source=chatgpt.com))
Jadi saya tidak akan mengganti QGIS dengan aplikasi WebGL.

**QGIS = laboratorium.**

**WebGL app = observatorium/pameran hasil.**

---

## Kapan saya justru memilih ArcGIS?

Kalau ternyata kampus/Bappenas/instansi tempatmu bekerja menyediakan lisensi dan workflow mereka memang Esri-heavy, ArcGIS menjadi sangat menarik.

Terutama kalau kamu ingin dengan relatif cepat menghasilkan:

```text
terrain
+
extruded buildings
+
3D scene
+
WebScene
+
interactive web app
```

ArcGIS memang memiliki pipeline 3D resmi dari WebScene/Scene Viewer ke SDK JavaScript. ([Esri Developer](https://developers.arcgis.com/javascript/latest/scenes-3d/?utm_source=chatgpt.com))
Jadi kalau targetmu:

> **“Saya butuh hasil 3D institusional yang polished cepat.”**

ArcGIS unggul.

Kalau targetmu:

> **“Saya ingin membangun visual language baru untuk menunjukkan metropolitan flows, borrowed size, shadow, animated commuting, dynamic extrusion.”**

Saya pilih:

> **deck.gl + MapLibre.**

Karena kalian punya developer, justru sayang kalau semua dibatasi UX ArcGIS.

---

# CARTO saya taruh belakangan

CARTO bukan sebenarnya pesaing langsung QGIS.

Lebih tepat:

```text
QGIS
= desktop GIS/workbench

CARTO
= cloud geospatial platform

deck.gl
= visualization engine
```

Dan CARTO sendiri sekarang memang menjadikan deck.gl sebagai teknologi visualisasi custom serta dapat menggunakan MapLibre untuk basemap. ([CARTO Docs](https://docs.carto.com/carto-for-developers/key-concepts/carto-for-deck.gl?utm_source=chatgpt.com))
CARTO mulai menarik kalau suatu saat datamu:

```text
10 juta+
50 juta+
100 juta+ observations

commuting
mobile positioning
GPS
building footprints
H3 cells
time-series
```

dan kamu ingin query data cloud tanpa mengirim semuanya ke browser. CARTO memang dirancang untuk menghubungkan aplikasi langsung ke warehouse seperti BigQuery, Snowflake, Databricks, Redshift, atau PostgreSQL. ([CARTO Docs](https://docs.carto.com/carto-for-developers/overview?utm_source=chatgpt.com))
Untuk skripsi S1?

**Belum tentu perlu.**

Jangan menambah infrastructure karena kelihatan enterprise.

---

# Jadi kalau mulai besok

**Kamu:**

```text
QGIS
+
Python
+
PostGIS
+
GEE
```

**Developer:**

```text
TypeScript
+
MapLibre GL
+
deck.gl
```

Lalu hanya kalau perlu:

```text
Three.js → exotic 3D
CARTO   → scale/cloud
ArcGIS  → institutional interoperability
Tauri   → desktop packaging
```

Dan ini punya keuntungan signaling yang saya rasa penting untukmu:

Bukan CV yang mengatakan:

> “Menguasai ArcGIS.”

melainkan:

> **“Developed an interactive WebGL metropolitan analytics system backed by a reproducible Python/PostGIS urban-science pipeline.”**

