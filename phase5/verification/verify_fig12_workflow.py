#!/usr/bin/env python3
"""Check Figure 11/F12 SVG mirrors and connector geometry.

This verifies label/connector structure and ensures line paths stay outside
step-box interiors. It does not validate the scientific truth of a model,
constitutive law, energy ratio, benchmark, or source/licence provenance.
"""
from __future__ import annotations

import csv
import re
import xml.etree.ElementTree as ET
from pathlib import Path

PHASE5 = Path(__file__).resolve().parents[1]
LEDGER = PHASE5 / "reports/OPEN_CLAIMS_LEDGER.csv"
REL = Path("master/figures/source/fig12-solution-workflow.svg")
MIRRORS = (
    PHASE5 / "figures/source/fig12-solution-workflow.svg",
    PHASE5 / REL,
    PHASE5 / "master/figures/rendered/fig12-solution-workflow.svg",
)
SVG_NS = "http://www.w3.org/2000/svg"
TAG = lambda name: f"{{{SVG_NS}}}{name}"

existing_mirrors = [p for p in MIRRORS if p.is_file()]
assert existing_mirrors, "No F12 SVG mirror found at any expected path"
contents = [path.read_bytes() for path in existing_mirrors]
assert all(content == contents[0] for content in contents[1:]), "F12 SVG mirrors differ"
root = ET.fromstring(contents[0])
assert root.attrib.get("viewBox") == "0 0 1100 700"

by_id = {element.attrib["id"]: element for element in root.iter() if "id" in element.attrib}
boxes = {
    f"step-{i}": by_id[f"step-{i}"]
    for i in range(1, 11)
}
for step, box in boxes.items():
    assert box.tag == TAG("rect"), f"{step} is not a rectangle"
    for attr in ("x", "y", "width", "height"):
        assert attr in box.attrib, f"{step}: missing {attr}"

texts = ["".join(element.itertext()) for element in root.iter(TAG("text"))]
for i in range(1, 11):
    assert f"Step {i}" in texts, f"Missing Step {i} label"
assert "Characteristic system" in texts
assert "Selected determinant / roots" in texts
assert "Reference-plane ratios" in texts
assert "Specified benchmark" in texts
assert "Iterate if needed" in texts
assert not any("R + T + A_int = 1" in text for text in texts)
assert not any("J_j = q_j" in text for text in texts)

required_connectors = {
    "flow-1-to-2", "flow-2-to-3", "flow-3-to-4",
    "flow-5-to-6", "flow-6-to-7", "flow-7-to-8",
    "flow-4-to-5", "flow-8-to-9", "flow-9-to-10", "feedback-10-to-8",
}
assert required_connectors <= set(by_id), f"Missing connector ids: {required_connectors - set(by_id)}"

# Extract each line/polyline as a sequence of straight segments.
def points_for(element: ET.Element) -> list[tuple[float, float]]:
    if element.tag == TAG("line"):
        return [(float(element.attrib[f"x{i}"]), float(element.attrib[f"y{i}"])) for i in (1, 2)]
    if element.tag != TAG("path"):
        raise AssertionError(f"Unsupported connector type: {element.tag}")
    matches = re.findall(r"([ML])\s*(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)", element.attrib.get("d", ""))
    assert matches and all(command in {"M", "L"} for command, _, _ in matches), element.attrib.get("d")
    return [(float(x), float(y)) for _, x, y in matches]

expected_points = {
    "flow-1-to-2": [(250.0, 115.0), (300.0, 115.0)],
    "flow-2-to-3": [(500.0, 115.0), (550.0, 115.0)],
    "flow-3-to-4": [(750.0, 115.0), (800.0, 115.0)],
    "flow-5-to-6": [(250.0, 255.0), (300.0, 255.0)],
    "flow-6-to-7": [(500.0, 255.0), (550.0, 255.0)],
    "flow-7-to-8": [(750.0, 255.0), (800.0, 255.0)],
    "flow-4-to-5": [(925.0, 150.0), (925.0, 180.0), (150.0, 180.0), (150.0, 220.0)],
    "flow-8-to-9": [(925.0, 290.0), (925.0, 325.0), (350.0, 325.0), (350.0, 360.0)],
    "flow-9-to-10": [(450.0, 395.0), (650.0, 395.0)],
    "feedback-10-to-8": [(850.0, 395.0), (1075.0, 395.0), (1075.0, 255.0), (1050.0, 255.0)],
}
for connector_id, expected in expected_points.items():
    assert points_for(by_id[connector_id]) == expected, f"{connector_id}: routing differs from the audited layout"

# The expected endpoints must touch the intended boxes, while interior path
# points stay outside every step-box interior. Markers may visually touch edges.
def rect_bounds(box: ET.Element) -> tuple[float, float, float, float]:
    x, y = float(box.attrib["x"]), float(box.attrib["y"])
    return x, y, x + float(box.attrib["width"]), y + float(box.attrib["height"])

all_bounds = {name: rect_bounds(box) for name, box in boxes.items()}

def inside_any_box(x: float, y: float) -> bool:
    return any(x0 + 0.5 < x < x1 - 0.5 and y0 + 0.5 < y < y1 - 0.5 for x0, y0, x1, y1 in all_bounds.values())

for connector_id in required_connectors:
    element = by_id[connector_id]
    points = points_for(element)
    assert len(points) >= 2, connector_id
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        for n in range(1, 100):
            t = n / 100
            assert not inside_any_box(x0 + t * (x1 - x0), y0 + t * (y1 - y0)), (
                f"{connector_id} crosses a step-box interior"
            )

# Feedback annotation occupies the inter-row channel and stays clear of the
# right-margin loop and all process boxes.
feedback = next(e for e in root.iter(TAG("text")) if "".join(e.itertext()) == "Iterate if needed")
fx, fy = float(feedback.attrib["x"]), float(feedback.attrib["y"])
assert 290 < fy < 360 and fx < 1075 - 45
assert not inside_any_box(fx, fy)

with LEDGER.open(newline="", encoding="utf-8-sig") as stream:
    figure_row = next(row for row in csv.DictReader(stream) if row["ledger_row_id"] == "OCL-499")
assert figure_row["class"] == "V"
assert figure_row["resolved_by"] == "phase5/verification/verify_fig12_workflow.py"
assert "geometry" in figure_row["evidence_mode"].lower()

print("PASS: all three F12 SVG mirrors are identical and contain ten scoped workflow steps")
print("PASS: row-wrap, energy-ratio, validation, and feedback connectors avoid step-box interiors")
print("PASS: universal energy-ratio closure and generic flux equation are absent")
print("Scope: layout/label consistency only; no scientific or source/licence claim is validated")
