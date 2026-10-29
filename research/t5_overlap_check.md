# T5 Overlap / Prior-Art Check: Quantum ED of Ghost Vacuum Decay vs Channel Count

Date: 2026-07-12
Plan under check: exact-diagonalization / Krylov real-time evolution of a genuinely
QUANTUM 1+1d two-field theory (normal phi + ghost chi, lambda phi^2 chi^2), 6-10
momentum modes, occupation caps, measuring d<N_phi>/dt and vacuum survival at short
times AS A FUNCTION OF the number of open (resonant) decay channels swept via mode
cutoff at fixed volume. Target claim: channel-ladder (multiplicity) scaling of the
quantum rate vs dynamically resummed suppression (Gross-Strumia-Teresi-Zirilli
arXiv:2007.05541 escape).

================================================================================
VERDICT TABLE
================================================================================
Item 1 (Deffayet et al 2604.21823 + 2504.11437 + Held 2509.18049) .... CLEAR
Item 2 (Ewasiuk-Profumo 2604.21348) .................................. CLEAR (adjacent method, different physics question)
Item 3 (real-time quantum sim of ghost vacuum decay, any) ............ CLEAR (nothing found)
Item 4 (Ham.-truncation / lattice phi^2 chi^2 with sign-flipped sector) CLEAR (only normal-field FVD precedents)
Item 5 (open-CHANNEL golden-rule scaling in discrete multimode bosons)  PARTIAL (Burshtein-Goldstein 2410.21941, normal photons, no ghost)
OVERALL .............................................................. CLEAR to proceed; no preemption of the ghost channel-count experiment found.

================================================================================
ITEM 1: Deffayet, Fathe Jalali, Held, Mukohyama, Vikman line
================================================================================

(a) arXiv:2604.21823 "Unitary Time Evolution and Vacuum for a Quantum Stable Ghost"
- SYSTEM: finite-degree-of-freedom quantum MECHANICS: one harmonic oscillator
  polynomially coupled to ONE ghost dof (negative kinetic energy). NOT field
  theory, NOT lattice, NOT momentum modes. This is the quantization of the
  classically stable mechanical models of their "Ghosts without runaway" line
  (arXiv:2108.06294, PRL 128, 041301 (2022); also JCAP 2023 "Global and local
  stability for ghosts coupled to positive energy degrees of freedom").
- COMPUTES: spectral properties + real-time Schrodinger evolution (numerical) +
  moment bounds. Abstract: "We prove that due to an integral of motion with a
  positive discrete spectrum: i) the Hamiltonian has a pure point spectrum
  unbounded in both directions, ii) the evolution is manifestly unitary,
  iii) the vacuum is well-defined."
- CHANNEL-COUNT SCALING OF A VACUUM DECAY RATE: none. There is no decay rate at
  all in their setup -- the whole point is that their specially chosen
  (confining, integrable-adjacent) interaction FORBIDS decay; the spectrum is
  pure point, so there is no continuum to decay into and no golden rule regime.
- VACUUM DEFINITION (physics trap, see Section TRAPS): their "vacuum" is the
  ground state of a positive-definite conserved integral of motion N, NOT the
  free-Fock vacuum of H0 with the ghost occupation annihilated. In a generic
  lambda phi^2 chi^2 theory no such positive integral of motion exists, so
  their vacuum construction does not transplant to our model.
- Companion: arXiv:2604.21826 "Quantum mechanics with a ghost: Counterexamples
  to spectral denseness" (same collaboration date-stamp): quantizes integrable
  point-particle ghost systems; shows discrete, non-dense spectra unbounded both
  ways. Again finite-dof QM, spectra only, no decay-rate or channel content.

(b) arXiv:2504.11437 "Ghostly interactions in (1+1) dimensional classical field theory"
- CLASSICAL only. Two coupled scalars with opposite-sign kinetic terms in 1+1d
  Minkowski; real-time classical PDE evolution; instability onset/suppression
  vs masses and self-interactions; finite-time extrapolation. No quantum
  lattice/ED content whatsoever. It is the classical counterpart of what we
  propose to do quantum-mechanically -- a citation, not a preemption.

(c) arXiv:2509.18049 Held, "Global stability of ghostly field theories:
    Classical scattering in (N+1) dimensions"
- CLASSICAL scattering under spherical symmetry, small-data/large-data global
  stability, polynomial potentials. No quantum content.

VERDICT: CLEAR. The quantum members of this program are 2-dof quantum mechanics
with hand-picked confining interactions engineered so that NO decay occurs; they
never pose, let alone answer, the question "how does the quantum decay rate of
the free-Fock vacuum scale with the number of open resonant channels in a
multimode field theory." The classical members are 1+1d PDE runs.

