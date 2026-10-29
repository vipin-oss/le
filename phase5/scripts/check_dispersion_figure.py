#!/usr/bin/env python3
"""Self-check for the generated dispersion figure (fig_dispersion.svg).

Parses the SVG output of phase5/tools/plot_dispersion.py and verifies:

  1. Tick labels are evenly spaced in coordinates (the y-pixel spacing of
     consecutive tick marks is constant).
  2. Tick label values match their coordinates through the same linear
     mapping used to draw them (no position/label drift).
  3. The classical curve (c/c0 = 1) is flat at value 1.0.
  4. The gradient curve maximum equals sqrt(1 + (ell * XMAX)^2) ≈ 2.06
     within 2 percent.

Usage:
    python3 phase5/scripts/check_dispersion_figure.py SVG_FILE
"""
from __future__ import annotations

import math
import re
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} SVG_FILE", file=sys.stderr)
        return 2
    svg_path = Path(sys.argv[1])
    if not svg_path.is_file():
        print(f"ERROR: SVG not found: {svg_path}", file=sys.stderr)
        return 2
    svg = svg_path.read_text(errors="replace")

    errors: list[str] = []
    pts: list[tuple[float, float]] = []

    # --- Extract y tick marks ---
    tick_lines = re.findall(
        r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="\2"[^>]*/>',
        svg,
    )
    y_ticks = []
    for x1, y1, x2 in tick_lines:
        x1f, x2f, y1f = float(x1), float(x2), float(y1)
        if x2f > x1f and abs(x1f - 67.0) < 5.0:   # y-axis ticks at X0 - 5 = 67
            y_ticks.append(y1f)
    y_ticks.sort()

    if len(y_ticks) < 2:
        errors.append(f"too few y tick lines found: {len(y_ticks)}")
    else:
        # Check even spacing in coordinates
        spacings = [y_ticks[i+1] - y_ticks[i] for i in range(len(y_ticks)-1)]
        spacing_mean = sum(spacings) / len(spacings)
        for i, sp in enumerate(spacings):
            if abs(sp - spacing_mean) > 0.5:
                errors.append(
                    f"tick spacing not uniform at tick {i}: {sp:.2f} vs mean {spacing_mean:.2f}"
                )

        # Extract y tick label values
        label_vals = re.findall(
            r'<text[^>]*y="([\d.]+)"[^>]*font-size="10"[^>]*text-anchor="end">([\d.]+)</text>',
            svg,
        )
        # Match labels to tick lines by y coordinate
        label_map: dict[float, float] = {}
        for ly, val in label_vals:
            lyf = float(ly)
            nearest = min(y_ticks, key=lambda t: abs(t - lyf))
            if abs(nearest - lyf) < 5.0:
                label_map[nearest] = float(val)

        # Check that label value is a linear function of tick coordinate
        pts = sorted(label_map.items())
        if len(pts) >= 3:
            (c0, v0), (c1, v1) = pts[0], pts[-1]
            a = (v1 - v0) / (c1 - c0)
            b = v0 - a * c0
            for coord, val in pts:
                expected = a * coord + b
                if abs(val - expected) > 0.02:
                    errors.append(
                        f"tick label {val:.2f} at coord {coord:.1f} deviates "
                        f"from linear mapping {expected:.2f} (position/label drift)"
                    )
        else:
            errors.append("too few tick labels matched to ticks")

    # --- Extract curves: polyline points ---
    polylines = re.findall(r'<polyline points="([^"]+)"', svg)
    if len(polylines) != 3:
        errors.append(f"expected 3 polylines, found {len(polylines)}")
    else:
        def parse_points(pts_str: str) -> list[tuple[float, float]]:
            pts = []
            for pair in pts_str.split():
                x, y = pair.split(",")
                pts.append((float(x), float(y)))
            return pts

        classical = parse_points(polylines[0])
        gradient = parse_points(polylines[2])

        if y_ticks and len(pts) >= 3:
            (c0, v0), (c1, v1) = pts[0], pts[-1]
            a = (v1 - v0) / (c1 - c0)
            b = v0 - a * c0

            def svg_y_to_value(sy: float) -> float:
                return a * sy + b

            # Classical curve must be flat at c/c0 = 1.0
            classical_vals = [svg_y_to_value(p[1]) for p in classical]
            classical_max_dev = max(abs(v - 1.0) for v in classical_vals)
            if classical_max_dev > 0.02:
                errors.append(
                    f"classical curve deviates from 1.0 by {classical_max_dev:.3f}"
                )

            # Gradient curve maximum ≈ sqrt(1 + (0.45 * 4)^2) ≈ 2.059
            grad_vals = [svg_y_to_value(p[1]) for p in gradient]
            grad_max = max(grad_vals)
            grad_expected = math.sqrt(1.0 + (0.45 * 4.0) ** 2)
            grad_rel_dev = abs(grad_max - grad_expected) / grad_expected
            if grad_rel_dev > 0.02:
                errors.append(
                    f"gradient max {grad_max:.3f} deviates from expected "
                    f"{grad_expected:.3f} by {100*grad_rel_dev:.1f}% (> 2%)"
                )
        else:
            errors.append("cannot map curve y to values: no tick label mapping")

    if errors:
        print("FAIL: dispersion figure self-check failed:")
        for e in errors[:30]:
            print(f"  {e}")
        return 1
    print("PASS: dispersion figure self-check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
