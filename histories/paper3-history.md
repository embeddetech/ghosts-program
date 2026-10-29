# Process history — Paper 3 (instantaneous): "Ghost vacuum decay as a stochastic process"

Sources: notes.md (dated entries, 2026-07-11), git history, the
archived session transcript and 16 subagent logs, research reports.
Fine-grained timings: `process_timeline_papers12.md` (mined; UTC).
Transcript-verified anchors: QFT-bridge research from 17:26 UTC
Jul 11; GSTZ attribution correction written 18:23; E4 retraction
19:10--19:14; Verlet control-firing 19:13; paper drafted 23:30;
push-hold + main rewind 23:39; S4c circularity caught by the
adversarial subagent 00:31 UTC Jul 12; M3 seed-null 01:02; d=3
label artifact 01:03; M3 100-run kill 01:15; session end 01:42.
The 16 subagents ran in four waves (3 paper-1 audit, 4 literature
deep reads, 5 paper-2 audit/prior-art, 4 final pass).
This is the program's richest error record: five caught artifacts,
one formal retraction, and repeated replication-driven downgrades,
all inside roughly one day.

## Timeline

**Theory bridge (B1–B5).** Post-v1.0 follow-up thread: Feller's
ladder criterion as the Fock-space time-of-flight; the
Lorentz-invariant ghost vacuum as an instantaneous state; the cutoff
as conservativity data; CJM-vs-GSTZ as multiplicity-vs-redundancy;
the QFT trilemma. Literature anchors verified by web search the same
day; novelty check performed BEFORE the numerics were designed.

**Stage 2 numerics (E1–E4).** E1–E3 as designed. E4's verdict
("classical cascade UV-suppressed") would later be RETRACTED — see
below. A validity condition (incoherent-jump reduction needs a dense
continuum) was stated honestly at the theory stage.