================================================================================
ITEM 2: Ewasiuk-Profumo arXiv:2604.21348
================================================================================
"Ghost Degrees of Freedom Without Quantum Runaway: Exact Moment Bounds from an
Operator Conservation Law"
- SYSTEM: again ONE harmonic oscillator + ONE ghost dof, with interactions that
  are BOUNDED and vanish at large separation (their theorem requires this).
- METHODS: analytic operator conservation law giving state-independent bound on
  mean squared phase-space radius; validated by quantum NUMERICS in three
  frameworks including Fock-space diagonalization (this is the closest anyone
  has come to "ghost exact diagonalization" -- but for 2 dofs, not field modes).
- Key claim: "Ghost quantum instability is ... not an inevitable consequence of
  a wrong-sign kinetic term but depends critically on the interaction structure."
- NO field-theory modes, NO vacuum decay rate, NO channel scaling. Their bounded
  interaction class explicitly EXCLUDES lambda phi^2 chi^2 (unbounded, grows at
  large field), so their no-runaway theorem does not cover our model -- in fact
  our experiment probes exactly the complementary (generic-coupling) regime.
VERDICT: CLEAR. Cite as the state of the art in quantum ghost numerics
(finite-dof Fock diagonalization) and as motivation: the open question is what
happens for unbounded, field-theoretic couplings with many modes.

================================================================================
ITEM 3: Any real-time quantum simulation of ghost/phantom vacuum decay
================================================================================
Searched: "ghost field exact diagonalization", "negative energy vacuum decay
lattice quantum", "Hamiltonian truncation ghost", "real-time Hamiltonian
truncation vacuum decay", "MPS negative kinetic energy", "quantum simulation
Ostrogradski", Krylov + phantom/ghost.

Findings:
- NOTHING that does quantum lattice/ED/Krylov/MPS real-time evolution of a
  multimode ghost field theory. The quantum literature on interacting ghosts is
  (i) finite-dof QM (items 1-2 above), or (ii) analytic continuum QFT:
    * Buoninfante arXiv:2605.29047 "Asymptotic Quantum Dynamics of Ghost Fields"
      -- analytic dressed-propagator / complex-conjugate-pole analysis; shows
      interference makes the negative-norm one-particle state non-orthogonal to
      multi-particle states; "a detector can never observe an isolated ghost
      particle asymptotically." No numerics, no rate-vs-channel study.
    * Buoninfante arXiv:2606.18349 "Ghosts versus Unstable Particles in QFT" --
      analytic; "ghosts survive asymptotically without decaying"; finite-time
      vs asymptotic formulations; no vacuum-decay computation, no numerics.
- Classical numerics only: 2504.11437 (above); Wysong, Overvaag, Lim, Kimn
  arXiv:2604.25635 "Numerical Investigations of Stable Dynamics in the Presence
  of Ghosts" -- CLASSICAL spacetime finite-element sims of ghost-normal coupled
  scalars in 1+1d and 2+1d; finds "long-lived, dynamically bounded evolution"
  with stability controlled by spectral content/amplitude, instability by
  "nonlinear spectral energy transfer rather than instantaneous runaway";
  a lifted phi^6 potential gives metastable regimes. Closest in SPIRIT to a
  metastability landscape, but entirely classical -- no hbar, no vacuum, no
  channel counting. Also "Bounded Chaos in a Ghost-Coupled Hamiltonian System"
  arXiv:2606.29342 (classical few-dof).
VERDICT: CLEAR. To our knowledge no one has ever time-evolved a genuinely
quantum multimode ghost+normal field system.

================================================================================
ITEM 4: Hamiltonian truncation / fuzzy sphere / DLCQ with a sign-flipped sector
================================================================================
- No hit for phi^2 chi^2 with an overall sign-flipped kinetic/energy sector in
  the Hamiltonian-truncation, fuzzy-sphere, or light-cone-quantization
  literatures. HT-on-quantum-devices work (e.g. arXiv:2407.19022) is normal-sign.
