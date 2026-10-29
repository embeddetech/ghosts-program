# Scoping report: Does the [completions = boundary data / minimal process = dissipative choice] structure map onto black-hole horizon boundary conditions?

Date: 2026-07-11. Scope: 2-day gap map + go/no-go.
Framework being mapped: Torkelson 2026 explosion dictionary — for finite classical
time-of-flight to a boundary: (i) limit circle / loss of essential self-adjointness,
(ii) conservative dynamics requires self-adjoint-extension boundary data (U(1) or
channel-scrambling S-matrix at the boundary), (iii) the regulator-independent object
is the minimal Feller semigroup, which is sub-stochastic (explosive), (iv) ONE
time-of-flight integral simultaneously decides classical completeness, Weyl LP/LC,
and Feller boundary type (regular/exit/entrance/natural).

Method: literature sweep (arXiv + secondary), 14 targeted searches + abstract-level
fetches of the two closest papers. arXiv IDs verified by search hit unless marked
(check). Pre-arXiv classics cited by journal.

---

## 0. The one-sentence answer up front

The operator-theoretic half of the map (self-adjointness at horizons, dissipative =
non-self-adjoint) exists in scattered, mutually disconnected pieces. The
probabilistic half (Feller boundary classification of the horizon, minimal
sub-stochastic semigroup = membrane paradigm) appears to be GENUINELY ABSENT, and
nobody has run the time-of-flight integral as the single decider across the
classical / quantum / stochastic columns at a horizon. The horizon adds one
genuinely new axis our NRQM paper did not have: the boundary classification is
CLOCK-DEPENDENT (Killing time vs proper/hyperboloidal time), implemented
mathematically as a singular time change (lapse blowing up at the boundary), which
flips natural <-> exit. Verdict below: GO.

---

## 1. Self-adjointness / LP-LC at horizons

### Exists
- Wald 1980, "Dynamics in nonglobally hyperbolic, static space-times", J. Math.
  Phys. 21, 2802: dynamics in a static region with boundary defined by choosing a
  positive self-adjoint extension of the spatial operator A (Friedrichs as
  canonical choice). This is the template for "completions = boundary data".
- Ishibashi-Wald, gr-qc/0305012 (prescriptions II) and hep-th/0402184 (AdS, III):
  proved that ANY conservative, locally-correct, energy-conserving dynamics
  corresponds to SOME positive self-adjoint extension of A. This is the horizon-free
  general-relativity twin of our "conservative dynamics = extension choice" theorem;
  applied by them to naked singularities and to the timelike boundary of AdS, NOT to
  horizons.
- Horowitz-Marolf, gr-qc/9504028, "Quantum probes of spacetime singularities":
  spacetime is "quantum-mechanically singular" iff the spatial Klein-Gordon operator
  is not essentially self-adjoint on C_c^infty; applied to SINGULARITIES. Large
  follow-up literature (Konkowski-Helliwell reviews, e.g. gr-qc/0408036,
  1112.5488, 1302.3970) — all singularity-focused. The horizon appears in this
  literature only as the place where the static region ends, and the standard
  reduction to tortoise coordinate r_* gives a Schrodinger operator on
  (-inf, +inf) with V -> 0 exponentially as r_* -> -inf (horizon) and V -> m^2 at
  +inf: LIMIT POINT AT BOTH ENDS, essentially self-adjoint, no boundary data needed
  at the horizon for Killing-time evolution. This is standard folklore, stated in
  passing in many QNM and quantum-singularity papers (e.g. searches surface it in
  Kerr-Newman-AdS Dirac work 0803.2496 and stringy-BH work hep-th/0403046), but we
  found NO paper whose subject is "the horizon in the Weyl LP/LC classification"
  with the classification itself as the result.
- Dirac operators: Finster-Roken 1512.00761, 1606.01509 (and Kerr
  horizon-penetrating propagator work): essential self-adjointness proved even
  though the Hamiltonian FAILS TO BE ELLIPTIC exactly ON the horizon in
  Eddington-Finkelstein-type (horizon-crossing) coordinates. Notable: they must
  place a Dirichlet wall BEYOND the Cauchy horizon to shield the singularity —
  boundary data at the singularity, none at the event horizon.
