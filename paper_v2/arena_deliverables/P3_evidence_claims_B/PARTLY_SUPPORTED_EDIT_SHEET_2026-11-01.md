# The 34 partly supported claims: one row per decision

`claim_register.csv` carries 224 claims. Seventy-four are SUPPORTED, five NOT SUPPORTED,
111 SOURCE NOT AVAILABLE - and **34 PARTLY SUPPORTED**. That last group is the one that cannot
wait, because each of those sentences is in the manuscript *and* rests on a source that was
actually read: the gap is between what the paper says and what the sentence claims, so it is
fixable today without any new reading in most cases.

This sheet does not re-decide any verdict. It takes the register's recorded finding for each of
the 34 and turns it into a decision: what the gap is, what to do about it, what would close it,
and whether it is mandatory or optional. **21 rows are mandatory, 13 optional.**

| gap | rows |
|---|---|
| `GAP-ATTRIB` the manuscript attributes a specific result to this source; the passage read states something narrower or different | 12 |
| `GAP-RECORD` the register read this source and found it narrower than the sentence; the note does not reduce the gap to one clause | 12 |
| `GAP-PAGE` the passage that decides the sentence was not read (front matter only, or the printed pages were not retrievable) | 4 |
| `GAP-QUOTE` the literal words are presented as the source's; the register did not find them in the source | 2 |
| `GAP-BIB` the bibliographic detail does not match the supplied file (name and content disagree) | 2 |
| `GAP-SOURCE` a source co-cited in the sentence was not supplied, so the sentence cannot be checked as a whole | 1 |
| `GAP-NAME` the manuscript uses a later or looser name for what the source does state | 1 |