**Stage 3: the factorization "theorem" — then the attribution
correction (Miss 2.1, caught by deliberate deep read).** The
boost-orbit factorization was derived, numerically verified to 0.1%,
and briefly held as a new theorem. Three parallel full-text reads
(CJM, GSTZ, wide sweep) found GSTZ's Eq. (88) IS the decomposition.
Status corrected in the notebook in so many words: "independent
rederivation + first numerical verification — NOT a new theorem."
The stage-1 back-of-envelope "d=1 converges" scale-counting was also
self-corrected (missed a vanishing Jacobian; the numerics adjudicated
against the author's own counting). Precision fixes A–D
(instantaneous-state probabilist language; two pathologies kept
separate; Born–Markov scope; tree-level bubble contrast) were written
as referee-hardening BEFORE drafting.

**The foliation thread (F1–F5) + Garriga–Vilenkin deep read.** The
GV read RESOLVED a soft spot (their D>2 rescue classified within our
menu), supplied the sharpest instantaneity statement ("a
Lorentz-invariant ghost vacuum can exist only if it was born"), and
CONFIRMED the trilemma against every known example.

**M3 (frame competition): a two-act honesty story.** Act 1: 16-run
ensembles suggested early-window state-frame anchoring (+0.23 at
N=128). Act 2 (downgrades 2.2a/2.2b): fresh seeds at N=128 gave
−0.002 (evidence WEAKENED, paper text rewritten to "suggestive");
then a 100-run settlement found the anchoring NULL (means −0.07 and
−0.02; the medians had been flukes). The paper's passage was
rewritten to claim only the robust findings (UV-directed cascade;
late-time frame erasure), with the covariant-window statement
guaranteed by principle, unresolved by lattice. Slogan amended
accordingly.

**E4-2D: RETRACTION (Error 2.3) + second artifact (2.4).** The
dimensional-reversal experiment was pre-registered in the docstring
before data. En route it exposed that the ORIGINAL stage-2 E4
"UV-suppression" was an artifact: the vacuum construction
under-weighted fine lattices by (N/L)^{d/2} — the shrinking source,
not physics. Formal RETRACTION recorded with contamination scope
(what fell: E4's verdict, one conjecture, one corollary; what stood:
E1–E3, stage 3, M3, all of paper 1). Caught by: a ⟨φ²⟩₀ control
column (fell when physics said rise). Same sweep, artifact 2: Verlet
drift at marginal timestep made the λ=0 CONTROL fire — caught by the
control column existing. Methods lesson banked: "each alone would
have produced a publishable-looking false trend."

**Exponent decomposition (the concession that sharpened).** The
"hotter start" objection to E4-2D was CONCEDED and quantified; the
reversal proved source-driven (tadpole ladder), and the honest
outcome was stronger: classical-statistical simulations are
tadpole-ladder probes; channel-ladder questions are intrinsically
quantum.

**S-series + artifacts 3–5.** S1 (no-signaling; new closed-form
corollary); S2 (completions as channels; artifact 2.5: a leapfrog
stability criterion wrongly throttling split-step FFT — runtime-only,
~400x; plus a CAP-strength leak fixed by class-dependent absorbers);
S3 (determinacy curve); S4a/b/c (decision matrix); S5 (flash flank
closed at tree level).

**Drafting (16 pp) and the audit cascade.**
- THREE-AGENT AUDIT: bibliography (31/34 confirmed; the Valentini
  arXiv ID was WRONG — pointed at an unrelated paper (Error 2.6);
  fixed); consistency agent re-ran 8 scripts and caught TWO
  self-description errors in our own text (the "all thirty-two
  cells clean" claim — actually 24 with L=6 excluded and FIRING;
  and a misattributed artifact in our own methods narrative
  (Errors 2.7, 2.8)); ADVERSARIAL agent caught **artifact 4
  (Error 2.9, CRITICAL): the S4c dipole mock was CIRCULAR** — it
  sampled a fixed photon population (aberration-only) and had
  "confirmed" analytics that had been wrongly corrected DOWN to
  match it. The original 3β was right. Corrected numbers made the
  signal LARGER (the error had been conservative). Lesson recorded:
  a mock sharing the analyst's observable definition cannot catch a
  definition error.
- PRIOR-ART SWEEPS: trilemma not preempted but both EDGES are prior
  art (CJM; Hardy 1992) — cited as such; one rival equilibrium route
  found and distinguished; the DGB-dipole author list completed.
- CLOSEOUTS: artifact 5 (Error 2.10): the first d=3 factorization
  run's "flat in H" label transplanted the d=1 orbit measure — the
  data was right, the label wrong; caught on re-derivation, fixed
  with the correct sinh² measure. Also: a sweep point below pair
  threshold (empty window) silently biasing a fit — fixed.
- SHIELD CORE: proved as a proposition — then the FINAL FOUR-AGENT
  PASS found Barandes–Hasan–Kagan (Dec 2025) had published the
  unitary case (Miss 2.11, caught pre-circulation): repositioned as
  the dilation extension + conditioning-breakpoint identification.
- FINAL PASS also: 2 critical + 5 minor self-description/drift items
  fixed; all calculations re-run bit-consistent; 48/48 + 46/46
  citations resolving.

**Post-final updates (2026-07-12):** the CJM bound superseded in the
literature (Cline et al. 2023: 18.8 MeV) — two-sentence update +
MeV-gap statement added; the wedge-edge statistics (from the T3
follow-up) recorded in the notebook as a correction to how s4c's
edge numbers apply to the cosmologically integrated signal; the GSTZ
title hyphen fixed (had survived every audit); provenance note
standardized and links rewired for the repo split.

## Errors & misses ledger

| # | What | Caught by | Fate |
|---|---|---|---|
| 2.1 | factorization briefly held as ours | deliberate full-text deep read | reattributed to GSTZ; ours = rederivation + first numerics |
| 2.2 | M3 early-window anchoring (twice) | fresh seeds; then 100-run replication | downgraded to NULL; paper rewritten |
| 2.3 | E4 "UV-suppression" (RETRACTED) | ⟨φ²⟩₀ control column | retraction with scope; replaced by stronger corrected result |
| 2.4 | λ=0 control firing (Verlet drift) | the control column | timestep fixed; thresholds re-verified |
| 2.5 | split-step throttled by leapfrog criterion | THE USER ("still running?"), then a CPU check | fixed (~400x); runtime-only |
| 2.6 | Valentini arXiv ID → unrelated paper | bibliography agent | corrected |
| 2.7 | "all 32 cells clean" (was 24, L=6 fires) | consistency agent re-running scripts | corrected in text |
| 2.8 | misattributed artifact in own methods text | consistency agent | corrected |
| 2.9 | S4c dipole mock CIRCULAR (3β wrongly "corrected" down) | adversarial agent | fixed; signal larger; lesson recorded |
| 2.10 | d=3 orbit-measure label transplanted from d=1 | re-derivation at closeout | fixed (sinh² measure); data unaffected |
| 2.11 | shield-core unitary case published by BHK (Dec 2025) | final-pass prior-art reconfirmation | cited; ours scoped as the extension |
| 2.12 | GSTZ title hyphen | paper-4 bibliography audit (2026-07-12) | fixed; had survived all prior rounds |

## Process events (high level)

prior-art searches: 4+ (bridge anchors; three full-text deep reads;
two sweeps; final reconfirmation). adversarial/verification rounds:
3 (three-agent audit; final four-agent pass; calculation re-runs
bit-consistent). retractions: 1, with published scope. downgrades:
the M3 pair, plus the flash remark downgraded to conditional before
S5 re-upgraded the flank on new evidence. controls: two artifacts
caught by control columns that existed for exactly that purpose;
one caught only by an adversarial agent after the controls
(necessarily) missed it. human steering: green-lit the follow-up
thread, ordered the push hold and title/scope decisions, demanded
honesty-first treatment throughout. Status: final (v-current
includes the 18.8 MeV update); publication pending hold-lift.


## Gate audit passes (release gate; per-lane K: claims 4, biblio 3, numerics 3)

### Pass 1 — 2026-07-13 (Opus x3; first dedicated gate audit) — NOT CLEAN
Three fresh-eyes Opus auditors, one per lane, given no histories/notes.
Numerics ran internal arithmetic/cross-consistency (the simulation
scripts are not co-located, so not re-run); bibliography verified all 58
refs against arXiv/Crossref. Enters at counter 0.

**Claims — NOT CLEAN (1 MAJOR, 4 MINOR).**
- MAJOR (ledger #9): the headline trilemma was asserted unconditionally
  in the abstract slogan and Claim 6.1, though the multiplicity horn is
  a tree-level statement contingent on the resummation/DDP open question
  — the caveat existed only in Sec. 9. FIX: "(at tree level)" on the
  abstract slogan + a tree-level/resummation-contingency sentence in
  Claim 6.1 (points to Sec. 9). Not a wrong result; a scope surfacing.
- MINOR: Prop 6.2 said the divergence needs "no reference to ... any
  sample-space choice" while the adjacent clause said "iff the
  multiplicity sum does" — reworded to ontology-neutral-but-
  multiplicity-conditional.
- MINOR: Sec. 5 "the d=1 rate saturates—a continuum limit exists" is
  over-strong for a log-divergent tadpole driver -> "effectively
  marginal (only logarithmic in d=1, consistent with a continuum limit)".
- MINOR: the abstract's "verified ... to 0.1%" is a d=1-only number
  (Sec. 9 says so) -> "to 0.1% in d=1".
- MINOR: Sec. 9 grading listed the (numerical) factorization verification
  under Theorem-grade -> moved to Measured (the analytic factorization is
  GSTZ's; the authors' contribution is the verification).

**Numerics — NOT CLEAN (1 MAJOR, 2 MINOR).** Every core closed form
reproduced independently (LHFL asymptote TV(inf)=kappa~/sin theta;
growth-law exponents; Compton-Getting dipole template; Lambda^8
knife-edge; 5-sigma photon count).
- MAJOR (ledger #10): the "reconstruction closes" exponent k_max^2.9
  mis-combined the d=1 amplitude power (4.96) into a d=2 reconstruction;
  the correct d=2 value is 1.16 x 4.45 / 2 = 2.58, which closes BETTER
  against the observed 2.7. FIX: 2.9 -> 2.6, using the d=2 power 4.45.
- MINOR (DEFERRED, not an auditor error): the d=2 sweep is labeled
  "N=16..64" with four rate values (a doubling grid over 16-64 has only
  three points); the 2.7 exponent is consistent with a factor-4 k_max
  span but the intermediate grid is non-doubling and unstated. NOT
  edited — the exact N grid can't be recovered without the
  (non-co-located) scripts. To state the grid when the scripts are rerun.
- MINOR: "all twenty-four cells" was undefined -> defined as two
  potentials x two completions x three separations (L=8,10,12) x Alice's
  two bit settings = 24.

**Bibliography — CLEAN (0 major/critical; 5 MINOR).** 58 bibitems; every
\cite resolves, no orphan/undefined; no arXiv ID/DOI points to a wrong
paper (52 confirmed, 1 unverifiable self-reference). All 5 MINOR were
re-verified against arXiv (rule 7) and applied:
- DESIDR2: removed the spurious word "model-independent" from the title.
- KinDipole2026: added author (T. T. Takeuchi) + restored the dropped
  subtitle ("Beyond the Ellis-Baldwin approximation").
- LatticeFVD2022: added authors (Braden, Johnson, Peiris, Pontzen,
  Weinfurtner).
- DESIreview: added authors (Li, Du, Wang, Li, Zhang, Zhang).
- DESIskeptic: added authors (Cortes, Liddle).

Recompiled clean (21 pp, 0 undefined refs/cites). No auditor leads were
rejected this pass (nothing for auditor-error-log.md).

**Counter move:** all three lanes had applied findings, so each lane
stays at 0. After pass 1: **claims 0/4, biblio 0/3, numerics 0/3.**

Note: paper 2's in-text script-path normalization (bare \texttt{name.py}
-> scripts/name.py) was deliberately NOT done here — paper 2 was mid-audit
during the corpus script reorg (user's call). It is the sole paper still
using bare refs; normalize at the user's word or at repo assembly.

## 2026-07-14 — WAVE 6: claims pass 2 (Fable) + biblio pass 2 (Opus) + numerics pass 2 (Opus). TWO MAJORs.
- **claims (Fable, pass 2, adversarial): 2 MAJOR + 7 MINOR + 4 NIT.** Core theorems 7.1/7.2 re-derived clean by the auditor.
  - MAJOR M1 (major-findings 29): thm:instantaneity born-vacuum sentence omitted a hypothesis — the causal age bound regulates only the boost ORBIT, but prop:ladder's reduced integral is UV-divergent (Lambda^4/Lambda^8) in d=3, so a UV-local coupling still has q=inf; the GV2013 example given is UV-soft (exactly the missing case). APPLIED: added "whose reduced integral is UV-finite (a UV-soft coupling, or d=1)" + a clause that a UV-local coupling in d>=2 keeps q=inf; threaded the proof ("q(Lambda), or -- when the reduced integral is UV-finite -- q(t)").
  - MAJOR M2 (major-findings 30): "classical decay rate has a continuum limit in 1+1d" overclaims a bare log-divergent tadpole driver (<phi^2>~k_max^{d-1} is log/marginal at d=1 = slow unbounded growth, not a finite limit; data 0.0127->0.0249 still rising at N=128). APPLIED at all 4 instances (intro item, Sec 5 L528, claim:twoladders L552, Discussion L1121) -> "marginal (logarithmically growing) in 1+1d, power-law divergent in 2+1d".
  - MINOR applied: #5 "admits a well-defined [process/sample space] only relative to a frame" (x3: abstract L61, intro L195, cor:frame L473) -> "non-degenerate" (the minimal process IS well-defined; it is the degenerate zero-lifetime state; a non-degenerate one needs the frame).
  - MINOR PENDING micro-pass: #3 Discussion "factorization verified d=1 only" vs prop:ladder d=3 MC ~3% (internal contradiction -> "0.1% d=1 and ~3% d=3"); #4 sec7.3 "both gated by spectral positivity" refuted by thm:lhfl (bounded-below lossy dimer) -> attribute conditioning door to post-selection; #6 prop:state stated as Prop with no proof -> supply 2-line tree-level <N(t)> OR downgrade to Claim (ties to the standing "p3 prop:state proof" NEW-INVESTIGATION thread); #7 prop:shieldcore "core proved" nowhere uses positivity -> state it proves no-signaling for all dilated product dynamics, positivity only via the conjectured interacting extension; #8 sec7.2 "acausal channel exactly in explosive class" tested on 2 potentials -> hedge; #9 lem:growthlaw silently identifies mean-field growth exponent with ladder-rate exponent -> add pure-birth/mean-field hypothesis. Plus 4 NIT.
- **biblio (Opus, pass 2): 57/57 web-verified, ZERO MAJOR / ZERO hallucinated cites.** 1 MINOR + 5 NIT. MINOR applied: DESIskeptic (Cortes-Liddle) cited for "parameterization-dependent" but its actual argument is statistical (SNe-sample significance combination ~3.1sigma) -> reworded caveat to "the quoted significance depends on which supernova sample is combined, a principled combination giving ~3.1sigma". NIT pending: Smilga "vs."->"versus"; Dvali "footnote 5"->"note 5"; Buoninfante title caps; Coleman erratum note; EGW2014 hyphenation.
- **numerics (Opus, pass 2): CLEAN.** 30+ values across 11 scripts all MATCH; NO d=1/d=2 exponent error (the historically error-prone spot). 1 MINOR provenance (foliation_m3.py does not emit the quoted band-energy fractions 57%/89% or the 100-run N=128/256 settlement means; committed script gives only median v* per N — qualitative v*~0 reproduced). Being CLOSED by the background Fable provenance agent. Two expensive lattice scripts (e4_2d, decomp) not re-run per guard, internally consistent (d=2 log-slope 2.66; reconstruction 1.16x(4.45/2)=2.58).
- Recompiled clean, 21pp. Counters: claims 0, biblio 0, numerics 0 (all had applied findings). Opus-p1-clean -> Fable-p3 TWO MAJORs: cross-model diversity again load-bearing.

## 2026-07-14 — WAVE 6 follow-up: p3 foliation_m3.py provenance -> MANUSCRIPT NUMBERS CORRECTED (MINOR).
The background provenance agent extended foliation_m3.py (band-energy decomposition + 100-run settlement
modes; default sweep output bit-identical, regression-verified; band sums lattice-exact, asserted at
runtime) and found two §5.3 figures did NOT reproduce (conclusions v*~0 + heavy-tailed DO hold):
- Band fractions: quoted "57% in 3<|k|<=6, ~89% above support" matches no single N. Reproduced (seed 11):
  N=64 53.7%/82.8%, N=128 29.2%/93.2%, N=256 18.3%/92.9% (also epoch-dependent). APPLIED: reworded to
  "at N=64, 54% ... ~83% above support; at N=128-256 over 90% above support, majority beyond |k|=6".
- Settlement means: quoted -0.07+/-0.11 / -0.02+/-0.30 not reproduced (raw means outlier-dominated when
  early transfer ~0). Screened (dE/dt>0.1x median): +0.044+/-0.050 / -0.034+/-0.095. APPLIED: reworded to
  "screened means +0.04+/-0.05 and -0.03+/-0.10 ... runs with negligible early-window transfer must be
  excluded or they dominate the raw mean".
p3 recompiled clean (21pp). Numerics counter stays 0 (applied finding). Classed MINOR (secondary §5.3
figures; the frame-erasure conclusion is unaffected). Also fixed a pre-existing foliation_m3.py label bug
(regression header said t in [5,80] but the fit mask was always t>=3).

## 2026-07-14 — WAVE 6 follow-up: remaining p3 claims MINORs APPLIED (in-session).
The MINORs logged "pending micro-pass" above are now APPLIED (verify-before-apply): #3 factorization
"verified in d=1 only" contradicted prop:ladder's d=3 MC -> "verified to 0.1% in d=1 and ~3% by MC in
d=3"; #4+#7 synthesis "both entry points gated by spectral positivity" overclaimed (thm:lhfl's
conditioning signal lives in a bounded-below lossy dimer) -> conditioning door is a post-selection
artifact gated by whether one conditions on survival, positivity gates only the acausal-completions door
+ shield; the finite core (prop:shieldcore) proves no-signaling for ANY dilated local dynamics, positivity
entering only in op:shield; #8 "acausal channel exactly in the explosive class" -> hedged "in the cases
tested (-x^4,-x^2), and as the time-of-flight dictionary predicts"; #9 lem:growthlaw -> added the
pure-birth hypothesis (rates lambda_n=n^alpha, mean-field n-dot=lambda_n). Only #6 (prop:state stated as
Prop w/o proof) LEFT OPEN -> the standing "p3 prop:state proof" NEW-INVESTIGATION thread. p3 recompiled
clean (21pp). Residual for p3: 4 claims NIT + 5 biblio NIT (cosmetic) + prop:state proof.

## WAVE 7 (2026-07-16) — full 3-lane pass (Opus): claims p4 / biblio p4 / numerics p4.
No CRITICAL/MAJOR across all three lanes.
CLAIMS (agent aa2eeaed): prop:state (Prop 6.5) "it diverges iff the multiplicity sum
does" was a literal false-converse — in d>=2 the invariant reduced integral carries
its own UV divergence (prop:ladder), so <N> can diverge with the multiplicity sum
finite. NB the auditor's suggested one-directional downgrade would have BROKEN the
paper's own escape argument (lines ~718 and ~1116), which needs the CONVERSE
(resummed suppression renders the multiplicity sum convergent => first horn relaxes
=> finite). APPLIED the correct fix instead: added the qualifier "with the invariant
reduced integral held ultraviolet-finite (its ordinary UV divergence regulated as
usual)", which preserves the iff in both directions and closes the hole. HELD NITs:
claim:shield (6.1) shield-breaking half inherits the "multiplicity horn" conditioning
by pointer only; lem:growthlaw (2.1) mean-field ODE makes alpha_eff=alpha tautological
(conclusion still correct via Feller exact sum). The standing prop:state PROOF
NEW-INVESTIGATION thread is untouched (only the iff statement was corrected). Claims
stays 0 (finding applied).
BIBLIO (agent a4d1531c): CLEAN. Companion->p01 self-cite claim-support-checked under
amended rule 6 (terminal-indivisibility closed forms match p01 character-for-character,
reciprocity clean). All 2025-26 external preprints web-verified REAL (DESI DR2
2503.14738, ClinePhantom Lambda<=19 MeV, CJM Lambda<=3 MeV, GSTZ2021, GV2013). ~44
canonical refs accepted on standard metadata. 3 cosmetic bibkey-year labels HELD
(ClinePhantom2024 work is 2023; JGB2019 entry is 2021; Barandes2023 entry is 2025 —
entries accurate, keys only). [Control: helper subagents died on 529 Overloaded; agent
self-recovered, verified directly.] Biblio 0->1.
NUMERICS (agent a497d291): CLEAN, no wrong numbers. 14 scripts mapped; ~24 manuscript
values reproduced to precision (I_s 0.619222; factorization 0.999/1.000/1.001/1.000;
dimension ladder slopes 0/2/4; TV(inf) 0.707107 to 2.2e-16; determinacy SNR; dipole
3.7-4.3e-3, N~4-5.5e6; horn-3 machine-zero). Lattice/MC tables (e4_2d d=1/d=2,
closeout d=3, foliation bands, s4a) NOT run per rails — verified via closed-form
backbones (reconstruction 1.16 x 4.45/2 = 2.58 ~ 2.6; d=2 internal exponent 2.66 ~ 2.7;
no d1/d2 exponent mix-up). 1 NIT: s4b script self-annotation (g/2w)^2=0.005625 vs
reproduced peak 0.0229; manuscript claim only qualitative, holds; no paper impact.
Numerics 0->1.
Recompiled clean (21pp), main.log 0 errors / 0 undefined refs+cites.

## WAVE 8 (2026-07-16) — full 3-lane FABLE pass: claims p5 / biblio p4 / numerics p4. 2 MAJOR (ledger 32,33) + MINORs.
The all-Fable diversity check overturned wave-7's all-Opus "clean" on p3.
CLAIMS (agent a8a52293) — 2 MAJOR:
- [MAJOR ledger 32 APPLIED] thm:instantaneity rate-vs-rate-DENSITY conflation. eq:factorization is Gamma/V; theorem said "total exit rate infinite" but born-vacuum comparison quotes a rate density (dim E^4) -> dimensionally mismatched, and "total rate infinite" doesn't distinguish the ghost from a healthy vacuum in infinite V. Fix: "exit rate per unit volume" on both sides + "(total rate diverges already at any fixed finite volume)". [Fable's own suggested one-directional fix was NOT used - it would have mis-stated; the per-volume fix is the correct scope.]
- [MAJOR ledger 33 -> see numerics lane] the Sec-5 reconstruction exponent (belongs to numerics).
- [MINOR APPLIED] sec:foliation.2 false converse "the state that determines no foliation is EXACTLY the state whose ghost dynamics is ill-posed" -> "is the state ... (one direction only---a frame is necessary, not sufficient, to tame q=inf)".
- [MAJOR->NO FIX, ledger/auditor-error-log] "1+1d marginal/log growth, still rising at N=128" — Fable called it a MAJOR (last data increment collapses), but the claim is THEORY-backed (log tadpole) and "still rising" is literally true; applying the implied fix would have reversed ledger entry 30. Left as-is; logged as wrong-severity.
- HELD: thm:instantaneity "d>=2 ... prop:ladder" (ladder computes only d=3) MINOR; abstract(vi) iff hedge; prop:shieldcore "only where"/uniqueness; strength-inventory ladder grade; prop:state no proof (standing thread); abstract(iv) hedge.
BIBLIO (agent ab6085a9) — 1 MINOR:
- [MINOR APPLIED] L711-715 over-attribution: "PT/no-ghost quantization [BM], Euclidean state-space surgery [HawkingHertog]---which the companion paper showed exit the sample space" -> p01 shows sample-space-exit ONLY for Bender-Mannheim; ZERO Hawking-Hertog content. Fix: scoped "(which the companion paper showed exits the sample space)" to the no-ghost quantization only.
- [nit APPLIED] Dvali2011 "footnote 5" -> "note 5" (it's Dvali's bib note [5], not a footnote).
- 52 external refs verified, 0 hallucinated/misattributed. Self-cite Companion->p01 SUPPORTED 7/8 sites.
NUMERICS (agent a26870d4, ran ALL 14 scripts to completion) — 1 MAJOR:
- [MAJOR ledger 33 APPLIED] Sec 5 reconstruction "(using the d=2 amplitude power 4.45)": 4.45 is the d=1 power; d=2 is 4.96 (ORCHESTRATOR RE-RAN decomp.py: d=2 +4.96, d=1 +4.45). "2.6"->"2.9" (1.16x4.96/2=2.87), "closes"->"closes to ~10%", "observed 2.7"->"~2.7". Section's load-bearing finding unaffected. [Wave-6 + wave-7 Opus numerics both verified the wrong-dim "1.16x4.45/2=2.58 MATCH".]
- [NIT] foliation_m3.py docstring stale band numbers (paper matches OUTPUT). every other manuscript number reproduced exactly.
Counters: claims 0 (applied), biblio 1->0 (applied), numerics 1->0 (applied). Recompiled 21pp, 0 errors / 0 undefined refs+cites.

## WAVE 9 (2026-07-16) — full 3-lane (OPUS, convergence re-check of wave-8). 2 NIT applied (numerics); no CRITICAL/MAJOR/MINOR.
CLAIMS pass 5 (Opus, adversarial) CLEAN: thm:instantaneity, prop:ladder, lemma:growthlaw, thm:lhfl, prop:state, prop:shieldcore, foliation-determinacy, trilemma all re-derived. Wave-8 MAJOR (ledger 32, rate-density/per-volume) re-derived and HOLDS — the infinity is carried at fixed finite V, distinguishes ghost from healthy vacuum. 4 NIT HELD (abstract "precisely alpha_eff>1" softening; thm:instantaneity title clause; lemma:growthlaw pure-power tautology note; Cline year-bundle = known-good per biblio lane).
BIBLIO pass 4 (Opus) CLEAN: 12/12 high-risk externals web-verified (0 hallucinated); 9/9 Companion self-cite SITES claim-supported against paper1/ (column-norm closed forms, terminal-indivisibility params, "exits the sample space" subsection all present). Wave-8 HawkingHertog over-attribution stays fixed.
NUMERICS pass 4 (Opus) — re-ran decomp.py FULL: 4.96=d2 / 4.45=d1 with CORRECT labels (wave-8 MAJOR ledger 33 fix HOLDS, no cross-dim mislabel). Every table/figure/exponent reproduces. 2 NIT APPLIED (confirmed wrong-as-written):
- [NIT APPLIED] L549 "raised to the d=2 amplitude power 4.96 predicts k_max^2.9" — literally 1.16x4.96=5.75, not 2.9; omitted the variance->amplitude /2 factor. Fixed to "raised to HALF the d=2 amplitude power (4.96/2=2.48, since rate~a^4.96 while variance~a^2)"; 1.16x2.48=2.88~2.9 now computes as written.
- [NIT APPLIED] L668 "over 90% lands above the support, the majority beyond |k|=6" — at N=128 the |k|>6 band is 48% (majority only by N=256). Softened "the majority"->"much of it".
- [NIT HELD] foliation_m3.py docstring stale band numbers (code comment, not manuscript).
Counters: claims 0->1, biblio 0->1, numerics STAYS 0 (applied NITs). Recompiled 21pp, 0 errors / 0 undefined refs+cites. Agents a4ead479 (claims) / a62422f6 (biblio) / a710c2cd (numerics).

## WAVE 9 STATE: claims 1 / biblio 1 / numerics 0.

## WAVE 10 (2026-07-16) — full 3-lane (claims Fable / biblio Fable / numerics Opus). 3 MINOR applied (claims); no MAJOR. Diversity check fired.
CLAIMS pass 6 (Fable, adversarial): every theorem re-derived + held (instantaneity per-vol; lem:growthlaw m=6->1.167 vs measured 1.172; thm:lhfl; prop:shieldcore); reconstruction 1.16x2.48=2.88 confirmed. 3 MINOR APPLIED:
- prop:state (L733): "the particle-number expectation N(t)" omitted the per-volume qualifier while invoking the per-volume factorization -> "per unit volume N(t)/V" (the un-propagated ledger-32 rate-density-vs-total class).
- abstract (L51): "blowup corresponds PRECISELY to alpha_eff>1" overstated (counterexample lambda_n = n log^2 n: explosive, alpha_eff->1) -> dropped "precisely", added "(up to marginal logarithmic cases at alpha_eff=1)".
- trilemma headline (claim:trilemma L697) + abstract (L81): "Ghosts"/"ghosts" -> "Coupled ghosts"/"coupled ghosts" (a decoupled ghost satisfies all three; bullet 2 already said "no coupled ghosts").
1 MINOR REJECTED (auditor-error-log): thm:instantaneity "d>=2 keeps q=inf" — statement CORRECT (reduced integral ~ Lambda^{d-1} diverges for all d>=2 by the same power counting prop:ladder uses at d=1,3); "restate as d=3" would WEAKEN a true claim. No edit. 3 NIT held.
BIBLIO pass 5 (Fable): 57/57 external verified (0 hallucinated, all suspicious 2025-26 arXiv IDs real), 10/10 Companion sites PASS. 3 completeness MINOR HELD (arXiv-only refs Babichev2024=PRD 112 084007, DESIDR2=PRD 112 083515; Smilga2005 title punctuation) -> arXiv-only is valid pre-publication; deferred to the final-publication biblio pass. Lane CLEAN 1->2.
NUMERICS pass 5 (Opus): CLEAN. Every number traces; Sec-5 factor-of-2 (4.96/2=2.48 -> 2.877~2.9) independently confirmed; foliation N=64 bands 53.7%/82.8% reproduce. foliation_m3.py stale 57%/89% docstring FIXED to ~54%/~83% (housekeeping, thrice-flagged). "~2.7" fit non-unique NIT held. Counter numerics 0->1.
Counters: claims 1->0 (applied), biblio 1->2 (clean), numerics 0->1 (clean). Recompiled 21pp, 0 errors / 0 undefined. Agents a924c52f (claims) / af2fbb59 (biblio) / a8c143ad (numerics).

## WAVE 10 STATE: claims 0 / biblio 2 / numerics 1.

## WAVE 11 (2026-07-17) — full 3-lane (all-FABLE, user-directed). claims 2 MINOR + consistency applied; BIBLIO CERTIFIED (K=3); numerics clean.
CLAIMS pass 7 (Fable): all theorems re-derived + held (wave-10 fixes confirmed: prop:state N/V sound both directions; trilemma "coupled" scopes out a decoupled ghost; generic-ray area clean). Applied:
- [MINOR] abstract L79 + intro L230: "latency distance-independent EXACTLY in the explosive class" dropped the body hedge (L894 "in the cases tested: -x^4, -x^2") -> "distance-independent in the explosive class (in the cases tested)" at both sites.
- [MINOR] Sec 7.3 L905: "apparent superluminal signaling has EXACTLY two entry points" = unproven taxonomy completeness -> "enters at the two points we identify".
- [consistency] completing the wave-10 headline fix: intro trilemma L234 + bullets L708/L714 still bare "ghosts" -> "coupled ghosts" (ALL trilemma sites now consistent).
4 NIT held. Counter claims stays 0 (applied).
BIBLIO pass 6 (Fable): CLEAN. 57/57 external verified (0 hallucinated), 9/9 Companion sites PASS incl. provenance site L106. 3 completeness NITs (DESIDR2/Babichev2024/DESIreview journal-refs) held for a final-publication pass. **Counter 2->3 = CERTIFIED (K=3).**
NUMERICS pass 6 (Fable): NO manuscript error. Every number re-traced (factor-of-2 confirmed; decomp d2/d1 labels correct). 2 flagged MINOR both NON-errors: (a) "every band shows v*~0" not reproduced at REDUCED stats -> ORCHESTRATOR RE-RAN full --bands nens=16: N=256 v*_b = -0.004/0.078/0.063/-0.083 (all ~0) CONFIRMED (reduced-stats noise; rejected lead -> auditor-error-log); (b) "~2.7" fit defensible (2.59 all-points / 2.99 last-3), held. Counter 1->2. Recompiled 21pp clean. Agents ac7c3cc5 (claims) / a6cceb5a (biblio) / adbd188c (numerics).

## WAVE 11 STATE: claims 0 / biblio 3 CERT / numerics 2.

## WAVE 12 (2026-07-17) — claims pass 8 (Fable) + numerics pass 7 (Fable). 1 MAJOR + 5 MINOR applied (claims); numerics CERTIFIED.
CLAIMS pass 8 (Fable, abstract-consistency sweep): theorem spine re-derived clean; findings concentrated in summary text.
- [MAJOR ledger 36 APPLIED] Intro item 4 (L190-192) dropped thm:instantaneity's "tree-level (orbit-degenerate) rates" hypothesis + said "infinite TOTAL exit rate" (theorem: per unit volume); the body's own DDP analysis (L431-433) shows distinctness alone does NOT suffice. Fix: added the hypothesis + "exit rate per unit volume" + born-vacuum "with a UV-finite reduced integral (UV-soft, or d=1)".
- [MINOR] abstract (v) L72 shield "would render observable" as fact -> "(shown for the finite core; conjectured in general)".
- [MINOR] intro item 7 L222 "at EXACTLY two points" -> "at the two points we identify" (completes the wave-11 synthesis fix).
- [MINOR] Sec 9 L1070 "Three of the four cells are decisive for both questions" contradicts the 2x2 matrix (top row = 2 cells decide both; bottom-right decides ghost only; bottom-left inconsistent) -> corrected breakdown.
- [MINOR] Discussion L1106 mis-graded the dimension ladder as "Theorem-grade" -- prop:ladder states it "fitted to three decimals" (numerical) -> moved to "Measured".
- [MINOR] Sec 5 L547 amplitude powers a^4.96/a^4.45 unlabeled by dimension -> added (d=2)/(d=1) (values re-confirmed by numerics).
3 NIT held. Counter claims stays 0.
NUMERICS pass 7 (Fable): re-ran ALL 14 scripts at full statistics; every number reproduces (Sec-5 factor-of-2, v*~0 nens=16, all tables digit-for-digit). Only finding = the 4th-occurrence "~2.7" fit (LS 2.59 / last-3 2.99); HELD as defensible (non-unique fit; load-bearing 10% closure robust) -> auditor-error-log. Counter numerics 2->3 = CERTIFIED (K=3). Recompiled 21pp clean. Agents a637051e (claims) / ad03c6aa (numerics).

## WAVE 12 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 13 (2026-07-17) — claims pass 9 (FABLE; broadened). 1 MINOR applied, several HELD. Counter stays 0.
Spine re-derived clean; all cross-refs/cites resolve. Findings now hypothesis-precision (4th Fable pass):
- [MINOR APPLIED] prop:state: "diverges iff multiplicity sum" fails at ZERO coupling (reduced integral=0 -> N/V finite while multiplicity sum diverges). Fix: "reduced integral held ultraviolet-finite AND NONVANISHING".
- [MINOR HELD, subtle] thm:instantaneity born-vacuum d>=2: the causal cap makes orbit volume s-dependent, so finiteness needs the s-WEIGHTED integral, not just "reduced integral UV-finite"; the (mu t)^2 example masks it. Needs careful derivation -> held/logged (NEW-INVESTIGATION thread).
- [MINOR HELD, subtle] decision matrix: the signal-excluded cell decides "against configs" only under bound-saturation (dilution lets a sub-bound CJM phantom keep beables) -> knife-edge should be in the cell header.
- [MINOR HELD, recurring] prop:ladder (2pi)^2 normalization crossed between the two verifications (3rd flag) -> a normalization note; held pending factor-verification.
5 NIT held (symbol overloads q/s/Gamma -> notation pass; recurring d=2-interpolated + rho+p null-flux; Feller pure-birth). Counter claims stays 0. Recompiled 21pp clean. Agent aaf7e7c6.

## WAVE 13 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 14 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 10 OPUS (cross-model check after 4 straight Fable waves).
1 MAJOR (ledger 39) + 1 MINOR applied; load-bearing theorems (thm:lhfl conditioning closed form, prop:shieldcore no-signaling core, lem:growthlaw+Feller, prop:state iff, instantaneity ETERNAL-vacuum half) all re-derived SOUND by Opus.
- [MAJOR ledger 39 APPLIED] thm:instantaneity BORN-vacuum clause: "reduced integral UV-finite (UV-soft coupling, or d=1)" is INSUFFICIENT for d>=2. The causal cap cosh(eta)<t*sqrt(s) on the orbit measure sinh^{d-1}(eta) d(eta) gives int_0^{eta_max} ~ (t*sqrt s)^{d-1}/(d-1) for d>=2, injecting a weight s^{(d-1)/2} into the reduced integrand -> finiteness needs the CAUSALLY-WEIGHTED int ds s^{(d-1)/2} sigma_d rho_n rho_g |M|^2 < inf. Counterexample d=3, integrand~s^{-5/4}: plain converges (UV-finite), s^{1/2}-weighted diverges -> q=inf. CONFIRMS + DERIVES the wave-13 "[MINOR HELD, subtle] NEW-INVESTIGATION thread"; an independent Fable verifier re-derived the weight from the paper's own measure+cap, matching the D=2 log-slope I_s=0.619 and the GV (mu t)^2 factor. Fixed at 3 coupled sites (grep-all-copies): thm clause, intro (i)-echo L196, proof body L470 (which ALSO restated the weak hypothesis) + added the causal-cap derivation. p3 21->22pp.
- [MINOR APPLIED] abstract (ii): "dimension ladder (Lambda^0/Lambda^4/Lambda^8) reproduces the CJM scaling" -> only the Lambda^8/M_Pl^4 rung is CJM's (Lambda^0, Lambda^4 are this paper's own results). Fix: "whose Lambda^8/M_Pl^4 rung reproduces the CJM scaling".
- [NIT HELD] decision-matrix saturation is already disclosed in-body (knife-edge stated at L1009-1013); optional hoist. The two other wave-13 held threads (decision-matrix knife-edge cell decisive only under bound-saturation; prop:ladder (2pi)^2 norm) remain open NEW-INVESTIGATION.
Counter claims stays 0. Recompiled 22pp clean. Agents ae4625fb (claims) / a438d346 (born-vacuum verifier).

