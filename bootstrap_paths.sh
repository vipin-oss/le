#!/bin/sh
# bootstrap_paths.sh — make the PAPER_PROJECT scripts runnable from this checkout.
#
# Why: 15 scripts of PAPER_PROJECT (including three files that are inside
# CODE_FREEZE_v2_blockF.json: 07_Tests/run_tests.py, 08_Experiments/analyze_v2.py and
# 08_Experiments/make_figures.py) hard-code the absolute paths
#     /home/user/PAPER_PROJECT   and   /home/user/work/handoff
# which is where the project lived when it was produced (2026-10-01).
# Patching those files would change their SHA-256 and invalidate the code freeze, so we
# restore the expected paths with symlinks instead.  Idempotent — safe to re-run.
#
# Usage:  sh bootstrap_paths.sh            (or:  . ./bootstrap_paths.sh)
# Run it once per session / after any workspace restore.

set -e
REPO=$(cd "$(dirname "$0")" && pwd)

ln -sfn "$REPO/PAPER_PROJECT" /home/user/PAPER_PROJECT
ln -sfn "$REPO/work"          /home/user/work

echo "PAPER_PROJECT -> $(readlink /home/user/PAPER_PROJECT)"
echo "work          -> $(readlink /home/user/work)"
test -f /home/user/work/handoff/MANIFEST_SHA256.json || { echo "ERROR: handoff baseline not found" >&2; exit 1; }
echo "handoff baseline OK"