- METHOD PRECEDENTS (normal fields, real-time FALSE-vacuum decay -- cite as
  methodology, they do not preempt the ghost question):
    * Lagnese, Surace, Kormos, Calabrese arXiv:2107.10176 "False vacuum decay in
      quantum spin chains" (PRB 104, L201106): real-time numerics of metastable
      vacuum decay in Ising/XXZ chains; the canonical discrete-system FVD study.
    * Follow-ons: arXiv:2508.13780 (many-body theory of FVD in spin chains),
      arXiv:2607.03274 (long-range FVD), Moss arXiv:2510.12592 (notes on FVD in
      quantum Ising), arXiv:2601.04305 (2+1d Ising bubble dynamics).
    * Abel, Spannowsky, Williams arXiv:2506.17388 "Qumode Tensor Networks for
      False Vacuum Decay in QFT": MPS over high-dimensional bosonic (qumode)
      sites for 1+1d scalar FVD with TEBD real time -- the nearest methodological
      template to "bosonic modes + occupation caps + real-time evolution".
    * Lattice real-time bubble nucleation arXiv:2508.13645; thermal 1+1d FVD
      arXiv:2408.06411; cold-atom gauge-theory FVD quantum simulator
      arXiv:2411.12565; bubble nucleation across a QPT arXiv:2505.09607.
  All of these are NORMAL-sign theories decaying between two vacua of a
  potential; none has a wrong-sign sector, and none sweeps channel count.
VERDICT: CLEAR (method precedents exist and should be cited as such).

================================================================================
ITEM 5: Golden-rule open-CHANNEL multiplicity scaling in discrete multimode bosons
================================================================================
- Superradiance literature does N-scaling in the number of EMITTERS -- different
  axis, as anticipated; not overlap.
- CLOSEST FOUND: Burshtein & Goldstein arXiv:2410.21941 "Quantum simulation of
  the microscopic to macroscopic crossover using superconducting quantum
  impurities": a single photon in a FINITE transmission line coupled via a
  nonlinear impurity (qubit) to several "baths" of n-photon states (discrete
  because the line is finite). They "uncover the conditions under which the
  photon's decoherence rate approaches the decay rate predicted by Fermi's
  golden rule," and find cascade processes where the presence of other
  photon-number baths ENHANCES the decay rate into a given n-photon bath.
  This is a genuine discrete-mode test of golden-rule onset and inter-bath
  enhancement -- but: (i) normal-sign photons, positive-definite H; (ii) decay
  of an EXCITED single-photon state, not of the vacuum; (iii) the swept variable
  is system size / mode density, not an open-channel count at fixed volume, and
  there is no multiplicity-horn claim.
- Cavity-QED numerics (e.g. quant-ph/9812001) and cavity-modified FGR work
  (multimode enhancement over single-mode, J. Chem. Phys. 159, 151105) confirm
  the generic DOS-proportionality of FGR in discrete settings, but again no
  systematic open-channel-count sweep of a VACUUM decay rate.
