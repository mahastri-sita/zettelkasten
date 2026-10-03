"""Bab 4 maps G4.1-G4.8 (UTM 48S, one style, Times New Roman, decimal comma)."""
import sys, json, re
import numpy as np, pandas as pd, geopandas as gpd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, FancyArrow, Rectangle
from matplotlib.lines import Line2D
from matplotlib.colors import BoundaryNorm, LogNorm, ListedColormap
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
from shapely.geometry import box, Point, LineString

S, OUTDIR = sys.argv[1], sys.argv[2]
VAULT = "/Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten"
plt.rcParams.update({"font.family": "Times New Roman", "font.size": 9, "axes.linewidth": 0.6})
UTM = 32748
adm2 = gpd.read_file(f"{S}/out/adm2_region.gpkg").to_crs(UTM)       # kab/kota in region incl. neighbours
adm1 = gpd.read_file(f"{S}/out/adm1_java.gpkg").to_crs(UTM)         # Java provinces (inset)
kec = gpd.read_file(f"{S}/out/kecamatan_141.gpkg").to_crs(UTM)
dki_kec = gpd.read_file(f"{S}/out/kecamatan_dki.gpkg").to_crs(UTM)

JABO = ["Kota Jakarta Selatan", "Kota Jakarta Timur", "Kota Jakarta Pusat", "Kota Jakarta Barat", "Kota Jakarta Utara",
        "Kabupaten Bogor", "Kota Bogor", "Kota Depok", "Kabupaten Tangerang", "Kota Tangerang", "Kota Tangerang Selatan",
        "Kabupaten Bekasi", "Kota Bekasi"]
adm2["jabo"] = adm2["nama"].isin(JABO)
dki = adm2[adm2["nama"].str.startswith("Kota Jakarta")]
dki_union = dki.union_all()
jabo = adm2[adm2.jabo]
xmin, ymin, xmax, ymax = jabo.total_bounds
pad = 6000
EXT = (xmin - pad, xmax + pad, ymin - pad - 22000, ymax + pad)
SEA = "#dfe9f2"; NEIGH = "#d4d4d4"; EDGE = "#4d4d4d"

def fmt(x, d=0):
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

def base(ax, neighbours=True, dki_grey=False, labels=False):
    ax.set_facecolor(SEA)
    land = adm2
    land.plot(ax=ax, color=NEIGH, edgecolor="white", linewidth=0.5, zorder=0)
    if dki_grey:
        dki.plot(ax=ax, color="#c9c9c9", edgecolor="white", linewidth=0.3, zorder=1)
    ax.set_xlim(EXT[0], EXT[1]); ax.set_ylim(EXT[2], EXT[3]); ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel(""); ax.set_ylabel("")
    if neighbours:
        for _, r in adm2[~adm2.jabo].iterrows():
            c = r.geometry.intersection(box(EXT[0], EXT[2], EXT[1], EXT[3]))
            if c.is_empty or c.area < 4e7 or "Waduk" in r["nama"]: continue
            p = c.representative_point()
            if min(p.x - EXT[0], EXT[1] - p.x, p.y - EXT[2], EXT[3] - p.y) < 7000: continue
            ax.text(p.x, p.y, r["nama"].replace("Kabupaten ", "Kab. "), fontsize=6.5, color="#7a7a7a", ha="center", va="center", style="italic", zorder=6)

def outline(ax, lw=0.7):
    jabo.boundary.plot(ax=ax, color=EDGE, linewidth=lw, zorder=5)
    gpd.GeoSeries([dki_union], crs=UTM).boundary.plot(ax=ax, color="black", linewidth=lw + 0.5, zorder=5)

def furniture(ax, src):
    # scale bar 20 km
    x0, y0 = EXT[0] + 4000, EXT[2] + 4000
    for i, c in enumerate(["black", "white"]):
        ax.add_patch(Rectangle((x0 + i * 10000, y0), 10000, 900, facecolor=c, edgecolor="black", linewidth=0.5, zorder=10))
    for i, t in enumerate(["0", "10", "20 km"]):
        ax.text(x0 + i * 10000, y0 + 1500, t, ha="center", fontsize=7, zorder=10)
    # north arrow
    xn, yn = EXT[1] - 5000, EXT[3] - 12000
    ax.add_patch(FancyArrow(xn, yn, 0, 7000, width=900, head_width=3200, head_length=3000, color="black", zorder=10))
    ax.text(xn, yn - 1200, "U", ha="center", va="top", fontsize=9, fontweight="bold", zorder=10)
    ax.text(EXT[1] - 1500, EXT[2] + 1500, src, ha="right", va="bottom", fontsize=6.3, color="#333333", zorder=10,
            bbox=dict(facecolor="white", alpha=0.75, edgecolor="none", pad=1.5))

