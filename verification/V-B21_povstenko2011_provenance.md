# V-B21 — independent provenance of `povstenko2011.pdf` from the original Drive archive `R4.zip`

**Verifier:** Brave (independent), batch **B21**, 2026-10-24.
**Branch examined:** `arena/04fdf32e-le` @ **`d02e58e`** (my branch, `origin` updated this batch; no other branch touched).
**Bottom line: retrieval SUCCEEDED, and it is the original archive — SHA-256 of the downloaded bytes matches the SHA-256 recorded by Google Drive for the file. `povstenko2011.pdf` is present, is the `.511931` paper, is legible, and its Eq. (29) does NOT print the Γ-normalised prefactor. The manuscript's Γ(1+α) claim stays OPEN. No project file was changed. R3 remains NOT PASSED.**

## 1. Task

Resolve the provenance of the claimed `povstenko2011.pdf` by inspecting the **original recorded Drive archive**, not a replacement copy: confirm the item can be retrieved with the authorised connector, record exact identity/filename/size/metadata and hashes, list the archive read-only, locate the member, verify its bibliographic identity against `10.1080/01495739.2010.511931` and distinguish it from `.511929`, then read Eq. (29) on printed p. 101 and Appendix A on printed p. 113 with the real leaf mapping — or report the exact access failure.

## 2. Method and retrieval result

| step | call | result |
|---|---|---|
| 1. metadata | Drive connector `get_file` on id `1atjU8CpTSNWzszaVEq061N0t8rZ5NtQ4` | **success** — see §3 |
| 2. retrieval | Drive connector `download_file` (`supports_all_drives: true`) | **success** — 62,292,559 bytes written to `google_drive/R4.zip` in the workspace |
| 3. moved out of the repo | `mv google_drive/R4.zip /tmp/b21/R4.zip` | the connector's default landing directory is inside the repo; moved to `/tmp` **before** any commit so nothing enters Git |
| 4. hash | `sha256sum`, `md5sum` on the received bytes | `ae550e57…54bb` / `7e9b30f4…34fe` — **both equal the Drive-recorded checksums** |
| 5. integrity | `unzip -t` | "No errors detected in compressed data" |
| 6. listing | `unzip -l` (read-only) | 19 members, exact list in §4 |
| 7. member extract | `unzip -j R4.zip povstenko2011.pdf -d /tmp/b21/member` | 434,436 bytes, §5 |
| 8. identity | pypdf text layer + rendered page images | §5, §6 |
| 9. pages | pypdf text; `pypdfium2` 2.2× renders of leaves 6, 17, 18 | §6 |

**Direct network egress is not the mechanism and was not used.** My sandbox has no route to `drive.google.com`, `www.googleapis.com` or `storage.googleapis.com` (all three fail immediately; only `github.com` is reachable). The authorised Drive **connector** is the retrieval path, and it worked. This is important for the provenance question: the bytes came from Drive through the connector, not from a search engine, a publisher mirror, or anything Arena supplied.

## 3. Archive identity (metadata as returned)

| field | value |
|---|---|
| name | `R4.zip` |
| Drive id | `1atjU8CpTSNWzszaVEq061N0t8rZ5NtQ4` — **matches the id in the request** |
| size | **62,292,559 bytes** — **matches the recorded size exactly** |
| MIME | `application/x-zip-compressed` |
| **SHA-256 (Drive)** | `ae550e57c0b117233df65cc8c8b922d4844f9948b917b69e786f7644f3fb54bb` |
| **MD5 (Drive)** | `7e9b30f4eb2e5b4538ea548cf9ad34fe` |
| created / modified | 2026-10-24T06:28:33Z / 2026-10-24T06:26:19Z |
| owner | Vipin Gupta (vipin@gurugramuniversity.ac.in) |
| trashed | false |
| canDownload | true |
| parent | one folder id, recorded but **not named here** (B10a privacy rule: the private/personal folder name is never written into a repo file) |

**SHA-256 of the bytes I received: `ae550e57c0b117233df65cc8c8b922d4844f9948b917b69e786f7644f3fb54bb` — identical to Drive's own recorded value.** That equality is the provenance proof: the file whose directory I inspected is byte-for-byte the file Drive holds under the requested id. Nothing was substituted.

## 4. Archive directory listing (read-only, as archived)

19 members, all at the archive root, no directories, all timestamps 2026-10-24 06:12:

| member | bytes |
|---|---|
| `fabrizio2014.pdf` | 385,286 |
| `gurtin1968.pdf` | 561,126 |
| `hetnarski2000.pdf` | 171,861 |
| `huberman2019.pdf` | 1,220,875 |
| `jackson1970.pdf` | 588,695 |
| `jou2010.pdf` | 4,687,450 |
| `lamb1917.pdf` | 1,410,158 |
| `lim2015.pdf` | 1,514,270 |
| `liu1972.pdf` | 752,083 |
| `maxwell1867.pdf` | 2,929,291 |
| `mindlin1965.pdf` | 1,336,013 |
| `mindlin1968.pdf` | 862,068 |
| `mitra1995.pdf` | 1,935,744 |
| `nayfeh1971.pdf` | 726,447 |
| `New_fractional_derivatives_with_nonlocal_and_non-s.pdf` | 422,121 |
| `nonlocal-continuum-field-theories-2004.pdf` | 29,709,054 |
| **`povstenko2011.pdf`** | **434,436** |
| `povstenko2015.pdf` | 18,574,414 |
| `puri1972.pdf` | 712,742 |
| **total uncompressed** | **68,934,134** |

The archive was **not** modified, renamed, re-zipped, or replaced; the only writes were to `/tmp`.

## 5. The matching member

| field | value |
|---|---|
| archive member path | **`povstenko2011.pdf`** (root of `R4.zip`, no subdirectory) |
| member SHA-256 | **`8ca735824dc415cba120753457c6502f61ffb41a2346f04b90148f6eef50ebd1`** |
| member MD5 | `f074fafe9d0157cfbb103419080cdbd2` |
| member size | 434,436 bytes |
| PDF leaves | 19 |
| PDF metadata | `/Creator: 3B2 Total Publishing System 7.51c/W`, `/Producer: iText 4.2.0 by 1T3XT`, created `D:20110107172618Z`, modified `D:20150103152446-08'00'` — a publisher-typeset PDF with a real text layer |

**Bibliographic identity — from the article's own splash page (leaf 1), not from a catalogue:**

> "Fractional Cattaneo-Type Equations and Generalized Thermoelasticity / Y. Z. Povstenko / Institute of Mathematics and Computer Science, Jan Długosz University in Częstochowa … **Published online: 11 Jan 2011** … Journal of Thermal Stresses, **34:2, 97-114**, **DOI: 10.1080/01495739.2010.511931**."

**Identity: VERIFIED as `10.1080/01495739.2010.511931`.** It is the **fractional-Cattaneo** paper, **not** the `.511929` *Dirichlet problem for time-fractional radial heat conduction in a sphere…* (34(1):51–67) article. The archive contains **no** file corresponding to `.511929` — the two Povstenko members are `povstenko2011.pdf` (`.511931`) and `povstenko2015.pdf` (the book). So the manuscript's `Povstenko2011` key, which carries the `.511929` DOI, cannot have come from this archive: the supplied file is the other paper. B20's key mismatch stands, now with the supplied artefact in hand.

## 6. Printed-page ↔ PDF-leaf mapping, and what the pages actually print

Cover-to-cover the file is **1 splash leaf + 18 printed pages (97–114)**, so the mapping is **leaf = printed page − 95** throughout, with **no offset drift** and **no skipped or duplicated leaf**. Verified against the running heads (recto `FRACTIONAL CATTANEO-TYPE EQUATIONS nnn`, verso `nnn Y. Z. POVSTENKO`):

| leaf | printed | content checked |
|---|---|---|
| 1 | — | Taylor & Francis splash/download page |
| 2 | 97 | article opening, running head + copyright line |
| 5 | 100 | ζ introduced: "where **ζ is a nonnegative constant**" (Eq. 16); Cattaneo Eq. (17), telegraph Eq. (18) |
| **6** | **101** | **Eqs. (23)–(31)** — the page the claim turns on |
| 17 | 112 | **APPENDIX A begins** (Riemann–Liouville I^α, A.1–A.8) |
| **18** | **113** | A.9, A.10 end Appendix A; **APPENDIX B** (Mittag-Leffler B.1–B.4); **APPENDIX C** begins (C.1) |
| 19 | 114 | Appendix B/C continuation, end of article |

**Legibility: YES.** The text layer is complete and clean, and I additionally rendered leaves 6, 17 and 18 at 2.2× (1109×1585 px) and read the mathematics visually. The equations are fully legible; no page needed for this check was missing, corrupted, or image-only.

**Correction to a premise in the assignment:** **Appendix A is not "printed p. 113" alone — it starts on printed p. 112 (leaf 17) and its last two equations, (A.9) and (A.10), are on p. 113 (leaf 18)**, followed there by Appendices B and C. A reader sent to "p. 113" for Appendix A would land mid-appendix.

### 6.1 Eq. (29), printed p. 101 — what is actually printed

Read from the rendered page and confirmed against the text layer:

> **q + ζ ∂^α q/∂t^α = −k grad T,  0 < α ≤ 1**   (29)

