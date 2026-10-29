# Arc-A: Ilhan-Kovner mapping report (agent, 2026-07-12)

Verdict: MAPS PARTIALLY. Independently reproduced locally same day
(solve_ivp vs their Eq.58: gamma_r reldiff 1e-10..1e-11, blowup at
t = 2.828424 vs predicted t_c = 2^{3/2}/gamma_0 = 2.828427).

## Identification (title correction)
- arXiv:1403.4664 = "Conformal Gravity Redux: Ghost-turned-Tachyon",
  Ilhan & Kovner, PRD 89, 104015 (2014). (NOT the PU paper.)
- Companion: arXiv:1301.4879 = "Some Comments on Ghosts and Unitarity:
  The Pais-Uhlenbeck Oscillator Revisited", PRD 88, 044045 (2013) —
  THIS one carries the Jordan-block/non-diagonalizability statement.

## Their mechanism (1403.4664)
- Weyl^2 conformal gravity, k=0 (translationally invariant) sector,
  Eq.(1) action; Ostrogradsky via multiplier (Eq.20); H is a
  constraint combination => physical E = 0 (load-bearing).
- After GL-charge reduction, Eq.(56):
  H = -(1/18)[p1^2+p2^2] + (9/16)[g1^2+g2^2]^2
  Negative kinetic (ghost) + POSITIVE quartic induced by nonlinearity
  = anti-restoring force ("ghost-turned-tachyon").
- Exact zero-angular-momentum solution Eq.(58):
  gamma_r(t) = gamma_0/(1 -+ (gamma_0/2^{3/2}) t), singular at
  t_c = 2^{3/2}/gamma_0. EOM: gamma'' = +(1/4) gamma (gamma.gamma).
- Scaling: H = -p^2/(2 mbar) + lam (gamma^2)^2 =>
  t_c = (1/gamma_0) sqrt(mbar/(2 lam)); theirs mbar=9, lam=9/16.

## Mode-level reduction (our overlay, agent-derived + verified)
- Linearized k=0 sector: secular set {1,t,t^2,t^3} = maximally
  degenerate PU/Jordan block at omega1=omega2=0.
- Frozen-amplitude analysis: delta-gamma'' = +(3/4) gamma_b^2
  delta-gamma => omega = +/- i (sqrt(3)/2) gamma_b: the degenerate
  pair unfolds onto the IMAGINARY axis (complex/broken-PT direction),
  with self-consistent amplification (gamma_b grows) => finite-time
  singularity. Einstein m^2 unfolds the same block onto the REAL axis
  (Stelle). Sign dichotomy is exactly Arc-A's claim.

## Limits of the mapping (blunt, from agent — keep in paper 6)
(a) Their EP is at omega=0 (k=0 corner), not finite frequency;
    finite-k extrapolation is OURS, not theirs.
(b) Detuning is self-induced/amplitude-dependent (mu_eff^2 ~
    gamma_b^2), not spectral — phrase as "self-induced unfolding";
    NEVER as a linear-spectrum statement.
(c) EP/PU/Jordan language absent from 1403.4664 (our overlay);
    Jordan statement citable from 1301.4879 (H non-diagonalizable as
    Delta -> 0, normalizable state -> delta function, tied to broken
    emergent conformal symmetry).
(d) 1301.4879 also constructs a STABLE interacting particle-ghost
    system (unitary classically + quantum) => "interactions
    destabilize ghosts" is NOT universal; their stable example is the
    natural test of stability <=> real-direction unfolding.
(e) E=0 constraint is forced and used in Eq.(58); generic PU toys
    reproduce blowup qualitatively, not the exact coefficients.

## Reproduction recipe
g'' = 0.25 g (g.g), IC g=(gamma0,0), g'=(gamma0^2/2^{3/2},0);
expect gamma_r(t)=gamma0/(1-gamma0 t/2^{3/2}). Verified 2026-07-12.