- QNM boundary-condition literature, modern form: the hyperboloidal program.
  Warnick 1306.5760 (QNMs as genuine eigenvalues of a non-self-adjoint generator
  on AdS/asymptotically flat slicings); Jaramillo-Panosso Macedo-Al Sheikh
  2004.06434 (PRX 11, 031003: pseudospectrum, "non-normality associated with
  losses through spacetime boundaries"); Keldysh expansions 2412.02793; review/
  editorial stream in Frontiers (2409.00857 and the 2025 editorial). Explicit
  statement found in 2409.00857: in certain parameter ranges the analytically
  continued QNMs "do not belong within the domain of any self-adjoint extension".
  This community has fully internalized "dissipative boundary => non-self-adjoint
  generator" but does NOT use extension theory as a classification of physical
  completions, and has no probabilistic column at all.
- Balachandran-de Queiroz-Saa 1810.00020, "Near-horizon modes and self-adjoint
  extensions of the Schrodinger operator": (fetched in detail) tortoise-coordinate
  near-horizon operator on (-inf, x_max], deficiency indices (1,1), U(1) family of
  self-adjoint extensions, framed as "a generalization of the standard brick wall
  hypothesis". CRUCIAL READING: their extension lives at the OUTER edge x_max of
  the truncated near-horizon region, not at the horizon (the horizon end r_* = -inf
  stays limit point). They state the alpha-parameter's physical meaning is
  "still rather unclear" and that extensions are scattering/thermally equivalent.
  No dissipative alternative, no Feller/stochastic language.

### Close but different
- Near-horizon conformal quantum mechanics: Gupta-Sen hep-th/0204137 (one-parameter
  U(1) family e^{iz} of self-adjoint extensions of the near-horizon Klein-Gordon
  operator; bound states and near-horizon entropy from the extension choice);
  Camblong-Ordonez hep-th/0411008, 0709.2942 (inverse-square / conformal QM at the
  horizon, renormalization = extension choice, entropy holography; later
  multichannel-S-matrix framing of singular QM that "subsumes renormalization and
  self-adjoint extensions"). This is the closest thing to "the horizon needs a U(1)
  of boundary data" — but note the operator they treat is the near-horizon
  TRUNCATION in a radial variable where the horizon sits at finite distance
  (proper-distance-like variable, inverse-square potential at rho = 0: limit
  circle). The LC-at-finite-endpoint vs LP-at-r_*=-inf tension between this
  literature and the tortoise-coordinate folklore is exactly our "which clock /
  which Hilbert space" dichotomy, and NOBODY has reconciled the two as a
  classification statement.
- Hofmann-Schneider 1504.05580 "Classical versus quantum completeness" (+
  1710.07645): Schwarzschild BH geodesically incomplete but "quantum complete" —
  the classical/quantum completeness MISMATCH made explicit, but at the
  singularity, via ground-state wave functionals, not via LP/LC at the horizon and
  not with a stochastic column.

### Absent
- A theorem of the form: "for the exterior Killing-time generator the horizon is
  limit point (natural, no data); for horizon-adapted (hyperboloidal/PG/proper-
  time) descriptions the exterior generator is maximally dissipative and its
  conservative dilations are parameterized by boundary data at the (stretched)
  horizon" — i.e. the LP/LC-vs-clock dichotomy AS a theorem.
- Any use of the classical time-of-flight integral as the decider of horizon
  boundary type across the three columns.

## 2. Feller boundary classification at horizons

### Exists
- Nothing found that applies Feller's regular/exit/entrance/natural taxonomy to a
  black-hole horizon. Searches combining "Feller boundary classification" with
  horizon/diffusion terms return only mathematical-finance and population-genetics
  diffusions. This looks like a genuinely empty intersection.

### Close but different
- Franchi-Le Jan math/0410485 (Comm. Pure Appl. Math. 60 (2007) 187): the
  relativistic diffusion (Dudley diffusion, white-noise acceleration in PROPER
  time) on Schwarzschild; they prove capture by the black hole, hitting of the
  singularity, and even "regeneration through the singularity" — i.e. they compute
  hitting behavior of a proper-time-parameterized process at the horizon and
  singularity. This is the correct STOCHASTIC PROCESS but no Feller boundary
  classification of the horizon, no comparison of Killing-time vs proper-time
  parameterizations as a boundary-type flip, no operator/extension dictionary.
- Holographic Brownian motion: de Boer-Hubeny-Rangamani-Shigemori 0812.5112;
  Son-Teaney 0901.2338 (Langevin equation derived AT a stretched horizon; the
  horizon supplies noise and drag; trailing-string boundary condition at the
  horizon is purely ingoing = absorbing); Banerjee-Sathiapalan 1308.3352 (BTZ).
  Physically this IS "horizon = source of dissipation + noise for an exterior
  stochastic process", i.e. the fluctuation side of the membrane paradigm, but the
  boundary is treated by ingoing-wave prescription, never classified in Feller
  terms, and the [minimal sub-stochastic vs conservative extension] fork is never
  posed.
- Stochastic gravity: Hu-Verdaguer Living Rev. Rel. 11:3 (2008), 0802.0658
  (Einstein-Langevin, horizon fluctuations of evaporating BHs); recent
  "stochastic horizon structure" ringdown phenomenology (e.g. 2602.08034). Noise
  near horizons, but again no boundary-classification statement.
- Distantly related: "random walk cannot cross the horizon in Lorentzian
  signature" remarks in string-thermodynamics near horizons (1506.07798).

### Absent
- "The horizon is a natural Feller boundary for the exterior radial diffusion in
  Killing-time parameterization and an exit boundary in proper-time
  parameterization; the two are related by the singular time change with rate
  1/f(r) (the lapse), and Feller type is not invariant under singular time
  changes" — nobody has said this, and it is textbook-provable.

## 3. Membrane paradigm as dissipative effective boundary

### Exists
- Damour 1978-79 (horizon Ohm/Navier-Stokes); Thorne-Price-Macdonald 1986 (book);
  Parikh-Wilczek gr-qc/9712077 "An action for black hole membranes": the stretched
  horizon as a dissipative fluid membrane; dissipation arises because the exterior
  variational principle needs a surface term once the interior is discarded —
  i.e. the membrane paradigm IS, in words, "trace out the interior, get a
  dissipative (non-conservative) exterior description". Null-surface-limit
  subtleties: 2309.14036. QNM/membrane link: 0806.3797. Fluid-membrane survey:
  2411.06164.
- Susskind-Thorlacius-Uglum hep-th/9306069: stretched horizon + complementarity;
  dissipative properties from coarse-graining of horizon microphysics; unitarity
  for the distant observer requires keeping stretched-horizon degrees of freedom.

### Close but different
- The Parikh-Wilczek surface term is morally "boundary data at the stretched
  horizon restoring a good variational principle" — one renaming away from
  "extension data restoring conservativity". But no one states the fork
  [unitary completion with boundary data] vs [minimal dissipative description] as
  the horizon analogue of self-adjoint extensions vs minimal semigroup. The QNM
  hyperboloidal papers (2004.06434 etc.) have the dissipative-operator half; the
  near-horizon-extension papers (1810.00020, hep-th/0204137) have the boundary-data
  half; the membrane papers have the physics; the three literatures do not cite
  each other's structure.

### Absent
- "The membrane paradigm is the minimal (sub-stochastic / contractive) semigroup of
  the exterior problem; every unitary completion is a conservative dilation labeled
  by boundary data on the stretched horizon; regulator (wall-position) independence
  holds only for the minimal object." Absent as a statement and as a theorem.

## 4. Brick wall and horizon regularizations

### Exists
- 't Hooft, Nucl. Phys. B256 (1985) 727: Dirichlet wall at proper distance
  ~ Planck length; entropy diverges as wall -> horizon; wall position is an ad hoc
  cutoff. Follow-ups: hep-th/9607166, gr-qc/0303006, hep-th/0302183 (hidden
  degeneracy: entropy depends on ratio of an extra parameter to the wall cutoff),
  1307.5933 (brick walls in AdS/CFT), recent self-regularization claims 2508.20421.
- The extension-dependence reading EXISTS in nascent form: 1810.00020 explicitly
  calls its U(1) extension family "a generalization of the standard brick wall
  hypothesis" (Dirichlet at the wall = one point on the U(1)); Gupta-Sen and
  Camblong-Ordonez tie the near-horizon extension parameter to entropy.

### Absent
- The regulator-theory statement: "wall-position/extension dependence is exactly
  extension dependence in the Wald-Ishibashi sense; the regulator-INDEPENDENT
  object is not any extension but the minimal dissipative semigroup (membrane);
  entropy divergences are the price of demanding a conservative exterior." Also
  absent: any Feller-side reading (Dirichlet wall = elastic/absorbing barrier;
  wall removal = convergence to minimal process).

## 5. Black hole information: boundary data at the horizon?

### Exists
- Complementarity hep-th/9306069; AMPS firewalls 1207.3123; Horowitz-Maldacena
  final-state boundary condition hep-th/0310281 (data at the SINGULARITY, the
  clearest existing "extra boundary data restores unitarity" proposal);
  't Hooft antipodal boundary condition at the horizon, 1601.03447 (+ follow-ups):
  literally a channel-scrambling identification ON the horizon chosen to make
  evolution unitary — structurally our "S-matrix at the boundary" completion;
  Marolf 1212.6944 (boundary unitarity); Wikipedia-level consensus that the
  paradox is about whether the exterior description is unitary (conservative) or
  fundamentally lossy.

### Close but different
- The debate is conducted in terms of states, entanglement, and holography, not
  operator domains. "Horizon needs no data" (equivalence principle, natural
  boundary) vs "horizon carries data" (fuzzball/firewall/antipodal) is precisely a
  natural-boundary vs boundary-data dispute, but no one frames it as extension
  theory, and no one observes that BOTH can be right because the boundary type is
  clock-dependent.
- Vacuum-choice literature: Boulware / Unruh / Hartle-Hawking as "boundary
  conditions at the horizon and infinity" (e.g. 0810.5683; Boulware-vs-regularity
  2411.12617; Kay-Wald Phys. Rep. 207 (1991) 49 uniqueness of the Hartle-Hawking
  state on the bifurcate horizon). Important for honesty: this is boundary data at
  the level of STATES (two-point functions), not operator domains; a paper must
  cleanly separate the two or referees from QFT-in-CS will object.

### Absent
- Any statement of the form "complementarity vs information loss = self-adjoint
  extension vs minimal sub-stochastic semigroup, and the choice is invisible to
  exterior scattering observables" (note 1810.00020 already proved the
  extension-independence of exterior scattering/thermality — an unused lemma
  for exactly this argument).

