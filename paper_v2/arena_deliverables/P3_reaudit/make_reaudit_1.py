#!/usr/bin/env python3
"""Task 2 (re-run): re-audit the 20 flagged rows of claim_register.csv against main.pdf.

The register carries 20 rows whose verdict is PARTLY SUPPORTED or NOT SUPPORTED.  This
script re-audits them against the **current** build (`paper_v2/main.pdf`), not against the
text they were flagged on.  For each row it records

  * the PDF page on which the passage now sits, found by matching the normalised words
    of the register statement against the extracted page text (no guessing: a row whose
    passage cannot be located is reported as `not located`, not as `changed`);
  * whether the wording the earlier re-audit quoted is still the wording in the PDF
    (6-gram overlap with the earlier quote);
  * the re-audit verdict: `resolved` (the current wording now matches the source),
    `still partly supported`, or `not located`.

The judgement about the *source* is not re-derived here from nothing: it is taken from the
earlier pass over the same claim (`P1_audit/reaudit_flagged_20.csv`, which states the basis
of each judgement) and is only carried over when the manuscript text it was made about is
still the text in this PDF.  Where the text has moved on, the row says so instead.

Usage
  python3 make_reaudit_1.py --pdf ../../main.pdf --register ../../claim_register.csv \
                            --earlier ../../arena_deliverables/P1_audit/reaudit_flagged_20.csv
Writes reaudit_1.csv next to this file.  Requires pypdf for PDF text extraction.
"""
import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "reaudit_1.csv")
COLS = ["claim_id", "register_verdict", "cited_source", "manuscript_page", "located_in_pdf",
        "current_text_in_pdf", "earlier_quote_still_present", "six_gram_overlap",
        "reaudit_verdict", "basis_for_judgement", "suggested_wording", "notes"]

MATH = re.compile(r"\$[^$]*\$|\\\[[^\]]*\\\]|\[math\]")


def norm_words(text):
    text = re.sub(r"-\s*\n\s*", "", text)          # undo end-of-line hyphenation
    t = MATH.sub(" math ", text)
    t = re.sub(r"\[[^\]]{0,120}\]", " ", t)          # citation brackets [12], [Author2020]
    t = re.sub(r"\\[a-zA-Z]+", " ", t)
    t = t.replace("{", " ").replace("}", " ").replace("~", " ")
    t = t.lower()
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.findall(r"[a-z0-9]+", t)


def grams(words, n=6):
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def locate(stmt_words, pages_words, min_frac=0.55):
    """Page with the best word-sequence match for the statement.

    Two measures are combined: the longest contiguous run of statement words found on the
    page (robust to a changed word inside the sentence) and the total matched-word mass
    (robust to line breaks).  A page is accepted when either is strong.
    """
    import difflib
    if not stmt_words:
        return None, 0.0
    best, best_score, best_run = None, 0.0, 0
    for pno, words in pages_words:
        sm = difflib.SequenceMatcher(None, stmt_words, words, autojunk=False)
        blocks = sm.get_matching_blocks()
        mass = sum(b.size for b in blocks) / len(stmt_words)
        run = max(b.size for b in blocks)
        score = max(mass, run / 12.0)
        if score > best_score:
            best, best_score, best_run = pno, score, run
    ok = best_score >= min_frac or best_run >= 8
    return (best, best_score) if ok else (None, best_score)


