# T1 Literature Triage: Conditioned-Signal TV vs Survival Probability Trade-off

Date: 2026-07-11. Scope: is the conjectured universal trade-off -- TV between Bob's
POST-SELECTED (survival-conditioned) marginals bounded by a function of Alice's
survival probabilities p1, p2 -- already published? Broken-PT dimers on a Bell state
conjectured extremal, TV(inf) = sqrt(1-(s/sin theta)^2), survival ~ exp(-2 sin(theta) t).

All searches run 2026-07-11 via web search + arXiv fetches. ASCII only.

---

## (a) VERDICT PER QUESTION

### Q1. Exact trade-off (conditioned distinguishability vs post-selection success): CLEAR
No paper found that states or proves a bound of the form
TV(sigma_1^B|survive, sigma_2^B|survive) <= f(p1, p2 [, rho_AB])
in the bipartite/no-signaling setting where Alice's local trace-nonincreasing CP map
choice is the "signal" and Bob's conditioned marginal is the receiver variable.
Closest misses:
- Regula, Lami, Wilde, "Postselected quantum hypothesis testing", arXiv:2209.10550
  (IEEE Trans. Inf. Theory 69, 3453 (2023)): postselected discrimination of two states
  held IN HAND (measurement with an abstain outcome); asymptotic error exponents given
  by Hilbert projective / Thompson metrics. Single-system, asymptotic, no remote
  conditioning, no bipartite marginal constraint. Trade-off is error-exponent vs
  copies, not TV vs success probability.
- Gavorova, "Notes on distinguishability of postselected computations",
  arXiv:2011.08487: defines trace-induced and diamond distances for postselected
  computations; shows convexity/contractivity/subadditivity FAIL for postselected
  maps, proves weaker versions via a "conversion lemma". Computation-oriented; no
  bipartite signal bound, no explicit TV-vs-p function.
- Qian, Gagatsos, "Heralded enhancement in quantum state discrimination",
  arXiv:2506.14105: post-selection can beat Helstrom conditionally while the average
  obeys Helstrom; explicitly NO quantitative bound of conditional error vs heralding
  probability, and no bipartite/no-signaling setting.
- "Postselected communication over quantum channels", Ji, Regula, Wilde(?),
  arXiv:2308.02583: postselected capacities; channel-coding setting, not our quantity.
- No-signaling used as an AXIOM to bound discrimination (e.g. Hwang/Bae,
  arXiv:0708.3909 "No-signaling bound on quantum state discrimination"; also
  no-signaling bounds for cloning/metrology, arXiv:1412.3361): direction is reversed
  (no-signaling => Helstrom-type bounds on unconditioned tasks). Nobody inverts it into
  a quantitative bound on the CONDITIONED signal.

