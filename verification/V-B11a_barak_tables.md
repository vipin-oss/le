# V-B11a — Barak et al. energy-ratio tables: render check, and withdrawal of the numeric claim

**Order:** `control/BRAVE_B11.md` condition 1 @ `origin/claude/control` `a0ace86`. **Access date:** 2026-10-22.
**Effect:** `V-B9c` §3.3's numeric evidence is **withdrawn** (tag `UNVERIFIED`); the paper-level row is
tagged `CONDITIONAL`; no accusation is recorded anywhere.

---

## 1. Task

The numeric claim I made in `V-B9c` — that nine printed numbers sum to 0.120 / 0.889 / 1.121 and so
violate the paper's own eq (58) — must be re-read from the **page render** of the tables, not from a text
layer. Until two renderings agree, tag it `UNVERIFIED`. The review may state only, neutrally, that the
printed values do not satisfy the stated unity at the stated precision, and must never accuse. The paper
row is to be tagged `CONDITIONAL`, not `WRONG`.

## 2. Method

Three independent render paths were attempted for the tables beneath Figs 2–9 (incident `P`):

1. **Publisher PDF** (`nature.com/articles/s41598-023-44339-5.pdf`, 11 chunks): the fetch returned the
   figure data as markdown-like tables with angles `0…90°` and columns for `n=p=l=1`, `n=3,p=2,l=2`,
   `n=4,p=3,l=3`. This is the single rendering that yields numbers, and it is the one `V-B9c` used.
2. **Publisher HTML article page** (18 chunks, all figure captions + `lw685` PNG links): **no data table**
   for any figure — only captions and image URLs. Checked chunk 10 (Figs 22–25 and the "For incident P
   wave" discussion) and the figure-anchor chunks: no `Angle of incidence` table anywhere in the HTML.
3. **Per-figure HTML** (`/articles/s41598-023-44339-5/figures/9`): the page contains the figure **image**
   (`41598_2023_44339_Fig9_HTML.png`) and a one-line caption. No table, no numeric axis labels in text.

## 3. Result

**Two renderings do not agree — because only one of them yields numbers at all.**

| path | numbers available? |
|---|---|
| PDF conversion | yes (the set used in `V-B9c`) |
| HTML article page | no (images + captions only) |
| per-figure HTML page | no (image + caption only) |

Therefore, per the condition:

* The claim "the printed values violate eq (58)" is **UNVERIFIED** and is **withdrawn as evidence**.
  `V-B9c` §3.3 and the `V-B9a`-CHECK-5 comparison are marked accordingly.
* The paper row is tagged **`CONDITIONAL`**, not wrong. Nothing in the review may say the paper is in
  error. The strongest wording permitted — and only if a reviewer supplies a second, agreeing read of the
  figures — is: *"the printed values do not satisfy the stated unity at the stated precision."*
* I am not able to inspect the figure images themselves (the sandbox cannot render them, and a page image
  must never be committed to this public repository), so the second rendering is out of reach here rather
  than absent from the world.

What **survives** from `V-B9c` unchanged, because it rests on **equations** (and the HTML and PDF agree on
the equations, so those two renderings do agree):

* eq (53) builds the transmitted flux of each mode on `‖H_s‖²` alone (diagonal);
* eq (57) carries the pairwise products `H_s H̄_t`, `s ≠ t`, and `E_int = Σ_{s≠t}E_st` (eq 58);
* eq (58) asserts `Σ_s(ES_s + E_int + E_RP + E_RT + E_RS) = 1`;
* hence `E_int` is a **lumping of pairwise products**, i.e. the sum rule is a definitional bookkeeping
  statement, not an independent check — this is a statement about the *structure*, which needs no figures.

The quantitative part of the E_int finding in `V-B9c` §3.1–§3.2 (my own `V-B3d` case: deficits
`−4.3×10⁻⁴` diagonal and `−9.5×10⁻⁴` with the outgoing cross term) is **untouched**: it is my
computation, not the paper's data. The conclusion "the identity is not automatic" therefore stands on
`V-B3c`'s own numbers, and no longer on the paper's tables.

## 4. Evidence / sources

* Barak, Ahmad, R. Kumar, R. Kumar, Gupta, Awwad, Ismail (2023), *Sci. Rep.* **13**,
  DOI `10.1038/s41598-023-44339-5` (gold OA). Access 2026-10-22, publisher PDF (chunks 4–6) and publisher
  HTML (chunks 7, 10, 11) and per-figure page `/figures/9`. **Access level: equations FULL; figure
  data unreachable in more than one rendering.**
* `V-B9a_checks.py` CHECK 5 (the arithmetic, retained but now labelled provisional).
* `control/BRAVE_B11.md` condition 1.

## 5. Checks done

1. Three render paths tried, not one (PDF, HTML article, per-figure page).
2. The *equations* were checked for two-rendering agreement separately from the *tables* — so the part
   that survives is not contaminated by the part that fails.
3. The withdrawal is propagated to every file that used the numbers (`V-B9c` §3.3, `V-B9a_checks.py`
   CHECK 5 output, and the `LITERATURE_BASE` row for this paper).
4. Wording checked against the condition: no sentence anywhere states or implies misconduct; the tag is
   `CONDITIONAL`; the neutral sentence is recorded as the maximum permitted, and only pending a second
   agreeing read.

## 6. Confidence

* That only one rendering yields numbers: **HIGH** (three fetches, quoted above).
* That the equations decompose as claimed: **HIGH** (HTML and PDF agree on eqs 53/57/58; arithmetic
  survives).
* That the printed figures do or do not satisfy eq (58): **UNVERIFIED** — no confidence claimed.

## 7. NOT verified / open issues

* The figure **images** were never read. Any future check needs a human or a vision pass on the PNGs, in
  a context where the images are *not* committed to this public repository.
* `V-B9c` §3.3's three specific numbers (0.120 / 0.889 / 1.121) are retained in the file only as the
  single-rendering observation, clearly marked; they are not to be quoted in the review.
* No other table in the paper was checked (Figs 10–25 for incident `T`/`SV` were not read at all).
* If a second rendering later agrees, the tag can move to
  `CONDITIONAL on the printed precision` with the neutral sentence; the paper-level tag should not move
  to WRONG even then, by order.