def inset(fig, rect=(0.735, 0.70, 0.24, 0.16)):
    a = fig.add_axes(rect); a.set_facecolor(SEA)
    adm1.plot(ax=a, color="#d2d2d2", edgecolor="white", linewidth=0.3)
    gpd.GeoSeries([box(EXT[0], EXT[2], EXT[1], EXT[3])], crs=UTM).boundary.plot(ax=a, color="red", linewidth=0.9)
    b = adm1.total_bounds; a.set_xlim(b[0], b[2]); a.set_ylim(b[1], b[3]); a.set_xticks([]); a.set_yticks([]); a.set_xlabel(""); a.set_ylabel("")
    for s in a.spines.values(): s.set_linewidth(0.5)
    a.text(0.02, 0.05, "Pulau Jawa", transform=a.transAxes, fontsize=6)

def save(fig, name):
    for a in fig.axes:
        if a.get_position().height > 0.1: a.set_xlabel(""); a.set_ylabel("")
    fig.savefig(f"{OUTDIR}/{name}.pdf", bbox_inches="tight", pad_inches=0.03)
    fig.savefig(f"{OUTDIR}/{name}.png", dpi=300, bbox_inches="tight", pad_inches=0.03)
    plt.close(fig); print("saved", name)

def newfig():
    w = 6.3; h = w * (EXT[3] - EXT[2]) / (EXT[1] - EXT[0])
    fig, ax = plt.subplots(figsize=(w, h)); fig.subplots_adjust(0, 0, 1, 1)
    return fig, ax

# ---------------- G4.1 admin/status ----------------
fig, ax = newfig(); base(ax)
cls = {"DKI Jakarta (inti)": "#7f7f7f", "Kota": "#bdbdbd", "Kabupaten": "#ffffff"}
for _, r in jabo.iterrows():
    k = "DKI Jakarta (inti)" if r["nama"].startswith("Kota Jakarta") else ("Kota" if r["nama"].startswith("Kota") else "Kabupaten")
    gpd.GeoSeries([r.geometry], crs=UTM).plot(ax=ax, color=cls[k], edgecolor="white", linewidth=0.4, zorder=2)
outline(ax)
lab = jabo[~jabo["nama"].str.startswith("Kota Jakarta")]
for _, r in lab.iterrows():
    p = r.geometry.representative_point()
    ax.text(p.x, p.y, r["nama"].replace("Kabupaten", "Kab.").replace("Kota Tangerang Selatan", "Kota Tangerang\nSelatan"),
            fontsize=7.2, ha="center", va="center", zorder=7, bbox=dict(facecolor="white", alpha=0.6, edgecolor="none", pad=0.6))
p = dki_union.representative_point(); ax.text(p.x, p.y, "DKI Jakarta", fontsize=8, fontweight="bold", ha="center", zorder=7, color="white")
ax.legend(handles=[Patch(facecolor=v, edgecolor="#666", label=k) for k, v in cls.items()] +
          [Patch(facecolor=NEIGH, edgecolor="#999", label="Di luar wilayah penelitian")],
          loc="lower left", bbox_to_anchor=(0.0, 0.07), fontsize=7, frameon=True, framealpha=0.9)
ax.text(EXT[0] + 3000, EXT[3] - 5000, "Kepulauan Seribu (DKI) tidak digambar;\ntidak tercakup tabulasi komuter.", fontsize=6.5, va="top")
furniture(ax, "Batas: COD-AB HDX (BPS, 2020). Proyeksi UTM 48S."); inset(fig); save(fig, "bab4_admin_status")

# ---------------- G4.2 density ----------------
fig, ax = newfig(); base(ax, dki_grey=True)
bins = [0, 2000, 5000, 8000, 11000, 20000]
cmap = ListedColormap(["#fff5eb", "#fdd0a2", "#fd8d3c", "#d94801", "#7f2704"])
norm = BoundaryNorm(bins, cmap.N)
kec.plot(ax=ax, column="kepadatan", cmap=cmap, norm=norm, edgecolor="white", linewidth=0.25, zorder=2)
outline(ax)
labs = [f"{fmt(bins[i])}–{fmt(bins[i+1])}" for i in range(len(bins) - 1)]
ax.legend(handles=[Patch(facecolor=cmap(i), edgecolor="#888", label=labs[i]) for i in range(len(labs))] + [Patch(facecolor="#c9c9c9", label="DKI Jakarta (inti)")],
          title="Kepadatan (jiwa/km²)", loc="lower left", bbox_to_anchor=(0.0, 0.07), fontsize=7, title_fontsize=7.5, framealpha=0.9)
