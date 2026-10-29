# Autonomy Log

## 2026-10-29 — CI GREEN at commit 25ed5d2

CI run 40826618816 passed all steps:
- TeX build: 2m59s, 131 pages
- Undefined references/citations: 0
- Forbidden tags: 0 privacy-token, 0 internal-artifact, 0 internal-path, 0 manuscript-tag
- Rendered figure PDFs: 19 / Figure includes: 17
- Near-overfull boxes: 0

## Ledger Restoration (P0, complete)

Restored OPEN_CLAIMS_LEDGER.csv from git history (ceceac3: 619 rows, A=82/B=154/C=333/V=50).

**Merge method:** Base rows (ceceac3) kept byte-identical; appended 7 new rows from current file not in base (OCL-620..OCL-625, OCL-V-DISP). 44 overlapping IDs with different content kept base rows (differences documented in /tmp/ledger_diff_note.md).

**Result:** 626 rows, A=88, B=154, C=333, V=51. Validator passes.

**No rows were dropped from the failed rebuild.** All 7 new rows (OCL-620..625, OCL-V-DISP) describe real claims and were appended.

**No A rows were intentionally downgraded or removed.** A=29 (previous head) vs A=88 (restored) — the earlier A=29 was due to ledger corruption (~485 rows permanently lost during failed Python fix), partially rebuilt to 179 rows, now fully restored to 626 rows from git history.

## Gate script fixes

1. **verify_interface_energy.py** — Reverted graceful `continue`/silent-skip on missing figure paths (commit f4e6719). Now hard-reads only `master/figures/source/fig13-interface-reflection.svg` with `assert`.
2. **build_figures.sh** — Reverted `2>/dev/null || true` on `cp` commands (commit eae7906). Removed redundant copy from untracked dir. `cp` fails hard if source PDFs absent.
3. **validate_claim_ledger.py** — Added try/except with traceback output. Class V path check now tries `Path(script)` first (repo-root relative, works in CI), then `ROOT.parent / script` fallback.
4. **check_ledger_monotonic.py** — NEW gate script. Fails when ledger IDs at HEAD are not a superset of parent commit IDs, or when A+V count decreases without DOWNGRADE marker. Wired into CI after `validate_claim_ledger.py`.
5. **Q3_THEORY_STATUS.csv** — Tracked in git (was untracked, referenced by 4 Class V rows OCL-549/557/558/561).

## CI workflow changes

- Checkout `fetch-depth: 2` (required for `git show HEAD~1` in check_ledger_monotonic.py)
- Added `Check ledger ID monotonicity` step after `Validate A/V claim-ledger provenance`

## Commit/CI IDs

- Final commit: 25ed5d2 (CI GREEN, run 40826618816)
- Previous: b22eb6b (track Q3_THEORY_STATUS.csv)
- Previous: 206c120 (merge CI artifacts)
- Previous: a6127a7 (restore Class V path check)

No submission/sending/sharing requested or performed.
