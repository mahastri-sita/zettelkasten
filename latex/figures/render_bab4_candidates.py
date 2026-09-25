"""Rebuild the candidate audit map on the same base as Bab 4's first map."""

from pathlib import Path
import xml.etree.ElementTree as ET


HERE = Path(__file__).resolve().parent
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


def tag(name):
    return f"{{{NS}}}{name}"


def add(root, name, **attributes):
    return ET.SubElement(root, tag(name), {key.replace("_", "-"): str(value) for key, value in attributes.items()})


def label(root, x, y, value, size=9.5, weight="400"):
    element = add(root, "text", x=x, y=y, font_family="Arial", font_size=size,
                  font_weight=weight, fill="#20262b")
    element.text = value
    return element


root = ET.parse(HERE / "bab4_admin.svg").getroot()
place_names = {
    "Kab. Tangerang", "Kota Tangerang", "Tangerang Selatan", "DKI Jakarta",
    "Depok", "Kota Bekasi", "Kab. Bekasi", "Kota Bogor", "Kab. Bogor",
}

# Retain the administrative geometry, grid, north arrow, and scale. Replace
# province labels and legend with audit locations; the map must not imply that
# these points or dashed lines are classified centers or observed flows.
legend_started = False
for element in list(root):
    if element.tag == tag("rect") and element.get("x") == "975":
        legend_started = True
    if legend_started and not (element.tag == tag("line") and element.get("y1") == "700"):
        root.remove(element)
        continue
    if legend_started:
        legend_started = False
    if element.tag == tag("text") and element.text in place_names:
        root.remove(element)
    elif element.tag == tag("text") and (element.text or "").startswith("Sumber geometri:"):
        element.text = ("Sumber geometri: geoBoundaries gbOpen Indonesia ADM2, build 2023 "
                        "(batas 2020). Titik dan garis adalah label audit, bukan hasil klasifikasi atau arus aktual.")

points = {
    "I": (524.5, 246.2, "Jakarta"),
    "1": (409.9, 308.4, "Tangerang–Tangsel"),
    "2": (518.9, 379.7, "Depok"),
    "3": (503.3, 498.6, "Bogor"),
    "4": (659.1, 284.6, "Bekasi"),
    "5": (791.5, 332.2, "Cikarang"),
}

for source, target in [("I", "1"), ("I", "2"), ("I", "4"), ("2", "3"), ("4", "5")]:
    x1, y1, _ = points[source]
    x2, y2, _ = points[target]
    add(root, "line", x1=x1, y1=y1, x2=x2, y2=y2, stroke="#39434b",
        stroke_width="1.5", stroke_dasharray="6,5", opacity="0.72")

for number, (x, y, _) in points.items():
    add(root, "circle", cx=x, cy=y, r="11", fill="#ffffff", stroke="#20262b",
        stroke_width="1.8")
    element = label(root, x, y + 3.3, number, size=9.5, weight="700")
    element.set("text-anchor", "middle")

add(root, "rect", x="975", y="62", width="126", height="186", fill="#ffffff",
    stroke="#343a40", stroke_width="0.8")
label(root, 988, 82, "Lokasi audit", size=10.5, weight="600")
for index, (number, (_, _, name)) in enumerate(points.items()):
    y = 102 + index * 20
    label(root, 988, y, number, size=9.4, weight="700")
    label(root, 1003, y, name, size=9.1)
add(root, "line", x1="988", y1="229", x2="1007", y2="229", stroke="#39434b",
    stroke_width="1.5", stroke_dasharray="6,5")
label(root, 1013, 232, "Relasi audit", size=8.7)

output = HERE / "bab4_candidates.svg"
ET.indent(root, space="  ")
ET.ElementTree(root).write(output, encoding="unicode", xml_declaration=True)