furniture(ax, "Data: BPS, WSM 2024, Lampiran 3. Batas: COD-AB HDX."); inset(fig); save(fig, "bab4_kepadatan_kecamatan")

# ---------------- G4.4 % commuters to core ----------------
fig, ax = newfig(); base(ax, dki_grey=True)
bins = [0, 7, 15, 25, 35, 50]
cmap = ListedColormap(["#f7fbff", "#c6dbef", "#6baed6", "#2171b5", "#08306b"]); norm = BoundaryNorm(bins, cmap.N)
kec.plot(ax=ax, column="wsm", cmap=cmap, norm=norm, edgecolor="white", linewidth=0.25, zorder=2)
noninti = kec[kec.delineasi != "Inti 1"]
noninti.plot(ax=ax, facecolor="none", edgecolor="#b30000", linewidth=0.6, hatch="///", zorder=3)
outline(ax)
labs = [f"{fmt(bins[i])}–{fmt(bins[i+1])}" for i in range(len(bins) - 1)]
ax.legend(handles=[Patch(facecolor=cmap(i), edgecolor="#888", label=labs[i]) for i in range(len(labs))] +
          [Patch(facecolor="none", edgecolor="#b30000", hatch="////", label="Bukan inti WSM (periferi/bukan WSM)"), Patch(facecolor="#c9c9c9", label="DKI Jakarta")],
          title="% komuter ke Kawasan Inti 1", loc="lower left", bbox_to_anchor=(0.0, 0.07), fontsize=7, title_fontsize=7.5, framealpha=0.9)
furniture(ax, "Data: BPS, WSM 2024, Lampiran 13 (MPD Agustus 2024). Batas: COD-AB HDX."); inset(fig); save(fig, "bab4_komuter_ke_inti_kecamatan")

# ---------------- G4.8 mass-based centres ----------------
fig, ax = newfig(); base(ax, dki_grey=True)
cat = np.where(kec.pusat_pend_p75 & kec.pusat_vres_p75, "Penduduk dan volume hunian",
      np.where(kec.pusat_pend_p75, "Penduduk saja", np.where(kec.pusat_vres_p75, "Volume hunian saja", "Tidak ditandai")))
kec["cat"] = cat
cols = {"Penduduk dan volume hunian": "#54278f", "Penduduk saja": "#9e9ac8", "Volume hunian saja": "#dadaeb", "Tidak ditandai": "#ffffff"}
for k, c in cols.items():
    s = kec[kec.cat == k]
    if len(s): s.plot(ax=ax, color=c, edgecolor="#999999", linewidth=0.25, zorder=2)
outline(ax)
ax.legend(handles=[Patch(facecolor=c, edgecolor="#888", label=f"{k} ({int((kec.cat == k).sum())})") for k, c in cols.items()] + [Patch(facecolor="#c9c9c9", label="DKI Jakarta")],
          title="Kuartil teratas (P75)", loc="lower left", bbox_to_anchor=(0.0, 0.07), fontsize=7, title_fontsize=7.5, framealpha=0.9)
furniture(ax, "Penduduk: BPS, WSM 2024, Lampiran 3. Volume hunian: GHSL R2023A (epoch 2020). Batas: COD-AB HDX."); inset(fig); save(fig, "bab4_pusat_berdasarkan_massa")

# ---------------- G4.7 industrial estates and new towns ----------------
ki = gpd.read_file(f"{S}/ki/Data Dukung Kawasan Industri - 125 KI/Data_Kawasan_Industri_125KI.shp").to_crs(UTM)
ki = ki[ki.intersects(box(EXT[0], EXT[2], EXT[1], EXT[3]))]
nt = json.load(open(f"{S}/osm/newtowns.json"))
fig, ax = newfig(); base(ax)
jabo.plot(ax=ax, color="#fafafa", edgecolor="#bbbbbb", linewidth=0.4, zorder=1); outline(ax)
ki.plot(ax=ax, color="#d7301f", edgecolor="#7f0000", linewidth=0.3, zorder=4)
lbl = {"Bumi Serpong Damai, Tangerang Selatan": "BSD", "Lippo Karawaci, Tangerang": "Lippo Karawaci", "Lippo Cikarang, Bekasi": "Lippo Cikarang",
       "Kota Jababeka, Cikarang, Bekasi": "Kota Jababeka", "Sentul City, Bogor": "Sentul City", "Summarecon Bekasi, Bekasi": "Summarecon Bekasi",
       "Alam Sutera, Tangerang Selatan": "Alam Sutera", "Kota Wisata, Bogor": "Kota Wisata"}
