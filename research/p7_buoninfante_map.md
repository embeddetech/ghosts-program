# Arc-F: Buoninfante mapping — extraction + process-level image
(agent extraction + p7_buoninfante_map.py numerics, 2026-07-12)

LANE: OPEN (no PT/non-Hermitian/stochastic content in the trilogy;
quant-ph cross-listing signals foundations intent but content is
QFT-analytic). Live controversy: Anselmi-Briscese-Calcagni-Modesto
JHEP 05 (2025) 145 (arXiv:2503.01841) argue ONLY the fakeon
prescription is viable — cite both camps.

## The trilogy (exact citations)
- P1: "Remarks on ghost resonances," JHEP 02 (2025) 186,
  arXiv:2501.04097.
- P2: "Asymptotic Quantum Dynamics of Ghost Fields,"
  arXiv:2605.29047 (2026, preprint).
- P3: "Ghosts versus Unstable Particles in Quantum Field Theory,"
  arXiv:2606.18349 (2026, preprint).
CAVEAT (from extraction agent): equation numbers verified once via
HTML render; spot-check against PDFs before typesetting any
specific equation citation.

## Their discriminant (verbatim-anchored)
Same CC pole pair m^2 +- i m Gamma; ONLY the sheet differs:
ghost (a=-1) => FIRST (physical) sheet; ordinary unstable (a=+1) =>
second sheet, no first-sheet pole. KL structure (P3 Eq. 20, 26):
- a=+1: pure positive continuum, sum rule 1 = C: full norm
  transfer to continuum = complete decay.
- a=-1: continuum rho STILL POSITIVE; non-positivity enters via
  explicit NEGATIVE-residue CC-pole terms off the real axis
  (-Z Delta_F(M^2) - Z* Delta_F(M*^2) + positive continuum);
  sum rule Z + Z* = 1 + C: the one-particle component PERSISTS.
- ANTI-INSTABILITY (P2): the ghost does NOT decay (norm
  conservation in the indefinite metric forbids negative->positive
  norm evolution) and does NOT run away; instead MULTI-PARTICLE
  MASKING: overlap grows as sinh^2(Gamma t/2) (P3 Eq. 57; general
  P2 Eq. 88), timescale 2/Gamma; no free asymptotic one-particle
  ghost state. Microcausality: Feynman ghost stays CAUSAL. Vacuum
  decay: not discussed anywhere in the trilogy.

## Correction to our first Bochner statement
Our mapping's positivity-failure claim must be stated precisely:
the ghost's spectral CONTINUUM is positive; positive-definiteness
of A(t) fails through the DISCRETE negative-residue complex-pole
part. (Our numerics conclusion unchanged: no positive spectral
measure => |A| can exceed 1 => conditioning mandatory.)

## The process-level image (numerics: p7_buoninfante_map.py)
- 2nd sheet: positive measure => Bochner => |A(t)| <= 1 always
  (measured exactly 1.000000): UNCONDITIONED sub-stochastic
  survival process; transient backflow only. Unstable particles
  survive unconditioned.
- 1st sheet: max||e^{-iHt}|| = 1099: no unconditioned process
  exists; sigma_max conditioning MANDATORY => paper-1 terminal
  class (t_c 0.6400 vs closed form 0.6487; generator floor -2.603
  -> -2.618). Ghosts survive only conditioned.
- Sheet-crossing sweep: classifier crosses at the boundary exactly.

## The quantitative hook (verified 1e-14..1e-15)
Broken-dimer closed form |U_12(t)|^2 = (kappa/kt)^2 sinh^2(kt t).
With kt = Gamma/2 this IS Buoninfante's masking law
sinh^2(Gamma t/2) up to the prefactor: his multi-particle masking
overlap = the conditioned dimer's cross-population growth. His
"anti-instability" (nothing decays or grows in the indefinite
metric) = the closed-currency statement; our conditioning (growth
divided out exactly) = the beable-currency statement — CONSISTENT:
after conditioning nothing physical grows, matching anti-
instability. Two bookkeepings, same pole pair, with a shared
closed form.

## Taxonomy alignment (P1's (a;b,c) prescriptions vs our currencies)
- Feynman ghost (b=c=+1): negative odd-ghost norms, CAUSAL, first-
  sheet pair => our horn 3 / conditioning reading (no configuration
  sample space; conditioned open process).
- Anti-Feynman (b=c=-1): POSITIVE norms, ACAUSAL (reversed arrow)
  => structurally the Donoghue-Menezes Merlin route (DM NOT cited
  by Buoninfante; "Merlin" absent — the connection is ours to
  state, carefully): pay causal order, keep sample space = paper-4
  Table 1 row, now anchored in the (a;b,c) taxonomy.
- Fakeon (b=-c): Im[amplitude] = 0, purely virtual => the "silence"
  leg. Anselmi camp says only this survives; Buoninfante's
  anti-instability says Feynman ghost is consistent — the dispute
  is exactly a currency dispute; our trilemma prices both sides.

## For paper 7
Section: "The pole sheet is readable in the divisor." Contents:
Bochner proposition (with the precise discrete-part failure mode),
the sheet-crossing classifier, the sinh^2 identification, the
(a;b,c)-to-currency dictionary, DM connection stated as ours,
Anselmi-camp engagement, and the scope line: Buoninfante's masking
is an overlap statement in indefinite-metric QFT — our reading
adds the sample-space currency, claims nothing about his
finite-time resummation.
