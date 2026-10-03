# Phase 7 changelog

- `lang_audit.py` added: screening for internal vocabulary, banned hyperbole, duplication,
  orthography/mechanics, long sentences, unglossed acronyms; writes `lang_audit.json`.
- `patch_phase7_language.py` + two follow-up passes applied to the builders:
  internal vocabulary reworded in Sections 9.1-9.3 and in the companion's reproduction
  note; "robust" -> "insensitive" in the companion; prose unified to -ise (reference titles
  untouched); en dash in "Sections 5.1-5.3"; CV/F glossed at first use; four over-long
  clause chains split at clause boundaries; the Data availability grammar defect left by
  the Phase 6 placeholder substitution repaired.
- Documents rebuilt against `CODE_FREEZE_submission_2026_10_03i.json`; audit_tex,
  check_crossrefs, check_tex_commands and verify_pdf (manuscript and companion) all green;
  `lang_audit.py`: B 1->0, A printed-text hits 6->0 (remaining flags are `propagate`,
  `C11/C12`-style table labels and the deposited manifest filenames, all kept by choice).
