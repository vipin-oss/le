# Born and Huang (1954) read: what the book settles about CR181, and what it does not

`claim_register.csv` has exactly one claim that mentions Born at all — **CR181**, the last claim on the
request list:

> For a monatomic chain with nearest-neighbour spring constant kappa_s, mass m and spacing a the exact
> relation is omega = 2 sqrt(kappa_s/m) |sin(ka/2)| (Born and von Karman 1912).

The related book arrived on 2026-11-01 and was read on its printed pp. 55–57 and p. 79, as page images
(the scan's text layer is OCR and was used only to find the pages, never to quote them). The full record
is `BORN_HUANG_1954_READ_2026-11-01.csv`, eleven rows: seven of printed matter, three of algebra and
numerics, one negative finding.

## What the pages say

| printed page | what is there | what it settles |
|---|---|---|
| p. 55, §5 opening | "a simple model due originally to Born and Kármán" | the attribution: the model is the two authors' jointly |
| p. 55, footnote | "M. Born and Th. von Kármán, *Phys. Zeit.* **13**, 297 (1912)" | the reference as cited, including the first page 297 |
| p. 55 | neighbours at `s/2`, like particles at `s` | the two spacings the symbol mapping needs |
| p. 56, (5.5)–(5.8) | `m ü_l = φ″(½s){(u′_l − u_l) − (u_l − u_{l−1})}`, 2×2 determinant | the bond constant is `φ″(½s)`, i.e. the manuscript's `kappa_s` |
| p. 56, (5.9) | `ω² = (φ″(½s)/mm′)[(m+m′) − {(m+m′)² − 4mm′ sin²πη}^½]` | the exact dispersion of the model |
| p. 57, (5.11) + text | `−½ ≤ η < ½`, "cut-off of the wave-number at (1/2s)" | how `η` becomes the manuscript's `k` |
| p. 57, last display | `ω² = (2π²φ″(½s)/(m+m′))η² + O(η⁴)` | the authors' own long-wave expansion — an anchor that is not my algebra |
| p. 79, §6 | "When the masses of the ions are equal, the lattice behaves somewhat like a monatomic solid with one atom to each cell" | the equal-mass case is treated, but in words |

## The three computations

1. **Equal-mass limit.** With `m′ = m`, (5.9) gives `ω² = (4φ″/m) sin²(πη/2)` (acoustic) and
   `(4φ″/m) cos²(πη/2)` (optical). Checked for `m = 1, 2.5, 0.37` on 20 values of `η`: **max |difference|
   3.55e-15**.
2. **Against the book's own expansion.** The limit's small-`η` coefficient is `π²φ″/m`; the coefficient
   printed on p. 57 with `m′ = m` is `2π²φ″/(m+m′) = π²φ″/m`. They agree to **1e-10** (9.8696043116
   measured against 9.8696044011), so the limit is consistent with the authors' own series and not only
   with their equation.
3. **The manuscript's form.** With `κ_s = φ″(½s)`, `a = s/2`, `k = 2π/λ`, `η = s/λ` — so that `πη/2 = ka/2`
   — the limit reads `ω = 2√(κ_s/m)|sin(ka/2)|`. Checked over 500 random wavelengths `λ ∈ (2, 30)`:
   **max |difference| 8.88e-16** over a seeded generator, so the figure is reproducible. Every factor of two is accounted for in the CSV row, because that is
   exactly where a wrong mapping would hide.

## The negative finding

**The book nowhere displays the monatomic formula.** §5 is titled *Vibrations of a diatomic chain*; the
equal-mass case appears as the limit of (5.9) and, on p. 79, as a sentence about the branches joining.
A search of all 431 pages for "monatomic" turned up nothing closer, and the contents list has no monatomic
section.

## What this means for the claim

**Proposed verdict: PARTLY SUPPORTED** (from `SOURCE NOT AVAILABLE`, level R0), and it is recorded here
rather than written into the register, because the register's verdict column is the author's.

- The **model**, the **attribution** and the **derivation** are now backed by a held source, with page
  numbers, and the reference's first page 297 is confirmed by the authors themselves.
- The **1912 note is still unread**, and the book does not print the monatomic relation as a displayed
  equation. So the claim as written — "the exact relation is …, (Born and von Kármán 1912)" — is true but
  rests on a limit computed here, not on a page that prints it in that form.

The clean fix is a citation change, not an evidence hunt: cite **Born and Huang (1954), §5, eq. (5.9)** for
the formula, and keep **Born and von Kármán (1912)** for the model, exactly as the book itself does in its
footnote. On that reading the sentence needs no new source at all; only a direct quotation of the 1912 note
would still want the 1912 note.

## Reproduce

```bash
python3 check_born_huang_read.py     # PASS all checks (rows=11, limit and mapping recomputed)
```

The checker recomputes rows 8 and 9 of the CSV from eq. (5.9) as transcribed here, so the numbers in the
file cannot drift from the file's own arithmetic.