and the companion results on the same page: Eq. (23) `∂^{1−γ}q/∂t^{1−γ} + ζ ∂q/∂t = −k grad T`; Eq. (26) `I^{1−α}q + ζ ∂^α q/∂t^α = −k grad T`; Eq. (30) `∂T/∂t + ζ ∂^{1+α}T/∂t^{1+α} = aΔT`; solutions (25), (28), (31) written as Mittag-Leffler convolutions with the kernel `(t−τ)^{α−1}E_{α,α}[−(t−τ)^α/ζ]` and prefactor `−k/ζ`.

**The coefficient of the fractional derivative is ζ — a single symbol, defined two pages earlier at Eq. (16) as "a nonnegative constant" (the relaxation time in `q = −(k/ζ)∫exp(−(t−τ)/ζ) grad T dτ`). No Γ-normalised prefactor appears anywhere on the page.**

Full-article check, not just this page: the string `Γ(1+α)` **does not occur anywhere in the 18 printed pages** (0 hits). Every Γ occurrence is either the Riemann–Liouville/Caputo kernel normalisation `1/Γ(α)`, `1/Γ(n−α)`, `1/Γ(α−k+1)` in Appendix A, or `Γ(αn+1)`, `Γ(αn+β)` inside the Mittag-Leffler series (B.1), (B.2). The nondimensionalisation Eq. (38) scales the coefficient as `ζ̄ = ζ t₀^{2−α}`, i.e. ζ is treated as a constant carrying the fractional time dimension, **not** as `τ^α/Γ(1+α)`.

**Therefore: the manuscript's Eq. (11.4) form `q_i + [τ^α/Γ(1+α)] {}^C D_t^α q_i = −k T_{,i}` is NOT printed in this source.** The source supports *a* fractional Cattaneo flux law for `0 < α ≤ 1` with coefficient `ζ`; it does not supply the Γ-normalised parameterisation, and it does not identify ζ with `τ^α/Γ(1+α)`.

**Per the control: the exact Γ-normalised prefactor claim stays OPEN.** Direct source evidence does not prove it; if anything it now proves the source prints a different, un-normalised coefficient. I make no claim about whether some *other* Povstenko text (e.g. the 2015 book) uses the Γ-normalised form — I did not check that here.

## 7. Reading against Arena's audit — where we now agree and where the record still differs

| item | Arena (`scientific-audit.md`, commit `0a1eb01`) | this batch |
|---|---|---|
| supplied file is `.511931`, not `.511929` | asserted | **now independently VERIFIED** at the file's own splash page, with archive hash |
| Eq. (29), p. 101, `0<α≤1` | asserted | **VERIFIED**, rendered and read |
| "Eq. (29) … does **not** print the manuscript's Γ(1+α) denominator" | asserted | **VERIFIED** — zero occurrences of `Γ(1+α)` in the whole article |
| "pp. 105–108 were not read" | stated as a limitation | consistent with what is legible; I read pp. 100–101, 112–114 in detail and did not attempt a full read either |
| page anchors "printed pp. 97–104 and 109–110" | stated | plausible on the leaf mapping (leaf = page − 95); not re-read page by page here |
| "Appendix A, p. 113" (assignment premise) | — | **corrected**: Appendix A spans printed pp. 112–113; it *begins* on 112 |

Arena described the position correctly; my job was to establish that the artefact behind it is the original, and it is.

## 8. A by-product: the `Povstenko2016` edition question is now closed at the source

Extracting `povstenko2015.pdf` from the same original archive (261 leaves) and reading its copyright page (leaf 5) gives, verbatim:

> "ISSN 0925-0042 ISSN 2214-7764 (electronic) / Solid Mechanics and Its Applications / **ISBN 978-3-319-15334-6  ISBN 978-3-319-15335-3 (eBook)** / **DOI 10.1007/978-3-319-15335-3** / Library of Congress Control Number: 2015932244 / Springer Cham Heidelberg New York Dordrecht London / **© Springer International Publishing Switzerland 2015**"

Member SHA-256 of `povstenko2015.pdf`: `fa737318ac8108b016bbd83cdc77a8dd2958c2491a31e85c11ea08bb197488e1`.

So B20's conclusion is upgraded from "unresolvable" to **contradicted by the supplied copy itself**: the supplied book is the **2015** Springer volume, print ISBN **978-3-319-15334-6**, DOI `10.1007/978-3-319-15335-3` — **not** year 2016 and **not** ISBN 978-3-319-29637-0. The local `Povstenko2016` bib entry (`year = 2016`, `isbn = 9783319296370`, `verified = {NO_DOI}`) does not describe the supplied copy on any of its three fields.

## 9. Evidence / sources