## 6. Analogue gravity

### Exists
- Unruh PRL 46, 1351 (1981); Visser acoustic-BH kinematics; Barcelo-Liberati-Visser
  Living Review gr-qc/0505065. Dispersive regularization of the horizon: Jacobson
  PRD 44, 1731 (1991); Corley-Jacobson; Coutant-Parentani(-Finazzi) S-matrix with
  dispersion 1108.1821, two-regimes 1202.6015; mode conversion means the ingoing
  branch "bounces" without trans-Planckian blueshift — dispersion REPLACES the
  horizon boundary condition with bulk mode conversion (regulator analogy: brick
  wall :: dispersion). Dissipative UV completions: Parentani and collaborators
  (dissipative fields in dS/BH); "Dissipative processes at the acoustic horizon"
  2202.13790 (effective near-horizon shear/bulk viscosities — a fluid-mechanics
  membrane paradigm for acoustic holes). Black-hole lasers 0803.0669 (two horizons
  = cavity: boundary conditions produce instability). Observation: Steinhauer
  1510.00621 (check).

### Close but different
- The dispersive-vs-dissipative dichotomy in analogue Hawking radiation is a
  physical realization of [unitary completion vs lossy completion] of an
  incomplete effective description, and 2202.13790 even builds near-horizon
  viscosities. But no LP/LC, no Feller classification, no extension-theory
  framing; analogue QNM papers impose ingoing conditions by hand.

