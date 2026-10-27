#!/usr/bin/env python3
"""B23b — mutation harness for the two phase5 scripts under dispute.

A check that cannot fail is not a check. This harness injects four targeted
mutations into *copies* of the phase5 scripts and reports whether each mutant is
killed (non-zero exit) or survives. The originals are never modified.

Usage:
    python3 B23b_mutation_test.py <path-to-phase5-root>

Mutations
  1. drop the advective term E*v from the exact Eulerian flux in
     scripts/verify_classical_flux.py;
  2. flip the sign of the advective term there;
  3. flip the sign of the beta*T0*du/dt term in the Section 4 heat equation
     string assertion in verification/verify_classical_thermoelastic.py;
  4. drop the quadratic-remainder degree assertion in the same script
     (expected to SURVIVE: deleting a check cannot make the script fail;
      recorded to show the difference between a check and a gate).
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/user/b23b_src/phase5")
flux = (root / "scripts/verify_classical_flux.py").read_text()
therm = (root / "verification/verify_classical_thermoelastic.py").read_text()

MUTANTS = [
    ("flux: drop E*v from exact flux", "flux",
     "eulerian_flux = [q[j] - stress_power_flux[j] + advective_flux[j] for j in range(N)]",
     "eulerian_flux = [q[j] - stress_power_flux[j] for j in range(N)]"),
    ("flux: flip sign of E*v", "flux",
     "eulerian_flux = [q[j] - stress_power_flux[j] + advective_flux[j] for j in range(N)]",
     "eulerian_flux = [q[j] - stress_power_flux[j] - advective_flux[j] for j in range(N)]"),
    ("therm: flip sign of beta*T0*du/dt", "therm",
     r"\rho c_v \dot{T} = k\nabla^2 T - \beta T_0 \dot{u}_{i,i}",
     r"\rho c_v \dot{T} = k\nabla^2 T + \beta T_0 \dot{u}_{i,i}"),
    ("therm: delete quadratic-remainder degree assert", "therm",
     "assert sp.Poly(sp.expand(scaled_remainder), eps).degree() == 2",
     "assert True"),
]


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="b23b_mut_"))
    (tmp / "scripts").mkdir()
    (tmp / "verification").mkdir()
    (tmp / "master").symlink_to(root / "master", target_is_directory=True)
    killed = survived = unapplied = 0
    for name, target, old, new in MUTANTS:
        src = flux if target == "flux" else therm
        if old not in src:
            print(f"UNAPPLIED (motif missing): {name}")
            unapplied += 1
            continue
        rel = "scripts/verify_classical_flux.py" if target == "flux" else "verification/verify_classical_thermoelastic.py"
        (tmp / rel).write_text(src.replace(old, new))
        proc = subprocess.run([sys.executable, str(tmp / rel)], cwd=tmp, capture_output=True, text=True)
        if proc.returncode == 0:
            print(f"SURVIVED: {name}")
            survived += 1
        else:
            tail = (proc.stderr.strip().splitlines() or ["?"])[-1]
            print(f"KILLED  : {name}  [{tail[:70]}]")
            killed += 1
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"\nsummary: killed={killed} survived={survived} unapplied={unapplied}")
    # Mutants 1-3 must die for the checks to be load-bearing; mutant 4 is a
    # deliberate negative control and is expected to survive.
    return 0 if (killed == 3 and survived == 1 and unapplied == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