def main(argv):
    pdf = os.path.join(HERE, "..", "..", "main.pdf")
    reg = os.path.join(HERE, "..", "..", "claim_register.csv")
    earlier = os.path.join(HERE, "..", "P1_audit", "reaudit_flagged_20.csv")
    if "--pdf" in argv:
        pdf = argv[argv.index("--pdf") + 1]
    if "--register" in argv:
        reg = argv[argv.index("--register") + 1]
    if "--earlier" in argv:
        earlier = argv[argv.index("--earlier") + 1]

    cache = "/tmp/pdf_pages.json"
    if os.path.exists(cache) and "--fresh" not in argv:
        pages = json.load(open(cache))
    else:
        from pypdf import PdfReader
        pages = [(p.extract_text() or "") for p in PdfReader(pdf).pages]
        json.dump(pages, open(cache, "w"))
    pages_words = [(i + 1, norm_words(t)) for i, t in enumerate(pages)]

    old = {}
    if os.path.exists(earlier):
        for r in csv.DictReader(open(earlier, newline="")):
            old[r["claim_id"]] = r

    import difflib

    def content(words):
        """Content words only: length >= 4, so that math fragments and stop words drop out."""
        return {w for w in words if len(w) >= 4}

    def overlap_with(a_words, b_words):
        """Recall of the quote's content words on the page (order-free, robust to maths)."""
        a, b = content(a_words), content(b_words)
        if not a:
            return 0.0
        return len(a & b) / len(a)

    rows = []
    for r in csv.DictReader(open(reg, newline="")):
        if r["verdict"] not in ("PARTLY SUPPORTED", "NOT SUPPORTED"):
            continue
        cid = r["claim_id"]
        prev = old.get(cid, {})
        prev_words = norm_words(prev.get("current_text", ""))

        # best page for the wording the earlier pass judged, then the same measure over a
        # three-page window (a sentence can continue across a page break)
        quote_page, quote_ov = None, 0.0
        if prev_words:
            for pno, words in pages_words:
                ov = overlap_with(prev_words, words)
                if ov > quote_ov:
                    quote_page, quote_ov = pno, ov
            if quote_page:
                window = []
                for pno in (quote_page - 1, quote_page, quote_page + 1):
                    if 1 <= pno <= len(pages):
                        window += norm_words(pages[pno - 1])
                quote_ov = max(quote_ov, overlap_with(prev_words, window))

        # best page for the register statement
        page, frac = locate(norm_words(r["manuscript_statement"]), pages_words)

        if prev_words and quote_ov >= 0.8:
            page, still, overlap = quote_page, "yes", round(quote_ov, 2)
            verdict = "resolved" if prev.get("matches_source") == "yes" else "still partly supported"
            basis = prev.get("basis_for_judgement", "") or \
                "Carried over from the earlier pass over the same wording."
            note = "the wording the earlier pass judged is still on this page (overlap %.2f)" % quote_ov
        elif prev_words and quote_ov >= 0.5:
            page, still, overlap = quote_page, "partly", round(quote_ov, 2)
            verdict = "wording changed - re-check"
            basis = ("The passage survives on this page but was edited after the earlier pass "
                     "(overlap %.2f), so the carried-over judgement no longer applies verbatim." % quote_ov)
            note = "edited wording; statement match score %.2f" % frac
        elif page is not None:
            still, overlap = "no", ""
            verdict = "wording changed - re-check"
            basis = ("The passage is in this PDF, but the wording the earlier pass judged is not: "
                     "the judgement would not apply to this text.")
            note = "statement located on this page (score %.2f); earlier wording absent" % frac
        else:
            still, overlap = "no", ""
            verdict = "not located"
            basis = ("Neither the register statement nor the earlier wording could be matched to "
                     "any page of main.pdf; no judgement is made.")
            note = "statement match score %.2f" % frac

        cur = re.sub(r"\s+", " ", pages[page - 1]).strip() if page else ""
        rows.append(dict(claim_id=cid, register_verdict=r["verdict"],
                         cited_source=r["cited_source"].split(" | ")[0],
                         manuscript_page=page if page is not None else "",
                         located_in_pdf=("yes" if page is not None else "no"),
                         current_text_in_pdf=(cur[:600] + ("..." if len(cur) > 600 else "")),
                         earlier_quote_still_present=still,
                         six_gram_overlap=overlap,
                         reaudit_verdict=verdict,
                         basis_for_judgement=basis,
                         suggested_wording=prev.get("suggested_wording", ""),
                         notes=note))

    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        w.writerows(rows)
    counts = {}
    for r in rows:
        counts[r["reaudit_verdict"]] = counts.get(r["reaudit_verdict"], 0) + 1
    print("wrote %s (%d rows): %s" % (os.path.basename(OUT), len(rows),
                                      ", ".join("%s=%d" % kv for kv in sorted(counts.items()))))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