### Absent
- "Acoustic horizon = Feller natural boundary in lab time for the phonon
  Schrodinger problem; subluminal dispersion converts it to a regular/reflecting
  boundary; dissipation selects the minimal semigroup" — absent, and testable in
  principle in BEC analogues.

## 7. The time-of-flight inversion (Killing vs proper time)

### Exists (as folklore, never as operator theory)
- Every GR textbook: radial infall reaches the horizon in finite PROPER time while
  Schwarzschild (Killing) time diverges; the tortoise coordinate is the
  logarithmic divergence of the Killing-time-of-flight integral made into a
  coordinate. Our dictionary's time-of-flight integral T = int dr / v(r): with
  v from the Killing-time parameterization, T(horizon) = int dr / (f(r) ...)
  DIVERGES (log divergence at f -> 0); with proper-time parameterization it
  CONVERGES. This is the exact inversion the scoping question names.
- Operator shadows of the dichotomy exist piecemeal: (a) static exterior,
  Killing generator: LP at horizon, essentially self-adjoint (folklore + quantum-
  singularity literature); (b) horizon-penetrating slicings: generator non-elliptic
  ON the horizon (Finster-Roken 1512.00761) or non-self-adjoint with QNM
  eigenvalues (Warnick 1306.5760, hyperboloidal program); (c) proper-time
  stochastic processes cross, Killing-time ones do not (Franchi-Le Jan
  math/0410485 vs static-exterior diffusions).

