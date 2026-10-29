#!/usr/bin/env python3
"""PDF geometry gate: every text span and drawing must lie within the page rectangle.

Detections:
  1. get_text("words", clip=large_rect) — words inside a clip rect much larger
     than the page (e.g. 2x page size in each direction). Text drawn outside
     the page rect but inside the large clip is still returned, so off-page
     text is caught here.
  2. page.get_drawings() — every vector drawing's bbox; any drawing outside the
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


def annotate(title: str, finding: str) -> None:
    """Print a GitHub Actions error annotation."""
    print(f"::error title={title}::{finding}")


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

        # --- Check 1: words inside a clip rect MUCH LARGER than the page ---
        # Use a clip rect that extends well beyond the page edges so that
        # text drawn outside the page is still returned and can be detected.
        margin = 1000.0  # points beyond each page edge
        large_rect = fitz.Rect(
            -margin, -margin, rect.width + margin, rect.height + margin
        )
        try:
            words = page.get_text("words", clip=large_rect)
        except Exception:
            words = []

        for w in words:
            x0, y0, x1, y1 = w[:4]
            if (x0 < -tolerance or y0 < -tolerance
                    or x1 > rect.width + tolerance
                    or y1 > rect.height + tolerance):
                bad_pages.setdefault(page_num + 1, []).append(
                    f"word outside page rect: [{x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f}] "
                    f"text={w[4][:40]!r}"
                )

        # --- Check 2: vector drawing bboxes outside page rect ---
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

    # Print annotations (cap at ~50 lines)
    total_issues = sum(len(v) for v in bad_pages.values())
    count = 0
    for pageno in sorted(bad_pages):
        for issue in bad_pages[pageno]:
            if count >= 50:
                break
            annotate(
                "PDF geometry check (text blocks within page rectangle)",
                f"Page {pageno}: {issue}",
            )
            count += 1

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
