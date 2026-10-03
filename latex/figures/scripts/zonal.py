"""Zonal GHSL volumes per kecamatan (Jabodetabek) and frozen mass thresholds.

Inputs: HDX COD-AB admin3 (kecamatan), GHSL BUILT-V total & NRES epoch 2020
(3 arcsec, m3 per cell), Kemenperin industrial-estate polygons, WSM 2024
Lampiran 3 / 13 tables parsed from the vault source note.
"""
import re, sys, json
import numpy as np, pandas as pd, geopandas as gpd
import rasterio
from rasterio.mask import mask as rmask

S = sys.argv[1]
VAULT = "/Users/mac/Documents/Mac/[2] Obsidian Vault/zettelkasten"
adm3 = gpd.read_file(sys.argv[2])  # pre-extracted Jabodetabek admin3 (EPSG:4326)

# --- WSM tables from source note ---------------------------------------
note = open(f"{VAULT}/source/official-document/BPS - 2026 - Wilayah Statistik Metropolitan Indonesia 2024.md").read()
l13 = note.split("### Lampiran 13")[1].split("### Lampiran 3")[0]
l3 = note.split("### Lampiran 3")[1].split("## Provenance")[0]
num = lambda s: float(s.replace(".", "").replace(",", "."))
w13 = pd.DataFrame([dict(kode=m[0], nama=m[1].strip(), kabkota=m[2].strip(), wsm=num(m[3]), delineasi=m[4].strip())
                    for m in re.findall(r"^\| (3[26]\d{5}) \| ([^|]+) \| ([^|]+) \| ([\d,]+) \| ([^|]+) \|", l13, re.M)])
w3 = pd.DataFrame([dict(kode=m[0], pend=num(m[2]), luas=num(m[3]), kepadatan=num(m[4]))
                   for m in re.findall(r"^\| (3[26]\d{5}) \| ([^|]+) \| ([\d.]+) \| ([\d,]+) \| ([\d.,]+) \|", l3, re.M)])
wsm = w13.merge(w3, on="kode")
assert len(wsm) == 141, len(wsm)

# --- match boundaries to BPS 2024 codes ----------------------------------
adm3["kode"] = adm3["adm3_pcode"].str.replace("ID", "", regex=False).str.replace(r"\D", "", regex=True)
m = wsm.merge(adm3[["kode", "adm3_name", "geometry"]], on="kode", how="left")
unmatched = m[m.geometry.isna()]
print("unmatched codes:", len(unmatched), unmatched[["kode", "nama"]].to_dict("records"))
gdf = gpd.GeoDataFrame(m.dropna(subset=["geometry"]), geometry="geometry", crs=adm3.crs)

# --- industrial estates (Kemenperin) -------------------------------------
ki = gpd.read_file(f"{S}/ki/Data Dukung Kawasan Industri - 125 KI/Data_Kawasan_Industri_125KI.shp").to_crs(4326)
ki = ki[ki["Kab_Kota"].str.contains("Bekasi|Bogor|Tangerang|Depok|Jakarta", na=False) & ~ki["Kab_Kota"].str.contains("Sukabumi", na=False)]
ki_union = ki.union_all()

# --- zonal sums ----------------------------------------------------------
tot = rasterio.open(f"{S}/ghsl/GHS_BUILT_V_E2020_GLOBE_R2023A_4326_3ss_V1_0_R10_C29.tif")
nres = rasterio.open(f"{S}/ghsl/GHS_BUILT_V_NRES_E2020_GLOBE_R2023A_4326_3ss_V1_0_R10_C29.tif")

def zsum(src, geom):
    arr, _ = rmask(src, [geom], crop=True, filled=True, nodata=0, all_touched=False)
    return float(arr.astype("float64").sum())

rows = []
for _, r in gdf.iterrows():
    g = r.geometry
    v_tot, v_nres = zsum(tot, g), zsum(nres, g)
    g_out = g.difference(ki_union) if g.intersects(ki_union) else g
    v_nres_out = zsum(nres, g_out) if not g_out.is_empty else 0.0
    ki_area = gpd.GeoSeries([g.intersection(ki_union)], crs=4326).to_crs(32748).area.iloc[0] / 1e4
    near = g.buffer(0.0).touches(ki_union) or g.intersects(ki_union)
    rows.append(dict(kode=r.kode, v_total=v_tot, v_nres=v_nres, v_res=v_tot - v_nres,
                     v_nres_luar_ki=v_nres_out, ki_ha=ki_area, ki_dalam=bool(g.intersects(ki_union) and ki_area > 0.5)))
z = pd.DataFrame(rows)
gdf = gdf.merge(z, on="kode")

# KI moderator flag: contains or borders an estate polygon
gdf_m = gdf.to_crs(32748)
ki_m = gpd.GeoSeries([ki_union], crs=4326).to_crs(32748).iloc[0]
gdf["ki_dekat"] = gdf_m.geometry.buffer(1).intersects(ki_m).values

def pct(x, q): return float(np.percentile(np.asarray(x, dtype=float), q))
thr = {q: dict(pend=pct(gdf.pend, q), v_res=pct(gdf.v_res, q)) for q in (66, 75, 80)}
for q in (66, 75, 80):
    gdf[f"pusat_p{q}"] = (gdf.pend >= thr[q]["pend"]) | (gdf.v_res >= thr[q]["v_res"])
gdf["pusat_pend_p75"] = gdf.pend >= thr[75]["pend"]
gdf["pusat_vres_p75"] = gdf.v_res >= thr[75]["v_res"]

gdf.to_file(f"{S}/out/kecamatan_141.gpkg", driver="GPKG")
gdf.drop(columns="geometry").to_csv(f"{S}/out/kecamatan_141.csv", index=False)
json.dump(thr, open(f"{S}/out/thresholds.json", "w"), indent=1)
print("n", len(gdf)); print(json.dumps(thr, indent=1))
print("pusat P75:", int(gdf.pusat_p75.sum()), "| pend only", int(gdf.pusat_pend_p75.sum()), "| vres only", int(gdf.pusat_vres_p75.sum()),
      "| both", int((gdf.pusat_pend_p75 & gdf.pusat_vres_p75).sum()))
print("ki_dekat", int(gdf.ki_dekat.sum()), "ki_dalam", int(gdf.ki_dalam.sum()))
print("totals (Mm3): total %.1f nres %.1f nres_luar_ki %.1f" % (gdf.v_total.sum()/1e6, gdf.v_nres.sum()/1e6, gdf.v_nres_luar_ki.sum()/1e6))
print(gdf.groupby("kabkota")[["v_total","v_nres","v_nres_luar_ki","pusat_p75"]].sum().round(0))