### Absent
- NOBODY has assembled (a)+(b)+(c) into the statement: "the Killing-time vs
  proper-time dichotomy IS an operator-domain statement; the horizon's boundary
  classification (Weyl and Feller) is not slicing-invariant; the flip is a
  singular time change (multiplication of the generator by the lapse), and the
  same one-line time-of-flight integral decides which side of the dictionary you
  are on once you fix the clock." This is the sharpest empty slot found.

---

## (a) Gap map table

| # | Topic | Prior art (best) | Status | Our potential addition |
|---|-------|------------------|--------|------------------------|
| 1 | Self-adjointness at horizon | Wald 1980; Ishibashi-Wald gr-qc/0305012; folklore LP-at-horizon in r_*; 1810.00020 U(1) extensions (at wall, not horizon); Finster-Roken 1512.00761 | Pieces exist, never as a horizon LP/LC classification theorem | Prove the clock-dependent LP/LC dichotomy; reconcile tortoise-LP vs near-horizon-CQM-LC as Hilbert-space/clock choice |
| 2 | Feller classification at horizon | NONE on target; Franchi-Le Jan math/0410485 (proper-time diffusion crosses); Son-Teaney 0901.2338 (absorbing stretched horizon) | EMPTY intersection | Horizon = natural boundary (Killing clock) vs exit boundary (proper clock); singular-time-change theorem; classify all four Feller types vs surface gravity |
| 3 | Membrane paradigm as extension-vs-minimal fork | Parikh-Wilczek gr-qc/9712077 (surface term); STU hep-th/9306069; QNM non-self-adjoint program 2004.06434 | Physics exists; structural identification absent | Membrane = minimal sub-stochastic semigroup; unitary completions = conservative dilations with stretched-horizon data; wall-independence only for minimal object |
| 4 | Brick wall = extension dependence | 't Hooft 1985; 1810.00020 says "generalization of brick wall"; Gupta-Sen hep-th/0204137; Camblong-Ordonez hep-th/0411008 | Half-done (extension family known; regulator theory absent) | Wall-position dependence == extension dependence theorem; entropy divergence as price of conservativity; minimal process as the regulator-free object |
| 5 | Information paradox as boundary-data choice | 't Hooft antipodal 1601.03447 (S-matrix ON horizon); Horowitz-Maldacena hep-th/0310281 (data at singularity); AMPS 1207.3123 | Framings exist, never as extension theory | Complementarity vs loss = extension vs minimal semigroup; both consistent because boundary type is clock-dependent; scattering-equivalence of extensions (lemma already in 1810.00020) |
| 6 | Analogue horizons | BLV gr-qc/0505065; dispersion 1108.1821; dissipation 2202.13790 | Physics rich, classification absent | Feller/Weyl classification of acoustic horizons; dispersion = regularizing to regular boundary, dissipation = minimal process; lab-testable discriminator |
| 7 | Killing vs proper time as operator statement | Folklore + piecemeal (Warnick 1306.5760; Finster-Roken; Franchi-Le Jan) | Sharpest gap | One time-of-flight integral, clock as dial: the full dictionary flips columns under singular time change; horizon = the maximal-splitting example |