## WAVE 14 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 15 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 11 FABLE (adversarial).
2 MAJOR (ledger 41, 42) + 4 MINOR + 2 NIT applied; load-bearing thms (thm:lhfl, prop:shieldcore, lem:growthlaw+Feller, prop:state, instantaneity d>=2 + eternal halves) re-derived SOUND.
- [MAJOR ledger 41 APPLIED] the wave-14 born-vacuum d=1 clause "weight is trivial, plain UV-finiteness suffices" is FALSE -- d=1 capped orbit factor = arccosh(t sqrt s) ~ ln t + (1/2)ln s is LOGARITHMIC; needs int I ln s ds < inf (counterexample I~1/(s ln^2 s)). d=1 clause -> log-weighted condition. OPUS VERIFIER CONFIRMED. Corrects ledger 39. LESSON: don't accept a verifier's self-downgrade of a subtlety it raised (the wave-14 verifier flagged this; I wrongly accepted "keep d=1 plain").
- [MAJOR ledger 42 APPLIED] decision-matrix "signal excluded -> against configurations" hides a bound-saturation assumption (the standing wave-13 held thread) -- a sub-saturating small-Lambda frame-cutoff phantom keeps beables. Cell -> "no OBSERVABLE decay ... IF the cutoff saturates the bound"; + scoping sentence.
- [MINOR APPLIED] F3 prop:ladder (2pi)^2: "dGamma/dlnT=0.6193" was really (2pi)^2 dGamma/dlnT (script prints "Gamma x (2pi)^2") -> fixed (same stripped convention). The recurring 3rd-flag thread, closed. F4 abstract (v) parenthetical -> "hiddenness proved for the finite core; observability argued at tree level". F5 abstract (iv) "invisible" -> "flat ... within measurement resolution". F6 prop:state: added the analytic argument (number expectation sums the same final-state phase space; boost-orbit members share particle number) so the factorization is ARGUED not just channel-toy-verified.
- [NIT APPLIED] F8a "positive for any nonvanishing coupling" -> "whenever the reduced integrand does not vanish identically"; F8b label cor:frame -> claim:frame.
- [HELD -> notation pass] F8c Gamma/s symbol overloads. F7 already-satisfied (Sec 7.2 already hedged "in the cases tested"; "cannot both be kept" not in current text).
Counter claims stays 0. Recompiled 22pp clean. Agents a95a3ed5 (claims) / a216d9d7 (verifier).

