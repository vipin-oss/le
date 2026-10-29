#!/usr/bin/env python3
"""PDF geometry gate: every text block must lie within the page rectangle.

Uses PyMuPDF to inspect each page of the built PDF. Fails if any text block
extends beyond the page rectangle (small tolerance) or below the bottom margin.

Usage:
    python3 phase5/scripts/check_pdf_geometry.py build/main.pdf
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
        # Bottom margin: content should not extend below page height - tolerance
        bottom_limit = rect.height - tolerance
        blocks = page.get_text("blocks")
        for block in blocks:
            x0, y0, x1, y1, text = block[0], block[1], block[2], block[3], block[4]
            # Check within page rectangle
            if x0 < -tolerance or y0 < -tolerance or x1 > rect.width + tolerance or y1 > rect.height + tolerance:
                bad_pages.setdefault(page_num + 1, []).append(
                    f"block outside page rect: [{x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f}] text={text[:40]!r}"
                )
            # Check below bottom margin
            if y1 > bottom_limit:
                bad_pages.setdefault(page_num + 1, []).append(
                    f"block below bottom margin: y1={y1:.1f} > {bottom_limit:.1f} text={text[:40]!r}"
                )

    page_count = len(doc)
    doc.close()

    if bad_pages:
        print("ERROR: text blocks outside page geometry on the following pages:")
        for pageno in sorted(bad_pages):
            print(f"  Page {pageno}:")
            for issue in bad_pages[pageno][:5]:
                print(f"    {issue}")
        return 1
    print(f"PASS: all {page_count} pages have text blocks within page geometry")
    return 0


if __name__ == "__main__":
    sys.exit(main())