## (b) Sharpest candidate novel statements

S1 (Clock-dependence theorem / the flagship). For the Schwarzschild exterior radial
problem: in Killing time the horizon is Weyl limit point and a Feller NATURAL
boundary (infinite time-of-flight; essentially self-adjoint generator; conservative
minimal semigroup; no boundary data — this is WHY QNM "ingoing" conditions are
asymptotic regularity conditions, not extension parameters); in proper-time-adapted
(PG/Lemaitre/hyperboloidal) variables the time-of-flight is finite and the horizon
becomes an EXIT boundary for the exterior process, the exterior generator is only
maximally dissipative, and its minimal semigroup is sub-stochastic (mass = flux
through the horizon). The two pictures are related by a singular time change (rate =
lapse 1/f), under which Feller boundary type is not invariant. One time-of-flight
integral, evaluated with the clock as input, decides everything. (New axis relative
to our NRQM paper: there, the classification was absolute; at horizons it is
clock-relative. This also cleanly arbitrates the LP-tortoise vs LC-near-horizon-CQM
tension in the literature.)

S2 (Membrane paradigm = minimal process). The stretched-horizon membrane paradigm
(Damour; Thorne-Price-Macdonald; Parikh-Wilczek surface term) is the minimal
sub-stochastic (contractive) semigroup of the exterior problem in horizon-adapted
time: dissipative, regulator-independent, no boundary data. Unitary exterior
completions (brick-wall Dirichlet, Balachandran et al U(1) extensions, 't Hooft's
antipodal S-matrix) are precisely the conservative dilations, parameterized by
boundary data at the (stretched) horizon; they are mutually equivalent for exterior
scattering and thermality (extending the equivalence lemma of 1810.00020) but
inequivalent for entropy counting — which is exactly 't Hooft's wall dependence,
now identified as extension dependence.

S3 (Information-paradox dictionary entry). "Does the horizon need extra data?" has
a clock-indexed answer: NO in Killing time (natural boundary — complementarity's
exterior unitarity is the unique conservative dynamics, no choice involved), and
YES in infalling time IF one insists on exterior conservativity (any unitary
exterior description = a choice of dilation data at the horizon; refusing the
choice = accepting the sub-stochastic minimal description = information loss for
the exterior algebra). Firewall-type tensions arise from demanding a single
clock-independent classification that provably does not exist.

## (c) Honest already-done risk assessment

HIGH-RISK (do not claim as new):
- "Conservative dynamics = choice of self-adjoint extension" in static spacetimes:
  Wald 1980 + Ishibashi-Wald proved it in exactly our spirit. We must present our
  contribution as importing the STOCHASTIC column and the time-of-flight decider,
  citing them as the quantum column's owners.
- "Dissipative horizon boundary => non-self-adjoint generator": fully occupied by
  the hyperboloidal/pseudospectrum program (Warnick 1306.5760, Jaramillo et al
  2004.06434, 2409.00857 — the last even discusses domains of self-adjoint
  extensions). Any operator-only paper from us would be scooped-at-birth.
- "Near-horizon U(1) extension family / brick-wall generalization": Balachandran-
  de Queiroz-Saa 1810.00020 + Gupta-Sen + Camblong-Ordonez own the extension
  family and its entropy link.

