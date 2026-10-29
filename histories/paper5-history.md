# Process history — Paper 5 (choosing): "Conformal gravity must choose"

Sources: session record 2026-07-12 (direct), notes.md entries, git
history, research/t4_literature_triage.md, t4_vertex_conventions.md,
t4_threads_report.md. Commit-anchored throughout.

## Timeline

**Kickoff (user-directed choice of T4 over T5/T10).**
- Agent dispatched: literature triage (equal-frequency PU kinematics;
  quadratic-gravity ghost-decay rates; trilemma precedents). Run in
  background while the kinematic leg was computed inline.

**Kinematic leg (same hour, `t4_ep_dictionary.py`).**
- Per-mode EP scaling measured (cond = 2.00/delta over five decades);
  Stelle-dispersion UV sweep measured cond ~ k^5. **The k^5 was
  immediately suspected of a units artifact** and a dedicated
  units-only control (well-separated frequencies at the same k) was
  added BEFORE the number was logged: decomposition k^5 = units k^3
  x EP-driven k^2 (= inverse relative detuning). **Miss-averted
  4.1** — the headline exponent would have been misleading as first
  measured; caught by self-imposed control, same session.
- Process-side control: Hermitian grid realization doubly stochastic
  at the EP to 1.1e-14.

**Triage verdict (agent return).** Part A partial-favorable (a live
published standoff: Bender-Mannheim "unitary via nonstationary
states" vs Smilga "unitarity is broken"); Part B: GSTZ treat
4-derivative gravity only in the Planck-suppressed regime; the
pure-conformal rate lane CLEAR; Part C (trilemma) CLEAR, zero hits
for stochastic-process language in the corpus.

**Rate leg, first pass — CONTAINED A WRONG HEADLINE (Error 4.2).**
The first bound statement ("for ANY alpha_g within 8 decades of
unity, macroscopic-wavelength cutoff") implicitly assumed a
natural-sized coupling. A conventions agent (dispatched in parallel)
returned: no numerical alpha_g exists in print; face-value matching
to the rotation-curve fits gives |alpha_g| ~ 3e109, at which the
bound is VACUOUS. **Caught by: the parallel data-gathering agent,
same day; corrected to the alpha_g FORK before any draft existed.**
Notes entry explicitly marked "CORRECTION ... supersedes." The
correction strengthened the paper: the fork (vacuous-but-
observationally-dead vs macroscopic cutoff) closes the horn either
way. Also caught in the same return: the agent's own summary line
"Lambda^8/alpha_g^2" was a dimensional slip (E^8 for an E^4
quantity) — detected by dimensional analysis in the main session and
discarded; the underlying equations in the same report were
consistent.

**Quantum leg (`t4_jordan_process.py`).**
- No-representation lemma formulated + verified; BM-vs-Smilga
  adjudication; NEW mechanism found (one-way cascade; conditional
  mass creation). Two development-time defects caught by the
  script's own controls and fixed before commit: an asymptotic-
  window fit blowing up (machine-epsilon Jordan splitting turning
  polynomial into exponential — itself banked as EP physics) and a
  wrong expectation about the divisor mechanism (det-crossing
  expected; triangular structure found — became the new-mechanism
  result). **Miss-averted 4.3, error-become-result 4.4.**

**Draft v0.1 (10-11 pp) assembled**; bibliography explicitly flagged
as carrying agent-reported details needing audit re-verification.

**Audit cycle (four agents: bibliography, adversarial, independent
calc, threads scout — the scout at the author's request).**

- INDEPENDENT CALC: A-H all PASS; delivered analytic upgrades
  (DERIVED 1/delta law — the detuning is a non-generic unfolding,
  eigenvector angle linear in delta with angle/delta = sqrt5/2;
  sigma_max closed form; 1/(k-1)! prefactors; the mechanism
  dichotomy double-confirmed from both sides).
- BIBLIOGRAPHY: 21 OK, 11 fixes, 3 major. **Two chimera citations
  (Errors 4.5, 4.6):** one bibitem fused two Mostafazadeh papers,
  another fused three Mannheim papers (the correct target being his
  Comment-on-Yoon — both body claims survived on the corrected
  source). **One false quotation (Error 4.7):** "unitarity at the
  price of causality" appears in no Donoghue-Menezes paper —
  de-quoted and replaced with their verbatim words. A quoted phrase
  traced to a third Anselmi paper not in the bundle (added). The
  Smilga quote verified verbatim but needing scope ("said of the
  nonstandard realization" — added). A misattributed technical
  claim (per-mode linear growth: not in Deruelle et al., explicit
  in Hell-Lust-Zoupanos — reattributed). **Plus a program-level
  catch: the GSTZ title is hyphenated ("meta-stable?") — wrong in
  paper 2 as well, having SURVIVED ALL PRIOR AUDIT ROUNDS there
  (Miss 4.8); verified directly and fixed in both papers.** One
  audit-vs-audit conflict (RLW-style): the triage doubted the
  Ilhan-Kovner arXiv ID; direct verification showed the bibitem was
  right and the doubt wrong.
- ADVERSARIAL: **1 CRITICAL (Error 4.9, the paper's load-bearing
  wall): the Lemma's first proof step was FALSE** — "unistochasticity
  requires V unitary" fails as a matrix statement (counterexample:
  the singular Hadamard-modulus matrix). The audit was aimed at this
  exact step by name, and hit. The repair (Frobenius norm:
  column-stochasticity bounds ||V||_F = sqrt(n)) is two lines,
  STRICTLY STRONGER (now excludes all stochastic closed
  representations), and consistent with paper 1's definitions.
  **Root cause traced into PAPER 1 (Sec. 2, "doubly stochastic iff
  unitary" — only 'if' holds), where it had survived paper 1's four
  audit rounds (Miss 4.10); fixed there the same day.**
  Also: 3 major (abstract/intro "every field mode" overclaimed vs
  the spin-1 content — the body had been fixed mid-audit, the
  abstract not; the decay-channel schematic drew the wrong diagram
  (matter T at both ends) though the conclusion was robust — the
  repair added the scale-invariance derivation, a better foundation
  than the defect had; the horn table's "no fourth position" was
  undercut by its own Merlin row and a missing metastability route —
  row added, caption honestly hedged) and 8 minors (a reduced-vs-
  physical wavelength conflation, an understated Halmos error, a
  tier misfiling, undefined symbols including the load-bearing
  c_ps).
- THREADS SCOUT: ranked follow-up directions; identified the
  paper-5 arc; recommended dropping a standalone alpha_g note as
  indefensible alone.

**v0.2 (11 pp) — all findings applied same day.**

## Errors & misses ledger

| # | What | Introduced by | Caught by | Fate |
|---|---|---|---|---|
| 4.1 | k^5 headline (units-contaminated) | raw measurement | self-imposed units control, pre-logging | decomposed k^3 x k^2; derived |
| 4.2 | unconditional cutoff-bound claim | natural-coupling assumption | parallel conventions agent (alpha_g ~ 3e109) | superseded by the fork; noted as correction in notes.md |
| — | agent's Lambda^8/alpha_g^2 line | agent summary slip | dimensional analysis, main session | discarded; report flagged |
| 4.3 | conjugated-fit blowup | numerics of Jordan fragility | script control | replaced by exact inequality; fragility banked as physics |
| 4.4 | wrong divisor-mechanism expectation | analogy to dimer EP | script output contradicting it | became the new-mechanism RESULT |
| 4.5 | chimera bibitem (Mostafazadeh x2) | agent-reported details, undrafted verification | bibliography agent | dissolved to the real paper |
| 4.6 | chimera bibitem (Mannheim x3) | same | bibliography agent | corrected to Comment-on-Yoon; claims survive |
| 4.7 | false quotation (Donoghue-Menezes) | paraphrase drifted into quotes | bibliography agent | de-quoted; verbatim words substituted |
| 4.8 | GSTZ title hyphen (also paper 2) | typo, then audit blind spot | bibliography agent + direct verification | fixed in papers 2 and 4 |
| 4.9 | FALSE proof step in the Lemma | inherited from paper 1's "iff" | adversarial agent, aimed at the step by name | repaired to a STRONGER lemma |
| 4.10 | the same "iff" in paper 1, 4 audits old | original drafting | consequence of 4.9 | fixed in paper 1 v1.1 |

## Process events (high level)

prior-art searches: 2 (triage; conventions/quotes verification).
adversarial review: 1 (aimed, by name, at the weakest step — and it
hit). independent recomputation: 1 (all claims + analytic
derivations the main session hadn't done). threads scouting: 1
(author-requested). self-corrections before any external eye: 4
(4.1-4.4). human steering: chose T4, ordered the audit + scout,
asked for these histories. Status at write-up: v0.2, audit-clean,
optional in-window strengthening pending author decision.

## A note on the pattern

The two most serious defects (4.2, 4.9) were both caught by
mechanisms DESIGNED to catch them: a data-gathering agent dispatched
because the coupling value was flagged as unknown, and an
adversarial agent instructed to attack the proof's first step by
name. Neither would likely have fallen to a generic read-through —
4.9 had already survived four generic audit rounds in paper 1. The
transferable lesson for AI-led (and human-led) research: audits find
what they are aimed at; aim them.

## 2026-07-12 — RELEASE-GATE PASS 1 (three cross-model Opus agents).
NOT clean. Counter: 0. (Paper 4 had a pre-gate audit earlier this
session; this is its first cycle under the K=2 gate.)

All four central proofs re-verified AIRTIGHT (Frobenius Lemma 3.1 -
no false-iff residue confirmed; Prop 3.3 sector tower; Thm 3.5;
alpha_g + rate arithmetic). Findings are scope/consistency, not
broken math.

Claims (7): F1 MAJOR - the alpha_g fork is NOT exhaustive: an
unfixed intermediate alpha_g ~ 1e40 gives Lambda_max ~ 100 MeV
(particle-scale, neither vacuous nor solar-system-dead), so "Horn 1
untenable on either branch" needs an explicit naturalness prior to
close the ~8-decade gap. F2 cond=2/delta vs angle=(sqrt5/2)delta
coefficients unreconciled (cond*angle ~ sqrt5, unexplained). F3
cond=2/delta (absolute) vs UV k^2 (inverse-RELATIVE detuning) not
spelled out. F4 "no sample space at any coupling however weak"
overreaches free-theory theorems (hedge to free/kinematic limit).
F5-7 nits (provably->numerically; "bounded metric"->boundedly-
invertible; dual-functional "norm 1" imprecise).
Numerics (3): all traceability - sqrt5/2 angle & 1/(k-1)! prefactor
"measured" but not script-emitted (both independently reproduced
correct); 0.486 zero-step not emitted (correct, protocol-flagged).
Biblio (4): F1 MAJOR "B.~Wang"->"Q.~S.~Wang" (2308.12989) -
VERIFIED against arXiv before applying (fourth author = Qiu Shi
Wang); F3 added arXiv:gr-qc/0703037 to Mannheim2007 - VERIFIED;
F2 DM microcausality quote unconfirmed verbatim -> softened to
paraphrase (removed quote marks, safe). Zero chimeras; all other
verbatim quotes (Smilga, Bender-Mannheim, GSTZ x4, Anselmi, FMT,
Deruelle) confirmed EXACT.

APPLIED NOW (trivial + VERIFIED): Cline author, Mannheim arXiv ID,
DM quote->paraphrase. QUEUED for Fable (substantive, coordinate
with paper 6): alpha_g-fork naturalness prior (F1 claims), the
scope-hedges (F4), coefficient reconciliations (F2/F3 claims),
script-transparency (add sqrt5/2 + prefactor prints). CROSS-PAPER:
paper 6 referee finding-2 (conditional mass creation is sigma_max-
normalization-dependent) APPLIES TO PAPER 4's central k=2 result
too - must be treated together in the Fable rescoping.

## 2026-07-12 — GATE-PASS-1 RESCOPE APPLIED (Fable). v0.4.
Counter: 0 (content change). All queued findings addressed:

SHARED sigma_max (paper-6 referee F2): minimal-contraction
justification added to "what survives" (sigma_max = pointwise-least
normalization admitting a unitary dilation; discards nothing beyond
what the dynamics loses); M1-signs-invariant vs M2-column-sums-
convention-relative split stated; NEW minimality dichotomy
(crossing-free renormalization iff-bounded by c^2 >= c^2(0)
e^{kappa^2 t^2}; Gaussian conditioning vs polynomial dynamics;
divergent overhead) verified in t4_jordan_process.py [3b]; abstract
flags the convention.

F1 (alpha_g fork not exhaustive): the gap is now CLOSED EXPLICITLY
by a stated naturalness prior, new paragraph "The gap between the
branches, priced": Lambda_max ~ alpha_g^{2/5} puts lab-scale
content at |alpha_g| >~ 1e13 and a 100-MeV cutoff at ~1e40; the
evasion window 1e13-1e109 is unadvocated in print and excluded as
a PRIOR, honestly labeled (an observational closure is NOT
available: background-density substitution tightens only by the
fifth root, factor ~10). Abstract + horn-1 bullet + registry row
updated to name the prior.

F2/F3 (coefficient reconciliation): the sqrt5/2 angle coefficient
is now DERIVED (chain eigenvector (1, lam, gamma w1^2 w2^2/lam,
gamma lam^2); pair difference delta*(0,i,i,-2) vs v=(1,i,-i,-1)
gives angle = sqrt(6-1)/2 delta) and the cond-angle link is the
script-emitted identity cond(V)*angle -> sqrt5 (2.2363 vs 2.2361):
cond = sqrt5/angle = 2/delta — one law, not two. Absolute-vs-
relative detuning spelled out (per-mode law at omega=1; dispersion
cost follows delta/omega, isolated by the units control).

F4 hedge: "no sample space at any coupling however weak" ->
free/kinematic-level statement with explicit scope pointer.
Nits: "bounded metric" -> bounded metric with bounded inverse
(abstract); dual functional "(bounded, norm 1)" -> "(bounded)";
"provably never does" -> proof pointer to the triangularity
parenthetical. Script transparency: t4_ep_dictionary.py [1b] emits
the angle law + cond-angle identity; t4_jordan_process.py [1] now
emits 1/(k-1)! prefactors (1.0022/0.5044/0.1700 vs 1/0.5/0.1667).

Recompiled clean (13 pp). Gate pass 2 (three fresh agents) to
launch against v0.4.

## 2026-07-12 — GATE PASS 2 (three fresh Fable agents). NOT CLEAN.
Counter: 0. Totals: 13 findings (claims 4 MINOR + 5 NIT; numerics
1 LOW + 1 MEDIUM; biblio 2 LOW). ZERO critical/major. All proofs
re-derived again (lemma, tower shift-weights sqrt((s+1)(M-s)),
Fock-tower functional analysis, sqrt5/2 pair-difference, alpha_g
counting, all Lambda arithmetic incl. window endpoints); all 54
numbers traced clean; all verbatim quotes verified (one
quotation-mark hygiene issue); zero chimeras; prior-art survives
fresh refutation attempts (nearest new neighbor: Fring et al.
2506.21400, similarity-dictionary route — no overlap).

Fixed: "three"->"four" scripts (Code availability); zero-step
0.486 now BOTH emitted by t4_jordan_process.py (root of
2 t sigma^2 = (sigma^2)', prints 0.4859) and given its defining
equation in-text; Claim 6.1 carries the boundedness qualifier
(per-mode any similarity / Fock tower bounded-with-bounded-
inverse); Discussion "Measured" inventory flags the sigma_max
convention on conditional mass creation; "13-100 decades" ->
"tens of decades"; meV threshold honestly 3e12 (window statement's
"~1e13 <~" stands as approximate); abstract "every linearized
spin-2 field mode"; bridge sentence added after the tower
proposition (A = the +i omega Jordan cell of Sec 3's mode matrix);
abstract "This, we argue, adjudicates"; abstract quote marks
removed from the non-verbatim "unitary evolution via nonstationary
states" (body wording was already quote-free); Smilga2014 bibitem
set to published "Giving" title after direct Crossref verification
(DOI 10.1007/s10773-014-2404-2; % comment records the evidence;
same fix propagated to paper 6).

Recompiled clean (13 pp). Counter: 0. PASS 3 launching.

## 2026-07-12 — GATE PASS 3 (three fresh Fable agents). NOT CLEAN.
Counter: 0. Totals: claims 1 MAJOR + 4 MINOR + 3 NIT; numerics
1 MEDIUM + 1 MEDIUM + 1 LOW (52 traced, 51 pass); biblio 3 MEDIUM
+ 6 LOW (all quotes verbatim, zero chimeras; prior-art survives
with a proximity warning). All proofs re-derived AGAIN clean.

THE MAJOR (claims): the italicized post-lemma corollary ("no
closed probability representation on any beables AT ALL") claimed
a universality neither theorem delivers (lemma = finite-dim;
tower = bounded-with-bounded-inverse only). Fixed with explicit
qualifiers there + in the Discussion inventory + the lemma
statement now says "matrix on finitely many configurations".

Convergent MEDIUMs: t4_jordan_process.py docstring [3] described
the PRE-DISCOVERY expectation (det-crossing+negativity) that the
code/output/paper all contradict - rewritten to the conditional-
mass-creation mechanism. Dimer comparator "t~0.7" was the
UNIT-COUPLING value (1/sqrt2), not paper-1's canonical theta=pi/4
device (~1.0) - convention now stated in-text with the 1/(kappa
sqrt2) closed form (verified by direct computation). Face-value
alpha_g matching now SCRIPT-EMITTED (t4_rate_ladder.py: routes
4.1e109 / 3.1e109 from the research-doc constants); Code
availability sentence scoped accordingly + "three"->"four" (prior
pass) stands.

Biblio: two MIS-ANCHORED cites fixed (1/2 hT vertex no longer
attributed to Mannheim2011's text; zero-norm states re-anchored to
BenderMannheim2008PRD, "(dipole)" dropped at the attribution
point); Deruelle2012 dropped from the per-mode-linear-growth cite
(HLZ carries it; matches the original audit's reattribution that
had been incompletely applied); Steinwachs recharacterized as a
DIFFERENT triangle, not an edge. FOUR published-title fixes, ALL
verified directly via Crossref before applying (gate rule 7; two
REVERSED earlier "verified" forms that were arXiv artifacts):
GSTZ "metastable" (unhyphenated - reverses error-4.8's fix, which
had verified the arXiv form; propagated to paper 2), IK
"Ghost-turned tachyon" (one hyphen - propagated to paper 6 bibitem
+ both in-text coinages), Deruelle "vs.", Steinwachs serial comma.
% comments record the Crossref evidence in each bibitem.

Proximity literature (biblio F9) ENGAGED: four new
arXiv-verified citations with differentiating text - Fring-Taira-
Turner 2506.21400 (non-unitary similarity route = a similarity
dictionary, meets the lemma), Dey-Fring 2603.15395 (Bohmian
degenerate PU = deterministic-trajectory beables, complementary
to the stochastic lemma), Holdom 2408.04089 + Kuntz 2410.08278
(flagged as pending trilemma-registry classifications, not
adjudicated rows). "0.05-step protocol" clarified to base grid +
pair step (p6-pass-11 numerics observation). Sector exponents
labeled M=1,2,4,6,8. Abstract: linearized qualifier kept, "we
argue" hedge kept, solar-system sentence now "on published
(Mannheim-disputed) analyses". Dead code removed from
t4_ep_dictionary.py; rate-ladder printout carries the disputed
hedge.

Recompiled clean (14 pp). Counter: 0. PASS 4 launching (Opus
agents per the new model policy).

## 2026-07-12 — GATE PASS 4 (three fresh OPUS agents, first
## all-Opus pass under the model policy). NOT CLEAN.
Counter: 0. Totals: claims 3 MINOR + 2 NIT (zero math/numerical
errors; all four proofs re-derived clean again); numerics 1 MEDIUM
(~55 traced, ZERO manuscript discrepancies — the first
all-numbers-clean body in the paper's history; the lone defect was
in the CITED PROVENANCE FILE); biblio 3 findings (journal-version
upgrades only; zero factual/quotation/chimera defects; novelty
claims survive again).

Fixes applied:
- research/t4_vertex_conventions.md: the STALE PRE-CORRECTION rate
  template Lambda^8/a_g^2 (two places) corrected to the contact-
  rung Lambda^4/a_g^2 with the dimensional check recorded inline —
  the fossil of the same-day correction the paper itself records
  (error 4.2's ecosystem residue; fix-propagation lesson re-earned
  on a RESEARCH DOC surface).
- Provenance sentence + Code availability now scope the one-loop
  pole estimates as in-text analytic computations; the Discussion
  "Argued" inventory now files the Merlin-width resonance-EP
  statement.
- 18.8 MeV finding resolved by VERIFICATION, no change: two prior
  independent agents confirmed the number verbatim in
  ClinePhantom2024 (95% C.L. COMPTEL, their Eq. 3); in-text
  clarifier "(the latter being the 95% C.L. limit quoted in...)"
  added to make the attribution self-evident.
- Abstract horn sentence carries the free/linearized qualifier;
  opaque ghost-leg parenthetical replaced by the transparent
  vertex-vs-two-propagators count (a_g * a_g^-2 = a_g^-1).
- Journal versions added, ALL Crossref-verified before applying:
  Holdom NPB 1008, 116696 (2024); Kuntz CQG 42, 175003 (2025);
  Dey-Fring Universe 12(7), 200 (2026) (concurrent-month
  publication, DOI live).

Recompiled clean (14 pp). Counter: 0. PASS 5 to launch (Opus).

## 2026-07-12 — GATE PASS 5 (three fresh Opus agents). NOT CLEAN
## by three wording items: biblio CLEAN (first clean p5 lane;
## all 36 items + all quotes verified, novelty survives), numerics
## CLEAN (~50 traced, 0 failures, external anchors corroborated),
## claims 2 MINOR + 1 NIT.
Counter: 0. All proofs re-derived clean again (the claims agent's
own first hand-attempt at the sqrt5/2 derivation erred and the
paper's construction corrected it — the right failure mode).

Fixes applied:
- Bridge sentence (added pass 3) conflated the classical cell's
  +i omega with the one-particle Hamiltonian's real omega — now
  states A = Hamiltonian (real eigenvalue), inheriting the CELL'S
  NILPOTENT (eigenvalue differs by i^-1, nilpotent identical).
  Genuine catch on fresh text; no result touched.
- Reduced-measure power counting moved OUT of Theorem-grade into
  the Argued item alongside its vertex-parallel premise
  (s-flatness analytic-forced, slopes measured, premise argued).
- Naturalness-window lower endpoint unified at 3e12 (was quoted
  1e13 in one place, 3e12 in the other).

Recompiled clean (14 pp). Counter: 0. PASS 6 NOT LAUNCHED (user
hold: session limit). On resume: pass 6 on Opus; the two
mechanical lanes have now been clean twice in a row and claims is
down to wording-only — clean candidate imminent.

## 2026-07-13 — GATE PASS 6 (three fresh Opus agents). NOT CLEAN:
## numerics CLEAN (~55/55, all robustness checks), biblio 1 LOW,
## claims 1 MAJOR + 1 NIT. Counter: 0.

THE MAJOR — the deepest calibration catch since the pass-9
referee, a SIX-PASS SURVIVOR: the flagship "definite-
configurations seat does not exist at the conformal point"
(abstract iv, lemma corollary, Claim opening, Discussion
inventory) CONTRADICTED the paper's own horn 1 (ghosts +
configurations) and its own Sec-3 control — the Hermitian-
Ostrogradski realization IS a closed doubly-stochastic
configuration process at the EP (script [3], 1.1e-14), is NOT
similar to the Jordan Hamiltonian (diagonalizable vs defective),
and so was never touched by the lemma. What the lemma kills is
configurations FOR THE NO-GHOST (Jordan/PT) DYNAMICS. All four
loci rescoped: abstract (iv) "no-ghost quantization has already
picked ... while the Hermitian ghost realization keeps
configurations at precisely horn 1's price; we price both seats";
corollary now names the ghost realization as the different,
non-similar operator that keeps the seat; Claim opening =
"no-ghost kinematics removes the third ... configurations survive
only in the Hermitian ghost realization, never jointly with the
other two virtues"; Discussion Theorem-grade line scoped to "the
Jordan (no-ghost) dynamics". The trilemma is SHARPER for it: the
seat is not absolutely absent — it is never available jointly
with the other two virtues.

Also applied: NIT (bridge "nilpotent the same up to the scalar
i^-1, Jordan structure unchanged"); biblio LOW (Holdom
characterization rescoped to 0+1d models + the constructed-inner-
product mechanism, with the currency's own reading of that
construction as a sample-space exit). Numerics agent confirmed
the corrected conventions doc and independently re-verified the
one-loop arithmetic and the tower theorem's unboundedness
parenthetical (log-norm ~ M).

Recompiled clean (14 pp). Counter: 0. PASS 7 launching (Opus).

## 2026-07-13 — GATE PASS 7 (three fresh Opus agents). CLEAN.
## COUNTER: 1 — the corpus's first counter movement.

Lane verdicts: claims CLEAN (hostile from-scratch re-derivation of
every result — lemma, tower, sqrt5/2, alpha_g counting, Lambda_max
arithmetic, zero-step onset, sigma_max convention, one-loop; horn
logic of the pass-6 rescope confirmed "stated correctly
throughout"); biblio CLEAN (38/38 sub-entries vs publisher
records; both punctuation suspicions resolved IN THE MANUSCRIPT'S
FAVOR via Crossref; novelty survives again); numerics CLEAN on
manuscript+scripts (43/43) with ONE LOW finding in the CITED
PROVENANCE DOC ONLY (research/t4_vertex_conventions.md route-A
rounding 4.2e109 -> 4.15e109; the manuscript never quotes the
value; fixed same-hour).

ADJUDICATION (disclosed to user in-session): the gate rule defines
clean as "zero findings requiring a change TO THE MANUSCRIPT OR
SCRIPTS" (user-set, 2026-07-12). The sole finding touched neither;
its own impact statement was "none on the manuscript." Under the
rule's letter, pass 7 is CLEAN. Counter: 0 -> 1. (If the stricter
reproducibility-chain reading is preferred, reset to 0 — recorded
here so the choice is auditable.)

PASS 8 = the K-1 CONFIRMING PASS, run on FABLE agents per the
model policy. If clean: paper 4 is release-eligible (publish hold
still in force; corpus-wide prior-art sweep at hold-lift remains a
release condition).

## Pass 8 — 2026-07-13 (claims+numerics Opus, bibliography Fable)

COUNTER RESET 1 -> 0 (pass-7 counter=1 streak broken), and the
GATE ESCALATION CLAUSE FIRED: these findings existed during
declared-clean pass 7, so K rises 2 -> 3. User accepted the
escalation (2026-07-13) rather than re-scoping the clause to
MAJOR+. Model policy set the same day: counter-1 and counter-2
confirming passes run on Fable; routine passes on Opus.

- Numerics: CLEAN (all four scripts rerun, every quoted number
  traced).
- Claims: 1 MINOR — along the Stelle dispersion (w1=k,
  w2=sqrt(k^2+m2^2)) the detuning delta = w1-w2 is NEGATIVE; the
  text quoted delta(k) ~= +m2^2/2k. FIX: magnitude bars at three
  sites (|delta(k)| ~= m2^2/2k, (|delta|/k)^{-1}, complex detuning
  "of magnitude |m2^2+i gamma|/2k"). 1 NIT — "map onto the horns
  without remainder" overclaims; softened to "with no remainder we
  have been able to identify."
- Bibliography (Fable, confirming-grade): F1 MINOR — published PRD
  title of Donoghue-Menezes 1908.02416 carries the serial comma
  ("Unitarity, stability, and loops..."); VERIFIED against the raw
  Crossref JSON for DOI 10.1103/PhysRevD.100.105006 before
  applying (rule 7); comma inserted, %-comment records the
  governing record. F2 MODERATE — prior-art currency: Bateman-
  Turok, "Escape from Ostrogradsky via Hidden Ghost Parity,"
  arXiv:2607.00096 (June 30, 2026; Krein-space 4-derivative QFT,
  generalized Born rule) postdates the registry's newest paper
  entry and was uncited; VERIFIED against the arXiv abs page
  before applying (rule 7 — the paper is real, exactly as the
  agent described; it was already a PENDING registry row from the
  2026-07-11 threads scout). FIX: registered in the intro
  pending-classification sentence (Holdom, Kuntz, Bateman-Turok
  "all three"), new bibitem with %-provenance. Recommended-only:
  Kumar-Marto 2603.07150 (already a PENDING row) and Deffayet et
  al. 2604.21826 (verified real, companion to the row's
  2604.21823; added to the registry only, not the paper).
  Everything else clean: ~38 records, all quotations verbatim,
  no anticipation of the trilemma/sample-space vertex or the
  stochastic currency found by adversarial sweeps through July
  2026.
- BOILERPLATE (no counter effect, rule-3 exception, logged): the
  audit-gate provenance sentence added to the page-2 pledge; the
  sentence's gate description updated corpus-wide (papers 2, 3,
  5, 6, 8) from "two consecutive passes" to "three" after the
  K=3 ruling; AUDIT.md updated to match.

Recompiled clean (14 pp; papers 2/3/5/6/8 recompiled for the
boilerplate word). Counter: 0 of K=3. PASS 9 launching (Opus).

BOILERPLATE LOG (2026-07-13, rule-3 exception, no counter effect):
the audit-gate provenance sentence now reads "repeated adversarial
audit passes" (user request — the sentence should say the agents
are prompted as hostile referees, which they are); identical edit
across all seven papers, recompiled clean.

## Pass 9 — 2026-07-13 overnight (Opus x3)

- Numerics: CLEAN (~40 claims traced across all four scripts incl.
  t4_sector_tower; sqrt5/2 law independently re-derived from the
  chain eigenvector, not just refit; window edges 3.29e12/1.04e40
  recomputed by hand; no stale Lambda^8/alpha_g^2 predecessor
  anywhere; epsilon claims all honestly worded).
- Claims: 1 MINOR + 2 NIT, no correctness error. MINOR: cond=2/delta
  displayed with SIGNED delta in the abstract and Eq. (3.1) while
  the paper itself takes delta<0 along the Stelle dispersion —
  fixed to 2/|delta| at three sites + "(the law is even in the
  signed detuning)". NIT-1: "one cubic vertex against two 1/alpha_g
  propagators" is not a connected 0->4 topology — replaced with the
  topology-independent counting (vertex alpha_g, internal line
  1/alpha_g, canonical external leg alpha_g^{-1/2}: any V-vertex
  tree gives alpha_g^{V-(V-1)-2} = alpha_g^{-1}), consistent with
  research/t4_vertex_conventions.md. NIT-2 (fitted -0.993 alongside
  the exact -1): NO ACTION — text already states the -1 is derived,
  fit is corroboration.
- Bibliography: 1 MAJOR + 1 MINOR + 2 NIT. MAJOR (accepted,
  verified): Kumar-Marto direct-sum program unregistered —
  arXiv:2603.07150 + arXiv:2604.19707 ("Unitary Quadratic Quantum
  Gravity in 4D", v3 revised 2026-07-07, five days before
  manuscript date); BOTH abs pages verified before applying
  (rule 7); registered in the intro pending-classification
  sentence ("all four") + new bibitem + registry row updated.
  MINOR (verified, NO manuscript change): 18.8 MeV / 95% C.L.
  confirmed VERBATIM in the Cline-Puel-Toma-Wang body (Sec. II);
  %-comment records it. NIT "add 'The' to the PRL title":
  REJECTED by rule-7 check — Crossref record for
  10.1103/PhysRevLett.123.171601 has NO leading "The" (arXiv-side
  only); journal-led bibitem, publisher governs; %-comment added.
  NIT "Smilga year 2014": REJECTED — Crossref published-print is
  Nov 2015 (vol 54, issue 11, 3900-3906); 2014 is online-first;
  %-comment extended.

Recompiled clean (14 pp). Counter: 0 of K=3. PASS 10 launching
(Opus x3).

## Pass 10 — 2026-07-13 overnight (Opus x3)

- Numerics: CLEAN (~65 claims traced across all four scripts;
  Lambda^8 predecessor sweep empty; 2/|delta| evenness confirmed
  STRUCTURAL — mode matrix identically symmetric under w1<->w2).
- Claims: 1 NIT applied — angle law displayed sign-consistently
  as (sqrt5/2)|delta| (line 309; the abstract carries only the
  cond form, already |delta| from pass 9). 1 MINOR REJECTED with
  evidence: "gamma-ray bound scale" for the 18.8 MeV limit is
  CORRECT — the Cline-Puel-Toma-Wang body derives it from
  COMPTEL diffuse gamma-ray flux (verified pass 9 via ar5iv).
  All proofs re-derived clean again (eigenvector residual reduces
  to (lambda^2+w1^2)(lambda^2+w2^2)=0; t_c=0.48587 independent).
- Bibliography: CLEAN verdict; all %-comments independently
  re-confirmed (Smilga, GSTZ, both D-M, IK, Cline body quote).
  Optional registration ACCEPTED (free — pass already not-clean):
  ghost-confinement route registered as Oda2026, arXiv:2605.01966
  — RULE-7 CATCH: the agent attributed the paper to "Ozonder";
  the arXiv abs page says Ichiro Oda (v2 2026-06-27). Verified
  before applying; %-comment records the misattribution. Intro
  now "all five"; registry row split (Deffayet 2604.21823 own
  row, Oda own row). Deruelle "vs." NIT REJECTED: Crossref
  JHEP09(2012)009 title carries the period — bibitem correct.
  Barandes "stochastic--quantum" dash NO-ACTION (house style;
  consistent across corpus; two prior lanes accepted it).
  Prior-art: trilemma/lemma/currency unpreempted through
  mid-July 2026 (Gudder 2603.27369 checked — general dictionary,
  no ghost content, not required).

Recompiled clean (14 pp). Counter: 0 of K=3. PASS 11 launching
(Opus x3).

## Pass 11 — 2026-07-13 overnight (Opus x3) — CLEAN (counter 1)

- Numerics: CLEAN (~37 quantities traced; agent independently ran
  NEGATIVE-delta scans confirming the evenness claim empirically;
  Lambda^8 predecessor sweep clean again; one no-action wording
  observation on the script-emitted 1.11802 coefficient,
  "defensible as written").
- Claims: CLEAN (every proof re-derived from scratch a third
  consecutive time; strength ledger audited entry-by-entry; no
  false iff, no overreach, no sign issue; three no-action
  observations).
- Bibliography: CLEAN (all ~41 records + all %-comments
  independently re-confirmed; quotations verbatim; five pending
  routes complete; prior-art unpreempted through mid-July 2026).
  ADJUDICATIONS (disclosed): (a) Deruelle "vs." NIT re-raised and
  again rejected — the auditor conditioned it on "matching arXiv
  casing," but the bibitem is journal-first and Crossref's
  published title CARRIES the period (verified pass 10); no
  change. (b) Buoninfante 2501.04097 (ghost resonances, JHEP 02
  (2025) 186) assessed by the auditor itself as "diagnostic, not
  an escape route... does not belong in the trilemma registry...
  not required" — treated as no-action under rule 2; noted here
  so a future pass can revisit if the resonance-EP paragraph
  ever strengthens.

Counter: 1 of K=3. PASS 12 launching on FABLE (counter-1
confirming pass per model policy).

## Pass 12 — 2026-07-13 overnight (FABLE x3, counter-1 confirming)

COUNTER RESET 1 -> 0, and ESCALATION TRIGGER #3: the biblio
findings existed during declared-clean pass 11. K stays 3 pending
the user's morning ruling (see also trigger #2, paper 6 pass 17).

- Claims (Fable): CLEAN — zero findings. Every proof re-derived
  from scratch a fourth time (incl. sigma_max minimality iff,
  Gaussian-envelope necessity AND sufficiency, t_c=0.485868 by
  own brentq, full constants re-derivation of the naturalness
  window from independent rho_cr/t0). Three no-action
  observations (m_r vs m_2 identification; sqrt-eps defectiveness
  phrasing; 0.0497 grid rounding).
- Numerics (Fable): CLEAN — 62 claims traced, zero mismatches;
  own negative-delta probe (cond*|delta| -> 2.0000 at
  delta=-1e-4); grid/seed perturbations stable; Lambda^8 sweep
  clean again.
- Bibliography (Fable): 1 MINOR + 1 NIT. MINOR: the "(premise)"
  table row lacked its strongest 2026 QM-level representatives —
  Deffayet-Fathe Jalali-Held-Mukohyama-Vikman arXiv:2604.21823
  (unitary evolution, well-defined vacuum) and Ewasiuk-Profumo
  arXiv:2604.21348 (exact moment bounds). Both LONG-VERIFIED in
  this program (2604.21823 fetched directly 2026-07-13; both are
  paper-1 bibitems confirmed by two independent biblio passes) —
  added to the premise row + bibitems (mirroring paper 1's
  verified entries) + registry. Correctly assessed as premise-row
  reinforcement, NOT a sixth pending route. NIT: "contested this
  year" cited June-2025 FringTairaTurner — now "contested into
  this year". All 41 records + all 5 %-comments independently
  re-confirmed; prior-art clean through 2026-07-13; Buoninfante
  papers assessed no-action (covered by the Merlin row).

Recompiled clean (15 pp — premise-row text pushed it over the
14pp break). Counter: 0 of K=3. PASS 13 launching (Opus x3).

## Pass 13 — 2026-07-13 overnight (Opus x3)

- Claims: CLEAN (every proof re-derived a fifth time; 3 no-action
  NITs, one applied gratis: abstract now ~3x10^109 matching the
  body's coefficient discipline).
- Numerics: CLEAN (~50 quantities traced; negative-delta probe
  again; Lambda^8 sweep clean).
- Bibliography: 1 MAJOR + 1 MINOR, records themselves 43/43
  clean. MAJOR (accepted, rule-7 verified): the Shapiro-school
  complex-ghost bound-state / reflection-positivity route was
  unregistered against the "no remainder" claim — Asorey-KREIN-
  Pardina-Shapiro ("Krein" is co-author Gastao Krein, not the
  space — verified on the arXiv abs page), JHEP 02 (2026) 020 =
  arXiv:2511.15283 + JHEP 01 (2025) 113 precursor, BOTH JHEP
  records verified via Crossref before citing. Registered as the
  sixth pending route (intro "all six") + bibitem + registry row
  (horn-3-adjacent Merlin-like seat plausible). MINOR (accepted):
  premise row now also cites the classical foundation Errasti
  Diez-Gaset Rifa-Staudt 2408.16832 (bibitem mirrored from paper
  1's Crossref-verified entry). Buoninfante cluster again
  assessed no-action (third pass in a row).

Recompiled clean (15 pp). Counter: 0 of K=3. PASS 14 launching
(Opus x3).

## Pass 14 — 2026-07-13 overnight (Opus x3)

- Numerics: CLEAN (~48 traced; slopes within 3.6e-5 of integers;
  seed probe on the Fock-tower norm across seeds 0/42/123;
  evenness re-verified structurally; Lambda^8 sweep clean).
- Bibliography: CLEAN (all ~43 records + every %-comment
  independently re-confirmed, incl. AsoreyKPS DOIs and the
  Krein-is-a-surname note; quotations verbatim; prior-art clean —
  Santillan 2505.20597 and Felski-Fring-Turner 2505.07869
  assessed optional/no-action; a mis-fetched Kuntz record was
  itself refuted by Crossref, bibitem correct).
- Claims: 1 MINOR — the Discussion ledger's "the validity of the
  open (dilated) process THERE" grammatically scoped the claim to
  the Fock tower, where no sigma_max normalization exists; the
  process is proved only for the 2x2 Jordan cell. Fixed: "for the
  mechanical Jordan cell (Sec. lemma)". All proofs re-derived
  clean a sixth time (incl. sub-stochasticity (1+t^2)/sigma^2<=1
  proved analytically by the agent).

Recompiled clean (15 pp). Counter: 0 of K=3. PASS 15 launching
(Opus x3).

## Pass 15 — 2026-07-13 overnight (Opus x3)

- Numerics: CLEAN (~49 traced; agent's own negative-delta run;
  "eight decades" checked and found CONSERVATIVE).
- Bibliography: CLEAN (45/45 records; all %-comments held under
  independent re-check — incl. the agent initially suspecting the
  Steinwachs Oxford comma and then confirming the published
  Frontiers record CARRIES it, exactly the journal-first rule;
  six-route registry complete; Santillan 2505.20597 assessed
  horn-3-not-new-route, Doukas 2602.22095 Markovian-divisibility
  framework no-threat, Buoninfante again no-action).
- Claims: 1 MINOR — the italicized corollary "no Hermitian
  counterpart means no closed probability representation..."
  read as a general implication the lemma does not deliver (it is
  silent on decaying diagonalizable dynamics); rephrased so
  nondiagonalizability is named as the operative hypothesis and
  BM's phrase is its diagnosis for THIS dynamics. Sharper reading
  than pass 14's no-action on the same sentence — the stricter
  agent wins. Everything else re-derived clean a seventh time
  (t_c from an independent SVD; sector tower rebuilt at
  M=1,3,5,7).

Recompiled clean (15 pp). Counter: 0 of K=3. PASS 16 launching
(Opus x3).

## Pass 16 — 2026-07-13 overnight (Opus x3)

- Numerics: CLEAN (~46 traced; negative-delta probe again; the
  1.11802-coefficient phrasing no-actioned by a second agent;
  dimer theta=pi/4 value correctly identified as companion-lane).
- Claims: 1 NIT applied — omega in R now explicit inside the
  sector-tower proposition environment (it propagates to the
  tower theorem via "as above"; the growth conclusions need
  |e^{-i omega t}|=1). Everything else re-derived clean an
  eighth time.
- Bibliography: 2 MINOR (records themselves 43/43 clean; all
  %-comments re-held). Third pass to surface Santillan and
  Buoninfante; the recurring-flag ratchet + the "no remainder we
  have been able to identify" sentence decided registration.
  RULE-7: Santillan EPJC 85, 810 (2025) verified via Crossref
  (DOI 10.1140/epjc/s10052-025-14530-1; Crossref renders "Lsz",
  a title-case artifact — %-comment records it; the arXiv abs
  page lists no jref); Buoninfante 2605.29047 verified on the
  abs page. Registered as routes seven and eight in the intro
  ("all eight") + bibitems + registry rows (Santillan horn-3
  Salvio-Strumia dialect; Buoninfante horn-3-adjacent
  complex-pole family).

Recompiled clean (15 pp). Counter: 0 of K=3. PASS 17 launching
(Opus x3).

## Pass 17 — 2026-07-13 overnight (Opus x3) — CLEAN (counter 1)

- Claims: CLEAN. Ninth from-scratch re-derivation; the agent
  additionally derived the exact sector-norm growth
  ||e^{-iHt}v^M||^2 = sum t^{2k} M!/((M-k)!k!) ~ e^{t^2 M},
  confirming the tower theorem's parenthetical quantitatively;
  cross-checked the alpha_g counting in canonical normalization
  (same -1). One NIT explicitly no-action (intro roadmap sentence
  terser than abstract on the naturalness-prior window;
  "defensible as written").
- Numerics: CLEAN (~44 traced; refit probe showed the quoted
  -0.993 is the conservative fit; signed-detuning, grid, and
  print-contamination probes all negative).
- Bibliography: CLEAN (47/47; all %-comments upheld incl.
  Santillan "Lsz" artifact and AsoreyKPS; the Mannheim2011
  arXiv-page misread was caught by the agent itself and resolved
  via Crossref in the bibitem's favor; eight-route registry
  judged complete; Santillan follow-on 2602.20047 assessed
  same-cluster no-action).

Counter: 1 of K=3. PASS 18 launching on FABLE (counter-1
confirming pass per model policy).

## Pass 18 — 2026-07-13 ~02:50 (FABLE x3, counter-1 confirming) — INCOMPLETE

- Numerics (Fable): CLEAN (58 traced, zero discrepancies; gamma=2
  prefactor scope probe; constants recomputed from scratch).
- Bibliography (Fable): CLEAN (47 records; every %-comment
  re-verified; two fetch artifacts self-caught and resolved via
  Crossref in the bibitem's favor; prior-art sweep through
  2026-07-13 — Cline-Hell 2603.05683 examined and excluded as an
  attack-not-rescue; eight-route registry judged complete;
  optional enrichments noted no-action). ALSO FLAGGED (echoed in
  p6 pass-20): the public GitHub repos are 163 commits behind /
  placeholders — public sync is a PRE-CIRCULATION gate step.
- Claims (Fable): LANE DIED MID-RUN — session limit (resets
  4:50am America/Chicago). Partial transcript shows the mode
  matrix re-derivation had already matched. RELAUNCH the claims
  lane after reset; the pass verdict is HELD OPEN (two lanes
  clean, one incomplete). Counter remains 1 pending the relaunched
  lane.

## Pass 18 — CLOSED 2026-07-13 morning (claims lane relaunched post-limit)

COUNTER RESET 1 -> 0; ESCALATION TRIGGER #6 (finding existed
during declared-clean pass 17).
- Claims (Fable relaunch): 1 MINOR — internal provenance
  contradiction: the naturalness-window parenthetical called
  3x10^109 "the only in-print number" while lines ~686/~915 and
  the conventions doc correctly state NO alpha_g exists in print
  (it is our arithmetic on published fit parameters). Fixed:
  "the only value derivable from in-print fit parameters is our
  face-value matching 3x10^109". Everything else re-derived
  clean a tenth time (four no-action observations logged in the
  agent report, incl. the Fourier-convention hedge note).
- Numerics + biblio: CLEAN (ledgered at the checkpoint entry).

Recompiled clean (15 pp). Counter: 0 of K=3. PASS 19 launching
(Opus x3).

## Pass 19 — 2026-07-13 morning (Opus x3)

- Numerics: CLEAN (~43 traced; k=3000 probe correctly identified
  the double-precision cond ceiling as non-physics — the script's
  window is the honest range; 1.11802-label NIT no-actioned a
  third time).
- Bibliography: CLEAN (47/47; all %-comments re-verified incl.
  the new Santillan/Buoninfante/AsoreyKPS entries; another
  Mannheim2011 fetch-misread self-caught and resolved via
  Crossref; Fring-cluster extras assessed optional).
- Claims: 1 NIT applied — omega in R now stated inside the tower
  THEOREM environment ("as above (A = omega 1 + N ... omega in
  R)"); everything else re-derived clean an eleventh time.

Recompiled clean (15 pp). Counter: 0 of K=3. PASS 20 launching
(Opus x3).

## Pass 20 — 2026-07-13 morning (Opus x3)

- Numerics: CLEAN (~42 traced, 12th consecutive clean numerics
  lane; own negative-delta run again; fix-propagation clean).
- Bibliography: CLEAN (47/47; every %-comment re-verified; the
  Steinwachs-comma and Deruelle-"vs." NITs re-raised and again
  no-actioned — the published records govern and carry both, per
  three prior Crossref checks; eight-route registry confirmed
  internally consistent).
- Claims: 1 NIT applied — the tower theorem's parenthetical
  claimed the hypothesis forces e^{-iHt}S^{-1}e_j in ell^2, which
  is not proved; replaced with the a-fortiori clause (outside
  ell^2 the column sum is infinite, so the conclusion holds
  regardless) — strictly more honest AND stronger. One deep
  no-action observation logged: the energy-density bound goes
  vacuous at ~1.6e90, inside the stated window — the naturalness-
  prior closure is unaffected and the text already concedes
  exactly this.

Recompiled clean (15 pp). Counter: 0 of K=3. PASS 21 launching
(Opus x3).

## Pass 21 — 2026-07-13 morning (Opus x3) — CLEAN (counter 1)

- Claims: CLEAN, zero findings (12th re-derivation; the agent
  caught and corrected its OWN chain-rule slip before reporting —
  direct matrix simulation confirmed t_c=0.4859; noted the cond
  lower bound is actually PROVABLE via Van der Sluis, so the
  "Measured" filing under-claims — no-action).
- Numerics: CLEAN (~40 traced; M=8 exponent verified genuine by
  pushing t to 30000 and recovering exactly 8!; nilpotency exact
  so no eps-splitting artifact).
- Bibliography: CLEAN (47/47; Steinwachs-comma NIT moot — four
  Crossref checks on record confirm the published title carries
  it; Buoninfante-2501/Fring-extras again assessed
  defensibly-omitted).

Counter: 1 of K=3 (third return). PASS 22 launching on FABLE
(counter-1 confirming pass per model policy).

## Pass 22 — 2026-07-13 morning (FABLE x3, counter-1 confirming)

COUNTER RESET 1 -> 0; ESCALATION TRIGGER #8 (biblio findings
existed during declared-clean pass 21).
- Claims (Fable): CLEAN, zero findings (hand-solved t_c
  0.485868; rebuilt the dimer EP from scratch; power counting
  re-derived two independent ways).
- Numerics (Fable): CLEAN, 63/63 (fit-window perturbations;
  onset-tolerance perturbations; k=3000 float-ceiling probe
  documented for future auditors).
- Bibliography (Fable): 2 MINOR + 2 NIT.
  F1 (reorg-exception, counter-neutral per the user ruling but
  applied now): companion/code URLs updated to canonical pNN-
  names; provenance pointers -> ghosts-program hub; the
  public-artifact push re-confirmed as a hard pre-circulation
  gate step. F2 (ordinary MINOR, accepted): the premise row used
  Smilga's own term "benign ghosts" without citing him — 
  Smilga2005 (NPB 706, 598 (2005), hep-th/0407231, mirroring
  paper 1's verified record) added to the row + bibliography.
  F3/F4 (NITs, accepted — stricter-agent-wins over earlier
  no-actions): Barandes2023 title en-dash -> published hyphen
  (LSE Press/Crossref/arXiv agree); DeyFring2026 title hyphen ->
  published MDPI en-dash; both now carry governing-record
  %-comments. Prose en-dashes remain house style.
  Prior-art: eight routes still complete; Doukas/Fring-extras/
  Ghilencea-cluster all examined and excluded with reasons.

Recompiled clean (15 pp). Counter: 0 of K=3. PASS 23 launching
(Opus x3). Note: F2-F4 existed during pass 21's declared-clean
biblio — the same-lane Opus agents accepted what the Fable lane
did not; logged for the cross-model dataset.

## Pass 23 — 2026-07-13 (Opus x3) — closed

Numerics CLEAN, biblio CLEAN, claims 1 borderline NIT applied
preemptively (real-eigenvalue qualifier at abstract + intro
roadmap — the p6-pass-22 missing-qualifier class). Counter 0.
Opus dry streak resets to 0 (accepted finding). PASS 24 launching
(Opus x3).

## Pass 24 — 2026-07-13 (Opus x3) — INCOMPLETE (wind-down kill)

- Claims: CLEAN (real-eigenvalue qualifier re-verified as placed
  and load-bearing; exact sector norm (1+t^2)^{M/2} derived).
- Numerics: CLEAN (~46 traced; own negative-delta probe; Lambda^8
  propagation clean).
- Bibliography: KILLED mid-run at the user's wind-down; last
  report had cleared the two prior-art candidates as follow-ons
  and was on "one title-punctuation question" — unresolved, lost.
  Pass 24 INCOMPLETE, does not adjudicate. Counter remains 0
  (pass 23) pending a fresh pass next session.

## Pass 25 — 2026-07-13 (Opus x3) — closed

- Claims: CLEAN + 2 NITs. "the Fock tower" summary in the ABSTRACT
  now "a conformal mode's Fock tower" (the theorem is one-mode;
  body sites already carry a nearby "per mode" qualifier) —
  preemptive, missing-qualifier-in-summary class. Eq.(1) "=" vs
  "≃" left (author's stylistic call; no-actioned across many
  lanes).
- Numerics: CLEAN (~50 traced; 16th consecutive clean numerics
  lane; deterministic double-run).
- Bibliography: 1 MINOR — Felski-Fring-Turner arXiv:2505.07869
  (MPLA 41, 2650019 (2026), DOI 10.1142/S0217732326500197)
  REGISTERED in the Fring-cluster intro list after THREE passes
  re-flagged it (p1 p13, p5 p23, p5 p25); rule-7 verified via
  arXiv abs before adding; %-comment records it as a
  bi-Hamiltonian PU-representation route, cluster representative-
  not-exhaustive. Does not touch the eight QFT-route registry.
  The prior "one title-punctuation question" resolved CLEAN (all
  six flagged punctuation items re-confirmed vs raw Crossref).

Recompiled clean (15 pp). Counter: 0 of K=3. Opus dry streak
resets to 0 (accepted findings this pass). PASS 26 pending.

## Rescope-integrity re-audit — 2026-07-13 (Opus x1, UNCOUNTED)

User-directed confirmation of the gate-pass-1 rescope (v0.4), NOT a
counter pass — counter stays 0. One hostile-referee agent, no
histories/notes access, original findings supplied verbatim; re-derived
the fix sites and re-ran t4_ep_dictionary.py / t4_jordan_process.py.
ALL RESOLVED:
- F1 (MAJOR, alpha_g fork non-exhaustive): evasion window named
  (3e12 <~ |alpha_g| << 1e109), excluded as an explicitly STATED prior
  (not data); observational non-closure volunteered (fifth-root /
  factor-~10); abstract + horn-1 bullet + closing separate branch-death
  from window-exclusion; alpha_g^{2/5} arithmetic consistent.
- F2 (MAJOR, shared sigma_max): flagged at abstract/body/Measured
  inventory; minimality justification correct; Fock tower kept distinct.
- F2/F3-coeff: sqrt5/2 derived in-text; one-law framing; [1b] emits
  cond*angle = 2.2363 vs sqrt5 = 2.2361 (verified by re-run).
Borderline: intro summary line + Table 1 horn-1 cell omit the window —
judged acceptable summary compression (governing bullet carries the
qualifier). No residue. No edits applied. Verdict: horn-1 closure and
conditional mass creation read honestly-scoped-not-asserted.

## Pass 26 — 2026-07-13 (OPUS x3) — NOT CLEAN (counter stays 0)

Opus dry streak stays 0 (Opus lane produced accepted findings).

- Numerics: CLEAN. All 4 t4_*.py rc=0; ~50/50 traced and matched;
  no epsilon-as-exact, no grid artifacts, no untraceable numbers; no
  MC estimator (deterministic trapezoid) so no prior-echo risk. Two
  no-action: "~130 m" is a 1-sig-fig round of 126 m under "~"; the
  sign-evenness of the 2/|delta| law is asserted + independently
  verified (cond(-d)/cond(+d)=0.990..0.99990) but the shipped [1]
  scan is one-sided (optional).
- Bibliography: CLEAN. ~50 bibitems / ~65 papers verified vs
  Crossref/arXiv incl. all future-dated 2026 IDs; published-title
  cases (GSTZ "metastable", Smilga "Giving", IK "Ghost-turned", DM
  serial comma) all correctly track the publisher record; every
  in-text quotation verbatim; novelty claims hedged, no closer prior
  art. One INFO: ClinePhantom2024 "18.8 MeV" in-body figure behind a
  paywall, consistent with the abstract's <~19 MeV (rests on prior
  verification).
- Claims: 6 findings VERIFIED then FIXED (rule 7); 1 no-action; 5
  confirmed-sound (Lemma 2.1, Prop/Thm 3.5 proof, sector tower,
  kinematics angle law, rate arithmetic all re-derived independently).
    F1 (MINOR) field-level exclusion framing: the bounded-inverse
      hypothesis of Thm 3.5 (thm:tower) looks like it dodges the
      physically-realized (collapsing/unbounded) PT metric. FIX: added
      one sentence (:439) noting the per-mode lemma carries NO
      boundedness hypothesis (finite-dim modes), so it already covers
      the physical mode-by-mode dictionaries; Thm 3.5 buys only the
      general sector-mixing field-dictionary case. Correct + additive;
      no new science.
    F2 (MINOR) ":696 'two independent routes agree to order unity'
      overstates -- routes A=Msun/(8 pi g*), B=3Msun/(32 pi g*) share
      inputs, differ by a FIXED 4/3 (numerics agent: 4.1 vs 3.1e109,
      ratio 4/3). FIX: 'two normalization conventions differing by a
      fixed factor 4/3'.
    F4 (MINOR) abstract :49 'cond=2/|delta|' is dimensionful (cond is
      dimensionless) and asymptotic; the BODY already scopes it (fixed
      omega=1 / relative detuning delta/omega, :328-331) but the
      abstract dropped the caveat. FIX: abstract -> 'cond -> 2 omega/
      |delta| in the relative detuning'. Body/Eq (2) left (already
      derived + scoped).
    F5 (MINOR) abstract :63 'adjudicates' contradicts the paper's own
      intro ('dissolves into two currencies', :226/:606) and
      Discussion ('an interpretation of their formalism, not a
      theorem', :907-910). FIX: 'adjudicates' -> 'recasts' (internal
      consistency, no new claim).
    F6 (MINOR) Sec-3 title 'conformal gravity lives at the exceptional
      point' reads unrestricted; the body restricts EP claims to the
      spin-2 sector everywhere else (:216-219, :283-286, abstract).
      FIX: title -> "conformal gravity's spin-2 sector lives at the
      exceptional point". Paper title untouched.
    F7 (NIT) undefined P_2, xi, N_eff, m_r, Gamma_M. FIX: added brief
      glosses at first use (P_2 the TT spin-2 projector; m_r real pole
      mass; xi ghost-matter coupling; N_eff effective loop
      multiplicity; Gamma_M = gamma/m_r).
    F3 (MINOR, NO ACTION) Gamma/gamma symbol overloading: the Gamma
      variants are typographically decorated (Gamma(t), dGamma(.),
      Gamma/V, Gamma_M) and gamma's two uses are section-separated and
      never collide in one formula -- disambiguated in context; a
      rename would be an invasive, risky diff for no correctness gain.
      Logged, no change (not counter-affecting).
- No REJECTED/refuted auditor leads this pass (all leads valid).

Counter: stays 0 of K=3 (F1/F2/F4/F5/F6/F7 counter-resetting).
Recompiled clean (16 pp); log shows no errors, no undefined
refs/citations. Opus dry streak stays 0.

## 2026-07-13 — GATE PASS 27 (three fresh Opus agents). NOT CLEAN (claims).
Fresh-eyes Opus x3 (claims/numerics/biblio), no histories/notes;
numerics given absolute output paths, biblio given raw-Crossref
instructions. Part of a user-directed "do more" batch (p1+p5+p6 same
session).

**Claims — NOT CLEAN (2 MINOR; both VERIFIED then FIXED, rule 7).**
The three genuine theorems (Lemma 5.1, Prop 5.4, Thm 5.5)
independently re-derived and confirmed; sqrt5 EP identity,
k^5=k^3 x k^2 UV decomposition, one-loop Merlin width, alpha_g
counting, rate/cutoff arithmetic, and the t_c=0.486 onset all
re-checked sound. Two applied:
  F1 (MINOR) :375 labeled the diagonalizable Hermitian object at the
    exact conformal point the "Hermitian (Ostrogradski) realization"
    -- but a Hermitian operator is diagonalizable while the confluent
    Ostrogradski H at omega1=omega2 IS the Jordan block, and the
    paper's own :453-454 already calls this Hermitian realization "a
    different operator not similar to the Jordan one." Internal
    contradiction. FIX: dropped "(Ostrogradski)"; added the "a
    different operator not similar to the confluent Jordan one"
    qualifier inline at :375, matching :453-454. (Abstract echoes
    :52/:89 already read "Hermitian ghost realization" -- clean.)
  F2 (MINOR) abstract :57 "the lemma lifts to the field level" is
    mildly broader than the result (a single free mode's Fock tower;
    Discussion :946-951 scopes to the free flat-space tower only).
    FIX: "the field level" -> "the free field level".
- Two NITs NO-ACTION (not auditor errors): F3 Deruelle table-horn vs
  prose "two-horn special case" (the auditor itself judged "not a
  contradiction"; cosmetic); F4 Lemma 5.1 lead clause broader than
  the proved real-eigenvalue case (the parenthetical already carries
  the hypothesis -- auditor said "no change strictly needed"). Logged
  here, not counter-affecting; nothing for auditor-error-log.md.

**Numerics — CLEAN.** All four t4_*.py rerun clean (Py 3.14,
NumPy/SciPy); every quoted number traced to its script or a
hand-checkable in-text derivation (cond=2/|delta| slope -0.993;
cond x angle = sqrt5 = 2.2361; Stelle k^5 = k^3 x k^2; growth
exponents 1/2/3/.../M; two-route alpha_g 4.1e109 vs 3.1e109 = 4/3;
Lambda_max, window thresholds 3e12 / 1e40, 20 m / 130 m wavelengths;
108.3 MeV phantom anchor). No discrepancies.

**Bibliography — CLEAN.** 49 bibitems; 46 verified vs Crossref-by-DOI
+ arXiv, 3 are the author's own GitHub companions (unindexable). All
titles/authors/years/venues/volumes/pages match; every cite resolves
(incl. Companion3 :153), no orphans/undefined, topical fit correct.
Curation notes (LSZ vs Crossref "Lsz"; Smilga "giving"/2015 print
year; en-dash cases; Smilga2005 p.598 not p.411) all independently
re-confirmed correct.

Recompiled clean (16 pp); log shows no errors, no undefined
refs/citations. No auditor leads rejected (nothing for
auditor-error-log.md). Not CRITICAL/MAJOR and no prior-fix reversal,
so nothing for major-findings-ledger.md.

**Counter move:** claims had applied findings -> resets to 0; biblio
and numerics both CLEAN -> +1 each. After pass 27: **claims 0/4,
biblio 1/3, numerics 1/3.** Opus dry streak stays 0 (claims lane not
clean).

---

## 2026-07-13 — PASS 28 (Fable x3; user-directed "do more" batch p1+p4+p5+p6)

Fresh-eyes Fable x3 per the per-lane cadence (claims flips Opus->Fable;
biblio & numerics at counter 1 -> Fable = all-Fable pass). No
histories/notes; numerics absolute output paths + standalone-only;
biblio raw-Crossref; claims adversarial framing + a compact-output
guard (see agent-control note).

AGENT-CONTROL NOTE: the p5-claims Fable agent FAILED on first launch
("Request timed out", 0-byte transcript, nothing recoverable) and was
relaunched fresh with a hard compact-output instruction; the relaunch
returned cleanly. (Companion failure this session: p1-claims overran
the 64k output cap, also 0-byte, also relaunched.)

**Claims — NOT CLEAN (2 MINOR + 3 NIT; 1 applied, 3 HELD for author,
1 no-change).** All numbers/proofs re-derived clean by the auditor
(sqrt5/2 pair-angle + cross-pair Gram giving the 4x4 coeff 2.00 vs
isolated 4/sqrt5; k^5=k^3*k^2; Lemma 4.1 Frobenius; Prop 4.2 shift
nilpotency; Thm 4.3 dual-functional; (1+t)^M sector norms; divisor
column sum; Gaussian envelope nec/suff; t_c=0.486; alpha_g^{-1}
counting; Lambda_max scalings; 20 m/130 m). No CRITICAL/MAJOR; the
alpha_g fork is exhaustive (window closed by a STATED prior, both
endpoints exact). Dispositions:
  F4 (NIT, APPLIED) :519-521 Thm 4.3 hedge "the column sum is
    infinite": when e^{-iHt}S^{-1}e_j not in l^2 (S bounded) the matrix
    element is not even defined. FIX: "undefined or infinite".
  F3 (NIT, NO CHANGE) abstract :53-56 "under any similarity
    whatsoever": subject is a (finite) Jordan-block Hamiltonian and the
    next clause already lifts to field level WITH the bounded-inverse
    qualifier; body :444 already says "per (finite-dimensional) mode".
    Distinction already drawn -> adequate.
  F1 (MINOR, HELD for author) :446-450 "each mode is finite-dimensional
    ---so it already covers the physically realized mode-by-mode
    dictionaries." A single field mode's Fock tower is INFINITE (the
    paper itself says so at :58, "a conformal mode's Fock tower"); the
    finite object is the M-quantum SECTOR. Realized Gaussian dictionaries
    (BM e^{-Q/2}, FTT) are unbounded and mix M-sectors by +-2, so the
    per-finite-sector lemma does not directly cover them (the intended
    Gaussian/symplectic-avatar reduction is sound but unstated).
    HELD: the word "mode" is used in BOTH senses across the paper
    (:58 infinite tower vs :444 "(finite-dimensional) mode"); resolving
    this needs the author's operator-theory/terminology call, not a
    guessed edit. Auditor's safe option: weaken to "covers the
    quadratic-level avatars of the realized dictionaries."
  F2 (MINOR, HELD for author) :563-566 / :626-632 (adjudication) /
    abstract :64-67: sigma_max-normalized contraction + Halmos dilation
    exist only per finite cell/sector; on the Fock tower ||e^{-iHt}||=inf
    (sector norms ~(1+t)^M, sup diverges) so no global normalization
    makes tower evolution a contraction and "the dilation" is not a
    single field-level object. The BM adjudication applies "the
    conditional bookkeeping of the dilated open process" to BM's tower
    construction without saying "sector-wise." HELD: auditor's fix is a
    one-clause "per-sector on the tower" qualifier; deferred to author
    (same tower/sector-scope subtlety as F1).
  F5 (NIT, HELD for author) :665-668 (scope :776-779): the external
    "ghost-graviton pair" at the exactly degenerate point lives in the
    nondiagonalizable tower (Prop 4.2), so the golden-rule rate is
    strictly the epsilon-split-pole limit (smooth here). Auditor: one
    clause stating the limit convention. HELD (physics clause; author).

**Numerics — CLEAN (1 NIT held-nominal, 1 deferred).** All 4 t4_*.py
reproduced (cond(V)=2/|delta|; sqrt5/2 angle 2.2363 vs sqrt5=2.2361;
Jordan exponents 1/2/3/4/6/8; alpha_g routes 4.1e109/3.1e109 ratio 4/3;
Lambda_max/wavelength ladder). NITs:
  grid-step (:592-593) "base grid and pair step are both 0.05": the
    pair step is exactly 0.05; the base grid linspace(0.1,8,160) is
    0.0497. HELD as NOMINAL-correct (0.6% vs the stated design
    resolution; zero numerical impact; no script-internal
    contradiction, unlike the p6 docstrings that disagreed with their
    own output). No change; lane clean.
  packaging (research/t4_vertex_conventions.md path) DEFERRED to the
    held assembly batch (verify the per-paper repo ships it).

**Bibliography — CLEAN.** 49/49 verified vs Crossref/publisher; zero
corrections. Pre-existing %-comment cases (GSTZ "metastable", Smilga
"Giving"/2015, Donoghue serial comma / "The", Dey-Fring en-dash,
Santillan "Lsz", Felski-Fring-Turner "Ghost-free" casing) all
re-confirmed. Verbatim in-text quotes (GSTZ, Smilga2008, Anselmi,
FMT2026, Cline 18.8 MeV) all supported.

Recompiled clean (16 pp); log shows no errors/undefined. No auditor
leads rejected (held items are author-adjudication scope residue, not
refuted; F3 judged adequate). Not CRITICAL/MAJOR, no prior-fix
reversal -> nothing for major-findings-ledger.md.

**Counter move:** claims applied a finding (F4) -> stays 0; biblio
CLEAN -> +1; numerics CLEAN (NITs held nominal/deferred) -> +1.
After pass 28: **claims 0/4, biblio 2/3, numerics 2/3.**

### 2026-07-13 (same day, follow-up) — HELD claims findings F1/F2/F5 APPLIED after independent review

The pass-28 held items were adjudicated by a fresh independent Fable
reviewer (read paper5/main.tex only, no histories/notes). Its verdict:
all three valid at flagged severities (F1 MINOR, F2 MINOR, F5 NIT), the
mode-vs-sector ambiguity is GENUINE but LOCALLY fixable (only the
:446-450 sentence attaches a finiteness claim to "mode"), no global
reconciliation needed -> apply all three now, none needs the author.
User (author) approved. Applied (verify-before-apply; labels prop:tower
:468 / thm:tower :509 confirmed):
  F1: :443-450 "each mode is finite-dimensional ... covers the
    physically realized mode-by-mode dictionaries" -> "each M-quantum
    sector, like the mechanical mode matrix itself, is finite-
    dimensional ... covers the quadratic-level avatars of the realized
    dictionaries and every sector-preserving field dictionary"; and the
    :444 clause "per (finite-dimensional) mode" -> "at the (finite-
    dimensional) quadratic level, sector by sector on the tower". Two
    echoes harmonized: Claim 6.1 :797 "per mode"->"per sector";
    Discussion :907 "per mode"->"per sector".
  F2: Sec 4.2 opening :564 added a scope clause ("(for the mechanical
    cell, and sector by sector on the tower---H preserves each finite
    sector ... no tower-wide normalization exists, by the unbounded
    sector norms of Theorem~\ref{thm:tower})"); adjudication bullet
    :628 "the dilated open process" -> "... (read sector-wise on the
    tower)".
  F5: Scope paragraph :777 added "with the exactly degenerate external
    pair understood as the smooth delta->0 limit of the split-pole
    spectrum (the degenerate tower of Prop.~\ref{prop:tower} has no
    stationary final-state basis at delta=0)".
Recompiled clean (16 pp; both new \ref resolve). Counter-neutral (claims
already at 0 from pass 28). No longer any p5 author-review backlog.

---

## GATE PASS 29 — 2026-07-13 (claims Opus; biblio+numerics Fable; user-directed p1/p5/p6 batch)
Per-lane cadence: claims flips Fable->Opus (adversarial); biblio & numerics
at counter 2 -> Fable. Fresh-eyes, compact-output guard.

**Claims — NOT CLEAN (1 MINOR + 2 NIT, all applied, all verified).** All
formal results re-derived clean (lem:jordan, prop:tower, thm:tower,
claim:choose, cond=2/|delta| + sqrt5 angle identity, alpha_g vertex power-
counting alpha_g^{-1}, Lambda_max ~ alpha_g^{2/5} window arithmetic
3e12/1e40, one-loop complex-detuning suppression, Halmos dilation). No
false converse, no half-domain generalization; abstract<->body scope tight.
  MINOR (APPLIED) :298-303 "the eigenvector-matrix condition number ...
    lower-bounds the conditioning of ANY similarity dictionary" overstates:
    cond(V) is column-scaling-dependent, not a scaling-invariant lower
    bound. FIX: attributed the divergence to the scaling-invariant angle
    between the merging eigenvectors ("which no column rescaling can
    repair"), which legitimately lower-bounds every dictionary up to O(1).
  NIT (APPLIED) :276-79 spin-2 propagator written prop P2/(alpha_g k^4) in
    Sec 3 but the rate-matching :714 uses 1/(2 alpha_g k^4). FIX: at first
    use noted the overall constant is fixed below, where the flat-space
    exchange is written 1/(2 alpha_g k^4) (ties the two loci; the "prop"
    was not wrong, and the 4/3 note at :716 is a separate convention pair).
  NIT (APPLIED) :497-98 Prop 3.3 "+i omega Jordan cell (one of its two
    conjugate blocks)" stated as inheritance; FIX: flagged as "the
    positive-frequency one" (the modeling selection).

**Numerics — CLEAN.** All 4 scripts rc=0; ~45 values traced, all match
(cond 2.00/|delta| fitted power -0.993; sqrt5=2.2361; UV/units/EP powers
k^5/k^3/k^2; Jordan exponents 1/2/3 + prefactors 1/(k-1)!; rate-ladder
slopes 2/4/2, 4/3 face-value ratio, Lambda_max 9.8e-9 eV, window endpoints
meV@3e12 / 100 MeV@1e40). 2 NITs held no-action (t4_rate_ladder stale
docstring phrase; base-grid step ~=0.05 rounding-level description).

**Bibliography — CLEAN.** 49/49 items verified vs Crossref/arXiv; all 3
companion GitHub URLs HTTP 200 (p04/p06 CREATED this session -- see below);
no chimeras/wrong-author/vol-page-year/DOI errors; every cite resolves;
%-comment provenance re-verified; 2026 preprints all real. 2 style NITs
(year-placement harmonization on arXiv-only entries; AsoreyKPS optional
arXiv id) held no-action.

Recompiled clean (16 pp); log clean (no errors, no undefined refs/cites).
No CRITICAL/MAJOR, no prior-fix reversal, no rejected leads.

**Counter move:** claims applied -> reset to 0; numerics CLEAN -> 2->3 =
**CERTIFIED (K=3)**; biblio CLEAN -> 2->3 = **CERTIFIED (K=3)**. After pass
29: **claims 0/4, biblio 3/3 CERT, numerics 3/3 CERT.** Publish HELD.

## 2026-07-13 — AUDIT PASS 30 (three fresh FABLE agents). NOT CLEAN (claims).
Per-lane cadence: claims Fable (adversarial); biblio+numerics Fable guard
(both CERT). Fresh eyes, no histories/notes.

**Claims — 3 MINOR + 2 NIT (no CRITICAL/MAJOR). 1 MINOR + 1 NIT APPLIED;
2 MINOR HELD FOR AUTHOR.**
APPLIED:
- MINOR (Sec 5 amplitude form): "any tree-level 0->4 massless amplitude is
  s^0 f(alpha_g)" asserted angle-*independence*; scale invariance only fixes
  the overall Mandelstam degree. FIX: s^0 f(alpha_g; t/s, u/s) + clause
  "scale invariance fixes the overall Mandelstam degree, not the angular
  dependence." (Contact-rung assignment unaffected -- only overall scaling
  feeds the ladder.)
