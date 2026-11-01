#!/usr/bin/env bash
# Pull the latest Overleaf project into this repository as a NEW folder.
#
#   ./pull_from_overleaf.sh <overleaf-git-url> [branch]
#   OVERLEAF_GIT_URL=git.overleaf.com/<project-id> ./pull_from_overleaf.sh
#
# What it does
#   1. clones the Overleaf project into a throw-away directory (shallow, one branch);
#   2. copies the whole project into paper_v2/from_overleaf/<UTC timestamp>/ ;
#   3. writes CHANGED_FILES.md next to that copy, listing every file that differs from
#      the copy already in the repository (added / changed / only-on-Overleaf).
#
# What it never does
#   It never overwrites an existing file in this repository, and in particular it never
#   touches a .tex file outside paper_v2/from_overleaf/. The author's standing rule is
#   that .tex files are not edited by the agent; bringing a newer copy in and letting a
#   human decide what to replace keeps that rule intact.
#
# Credentials
#   Overleaf's git bridge asks for your Overleaf e-mail and a git token that Overleaf
#   shows under Account -> Git integration. git will prompt for them itself: type them at
#   the prompt, never into a chat, a document or a repository file. Nothing here stores
#   them; do not put them in the URL.
#
# Requires: git. No other dependency.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

URL="${1:-${OVERLEAF_GIT_URL:-}}"
BRANCH="${2:-${OVERLEAF_BRANCH:-main}}"

if [ -z "${URL}" ]; then
    echo "FAIL no Overleaf git URL given"
    echo "     usage: $0 git.overleaf.com/<project-id> [branch]"
    echo "     the URL is in Overleaf under Menu -> Git (it ends in the project id)"
    exit 2
fi

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
DEST="${OVERLEAF_DEST:-${REPO_ROOT}/paper_v2/from_overleaf/${STAMP}}"

TMP="$(mktemp -d)"
trap 'rm -rf "${TMP}"' EXIT

echo "== cloning ${BRANCH} from the Overleaf project (shallow)"
if ! git clone --depth 1 --branch "${BRANCH}" "${URL}" "${TMP}/src" 2>"${TMP}/clone.err"; then
    if grep -qiE "not found|remote branch|couldn't find" "${TMP}/clone.err"; then
        echo "   branch ${BRANCH} not there, taking the project's default branch"
        git clone --depth 1 "${URL}" "${TMP}/src"
    else
        echo "FAIL clone failed - see the message above"
        echo "     a blocked network, a wrong project id and a wrong token all look like this;"
        echo "     git.overleaf.com is not reachable from every sandbox, so run this on the"
        echo "     machine that can open Overleaf in a browser."
        exit 1
    fi
fi

rm -rf "${TMP}/src/.git"
mkdir -p "${DEST}"
echo "== copying into ${DEST#"${REPO_ROOT}/"}"
cp -a "${TMP}/src/." "${DEST}/"

echo "== comparing with what the repository already holds"
CHANGED="${DEST}/CHANGED_FILES.md"
{
    echo "# What the Overleaf pull brought, compared with this repository"
    echo
    echo "- pulled (UTC): ${STAMP}"
    echo "- branch: ${BRANCH}"
    echo "- landed in: paper_v2/from_overleaf/${STAMP}/"
    echo "- nothing outside that folder was overwritten"
    echo
    echo "| file | state |"
    echo "|---|---|"
} > "${CHANGED}"
n_new=0
n_diff=0
while IFS= read -r -d '' f; do
    rel="${f#"${DEST}/"}"
    other="${REPO_ROOT}/paper_v2/${rel}"
    if [ ! -e "${other}" ]; then
        echo "| \`${rel}\` | new - not in the repository |" >> "${CHANGED}"
        n_new=$((n_new + 1))
    elif ! cmp -s "${f}" "${other}"; then
        echo "| \`${rel}\` | differs from \`paper_v2/${rel}\` |" >> "${CHANGED}"
        n_diff=$((n_diff + 1))
    fi
done < <(find "${DEST}" -type f ! -name 'CHANGED_FILES.md' -print0 | sort -z)

n_tex=$(find "${DEST}" -type f -name '*.tex' | wc -l | tr -d ' ')
n_all=$(find "${DEST}" -type f ! -name 'CHANGED_FILES.md' | wc -l | tr -d ' ')
{
    echo
    echo "Total: ${n_all} files, ${n_tex} of them .tex; ${n_new} new, ${n_diff} differing."
} >> "${CHANGED}"

echo "     ${n_all} files (${n_tex} .tex), ${n_new} new, ${n_diff} differing"
echo "     file list: ${CHANGED#"${REPO_ROOT}/"}"
echo "PASS overleaf pull complete ($(printf '%s' "${n_all}") files, ${n_tex} tex, ${n_new} new, ${n_diff} differing)"
exit 0