pts = gpd.GeoDataFrame({"n": [lbl[k] for k in nt]}, geometry=[Point(float(v["lon"]), float(v["lat"])) for v in nt.values()], crs=4326).to_crs(UTM)
pts.plot(ax=ax, marker="^", color="#08519c", markersize=28, edgecolor="white", linewidth=0.4, zorder=6)
for _, r in pts.iterrows():
    dx, dy = {"Lippo Karawaci": (-1500, 1800), "Alam Sutera": (1200, -2600), "Kota Wisata": (-1200, -2800)}.get(r.n, (1200, 900))
    ax.text(r.geometry.x + dx, r.geometry.y + dy, r.n, ha="right" if dx < 0 else "left", fontsize=6.8, color="#08306b", zorder=7, bbox=dict(facecolor="white", alpha=0.6, edgecolor="none", pad=0.4))
ax.legend(handles=[Patch(facecolor="#d7301f", edgecolor="#7f0000", label="Kawasan industri formal (poligon; termasuk di kabupaten tetangga)"),
                   Line2D([0], [0], marker="^", color="w", markerfacecolor="#08519c", markersize=8, label="Kota baru skala besar (titik indikatif)")],
          loc="lower left", bbox_to_anchor=(0.0, 0.07), fontsize=7, framealpha=0.9)
furniture(ax, "Kawasan industri: Kemenperin 2025. Kota baru: geocoding Nominatim OSM, 3 Okt 2026. Batas: COD-AB HDX."); inset(fig); save(fig, "bab4_kawasan_industri")

# ---------------- G4.6 existing network ----------------
net = json.load(open(f"{S}/osm/net.json"))
rows = []
for e in net["elements"]:
    g = e.get("geometry")
    if not g or len(g) < 2: continue
    t = e["tags"]; k = "Jalan tol" if t.get("highway") == "motorway" else ("MRT/LRT" if t.get("railway") in ("subway", "light_rail") else "Rel KRL/kereta")
    rows.append(dict(k=k, geometry=LineString([(p["lon"], p["lat"]) for p in g])))
ng = gpd.GeoDataFrame(rows, crs=4326).to_crs(UTM)
fig, ax = newfig(); base(ax)
jabo.plot(ax=ax, color="#fafafa", edgecolor="#bbbbbb", linewidth=0.4, zorder=1); outline(ax)
sty = {"Jalan tol": dict(color="#e6550d", linewidth=1.1), "Rel KRL/kereta": dict(color="#252525", linewidth=0.9), "MRT/LRT": dict(color="#3182bd", linewidth=1.3)}
for k, s in sty.items(): ng[ng.k == k].plot(ax=ax, zorder=4, **s)
ax.legend(handles=[Line2D([0], [0], label=k, **s) for k, s in sty.items()], loc="lower left", bbox_to_anchor=(0.0, 0.07), fontsize=7, framealpha=0.9)
furniture(ax, f"Jaringan: © kontributor OpenStreetMap (ODbL), Overpass {net['osm3s']['timestamp_osm_base'][:10]}. Batas: COD-AB HDX."); inset(fig); save(fig, "bab4_jaringan_eksisting")

# ---------------- G4.3 OD flows 2023 ----------------
od = json.load(open(f"{S}/out/od2023.json"))   # {(o,d): flow} with DKI aggregated
nodes = {}
for _, r in jabo.iterrows():
    key = "DKI Jakarta" if r["nama"].startswith("Kota Jakarta") else r["nama"]
    nodes.setdefault(key, []).append(r.geometry)
cent = {k: gpd.GeoSeries(v, crs=UTM).union_all().representative_point() for k, v in nodes.items()}
fig, ax = newfig(); base(ax)
jabo.plot(ax=ax, color="#fafafa", edgecolor="#bbbbbb", linewidth=0.4, zorder=1); outline(ax)
flows = sorted([(o, d, f) for (o, d, f) in od if f >= 20000], key=lambda x: x[2])
for o, d, f in flows:
    a, b = cent[o], cent[d]
    col = "#cb181d" if d == "DKI Jakarta" else ("#2171b5" if o != "DKI Jakarta" else "#6a51a3")
    # curved arrow so that the two directions do not overlap
    ax.annotate("", xy=(b.x, b.y), xytext=(a.x, a.y), zorder=4,
                arrowprops=dict(arrowstyle="-|>", color=col, lw=0.35 + f / 30000, alpha=0.8, connectionstyle="arc3,rad=0.18", shrinkA=6, shrinkB=6, mutation_scale=8))
