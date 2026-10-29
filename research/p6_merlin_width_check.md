# Arc-E: Merlin-width EP-detuning check (agent, 2026-07-12)

VERDICT: (a) — the tree-level UV exceptional line SURVIVES loop
dressing. My tasking premise ("pole width => frequency detuning floor
|w1-w2| >= Gamma_M/2, EP never reached, cond saturates ~2w/Gamma") was
REFUTED by the agent's relativistic analysis — recorded as a caught
wrong hypothesis (detector: DM Eq (35) dispersion).

## Width formula (Donoghue-Menezes 1908.02416; eq numbers theirs)
- Correct source ID: 1908.02416 = "Unitarity, stability and loops of
  unstable ghosts", PRD 100, 105006 (2019). "Merlin" coined in its
  footnote 1. (1704.01533 = quartic propagators/confinement;
  2105.00898 = Ostrogradsky-overcome; 2112.01974 = overview, Merlin
  propagator -1/(q^2 - M^2 - i gamma) its Eq 16.)
- Eq (13): complex pole M^2 = m_r^2 + i gamma,
  gamma = xi^2 m_r^2 N_eff/(320 pi), residue -1. Eq (37):
  Gamma_M = xi^2 m_r N_eff/(320 pi) = N_eff m_2^3/(20 M_P^2).
- SHEET: pole at q^2 = m^2 + i gamma on the PHYSICAL sheet, unmodified
  Feynman contour (wrong side vs normal resonance) => microcausality
  violation ~1/Gamma_M; Lee-Wick spectral rep has the conjugate pair.
- DECISIVE: pole shift is Lorentz-invariant in q^2, NOT a fixed
  frequency broadening. Eq (35): omega_2(k) = sqrt(k^2+m^2+i gamma)
  ~ E_k + i gamma/(2E_k) — frequency width falls as 1/k (time
  dilation, decay factor exp(-gamma t/2E_q), Eq 36). Graviton branch
  omega_1 = k stays EXACTLY real (loop ~ q^4 ln q^2; massless pole
  unshifted, width-free).

## Arithmetic
- delta_loop(k) = (m^2/2k^2) sqrt(1+(gamma/m^2)^2);
  cond_loop(k) = (4k^2/m^2)[1+(gamma/m^2)^2]^{-1/2} — UNBOUNDED.
- gamma/m^2 = xi^2 N_eff/(320 pi); xi=1, N_eff~20 => 0.020;
  cond suppression 1 - 2e-4. Negligible.
- Approach-ray tilt: fixed phase arctan(gamma/m^2) ~ 1.1 deg,
  k-independent (xi^2 asymptotically free => tilt shrinks in UV).
- Naive fixed-Gamma foil (DISCLAIM in paper): cond_max ~ 640 pi/
  (xi^2 N_eff) ~ 1e2 (xi=1, N_eff=20); ~2e6 at m2 = 1e-3 M_P. This is
  what nonrelativistic-cavity intuition predicts; Eq (35) kills it.

## Qualitative addition for paper 4 (one paragraph, no retraction)
Dressed coalescing pair is (real, complex) at every finite k —
"resonance-EP" type (unequal linewidths, chiral detuning), not a
real-axis PT-type EP.

## Caveats
One-loop weak coupling (xi<<1, m2<<M_P; DM say numerics needed at
xi~O(1)); gamma ~ G q^4 off-shell growth => off-shell mode-matrix
claims at |q^2|>>m^2 stay tree-level-labeled (pole statement safe).

## Prior art
No Merlin/ghost-width x EP/Petermann connection in print — LANE OPEN.
Cite 1409.8450 (infinite-order EP, tree). Pre-submission skim:
"Remarks on ghost resonances", JHEP 02 (2025) 186.
