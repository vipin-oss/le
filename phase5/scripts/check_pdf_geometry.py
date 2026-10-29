#!/usr/bin/env python3
"""PDF geometry gate: every text span must lie within the page rectangle.

Uses PyMuPDF rawdict extraction (no clipping) to inspect each page of the
built PDF. Fails if any text span's bbox leaves the page rectangle or the
bottom margin. Unlike get_text("blocks"), rawdict does not clip spans to
the mediabox, so text drawn outside the page is still detected.

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
    bottom_limit = None
    bad_pages: dict[int, list[str]] = {}

    for page_num in range(len(doc)):
        page = doc[page_num]
        rect = page.rect
        bottom_limit = rect.height - tolerance

        # Use rawdict (no clipping) to catch spans outside the mediabox.
        d = page.get_text("rawdict")
        for block in d.get("blocks", []):
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    bbox = span["bbox"]
                    x0, y0, x1, y1 = bbox
                    # Check within page rectangle
                    if (x0 < -tolerance or y0 < -tolerance
                            or x1 > rect.width + tolerance
                            or y1 > rect.height + tolerance):
                        bad_pages.setdefault(page_num + 1, []).append(
                            f"span outside page rect: [{x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f}] "
                            f"text={span.get('text', '')[:40]!r}"
                        )
                    # Check below bottom margin
                    if y1 > bottom_limit:
                        bad_pages.setdefault(page_num + 1, []).append(
                            f"span below bottom margin: y1={y1:.1f} > {bottom_limit:.1f} "
                            f"text={span.get('text', '')[:40]!r}"
                        )

    page_count = len(doc)
    doc.close()

    if bad_pages:
        print("ERROR: text spans outside page geometry on the following pages:")
        for pageno in sorted(bad_pages):
            print(f"  Page {pageno}:")
            for issue in bad_pages[pageno][:5]:
                print(f"    {issue}")
        return 1
    print(f"PASS: all {page_count} pages have text spans within page geometry")
    return 0


if __name__ == "__main__":
    sys.exit(main())
