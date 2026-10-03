# RESTORE_PROJECT_TREE

**Read this if you want to run the code rather than read the archive.**

The archive is organised by question — `01_PROGRAM`, `02_OVERLEAF`, `03_DATA`, … — because that is how a
reviewer looks for things. The code, though, resolves paths against the layout it was written in
(`PAPER_PROJECT/09_Raw_Data/...`, `tools/`, `work/handoff/...`). `restore_project_tree.py` (same folder)
rebuilds that layout from the archive:

```bash
python3 01_PROGRAM/restore_project_tree.py --list          # what it would do, nothing more
python3 01_PROGRAM/restore_project_tree.py --into ../run-here
cd ../run-here && sh bootstrap_paths.sh
```

## How it knows where things go

It reads `09_ARCHIVE_METADATA/file_manifest_sha256.csv` and replays its `source_path` column, verifying
each file's SHA-256 before copying. There is deliberately no mapping table inside the restorer: a second
copy of the layout rules is how a restorer starts writing files to the wrong place while still reporting
success. If the manifest and the archive disagree, the hash check fails loudly instead.

## What you get, and what you do not

- **You get** every source file, every raw and processed data file, every document and configuration, the
  code-freeze manifests, and the generated index documents — enough that `analyze_v2.py`,
  `make_provenance.py`, `make_figures.py`, `reproduce.py`, `run_tests.py`, the three manuscript builders and
  all the QA gates run without edits.
- **You do not get** a git checkout (no `.git`), nor the files the project never tracked: the 600-dpi PNG
  and TIFF renditions and the generated archives under `PAPER_PROJECT/packages/`. Each is one command away
  (`RUN_ORDER.md` steps 5 and 8); a restored tree missing them is expected, not broken.
- **Then verify, don't assume.** `python3 PAPER_PROJECT/06_Source_Code/verify_code_freeze.py` re-hashes the
  27 frozen files against `CODE_FREEZE_submission_2026_10_03j.json` and exits non-zero on any difference.
  It is used instead of `tools/connection_audit.py` here because that tool also inspects git state and a
  restored tree has no `.git`; inside a real checkout either works, and the archive records both.
  Old wording kept for the record: `python3 tools/connection_audit.py` (read-only) re-hashes the 27 frozen
  files against `CODE_FREEZE_submission_2026_10_03j.json` and fails on any difference. Run it after a
  restore and after any edit — it is the mechanism that turns "the code looks the same" into a checked
  statement. The manuscript builders apply the same rule from the other side: they abort *before writing*
  when the deposited manifest is not current, which is why a restored tree cannot quietly rebuild a
  manuscript from modified code. Neither script takes a `-c` flag; the builders take no options at all.