for k, p in cent.items():
    ax.plot(p.x, p.y, "o", color="black", markersize=3, zorder=6)
    ax.text(p.x, p.y - 2500, k.replace("Kabupaten", "Kab."), fontsize=6.8, ha="center", va="top", zorder=7, bbox=dict(facecolor="white", alpha=0.65, edgecolor="none", pad=0.4))
ax.legend(handles=[Line2D([0], [0], color="#cb181d", lw=2, label="Menuju DKI Jakarta"), Line2D([0], [0], color="#2171b5", lw=2, label="Antarpinggiran"),
                   Line2D([0], [0], color="#6a51a3", lw=2, label="Dari DKI Jakarta"),
                   Line2D([0], [0], color="#555", lw=0.35 + 20000 / 30000, label="20.000 orang"), Line2D([0], [0], color="#555", lw=0.35 + 200000 / 30000, label="200.000 orang")],
          title="Arus komuter ≥20.000 orang", loc="lower left", bbox_to_anchor=(0.0, 0.07), fontsize=7, title_fontsize=7.5, framealpha=0.9)
furniture(ax, "Data: BPS, Statistik Komuter Jabodetabek 2023, Tabel 2. DKI digabung menjadi satu simpul."); inset(fig); save(fig, "bab4_komuter_od_2023")

# ---------------- G4.5 GHSL total and NRES ----------------
fig, axes = plt.subplots(1, 2, figsize=(6.3, 3.9)); fig.subplots_adjust(0, 0.22, 1, 0.93, wspace=0.03)
for ax, f, ttl in zip(axes, ["GHS_BUILT_V_E2020_GLOBE_R2023A_4326_3ss_V1_0_R10_C29.tif", "GHS_BUILT_V_NRES_E2020_GLOBE_R2023A_4326_3ss_V1_0_R10_C29.tif"],
                      ["(a) Volume terbangun total", "(b) Volume terbangun nonhunian"]):
    src = rasterio.open(f"{S}/ghsl/{f}")
    bb = gpd.GeoSeries([box(EXT[0], EXT[2], EXT[1], EXT[3])], crs=UTM).to_crs(4326).total_bounds
    win = rasterio.windows.from_bounds(*bb, transform=src.transform)
    arr = src.read(1, window=win).astype("float32"); tr = src.window_transform(win)
    dst_tr, w, h = calculate_default_transform(4326, UTM, arr.shape[1], arr.shape[0], *rasterio.windows.bounds(win, src.transform), resolution=90)
    out = np.zeros((h, w), dtype="float32")
    reproject(arr, out, src_transform=tr, src_crs=4326, dst_transform=dst_tr, dst_crs=UTM, resampling=Resampling.bilinear)
    out[out <= 0] = np.nan
    ex = (dst_tr.c, dst_tr.c + w * dst_tr.a, dst_tr.f + h * dst_tr.e, dst_tr.f)
    base(ax, neighbours=False)
    im = ax.imshow(out, extent=ex, cmap="magma_r", norm=LogNorm(vmin=100, vmax=200000), zorder=2, interpolation="nearest")
    outline(ax, lw=0.5); ax.set_title(ttl, fontsize=9)
cax = fig.add_axes([0.25, 0.14, 0.5, 0.025]); cb = fig.colorbar(im, cax=cax, orientation="horizontal")
cb.set_label("m³ per sel 3 detik busur (skala log)", fontsize=7.5); cb.ax.tick_params(labelsize=7)
cb.ax.set_xticklabels([fmt(float(t.get_text().replace("$\\mathdefault{10^{", "1e").replace("}}$", "")) if "mathdefault" in t.get_text() else 0) for t in cb.ax.get_xticklabels()]) if False else None
fig.text(0.5, 0.0, "Data: GHSL GHS-BUILT-V R2023A, epoch 2020 (JRC, CC BY 4.0). Batas: COD-AB HDX. Proyeksi UTM 48S.", ha="center", fontsize=6.3)
save(fig, "bab4_terbangun_nonhunian")