VERDICT: PARTIAL. The FGR-in-finite-discrete-systems methodology has published
precedent (cite 2410.21941 for validation of the "rate vs discrete channel
structure" observable); the specific object -- vacuum decay rate of a ghost-
coupled theory vs number of open resonant channels -- is untouched.

================================================================================
THE 3 CLOSEST WORKS (with exact statements)
================================================================================
1. Ewasiuk & Profumo, arXiv:2604.21348 -- Fock-space diagonalization of ONE
   oscillator + ONE ghost with BOUNDED interactions; proves/verifies moment
   bounds, real spectrum, Poisson statistics. Exact statement: "Ghost quantum
   instability is therefore not an inevitable consequence of a wrong-sign
   kinetic term but depends critically on the interaction structure."
   Distance from us: 2 dofs vs 6-10 field modes; bounded coupling vs phi^2 chi^2;
   no vacuum decay rate; no channel sweep.
2. Deffayet, Fathe Jalali, Held, Mukohyama, Vikman, arXiv:2604.21823 --
   quantized 2-dof ghost+oscillator with confining polynomial coupling. Exact
   statement: "the Hamiltonian has a pure point spectrum unbounded in both
   directions, ... the evolution is manifestly unitary, ... the vacuum is
   well-defined." Distance: pure point spectrum by construction => no decay
   channels exist at all; vacuum defined via integral of motion, not free Fock.
3. Burshtein & Goldstein, arXiv:2410.21941 -- discrete-mode circuit-QED test of
   FGR onset and multi-bath cascade enhancement of a single-photon decay rate.
   Distance: normal-sign theory, excited-state (not vacuum) decay, sweeps
   size/density not channel count, no ghost.

================================================================================
METHOD PRECEDENTS WORTH CITING
================================================================================
- Lagnese et al arXiv:2107.10176 (+2508.13780, 2607.03274): real-time FVD in
  discrete quantum systems -- observable design (survival probability, bubble
  precursors) directly reusable.
- Abel, Spannowsky, Williams arXiv:2506.17388: bosonic-mode (qumode) truncation
  with occupation caps + real-time evolution for 1+1d scalar FVD -- nearest
  template for our mode-truncated Hamiltonian construction.
- Ewasiuk-Profumo 2604.21348: precedent for Fock-space diagonalization of a
  ghost-containing quantum Hamiltonian (2 dofs) -- extend to multimode.
- Burshtein-Goldstein 2410.21941: precedent for extracting FGR-like rates from
  finite discrete-mode real-time quantum dynamics, including regime-of-validity
  criteria (rate vs level spacing) -- directly relevant to our short-time
  window and to arguing when d<N_phi>/dt is a "rate".
- Gross, Strumia, Teresi, Zirilli arXiv:2007.05541 (PRD 103, 115025): the
  suppression hypothesis we test; they compute run-away rates analytically +
  numerically but classically/semiclassically, not by quantum multimode ED.
- Cline, Jeon, Moore hep-ph/0311312 (PRD 70, 043543) and Carroll-Hoffman-Trodden
  (PRD 68, 023509): the divergent-phase-space / cutoff framing of ghost vacuum
  decay that our channel-count sweep discretizes and tests directly.

================================================================================
PHYSICS TRAPS FLAGGED BY THE LITERATURE
================================================================================
T1. VACUUM DEFINITION IS CONTESTED. Deffayet et al 2604.21823 define the vacuum
    as the ground state of a positive-definite integral of motion N (their
    interaction is engineered so N exists); it is NOT the free-Fock vacuum
    |0_phi> x |0_chi> annihilated by both sets of lowering operators with
    positive-norm quantization of the ghost. Our free-Fock choice is standard in
    the vacuum-decay literature (GSTZ, Cline-Jeon-Moore) but a referee versed in
    the Deffayet line may object that "the" ghost vacuum is model-dependent.
    Mitigation: state explicitly that we quantize the ghost with positive norm
    and negative energy (Hamiltonian unbounded below), take the free-Fock state
    as the t=0 state, and measure its survival -- i.e., we test the GSTZ
    question on its own terms. Note that for lambda phi^2 chi^2 no positive
    integral of motion of the Deffayet type is known, so their alternative
    vacuum does not exist in our model.
T2. INTERACTION-STRUCTURE DEPENDENCE. Both 2604.21823/21826 and 2604.21348 prove
    stability only for special interactions (confining/integrable, or bounded
    and vanishing at infinity). Our phi^2 chi^2 is in neither class. Expect the
    objection "your instability is an artifact of an unbounded coupling"; the
    counter is that phi^2 chi^2 is precisely the generic EFT coupling GSTZ and
    the phantom literature consider.
T3. OCCUPATION CAPS vs UNBOUNDED SPECTRUM. Because H is unbounded below along
    the chi ladder, occupation caps are not an innocuous truncation as in
    normal-field HT: the cap itself can fake metastability (a capped ghost
    ladder is effectively a confined ghost, i.e., exactly the Deffayet-stable
    situation). MUST demonstrate cap-independence of the short-time rate
    (sweep N_max) or restrict claims to times before the cap boundary is
    populated. This is the single most dangerous artifact.
T4. FINITE-SIZE FGR WINDOW. Burshtein-Goldstein show FGR rates emerge in
    discrete systems only when the rate exceeds the level spacing and before
    recurrences; with 6-10 modes the golden-rule window is narrow. Report
    d<N_phi>/dt inside a validated window (rate >> mode spacing^-1 caveat, t <<
    Heisenberg time), else the "rate" is a quadratic-in-t Zeno slope.
T5. ASYMPTOTIC vs SHORT-TIME. Buoninfante 2605.29047/2606.18349 argue ghosts
    never appear as asymptotic particles due to interference with multiparticle
    states; this concerns asymptotic S-matrix structure and does not contradict
    a short-time vacuum-depletion rate, but the paper should say so to preempt
    conflation.
T6. CLASSICAL METASTABILITY IS SPECTRAL-CONTENT-DEPENDENT. 2604.25635 and
    2504.11437 find classical lifetime depends strongly on UV vs IR content and
    amplitude; our channel-count sweep via cutoff changes UV content too --
    disentangle "more channels" from "more UV modes" by also sweeping a
    detuned (non-resonant) cutoff as control.

================================================================================
BOTTOM LINE
================================================================================
No published work performs real-time quantum evolution of a multimode
ghost+normal field theory, and no published work measures any vacuum decay
observable as a function of open-channel count, in ghost systems or otherwise.
The experiment is CLEAR to proceed. The novel axis (channel-count sweep at fixed
volume of a genuinely quantum ghost theory) is unclaimed territory; the nearby
literature supplies method precedents (FVD spin-chain/qumode numerics; finite-
system FGR extraction) and two active opposing camps (Deffayet/Ewasiuk-Profumo
"stability is interaction-structural" vs GSTZ "metastable escape") for whom the
result will be directly load-bearing either way.
