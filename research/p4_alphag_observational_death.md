# Can the observational death of alpha_g be extended to all |alpha_g| >~ 3e109?

Short answer: **conditionally yes — the fork itself does it, not a new observable.**
On face-value physics the observational death extends monotonically to the entire
line above (and below) the fitted value. On Mannheim physics *no* value of alpha_g
was ever observationally touched — including 3e109 — so the prior was always doing
the Mannheim-branch work, and its domain is the unbounded island. There is **no**
branch-independent observational closure of large alpha_g; but there is also no
branch on which large alpha_g is *observationally alive while 3e109 is dead*.
The audit's flagged asymmetry dissolves once the exclusion is routed through the
same fork the paper already uses, rather than pinned to the single fitted point.

## 1. Setup (conventions as in research/t4_vertex_conventions.md)

Pure Weyl gravity: I_W = -alpha_g Int C^2; TT propagator P2/(2 alpha_g k^4);
matter vertex (1/2) h T fixed by the sourced field equation 4 alpha_g W_mn = T_mn.
There is no Einstein-Hilbert term (forbidden by conformal symmetry) and no M_Pl.
Consequence used throughout:

> **(S) Every tree-level gravitational observable computed from known sources
> scales as 1/alpha_g.** The exchange amplitude is T (1/(2 alpha_g k^4)) T with
> the vertex and T_mn fixed by known physics; alpha_g enters only through the
> single propagator factor. FT[1/k^4] = -r/(8 pi), so the potential is purely
> LINEAR: V(r) = m1 m2 r/(16 pi alpha_g) x O(1). No 1/r term arises from point
> matching at ANY alpha_g (the beta term needs the r'^4 source moment, which
> vanishes for point sources — Yoon's point).

"Face-value branch" = the physics assumption that this flat-space inversion with
known T_mn is valid (the theory Flanagan and Yoon analyze). "Mannheim branch" =
the assumption that it is not (conformal source dressing by S(x); macroscopic
coefficients beta*, gamma* are uncomputable moments ~ (source moment)/alpha_g).

## 2. Face-value branch: the death IS monotone and covers the whole line

Under face-value physics the Mannheim–O'Brien fits *measure* alpha_g: the
per-solar-mass linear coefficient is gamma(alpha_g) = gamma* x (3e109/|alpha_g|),
with gamma* = 5.42e-41 cm^-1 the fitted value. Then:

- **|alpha_g| > 3e109 (the audit's flagged region):** gravity UNDERSHOOTS.
  The total face-value gravitational acceleration of the Earth by the Sun is the
  linear term only, gamma c^2/2 = 2.4e-20 (3e109/|alpha_g|) cm/s^2, versus the
  observed 0.59 cm/s^2 — a deficit of >= 19.4 decades already at the fitted
  value, growing linearly in |alpha_g|. There is no 1/r term and no dark-matter
  sector to substitute. The Sun could not bind the planets. Monotone: force
  ∝ 1/|alpha_g|, so once dead, deader. Additionally the rotation-curve linear
  term falls below gamma*, so the one phenomenological success that motivated
  the theory is lost by the factor |alpha_g|/3e109. Flanagan's Eddington
  parameter gamma_Edd = -1 + O(L^2 m_p^2/alpha_g) → -1 as alpha_g grows
  (observed: +1 +/- 2.3e-5, Cassini): the light-bending violation *saturates at
  maximal*, it is not relieved by large alpha_g.
- **3e12 <~ |alpha_g| < 3e109 (the stated window):** gravity OVERSHOOTS.
  gamma > gamma* by up to 97 decades; for |alpha_g| < ~1e90 the linear force per
  solar mass at 1 AU alone exceeds the entire observed solar attraction; for
  1e90 < |alpha_g| < 3e109 it contradicts the 138-galaxy fits that measure
  gamma*. Monotone downward.
- **|alpha_g| = 3e109 (the measured point):** the existing branch-A death
  (Flanagan/Yoon solar-system failures), as the paper already states.

So on face-value physics the observational exclusion covers the ENTIRE real
line, monotonically on both sides of the fitted point, with the fitted point
itself killed by the solar system. Nothing here is pinned to 3e109.

**Caveat (inherited, not new):** all of this stands or falls with the face-value
inversion, i.e. with exactly the analyses Mannheim disputes. That is the same
conditionality the paper's branch A already carries ("or, if Mannheim's
rebuttals stand, one is on the other branch"). The extension adds no new
vulnerability, but it cannot escape the fork.

## 3. Mannheim branch: no observable reaches alpha_g — honestly, the prior

If the flat-space inversion is rejected, beta*, gamma* constrain only the ratios
(source moment)/alpha_g; alpha_g decouples from ALL macroscopic gravity
(background cosmology too: FRW is conformally flat, C = 0, so alpha_g drops out
identically). The routes suggested for an independent observational closure all
fail, for structural reasons:

1. **Lambda_max ~ alpha_g^{2/5} growth is not a pathology.** Lambda_max is a
   CEILING (the largest Lorentz-violating cutoff consistent with the
   energy-density bound), not a prediction. Horn 1 needs only Lambda >~ meV
   (so the graviton sector survives at Eot-Wash-tested scales); at fixed
   physical Lambda the decay rate Gamma/V ~ c_ps Lambda^4/alpha_g^2 DECREASES
   in alpha_g. Larger alpha_g makes the ghost sector *less* visible, not more.
   No vacuum-decay, dispersion, or short-distance observable grows with
   alpha_g; the k^-4 sector is gravitational and SM physics is untouched.
2. **Rotation-curve overshoot has the wrong sign.** gamma ∝ 1/alpha_g:
   large alpha_g undershoots, and on the Mannheim branch even that is
   compensated by uncomputable source moments, so nothing overshoots.
3. **The moment-naturalness restatement.** Matching the OBSERVED beta*
   (= G M_sun/c^2) and gamma* with |alpha_g| = 10^(109+N) forces every
   nucleon's r^2- and r^4-weighted gravitational source moments to exceed
   their hadronic-scale values (m_p r_N^k) by the same N decades, with no
   mechanism — the only in-print-derivable anchor is 3e109 (both matching
   routes in the conventions sheet). This is a sharper, more physical way to
   *state* the prior (fine-tuning of the coupling = fine-tuning of the
   moments), but Mannheim's framework declines to compute the moments, so it
   is NOT an observational exclusion. It remains a naturalness argument.

Conclusion for this branch: large alpha_g genuinely evades observation at this
level of analysis. The island is closed by the prior — as it already was for
the window; the point is that the prior's domain is |alpha_g| >~ 3e12
**unbounded above**, not the bounded interval currently printed.

## 4. Recommended paper fix (no new physics claims required)

Replace the bounded-island sentence ("couplings in the window
3e12 <~ |alpha_g| << 1e109 would evade both branches") with the fork-complete
statement:

- The island of couplings evading the energy-density bound is
  |alpha_g| >~ 3e12, **unbounded above**.
- On face-value physics the entire island (indeed the entire alpha_g line) is
  observationally dead, monotonically: below 3e109 the linear potential
  overshoots (by up to 97 decades; below ~1e90 the per-solar-mass linear force
  at 1 AU exceeds the Sun's entire observed attraction), at 3e109 the
  solar-system failures of branch A apply, and above 3e109 the theory's total
  gravitational force — 1/r-free and ∝ 1/alpha_g — undershoots the observed
  solar attraction by >= 19 decades and loses the rotation curves it was built
  to fit; Flanagan's gamma_Edd → -1 is maximally violated in the large-alpha_g
  limit.
- On Mannheim physics alpha_g decouples from all macroscopic gravity, so no
  observation reaches it anywhere on the island (nor at 3e109 — that is what
  his rebuttals assert); there the island, now unbounded, is closed by the
  stated naturalness prior, equivalently by moment-naturalness: |alpha_g| tens
  of decades above the only derivable anchor requires nucleon source moments
  tens of decades above their hadronic values, with no mechanism.

Net: horn 1 still fails on both branches; the unboundedness is repaired by
routing the large-alpha_g region through the same fork, with the face-value
side now carrying an explicit monotone scaling instead of a single-point death.

## 5. Optional strengthener (VERIFY BEFORE CITING — from memory, not checked)

Caprini, Hoelscher & Schwarz, PRD 98, 084002 (2018) (arXiv:1806.10940) analyze
gravitational waves from binaries in conformal gravity and find the emission
incompatible with observed events for rotation-curve-fit parameters. If it
holds up on reading, GW emission ∝ 1/alpha_g gives another monotone face-value
observable (Hulse–Taylor orbital decay at 0.1% + LIGO amplitudes), worsening
with alpha_g. Do NOT cite without fetching and checking the actual scaling and
conclusions; it is also subject to the same face-value caveat.

## Numbers used (checked against scripts/t4_rate_ladder.py conventions)

- Lambda_max = (alpha_g^2 rho_cr/(t0 c_ps))^{1/5}; meV crossing at
  |alpha_g| = 3.3e12; 5e7 M_Pl at 3e109. (Reproduced.)
- gamma* c^2/2 = 2.44e-20 cm/s^2 per M_sun; observed a_sun(1 AU) = 0.593
  cm/s^2; deficit 10^19.4. Overshoot crossover (linear force alone exceeds
  observed solar attraction at 1 AU): |alpha_g| ~ 1.2e90.