### Q2. Steering / max TV subject to p_i sigma_i <= rho_B: CLEAR (tools PARTIAL)
The constraint set is fully characterized in the literature (Schrodinger-HJW/GHJW:
an ensemble member (p, sigma) is remotely preparable iff p sigma <= rho_B; steering
review with SDP formulations: Cavalcanti, Skrzypczyk, arXiv:1604.00501). The steering
ellipsoid (Jevtic, Pusey, Jennings, Rudolph, arXiv:1303.4724, PRL 113, 020402 (2014);
also Verstraete's thesis 2002) gives the GEOMETRY of steered Bloch vectors for two
qubits, but the ellipsoid literature does not weight points by their preparation
probability, and no paper found solves or even poses
  max TV(sigma_1, sigma_2)  s.t.  p_i sigma_i <= rho_B  (i = 1,2)
as a theorem with a closed-form value. Related-but-different published quantities:
- steering-degree/steerability SDPs (trace-distance to LHS assemblages,
  arXiv:1709.06703, arXiv:2311.10552) -- distance to UNSTEERABLE models, not
  pairwise distinguishability of two steered members at fixed weight.
- steering <=> subchannel discrimination advantage (Piani-Watrous; experiment
  npj QI 4, 41 (2018)) -- again a different functional.
The specific optimization is an SDP whose dual involves D_max(sigma_i || rho_B)
(note p <= exp(-D_max(sigma||rho_B)) is exactly HJW feasibility), so the machinery
exists, the theorem does not. Verdict: the optimization problem itself appears OPEN
in print; publishing its solution + extremal family is a real increment.

### Q3. Post-selected metrology bounds: PARTIAL (no preemption)
- Arvidsson-Shukur, Yunger Halpern, Lepage, Lasek, Barnes, Lloyd, "Quantum advantage
  in postselected metrology", arXiv:1903.02563 (Nat. Commun. 11, 3775 (2020)): the
  postselected Fisher information times the postselection probability
  (information-cost rate) is bounded classically and can exceed the bound iff the
  doubly extended Kirkwood-Dirac quasiprobability has negativity. This IS a
  "conditioned information vs success probability" trade-off -- but for LOCAL
  parameter estimation (Fisher information), single system, and the bound is
  contextuality-flavored, not a TV bound and not bipartite/no-signaling.
- Combes, Ferrie, Jiang, Caves, "Quantum limits on postselected, probabilistic
  quantum metrology", PRA 89, 052117 (2014) (companion: Ferrie, Combes,
  arXiv:1307.4016; Knee-Combes-Ferrie-Gauger "weak-value amplification: state of
  play"): postselection cannot increase Fisher information ABOUT the parameter beyond
  the unpostselected optimum once the discarded events are accounted; p*F_post <= F.
- Jenne, Arvidsson-Shukur (arXiv:2011.04638 "Unbounded and lossless compression of
  multiparameter metrological information" / related postselected-metrology
  follow-ups): filters compress Fisher information into few survivors at rate limited
  by quasiprobability negativity.
Implication for us: these results bound p * (information) and are LOCAL (derivative
at a point); a TV bound is a GLOBAL two-point statement. Fisher bounds do not imply a
TV-vs-p bound (integration of the QFI bound along a path gives Bures-angle bounds on
the states Alice HOLDS, not on Bob's conditioned marginals). Cite as analogy; not
preemption. Note: our TV bound at p -> family of Fisher corollaries; worth one remark
in the paper.

### Q4. PT-specific literature: CLEAR on the quantitative bound
The controversy chain:
- Lee, Hsieh, Flammia, Lee (LHFL), "Local PT symmetry violates the no-signaling
  principle", PRL 112, 130404 (2014), arXiv:1312.3395.
- Tang et al., "Experimental investigation of the no-signalling principle in
  parity-time symmetric theory using an open quantum system", Nat. Photonics 10, 642
  (2016): embeds PT dynamics in an open (lossy) system; signal disappears
  unconditionally, appears only under post-selection; experiment, no bound.
- Brody, "Consistency of PT-symmetric quantum mechanics", J. Phys. A 49, 10LT03
  (2016): with the correct (CPT) inner product/Hilbert-space geometry there is no
  violation; no bound on the conditioned signal.
- Japaridze, Pokhrel, Wang, "No-signaling principle and Bell inequality in
  PT-symmetric quantum mechanics", arXiv:1703.03529: no-signaling preserved in the
  CPT framework; CHSH reproduced.
- Ju, Miranowicz, Chen, Nori, "Non-Hermitian Hamiltonians and no-go theorems in
  quantum information", PRA 100, 062118 (2019), arXiv:1906.08071 (+ Ju et al. PRA
  2022 "Einstein's quantum elevator", arXiv:2107.03864): embedding/metric formalism
  restores all no-go theorems; the apparent violation is an artifact of reading
  non-Hermitian states with the wrong metric.
- Kumari, Sen, "Local PT-symmetric evolutions on separable states and violation of
  no-signaling", arXiv:2202.02744 (2022): the naive-inner-product violation occurs
  even for separable and classically correlated states (entanglement not the
  resource); CPT inner product removes it. No quantitative signal-vs-survival bound.
- 2020-2026 sweep (searches on "PT-symmetric no-signaling", "non-Hermitian
  postselection signal", Leggett-Garg/PT arXiv:2112.14775, PT fidelity Quantum 7, 960
  (2023)): follow-ups are qualitative (violation yes/no, which inner product) or
  study other witnesses. NO paper found that bounds the magnitude of the
  post-selected signal as a function of the survival probability, and none identifies
  an extremal PT family. This is exactly the gap.

### Q5. Mathematical tools: PARTIAL (rich toolbox, no assembled theorem)
- Reeb, Kastoryano, Wolf, "Hilbert's projective metric in quantum information
  theory", J. Math. Phys. 52, 082201 (2011), arXiv:1102.5170: contraction of the
  Hilbert projective metric h is NECESSARY AND SUFFICIENT for existence of a
  trace-nonincreasing CP map sending (rho1, rho2) -> (sigma1, sigma2) (probabilistic
  interconversion); inequalities between h and trace norm, fidelity, Chernoff bound;
  base-norm/distinguishability duality. This governs WHICH conditioned pairs are
  reachable but does not fix the success probabilities nor the bipartite constraint
  sigma_i steered from one shared rho_AB.
- Regula, "Tight constraints on probabilistic convertibility of quantum states",
  Quantum 6, 817 (2022), arXiv:2112.11321: "projective robustness" monotone (built
  from Hilbert projective metric) gives TIGHT necessary conditions on success
  probability of probabilistic transformations; SDP-computable.
- Regula, Lami, Wilde, arXiv:2209.10550 (above): Thompson metric
  max{D_max(rho||sigma), D_max(sigma||rho)} = postselected symmetric discrimination
  exponent.
- Gavorova, arXiv:2011.08487: weaker contractivity/subadditivity that survive
  postselection; conversion lemma standard -> postselected inequalities.
- Discrimination with fixed inconclusive rate (FRIO): Fiurasek, Jezek, PRA 67,
  012321 (2003); Bagan, Munoz-Tapia, Olivares-Renteria, Bergou, PRA 86, 040303(R)
  (2012), arXiv:1206.4145: complete error-vs-abstention-rate curve, interpolating
  minimum-error <-> unambiguous (IDP). This is the measurement-side twin of our
  question and supplies the correct "shape intuition" (perfect distinguishability
  below a critical p, algebraic decay above).
- Buscemi reverse data-processing / statistical morphisms, arXiv:1607.08335:
  comparison-of-experiments machinery if we want an operational converse.
- Probabilistic entanglement generation trade-off, arXiv:2112.03233: success
  probability vs output quality, resource-theoretic; analogous shape, different
  quantity.

### Q6. Extremality / optimal filters: CLEAR
- Popescu, PRL 74, 2619 (1995) (hidden nonlocality via sequential measurements);
  Gisin, Phys. Lett. A 210, 151 (1996) (local filters reveal CHSH violation);
  activation follow-ups (e.g. arXiv:2307.05015 CGLMP; experiment Opt. Express 28,
  13638 (2020); hidden steerability via filters, 2017).
- Verstraete, Dehaene, De Moor: two-qubit local filtering normal form
  (quant-ph/0011111), SLOCC normal forms and optimal filters maximizing entanglement
  monotones (quant-ph/0105090, PRA 68, 012103 (2003)); recent "Optimal local
  filtering operation for enhancing quantum entanglement", arXiv:2401.08944.
These optimize ENTANGLEMENT or BELL VIOLATION after filtering, mostly WITHOUT a
constraint on success probability (SLOCC normal form is the p -> 0 limit). Nobody
maximizes Bob's conditioned-marginal distinguishability at FIXED success probability,
and no extremal family is identified for that functional. The broken-PT-dimer
extremality claim is untouched in the literature. Note the SLOCC normal form is the
natural tool to reduce the extremality proof to Bell-diagonal/normal-form states.

---

## (b) THE 3 CLOSEST PRIOR RESULTS (exact statements)

1. Reeb-Kastoryano-Wolf 2011 (arXiv:1102.5170, JMP 52, 082201), Thm ~4/5:
   "For two given pairs of quantum states, the contraction of Hilbert's projective
   metric is necessary and sufficient for the existence of a probabilistic quantum
   operation [trace-nonincreasing CP map] that maps one pair onto the other":
   exists Lambda with Lambda(rho_i) proportional to sigma_i  iff
   h(sigma1, sigma2) <= h(rho1, rho2),
   where h(A,B) = log( sup-spectrum ratio ) = D_max(A||B) + D_max(B||A).
   Also proves inequalities h vs trace-norm/fidelity/Chernoff and base-norm duality
   giving "bounds on measures for statistical distinguishability... under operations
   involving postselection". Closest in SPIRIT: it is the interconversion skeleton
   of our theorem, but it neither fixes p1, p2 nor imposes the bipartite/HJW
   marginal constraint, and gives no extremal dynamical family.

2. Regula-Lami-Wilde 2022 (arXiv:2209.10550, IEEE TIT 69, 3453 (2023)), main thm:
   In hypothesis testing with an inconclusive outcome allowed and errors conditioned
   on conclusiveness, the optimal asymptotic error exponents for discriminating rho
   vs sigma are exactly
   symmetric:   max{ D_max(rho||sigma), D_max(sigma||rho) }   (Thompson metric),
   asymmetric:  D_max(rho||sigma) + D_max(sigma||rho)         (Hilbert metric).
   Operationally: post-selection buys distinguishability paid in conclusiveness, and
   the exchange rate is the projective metric. Single-system, measured-in-hand,
   asymptotic; no single-shot TV-vs-p function, no remote (steered) conditioning.

3. Arvidsson-Shukur et al. 2020 (arXiv:1903.02563, Nat. Commun. 11, 3775), main thm:
   For postselected estimation of theta, the rate (Fisher information per attempted
   trial) p_ps * I_F^ps(theta) is bounded by a classical limit unless the doubly
   extended Kirkwood-Dirac quasiprobability of (state, postselection) has negativity;
   with negativity, p_ps * I_F^ps can be anomalously large (unbounded in principle).
   I.e., the published "signal x success probability" trade-offs are Fisher-type and
   can be BEATEN by quantum negativity -- which sharpens the interest of a TV bound
   that CANNOT be beaten (TV is bounded by 1 and by no-signaling structure).

   [Honorable mentions: Bagan et al. arXiv:1206.4145 -- exact minimum-error vs
   inconclusive-rate curve for two states (measurement-side twin); Ju et al.
   arXiv:1906.08071 -- restores no-go theorems for non-Hermitian dynamics but proves
   no quantitative conditioned-signal bound.]

---

## (c) RECOMMENDED POSITIONING

The surviving increment is real and clean. Position the theorem as:

1. FIRST QUANTITATIVE NO-SIGNALING LEAKAGE BOUND UNDER POST-SELECTION: everyone
   (LHFL, Tang, Brody, Ju et al., Kumari-Sen) argues about WHETHER the conditioned
   PT signal is a violation; nobody has published HOW LARGE it can be at given
   survival probability. Frame: "post-selection opens a signaling side-channel of
   at most f(p1,p2); no-signaling is recovered continuously as p -> 1, and the
   bound is saturated by broken-PT dimers on Bell states."
2. SINGLE-SHOT AND GLOBAL where prior art is asymptotic (Regula-Lami-Wilde) or
   local/Fisher (Arvidsson-Shukur, Combes et al.). Explicitly state the corollary
   relations: our bound at fixed p vs their exponents/rates, to preempt referee
   "isn't this RLW?" (it is not: different scenario -- Bob never learns whether
   Alice's filter clicked in the unconditioned reading; in ours the abstention is
   on ALICE's side and the distinguished objects are Bob's steered marginals).
3. STEERING-THEORETIC CORE: the theorem solves the (apparently unposed) extremal
   problem max TV(sigma1,sigma2) s.t. p_i sigma_i <= rho_B, giving the HJW
   feasibility cone an operational trade-off curve -- pitch this to the steering
   community independently of PT.
4. EXTREMALITY AS THE HEADLINE NOVELTY: identification of an explicit dynamical
   family (broken-PT dimers, survival exp(-2 sin(theta) t), TV(inf) =
   sqrt(1-(s/sin theta)^2)) saturating the bound; connects to the Gisin/Popescu
   optimal-filter tradition but with the success-probability constraint that
   literature never imposed.
Risks to manage: (i) cite RKW + Regula prominently -- referees from the resource
   theory community will know them; (ii) verify the conjectured extremal formula
   against the elementary LP bound below before claiming universality; (iii) check
   the exact statement of RKW's "bounds on distinguishability under postselection"
   section (full text, Sec. on base norms) -- closest textual overlap anywhere.

---

## (d) CANDIDATE PROOF TOOLS FOUND

1. HJW/GHJW constraint + LP/SDP DUALITY. Feasibility p_i sigma_i <= rho_B makes
   max TV an SDP. Elementary LP relaxation (diagonalize rho_B, only the "weight
   above the test projector" matters): for any test projector P with q = Tr[P rho_B],
   Tr[P sigma1] <= min(1, q/p1),  Tr[P sigma2] >= max(0, (q - (1-p2))/p2),
   so TV <= max_{q in [0,1]} [ min(1, q/p1) - max(0, (q-1+p2)/p2) ].
   For p1 = p2 = p and rho_B maximally mixed d=2 this yields TV <= min(1, (1-p)/p)
   -- a concrete curve to check the broken-PT dimer family against (their p is
   time-dependent; compare parametrically). Tightness direction: explicit filters
   achieving it (diag filters on a Bell state) -- likely gives the achievability
   half almost for free.
2. HILBERT PROJECTIVE / THOMPSON METRIC (RKW arXiv:1102.5170; Regula 2112.11321;
   RLW 2209.10550): p <= exp(-D_max(sigma_i || rho_B)) is HJW in D_max clothing;
   monotonicity of D_max under CPTP gives clean converses; projective robustness
   supplies tight probability bounds if the simple LP is not tight for degenerate
   rho_B.
3. SLOCC NORMAL FORMS (Verstraete-Dehaene-De Moor quant-ph/0011111,
   quant-ph/0105090): reduce arbitrary rho_AB and filters to normal form to prove
   the Bell-state/PT-dimer family extremal among ALL states at fixed (p1,p2);
   the filter polar decomposition (unitary x positive) reduces Alice's maps to
   positive diagonal filters wlog.
4. FRIO DISCRIMINATION CURVES (Bagan et al. 1206.4145; Fiurasek-Jezek): exact
   error-vs-abstention interpolation for two states; useful for the converse when
   Bob optimizes a measurement AND Alice's filter click is announced (the
   "conclusive Helstrom" comparison curve), and for the expected kink at the
   critical p (analog of the unambiguous-discrimination threshold).
5. GAVOROVA CONVERSION LEMMA (2011.08487): mechanical translation of contractivity
   inequalities into the postselected setting -- handy for the dynamical
   (time-dependent, Trotterized) version of the theorem for PT evolution.
6. KIRKWOOD-DIRAC NEGATIVITY (1903.02563): optional garnish -- express when the
   conditioned signal is nonzero at all in quasiprobability terms; links the paper
   to the postselected-metrology audience.

## Search log (main queries)
- post-selection no-signaling bound conditional states distinguishability (hits:
  2506.14105, 0708.3909, 2112.03233)
- postselected no-signaling trace distance survival probability (hits: 2308.02583,
  1412.3361)
- PT-symmetric no-signaling Tang/Brody/Ju + 2020-2026 follow-ups (hits: 1312.3395,
  Tang NatPhot 2016, 1703.03529, 1906.08071, 2202.02744, 2112.14775)
- steering ellipsoid Jevtic et al., HJW + SDP steering (hits: 1303.4724, 1604.00501,
  1709.06703, 2311.10552)
- postselected metrology (hits: 1903.02563, CFJC PRA 89 052117, 1307.4016)
- Hilbert projective metric / probabilistic conversion (hits: 1102.5170, 2112.11321,
  2209.10550, 2011.08487)
- hidden nonlocality filters / SLOCC (hits: Gisin 1996, Popescu 1995,
  quant-ph/0011111, quant-ph/0105090, 2307.05015, 2401.08944)
- FRIO discrimination (hits: 1206.4145, Fiurasek-Jezek PRA 67 012321)