- NIT (Lemma 4.1 proof): ||e^{-iHt}|| ~ t^{k-1} -> \gtrsim t^{k-1} (only the
  lower bound is used; exact-asymptotic form would need H to have no other
  eigenvalues). Strict-rigor improvement.
HELD FOR AUTHOR (both touch the flagship scope arguments -- flagged for
Jonathan, not applied autonomously):
- MINOR (Claim 6.1 headline / Sec 4 "structurally absent" / Table 1 horn-3
  cell): the proven exclusion = arbitrary per-sector similarities (Lemma 4.1)
  + bounded-with-bounded-inverse Fock dictionaries (Thm 4.5); unbounded
  *sector-mixing* dictionaries (e.g. realized e^{-Q/2}-type PT maps) are
  excluded by neither, yet the headline reads exhaustive. Auditor fix: one
  concession sentence naming the uncovered class + align Claim 6.1's headline
  with its own scoping parenthetical. [Overlaps the pass-9/gate-pass-1
  rescope territory -- author call on wording.]
- MINOR (Sec 5 alpha_g gap window): the stated window
  3e12 <~ |alpha_g| << 1e109 omits unanchored |alpha_g| >~ 3e109, which also
  evade both branches (bound vacuous; no rotation-curve anchor => don't
  inherit the face-value branch's observational death). Auditor fix: phrase
  the prior-excluded set as ALL unanchored |alpha_g| >~ 3e12 (the anchored
  face-value point 3e109 being the sole exception, which dies on its own
  branch). [Touches the honest-non-closure fork argument -- author call.]
- NIT (no-sample-space result relative to fixed-basis/time-independent-S
  definition): adequately disclosed by Sec 2's "beable basis chosen once"
  parenthetical -- no action.
No false converses (both "exactly when" claims hold both directions); abstract
(i)-(iv) match section scope.

**Numerics — CLEAN (guard).** All 4 t4 scripts run in seconds; every number
reconciles (cond*angle 2.2363 vs sqrt5 2.2361; exponent ladders; alpha_g
window exponents 3e12/1e40/1e109; rate-ladder slopes 2/4/2; 4/3 ratio).
Worst case 126 m quoted as ~130 m (within its stated "~"). CERT holds.

**Bibliography — CLEAN (guard).** 49/49 bibitems, 55/55 works vs Crossref/
arXiv; GSTZ "metastable", IK "Ghost-turned tachyon", Dey-Fring, FMT, Kuntz
all exact; no chimeras. 2 NITs (case-normalization consistency; AsoreyKPS
Shapiro middle-initial variance) no-action. CERT holds.

Recompiled clean (16 pp); log clean (no errors, no undefined refs/cites).
No CRITICAL/MAJOR, no prior-fix reversal, no rejected leads.

**Counter move:** claims 1 MINOR + 1 NIT APPLIED -> reset to 0 (2 MINOR held
for author do NOT independently move it); numerics CLEAN guard -> 3/3 CERT
holds; biblio CLEAN guard -> 3/3 CERT holds. After pass 30: **claims 0/4,
biblio 3/3 CERT, numerics 3/3 CERT.** Publish HELD. Two MINOR scope items
awaiting author review before the next claims pass is meaningful.

## 2026-07-13 — AUDIT PASS 31 (three fresh agents; 2nd pass this session).
Per-lane cadence: claims Opus (adversarial, flips from pass-30 Fable);
numerics+biblio Fable guard (both CERT). Fresh eyes, no histories/notes.
NOTHING APPLIED -- all claims findings HELD FOR AUTHOR. Counter unchanged.

**Claims (Opus) — 1 MAJOR + 1 MINOR + 2 NIT. This pass ADJUDICATED the two
pass-30 held items:**
- **[MAJOR] alpha_g fork exhaustiveness above the face-value point** (Sec 5
  l.762-779 + abstract iii): ESCALATION of pass-30's held MINOR 3. The
  stated island 3e12 <~ |alpha_g| << 1e109 is NOT exhaustive above 3e109 --
  since Lambda_max ∝ alpha_g^{2/5}, larger couplings make the bound even
  more vacuous, and the observational death pins only to the fitted 3e109,
  so |alpha_g| >~ 3e109 evade both branches too. Cross-model corroborated
  (Fable pass-30 MINOR + Opus pass-31 MAJOR). REFINES a prior applied fix
  (the rescope that named the bounded window). Verdict "horn 1 untenable
  under the prior" survives. -> major-findings-ledger entry 11. HELD FOR
  AUTHOR (fix flavor is an author call).
- **pass-30 held MINOR 1 (Claim 6.1 "under any dictionary" sector-mixing
  scope) DOWNGRADED by Opus:** substance is fine -- unbounded sector-mixing
  dictionaries ARE correctly left uncovered + flagged (l.450-455, 964-968);
  only a headline WORD-ORDER NIT remains (qualifier printed after "any
  dictionary"). Cheap to apply on the author's next touch; bundled into the
  author note, not applied autonomously (same held-text region).
- [MINOR] Enumeration sliver 1e8-3e12 assigned to neither branch nor window
  (cutoff sub-meV there, verdict unaffected). Same alpha_g fork region ->
  bundled with the MAJOR for the author.
- [NIT] result (a) imported as an "exists exactly when" biconditional whose
  converse is proven only in the Companion -- cited, acceptable, flag only.

**Numerics (Fable) — CLEAN (guard).** All 4 t4 scripts fresh-run; every
number re-traced + in-text arithmetic recomputed (cond*angle 2.2363 vs
sqrt5; window exponents independently re-derived meV@3.3e12 / 100MeV@1.0e40 /
face-value 3e109 -- corroborates the MAJOR's arithmetic). CERT holds.

**Biblio (Fable) — CLEAN (guard).** 49/49 re-verified vs Crossref/arXiv;
no chimeras; 1 NIT (en-dash vs published-hyphen name-compound normalization,
inconsistent with the bib's own Barandes rule) no-fix. CERT holds.

No recompile (no p5 edits this pass). No CRITICAL/MAJOR APPLIED; the alpha_g
MAJOR refines a prior fix (logged, held).

**Counter move:** nothing applied; claims NOT clean (held MAJOR+MINOR) ->
stays 0; numerics/biblio Fable guards CLEAN -> 3/3 CERT hold. After pass 31:
**claims 0/4 (1 MAJOR + held scope items), biblio 3/3 CERT, numerics 3/3
CERT.** Publish HELD. The alpha_g fork is now the gating claims item;
author adjudication needed before the claims lane can advance.

## 2026-07-13 — AUTHOR ADJUDICATION + APPLICATION (alpha_g MAJOR resolved).
User chose "attempt the stronger observational-death argument." Fable-
investigated (research/p4_alphag_observational_death.md) + orchestrator-
verified. VERDICT: the observational argument HOLDS on the FACE-VALUE branch
(every tree gravitational observable carries a single 1/(2 a_g k^4)
propagator => scales as 1/a_g, so the linear-potential coeff gamma_* is
fit-pinned to a_g=3e109; any deviation fails galactic/solar dynamics
monotonically -- below overshoots, above undershoots), and FALLS BACK to the
naturalness prior on the Mannheim branch (a_g decouples from conformally-
invariant observables). APPLIED to paper5/main.tex:
- Sec 5 fork paragraph rewritten: island restated as the unbounded ray
  |a_g| >~ 3e12 (no upper cap), closed observationally on the face-value
  branch + by the prior on Mannheim's; the Mannheim energy bound reaches the
  threshold (Lambda_max <~ meV for |a_g| <~ 3e12), absorbing the old
  1e8-3e12 enumeration sliver.
- Propagated to abstract (item on the fork), Table 1 horn-1 cell, and the
  closing "neither branch" line.
- Word-order NIT fixed: "under any dictionary" -> "under any admissible
  dictionary---any similarity per sector, or any bounded... (Thm tower)".
Recompiled clean (17 pp, 0 errors/undefined). major-findings entry 11 ->
RESOLVED. This is applied CLAIMS content (counter stays 0); p5 claims lane
wants a fresh pass. Publish HELD.

## 2026-07-13 — AUDIT PASS 32 (claims only; Fable; do-more batch p1/p5/p6). NOT CLEAN (1 MAJOR held).
Fresh claims pass on the applied alpha_g-fork text + whole paper. Per-lane
cadence: claims **Fable** (adversarial, flips from pass-31 Opus). biblio +
numerics NOT re-run (both 3/3 CERT). Fresh eyes, no histories/notes.

**Claims (Fable, adversarial) — 1 MAJOR + 5 MINOR + 4 NIT**, with an
extensive independently-CLEAN-verified list (Lemma 4.1 Frobenius bound;
Prop 4.2 weighted-shift nilpotency; Thm 4.3 functional argument; exponential
sector norms; sqrt5 angle/cond identity; alpha_g power counting; divisor
column sum; t_c=0.486; Lambda_max arithmetic; one-loop foil).
**MAJOR — HELD FOR AUTHOR** (major-findings ledger 16, verified vs source
L814-821 / 927-931): the Sec 4 title "No closed sample space at the conformal
point" + Claim 6.1 ("definite configurations survive **only** in the Hermitian
realization, never jointly") state an unqualified universal, but Lemma 4.1
covers only finite-dim similarities and Thm 4.3 only bounded S with bounded
inverse — leaving unbounded sector-mixing field dictionaries (where realized
PT metrics live) + continuum-beable (x,xdot) on L^2 uncovered. The Discussion
(L927-931) scopes correctly => headline-vs-body calibration gap (borderline
MAJOR/MINOR). Fix: name the residual open classes + weaken Claim 6.1 to "under
any dictionary in the stated classes."
MINORs (HELD): H=dGamma(A) identification asserted, not derived (Bogoliubov
construction degenerates at the Jordan point — deserves derivation/cite);
"single 1/(2 a_g k^4) propagator ⇒ every observable ∝1/a_g" false quantifier
(nonlinear tree observables scale as higher powers) — fix to "every
leading-order (one-exchange) observable"; golden-rule delta->0 limit
smoothness asserted (merging poles have opposite residues); Claim 6.1 horn-1
"untenable" rests solely on the naturalness prior — headline should read
"untenable up to the stated prior"; "a_g decouples ⇒ no measurement
constrains it" false at the quantum level (graviton-graviton scattering) —
scope to classical/fit observables.
NITs (HELD): \date status-token strip (circulation-time action); Table-1
horn-1 row reads stronger than the Claim it summarizes; "needs no prior"
monotone leg presupposes the no-dark-matter fit (solar anchor G_eff∝1/a_g is
the DM-independent leg — name it); abstract "within eight decades" vs 12.5
(lab-scale) unexplained gap.

**Counter move:** claims 1 MAJOR (held) => **stays 0**. biblio 3/3 CERT +
numerics 3/3 CERT unchanged (not re-run). After pass 32: claims 0/4, biblio
3/3 CERT, numerics 3/3 CERT. Only the claims lane remains for p5. Publish
HELD.

## 2026-07-14 — AUTHOR APPLICATION (do-more batch; user "apply all recommended").
- **MAJOR Claim 6.1** (ledger 16): weakened the universal to "within the
  stated classes, ... never jointly" + a sentence naming the residual open
  classes (unbounded sector-mixing field dictionaries; continuum-beable
  $(x,\dot x)$ on $L^2$), pointing to the Discussion.
- MINORs: "single $1/(2\ag k^4)$ propagator ... every observable" -> "every
  leading-order (one-exchange) observable" (+ note nonlinear obs scale as
  higher powers, close faster) [abstract + Sec 5]; "$\ag$ decouples ... no
  measurement" -> classical/fit scope (+ graviton-graviton caveat); horn-1
  "untenable" -> "untenable (Mannheim up to the stated prior)" [Sec 5 + Table
  1 row]; golden-rule $\delta\to0$ smoothness marked an assumption (opposite
  residues); $H=\dd\Gamma(A)$ per-level Jordan structure cited to
  BenderMannheim2008; solar anchor flagged dark-matter-independent.
- NIT: \date status token **stripped to a plain date** ("July 12, 2026")
  2026-07-14 per user "don't carry forward" + [[papers-hysteresis-free]];
  p5 recompiled clean (17pp).
Recompiled clean (17pp, 0 errors/undefined). ledger 16 -> RESOLVED. Claims
counter 0. Publish HELD.

## 2026-07-14 — CLAIMS PASS 33 (Opus, adversarial).
Per-lane cadence (claims Opus this pass); biblio/numerics 3/3 CERT not re-run.
**No CRITICAL/MAJOR.** Auditor re-derived Lemma 4.1, Prop 4.3, Thm 4.4, the
cond(V)=2/|δ| / angle=(√5/2)|δ| / product=√5 law, α_g power-counting, and the
Λ_max scaling — all sound. 2 MINOR + 2 NIT, ALL APPLIED (verify-before-apply):
- MINOR abstract clause (iv): "admits no definite-configurations seat" -> "...
  within the stated dictionary classes" (was reading as a closed no-go while
  Claim 6.1 explicitly leaves the unbounded / continuum-beable $(x,\dot x)$
  classes open).
- MINOR intro: FringTairaTurner2025 "meets Lemma 4.1 like every other" ->
  "(insofar as its Dyson map is a fixed, boundedly-invertible similarity)"
  (time-dependent/unbounded-at-EP maps land in the open class).
- NIT Table 1 vs prose: Deruelle2012 "two-horn special case" -> "horn-1 special
  case (with a horn-2 aspect)" (reconciled to the table's horn-1 label).
- NIT decade-count: "eight decades" headline marked "(a conservative figure; the
  same bound in fact reaches $|\ag|\lesssim3\times10^{12}$, below)".
Recompiled clean (17pp, 0 errors/undefined). Claims counter stays 0. Publish HELD.

## 2026-07-14 — CLAIMS PASS 34 (Fable, adversarial).
Per-lane cadence (claims flips Opus->Fable); biblio/numerics 3/3 CERT not re-run.
**No CRITICAL/MAJOR** — Fable re-derived Lemma 4.1, Prop 4.3, Thm 4.4 and the
α_g/Λ_max numerics, all sound. 3 MINOR + 4 NIT, ALL APPLIED (scope-propagation):
- MINOR abstract (i): "cond→2ω/|δ|" -> "the EP-driven cond→2ω/|δ|" (2/|δ| is proven
  at ω=1; general-ω cond carries a non-EP normalization factor).
- MINOR Sec 5 Mannheim: "α_g decouples from every classical observable" -> attributed
  ("on Mannheim's contention, via degeneracy with the undetermined conformal-source
  normalization").
- MINOR Table 1 horn-3: "no sample space (Lemma 4.1)" -> "...within the stated
  dictionary classes" (same qualifier Claim 6.1 carries; propagation of ledger-16).
- NITs: intro "neither branch tenable" -> "(on the stated closures)"; face-value
  hinge +linkage clause (rebuttals invoke the conformal-source structure defining the
  Mannheim branch); Flanagan "dark-matter-independent anchor" +"though
  Mannheim-disputed"; Claim 6.1 horn-3 "however weak the coupling that would dress it"
  CUT (free/kinematic-level statement).
Recompiled clean (17pp, 0 errors/undefined). Claims counter stays 0. Publish HELD.

## 2026-07-14 — CLAIMS PASS 35 (Opus, adversarial). VALIDATES wave-2 fixes.
Per-lane cadence (Fable->Opus). **No CRITICAL/MAJOR** — Opus re-derived Lemma
3.1/Thm 3.4 + the α_g/Λ_max numerics; qualifiers "propagate abstract->body->
table->discussion with unusual discipline" (the wave-2 scope fixes held). 2
MINOR + 3 NIT applied: Table-1 Deruelle straddle noted in the price cell ("a
two-horn special case"); abstract (iv) "map onto the horns" -> "(one
horn-adjacent)" (Merlin is horn-3-adjacent); intro "neither branch tenable" now
names the closures (observational death / naturalness prior); abstract face-value
ray reworded to point-collapse (ag pinned to a single solar-system-dead value,
not ray-exclusion); "contact rung" -> "contact (s-flat) rung". Claims stays 0.
Clean (17pp).

## 2026-07-14 — PROOF ADDED (rem:posdiag): the sector similarity is positive-diagonal.
Resolving the cross-paper SEAM behind p6's tower MAJOR (major-findings 22): p6's
tower corollary needs the beable(occupation) basis to be positive-diagonal-similar
to the Jordan basis at general M, which p6 asserted "as in the base cell" but
paper5 never proved. It IS provable and nearly immediate from prop:tower — the
shift dGamma(N)=a_u^dag a_v has strictly POSITIVE weights sqrt((s+1)(M-s)), so it
is D J_M D^{-1} with D a fixed positive diagonal; the t-independent D^2 passes
through the two-time divisor V(T)V(s)^{-1}, so entrywise signs transfer at every M.
Added as **Remark rem:posdiag** + backing **scripts/t4_tower_similarity.py**
(verified M<=12, err ~1e-16) + Code-availability. Opus cross-confirmed PROOF VALID.
NOT an audit finding on p5's own claims -> counters unchanged (claims 0, biblio/num
3/3 CERT). Recompiled clean (17->**18pp**). Publish HELD.

## 2026-07-14 — NEW-CONTENT AUDIT of rem:posdiag (Fable claims + numerics). MAJOR (writeup) applied.
The just-added proof got its own gate audit (never ship un-audited new content, even
after a math cross-confirm). **claims (Fable): 1 MAJOR + 2 MINOR + 3 NIT.** MAJOR
(major-findings 23): the conclusion "sign invariant UP THE TOWER" omitted the Toeplitz
step (the D-similarity is per-M; the cross-M lift needs e^{-iJt} offset-only) -> added
the Toeplitz clause + rephrased to per-M sign-transfer + the M-independent offset-k
entry. MINORs: U(t) missing the global phase e^{-iMwt} (cancels in |U|^2) -> inserted;
"standard Jordan block" direction unspecified -> "(ones on the subdiagonal, matching
s->s+1)". NITs: "corresponding entry" -> offset i-j; recursion range s=0..M-1; {u,v}
orthonormal noted. **numerics (Fable): BACKS THE CLAIM** (auditor independently rebuilt
a_u^dag a_v from ladder ops, matched to 1e-16, M<=12) + 1 MINOR: the sim-check was
self-confirming -> HARDENED t4_tower_similarity.py with a first-principles kron ladder
construction + a single-Jordan-block structure check (rank M, nilpotent^{M+1}=0).
Recompiled clean (18pp). Counters unchanged (new-content remark, not a p5-claims gate
pass). Publish HELD.

## 2026-07-14 — FULL WAVE: claims pass 36 (Fable). TWO MAJORs.
**2 MAJOR + 3 MINOR + 1 NIT.** MAJOR (ledger 25): "the PU cell never [develops divisor
negativity], provably" is BASE-CELL-only — at M≥2 the depth-two entry ¼(T²−s²)(T²−3s²)<0
(short step), carried to the beable basis by rem:posdiag; scoped to the size-2 cell +
added the M≥2 negativity (self-contained) + scoped the abstract mechanism-novelty. A
cross-paper consistency EXPOSED by proving the tower negativity this session (Stage-14 in
reverse). MAJOR (ledger 26): "published escape routes map onto the horns with no
remainder" vs the intro's eight pending 2026 routes -> "adjudicated" + pending note.
MINORs: rem:posdiag "every sector" -> "every sector M≥k" (the slip that would launder
ledger-25) + orthonormality-as-convention; abstract point-collapse "1/αg" ->
"gravitational (one-exchange)"; Claim 6.1 +deterministic-Bohmian-beable exclusion
(DeyFring2026). NIT (triangularity convention) no-action. Claims 0. Clean (18pp).

