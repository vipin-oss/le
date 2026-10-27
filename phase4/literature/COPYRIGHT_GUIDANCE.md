# Copyright and Usage Guidance for Research PDFs

**Branch:** arena/40393d9f-le  
**Date:** 2026-10-21  
**Purpose:** Guidance for handling the forthcoming corpus of 100+ original research PDFs.

---

## Core Principle

**Never commit copyrighted full-text PDFs to a public repository without explicit authorization from the copyright holder.**

Many of the papers in the forthcoming corpus are published by commercial publishers (Springer, Elsevier, Wiley, MDPI, etc.) and are protected by copyright. Uploading them to a public GitHub repository may constitute copyright infringement.

---

## Recommended Directory Structure

```
phase4/literature/
├── incoming/          # PDFs placed here by researcher (PRIVATE - not committed)
├── verified/          # PDFs verified for open-access status (PRIVATE - not committed)
├── metadata/          # Generated metadata, citation records, extraction indices (OK to commit)
├── extraction/        # Extracted text from PDFs (may contain copyrighted content - be cautious)
├── duplicates/        # Duplicate PDFs detected by hash (PRIVATE - not committed)
├── reports/           # Ingestion reports (OK to commit)
├── COPYRIGHT_GUIDANCE.md  # This file
└── pdf_ingestion_pipeline.py  # Processing script (OK to commit)
```

---

## Handling Different Access Levels

| Access Level | Example | Can Commit PDF? | Can Commit Metadata? | Can Commit Extracted Text? |
|-------------|---------|-----------------|---------------------|---------------------------|
| Open access (CC BY) | Scientific Reports, PLOS ONE | Yes (with attribution) | Yes | Yes |
| Open access (other license) | Some MDPI, Frontiers | Check license | Yes | Yes (check license) |
| Subscription/paywalled | JMPS, J. Mech. Phys. Solids | NO | Yes | No (fair use excerpts only) |
| Preprint (arXiv) | arXiv:1211.4481 | Yes | Yes | Yes |
| Placeholder/unverified | barak2023a, gupta2023a | NO | Yes (marked unverified) | No |

---

## Recommended Workflow

1. **Researcher places PDFs in `phase4/literature/incoming/`**
2. **Run ingestion pipeline:** `python phase4/scripts/pdf_ingestion_pipeline.py --all`
3. **Pipeline generates:**
   - SHA-256 hashes for deduplication
   - Extracted text (for open-access PDFs only)
   - Study index with DOI, title, section mapping
   - Ingestion report flagging scanned PDFs and extraction errors
4. **Researcher manually verifies:**
   - DOI-to-paper matching
   - Section mapping accuracy
   - Mathematical content extraction quality
5. **Open-access PDFs** can be moved to `verified/` and committed with attribution
6. **Paywalled PDFs** remain in `incoming/` or `verified/` but are NOT committed
7. **Metadata and reports** (no full text) are committed to the repository

---

## .gitignore Recommendations

Add to `.gitignore`:

```
# Copyrighted PDFs - do not commit
phase4/literature/incoming/*.pdf
phase4/literature/verified/*.pdf
phase4/literature/duplicates/*.pdf

# Extracted text may contain copyrighted content
phase4/literature/extraction/*.txt

# Committed items (metadata only)
!phase4/literature/metadata/
!phase4/literature/reports/
!phase4/literature/COPYRIGHT_GUIDANCE.md
!phase4/literature/pdf_ingestion_pipeline.py
```

---

## Fair Use Considerations

For paywalled papers, limited excerpt quotation for purposes of criticism, comment, or scholarly review may qualify as fair use. However:

- Extract only small portions (equations, short passages)
- Always cite the source
- Do not distribute extracted text publicly
- Use extracted content only for internal manuscript preparation

---

## When PDFs Arrive

The researcher should:
1. Place PDFs in `phase4/literature/incoming/`
2. Run the ingestion pipeline
3. Review the ingestion report
4. Manually verify ambiguous DOI/title matches
5. Map studies to manuscript sections using the section hint field
6. Flag studies requiring full-text equation verification

The ingestion pipeline never modifies or deletes original PDFs.

---

**End of Copyright Guidance**
