# Step 4 - upgrading R0 rows whose source is in the folder

The brief: within the 667 rows of `claim_check_B_batch_001..018.csv`, find the rows whose verdict is
`SOURCE NOT AVAILABLE` or whose level is R0/R1 **and whose source is now in the folder**, and take
them to page level (R3). Start with the nine PARTLY/NOT rows, then the rest.

## Result

| | before Step 4 | after Step 4 |
|---|---|---|
| `SOURCE NOT AVAILABLE` | 278 | 219 |
| `PARTLY SUPPORTED` | 9 | 28 |
| `SUPPORTED` | 380 | 420 |
| R3 rows | 56 | **113** |
| R0 rows | 271 | 212 |

65 rows were re-checked. Every one of them names a source that is physically in the folder under a
filename that does not look like the bibliography key - which is exactly why they were still R0.

## The nine PARTLY/NOT rows first

| row | what it is | outcome |
|---|---|---|
| CB-0274 | Barak et al. 2023, Indian J. Phys. - atlas row A12 | **R2 -> R3**, abstract page read; stays PARTLY because "play a vital role" is the atlas's wording, not the paper's |
| CB-0301, CB-0303, CB-0307, CB-0309, CB-0311 | this manuscript's own figure scripts | not upgradable by reading a paper: the evidence is the repo's own `numbers_log.txt`, already R3, and the PARTLY verdict is about the manuscript's reading of the figure, not about a missing source |
| CB-0317 | the manuscript's own convergence pipeline | same: R3 on the repo's own log |
| CB-0344 | deliverable `P4_second_impl` | same: R3 on the repo's own report |
| CB-0490 | bibliography record (Gorenflo, Kilbas, Mainardi, Rogosin 2014) | stays R1: the record is the bibliography entry, and the book itself is not in the folder |

So one of the nine could be moved on a page (CB-0274); the other eight are not source-availability
rows at all and were left alone, with the reason stated here rather than silently rewritten.

## The 65 upgraded rows, by source

Each row's `source_page_or_equation` now names the page that was read. The quote in
`source_wording_max25words` is copied from that page.

| source file in the folder | rows | level reached |
|---|---|---|
| `rayleigh1885.pdf` | CB-0021, CB-0022, CB-0068, CB-0069, CB-0070 | R3 (p. 7, Eq. (25), root 0.91275) |
| `stoneley1924.pdf` | CB-0063, CB-0064, CB-0071, CB-0072 | **blocked: image-only scan** |
| `cowin1983.pdf` | CB-0153, CB-0155, CB-0250 | R3 (p. 125 abstract, p. 126 two longitudinal branches) |
| `10.1007@bf01302942.pdf` (Iesan 1986) | CB-0154, CB-0156, CB-0251 | R3 (p. 67) |
| `LAg_Nonlocal_WM-6.pdf` (Lazar 2022) | CB-0029, CB-0092, CB-0244 | R3 (p. 1) |
| `singh2020.pdf` | CB-0060, CB-0124, CB-0263, CB-0264 | R3/R2 (p. 1 abstract) |
| `0020-72252990050-x.pdf` (Eringen 1972) | CB-0081, CB-0110, CB-0238 | R3 (pp. 425-427) |
| `0020-72252990033-0.pdf` (Eringen 1974) | CB-0095, CB-0239 | R3 (p. 1063) |
| `aifantis1992.pdf` | CB-0085, CB-0240 | R3 (p. 1279) |
| `aifantis2003.pdf` | CB-0086 | R3 (p. 1) |
| `RAGJAKI.pdf` (Guyer-Krumhansl 1966) | CB-0103, CB-0214 | R3 (p. 766) |
| `mitra1995.pdf` | CB-0201, CB-0222 | R3 (p. 568) |
| `talbot1979.pdf` | CB-0001, CB-0177 | R3 (p. 97) |
| `2ndSoundSolids.pdf` (Chester 1963) | CB-0213 | R3 (pp. 2013-2015) |
| `jackson1970.pdf` | CB-0217 | R3 (pp. 26-28) |
| `huberman2019.pdf` | CB-0218 | R3 (p. 1, first release) |
| `cahill2003.pdf` | CB-0221 | R3 (pp. 793-795) |
| `P07_2023_IJP...pdf` (Barak 2023) | CB-0041, CB-0194 | R3 (p. 1) |
| `quintanilla2019.pdf` | CB-0232 | R3 (p. 1) |
| `g.pdf` (Collet, Destrade, Maugin 2006) | CB-0067, CB-0258 | R3 (p. 695) |
| `s10950-013-9401-4.pdf` (Sharma 2014) | CB-0256, CB-0257 | R3 (p. 61) |
| `1.1722351.pdf` (Biot 1956) | CB-0225 | R3 (p. 240) |
| `green1972.pdf` | CB-0227 | R3 (p. 1) |
| `green1991.pdf` | CB-0228 | **blocked: image-only scan** |
| `green1993.pdf` | CB-0229 | R3 (p. 189) |
| `nunziato1979.pdf` | CB-0152 | R3 (p. 1) |
| `tauchert1968.pdf` | CB-0151 | R3 (p. 37) |
| `lim2015.pdf` | CB-0079 | R3 (p. 1 accepted manuscript) |
| `abate2006.pdf` | CB-0178 | R3 (p. 408) |
| `ivanov1991.pdf` | CB-0036 | R3 (p. 563) |
| `d.pdf` (Scholte 1947) | CB-0065 | R3 (p. 1) |
| `e.pdf` (Barnett et al. 1985) | CB-0066 | **blocked: image-only scan** |
| `yang2018.pdf` | CB-0111, CB-0116 | PARTLY at R1 (front matter only) |
| `ma11071186.pdf` (Zhang 2018a) | CB-0259 | R3 (p. 1) |
| `ma11122363.pdf` (Zhang 2018b) | CB-0260 | R3 (p. 1) |
| `01495730151078171.pdf` (Abd-Alla 2001) | CB-0255 | R3 (p. 367) |
| `bf00052480.pdf` (Agarwal 1978) | CB-0254 | R3 (p. 1) |
| `P11_2023_HFF...pdf` (Gupta et al. 2023) | CB-0054 | R3 (p. 1) |

