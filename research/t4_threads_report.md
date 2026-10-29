# T4 THREADS-TO-PULL REPORT — research-strategy scout
Date: 2026-07-11 (scout run against paper5/main.tex v0.1, notes.md 2026-07-12
entries, research/t4_literature_triage.md, research/t4_vertex_conventions.md,
papers 1-3 abstracts). ASCII throughout.

Novelty checks performed by web search this run (summarized inline where used):
 (i) PU-oscillator photonic analog: NOT FOUND in print — EP photonics is
     crowded (Wiersig sensing, higher-order EPs in coupled resonators,
     arXiv:1904-era Nature Comm, 2504.00655, 2509.02174) but no one has built
     or proposed "the Pais-Uhlenbeck / conformal-gravity mode in a photonic
     lattice," and no process-level observable (divisor negativity, cascade
     onset) appears anywhere in that literature.
 (ii) alpha_g numerical value: still nothing in print (consistent with the
     vertex-conventions agent's dedicated sweep). The 3e109 number is ours.
 (iii) Divisibility-mechanism classification: LIVE ADJACENT LITERATURE —
     "Quantum versus classical P-divisibility" (arXiv:2405.05794, PRA 110,
     052212), "On positively divisible non-Markovian processes"
     (arXiv:2401.12715), Chruscinski school lecture notes (2607.07332).
     All are trace-preserving/stochastic; the SUB-stochastic (probability-
     losing) divisor failure taxonomy — negativity vs column-sum violation —
     is not classified there. Risk uprated to medium, lane still open.
 (iv) Jordan-unfolding eps^(1/k) physics: Puiseux splitting is textbook and
     the EP-splitting-exponent literature is active (arXiv:2509.02174,
     PRResearch 7, 023132 graph-theoretic exponents), but no one maps
     unfolding DIRECTION -> oscillatory-vs-exponential -> physics of which
     deformation of conformal gravity you bought. Increment available.
 (v) Conformal-gravity cosmological perturbations: Mannheim himself has the
     growth story in print (arXiv:1109.4119 = PRD 85 124008; 2101.02608 =
     PRD 103 104022 "exact solution to perturbative conformal cosmology";
     tensor modes "grow far more rapidly than standard"). Seed 6 is therefore
     a REINTERPRETATION play, not an open computation.

Legend: effort = calendar time at this program's demonstrated pace (agents +
scripts); risk = prior-art preemption or technical failure; payoff = value to
the program (papers, falsifiability, external engagement).

================================================================================
RANKED LIST (best first)
================================================================================

--------------------------------------------------------------------------------
1. [SEED 2] SECTOR-RESOLVED NO-REPRESENTATION LEMMA AT THE INFINITE-ORDER EP
--------------------------------------------------------------------------------
First concrete result: Lemma extension. Smilga 1409.8450: the equal-frequency
QFT stacks Jordan blocks whose size grows with level number N (infinite-order
EP). Paper 4's lemma gives ||e^{-iHt}|| ~ t^{k-1} per block; with k(N)
unbounded, sup_N over sectors beats ANY polynomial at fixed t, and — the new
bite — there is NO UNIFORM dilation: the survival-conditioned normalization
sigma_max(t) that makes the open process work for one sector diverges across
sectors, so the Bender-Mannheim "unitary evolution via nonstationary states"
bookkeeping cannot be done uniformly on the Fock space. Corollary candidate:
the open process exists sector-by-sector but not as a single conditioned
process on the full field — a field-level sharpening of the adjudication.
Deliverable: one theorem + one script (t4_jordan_process.py already measures
k = 2,3,4 growth 1.000/1.999/2.997; extend to stacked blocks + uniformity test).
Effort: DAYS (2-4). The single highest-leverage item: it converts paper 4's
own stated weakest point ("the lemma constrains flat-space mode kinematics
only... the mechanical prototype") into a field-level statement, inside the
audit window, before circulation.
Risk: LOW-MEDIUM. Must verify Smilga's block-size structure (is k(N) linear
in N?) by a careful read of 1409.8450; the lemma arithmetic itself is safe.
Failure mode: blocks don't actually grow (then the result degrades to "k=2
everywhere, per-mode," which paper 4 already has).
Payoff: HIGH. Strengthens the flagship claim where a referee (or Mannheim)
would push first. Also the natural home for a one-paragraph engagement with
Fring-Marquette-Taira 2601.20752 (see item 5).
VERDICT: PURSUE NOW — fold into the paper-4 audit cycle as a section/appendix,
not a new paper.