## 2026-07-14 — WAVE 5: claims pass 37 (Opus). MAJOR fixes VALIDATED.
Opus INDEPENDENTLY RE-DERIVED the offset-2 divisor entry ¼(T²−s²)(T²−3s²) + confirmed its
M-independence (M≥2 scope justified) + the base-cell-vs-tower consistency (abstract + body)
+ rem:posdiag positivity/t-independence -> the full-wave MAJORs 25 (negativity scope) & 26
(routes) & the rem:posdiag proof all HOLD under fresh scrutiny. No new MAJOR. Refinements
APPLIED: "eight 2026 entries" -> "(2024-2026)" (3 predate 2026); BM "is ... the bookkeeping"
-> "we read ... as" (matches Discussion's "interpretation, not theorem"). No-action
(marginal/disclosed): Holdom pending-vs-priced; Merlin remainder phrasing; orthonormality
convention-dependence. Claims 0. Clean (18pp).

## 2026-07-14 — WAVE 6: claims pass 38 (Fable, adversarial). No MAJOR.
- **claims (Fable, pass 38): 0 CRITICAL/MAJOR; 5 MINOR + 5 NIT.** Every load-bearing proof (Lemma 4.1, Prop 4.3, Thm 4.4, Remark 4.5, alpha_g power-counting, Lambda_max arithmetic, t_c=0.486 root) re-derived sound; no false converses.
  - MINOR applied: #1 the chain-vector normalization gamma (1,lambda,gamma w1^2 w2^2/lambda, gamma lambda^2) COLLIDED with gamma = one-loop ghost width defined the next paragraph -> renamed the normalization to beta ("a fixed kinetic normalization"). #2 "lower-bounds the conditioning of ANY similarity dictionary built on the mode decomposition" (undefined class) -> added the normal-target hypothesis + the spectral-projector-norm ~1/angle bound. #3 Thm 4.4 "bounded" is convention-relative -> added a scope clause (relative to the occupation-number {u,v}-orthonormal Fock norm of rem:posdiag; a Dyson map bounded in a different Fock norm falls into the honestly-open unbounded/sector-mixing class). #4 Sec 5 horn-1 numbers rest on the smooth delta->0 final-state limit (disclosed in Scope but not propagated) -> added the caveat to Claim 6.1 horn 1. #5 "removes the third at the outset" outran the claim body's own exclusions -> qualified to "within the stated dictionary classes".
  - NIT applied: #7 kappa (cell off-diagonal coupling) undefined -> defined at first use (L626).
  - NIT no-change (already-conceded / pedantic): #6 cond law derived at omega=1 (text concedes the units control); #8 "every spin-2 mode at an EP" includes k=0 (higher-order EP, still an EP); #9 4-body 0->4 amplitude in 2->2 Mandelstam notation (schematic; s-flatness unaffected); #10 Thm 4.4 "sector norms grow exp in M" asserted (true, load-bearing only for the aside).
- Recompiled clean, 18pp. Counter: claims 0 (applied findings); biblio/numerics 3/3 CERT (not re-run). Opus-p37-clean -> Fable-p38 no-MAJOR (5 MINOR).

## 2026-07-15 — BIBLIO CERT REVOKED (author ruling; no audit pass run)

**Counter move: biblio 3/3 CERT -> 0/3.** Not triggered by any bibliographic error
in p5 — none was found, and its 46 external records remain verified across three
consecutive clean passes. Revoked because the certification's BASIS was
incomplete, exactly as in p6 (major-findings-ledger entry 31, methodology-timeline
Stage 17).

p5 carries **49 bibitems, of which 3 are `Companion*` self-citations**. The
lane's own reports state the carve-out plainly:
- one pass: *"49 bibitems; 46 verified vs Crossref-by-DOI + arXiv, **3 are the
  author's own GitHub companions (unindexable)**"*
- a later pass: *"49/49 items verified vs Crossref/arXiv; **all 3 companion GitHub
  URLs HTTP 200**"* — HTTP 200 is an EXISTENCE check, not rule-6 claim-support
- the middle pass's *"49/49 verified vs Crossref/publisher"* cannot be literal:
  GitHub self-cites have no Crossref record

So the lane asked whether the referents EXISTED, never whether they were any GOOD
— identical to the p6 defect. No lane failed; each did what rule 6 specified at the
time. Rule 6 has since been amended (SELF-CITATIONS ARE CITATIONS: open the
referent, apply claim-support, check its AUDIT STATUS, check reciprocity). p5
biblio re-earns K=3 from zero under the amended rule.

**Contrast, for the record: p1 was NOT reset** despite the author's ruling naming
it alongside p5. p1 has 59 bibitems and **zero** self-citations — it is the root of
the program's citation DAG and cites nothing within the program — so its
certification rests on 59/59 external records and the self-cite blind spot cannot
apply to it. Checked mechanically before applying.

Also this session (counter-neutral, rule-3 reorg exception): p5's `Companion*`
bibitem URLs re-plumbed for the single-logical-sequence renumber. p5 is now
**series paper 5**, repo `p05-choosing-ghosts` (was `p04-`); its companions
resolve to p01 / p03-instantaneous / p04-conditioned. All citations point backward.

## WAVE 7 (2026-07-16) — claims pass 39 (Opus, adversarial) + biblio RE-CERT pass 1 (Opus).
CLAIMS (agent a8fe344f): CLEAN on hard defects. 4 thm/lemmas re-derived sound —
cond scaling 2/|delta| (angle sqrt5/2), Lemma 3.1 (real-eigenvalue hypothesis present
and load-bearing), Thm 3.6, alpha_g^-1 topology-independent counting, Lambda_max ~
alpha_g^{2/5}. 2 MINOR, both already DISCLOSED in-text (no change, HELD): (a) the
field-level "no sample space" conclusion (thm:tower + Claim 4.1 horn 3) is load-bearing
on occupation-number-NORM boundedness — actual no-ghost Dyson maps (e^{-Q/2}) are
generically unbounded in that norm, so the theorem excludes only finite-dim per-sector
avatars, not the field level (abstract/title rhetoric runs hotter than Thm 3.6
licenses). (b) occupation-number beables assumed for the whole tower; field-config
(x,xdot) L^2 beables explicitly out of scope. 2 NIT HELD (Claim 4.1 restate
occupation-norm dependence; Sec 5 Mannheim-branch horn-1 closed by naturalness prior).
No manuscript change -> claims 0->1.
BIBLIO RE-CERT (was 3/3, CERT REVOKED 2026-07-15 ledger 31; earns K=3 from zero):
CLEAN. All 3 Companion self-cites given REAL claim-support under amended rule 6, each
referent OPENED (not HTTP-200): Companion->p01 divisor-onset 0.7 and 1.0 reconcile to
the single formula t_c=1/(s sqrt2) (kappa=1 -> 0.7; theta=pi/4 -> 1.0), no drift;
Companion2->p03 trilemma quoted verbatim + Lambda^0/Lambda^4/Lambda^8 ladder = CJM
counting; Companion3->p04 title matches, cited only as series member (no quant load).
The revocation defect (self-cites existence-checked only) is RESOLVED. All 46 external
refs independently metadata-verified (arXiv/Crossref/APS/ADS): 0 hallucinated, 0
misattributed, 0 could-not-confirm; all 13 high-risk 2026 arXiv items REAL with journal
records (FMT2026 2601.20752; Fring cluster; AsoreyKPS JHEP 02(2026)020 + 01(2025)113;
Santillan EPJC; etc.). Biblio 0->1 toward re-cert. Numerics remains 3/3 CERT.
[Control event: the biblio agent (ab2a9d40) tried to fan out helper subagents for
external metadata and stalled; force-resumed via SendMessage to emit self-cite results;
external metadata completed by a dedicated no-spawn follow-up agent (affcacfc). New
failure mode: biblio prompts must forbid spawning sub-agents.]

## WAVE 8 (2026-07-16) — claims pass 40 (FABLE, adversarial) + biblio RE-CERT pass 2 (FABLE). no CRITICAL/MAJOR claims; biblio 1 MINOR.
CLAIMS (agent a4b57da8) — no CRITICAL/MAJOR (corroborates wave-7 Opus); all load-bearing math re-derived sound (lem:jordan, prop:tower, rem:posdiag, thm:tower, cond=2/|delta| via Ostrogradsky eigvec, alpha_g^-1 counting, Lambda_max^{1/5} numbers, divisor algebra).
- [MINOR APPLIED] sec:intro L236 "the trilemma closes, with every PUBLISHED escape route assigned to a horn and priced" -> overclaim vs own scope (8 pending 2024-26 entries + metastability "(premise)"). Fix: "every ADJUDICATED escape route ... (several recent entries remain logged as pending)".
- [MINOR APPLIED] norm dependence unstated at abstract + Discussion L872: thm:tower boundedness is rel. to the occupation-number Fock norm (both Opus wave-7 + Fable wave-8 flagged). Fix: propagate "(bounded ... in the occupation-number Fock norm)" to both sites.
- HELD: Mannheim naturalness-prior direction (paper already labels it a prior); 2 NIT (2->2 invariant list for 0->4; lem:jordan "under any similarity" time-independence reminder).
BIBLIO RE-CERT pass 2 (agent a5dc297b) — 1 MINOR:
- [MINOR APPLIED] BenderMannheim2008 mis-targeted twin at L536: "per-level Jordan structure is the Bender-Mannheim equal-frequency construction \cite{BenderMannheim2008}" -> PRL 0706.0207 has ZERO Jordan content; the construction is the PRD twin 0804.4190 (=BenderMannheim2008PRD, cited correctly elsewhere). Fix: retargeted to \cite{BenderMannheim2008PRD}.
- 3 self-cites SUPPORTED (referents opened; Companion->p01 t_c=kappa~^-1 arcsinh(kappa~/(s sqrt2)) EP limit 1/(s sqrt2); Companion2->p03 trilemma+ladder; Companion3->p04 series role). 49 external works verified incl all 10 high-risk 2026 arXiv + quote-level (Cline Lambda<=18.8 MeV, D-M Eq.13, GSTZ 3 phrases).
- **This REVERSES the wave-7 p5 biblio re-cert pass-1 CLEAN -> re-cert 1->0** (pass-1 Opus missed the twin-cite mis-target). [Only a MINOR here; contrast p6's MAJOR.]
Counters: claims 1->0 (applied), biblio re-cert 1->0 (applied). Recompiled 18pp clean. Numerics remains 3/3 CERT.

## WAVE 9 (2026-07-16) — claims pass 41 + biblio re-cert pass 3 (OPUS, convergence re-check). BOTH CLEAN.
CLAIMS pass 41 (Opus, adversarial) CLEAN: Lemma 4.1, Prop 4.3, Thm 4.5 (tower), depth-two divisor negativity window (c2=(T^2-s^2)(T^2-3s^2)/4<0 on 1<T^2/s^2<3), alpha_g power-counting (tree I=V-1 => alpha_g^-1 topology-independent) all re-derived; arithmetic spot-checks correct (5e7 M_Pl, Lambda thresholds 3e12/1e40, one-loop 1-2e-4, cond=2/|delta|). Wave-8 trilemma-overclaim + occupation-norm fixes HOLD (Claim 6.1/horns/alpha_g stay inside stated dictionary classes). 4 "≈"-softening NIT HELD.
BIBLIO RE-CERT pass 3 (Opus, amended rule 6) CLEAN: ~24 self-cite SITES opened against referents (paper1/, paper3/, paper4/) and claim-supported incl load-bearing numeric transfers (onset 1/(kappa√2), Lambda^4/Lambda^8 ladder, 1e-3 slopes). BenderMannheim2008 PRL-vs-PRD twin-cite (wave-8 MINOR) now verifies CORRECTLY TARGETED — no swap. High-risk external sample 15/15 clean, 0 hallucinated. 1 NIT (2 x 2026 jrefs verifiable only via Crossref not arXiv).
Counters: claims 0->1, biblio re-cert 0->1 (toward K=3). Numerics remains 3/3 CERT. Agents ac58414c (claims) / a0d9e8fc (biblio).

## WAVE 9 STATE: claims 1 / biblio re-cert 1 / numerics 3 CERT.

## WAVE 10 (2026-07-16) — claims pass 42 (Fable) + biblio re-cert pass 4 (Fable). 1 MINOR applied (biblio). No MAJOR.
CLAIMS pass 42 (Fable, adversarial): all load-bearing re-derived (lem:jordan sqrt(n); Eq 1 cond*delta->2.000, angle->sqrt5/2; Prop 4.3 single Jordan block; depth-two divisor 1/4(T^2-s^2)(T^2-3s^2); Thm 4.5; alpha_g tree counting I=V-1; Sec-5 numbers 5e7 M_Pl). Wave-8 trilemma/occupation-norm fixes hold. 1 MINOR REJECTED (auditor-error-log): naturalness prior "tens of decades above unity" is defensible — the required alpha_g ~ 10^109 IS tens of decades above unity; Mannheim closes |alpha_g|<=3e12 and the prior only bites above that; the 10^12.5 endpoint is a technicality. 3 NIT held.
BIBLIO re-cert pass 4 (Fable, amended rule 6): 46/46 external verified (0 hallucinated), 22/22 self-cite SITES PASS; BenderMannheim PRL/PRD twin-cites verbatim-confirmed correctly targeted. 1 MINOR APPLIED:
- Companion2 trilemma first statement (L165-166) was unqualified "ghosts ... any two never all three" while paper3 carries "(at tree level)" and p5's own L266-269 says "coupled ghost sector" -> aligned to "coupled ghosts ... never all three (at tree level)".
1 NIT held (Flanagan2006 "wrong light bending" -> "wrong weak-field limit").
Counters: claims 1->2 (clean), biblio re-cert 1->0 (applied). Recompiled 18pp clean. Numerics remains 3/3 CERT. Agents a2fa94e5 (claims) / a3196f1b (biblio).

## WAVE 10 STATE: claims 2 / biblio re-cert 0 / numerics 3 CERT.

## WAVE 11 (2026-07-17) — claims pass 43 (Fable) + biblio re-cert pass 5 (Fable). BOTH CLEAN.
CLAIMS pass 43 (Fable): CLEAN. All theorems re-derived (lem:jordan; prop:tower growth exponents 1.000/1.999/3.998/5.997/7.997; Thm 4.5; divisor window; EP cond*delta=2.0000, angle=sqrt5/2; all 5 Sec-5 numbers; one-loop). Wave-10 trilemma fix holds. 4 NIT held (abstract "cond->2omega/|delta|" derived at omega=1 only, body correct -> defensible; DonoghueMenezes prefactor = biblio-lane, already verified; column-1-sum exactness; upper/lower-triangular wording). Counter 2->3 (toward K=4).
BIBLIO re-cert pass 5 (Fable): CLEAN, zero findings. 46/46 external verified (0 hallucinated), 22/22 self-cite SITES PASS incl. all provenance/numeric-transfer claims (onset 1/(kappa sqrt2), Lambda^4/Lambda^8 ladder, 10^-3 slopes); BenderMannheim twin-cite correct; wave-10 Companion2 trilemma fix confirmed PASS. Counter 0->1 (toward K=3). Numerics remains 3/3 CERT. Agents aff95577 (claims) / ae9e654c (biblio).

## WAVE 11 STATE: claims 3 / biblio re-cert 1 / numerics 3 CERT.

## WAVE 12 (2026-07-17) — claims pass 44 (Fable) + biblio re-cert pass 6 (Fable). 4 MINOR applied (claims); biblio CLEAN. Counter claims 3->0.
CLAIMS pass 44 (Fable, abstract-consistency sweep): all theorems + all 5 Sec-5 numbers re-derived clean (spine solid). Findings in abstract/captions:
- [MINOR; auditor rated MAJOR -> DOWNGRADED on verify] abstract (i) L49 "EP-driven cond->2omega/|delta|": body proves coefficient 2 only at omega=1 (along a dispersion the EP-driven part follows the relative detuning delta/omega); the auditor's escalation measured TOTAL cond (omega^4-contaminated), but the abstract says the EP-DRIVEN part. Real issue = coefficient-scope. Fix: "cond->2/|delta| at omega=1, following the relative detuning delta/omega along a dispersion" + "measure"->"lower-bound". (auditor-error-log)
- [MINOR] abstract (iii) L74 rate clause dropped the delta->0 stationary-final-state assumption (body Scope L849-858) -> "in the split-pole (delta->0) final-state limit".
- [MINOR] Sec 1 L226 "what that costs any similarity dictionary" dropped the normal-target class (body L309) -> "... with a normal target".
- [MINOR] tab:horns caption L941 "The published escape routes" reads exhaustive (8 pending routes absent) -> "The adjudicated published escape routes".
4 NIT held. Counter claims 3->0 (applied). Recompiled 18pp clean.
BIBLIO re-cert pass 6 (Fable): CLEAN, 46/46 external + 22/22 self-cite SITES PASS (incl provenance/numeric-transfer); BenderMannheim twin-cite correct; 1 optional NOTE. Counter 1->2 (toward K=3). Numerics 3/3 CERT. Agents a87f5e0f (claims) / a95fd41f (biblio).

## WAVE 12 STATE: claims 0 / biblio re-cert 2 / numerics 3 CERT.

## WAVE 13 (2026-07-17) — claims pass 45 (Fable) + biblio re-cert pass 7 (Fable). 2 MINOR applied (claims); biblio CERTIFIED.
CLAIMS pass 45 (Fable, broadened): spine re-derived clean (Lemma 4.1, Prop 4.3, Rem 4.4 depth-two window, Thm 4.5, all 5 Sec-5 numbers). Findings:
- [MINOR; auditor rated MAJOR -> DOWNGRADED on verify] registry completeness: Claim 6.1 "configs survive only in the Hermitian ghost realization" + Sec 6 "no remainder" omit tachyon (IlhanKovner2014)/Mostafazadeh2011 routes -- but the claim is scoped "within stated classes" + hedged "no remainder we could identify", and the routes are cited L182 as trading difficulty for costs. Fix: added them to the pending-routes note. (auditor-error-log)
- [MINOR] Code availability "four standalone scripts" -> "five" (five are listed).
- [MINOR HELD] symbol V overloaded 5 ways (worst: V=|U|^2 in Rem 4.4 vs Gamma=|V|^2 same section) -> dedicated notation pass.
4 NIT held. Counter claims stays 0. Recompiled 18pp clean.
BIBLIO re-cert pass 7 (Fable): CLEAN, 46/46 external + 18/18 self-cite SITES PASS (incl provenance/numeric-transfer); BenderMannheim twin correct. Counter 2->3 = CERTIFIED (K=3). The 07-15-revoked p5 biblio CERT is fully re-earned. Numerics 3/3 CERT. Agents aec1c086 (claims) / af994421 (biblio).

## WAVE 13 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 14 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 46 OPUS (cross-model check after 4 straight Fable waves).
ZERO confirmed MAJOR (1 auditor-MAJOR downgraded); math core re-derived SOUND (Lemma 1.1 no-closed-process-at-a-Jordan-point, sector-tower Prop, Fock-tower no-bounded-dictionary Theorem -- all hypotheses sufficient; eigenvector-angle sqrt5/2|delta| + cond=2/|delta| reconstruction, one-loop suppression, Lambda_max scale all spot-checked).
- [MAJOR -> MINOR DOWNGRADED, NO EDIT] "The trilemma, closed"/"closes" auditor-MAJOR: the Merlin (Donoghue-Menezes) route keeps all three virtues (coupled ghost + Lorentz invariance + configurations) and pays only in microcausality (a 4th currency) -> "never all three" claimed-falsified; "3-adjacent" self-contradictory (horn 3 = no configs, Merlin keeps them). DOWNGRADED: the paper does NOT claim Merlin occupies a horn -- abstract already "(one horn-adjacent; ...)", table caption already "No route occupies a fourth position ... the closest candidate is the Merlin route, which keeps the sample space and trades causal order ... a currency the trilemma does not list but operational physics does." Fix (a) [fold microcausality into Lorentz-violation] is physically WRONG (Merlin modes are Lorentz-invariant + unitary, violate only locality). "3-adjacent" defensible = adjacent to the fakeon horn-3 dialect (both pay microcausality). Logged to auditor-error-log. No edit.
- [MINOR APPLIED] cond(V) lower bound (Sec kinematics): "up to O(1) it lower-bounds the conditioning of ANY similarity dictionary with a normal target" asserted the universality without the reduction. Fix: added "a normal target is unitarily diagonalizable and the unitary factor leaves the condition number unchanged, reducing the bound to this diagonal case".
- [MINOR NO EDIT] Mannheim horn-1 "neither branch tenable" already disclosed in the abstract ("on Mannheim's branch by an explicit naturalness prior, stated as such", L83-86) + the body Claim carries "(Mannheim up to the stated prior)". Already-satisfied; logged to auditor-error-log.
Counter claims stays 0 (applied cond MINOR). Recompiled 18pp clean. Agent acf9439e.

## WAVE 14 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 15 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 47 FABLE (adversarial).
1 MAJOR (ledger 43) + 6 MINOR + 2 NIT applied; math core (Lemma 4.1, Prop 4.2, Remark 4.3 incl the M>=2 negativity formula, Theorem 4.4, sigma_max/Gaussian envelope, cond*angle->sqrt5, all Lambda_max arithmetic) re-derived SOUND.
- [MAJOR ledger 43 APPLIED] the "smooth delta->0 limit" of the split-pole spectrum is CONTRADICTED (not just assumed): LSZ-normalizing the split legs against the 1/(alpha_g delta) residues gives divergent ~delta^-1/2 per leg, |M|^2 ~ s^2/(alpha_g^2 delta^2), Gamma/V ~ Lambda^8/(alpha_g^2 delta^2) -> inf; direction = kills horn 1 HARDER. OPUS VERIFIER CONFIRMED via partial-fraction+LSZ. Applied: Scope disclosure + re-badged the contact rung as "maximally generous lower bound" at ALL 3 sites (abstract iii, results-in-brief, eq-(2) conclusion; grep-all-copies). Thesis untouched.
- [MINOR APPLIED] F2 "no sample space" -> "no CLOSED sample space" (horn-3 bullet + table + abstract; the paper constructs an open/conditioned process). F3 intro "every route assigned to a horn" -> "...one horn-adjacent (Merlin), one premise-disputing (metastability)". F4 Merlin tree-level reconciliation added ("a loop-level width construction, outside the tree-level trilemma"). F5 abstract pending count broadened. F6 FTT sentence: "Lemma 4.1 sector-wise, or Theorem thm:tower if bounded in the occupation Fock norm".
- [NIT APPLIED] F7 eq-(1) "one law" scoped to beta=omega=1 (invariant = 1/|delta|); F8 abstract (i) "every mode" -> "every mode (k>0)"; F9 Thm 4.4 "undefined or infinite" -> "the unit column-sum condition fails outright".
- [REJECTED -> auditor-error-log] F10 triangularity (auditor conflated the lower-tri generator J_M with the upper-tri divisor).
Counter claims stays 0. Recompiled 18pp clean. Agents a9ef09fb (claims) / ab890f58 (Opus F1 verifier).

## WAVE 15 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 16 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 48 FABLE (convergence check on wave-15).
ZERO MAJOR; wave-15 delta->0 fix VALIDATED (auditor independently re-derived the delta^-2 divergence, all 4 alpha_g thresholds, Lemma 4.1, Thm 4.4, Prop 4.3, cond(V) universality -- all SOUND; disclosure consistent at all 5 sites). 2 MINOR + 2 NIT applied:
- [MINOR APPLIED] "multiplicity horn of [Companion2]" (used once, never defined) -> "the multiplicity (instantaneous-decay-products) sample-space choice of [Companion2]".
- [MINOR APPLIED] Table-1 horn-1 row dropped the unanchored-ray/prior qualifier the abstract+Claim carry -> appended "(larger-coupling ray closed by fit or stated prior)".
- [NIT APPLIED] "consistently regulating only raises it" scoped to the regulator regime m(delta)<<Lambda (at the Scope mechanism site).
- [NIT APPLIED] ambiguous "tightens the horn-1 pricing below" -> "tightens (never loosens)".
Counter claims stays 0. Recompiled 18pp clean. Agent af744126.

## WAVE 16 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 17 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 49 FABLE. ZERO MAJOR; delta->0 disclosure re-derived + re-verified consistent at all 5 sites (a THIRD independent confirmation), all alpha_g arithmetic + lem:jordan + thm:tower + prop:tower + cond(V) re-derived SOUND. 5 MINOR/NOTE applied:
- [MINOR] thm:tower "unit column-sum condition fails outright" (the wave-15 F9 line) is asserted, not proven, for the ENTRYWISE (non-ell^2) reading -> folded ell^2-existence into the dictionary-class definition ("an entrywise column that leaves ell^2 is excluded by definition").
- [MINOR] F2 REFINES the orchestrator's OWN wave-16 edit: "strictly larger THROUGHOUT the regulator regime m<<Lambda" was stronger than the LSZ argument shows -> "parametrically larger (for modes with relative detuning <<1)".
- [MINOR] "branch that survives vacuum decay" -> "survives the vacuum-decay bound as stated (the contact-rung minimum)". [NOTE] angular-integrability caveat added to the s-flatness Scope; horn-3 bullet + "within the stated dictionary classes".
Counter claims stays 0. Recompiled 18pp clean. Agent af42b234.

## WAVE 17 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 18 (2026-07-17, conv 954cb52d) — notation pass + Fable claims pass 50
NOTATION: V=|U|^2 stochastic map -> Gamma (role-inversion vs central amplitude V(t)), occupation index s->nu (matches p6 Companion4 weight), Toeplitz offset k->l, Jordan block-size k->m (frees momentum k), complex pole mass M->mu + Gamma_M->Gamma_mu (frees sector M), tree vertex count V->n_v (frees Gamma/V volume), cond(V) appositive. CLAIMS: spine SOUND -- Lemma 4.1, Prop 4.3, Remark 4.4 (rem:posdiag re-derived WITH the new nu/l symbols), Thm 4.5, normal-target cond bound, depth-2 window, all rate arithmetic. ZERO new structural MAJOR. REGRESSION from the notation pass caught: cond(V) appositive 
ef{sec:kinematics} was self-referential -> sec:currency (Sec 2 where V(t) defined). MINOR: |ag| sign restored L832; intro Fring-Taira-Turner dichotomy given open-class caveat (claim:choose); m_r~=m_2 near-EP identification explicit. Held: registry FMT2026/FelskiFringTurner2025 (count-based pending clause covers); delta Sec3-vs-Sec5. Recompiled 19pp clean (was 18; +1 = cond(V) appositive). Counter claims 0.

## WAVE 19 (2026-07-17, conv 954cb52d) — Fable claims pass 51
Spine SOUND (Lemma 4.1, Prop 4.2, rem:posdiag incl. depth-2 divisor entry re-derived with the new nu/l symbols, Thm 4.4, all rate arithmetic). 0 MAJOR. Sibling of wave-18 |ag| sign fix: bare "(g=1)" L810 -> "(|g|=1)" (concept-swept ALL numeric ag sites carry bars). MINOR: abstract(ii)+intro L233 "(finitely many configurations)" (no-representation universal is finite-dim); pending list +Bohmian route + "no remainder"->"no further remainder (two rows horn-adjacent/premise-level)"; M_P->M_Pl; Claim 6.1 "(applied mode by mode)"; 1.11802 punctuation; Konnig caption "one row"->"one cited work". Recompiled 19pp clean. Counter claims 0.

## WAVE 20 (2026-07-17, conv 954cb52d) — Fable claims pass 52
Spine SOUND. MAJOR (sibling): trilemma "(at tree level)" missing from Sec 2c + abstract iv (intro had it) -> added both. MAJOR (refine wave-19): Claim 6.1 "applied mode by mode" presupposes mode-diagonal S -> "one-quantum-sector argument extends verbatim to the full free Fock space" (covers mode-mixing bounded dictionaries) + dropped dangling Sec-7 pointer. MINOR: abstract convention parenthetical reordered (negativity convention-INDEPENDENT; only t_c relative); pending "eight"->count-free at 3 sites (owed since wave 18). REJECTED: Sec 5 "~5 invariants" (0->4 is a 4-point amplitude = 2 Mandelstam; auditor-error-log). Recompiled 19pp clean. Counter claims 0.

## WAVE 21 (2026-07-17, conv 954cb52d) -- OPUS cross-model claims pass 53
CROSS-MODEL: no CRITICAL/MAJOR; Lemma 4.1/prop:tower/rem:posdiag (only SIGN M-independent, correctly claimed)/thm:tower + rate arithmetic all SOUND. LOW: Sec 2a "exactly when" iff -- converse attributed to Companion; Claim 6.1 "extends verbatim" -> "single-mode argument applies mode-wise" (multi-mode 1-particle space is a continuum); Sec 5 "cannot cancel (positivity is norm-relative)". Recompiled 19pp clean. Counter claims 0.

## WAVE 22 (2026-07-17, all-lane all-Fable; user: "run until Fable returns NOTHING 3x each lane")
- CLAIMS (Fable): no CRITICAL/MAJOR (all spines sound). 2 MIN + 1 NIT applied: (1) abstract result (i) given the "normal-target (mode-built) dictionary" qualifier the body's cond->2/|delta| bound requires; (2) Claim 6.1's multi-mode extension of Thm 5.4 (was asserted at citation strength) recorded as a new Remark (H=sum dGamma(A_k) commutes with each N_k; invariant one-quantum subspace; argument runs verbatim mode-wise); (NIT) "(k>0)" added to the intro + Sec-3 anchors.
- NUMERICS (Fable): CLEAN -- all 5 scripts re-run in full, every number traced, robustness spot-checks pass. Fable-clean 1/3.
- BIBLIO (Fable): 1 MIN (rule-6 reciprocity): Lemma 4.1 credits Companion's size-2 boundary-case exclusion (paper1/main.tex L454-460) as the m=2 antecedent; the lemma's novelty (arbitrary m, real eigenvalue, Fock tower) preserved.
- Recompiled 19pp clean. Counters: claims 0; numerics CERT + Fable-clean 1/3; biblio CERT->0. Fable-clean streak: numerics 1/3, claims 0/3, biblio 0/3.

## WAVE 23 (2026-07-18, all-lane all-Fable)
- CLAIMS (Fable): no MAJOR (spine sound; wave-22 mode-wise Remark + normal-target + Companion m=2 credit all re-validated). 2 MIN + 1 NIT: Sec-7 "Limits" + Theorem 5.3 heading "bounded dictionary" -> "boundedly invertible dictionary" (every other surface already correct; this was the last drift).
- NUMERICS (Fable): CLEAN -> Fable-clean 2/3 (all 5 scripts re-run, all numbers traced).
- BIBLIO (Fable): CLEAN -> Fable-clean 1/3 (all entries + self-cite claim-support re-confirmed; ClinePhantom=PRD 108 095033 verified).
- Recompiled 19pp clean. Counters: claims 0/3, numerics 2/3, biblio 1/3.


## WAVE 24 (2026-07-18, all-lane all-Fable) -- FIRST CONVERGED LANE
- CLAIMS (Fable): no MAJOR. 1 MIN + 2 NIT: abstract-(i) per-mode cost given the "up to an O(1) factor" hedge (the every-normal-target-dictionary bound is ~1/angle = (2/sqrt5)/|delta|, a factor sqrt5 weaker than the eigenvector-matrix 2/|delta|; body already hedged); Sec-5.2 "upper-triangular divisor" -> "triangular" (was clashing with Remark 5.3's subdiagonal orientation); Prop 5.2's numerical-verification sentence moved OUT of the \begin{proof} block (the analytic proof is complete).
- NUMERICS (Fable): CLEAN -> **Fable-clean 3/3 -- CONVERGED** (first lane to meet the user's 3-consecutive-Fable-clean bar; clean waves 22, 23, 24).
- BIBLIO (Fable): CLEAN -> Fable-clean 2/3.
- Recompiled 19pp clean. Counters: claims 0/3, numerics 3/3 CONVERGED, biblio 2/3.

## WAVE 25 (2026-07-18, all-lane all-Fable) -- TWO LANES CONVERGED
- CLAIMS (Fable): no MAJOR. 1 NIT: Lemma 4.1 hypothesis made restrictive -- "a nondiagonalizable matrix (a Jordan block of size m>=2 at a real eigenvalue)" -> "a matrix with a Jordan block of size m>=2 at a real eigenvalue (hence nondiagonalizable)" (the growth step needs |e^{-i lambda t}|=1, i.e. real eigenvalue; the appositive parse left it unproven). Wave-24 fixes (O(1) hedge, triangular, proof-env) re-validated.
- NUMERICS (Fable): CLEAN -> **Fable-clean 3/3 CONVERGED** (clean waves 22/23/24/25; 4th consecutive).
- BIBLIO (Fable): CLEAN -> **Fable-clean 3/3 CONVERGED** (clean waves 23/24/25).
- Recompiled 19pp clean. Counters: claims 0/3, numerics 3/3 CONVERGED, biblio 3/3 CONVERGED.

## WAVE 26 (2026-07-18, all-OPUS cross-model check; numerics+biblio SKIPPED as converged 3/3)
- CLAIMS (Opus): CLEAN -- full re-derivation cross-model; wave-25 fixes validated. Opus corroborated the rejection of the 0->4 Mandelstam-count NIT (re-derived cond=2/|delta|, found the amplitude parametrization fine). Applied the Fable-flagged intro "(built on the mode decomposition)" alignment (line 231) matching the abstract/body -- a consistency fix (Opus judged it adequately disambiguated by context, but the explicit qualifier is cleaner; applied).
- NUMERICS: SKIPPED (Fable-converged 3/3). BIBLIO: SKIPPED (Fable-converged 3/3).
- Recompiled 19pp clean. Fable-clean streaks: claims 0/3; numerics 3/3 CONVERGED; biblio 3/3 CONVERGED.

## WAVE 27 (2026-07-18, all-OPUS cross-model check, 2nd consecutive; numerics+biblio SKIPPED as converged 3/3)
- CLAIMS (Opus): essentially CLEAN, 1 cosmetic NIT applied. All four theorem-grade results re-derived from scratch (Lemma 4.1 real-eigenvalue Jordan collision, Prop 4.3 sector tower single Jordan block size M+1, Remark 4.4 divisor c2=(T^2-s^2)(T^2-3s^2)/4, Thm 4.5 no boundedly-invertible dictionary); cond(V)=2/|delta| law, ag power-counting, Lambda_max rate chain all re-verified; abstract/intro/table strength-filing checked consistent. Applied NIT (line 347): de-magic'd the pair-angle "sqrt(6-1)/2" -- added a gloss identifying 6=||(0,i,i,-2)||^2 and the subtracted 1 as the squared along-v projection (the "=sqrt5/2" simplification was already inline). Sibling-swept: sqrt{6-1} unique; downstream sqrt5 uses are the legitimate cond*angle->sqrt5 law.
- NUMERICS: SKIPPED (Fable-converged 3/3). BIBLIO: SKIPPED (Fable-converged 3/3).
- Recompiled 19pp clean (gloss). Fable-clean streaks: claims 0/3 (Opus wave doesn't advance; the applied gloss is Opus-only, does not reset a Fable streak); numerics 3/3 CONVERGED; biblio 3/3 CONVERGED.


## SESSION 2026-07-18/19 (numbering unification + claim-support + rotation-four Fable)
- Folder paper4/ -> paper5/ (series 5); cite keys -> codenames; wave-27 line-347 pair-angle gloss carried; release-gate leak removed.
- Claim-support (Opus): CLEAN; 24 load-bearing attributions SUPPORTED incl. attributed equations (Donoghue-Menezes ghost-width gamma Eq.13; CJM Lambda^8/M_Pl^4 Eq.3). 5 body-level precision notes, none a mischaracterization.
- Rotation-four Fable CLAIMS: CLEAN -- all theorem-grade results (Lemma 4.1, Prop 4.3, divisor c2, Thm 4.5, cond(V)=2/|delta|, rate section) re-derived from scratch; all arithmetic (3-decimal roots, 5-decade fits) reproduced; 2 leads REJECTED (fixed-linewidth foil O(1) convention; "conditional Sec 5" grade-stacking) -> auditor-error-log. Fresh streak: claims 1/3.

## FABLE CLAIMS PASS 2026-07-19 (Fable-spend rotation-four wave, Wave 2)
- **SOUND: zero CRITICAL/MAJOR.** 8 spines independently re-derived cross-model: Lemma 4.1 (no closed process at Jordan point -- ‖V‖_F=√n, e^{-iHt}~t^{m-1}, cond(S) chain, real-eigenvalue hypothesis essential+present); Prop 5.2 sector tower (single (M+1) Jordan block); Thm 5.4 bounded dictionary on Fock tower (α=0 contradiction, real ω present); EP-kinematics √5/2 coefficient law (dv=δ(0,i,i,-2), perp²=5δ², angle=√5/2|δ|, cond=2/|δ|, cond×angle=√5) + Stelle-dispersion + one-loop numbers; divisor mechanics (depth-2 ¼(T²-s²)(T²-3s²)<0 on s<T<√3s, mass-creation onset t=0.486, Toeplitz M-independence); Λ_max ∝ α_g^{2/5} (s⁰ flatness, α_g bookkeeping -1, all branch numbers recomputed: 1e-8 eV/19.7m at α_g=1, meV at 3e12, 100 MeV at 1e40; calibration 108 vs 18.8 = 5.7x); δ→0 non-commuting limit (rate ×δ^{-2}); trilemma/horn tree-level scope consistent. Applied 3 NITs: abstract "only raises it" + qualifier "(for modes of relative detuning ≪1)"; Lemma 4.1 proof garbled "∑_j(column sums)" -> "∑_j(jth column sum)=∑_j 1=n"; Γ overload flagged symmetric to the V flag (Γ/V rate site now notes Γ=vacuum-decay rate, not the Sec-2 stochastic map).
- Streak: p5-claims had findings (NITs) -> NOT a clean-streak pass. Recompiled clean; both gates PASS.

## FABLE BIBLIO PASS 2026-07-19 (Fable-spend rotation-four wave, biblio round) -- CLEAN
- **43/43 external bibitems CLEAN, 0 fix-needed, 0 unverifiable.** All 4 verbatim quotations confirmed at source (Smilga2008, BenderMannheim2008PRD, GSTZ2021 x3, FMT2026). Every historically-tricky ref verified: ClinePhantom2024 18.8 MeV / 95% C.L. attribution exactly right (incl. abstract-19 vs body-18.8, and the PRD journal-ref the arXiv page omits); GSTZ2021 + Smilga2014 both correctly follow the PUBLISHED title (publisher-governs); CJM2004 / HellLustZoupanos / Flanagan / Yoon / Riegert / Steinwachs claim-support all confirmed. 2 MEDIUM flags are machine-read caveats (Mannheim2015 neg-α_g sentence in arXiv full text; ErrastiDiez vol digit) -- not defects. 2 optional NITs (AsoreyKPS 2nd arXiv id; DonoghueMenezes "The") -- no action.
- **CLEAN pass -> advances the p5-biblio Fable-clean streak.** No manuscript change.

## OPUS CROSS-MODEL WAVE 2026-07-20 (Wave A; claims + numerics; biblio skipped -- Fable cleared it 43/43 this session)
- **FULLY CONVERGED: claims SOUND (Opus, confirms the Fable pass) + numerics CLEAN (Opus, first run this session).** Opus independently re-derived from scratch both quantitative cores -- the 2/|δ| EP law (from the chain-vector derivative dv=δ(0,i,i,-2), perp²=5, angle √5/2|δ|, cond·angle=√5) and Λ_max∝α_g^{2/5} (all three anchors: 1e-8 eV@α_g=1, meV@3.16e12, 100 MeV@1e40; face-value 3e109->5.1e7 M_Pl) -- both land on the stated numbers. Numerics: all 5 t4_* scripts run, every value reproduces (cond=2/|δ| power -0.993, Jordan exponents 1/2/4/6/8, sector tower, rate-ladder slopes 2/4/2, mass-creation t_c=0.486); deterministic (RNG only for margin-checks, no quoted value random). No CRITICAL/MAJOR/MINOR either lane. Discussion strength-tiering accurate (BM↔dilation correctly "Argued"). No manuscript change.

## OPUS DEEP CLAIMS 2026-07-20 (Wave D; Nth adversarial pass) -- SOUND
- all 3 hardest seams airtight (δ→0 non-commuting limit no hidden sign/factor -> contact genuinely minimum; two-branch α_g closure honest, all 4 anchors reproduce; Fock-tower domain fencing walked line-by-line); horn-3 free/linearized scope disclosed not hidden. No manuscript change.

## OPUS DEEP CLAIMS 2026-07-20 (hunt-what-was-rationalized wave, p5-p8) -- SOUND, 1 MINOR + 2 NIT applied
- No CRITICAL/MAJOR; Lemma 4.1 / Prop 4.2 / Thm 4.4 spines + EP angle law + α_g fork + one-loop suppression all re-verified; the two danger zones (Lemma real-eigenvalue hypothesis; δ→0 non-commuting limit) handled correctly and flagged in-text, not rationalized.
- Applied: (MINOR, §3 cond-scaling parenthetical) the universal normal-target lower-bound now scoped "for $\delta>0$, where a normal target exists---at $\delta=0$ there is none, and Lemma~\ref{lem:jordan} supersedes"; at the EP there is no Hermitian counterpart (Bender--Mannheim), so the bound cannot cover the quadratic-level BM map there. (NIT, Lemma 4.1 proof) the $t^{m-1}$ growth was credited to "the Jordan nilpotent part" alone, but the REAL-eigenvalue hypothesis ($|e^{-\ii\lambda t}|=1$) is load-bearing (counterexample: size-2 Jordan block at $\lambda=-\ii$ decays, bounded) -> added the clause. (NIT, abstract) "eight decades of unity" -> "(a conservative figure)"; the body already tightens to ~12 decades ($3\times10^{12}$), so the abstract was silently under-claiming.
- Recompiled 19pp, 0 undefined. Both gates PASS. No MAJOR.

## OPUS NUMERICS 2026-07-20 (Wave 6; reproduce-from-scripts) -- CLEAN
- Ran all 5 scripts. Every spine number reproduces: cond(V)=2.00/|delta| (power -0.993), angle law sqrt5/2 (1.11802), cond*angle->sqrt5 (2.2363), UV cost k^5 / units k^3 / EP-excess k^2, Lemma growth exponents 1/2/3, sector exponents to M=8, t_c=0.4859, column-sum 1+kappa^2(T^2-s^2); a_g fork anchors 3e109 / 5e7 M_Pl / 20 m@|ag|=1 / meV@3e12 / 100 MeV@1e40 / Lambda~a_g^{2/5}; one-loop 1-2e-4; gamma-ray 108/18.8=5.76. Depth-two divisor 1/4(T^2-s^2)(T^2-3s^2) SymPy-verified (block-size independent). 0 findings.
- No manuscript change.

## FABLE CLAIMS 2026-07-20 (cross-model diversity wave, p1/p3/p5/p6) -- 1 MINOR applied (self-edit bug)
- Fable re-derived the full spine (Lemma incl. the new real-eigenvalue clause -- CONFIRMED correct AND sufficient; sector tower; posdiag similarity; Toeplitz divisor sign window; tower theorem; the delta->0 non-commuting limit; the entire Sec 5 numeric chain). Zero CRITICAL/MAJOR, zero false converses.
- Applied: (MINOR #58) **self-edit bug caught cross-model** -- this session's normal-target scope clause "delta>0" should be "delta!=0" (the law is even in signed delta; a normal target exists for delta<0 too) -> one-token fix. The other two "delta>0" (abstract, Sec 5) are regulator conventions, correctly left.
- HELD (NITs): Deruelle table row "1" vs prose "two-horn special case" (parentheticals inform the reader); abstract registry drops the Maldacena "attempted" row (cosmetic).
- Recompiled 19pp, 0 undefined. Both gates PASS. No MAJOR.

## 4-WIDE FABLE CLAIMS AUDIT 2026-07-23 — spine SOUND (zero CRITICAL/MAJOR); MINOR + NIT applied
- Fable re-derived all proofs SOUND: Lemma jordan (real-eigenvalue hypothesis exactly sufficient), Theorem tower (dual-functional + ℓ²-column closure), Prop/Remark tower (Toeplitz divisor, depth-two entry recomputed), mass-creation onset (t_c=0.486), EP kinematics (perp²=6-1=5, cond×angle=√5), one-loop, δ→0 non-commuting limit, all rate arithmetic (Λ_max, forks). Cross-paper trilemma wording consistent p3/p7/p8/p9.
- APPLIED (minor-ledger #84): MINOR — abstract trilemma dropped "coupled" → "coupled ghosts" (a decoupled ghost coexists with both virtues; every sibling carries "coupled"). NIT — no-seat claim scoped "within the stated dictionary classes" (matches every other site; continuum L² kernels + unbounded sector-mixing dictionaries admitted open).
- HELD: "no numerical α_g in print" (L791) biblio-adjacent watch-NIT. Recompiled clean, gates PASS.

## W22 WIDE-OPEN AUDIT 2026-07-26 (Opus, adversarial; claims+numerics+biblio) — CLEAN cross-model; NO findings; counter 0->1
- **CLAIMS CLEAN:** every spine re-derived independently and correctly scoped — the no-closed-process-at-Jordan Lemma (Frobenius bound + t^{m-1} growth, one-directional, no false converse); sector tower Prop (single Jordan block M+1); Fock-tower Thm (dual-functional, sector norms confirmed exponentially growing in M, golden-ratio/1+√2 ratios); positive-diagonal-similarity Remark + depth-2 divisor ¼(T²−s²)(T²−3s²) neg on s<T<√3s (re-derived from scratch); angle/√5 kinematics (cond=2/|δ|, normalization-dependence correctly flagged); one-loop Merlin; rate/ag fork (all scoped tree-level/golden-rule/flat-space). No abstract-vs-body drift; qualifiers consistent across all appearances.
- **NUMERICS CLEAN:** all 5 scripts run, every quoted number reproduces AND model-congruent (PU mode matrix, grid Hermitian H, first-principles dΓ ladder). cond 2.00/|δ| slope −0.993, angle 1.11802 cond·angle 2.2363 vs √5, UV powers 5.0/3.0/2.0, ‖H−H†‖ 8e-15, tower exponents 1/2/4/6/8, t_c 0.486/0.50, Halmos 1.4e-8, ag routes 4.1e109/3.1e109 (4/3), Λ_max 5e7 M_Pl / 20 m, phantom 108 vs 18.8 MeV — all match.
- **BIBLIO CLEAN (internal):** 49 bibitems, 49 unique keys, 0 dangling, 0 uncited; all refs resolve; Smilga2014 "Giving" published-title convention respected (W21 #79 fix holds).
- **HELD (machine-provisional, human-PDF before circulation — NOT defects, do not reset streak):** (1) γ=ξ²m_r²N_eff/(320π) coefficient attributed to DonoghueMenezes (verify 320π); (2) "18.8 MeV, 95% C.L." from ClinePhantom2024 (verify number/limit — prior waves confirmed this); (3) Riegert1984 "particle content of linearized conformal gravity" coords "Phys. Lett. A 105, 110 (1984)" — LIKELY CORRECT (a DISTINCT paper from Riegert's better-known trace-anomaly PLB 134; the auditor conflated them); prior biblio-cert waves verified Riegert. No edit.
- No manuscript change. Both gates PASS (unchanged). **p5 -> 1/3** (first clean cross-model wave after the W21 Smilga-reversal+NIT reset; the recurring items were all fixed and did not resurface).

## W23 WIDE-OPEN AUDIT 2026-07-31 (Fable, adversarial; claims+numerics+biblio) - 1 MINOR + 5 NIT applied; NO MAJOR; counter -> 0
- **CLAIMS essentially CLEAN**, earned by full re-derivation (Lemma 4.1 Frobenius pin, Prop 5.1 weighted-shift single block, Remark 5.2 recomputed, Thm 5.3 dual-functional linear-growth proof step-by-step, angle law from the chain eigenvector, Gaussian-envelope necessity+sufficiency, alpha_g exponent bookkeeping, 0->4 massless invariant counting, one-loop numbers). Non-commuting delta->0 limit, normal-target restriction and tree-level scope disclosed at every sibling site. **MINOR applied:** Holdom attribution dropped "perturbatively" (arXiv:2408.04089 raw abstract). **NIT:** Oda gloss made conditional on a ghost-FP bound state (source says "if"); AsoreyKPS 2nd paper gained arXiv:2408.16514; "rank loss to machine precision" -> sqrt(machine precision) (script gives 3.7e-9 ~ sqrt(eps)).
- **NUMERICS CLEAN** - all five scripts run to completion, every quantitative claim reproduces; model congruence verified (grid Hamiltonian is the stated Ostrogradski PU H; all script constants independently recomputed). **Script hygiene NITs applied - this CLEARS the held legacy-pN bundle:** t4_ep_dictionary.py docstring "ANY similarity dictionary" -> normal-target/mode-built up to O(1); stale "paper 1"/"paper 2 stage 3" -> codenames in 3 scripts; t4_rate_ladder.py density comment 8.5e-30 -> 9.1e-30 g/cm^3 (orchestrator recomputed).
- **BIBLIO:** Smilga2014 title had a stray mid-title capital ("order Giving") - harmonized to the house sentence-case "giving", KEEPING the published word "Giving"/"giving" per the standing publisher-governs rule (NOT reverted to arXiv's "give"; see auditor-error-log). 2 auditor title flags REJECTED against Crossref (GSTZ "metastable" correct here; IK double-hyphen form wrong) - and verifying them exposed major-ledger #84 in p3/p6/p7. IK entry took the publisher's post-colon capital G. minor-ledger #156.

## W25 WIDE-OPEN AUDIT 2026-08-01 (Fable, adversarial) - NO MAJOR; NUMERICS/BIBLIO/MECHANICAL CLEAN; 1 MINOR applied; counter -> 0
- **All five scripts run to completion, exit 0, nothing skipped**; every quoted number reproduces; model congruence verified including that the detuning enters BOTH omega_1 occurrences. Whole spine re-derived from scratch (Lemma 4.1, Prop 4.3, Remark 4.4, Thm 4.5, the chain eigenvector from Hamilton's equations, alpha_g power counting, every rate-ladder evaluation, the 4/3 route ratio, the divisor algebra).
- **MINOR applied:** the Discussion dropped the norm qualifier at two sites while the abstract, Sec 4.1, intro and Claim 6.1 all carry "in the occupation-number Fock norm". This is load-bearing by the paper's own admission (L634-637: a Dyson map bounded in a different Fock norm "falls into the honestly-open class, not around the theorem"). Restored at both Discussion sites.
- The auditor independently confirmed that the W23/W24 attribution fixes hold: Smilga's quote is correctly scoped to the nonstandard realization, Oda's result carries its conditionality, and Holdom's carries "perturbatively". minor-ledger #170.