## The three things this pass could not do, stated plainly

1. **Six rows stay at SOURCE NOT AVAILABLE although the paper is in the folder** - CB-0063/0064/0071/0072
   (Stoneley 1924), CB-0066 (Barnett et al. 1985) and CB-0228 (Green-Naghdi 1991). All three files are
   image-only scans: the text extraction returns the JSTOR or Royal Society cover and nothing else. The
   identity of each paper is certain from that cover, and `found_in_library` now says `yes` for them, but
   no page can be read, so no statement is quoted. They need an OCR pass or a second copy.
2. **`yang2018.pdf` is a 500-page book.** Front matter only; the bars and the pyroelectric sign are in
   chapters that were not read. Those two rows are PARTLY at R1, not R3.
3. **Where the claim is a number from the body of a paper, the row says so.** Several rows were moved
   to R3 on the abstract but kept at PARTLY SUPPORTED, with the missing part named in the row: the
   critical angle of 28 degrees (CB-0264), the "almost unchanged" speed (CB-0258), the frequency trends
   (CB-0256, CB-0257), the exact Guyer-Krumhansl coefficient (CB-0103), the depth-2 equivalence of the
   exponential kernel (CB-0081), the branch counts (CB-0260), the LS-vs-GL characteristic equations
   (CB-0254). An abstract read is worth R2/R3 as a page, but it is not evidence for a number that is not
   on it.

## One correction that came out of this pass

`P11_2023_HFF_Reflection-Transmission-Plane-Waves-Interface-Ideal-Fluid.pdf` is **Gupta, Kumar, Kumar,
Pathania and Barak (2023), "Reflection/transmission of plane waves at the interface of an ideal fluid
and nonlocal piezothermoelastic medium"** - i.e. exactly the `Gupta2023IJNMF` paper that register row
CR175 cites. The Step-2 claim-check had recorded CR175 as SOURCE NOT AVAILABLE on the strength of the
*wrong* 2023 file (the Barak et al. solid-solid paper). Batch 005's row CC-0024 has been corrected to
SUPPORTED at R3 and CB-0054 upgraded on the same page. CR175 is therefore resolved; CR210 (Singh,
Sarkar and Pal, J. Heat Transfer 2020) remains genuinely absent.