MEDIUM-RISK:
- Someone in the hyperboloidal community connecting to Lindblad/dilation language:
  fragments of "QNMs as open-system resonances" exist; a full dilation-theory
  treatment could appear. Mitigation: our differentiator is the PROBABILISTIC
  (Feller/indivisible-process) column plus the classical time-of-flight decider —
  no visible competitor combines these.
- Franchi-Le Jan school proving horizon boundary-type statements for relativistic
  diffusions: they have the tools; 20 years of silence on Feller classification at
  the horizon suggests low appetite, but a math.PR referee will demand we engage
  their results.

LOW-RISK (the actual gap):
- Feller boundary classification of the horizon: no hits at all.
- The singular-time-change / clock-dependence theorem: no hits.
- Membrane paradigm = minimal semigroup: no hits.
- Triple-column dictionary at the horizon: no hits.

Caveats requiring care in the writeup: (i) state-choice (Boulware/Unruh/
Hartle-Hawking, Kay-Wald) vs domain-choice must be cleanly separated; (ii) PG time
is generated by the same Killing field (stationary, not static) — the honest
formulation of S1 must be in terms of the parameterization of the transported
process / the Hilbert-space and slicing pair, not naive "coordinate change"; the
diffusion (time-change) version is theorem-grade immediately, the QFT version needs
the hyperboloidal energy norms; (iii) our NRQM dictionary is 1D half-line
Schrodinger — the horizon reduction lands exactly there after partial waves, so the
machinery transfers, but the L^2 weight (measure f^{-1} dr) must be tracked
honestly since it is what moves the boundary between LP and LC.

## (d) Verdict

GO.

Reasoning: a paper-sized, referee-defensible gap exists and is reachable with
machinery we already possess. The core deliverables would be: (1) the
clock-dependence theorem S1, whose stochastic half is provable with textbook Feller
time-change arguments TODAY and whose quantum half reduces to known LP/LC facts
plus the hyperboloidal generator (citable rather than re-proved); (2) the
membrane-as-minimal-semigroup identification S2, which upgrades three disconnected
literatures (membrane, brick wall/extensions, QNM non-self-adjointness) into one
dictionary and reuses our sub-stochastic/minimal-process theorems verbatim; (3) the
information-paradox translation S3 as a discussion section, carefully fenced as
structural rather than a resolution. The differentiator that no competitor holds is
the Feller/indivisible-stochastic column and the single time-of-flight integral;
the operator column alone is crowded and must be cited, not claimed. Recommended
scope guard: stay at the level of a scalar field / radial diffusion on a fixed
Schwarzschild (and Rindler as warm-up) background; do not promise anything about
evaporation backreaction or holography. Estimated size: one focused paper
(Rindler + Schwarzschild), with the analogue-gravity discriminator (topic 6) as
either a section or a fast follow-up note.

## Citation confidence notes

Verified by direct search hit this session: gr-qc/9504028, gr-qc/0305012,
hep-th/0402184, gr-qc/0408036, 1810.00020 (fetched), hep-th/0204137,
hep-th/0411008, 0709.2942, 1306.5760, 2004.06434, 2409.00857, 2412.02793,
math/0410485, 0812.5112, 0901.2338, 1308.3352, gr-qc/9712077, 2309.14036,
0806.3797, 2411.06164, hep-th/9306069, hep-th/9607166, gr-qc/0303006,
hep-th/0302183, 1307.5933, 1601.03447, 1212.6944, hep-th/0310281 (memory,
standard), 1207.3123 (memory, standard), gr-qc/0505065, 1108.1821, 1202.6015,
2202.13790, 0803.0669, 1504.05580, 1710.07645, 1512.00761, 1606.01509,
2411.12617, 0810.5683, 0802.0658. Pre-arXiv: Wald JMP 21 2802 (1980); 't Hooft
NPB 256 727 (1985); Kay-Wald Phys. Rep. 207 49 (1991); Unruh PRL 46 1351 (1981);
Jacobson PRD 44 1731 (1991); Damour 1978-79; Thorne-Price-Macdonald 1986.
Flagged (check) = cite after verification: 1510.00621 (Steinhauer), 2602.08034,
2508.20421.
