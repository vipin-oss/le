# P3 evidence, batch 002: inventory and summary

ASCII only. Evidence only: no manuscript text was edited, no equation was derived, no
citation sentence was written. Every statement below was read from a file opened in this
session. Where a source does not contain a requested item, the entry says not found.

## 1. Archive and working copies

- Requested archive, exact name as delivered: `RIP7.zip` (letters R, I, P, 7).
- Retrieved from the project Drive folder and stored outside the repository at
  `/home/user/rip7/RIP7.zip`.
- Extracted outside the repository into `/home/user/rip7/ex/`. No PDF from this archive is
  committed to the repository, and no PDF path from the Drive folder is recorded in the
  deliverables.
- Contents of the archive (8 files, listed by `unzip -l`):

| File | Bytes | Identity confirmed on the first page |
|---|---|---|
| `A.pdf` | 1372370 | B. D. Coleman and M. E. Gurtin, "Thermodynamics with internal state variables", J. Chem. Phys. 47 (1967) 597; DOI 10.1063/1.1711937 |
| `B.pdf` | 336003 | P. J. Chen and J. W. Nunziato, "Thermodynamic restrictions on the relaxation functions of the theory of heat conduction with finite wave speeds", Journal of Applied Mathematics and Physics (ZAMP) 25 (1974) 791 |
| `c.pdf` | 678066 | R. Stoneley, "Elastic waves at the surface of separation of two solids", Proc. R. Soc. Lond. A 106 (1924) 416-428; DOI 10.1098/rspa.1924.0079 |
| `d.pdf` | 321720 | C. H. Scholte, "The range of existence of Rayleigh and Stoneley waves", Mon. Not. R. Astron. Soc. Geophys. Suppl. 5 (1947) 120-126 |
| `e.pdf` | 394976 | G. J. Barnett, J. Lothe, S. D. Gavazza and M. J. P. Musgrave, "Considerations of the existence of interfacial (Stoneley) waves in bonded anisotropic elastic half-spaces", Proc. R. Soc. Lond. A 402 (1985) 153-166; DOI 10.1098/rspa.1985.0112 |
| `f.pdf` | 371912 | Lord Rayleigh, "On waves propagated along the plane surface of an elastic solid", Proc. Lond. Math. Soc. 17 (1885) 4-11. The same scan continues on p.11 with an unrelated paper by Griffiths; only pp.4-11 were used |
| `g.pdf` | 189820 | B. Collet, M. Destrade and G. A. Maugin, "Bleustein-Gulyaev waves in some functionally graded materials", European Journal of Mechanics A/Solids 25 (2006) 695-706; DOI 10.1016/j.euromechsol.2006.01.007 |
| `someproblemsofge00loveuoft.pdf` | 11242098 | A. E. H. Love, "Some Problems of Geodynamics", Cambridge University Press 1911; chapter XI, printed pp.160-174 |

- Green and Naghdi 1993 is not in `RIP7.zip`. It was read from the separate library file
  `B13-029__bf00044969.pdf`, also kept outside the repository at `/home/user/rip7/`
  (A. E. Green and P. M. Naghdi, "Thermoelasticity without energy dissipation",
  J. Elasticity 31 (1993) 189-208; DOI 10.1007/BF00044969; printed page = PDF page + 188).
- Each identity above is a first-page match of title, authors, journal, volume and page on
  the file itself. No paper is identified by a citing paper or by a filename.

## 2. Branch and base record

- Repository: `vipin-oss/le`; working branch `arena/a7a306f6-le` (the session branch).
- Batch 001 is already on the remote at `a73f498`, whose own base is `69db6c4`.
- Batch 002 is built from `origin/review-paper-v2` = `7ec50f8a757462b54c5c544e36e2bfdeb754b535`.
  Because `7ec50f8` is not an ancestor of the pushed tip and force-push is not permitted,
  the review-paper-v2 tip was taken in by a merge (commit `5801e18`) rather than by a rebase.
  That merge is the only commit in this batch that touches tracked non-deliverable files, and
  it changes only the three binaries that `review-paper-v2` itself changed
  (`paper_v2/main.pdf`, `paper_v2/overleaf_package.zip`, `paper_v2/paper_sources.zip`,
  each by a few hundred bytes); no `.tex`, `.bib` or script was edited by hand.
