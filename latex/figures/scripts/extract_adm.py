"""Extract Jabodetabek admin layers from HDX COD-AB GDB into small GPKGs."""
import sys, re
import geopandas as gpd, pyogrio
from shapely.geometry import box

S = sys.argv[1]
gdb = sys.argv[2]
layers = [l[0] for l in pyogrio.list_layers(gdb)]
print(layers)
def find(n):
    c = [l for l in layers if l.endswith(f"admin{n}")]
    return c[0]
L1, L2, L3 = find(1), find(2), find(3)
bb = box(105.9, -7.25, 107.75, -5.75)  # region incl. neighbours
a2 = gpd.read_file(gdb, layer=L2, bbox=bb.bounds)
a3 = gpd.read_file(gdb, layer=L3, bbox=bb.bounds)
a1 = gpd.read_file(gdb, layer=L1)
print(a2.columns.tolist()); print(a3.columns.tolist())
code = lambda s: re.sub(r"\D", "", str(s))
a2["k"] = a2["adm2_pcode"].map(code); a3["k2"] = a3["adm2_pcode"].map(code)
NAMES = {"3201": "Kabupaten Bogor", "3216": "Kabupaten Bekasi", "3271": "Kota Bogor", "3275": "Kota Bekasi", "3276": "Kota Depok",
         "3603": "Kabupaten Tangerang", "3671": "Kota Tangerang", "3674": "Kota Tangerang Selatan",
         "3171": "Kota Jakarta Selatan", "3172": "Kota Jakarta Timur", "3173": "Kota Jakarta Pusat", "3174": "Kota Jakarta Barat", "3175": "Kota Jakarta Utara"}
a2["nama"] = [NAMES.get(k, n) for k, n in zip(a2.k, a2["adm2_name"])]
a2 = a2[a2.k != "3101"]  # Kepulauan Seribu not drawn
a2[["k", "nama", "geometry"]].to_file(f"{S}/out/adm2_region.gpkg", driver="GPKG")
java = a1[a1["adm1_pcode"].map(code).isin(["31", "32", "33", "34", "35", "36"])]
java[["adm1_name", "geometry"]].to_file(f"{S}/out/adm1_java.gpkg", driver="GPKG")
bodeta = a3[a3.k2.isin(["3201", "3216", "3271", "3275", "3276", "3603", "3671", "3674"])]
bodeta.to_file(f"{S}/out/adm3_bodetabek.gpkg", driver="GPKG")
a3[a3.k2.isin(["3171", "3172", "3173", "3174", "3175"])].to_file(f"{S}/out/kecamatan_dki.gpkg", driver="GPKG")
print("adm2", len(a2), "bodetabek kec", len(bodeta), "dki kec", int(a3.k2.isin(["3171","3172","3173","3174","3175"]).sum()))
print(bodeta.groupby("k2").size())