## WAVE 15 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 16 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 12 FABLE (convergence check on wave-15).
ZERO MAJOR; wave-15 fixes VALIDATED (auditor independently re-derived the born-vacuum d=1 log-weight as "exactly the right one", recomputed I_s=0.6195, confirmed the (2pi)^2 convention). Load-bearing thms (thm:lhfl, prop:shieldcore, prop:state, lem:growthlaw) re-derived SOUND. 4 MINOR applied:
- [MINOR APPLIED] decision-matrix "three of four cells decisive---TWO for both questions" left STALE by the wave-15 cell scope fix (the phantom-established/signal-excluded cell is now conditional) -> "one decisive for both, a second for both only where the flux is detectable". ANOTHER grep-all-copies propagation miss on my own wave-15 edit.
- [MINOR APPLIED] instantaneity theorem: the nonvanishing-reduced-integrand condition was load-bearing but only in the proof -> added "and a reduced integrand not vanishing identically on the accessible range" to the theorem hypothesis.
- [MINOR APPLIED] Feller "birth-type chain explodes iff sum 1/lambda_n < inf" -> "PURE-BIRTH chain" (birth-death needs Reuter's; the lemma already said pure-birth).
- [MINOR APPLIED] abstract (iii) "only relative to a frame" -> "a frame or birth surface" (matches body claim:frame).
Counter claims stays 0. Recompiled 22pp clean. Agent a0441fd2.

## WAVE 16 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 17 (2026-07-17, conv 9fa0e0c5): CLAIMS pass 13 FABLE. ZERO structural MAJOR; wave-15/16 fixes VALIDATED (d=1 log-weight re-derived, I_s recomputed 0.6195); load-bearing thms all SOUND. Findings applied (with the sibling-sweep GATE -- this wave exposed TWO grep-all-copies misses on prior fixes):
- [MINOR APPLIED] decision-matrix "counts against beables" -- a THIRD copy (the "two-sided test" sentence L1109) still un-swept after wave-15 fixed the cell + wave-16 fixed the count -> "count against the born-vacuum rescue outright (low-Lambda frame-cutoff region undecided)".
- [MINOR APPLIED] "birth-type" chain-class copies at the INTRO (L166) + ABSTRACT (L49) -- wave-16 fixed only the body -> "pure-birth" at all sites.
- [MINOR APPLIED] instantaneity theorem "ultraviolet-finite" -> "finite (locally integrable, no on-shell pole, + UV-finite)" (a real-axis pole is UV-finite but divergent). intro "in a lattice experiment the state proposes the frame" overclaimed a null result -> "the UV disposes in a lattice experiment while the state proposes BY COVARIANCE (the lattice could not resolve the early window)". prop:state "multiplicity-conditional" -> "conditional on the tree-level state".
- [NIT applied] d=1 log-growth "still rising at N=128" -> "+though the final doubling adds little; numerics lane owns the error bars" (light; respects the wave-8 ruling that the log-tadpole framing is theory-backed). Gamma vs Gamma/V/Gamma_orb notation (F7) -> notation pass.
Counter claims stays 0. Recompiled 22pp clean. Agent a4a107ea.

## WAVE 17 STATE: claims 0 / biblio 3 CERT / numerics 3 CERT.

## WAVE 18 (2026-07-17, conv 954cb52d) — notation pass + Fable claims pass 14
NOTATION: four-momentum q->Q (frees exit-rate q), vacuum-age T->t (frees T=temperature; matches Thm 4.1), joint no-signaling map Gamma=|U|^2 -> W, dimer coupling s parenthetical. CLAIMS: spine SOUND (Lemma 2.1, Thm 4.1 body both halves, Prop 3.1, Thm 6.1, Prop 6.3, Sec 5 reconstruction all re-derived). ZERO new structural MAJOR. Fix-propagation siblings applied: intro item 4 dropped the ledger-41 d=1 log-weight (body has it) -> log-weighted qualifier; intro item 8 trilemma dropped "(at tree level)" (abstract+body carry it) -> added. MINOR: "every rescue"->"every rescue that preserves definite configurations"; Sec 3 "(unregulated) orbit volume"; decision-matrix cell scoped to phantom-DE identification; abstract (iv) phi^2 log-at-d=1 caveat; Thm 4.1 d>=2 UV-divergence citation scoped (Prop computes d=3). Held defensible: Thm 4.1 log-weight sign formality. Recompiled 22pp clean. Counter claims 0.

## WAVE 19 (2026-07-17, conv 954cb52d) — Fable claims pass 14
Spine SOUND (Thm 4.1 both dir all d, Thm 7.1, Lemma 2.1); CONFIRMED the wave-18 d=1 log-weight fix complete+correct. MAJOR (fix-propagation sibling of wave-18): abstract (iii) "every rescue in the literature ... supplies one" still universal (wave-18 fixed only intro item 4) -> "every configuration-preserving rescue"; also scoped the claim-body bullet L731. MINOR: decision-matrix asymmetry from wave-18 partial fix (scoped only one cell) -> scoped item(a) "w>=-1 retires it as the DE explanation", bottom-right cell "observable ghost hypothesis", summary "fourth inconsistent under phantom-DE identification"; Sec 7.2 punchline "(in the completions tested)"; Sec 7.3 "two points" hedged to finite core; Discussion trilemma "(at tree level)". Recompiled 22pp clean. Counter claims 0.

## WAVE 20 (2026-07-17, conv 954cb52d) — Fable claims pass 16
Spine SOUND (Thm 4.2 all d + d=1 log-weight again). MAJOR (sibling of wave-19 fix): signaling-exhaustiveness hedge in Sec 7.3 body not propagated to abstract(vi)+intro item 7 -> "(exhaustively so in the finite core)" both. MAJOR (scope): decision-matrix cell "exit-the-sample-space horn wins" -> "(at tree level)" (a resummed suppression keeps beables). MINOR: channel-flat "within resolution"; Thm 4.2 "continuous reduced integrand"; abstract "dimension-and-coupling ladder"; Claim 6.1 shield cutoff-edge scoped; horn-2 "quantum equilibrium". Left defensible: L1082 "both axes" (axes ARE simulated). Recompiled 22pp clean. Counter claims 0.

## WAVE 21 (2026-07-17, conv 954cb52d) -- OPUS cross-model claims pass 17
CROSS-MODEL: no CRITICAL/MAJOR; Thm 4.2 (all d + d=1 log), decision matrix, trilemma, numerics all re-derived SOUND. LOW: Thm 4.2 integrand "continuous" -> "continuous, nonnegative" (positivity needs sign-definite); s^(d-1)/2 display tagged "d>=2; d=1 log below"; signaling "provably the only ones" -> conditioning door provably unique, completions door open. Recompiled 22pp clean. Counter claims 0.

## WAVE 22 (2026-07-17, all-lane all-Fable; user: "run until Fable returns NOTHING 3x each lane") -- HEAVIEST PAPER THIS WAVE
- CLAIMS (Fable): 1 MAJOR (ledger 53, Thm 4.2 Lambda^2-vs-Lambda at d=2, cross-confirmed by numerics; conclusion q=inf unaffected) + 2 MIN + 3 NIT. Applied: intro "proves"/"we show" -> measured wording ("attributes"/"find numerically"); finite-core uniqueness scoped to the framework's operations at 3 sites (abstract vi, intro, body L941); (NIT) rho+p!=0 -> perfect-fluid-form frame; (NIT) Sec-9 Argued inventory adds the state-content factorization (prop:state); (NIT) Thm 6.1 states s<sin theta so tilde-kappa real.
- NUMERICS (Fable): 1 MAJOR (ledger 52) + 3 MIN. MAJOR: d=2 lattice rate top rung 0.8186 non-reproducing; bumped e4_2d.py d=2 nens 6->60, requoted row N=16..64 = 0.0216/0.1186/0.2260/0.4093, "~k^2.7"->"~k^2.1", reconstruction "closes to ~10%"->"reproduces to ~30% (over-predicts)", + ensemble caveat. MIN: I_s 0.619222 -> 0.6192 (grid) converging to 0.6195; naive channel prediction restated as linear ~4x excluded a fortiori (not the log 2.2x); Thm 4.2 (= claims MAJOR).
- BIBLIO (Fable): 3 MAJOR (ledger 49 invented "pragmatic" CJM quote -> quotes dropped; 50 ClinePhantom 2308.12989 now PRD 108 095033 (2023) added [reverses wave-21 "arXiv-only"]; 51 DGBdipole MeV-band -> GeV-band) + 3 MIN (ClinePhantom 2nd paper year 2023->2024; Cortes -> Cortes-circumflex; provenance \cite{Companion} -> hub repository). All 6 Crossref/source-verified before applying.
- Recompiled 22pp clean. Counters: claims CERT-n/a (was 0)->0; numerics CERT->0; biblio CERT->0. Fable-clean streak: all p3 lanes 0/3.

## WAVE 23 (2026-07-18, all-lane all-Fable) -- all three lanes had residual findings, all MINOR/NIT
- CLAIMS: no MAJOR. 3 MIN + 1 NIT: intro item-5 d=1 rate "marginal (logarithmically growing)" -> "effectively marginal (consistent with the log tadpole; not separable from saturation at accessible N)"; trilemma horn given the "in-principle" qualifier (Sec-8 low-Lambda cell keeps all three under a practical reading); prop:state DEMOTED Proposition->Claim (claim:state) to match the "Argued" grade + paper convention (3 refs updated); abstract (iii) "only relative to a frame or birth surface" -> "only relative to a structure that individuates the channels (in every known rescue a frame or birth surface)".
- NUMERICS: no MAJOR (all wave-22 fixes re-validated: d=2 exp 2.10 reproduced, I_s 0.6195, table reproduces). 2 MIN + 2 NIT: "drift an order of magnitude below thresholds" -> honest "~3x below at top d=2 cutoff, >=10x elsewhere"; d=2 rates to 2 sig figs (0.022/0.12/0.23/0.41) + ensemble note (medians over 60; d=1 over 8) + scatter ~20-25% + check-granularity; closeout slope "4.3->4.1" -> "global fit 4.3 (4.1 upper interval)"; e4_2d docstring d=2 "marginal (log)"->"linear (Lambda)" + decomp docstring stale "2.7"->"2.1".
- BIBLIO: 1 MIN -- GSTZ verbatim quote "non-compact"->"noncompact" (publisher record). All else clean; ClinePhantom=PRD 108 095033 re-confirmed.
- Recompiled 22pp clean. Counters: claims/numerics/biblio all 0/3.


## WAVE 24 (2026-07-18, all-lane all-Fable) -- includes a wave-23 REVERT
- CLAIMS: no MAJOR. 1 MIN + 2 NIT: intro item-3 factorization "0.1%" scoped "in d=1" (matching abstract/Sec-9; d=3 is ~3% MC); Lemma 2.1 Feller ladder given positivity/range (lambda_n>0, n>=1); abstract-(i) "verified numerically" reordered so it no longer attaches to the marginal-log cases.
- NUMERICS: no MAJOR (wave-23 d=2 requote re-validated -- I_s 0.6192->0.6195, exponent 2.10). 2 MIN: d=2 rates rounded to ONE sig fig (0.02/0.1/0.2/0.4) since the 2nd figure is not seed-stable at nens=60 (threshold-check granularity ~0.5), scatter note widened to ~20-40%; d=1 "final doubling adds little" -> "within the ensemble scatter at n=8" (not seed-robust).
- BIBLIO: 1 MIN + 1 NIT. MIN: the mu~2e-3 eV window's "0.1 mm inverse-square-law" half was attributed to GV2013 (which has no ISL content) -> added Kapner2007 (PRL 98, 021101 (2007), verified) and scoped GV2013 to the cascade bound. NIT: **REVERTED the wave-23 "non-compact"->"noncompact" change** (wave-23 auditor misread the source; GSTZ actually reads "non-compact", confirmed by wave-24 auditor + orchestrator WebFetch) -> restored "non-compact". See auditor-error-log.
- Recompiled 22pp clean. Counters: all three lanes 0/3.

## WAVE 25 (2026-07-18, all-lane all-Fable)
- CLAIMS (Fable): no MAJOR. 2 MIN + 2 NIT: prop:shieldcore given its load-bearing UNITARITY hypothesis + ancilla bookkeeping (proof uses U_A^dag U_A=1); Lemma 2.1 growth clauses generalized to any pure-birth ladder (algebraic/exponential mean-field), with lambda_n=n^alpha confined to the Feller-sum sentence (the lemma is applied to non-power-law ladders); abstract/intro "exhaustively so in the finite core..." -> "the conditioning point provably the unique marginal-breaker in the finite core; the completions door left open" (body proves uniqueness only for the conditioning point); Sec-5 table row labels given explicit N values (16,32,64,128 / 16,32,48,64).
- NUMERICS (Fable): no MAJOR (wave-24 fixes re-validated: I_s 0.6192->0.6195, d=2 exp 2.1, closeout global 4.3/upper 4.1). 2 MIN + 2 NIT: d=1 rates to 2 s.f. (0.013/0.018/0.024/0.025) + inline sibling + extended ~+-30% seed-scatter caveat (medians over 8); settlement "consistent with zero" -> "no significant positive signal (<=2sigma)" (a 44-run replication gave +0.17+-0.08); "exactly N-independent" -> "up to O((k dx)^2) dispersion (<=3%)"; added an upper-interval-slope print to qft_bridge_closeout.py (emits 4.09, matching the quoted 4.1).
- BIBLIO (Fable): CLEAN -> Fable-clean 1/3. Independently CONFIRMED the wave-24 "non-compact" revert was correct (GSTZ source reads "non-compact") and Kapner2007 is valid.
- Recompiled 23pp clean (page count 22->23 from added lines). Counters: claims 0/3, numerics 0/3, biblio 1/3.

## WAVE 26 (2026-07-18, all-OPUS cross-model check; Fable exhausted)
- CLAIMS (Opus): 1 MIN + 1 NIT + 2 Fable-pending MIN applied. Opus: (a) Claim shield -- de-conflated "no-signaling" from "observable foliation" and made the finite core (prop:shieldcore) spectrum-independent (it needs neither bounded-below nor equilibrium; positivity enters only in the interacting extension), matching Sec-7.3; (b) NIT sigma-vs-sigma_d(s) disambiguation in thm:lhfl. Fable-pending: (c) Sec-8 "the one" second shield-breaker -> names both (Valentini + AmblardDrezet arrival-time); (d) Sec-7.2 marginal row "norm->0.000" -> "in-box norm", + note -x^2 is e.s.a. so its variants are box-controls not completions (only -x^4 is limit-circle). Opus VALIDATED the d=2 exponent (initially suspected wrong, then confirmed) + TV(inf) + factorization cross-model.
- NUMERICS (Opus): 2 NIT applied -- prop:ladder d=3 MC error "~3%" -> "~3-7%" (H=1.5 point 6.8%; + Discussion sibling L1183); d=1 seed-scatter caveat "~+-30%" -> "~+-30-50% (upper-skewed)". I_s, closeout slopes, dimension ladder all re-validated.
- BIBLIO (Opus): CLEAN. Confirmed the wave-24 non-compact revert + Kapner2007 + all self-cite claim-support cross-model.
- Recompiled 23pp clean. Fable-clean streaks: claims 0/3, numerics 0/3, biblio 1/3 (unchanged; all Opus-cross-model-validated).

## WAVE 27 (2026-07-18, all-OPUS cross-model check, 2nd consecutive; Fable exhausted)
- CLAIMS (Opus): CLEAN. All theorem-grade results re-derived from scratch (Lemma 2.1 growth law, instantaneity boost-orbit divergence, LHFL closed form Eq. 5.1, no-signaling core); trilemma/shield-breaker/self-adjointness taxonomy adversarially probed, all adequately hedged. Zero findings.
- NUMERICS (Opus): CLEAN. Full reproduction ledger -- I_s=0.6192->0.6195, GV log-slope 0.6193, dipole templates, foliation bands/settlement, lattice tadpole exponents (d=2 k_max^{1.16}, quoted-rate fit 2.13). The auditor's earlier reduced-sample Gamma/V_orb "constant?" suspicion was CLEARED by the full 36M-sample run (constant within 3-7%). Rail-compliant (long sweeps corroborated by cheap cross-checks).
- BIBLIO (Opus): CLEAN. Every externally-verifiable field re-checked via Crossref/arXiv; verbatim quotes (GV2013, GSTZ "we do not know the true rate", non-compact) confirmed; GSTZ metastable/JGB published-title publisher-record matches re-confirmed; self-cite (Companion=paper1) claim-support + reciprocity verified. (Novelty sweep not run -- WebSearch budget exhausted; disclosed, not a finding.)
- Recompiled 23pp clean (no edits). Fable-clean streaks: claims 0/3, numerics 0/3, biblio 1/3 (unchanged; all Opus-cross-model-validated a 2nd time).


## SESSION 2026-07-18/19 (numbering unification + claim-support + rotation-four Fable)
- Folder paper2/ -> paper3/ (series 3); cite keys -> codenames; release-gate leak sentence + biblio %-comment notes removed.
- Claim-support (Opus + Fable cross-model): CLEAN; QFT spine verified by DIRECT PDF extraction (GSTZ Eq.88 + "non-compact Lorentz group" verbatim; CJM Eq.9/Eq.3; GV Eq.72/73; Cline 18.8 MeV mechanism; BHK marginal-factorization eqs). Fixes: GV mu~=2e-3 window reworded to credit GV's OWN combination (their Eq.73); BHK "established" -> "no-signaling reading of the causal-locality condition they impose".
- Rotation-four Fable: NUMERICS CLEAN (13/15 re-run, I_s -> 0.6195). CLAIMS 1 MINOR + 3 NIT fixed -- the MINOR was an INTERNAL "numerics lane" JARGON LEAK in the manuscript (line 554) -> reworded; this exposed a gap in check_manuscripts.py (hardened with a "(claims|numerics|biblio) lane" pattern). NITs: "column norms"->"squared column norms"; "unique marginal-breaker" quantifier carried to abstract/intro; de-garbled trilemma "accessible" parenthetical. BIBLIO 1 MAJOR + 2 MINOR + 1 NIT (all verified vs primary sources): MAJOR AmblardDrezet first author "S."->"A." (arXiv:2604.17507 = Arnaud; ledger 56, survived prior CERT); KinDipole -> ApJS 285,3; DGBdipole claim-support (dropped "exposure systematics", which Kashlinsky et al. argue against); Deffayet2504 "proves"->"demonstrates numerically". Fresh streaks: num 1/3, claims 0/3, biblio 0/3.

## t3 SCRIPT RELOCATION 2026-07-19 (resolved the paper4 orphan)
- `t3_cosi_forecast.py` MOVED here from paper4/scripts/ (git mv, history preserved). It is the diffuse-background / COSI-era detectability FORECAST for the phantom-decay signal of Sec (b): its outputs are paper3 s own numbers -- dipole 3.7-4.3e-3 (imported from its sibling s4c_dipole_template.py, already here), the 0.12% spectral-edge modulation, and the 5-sigma photon counts. Displaced into paper4 only by the folder->series rename (git: was in paper3/scripts/ pre-unification, when "paper3" was the OLD conditioned folder; the rename carried it to paper4). Now CITED in Code availability alongside s4c. NOTE: filename keeps the legacy "t3" task-prefix (paper3 s other detection scripts are s4a/s4b/s4c) -- optional future rename to s4d for convention consistency.
- CONVENTION RENAME 2026-07-19: t3_cosi_forecast.py -> s4d_cosi_forecast.py (matches the s4a/s4b/s4c detection-script family); Code-availability + docstring updated (docstring keeps "task T3" provenance). Nothing imports it; no other live reference.

## FABLE CLAIMS PASS 2026-07-19 (Fable-spend rotation-four wave, 2nd fresh Fable pass)
- **SOUND: zero CRITICAL/MAJOR.** 9 load-bearing spines independently re-derived cross-model (Lemma growthlaw + PU/cascade checks; Prop 3.1 factorization incl. every dimension-ladder rung s^-2/s^-1/2/s^1/s^3; Thm 4.2 both branches incl. capped-orbit t^{d-1} + GV log-slope 0.6193 vs I_s=0.6192; Thm 7.1 closed form fully re-derived TV->κ̃/sinθ; Prop 7.3 shieldcore; completions -x^4/-x^2 taxonomy; §9(b) MeV/dipole numbers 3.69e-3/0.12%/photon-counts; trilemma; abstract-vs-body item-by-item). Applied: 1 MINOR (thm:instantaneity d=1 log-weight parenthetical was loose -- arccosh(t√s)~ln(2t)+½ln s needs BOTH the plain reduced integral AND the ln-s weighting, and bare "∫...ln s" is sign-wrong for s<1; rewrote to (1+|ln s|)-weighted, orchestrator-verified via the arccosh expansion) + 1 NIT (Thm 7.1 flagged the s and σ collisions but not q=dimer amplitude vs exit rate q -> added the q flag, matching the paper's own standard). Skipped 1 harmless NIT (Lemma 2.1 α vs α_eff, auditor said harmless).
- Streak: p3-claims had findings this pass (MINOR+NIT applied) -> NOT a clean-streak pass. Recompiled clean; both gates PASS.

## FABLE BIBLIO PASS 2026-07-19 (Fable-spend rotation-four wave, biblio round 2) -- CLEAN
- **55/55 external bibitems CLEAN, 0 fix-needed, 0 unverifiable.** All verbatim quotes + BOTH equation-number citations verified against RAW sources (Crossref JSON / downloaded LaTeX / raw HTML): GSTZ "we do not know the true rate" (+ Eq.88 + the dK_0 non-compact-Lorentz sentence, from downloaded ghostdecay.tex), CJM Eq.(9) age-regulated rate + "gamma<t0√s" (from CJM LaTeX), GV Γ~10⁻⁶(μ⁸/M_p⁴)(μT)² + cascade/ISL bounds + 0.1mm (from GV LaTeX), Dvali note-5, DESI DR2 "2.8-4.2σ" + skeptic "3.1σ" verbatim. Session fixes CONFIRMED in place: AmblardDrezet "A." (Arnaud), DGBdipole (Kashlinsky ApJL 961 L1, Fermi-LAT GeV), KinDipole (ApJS 285,3). 3 publisher-vs-arXiv title divergences where the bib CORRECTLY follows the publisher (GSTZ2021 "metastable", JGB2019, EGW2014) -- do NOT fix backward.
- **CLEAN pass -> advances the p3-biblio Fable-clean streak.** No manuscript change.

## FABLE NUMERICS PASS 2026-07-19 (Fable-spend rotation-four wave) -- 1 MAJOR + minor
- **1 MAJOR (ledger 59): §9(b) edge-modulation detectability overclaim.** Text claimed the 0.12% spectral edge recoverable at ~10σ with a few×10⁶ photons -- that is s4c's LOCAL step-edge signal-only stat. For the DIFFUSE cosmological background the redshift-integrated arriving spectrum is a linear WEDGE; s4d gives ~3σ@4e6, N_5σ≈1e7 (×9 window penalty at 3% res). Surfaced BECAUSE this session cited s4d in §9(b); orchestrator re-ran s4d and confirmed. FIXED to wedge stats (~3σ few×10⁶; 5σ near 10⁷). DIPOLE (primary signature, 4-5.5e6 for 5σ) UNAFFECTED/correct.
- **Otherwise CLEAN.** All 15 scripts run in full (longest ~25 min); every headline number reproduces: I_s=0.6192, ladder slopes 0/2/4=Λ⁰/Λ⁴/Λ⁸, d=2 exponent 2.12, d=1 rows, decomp a^4.96/a^4.45 + reconstruction ~30% closure, s1 TV residuals, s2/s2b latencies+silence, s3 settlement, s4a/s4b/s4c dipole 3.7-4.3e-3 + N_5σ 4-5.5e6, foliation --bands 54%/83%/>90% + --settlement +0.044±0.050 / -0.034±0.095 (digit-exact), s5. All deterministic (fixed-seed default_rng, no PYTHONHASHSEED); 100-run settlement correctly supersedes the old 16-run fluke. Applied 1 NIT: stage2 "flat across truncations" -> "nearly flat (within 2%)" (α=1.25 drifts 2%). Noted (not a defect): §5 uncertainty parentheticals (~20-40% scatter, ±0.2) are notes.md-documented ensemble estimates, not script-reproducible.
- Recompiled 23pp, 0 undefined; both gates PASS.

## OPUS CROSS-MODEL WAVE 2026-07-20 (Wave A; claims + numerics-revalidate; biblio skipped -- Fable cleared 55/55 this session)
- **FULLY CONVERGED cross-model.** Claims (Opus): spine SOUND -- independently confirmed the two session fixes: the d=1 (1+|ln s|) log-weight is genuinely strictly-stronger-than-plain-UV (explicit counterexample f~1/(s ln²s)); the §9(b) wedge edit is correct + internally consistent + leaves the dipole intact. Thm 4.3, LHFL closed form (TV->κ̃/sinθ), no-signaling core, growth-law, trilemma all re-derive SOUND; no overclaim. Numerics-revalidate (Opus): the ledger-59 §9(b) WEDGE FIX is CONFIRMED numerically right -- reproduced 4e6@3%res->3.0σ, N_5σ≈1e7, ×5-10 penalty; wedge derivation (linear ramp from redshift line-of-sight integral, num/analytic=0.9942) correct; dipole 3.7-4.3e-3 + N_5σ 4-5.5e6 UNAFFECTED; spot-checks I_s=0.6192, log-slope 0.6193, α_eff 1.0/1.172, foliation settlement v*≈0 all reproduce. Non-issue: s4c prints 0.25% peak-to-peak = 2β vs manuscript 0.12% amplitude=β (consistent). No new findings; the session's MAJOR (ledger 59) is now cross-model-confirmed. No manuscript change this wave.

## OPUS DEEP CLAIMS 2026-07-20 (Wave D; Nth adversarial pass) -- SOUND
- no error; a real lead CHASED INTO SCRIPTS AND KILLED (the d=2 ~Λ exponent verified correct via phase-space density ρ(s)~s^{(d-3)/2}, energy exp 3d-5=0/1/4, not naive Λ²); born-vacuum d=1 log-weight, §(b) dipole/edge/photon chain, Thm 7.1 closed form + shield all held. No manuscript change.

## OPUS DEEP CLAIMS 2026-07-20 (hunt-what-was-rationalized wave, p1-p4) -- SOUND, 1 MINOR applied
- No CRITICAL/MAJOR. One exposition MINOR: "knife-edge" used with OPPOSITE valence at two sites under the SAME $\Gamma\propto\Lambda^8$ premise -- L1068 "This is a knife-edge" (detectable band narrow) vs L1141 "makes this a wide region rather than a knife-edge" (undetectable-$\Lambda$ region). Reconcilable (complementary subjects) but a reader snag. Fixed L1141 by naming the subject: "makes this \emph{undetectable}-$\Lambda$ region wide (the \emph{detectable} band above being the knife-edge of the dilution estimate)".
- PRIMED CHECKS CONFIRMED (no change): ledger-59 wedge fix consistent everywhere -- grep of `step`/`wedge`/`sharp`/every `\sigma` shows NO stale "step"/"~10\sigma" sibling in abstract/intro/decision-matrix/discussion; born-vacuum causally-weighted hypothesis holds at every branch (incl. the L386 closeout $d\Gamma/d\ln t=0.6193\approx I_s$ = coefficient, not a contradiction of the log-weighted finiteness condition); no total-vs-per-volume slip; tree-level qualifier not dropped anywhere; no-signaling vs spectrum de-conflation clean (Prop 7.6 universal no-signaling vs survival-conditioning as the only uncovered local op). d=2 UV-scaling "plain counting" NIT held (honestly labeled "plain counting"; auditor: not a defect).
- Recompiled 23pp, 0 undefined. Both gates PASS. No MAJOR (ledger stays 59).

## OPUS NUMERICS 2026-07-20 (Wave 4; reproduce-from-scripts) -- CLEAN (all reproduce)
- Ran all 15 scripts. EVERY quantitative claim reproduces exactly. Ledger-59 §9(b) WEDGE confirmed from s4d_cosi_forecast.py: ~3σ at 4e6 photons, N_5σ≈1.0e7, edge-window 0.00716 (wedge) vs 0.06429 (step) at 3% res = ×9.0 penalty; dipole from s4c: 3.7-4.3e-3, 4.0-5.5e6 photons for 5σ, 0.12% edge. Prop-ladder: I_s=0.6192 grid→0.6195 converged (independently extended cutoff u_max=5000→0.619500); d=1 log-weight dΓ/dlnT=0.6193≈I_s; UV ladder Λ⁰/Λ⁴/Λ⁸; d=3 global slope 4.33 (4.09 upper interval). Thm 7.1 TV(∞)=κ̃/sinθ to 2.2e-16; completions table (V=−x⁴/−x² latencies); foliation bands + SEEDED settlement means (+0.044±0.050 N=128, −0.034±0.095 N=256). 0 findings; 1 NIT no-fix (the wedge window fractions live only in the script; prose compresses to "×5-10", faithful).
- No manuscript change.

## FABLE CLAIMS 2026-07-20 (cross-model diversity wave, p1/p3/p5/p6) -- 1 MINOR + 2 NIT applied
- Fable re-derived the instantaneity theorem (both branches, orbit caps), Thm 7.1 LHFL from scratch, the shield algebra, the wedge physics. Zero CRITICAL/MAJOR. **Independently CONFIRMED the ledger-59 wedge is physically correct** (redshift-superposed cutoffs -> linear wedge) and the knife-edge polarity consistent.
- Applied: (MINOR #54, FALSE CONVERSE) d=1 finiteness "requires the log-weighted condition" -> "is guaranteed by" -- necessity fails as s->0 (causal cap s>1/t^2 removes the ln s weight; counterexample f~1/(s ln^2 s) has finite capped rate but fails the log-weight); added the sufficient-not-necessary clause. (NIT #55) "Both of its edges" -> "Two of its three edges" (trilemma triangle). (NIT #56) s4d_cosi_forecast.py was the ONLY script not inline-cited in the body though the wedge numbers come from it -> cited at the wedge sentence.
- HELD-defensible: (MINOR #57) decision-matrix "signal seen (dipole+edge)" presupposes a frame-cutoff phantom; born-vacuum gives dipole-without-edge -- but line 658 already scopes the edge, body correct. (NIT) shield-core proof marginal shows sum over Alice a' + |b><b| without the explicit Bob-ancilla sum -- statement declares it and the no-signaling conclusion (via U_A^dag U_A=1) is unaffected; schematic notation, held.
- Recompiled 23pp, 0 undefined. Both gates PASS. No MAJOR.

## 4-WIDE FABLE CLAIMS AUDIT 2026-07-23 — spine SOUND (zero CRITICAL/MAJOR); MINOR + 3 NITs applied
- Fable re-derived the rich seams SOUND: born-vacuum causal weight, d>=2 orbit measure (∫sinh^{d-1} ≃ (t√s)^{d-1}/(d-1)), trilemma tree-level scope, instantaneity clause — all correctly hypothesized at every site. Trilemma sibling-consistent across all 5 statement sites; arithmetic (TV(t), κ̃/sinθ asymptote, dipole photon counts, Λ^8 dilution) recomputed exact.
- APPLIED (minor-ledger #85): MINOR — TV(∞)=κ̃/sinθ closed form scoped to "its broken-phase dimer analog" (Thm 7.1 is the broken-phase dimer, not LHFL's own unbroken construction), abstract+intro. NITs — marginal-breaker "among dilated local operations" → "over the framework's dilated local dynamics" (matches the Sec-7 synthesis; the "among" scoping was vacuous), abstract+intro; exit-rate q x-ref "Secs 3-4" → "the explosion dictionary above"; Claim-4.2 intro punchline "only relative to a foliation" → "only relative to an individuating structure---a frame or a birth surface".
- HELD: Remark 6.4 opener NIT (charitably scoped already). Recompiled clean, gates PASS.

## W22 CONVERGENCE RE-CONFIRMATION 2026-07-26 (Opus, adversarial; claims+numerics+biblio) — DEFECT-FREE; convergence HOLDS
- Every spine re-derived from scratch, hypotheses intact, no over/under-claim: σ_d(s)=½s^{(d-1)/2} Jacobian (cosh²−sinh²=1); causal-cap orbit integral (t√s)^{d-1}/(d-1) [d≥2], arccosh~ln2t+½ln s [d=1] — the emergent s^{(d-1)/2} causal weight correctly flagged as a SECOND factor distinct in origin (no double-count); dimension-ladder UV (3d-7)/2 -> Λ⁰/Λ⁴/Λ⁸ + causal-weighted d=2 Λ²; born-vacuum ~t^{d-1}; TV(∞)=κ̃/sinθ=√(1−(s/sinθ)²) full re-derivation; prop:shieldcore (Σ|a'⟩⟨a'|=1 collapse; conditioning breaks the first equality); thm:instantaneity hypotheses exactly sufficient, no false converse.
- **NUMERICS CLEAN (standalone, no stiff runs):** I_s 0.61922->0.61949; UV slopes 0/2/4; TV(∞) 8-digit match 3 param sets; GV log-growth 0.6193; channel toy 1.026 at M=32 + plateau 0.0640/0.0643; horn-3 ⟨n⟩=sinh²(gt) 2.27847 at gt=1.2 + requant exact 0; d=2 exponent 2.16; CG dipole β=1.234e-3, 3β=3.70e-3. All reproduce.
- **BIBLIO CLEAN:** 59 keys / 59 bibitems, 0 orphans either direction, 0 duplicates, no undefined/multiply-defined; Coleman/Feller/CJM spot-verified; codename-year offsets = house convention. Standing machine-provisionals (human-PDF before circulation): Takeuchi 2602.07389, Amblard-Drezet 2604.17507, Deffayet 2604.21823, Buoninfante 2606.18349, DESI review 2606.21826, DESIDR2/Babichev/ClinePhantom journal metadata.
- No manuscript change. Both gates PASS (unchanged). **p3 CONVERGENCE HOLDS (still 3/3).**

## W23 CROSS-PAPER BIBLIO CORRECTION 2026-07-31 (orchestrator, Crossref-verified) - 2 fixes; counter reset
- Surfaced by the W23 Fable p5 audit, which flagged p5's GSTZ title as wrong. Verifying that flag against Crossref REFUTED it (p5 was right) and exposed the inverse error here: p3 carried "Is negative kinetic energy **meta-stable**?" while Crossref (10.1103/PhysRevD.103.115025) gives "metastable". Also Konnig2016 carried "**Ya.**~Akrami"; Crossref (10.1007/JHEP11(2016)118) gives "Yashar Akrami" => "Y.". Both were introduced by the 07-24 Opus biblio wave (commit 9895cef) applying arXiv/INSPIRE forms over the published record - the same defective premise as major-ledger #79 (Smilga), whose sibling edits were never re-audited. **major-ledger #84.** Corpus re-grepped: zero stale copies. Rebuilt clean (3 overfull, all <6pt), both gates PASS.
- NOTE: this resets p3's clean streak. The rest of the paper was not re-audited this wave.

## W25 WIDE-OPEN AUDIT 2026-08-01 (Fable, adversarial) - NO MAJOR; NUMERICS CLEAN (15/15 scripts); 1 MINOR applied; counter -> 0
- **All 15 scripts executed, exit 0; every quoted number reproduced.** Spine re-derived by hand (growth-law lemma and the Feller sum, the boost Jacobian d^2Q = (1/2) ds d(eta) and sigma_d = (1/2) s^{(d-1)/2}, the causal-cap integrals in both d=1 and d>=2, the strictness of the log-weighted condition via the explicit counterexample 1/(s ln^2 s), Thm 7.2 in full including the asymptote, the shield-core marginal). Trilemma stress-tested against an eternal Lorentz-invariant UV-soft ghost with no birth surface -- it stays instantaneous, inside horn 1 as claimed. Strength ledger audited against every abstract and intro claim: the proved/measured/argued/conjectured grading is consistent.
- **MINOR applied (configuration provenance, the #83/#92 family):** the dimensional-dichotomy table's two rows are measured at DIFFERENT configurations (d=1: lambda=0.25, L=32, DeltaE=25, n=8; d=2: lambda=0.1, L=16, DeltaE=10, n=60) and nothing said so. Since companion papers inherit this dichotomy, a reader could take the rows as a same-parameter rate comparison. Added a footnote naming both configurations and stating that the claim is the dichotomy itself.
- **REJECTED, and it matters:** the auditor proposed re-attributing the "GV already note the 0.1 mm / mu ~ 2e-3 eV window" claim, on the strength of TWO independent ar5iv reads finding nothing. The orchestrator downloaded the arXiv PDF and extracted it with pypdf: GV Eq. (73) states "mu >~ 2 x 10^-3 eV, which is marginally consistent with (72)", the text states violations occur "up to 0.1 mm", and GV's own reference [21] IS Kapner et al. PRL 98, 021101 (2007). The paper is correct and well-sourced. **Second false negative from ar5iv in two waves** -- standing rule added: an ar5iv "not found" is not evidence of absence; fetch the PDF.
- **HELD (genuinely machine-extracted):** the GSTZ Eq. (88) locator and the dK_0 verbatim quote, unreachable through ar5iv truncation. minor-ledger #174.
