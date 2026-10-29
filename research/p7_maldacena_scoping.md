# Arc-D: Maldacena BC-as-conditioning scoping (agent, 2026-07-12)

VERDICT: POSSIBLE WITH CAVEATS (not exact-mapping, not slogan-only).
Core calculation identified and closed-form: price the Gaussian-
regularized effect M_sigma against the 4th-order BD state.

## (a) Maldacena 1105.5632, per mode
- 4th-order theory: 4 solutions per k (e^{+-i|k|t}, t e^{+-i|k|t});
  graviton sector eq 3.2: eps_ij, epshat_ij (t-growing ghost partner),
  zeta_i.
- (BC2) positive frequency in far past = STATE PREP (BD-type), NOT
  part of the effect. (BC1) Neumann d/dt g|_{t=0} = 0 at the FUTURE
  boundary = the effect. 4 -> 2 (BC2) -> 1 (BC1); survivor = Einstein
  graviton (dS). Psi_Conformal[g, gdot=0] ~ Psi_BD-ren(g) TREE LEVEL.
  Partner rep is the NEGATIVE-norm Delta=2.
- Effect form (our translation): M_k = 1_graviton (x) |f_k=0><f_k=0|
  — IMPROPER (delta-normalized, p -> 0). Bona fide:
  M_sigma = exp(-f_k^2/(2 sigma^2)), 0 <= M_sigma <= 1; det M_sigma
  and p_sigma vanish TOGETHER; ratio sqrt(det M)/p can stay finite
  for Gaussian in-states. Bound at fixed sigma, then sigma -> 0.

## (b) HLZ 2306.13714 — two DISTINCT failures
- dS: survivor h = B_T(1 + ik eta)e^{-ik eta} (their eq 34) IS an
  Einstein solution (C_- branch of eq 35) but only half the Einstein
  data — over-selection. For post-selection reading this is a
  FEATURE (post-selection pins a state). Fatal only to classical
  general-solution equivalence claims.
- Minkowski: same survivor is NOT an Einstein solution; growing
  t e^{-ikt} piece survives INSIDE the selected state. M exists but
  its image is NOT ghost-free.
- ROOT CAUSE (our diagnosis): flat space = degenerate PU point
  (Jordan block); the 4-dim solution space does not split invariantly
  into graviton (x) partner, so writing M = 1 (x) E is singular at
  H_Lambda = 0. dS splits the degeneracy (Delta=3 vs Delta=2).
  PREDICTION to check: price degenerates (p -> 0 or saturation) as
  H_Lambda -> 0. If the bound detects the HLZ obstruction, that is an
  independent selling point.
- HLZ alternative BCs (eqs 56, 64, 67): a second effect M' (TWO
  future conditions, no in-state restriction) — price M vs M'.
- Excluded-set size: constant-counting only (4->1 vs Einstein 2;
  vectors killed, eq 73); no measure given.

## (c) Prior art
- "Future BC = post-selection" EXISTS generally — MUST CITE:
  Horowitz-Maldacena hep-th/0310281 (+ Gottesman-Preskill critique,
  Lloyd-Preskill JHEP 08(2014)126); Anastopoulos 2401.07662;
  Davies-Magueijo 2606.02514; TSVF/Gell-Mann-Hartle background.
- Ghost-removal prescriptions (not post-selection framed): Anselmi
  fakeons, Donoghue-Menezes, Salvio 1902.09557, Mannheim 2104.03708,
  2506.21400.
- INTERSECTION EMPTY (4 targeted sweeps): nobody reads Maldacena's
  Neumann BC as a survival-conditioned effect; nobody prices any
  ghost-removing BC. Scope claims to (i) ghost context + (ii) the
  quantitative bound.

## (d) Caveats (all five go in the paper)
1. Improper effect: regularize (Gaussian family), control sigma -> 0.
2. Indefinite norm: partner is negative-norm; must choose a
   positive-norm PU quantization FIRST (plugs into the left/right/
   silence taxonomy; declare the choice, answer may depend on it).
3. dS-only: Minkowski version is singular (Jordan block); treat
   H_Lambda -> 0 as the singular limit and check the bound detects it.
4. Don't double-count: positive-frequency = state prep; only Neumann
   = the effect. Also price HLZ's M'.
5. Tree level only (matches corpus scoping; beyond tree inherits
   Gottesman-Preskill interaction problem).
