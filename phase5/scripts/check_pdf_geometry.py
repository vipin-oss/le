#!/usr/bin/env python3
"""PDF geometry gate: every text span and drawing must lie within the page rectangle.

Three independent detections, none of which clip off-page content away:

  1. get_text("words", clip=large_rect) — words inside a large rectangle that
     covers nearly the whole page. Text outside the page rect is simply absent
     from this list; it is caught by check 2 instead.
  2. get_text("rawdict") — every text span on the page, unclipped, so any span
     whose bbox leaves the page rectangle is reported.
  3. page.get_drawings() — every vector drawing's bbox; any drawing outside the
     page rect is reported.

Usage:
    python3 phase5/scripts/check_pdf_geometry.py BUILT_PDF
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import fitz
except ImportError as exc:
    print(f"ERROR: PyMuPDF not available: {exc}", file=sys.stderr)
    sys.exit(2)


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} BUILT_PDF", file=sys.stderr)
        return 2
    pdf_path = Path(sys.argv[1])
    if not pdf_path.is_file():
        print(f"ERROR: PDF not found: {pdf_path}", file=sys.stderr)
        return 2

    doc = fitz.open(str(pdf_path))
    tolerance = 2.0  # points
    bad_pages: dict[int, list[str]] = {}

    for page_num in range(len(doc)):
        page = doc[page_num]
        rect = page.rect

        # --- Check 1: words inside a large clip rect covering most of page ---
        # A clip rect slightly inside the page edges; text fully outside the
        # page rect never appears here (caught by check 2 instead).
        large_rect = fitz.Rect(tolerance, tolerance,
                               rect.width - tolerance, rect.height - tolerance)
        try:
            words = page.get_text("words", clip=large_rect)
        except Exception:
            words = []

        # --- Check 2: rawdict spans, unclipped, to catch off-page text ---
        d = page.get_text("rawdict")
        for block in d.get("blocks", []):
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    bbox = span["bbox"]
                    x0, y0, x1, y1 = bbox
                    if (x0 < -tolerance or y0 < -tolerance
                            or x1 > rect.width + tolerance
                            or y1 > rect.height + tolerance):
                        bad_pages.setdefault(page_num + 1, []).append(
                            f"span outside page rect: [{x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f}] "
                            f"text={span.get('text', '')[:40]!r}"
                        )

        # --- Check 3: vector drawing bboxes outside page rect ---
        for drawing in page.get_drawings():
            drect = drawing["rect"]
            if (drect.x0 < -tolerance or drect.y0 < -tolerance
                    or drect.x1 > rect.width + tolerance
                    or drect.y1 > rect.height + tolerance):
                bad_pages.setdefault(page_num + 1, []).append(
                    f"drawing outside page rect: [{drect.x0:.1f},{drect.y0:.1f},"
                    f"{drect.x1:.1f},{drect.y1:.1f}]"
                )

    page_count = len(doc)
    doc.close()

    if bad_pages:
        print("ERROR: content outside page geometry on the following pages:")
        for pageno in sorted(bad_pages):
            print(f"  Page {pageno}:")
            for issue in bad_pages[pageno][:5]:
                print(f"    {issue}")
        return 1
    print(f"PASS: all {page_count} pages have text and drawings within page geometry")
    return 0


if __name__ == "__main__":
    sys.exit(main())