| action | rows |
|---|---|
| `ACT-SOFTEN` narrow the sentence to what the register records as stated; do not strengthen the attribution | 12 |
| `ACT-AUTHOR` author decision; the register's own note is the evidence and no rewording is proposed here | 12 |
| `ACT-READ` read the named page before the sentence is kept as written | 6 |
| `ACT-BIBFIX` check the bibliography entry against the supplied file and correct whichever of the two is wrong | 2 |
| `ACT-MARK` mark the unsupplied co-citations as unread in the manuscript (no new request is made here; what to supply is the author's call) | 1 |
| `ACT-NONE` no change needed; record the naming point where the register already records it | 1 |

## What each gap means

- `GAP-ATTRIB` - the manuscript attributes a specific result to this source; the passage read states something narrower or different
- `GAP-PAGE` - the passage that decides the sentence was not read (front matter only, or the printed pages were not retrievable)
- `GAP-SOURCE` - a source co-cited in the sentence was not supplied, so the sentence cannot be checked as a whole
- `GAP-BIB` - the bibliographic detail does not match the supplied file (name and content disagree)
- `GAP-QUOTE` - the literal words are presented as the source's; the register did not find them in the source
- `GAP-NAME` - the manuscript uses a later or looser name for what the source does state
- `GAP-RECORD` - the register read this source and found it narrower than the sentence; the note does not reduce the gap to one clause

## The rows

| claim | level | source | gap | action | priority |
|---|---|---|---|---|---|
| CR007 | R3 | Rukolaine2014 | GAP-ATTRIB | ACT-SOFTEN | mandatory |
| CR024 | R3 | MooreGibson1960 | GAP-ATTRIB | ACT-SOFTEN | mandatory |
| CR032 | V1 | Aldandani2026 | GAP-ATTRIB | ACT-READ | mandatory |
| CR034 | V1 | Youssef2006 | GAP-ATTRIB | ACT-READ | mandatory |
| CR035 | R3 | Prasad2020 | GAP-SOURCE | ACT-MARK | mandatory |
| CR037 | V1 | Bassiouny2020 | GAP-ATTRIB | ACT-SOFTEN | mandatory |
| CR040 | R3 | Povstenko2004 | GAP-RECORD | ACT-AUTHOR | optional |
| CR045 | V1 | Ezzat2011 | GAP-ATTRIB | ACT-SOFTEN | mandatory |
| CR046 | V1 | GorenfloKilbasMainardiRogosin2014 | GAP-PAGE | ACT-READ | mandatory |
| CR063 | R3 | Povstenko2004 | GAP-RECORD | ACT-AUTHOR | optional |
| CR064 | R3 | Povstenko2007 | GAP-RECORD | ACT-AUTHOR | optional |
| CR065 | R3 | Povstenko2009 | GAP-RECORD | ACT-AUTHOR | optional |
| CR071 | V1 | Sur2025 | GAP-ATTRIB | ACT-SOFTEN | mandatory |
| CR076 | V1 | Ezzat2015 | GAP-ATTRIB | ACT-SOFTEN | mandatory |
| CR086 | R3 | Green and Naghdi 1993 | GAP-PAGE | ACT-READ | mandatory |
| CR088 | R3 | Chen and Nunziato 1974 | GAP-ATTRIB | ACT-SOFTEN | mandatory |
| CR091 | R3 | Green and Naghdi 1993 | GAP-QUOTE | ACT-SOFTEN | mandatory |
| CR099 | R3 | Lord and Shulman 1967 | GAP-RECORD | ACT-AUTHOR | optional |
| CR100 | R3 | Green and Lindsay 1972 | GAP-NAME | ACT-NONE | optional |
| CR104 | R3 | Green and Naghdi 1991 (Proc. R. Soc. Lond. A 432, 171) | GAP-RECORD | ACT-AUTHOR | optional |
| CR105 | R3 | Green and Naghdi 1992 (J. Thermal Stresses 15, 253) | GAP-RECORD | ACT-AUTHOR | optional |
| CR115 | R3 | Chirita, D'Apice and Zampoli 2016 (Int. J. Heat Mass Transfer) | GAP-ATTRIB | ACT-SOFTEN | mandatory |
| CR116 | R3 | Chirita, Ciarletta and Tibullo 2017 (Int. J. Heat Mass Transfer) | GAP-BIB | ACT-BIBFIX | mandatory |
| CR118 | R3 | Moore and Gibson 1960 (J. Aerospace Sci.) | GAP-RECORD | ACT-AUTHOR | optional |
| CR129 | R3 | Chirita, D'Apice and Zampoli 2016 (Int. J. Heat Mass Transfer) | GAP-ATTRIB | ACT-SOFTEN | mandatory |
| CR130 | R3 | Chirita, Ciarletta and Tibullo 2017 (Int. J. Heat Mass Transfer) | GAP-BIB | ACT-BIBFIX | mandatory |
| CR135 | R3 | Marotti de Sciarra 2013 (J. Engineering 2013, 516462) | GAP-RECORD | ACT-AUTHOR | optional |
| CR138 | R3 | Chandrasekharaiah 1996 (J. Thermal Stresses, uniqueness theorem for type II) | GAP-ATTRIB | ACT-SOFTEN | mandatory |
| CR140 | R3 | Zener 1937 (Phys. Rev. 52, 230) | GAP-QUOTE | ACT-SOFTEN | mandatory |
| CR141 | R3 | Zener 1937 (Phys. Rev. 52, 230) | GAP-PAGE | ACT-READ | mandatory |
| CR143 | R3 | Yang, Cheng, Cong, Jin and Borjalilou 2021 (Waves in Random and Complex Media) | GAP-RECORD | ACT-AUTHOR | optional |
| CR164 | R1 - cover page only; body not machine-readable, so no body statement is quoted | Lamb 1917 (Proc. R. Soc. Lond. A 93) | GAP-PAGE | ACT-READ | mandatory |
| CR183 | R3 | Eringen 1983 (J. Appl. Phys. 54) | GAP-RECORD | ACT-AUTHOR | optional |
| CR206 | R3 | Nunziato and Cowin 1979 (Arch. Rational Mech. Anal. 72) | GAP-RECORD | ACT-AUTHOR | optional |

## What this sheet does *not* do

- It does not change any verdict, and `check_partly_sheet.py` proves that: every claim here is
  still `PARTLY SUPPORTED` in the register.
- It does not write new physics sentences. Where a reworded sentence would help, the suggestion
  is to *keep the source's own words* and drop the rest of the attribution; everything else is
  marked as the author's decision.
- It does not ask for more papers. Two rows (`CR035`, `CR138`) fail only because a co-cited source
  was never supplied; the action there is to mark those co-citations as unread, not to request them.
- It does not touch the `.tex` files: this repository does not contain them.

Full detail - the sentence as written, the register's recorded finding, the gap, the action, the
suggestion and what would close it - is in the CSV beside this file:
`PARTLY_SUPPORTED_EDIT_SHEET_2026-11-01.csv`, 34 rows, 14 columns.
