# Task 7 — Green–Lindsay ordering in the three locations

**Status: SOURCE NOT AVAILABLE.**

Neither of the two primary sources named in the brief is in this sandbox: there is
no copy of Green & Lindsay, *J. Elasticity* 2 (1972) 1–7 (pp. 5–6) and no copy of
Ignaczak & Ostoja-Starzewski, *Thermoelasticity with Finite Wave Speeds* (OUP 2010)
p. 21. The earlier P18 pass reached the same conclusion from the repository side
(`P18_checks/gl_inequality.md`; `P13_books/books_inventory.csv` records the
Ignaczak volume as NOT SUPPLIED). Because the transcription would have to be
verbatim, with page and equation number, no transcription is given here and no
external claim is made about which ordering the two sources print.

What the manuscript itself now says can be recorded, and in this build the three
locations agree with one another.

## The three locations in the 153-page build (`review-paper-v2` @ `6457295`)

The brief names them as "below Eq. (39), Table 15, Table 22". The numbering moved
between the 157-page revision that P17 and P18 read and the present 153-page
build, so the locations are given here with the numbers and pages that the present
PDF actually prints.

| Location in the brief | In this build | Printed as | Source | What is printed |
|---|---|---|---|---|
| below Eq. (39) | below **Eq. (38)**, p. 27 | §4.2.3, "with τ₁ ≥ τ₀ > 0" | `sections/s05_hyperbolic.tex` lines 36–41 (label `eq:GL` on line 39) | the GL constitutive relations and energy equation, followed by the sentence "with τ₁ ≥ τ₀ > 0" and the mapping to Green & Lindsay's α and h |
| Table 15 | **Table 15**, p. 87 | row "Green–Lindsay" | `sections/s16_synthesis.tex` line 30 (caption line 25, printed p. 87) | extra parameters "2 (τ₀, τ₁)"; well-posed when "τ₁ ≥ τ₀ > 0" |
| Table 22 | **Table 22**, p. 118 | row `eq:GL` | `sections/appEqReg.tex` lines 34–36 (printed p. 118) | status PRIMARY-SOURCE-CHECKED, with the pointer "Green and Lindsay 1972, Eqs. (4.11), (4.13), (4.14), (4.16)" and the condition "τ₁ ≥ τ₀ > 0" |

All three print the same chain, **τ₁ ≥ τ₀ > 0**; the 157-page revision's
two-opposite-statements defect (R5 in the P17 report) is not present in this build.

## The conversion recorded in the manuscript, checked as algebra

The text below Eq. (38) (p. 27) states the mapping explicitly: τ₁ is the
coefficient α of θ̇ in the stress relation, and τ₀ = h/d is the ratio of the
coefficients of θ̈ and θ̇ in the energy equation; the restrictions it attributes to
Green & Lindsay are *dα − h ≥ 0* and *h > 0* (that paper's Eqs. (4.14) and
(4.16)).

With those definitions the printed ordering follows without any further input:
*dα − h ≥ 0* ⇔ α ≥ h/d ⇔ τ₁ ≥ τ₀, and *h > 0* with d > 0 gives τ₀ > 0. So the three
locations are consistent with the manuscript's own premises, and with the mapping
in the brief (α ↔ τ₁, and h ↔ τ₀ through τ₀ = h/d — note that the manuscript's τ₀
is h/d, not h, which is a refinement of the P18 note that simply paired h with τ₀).

What this does **not** establish:

* that Green & Lindsay (1972) prints *dα − h ≥ 0* at Eq. (4.14) and *h > 0* at
  Eq. (4.16) — no copy available, so **NOT VERIFIED**;
* that Ignaczak & Ostoja-Starzewski (2010) p. 21 prints the same condition —
  no copy available, so **NOT VERIFIED**;
* that the equation-register status PRIMARY-SOURCE-CHECKED for `eq:GL` is
  justified — it is the manuscript's own claim, recorded here, not evidence.

## What would close the item

A photograph or scan of Green & Lindsay (1972) pp. 5–6 and of Ignaczak &
Ostoja-Starzewski (2010) p. 21. With those two images the inequality could be
transcribed verbatim with page and equation number, and the three locations could
be checked against it one by one; until then the table above records only what the
manuscript prints, and the external verification stays open.
