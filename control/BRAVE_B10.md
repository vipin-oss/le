# BRAVE B10: Drive full-text base (handler connected Drive to Brave; ~400 published papers)
Do B9 first (unchanged), then B10.
HARD RULES
- Read ONLY the papers/publications folders in Drive. NEVER open, list or quote the private folder "Dr. Vipin Gupta - Personal (Private, kabhi share na karein)" or anything outside papers. If unsure whether a folder is private, skip it and say so.
- Repo is PUBLIC: never commit PDFs, full text, long quotes or page images of any paper. Commit only: metadata, claim-level facts, equation numbers, short (<15 words) quoted fragments, status tags.
B10a INVENTORY: DRIVE_INVENTORY.csv (file title, Drive id, first-author, year, journal, DOI if printed, matched LITERATURE_BASE key or NEW, read_level = NONE). No reading of bodies yet beyond title/first page.
B10b PRIORITY: rank by use for the review: (1) governing-equation papers: GL/LS/GN/DPL/TPL/MGT/MDD/nonlocal/GK originals and Barak/Gupta group papers behind sec 9.7 and EQ-10.12; (2) interface/energy-partition papers; (3) rest. Output DRIVE_PRIORITY.md.
B10c READ tier 1 in batches of <=10: for each, record in FULLTEXT_FACTS.csv: key, heat/constitutive law as printed (eq no.), stress/energy eq, parameter ordering/stability condition, energy-ratio definition (R_flux/R_ref/R_mode, cross terms), status tag (PRIMARY-SOURCE-CHECKED / SECONDARY-SOURCE ...), and every conflict with the manuscript or ledgers. Reading limits: if text layer is garbled (equations lost), render the page and read it; if still unreadable, mark UNVERIFIED, never guess.
B10d REPORT: per batch, push to arena/04fdf32e-le, hash, 10-line status. Update LITERATURE_BASE read_level and fill missing authors/DOIs from the papers themselves (this also closes the 290 blank-author problem for those keys).