--------------------------------------------------------------------------------
2. [NEW N1] THE CONFORMAL POINT AS A PHASE BOUNDARY: UNFOLDING DIRECTION
   DECIDES OSCILLATORY VS EXPLOSIVE (Ilhan-Kovner closed into the taxonomy)
--------------------------------------------------------------------------------
First concrete result: classification theorem-let. Perturb the PU Jordan
block: eigenvalues split by ~eps^{1/k} (Puiseux, textbook), and the split is
either onto the real axis (two real frequencies: detuned PU = massive
quadratic gravity, unbroken side, closed representation exists at cost
2/delta) or into a complex-conjugate pair (broken side: exponential growth =
paper 1's transient/explosive class). Theorem-let: classify the physical
deformations of conformal gravity by which side of the EP they unfold onto —
(a) adding an Einstein term m2 =/= 0: real split (Stelle); (b) nonlinear/
interaction-induced effective mass of Ilhan-Kovner 1403.4664 ("ghost turned
tachyon," finite-time singularity): complex split, i.e. THEIR classical
blowup IS the program's broken-PT/explosion class, reached by unfolding the
same EP the other way. The banked numerical remark (machine-eps splits the
block by eps^{1/k}; polynomial -> exponential for t > eps^{-1/k}) becomes
physics: ANY regulator of conformal gravity (lattice, numerics, curvature
background) sits on one side or the other; the pure theory is the boundary.
Effort: DAYS-WEEKS (1-2 weeks). Script exists in embryo (the eps-perturbation
remark in t4_jordan_process.py); needs the direction-resolved sweep + a read
of Ilhan-Kovner to map their effective-mass sign.
Risk: LOW-MEDIUM. Puiseux/EP-splitting-exponent literature is active
(2509.02174 does splitting exponents vs perturbation positions) — the math
must be cited as known; the increment is the gravity mapping + process-class
assignment, which the search shows unclaimed. Failure mode: Ilhan-Kovner's
instability may not reduce cleanly to a mode-level complex split.
Payoff: HIGH. Closes a loop across papers 1 and 4 (conservative/transient/
explosive now has the conformal point as its organizing tricritical point);
gives paper 4's "fragility is the EP physics" remark a theorem to live in.
Publication shape: section in a paper-4 v2 or the seed of paper 5.
VERDICT: PURSUE — right after the paper-4 audit closes.

--------------------------------------------------------------------------------
3. [SEED 1] TAXONOMY THEOREM: MECHANISMS OF INDIVISIBILITY FOR SUB-STOCHASTIC
   FAMILIES (negativity vs conditional mass creation vs ...)
--------------------------------------------------------------------------------
First concrete result: complete classification for 2x2 (then triangular d x d)
sub-stochastic families of how the two-point divisor D(t+s,s) can fail to be
sub-stochastic: (M1) entrywise negativity (paper 1's broken-dimer mechanism),
(M2) column-sum > 1 with nonnegative entries (paper 4's conditional mass
creation), and whether (M3) mixed/other cells are possible in d >= 3. Conjecture
worth testing first in an afternoon: for 2x2 the two mechanisms are exhaustive
and exclusive, and M2 occurs iff the process is a one-way cascade (triangular
family) with non-log-concave survival along the receiving beable — i.e. M2 is
the signature of Jordan-type (polynomial) dynamics, M1 of complex-spectrum
(broken) dynamics. That would make the mechanism dichotomy the DIVISOR-LEVEL
IMAGE of item 2's phase boundary — the two threads are secretly one theorem,
which is why both rank high.
Effort: 1-2 WEEKS including the adversarial numerics.
Risk: MEDIUM. The P-divisibility literature (2405.05794, 2401.12715,
Chruscinski-Maniscalco lineage) classifies divisibility for stochastic/
trace-preserving dynamics and connects negativity of generator rates to
information backflow; it does NOT treat probability-losing families or the
column-sum failure mode, but a referee will demand that engagement, and there
is a real chance a partial result exists in the classical embedding-problem
literature (checked: the embedding/infinite-divisibility corpus — 1709.09561,
2409.11125 — is about exact roots of stochastic matrices, not failure
taxonomy; still, deep-read before claiming).
Payoff: MEDIUM-HIGH. It is the program's own bookkeeping made rigorous — every
future paper (and the photonic proposal) inherits a clean statement "measure
the divisor; the failure MODE tells you the spectrum class." Standalone short
paper (paper-5 candidate) or the theory backbone of item 4's proposal.
VERDICT: PURSUE — start with the 2x2 exhaustiveness check (one day) before
committing to the full paper.

--------------------------------------------------------------------------------
4. [SEED 3] PHOTONIC AT-EP DEVICE: MEASURE THE ONE-WAY CASCADE AND THE
   CONDITIONAL-MASS-CREATION ONSET (extend the T2 proposal)
--------------------------------------------------------------------------------
First concrete result: one new device row + error budget in proposal/main.tex.
The T2 measurement-chain proposal (Klauck-grounded coupled waveguides, kappa =
0.10-0.50 cm^-1, gamma up to 0.90 cm^-1, ladder-of-lengths, det-based t_c
estimator invariant to calibration) currently probes the BROKEN phase. Add
device D4 AT the EP (gamma = 2 kappa exactly): the transfer matrix is the
Jordan cell, |U|^2 is triangular (one-way cascade between the two guides),
amplitude in the receiving guide grows linearly in z (t^2 in intensity), and
the divisor's column-sum crosses 1 at z_c = t_c/kappa ~ 0.5/kappa — the first
laboratory observable ever proposed for indivisibility-by-mass-creation, and
simultaneously a table-top realization of conformal gravity's per-mode
kinematics (the honest framing: "the dipole ghost's open process in glass").
The det-zero estimator theorem-let needs a check at the EP (det Gamma may
degenerate — the estimator may need the column-sum observable instead: small
new theory item, feeds item 3). Existing MC harness (t2_measurement_chain.py)
does the error budget with ~1 day of modification.
Effort: 1-2 WEEKS (proposal-grade; no lab needed from us).
Risk: LOW-MEDIUM on novelty — web check found NO photonic PU/at-EP process-
observable proposal; EP photonics itself is very crowded, so framing must be
"process-level observables at the EP" not "we discovered EPs in waveguides."
Petermann-factor physics (cond = 2/delta) is known there (Wiersig) — cite,
never claim. Fabrication risk is the lab's, not ours; Klauck-type arrays sit
at gamma/2kappa ~ 0.25 today, EP operation (0.5) is a parameter change.
Payoff: HIGH. Makes paper 4's new mechanism falsifiable in an existing
experimental platform; strongest external-engagement magnet in the list
(EP-sensing community + PT-photonics community + ghost-QFT community).
Also the concrete deliverable for the T5 (quantum lattice) ambition at
near-zero cost. NOTE the k^4-dispersion metamaterial version (an EP LINE, all
k at once, via quartic band-touchings in flat-band photonics) is the stretch
goal — park it inside this thread, do the two-guide device first.
VERDICT: PURSUE — as an UPDATE to the existing proposal document, not a new
paper; sequence after items 1-2 (they feed its theory section).

--------------------------------------------------------------------------------
5. [NEW N2] ADJUDICATION COMMENT ON FRING-MARQUETTE-TAIRA 2601.20752
--------------------------------------------------------------------------------
First concrete result: a short comment (or a paper-4 subsection): FMT (Jan
2026) prove "classically equivalent Hamiltonians define inequivalent quantum
theories" at PU resonance — one non-diagonalizable, one diagonalizable. The
process currency supplies exactly the missing selection principle: the
diagonalizable realization admits a closed stochastic representation, the
Jordan one provably does not (paper 4's lemma); "inequivalent quantum
theories" = "different sample-space verdicts," and the choice is empirical
in principle (item 4's observable). Timely: the paper is six months old and
still uncontested.
Effort: DAYS (2-3) — the content already exists in paper 4; this is packaging.
Risk: LOW. Only risk is strategic: a standalone comment on a fresh paper by
active authors invites a reply cycle before paper 4 circulates.
Payoff: MEDIUM. Citation engagement with the one live 2026 thread on exactly
our object; positions the program inside the conversation rather than beside
it.
VERDICT: PURSUE-LITE — write it as a paper-4 v2 paragraph now; decide on the
standalone comment AFTER paper 4 is public (the comment cites it).

--------------------------------------------------------------------------------
6. [NEW N3] BOUNDARY CONDITIONS ARE CONDITIONING: PRICE MALDACENA'S
   GHOST-REMOVAL WITH THE PAPER-3 TRADE-OFF
--------------------------------------------------------------------------------
First concrete result: proposition. Maldacena 1105.5632 removes conformal
gravity's ghost by Neumann + positive-frequency boundary conditions;
Hell-Lust-Zoupanos 2306.13714 show this fails to select a general solution on
Minkowski. In process language a future/asymptotic boundary condition is a
POST-SELECTION (conditioning of the dilated process on a survival-type
effect), and paper 3's sharp bound TV^2 + (sqrt(det M)/p)^2 <= 1 prices it:
compute the survival probability cost of the Maldacena projection per mode
and exhibit the trade-off. Would unify the escape-route table's horn-2 row
with the paper-3 machinery — every horn then has a quantitative price from
inside the program (horn 1: the fork; horn 3: the lemma; horn 2: the
conditioning bound).
Effort: WEEKS (2-4) — mapping BCs to effects is genuinely new theory, not
packaging.
Risk: MEDIUM-HIGH. The identification "boundary condition = post-selection"
must be made exact, not slogan-level; on Minkowski the HLZ result may mean
the projection isn't even well-defined (which is itself a result, but a
weaker one).
Payoff: MEDIUM-HIGH. Completes the trilemma table into an all-three-horns-
priced-by-our-own-theorems structure — the natural capstone claim of a
program review.
VERDICT: PARK (queue behind items 1-4); promote when paper 4 is out — it is
the strongest candidate for "paper 5 proper" if item 3 stays an appendix.

--------------------------------------------------------------------------------
7. [SEED 4] THE UV EXCEPTIONAL LINE OF MASSIVE QUADRATIC GRAVITY:
   IS THE k^2 EP EXCESS PHYSICAL?
--------------------------------------------------------------------------------
First concrete result would be: attach an observable to the UV approach —
candidates: (a) Petermann-factor-enhanced mode noise (excess spontaneous
emission ~ cond^2 ~ k^4) in the ghost sector near M2; (b) survival-
conditioned distinguishability (paper-3 TV) as a function of k, showing the
UV modes saturate the post-selection frontier; (c) connection to the
Donoghue-Menezes Merlin width: does the resonance width regulate the EP
approach (complex pole = never exactly on the line)? Item (c) is probably
the truth and probably DEFLATES the thread: Merlin modes have finite width,
so the dressed theory detunes itself off the exceptional line — worth one
day to check, because if so, paper 4's UV-line statement quietly becomes
"tree-level only" (it is already scoped as such, but this would be the
mechanism).
Effort: WEEKS, open-ended; the one-day Merlin-width check first.
Risk: HIGH of remaining formal — dictionary cost is not an observable, and
the literature (Wiersig etc.) already owns EP-enhanced sensitivity as
physics.
Payoff: MEDIUM if an observable attaches; LOW otherwise.
VERDICT: PARK with a defined trigger: do the one-day "does the loop-induced
width detune the EP line?" check inside the paper-4 audit; pursue only if
the answer is interesting either way and cheap.

--------------------------------------------------------------------------------
8. [SEED 7] CROSS-THREAD: JORDAN LEMMA vs T10 (HORIZONS) AND T5 (LATTICE)
--------------------------------------------------------------------------------
Assessment: the deep connection is real but conceptual: the horizons thread's
clock-dependence theorem (natural boundary in Killing time vs exit boundary in
proper time — a singular TIME change) and the Jordan lemma (no representation
under any SIMILARITY — a singular BASIS change) are the two coordinate-
singularity axes of the same dictionary: one reparametrizes time, the other
the beables. A unifying slogan-theorem ("dictionary singularities come in two
kinds; horizons realize one, exceptional points the other; both leave the
open process intact") would be the organizing frame of a program review, not
a standalone result. For T5: the lattice test of the Jordan cell IS item 4.
Effort: DAYS to state; nothing to compute now.
Risk: LOW (it's internal glue).
Payoff: LOW now, MEDIUM later (review/synthesis paper).
VERDICT: PARK — write the paragraph into notes.md when T10 kicks off, so the
T10 paper is born with the cross-reference.

--------------------------------------------------------------------------------
9. [SEED 6] DIPOLE-GHOST COSMOLOGY: ONE-WAY CASCADE AS STRUCTURE GROWTH
--------------------------------------------------------------------------------
Assessment: Mannheim already owns the computation lane (1109.4119 = PRD 85
124008 "Cosmological perturbations in conformal gravity"; 2101.02608 = PRD
103 104022 exact solution recombination-to-now; tensor fluctuations growing
much faster than standard). The available increment is a REINTERPRETATION:
the per-mode t-growth of perturbations = the one-way conditioned cascade, so
the process picture says structure growth in conformal cosmology is fed by
conditional mass creation — probability flowing one way from the graviton
into its dipole partner — and any distinctive statement (e.g. scale-free
growth pattern, a cascade-direction asymmetry) must be dug out of Mannheim's
own solutions. Paper 4 already banks the safe version in one line (the
Deruelle-et-al linear-growth identification). Going further means fighting on
Mannheim's home field (conformal cosmology fits, contested data) for a
mostly interpretive payoff.
Effort: MONTHS.
Risk: HIGH (interpretation-only outcome likely; the fits themselves are
disputed territory).
Payoff: MEDIUM at best.
VERDICT: PARK — revisit only if item 2 (phase boundary) produces a growth-
rate discriminator for free.

--------------------------------------------------------------------------------
10. [SEED 5] THE alpha_g ~ 3e109 ARITHMETIC AS A STANDALONE NOTE
--------------------------------------------------------------------------------
Assessment: novelty confirmed twice (dedicated agent sweep + this run's web
check): NO numerical alpha_g exists in print, anywhere; the number is ours.
But: (a) the number's entire evidential weight depends on the face-value
flat-space inversion that Mannheim explicitly rejects (his anti-Yoon
argument), so a standalone note is a magnet for a one-line rebuttal ("wrong
premise, see 1506.02479"), whereas inside paper 4 it is armored — it is
presented as a FORK, and the fork is the point; (b) the headline juxtaposition
("the coupling conformal gravity needs is 10^109" next to the 10^120-flavored
naturalness lore) is a rhetorical, not scientific, increment. Keeping it in
paper 4 also keeps priority: the draft states it, dates it, and shows two
independent routes agreeing.
Effort: DAYS (that's not the issue).
Risk: LOW on prior art; MEDIUM-HIGH on reception.
Payoff: LOW as standalone; the arithmetic is already doing its full work in
Sec. 5 of paper 4.
VERDICT: DROP as standalone; keep in paper 4 (already done). Optional: a
sentence in paper 4's discussion flagging the number as previously unpublished
arithmetic, which it already effectively has.

--------------------------------------------------------------------------------
11. [SEED 8] THE "NO FOURTH POSITION" TABLE AS A LIVING FALSIFIABLE REGISTRY
--------------------------------------------------------------------------------
Assessment: cheap and genuinely useful as REPO INFRASTRUCTURE — a
TRILEMMA_REGISTRY.md in the main repo: every published escape route, its horn
assignment, its price, date-stamped; an open standing challenge ("submit a
fourth position"). Costs an hour to seed from Table 1 and minutes per new
paper (the 2025-26 wave — 2603.07150, 2604.21823, 2607.00096, 2605.01966 —
provides immediate entries beyond the table's eight). As a PUBLICATION it is
premature: living reviews earn their existence after the framework has
external uptake.
Effort: HOURS to seed; ongoing minutes.
Risk: NONE (registry); reputational only if oversold.
Payoff: LOW-MEDIUM — sharpens the falsifiability claim, gives referees a
target, builds the eventual review paper incrementally.
VERDICT: PARK-as-infrastructure — seed the registry file in the repo during
the paper-4 audit; DROP any near-term publication ambition.

--------------------------------------------------------------------------------
12. [NEW N4] PROCESS READING OF THE GHOST-vs-UNSTABLE-PARTICLE ANALYTIC
    DISTINCTION (Buoninfante 2501.04097 / 2606.18349)
--------------------------------------------------------------------------------
First concrete result: mapping proposition — first-sheet complex-conjugate
poles (Buoninfante's sharp discriminant of true ghosts from unstable
particles) correspond in the process currency to the broken-PT/terminal-
indivisibility class (complex energies = paper 1's exact closed forms),
while second-sheet resonances are ordinary open-system transients. Would give
the analytic-structure dichotomy a sample-space meaning and connect the
program to the most active current ghost-QFT thread.
Effort: 1-2 WEEKS.
Risk: MEDIUM — requires honest engagement with dressed-propagator analytic
structure, which is outside the program's demonstrated toolkit so far.
Payoff: MEDIUM — engagement value similar to item 5 but harder.
VERDICT: PARK — natural section of the eventual review; or promote if
Buoninfante's line keeps producing (watch 2606.18349's citations).

================================================================================
STRATEGIC NOTES
================================================================================
- SEQUENCING: items 1, 2, 3 share one mathematical core (Jordan structure,
  its unfolding, and its divisor image). Do them as ONE working block during/
  right after the paper-4 audit: item 1 lands inside paper 4; items 2+3
  together are the natural paper 5 ("The exceptional point as a phase
  boundary: unfolding directions, divisor mechanisms, and a photonic test"),
  with item 4 as its experimental section or a parallel proposal update.
  That is a coherent, low-risk, ~1-month arc entirely on ground the program
  already owns.
- The single most valuable DAY of work in this list: verify Smilga's block-
  growth structure (item 1 feasibility) + the 2x2 exhaustiveness check
  (item 3 feasibility). Both are go/no-go gates costing hours.
- EXTERNAL ENGAGEMENT: items 4 and 5 are where the program first touches
  communities that can respond (PT-photonics; the FMT/PU-quantization
  thread). Everything else is internal consolidation. After four papers of
  internal consolidation, one outward-facing artifact (the proposal update)
  is strategically overdue.
- WATCH ITEM: the EP-splitting-exponent literature (2509.02174 and the
  graph-theoretic PRResearch line) is moving fast and adjacent to items 1-2;
  re-sweep it at paper-5 kickoff.
