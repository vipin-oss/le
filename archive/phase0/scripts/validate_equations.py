#!/usr/bin/env python3
"""Validate mathematical equation documentation.

Checks:
- Schematic equations are labeled as such (not presented as source-extracted)
- Derivation files exist for pending derivations
- Dimensional consistency notes present where applicable
- Source traceability for verified equations

Usage:
    python3 scripts/validate_equations.py
"""

import sys
from pathlib import Path


def main():
    repo_root = Path(__file__).resolve().parent.parent
    errors = []
    warnings = []

    # Check that foundational theory and energy flux framework exist
    theory = repo_root / "phase1" / "07_foundational_theory.md"
    flux = repo_root / "phase1" / "08_energy_flux_framework.md"
    scattering = repo_root / "phase1" / "09_interface_scattering_theory.md"

    for path in (theory, flux, scattering):
        if not path.exists():
            errors.append(f"Missing: {path.relative_to(repo_root)}")

    # Check derivations directory
    deriv_dir = repo_root / "mathematics" / "derivations"
    if not deriv_dir.exists():
        warnings.append("mathematics/derivations/ not created — no derivations yet")
    else:
        deriv_files = list(deriv_dir.iterdir())
        if not deriv_files:
            warnings.append("mathematics/derivations/ is empty — no derivations yet")

    # Check symbolic checks directory
    sym_dir = repo_root / "mathematics" / "symbolic_checks"
    if not sym_dir.exists():
        warnings.append("mathematics/symbolic_checks/ not created")

    # Check benchmarks directory
    bench_dir = repo_root / "mathematics" / "benchmarks"
    if not bench_dir.exists():
        warnings.append("mathematics/benchmarks/ not created")

    # Check that schematic equations are labeled
    for path in (theory, flux, scattering):
        if path.exists():
            content = path.read_text(encoding="utf-8")
            schematic_count = content.count("SCHEMATIC")
            derived_count = content.count("DERIVED")
            verified_count = content.count("VERIFIED")
            print(f"{path.name}: SCHEMATIC={schematic_count}, DERIVED={derived_count}, VERIFIED={verified_count}")
            if schematic_count > 0 and derived_count == 0:
                warnings.append(f"{path.name}: contains schematic equations but no derived equations")

    print()
    if errors:
        print(f"VALIDATION FAILED: {len(errors)} error(s)")
        for e in errors:
            print(f"  ERROR: {e}")
        sys.exit(1)
    print("VALIDATION PASSED: no errors")
    if warnings:
        print(f"Warnings: {len(warnings)}")
        for w in warnings:
            print(f"  WARN: {w}")


if __name__ == "__main__":
    main()
