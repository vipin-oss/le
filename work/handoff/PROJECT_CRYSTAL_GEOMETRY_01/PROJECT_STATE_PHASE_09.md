# PROJECT_STATE_PHASE_09 — Production execution (30 Sep 2026)

## Outcome
Confirmatory production matrix COMPLETE: 38 runs (Block A φ×χ 24, B Λ/size 11,
C feedback-off 1, D iso-control 2) at 96×48; 1039 CPU-s. Plus η_d sensitivity 4 runs
+ 192×96 T4 spot checks 2 runs (~250 CPU-s). All per-run JSON+NPZ in data/PROD/.

## Deviations from frozen plan (pre-registered D015, before outputs)
R=80a (plan 25a — plan's causal claim fails: longitudinal round trip 2.47 t_th < pulse
peak 2.5 t_th; 80a gives 8.1 t_th > 6 t_th window); pulse kept frozen (t0=2.5, tw=1.2);
QoI window t≤6 t_th; η_d=0.05 dynamic damping (undamped statics).

## Evidence
logs/production_v2.log; data/PROD/PRODUCTION_SUMMARY.json; per-run .json/.npz
(38+6 runs). Run cost ~13 s (96×48) / ~95 s (192×96).

## Limitations
V2-PARTIAL grid uncertainty applies to ellipse σ̂ (±6.8%); addressed by 192×96 spots.
η_d regularization documented with sensitivity.

## Exact next action
Analysis phase (Phase 10) — completed; see PROJECT_STATE_PHASE_13.md evidence map.