- Merge base of the batch with `origin/review-paper-v2` after the merge: `7ec50f8` (the
  review-paper-v2 tip is fully contained in the branch).
- Content commit for this batch and the push proof are recorded in section 9.

## 3. Files written in this batch

Only these files were created; nothing from batch 001 was rewritten.

| File | Records | Columns |
|---|---|---|
| `claim_check_batch_002.csv` | 5 | 11 |
| `layered_dossier_batch_002.csv` | 6 | 12 |
| `benchmark_candidates_batch_002.csv` | 12 | 9 |
| `evidence_pages_batch_002.csv` | 26 | 8 |
| `inventory_and_summary_batch_002.md` | - | this file |

## 4. Claim check (manuscript claims S1-S4)

Rows are keyed by claim and cited source, as in batch 001. Source page = printed page.

- **S1, Coleman and Gurtin 1967: NOT SUPPORTED.** The paper is about internal state
  variables, not memory functionals. Its second law is the Clausius-Duhem inequality (3.2,
  p.598) and it assumes the entropy flux to be q/theta (p.599, "When q/theta is regarded to
  be a flux of entropy due to heat flow"). No relaxation function appears in the text read
  (pp.597-599); the words "relaxation function" and "entropy flux" in the memory sense were
  not found there. It therefore cannot support a claim about the second law restricting a
  relaxation function and the entropy flux.
- **S1, Chen and Nunziato 1974: PARTLY SUPPORTED.** Theorems 1 and 2 (printed pp.795 and
  797, abstract p.798) restrict the relaxation functions: beta(0) >= 0, alpha(0) >= 0,
  alpha'(0) <= 0, and the equilibrium conductivity positive. The entropy-flux half of the
  claim is not supported: the paper works with the classical q/theta flux and makes no
  statement that the second law restricts the entropy flux itself.
- **S2, Chen and Nunziato 1974: SUPPORTED.** The initial value and the initial slope of the
  energy and heat-flux relaxation functions are constrained exactly as the claim says
  (Theorem 1(ii), p.795; Theorem 2, p.797; abstract, p.798).
- **S3, Green and Naghdi 1993: SUPPORTED.** Type II is described as involving "no
  dissipation of energy" (p.198) and "an absence of internal rate of production of entropy"
  (p.200); the system (3.15)-(3.16) is stated to "permit propagation of harmonic waves
  without damping" (p.202, after eq (3.17)).
- **S4, Green and Naghdi 1993: PARTLY SUPPORTED.** Items (2.16)-(2.17) on p.192 define
  h = theta k and q = theta p, so the flux used is heat flux divided by the temperature
  theta, not by the reference temperature theta0; p.203 repeats the notation as
  "the internal flux of entropy k (= h/theta)". In linearized type I,
  p = -(kappa/theta0) grad theta (2.38)3, p.197, which is q/theta0 to first order, so the
  "different from q/T0" reading is not visible in that limit; in type II the flux follows
  from the Pi-derivative of the free energy ((3.13)3, p.201) instead of a Fourier law. The
  manuscript sentence is defensible only with that theta-versus-theta0 qualification. This
  keeps batch 001's PARTLY SUPPORTED verdict; no source sentence asserts a difference from
  q/T0 in words.

All five rows carry verification level R3 (the cited page and equation were read) and a
quote of 25 words or fewer.

## 5. Layered-wave dossier (six sources, all R3)

- **Rayleigh 1885** (`f.pdf`, printed pp.4-11). Free plane surface of a homogeneous isotropic
  solid; traction-free conditions (20) and (22). Frequency equation (23),
  {2(f^2+g^2) - h^2}^2 = 4 r s (f^2+g^2), rationalised to (24). Incompressible case (25):
  k^6 - 8k^4 + 24k^2 - 16 = 0, root k^2 = .91275 (f^2+g^2); eq (32) k = .9554 f, s = .2954 f;
  speed .9554 sqrt(mu/rho). No general existence criterion is stated; complex roots of the
  squared equation are rejected because the real part of s has the wrong sign. Exponents
  were OCR-garbled in the scan and are reported as uncertain rather than reconstructed.
- **Love 1911** (book, printed pp.160-174). Layer of thickness T on a half-space with
  welded contact; secular equation (40) tan(sT) = mu' s'/(mu s), with (35) and (39) for s
  and s'. Reality requires b' > b; the two limits (b' as f -> 0, and b for s -> pi/2) are
  given. Printed example (section 187): fT = 6, s/f = .25, rho' = rho gives V = .9682 b and
  mu'/mu = 2.325. Section 175 gives the rough Rayleigh estimate 0.9 sqrt(mu/rho) for rock
  constants, about 3 km/s.
- **Stoneley 1924** (`c.pdf`, printed pp.416-428; image-only scan, read from rendered page
  images). Two welded half-spaces; interface conditions (11)-(16); four equations (19)-(22)
  and the 4 x 4 determinantal equation (23), p.418. Compressible case: quartic in c (p.419),
  reduction to the Rayleigh equation when rho2 = 0 (eq (2)), and an existence proof for the
  equal-media limit (eq (3), root between 0 and x = 1). Incompressible numerical case
  (p.422): rho1 = 8.2, rho2 = 3.2 gives 16889.6 c^6 - 4225.6 c^4 + 77796 c^2 - 51984 = 0 and
  c = .99287 beta; the complex root c^2/beta^2 = .75806 +- 1.57720i is rejected on the decay
  requirement. Page 423 gives two further parameter sets with no root, and two roots of the
  squared equation (11) that fail the unsquared equation.
- **Scholte 1947** (`d.pdf`, printed pp.120-126; poor text layer, Greek letters mangled).
  Stoneley boundary curves (1) and (2) in rho/rho', w = (beta'/beta)^2 and the two Poisson
  parameters; asymptotes 2.9117 and 3.2360 (p.122). Existence is stated region by region,
  with a rule of thumb that a Stoneley wave exists when beta > beta' for any density
  contrast, otherwise only for small rho/rho' or small T/L; a second Stoneley wave appears
  for T/L of order 4.4 or more. Equations are partly illegible in the text layer and are
  described in words, not reconstructed.
- **Barnett, Lothe, Gavazza and Musgrave 1985** (`e.pdf`, printed pp.153-166; image-only
  scan, pp.153-156 read from rendered page images). Bonded anisotropic half-spaces; partial
  waves (2.1)-(2.2); subsonic interval (2.3) 0 <= v <= theta_hat(1) <= theta_hat(2);
  continuous displacements (2.5) and tractions (2.7); existence equation (2.8)-(2.11),
  A U(1) = 0 with A = Z(1) + Z^T(2) hermitian and det A = 0 at v = v_s. The paper states
  that at most one subsonic interfacial mode can exist and that its speed exceeds the slower
  Rayleigh speed (p.154). Sections 3-5 (numerical implementation) were not read.
- **Collet 2006** (`g.pdf`, printed pp.695-706). Functionally graded piezoelectric half-space
  (class 6mm), profiles P0-P10 in Table 1 (p.696) with c0 = beta^2, 0, -beta^2.
  Attenuation factors (3.11); subsonic condition (3.12); interface fields (3.13)-(3.14);
  metalized and free-surface dispersion equations (3.15) and (3.17) for the exponential-type
  profiles and (3.20)-(3.21) for the others; speeds (3.16) and (3.18). Section 3.3
  (pp.700-701) gives PZT-4 numbers: v_m = 2256.85 m/s, v_f = 2592.65 m/s, K^2_S about .242,
  and for the exponential profile the decay bound beta/k < chi^2/(2 sqrt(1+chi^2)) = .2015
  with K^2_S rising to about .324 at beta/k = 0.2.

## 6. Benchmark candidates (12 rows)

B01-B05 Rayleigh 1885 (incompressible speed 0.9554 sqrt(mu/rho); k^2/(f^2+g^2) = .91275;
k = .9554 f with s = .2954 f; displacement node at .8659/f, i.e. .1378 lambda'; the printed
table of k/sqrt(f^2+g^2) against lambda/mu). B06-B07 Love 1911 (V = .9682 b at fT = 6,
s/f = .25, rho' = rho; the 0.9 sqrt(mu/rho) rock estimate, about 3 km/s). B08-B10 Stoneley
1924 (c = .99287 beta for rho1 = 8.2, rho2 = 3.2; the rejected complex root; the two
extraneous roots x^2 = .9042 and .93615). B11-B12 Collet 2006 (v_m, v_f and K^2_S for PZT-4;
the beta/k bound .2015).

Each row records the inputs as printed, the value as printed, the printed page, and how the
source obtained the value. No value was recomputed; units are those printed by the source.

## 7. Limitations, not-found items and disagreements

- Rayleigh 1885 and Scholte 1947 print no DOI; Love 1911 is a book without a DOI. These
  fields are "-" for that reason, not because a lookup failed.
- No general existence criterion is printed by Rayleigh 1885 or by Collet 2006; both are
  recorded as not found.
- Barnett et al. print no numerical example in the pages read (pp.153-156); the numerical
  sections were not read.
- `c.pdf` and `e.pdf` have no text layer and were read from page images rendered at 160 dpi;
  no OCR engine is available in this environment, so all transcription is manual reading of
  images. `d.pdf` has a text layer whose Greek letters are mangled; equations that could not
  be read reliably are described in words and marked illegible.
- Disagreement to report to the authors: the manuscript says the Green-Naghdi entropy flux
  differs from q/T0, whereas the paper's own definitions give q = theta p, so the flux is
  q/theta and coincides with q/theta0 to first order in linearized type I (S4 above).
- Disagreement to report: the manuscript's S1 attributes to Coleman and Gurtin 1967 a
  statement about memory laws and entropy-flux restrictions that this paper does not make.

## 8. Compliance checks run on the deliverables

- Encoding: every byte of the four CSV files and of this file is ASCII; a byte scan found
  zero non-ASCII or control bytes.
- CSV: `csv` module quoting, one record per row, no embedded newlines; column counts are
  11, 12, 9 and 8, matching the header lines used in batch 001.
- No Drive ID, URL, or folder name appears in any deliverable; filenames of the working
  copies only.
- No value, quote or page number was invented. Quote fields are 25 words or fewer and are
  marked as quotes in the wording field.
- No manuscript file was edited: `paper_v2/main.tex`, `paper_v2/main.bib`, the build scripts
  and the P3 blueprint are untouched, and no LaTeX compilation is claimed.

## 9. Push proof

- Content commit of this batch: `b938cefbf8953dbb664801de061ed16492ee239e`
  ("P3 evidence batch 002: claim check S1-S4, layered dossier, benchmark candidates,
  evidence pages").
- Base of the branch before this batch: `a73f498d0167c700355b183c5bb4fafc9d7fe902`
  (batch 001, pushed earlier) plus merge commit `5801e18` of `origin/review-paper-v2`
  (`7ec50f8a757462b54c5c544e36e2bfdeb754b535`).
- Push of the content commit was a fast-forward, `a73f498..b938cef`, on
  `arena/a7a306f6-le`; no force-push was used and `main` was not touched.
- `git ls-remote origin arena/a7a306f6-le` immediately after that push:

```
b938cefbf8953dbb664801de061ed16492ee239e	refs/heads/arena/a7a306f6-le
```

- This section is carried by a record commit made after the content commit, so the branch
  tip is one commit beyond `b938cef`. The final `git ls-remote` output for the tip was
  taken after that second push and is reported with the delivery message.