| source | what it gave | access level |
|---|---|---|
| Drive connector `get_file`, id `1atjU8…NtQ4` | name, 62,292,559 bytes, Drive SHA-256 + MD5, owner, dates | metadata |
| Drive connector `download_file` | the archive bytes | **full file** |
| local `sha256sum`/`md5sum`/`unzip -t`/`unzip -l` | byte identity, integrity, member list | full file, read-only |
| `povstenko2011.pdf` (member), text layer + 2.2× renders of leaves 6/17/18 | splash identity, Eqs. (23)–(31), Appendices A–C, legibility | **full article read for the pages cited; not end-to-end** |
| `povstenko2015.pdf` (member), leaf 5 | copyright page: ISBNs, DOI, year | that page only |
| Crossref (from B20, 2026-10-24) | `.511931` = 34(2):97–114 | metadata |

## 10. Checks done

1. **Byte-identity check, not just "it downloaded".** Received SHA-256 **equals** the value Drive stores for the item, and received MD5 equals Drive's MD5. A substituted or corrupted download cannot match both.
2. **Size and id match the request exactly** (62,292,559 bytes; `1atjU8CpTSNWzszaVEq061N0t8rZ5NtQ4`).
3. **Zip integrity verified** before extraction (`unzip -t`: no errors).
4. **Read-only discipline:** the archive was listed and extracted to `/tmp`; nothing was renamed, re-zipped or overwritten, and no member was written back.
5. **Identity from the artefact, not the filename.** The splash page prints journal, volume, issue, pages and DOI; the filename alone proves nothing.
6. **Discrimination test:** explicitly checked that this is `.511931` and not `.511929`, and that the archive contains no `.511929` member at all.
7. **Page mapping established from running heads on every leaf**, not assumed: leaf = page − 95, no drift.
8. **Legibility established visually** at 2.2× render, not inferred from text extraction alone; the extraction was then cross-checked against the image on p. 101.
9. **Whole-article string test** for `Γ(1+α)` (0 hits) rather than a single-page glance — the negative claim is now article-wide.
10. **No project file touched:** `git status` after the batch shows no modification to any tracked file (see §12).

## 11. Confidence

- **Archive identity and proxy for provenance: HIGH.** Two independent hash functions from Drive agree with my local computation; id and size match the recorded values.
- **Member identity `.511931`: HIGH.** Printed on the article's own first page, corroborated by the Crossref record from B20.
- **Page/leaf mapping: HIGH.** Running heads checked leaf by leaf.
- **Eq. (29) text and the absence of `Γ(1+α)`: HIGH.** Read from a rendered image *and* the text layer, and checked across all 18 printed pages.
- **"The source supports a *related* law but not the manuscript's parameterisation": HIGH** as a statement about this article; **no** claim is made about the 2015 book's conventions.

## 12. Changed files and commits

**Project files: none.** No manuscript, bibliography, plan, control, evidence-matrix or status file was edited — `arena/b5e608f8-le` was not fetched into the workspace at all this batch (no `git show` of it was needed), and nothing under `phase5/` exists in my worktree.

**Untracked-then-removed:** the connector wrote `google_drive/R4.zip` inside the repo; it was moved to `/tmp/b21/R4.zip` in the same step chain and the empty `google_drive/` directory removed. It is **not** in Git and is not in the workspace snapshot. The archive and the two extracted members live only in `/tmp`.

**My own verification artefacts committed this batch** (allowed scope, `verification/` only):
- `verification/V-B21_povstenko2011_provenance.md` (this report)
- `verification/api_log/B21_r4_archive_provenance.csv` (archive + member identity, hashes, page map)

Commit: see the 10-line status below for the exact hash on `arena/04fdf32e-le`.

## 13. Remaining uncertainty

1. **The Γ-normalised prefactor claim is still OPEN** — now for a stronger reason: the original source prints `ζ`, not `τ^α/Γ(1+α)`. Whether *any* Povstenko text prints the Γ-normalised form is unchecked; the manuscript must either drop the attribution, re-word it as a review convention (it already labels Eq. 11.4 CONDITIONAL), or cite a source that does print it.
2. **The `Povstenko2011` bib key still points at `.511929`.** The correct `.511931` record is now proven available and hashed; the key fix is Arena's/supervisor's call, not mine.
3. **`Povstenko2016` still carries year 2016 and a non-existent ISBN** for the supplied 2015 book. Proven against the copyright page; not edited.
4. **I read pp. 100–101 and 112–114 closely and did not read the whole article.** Claims about Eqs. (1)–(22), the one-dimensional solution, or the figures are **not** verified by me.
5. **The other 17 archive members were not opened**; the listing only establishes presence and size. In particular I did not re-check that `jackson1970.pdf` is the mixed fragment Arena describes.
6. **"Original archive" is established by hash equality with Drive's stored value, which is as far as provenance can go from inside this environment.** Whether this uploaded ZIP is the same object that was originally received from the publisher in some earlier session cannot be proven from Drive metadata alone; the internal member timestamps are all 2026-10-24 06:12, i.e. the archive was assembled on that date.
7. **R3 remains NOT PASSED.** This batch resolves one provenance question and closes nothing else.
