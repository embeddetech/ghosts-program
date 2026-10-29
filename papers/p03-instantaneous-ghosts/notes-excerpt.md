# Lab-notebook excerpt: paper 3 (Ghost vacuum decay as a stochastic process)

Excerpted from the full running notebook (notes.md) in the program hub:
https://github.com/embeddetech/ghosts-program - which also contains the
preceding paper-1 entries and later follow-ups (the wedge-edge statistics and
the 18.8 MeV bound update that postdate the paper).

---

## 2026-07-11 — FOLLOW-UP THREAD: the QFT bridge (theory stage)

Post-v1.0 work; the released paper is frozen. Question (paper's
Outlook, item 2): does "the ghost is an explosion problem" survive the
passage to QFT vacuum decay?

### Literature anchors (all verified by web search 2026-07-11)

- **Carroll–Hoffman–Trodden**, PRD 68, 023509 (2003)
  (astro-ph/0301273): phantom (ghost) dark energy vacuum decays into
  positive-energy matter + negative-energy phantoms; "the decay rate
  is naively infinite because there is no boundary to the allowed
  phase space"; a ~10⁻³ eV momentum cutoff keeps the vacuum alive for
  the age of the universe.
- **Cline–Jeon–Moore**, PRD 70, 043543 (2004) (hep-ph/0311312), "The
  phantom menaced": vacuum → ghost pairs + photon pairs through
  GRAVITY alone; divergent final-state phase-space integral; only a
  LORENTZ-VIOLATING UV cutoff Λ tames it (Λ ≲ 3 MeV from the cosmic
  gamma-ray background); "theories of ghosts with a Lorentz-conserving
  cutoff are completely excluded."
- **Gross–Strumia–Teresi–Zirilli**, PRD 103, 115025 (2021)
  (arXiv:2007.05541), "Is negative kinetic energy metastable?": the
  divergence is an integral over the NON-COMPACT LORENTZ BOOST ORBIT
  of the final state; whether this means fast decay or exponentially
  suppressed (metastable) decay is NOT settled; they argue
  metastability up to cosmological times is possible.
- **Novelty check**: no prior work found connecting ghost vacuum decay
  to Markov explosion / instantaneous states / non-conservative
  minimal semigroups. The bridge below appears to be new.
- **Probability side (standard)**: a birth-type continuous-time Markov
  chain with rates λ_n explodes (infinitely many jumps in finite time,
  mass exits the state space) iff Σ 1/λ_n < ∞ (Feller); a state with
  TOTAL exit rate q = ∞ is an *instantaneous state*, and no honest
  (stable, standard) Markov process exists with one.

### The bridge

Configuration space: Fock occupation configurations n = {n_k} over
momentum modes (countable at finite volume + cutoff) — beables in the
Barandes sense. At lowest order the effective dynamics out of a
configuration is a jump process with golden-rule rates; the
regulator-independent object is the MINIMAL semigroup (paper §8).

**B1 (dictionary extension — time of flight has a Fock-space
sibling).** The 1D dictionary's classical integral T = ∫dx/√(2(E−V))
= Σ(sojourn times to infinity) has the exact jump-process image
T_Fock = Σ_n 1/λ_n = expected time to reach infinite occupation.
Explosion ⇔ T_Fock < ∞ is Feller's criterion — the same "finite total
time to infinity" statement in the fourth currency. (QM cross-check:
the quadratic cascade grows coherently, ⟨n⟩ = sinh²(gt), classical
field-space escape time = ∞ → transient ✓ matches Theorem-C
uniqueness; the malicious quartic has field-space T < ∞ → explosive ✓.
The coherent/incoherent distinction matters: naive golden-rule ladder
rates λ_n ∝ n² for the two-mode cascade would wrongly predict
explosion — the incoherent-jump reduction is only valid with a dense
final-state continuum, i.e., genuine QFT, not two isolated modes.
This validity condition must be stated honestly in any writeup.)

**B2 (the Lorentz-invariant ghost vacuum is an INSTANTANEOUS state).**
CJM's divergence, read stochastically: the vacuum's total exit rate
q_vac = Σ_channels (finite per-channel rates) diverges because the
channels form a non-compact Lorentz-orbit family. q = ∞ is precisely
the instantaneous-state pathology: NO Markov process — conservative,
minimal, or otherwise — exists. This is strictly WORSE than the QM
malicious case (explosive: finite nonzero t*). The QM → QFT passage
upgrades the pathology: explosion (t* > 0) → instantaneity (t* = 0⁺),
driven not by faster per-channel escape but by infinite channel
multiplicity — the field-theoretic image of the deficiency channel
count going from (2M,2M) → (∞,∞) → continuum-per-unit-volume.

**B3 (the cutoff is conservativity data, and it must break Lorentz).**
A UV cutoff compactifies the channel orbit → q < ∞ → the minimal
process exists again (explosive or transient by B1). CJM's "no
Lorentz-conserving cutoff" becomes: *the data needed to make the ghost
vacuum a valid stochastic process cannot be specified
Lorentz-invariantly* — the same structural statement as the paper's
"conservative completions are an S-matrix at infinity, data not
contained in H," now with the twist that in QFT even the MINIMAL
process needs regulator data (because instantaneity, unlike explosion,
kills the minimal semigroup too). Choose: Lorentz invariance or a
well-defined process on the beables — not both, for a coupled ghost.

**B4 (the CJM ↔ GSTZ dispute is a sharp dichotomy in this currency).**
The open QFT question "fast decay vs metastable" is exactly: does the
boost orbit contribute CHANNEL MULTIPLICITY (distinct final
configurations ⇒ rates add ⇒ q = ∞ ⇒ instantaneous) or GAUGE
REDUNDANCY (boost-related finals identified / measure-zero overlap ⇒
finite physical rate ⇒ transient/metastable)? The stochastic framing
does not resolve the dispute but states it as a single binary question
about the configuration space — which configurations are distinct
beables — rather than about regularization technique. Note the
resonance with the paper's H¹ theme: what must be quotiented is a
group orbit.

**B5 (trilemma, QFT edition).** The paper's trilemma survives with
sharpened horns: (i) minimal explosive process — now requires Lorentz
violation even to EXIST (B3); (ii) conservativity via S-matrix at
infinity — now an infinite-dimensional reflection law per unit volume;
(iii) exit the sample space (PT/no-ghost quantization) — unchanged,
and now visibly the only Lorentz-invariant option on the menu, at the
price of no configuration-space probability at all. This may be the
sharpest available statement of what Mannheim's program is buying.

### Stage-2 numerics (planned, laptop-scale)

1. Mode-scaling: 1+1D lattice ghost+normal fields, N modes; classical
   field-space escape time vs N (does inf over escape family → 0?);
   total quantum leak rate vs N (extensive = transient per volume vs
   super-extensive = instantaneity fingerprint).
2. Rate-growth dichotomy at QM level: engineered ladders with
   λ_n ~ n^α — verify explosion onset at α > 1 (Feller) with the Fock
   drift/leak machinery; the malicious quartic should sit in the
   explosive class via its ladder image.
3. Boost-orbit toy: non-relativistic stand-in for channel multiplicity
   (couple the escape to a k-continuum of transverse channels with
   flat measure) — watch q_vac diverge with channel count.

### Caveats

Perturbative (golden-rule) reasoning where CJM/GSTZ are perturbative;
the instantaneous-state statement B2 inherits whichever side of the
B4 dichotomy is true — B2 is CJM's horn, stated sharply, not a
resolution; no gravity constraints; 1+1D toys only at stage 2.

---

## 2026-07-11 — QFT BRIDGE STAGE 2: numerics (all four experiments)

Code: `qft_bridge_stage2.py` (~2 min). All four signatures came out as
designed; E4's verdict is the one genuinely new datum.

**E1 (Feller onset, the V4 diagnostic transported to Fock space).**
Pure-birth ladder λ_n = n^α, absorbing top N ∈ {200…1600}, absorbed
mass at t=6:
- α=0.8: 0.0000 at every N; α=1.0 (Yule, marginal): 0.61 → 0.02,
  decaying with N — regular;
- α=1.25: 0.961/0.954/0.947/0.941 and α=1.5: 0.988/0.987/0.987/0.987 —
  **N-independent absorption ≈ 1 = explosion**, exactly the
  box-independence signature of `explosion_theorem.py` V4.

**E2 (the paper's dichotomy IS Feller's).** Ladder exponent
α_eff = d log ṅ / d log n: identity α_eff = 1 + 1/m for algebraic
blowup n ~ (t*−t)^{−m}, = 1 for exponential growth. Measured:
quadratic cascade slope 1.0000 (transient/marginal ✓); classical
quartic-PU blowup slope 1.1720 vs predicted 7/6 = 1.1667 (energy
proxy n ~ τ^{−6}) ✓ explosive. One-line lemma worth keeping:
*finite-time blowup ⇔ α_eff > 1 ⇔ Feller explosion of the ladder
image* — the growth LAW, not the growth amount, decides.

**E3 (channel multiplicity vs orbit measure — B4 made concrete).**
Vacuum coupled to M flat quasi-continua (g=0.02, band ±8, ρ=10,
Γ₁ = 0.0253, exact eigendecomposition up to dim 5153):
- flat measure (boost-orbit stand-in): fitted Γ = 0.0252, 0.0504,
  0.1009, 0.2027, 0.4088, 0.8302 for M = 1…32 vs prediction M·Γ₁ =
  0.0253…0.8093 — **within 3% throughout, unbounded growth**: the
  instantaneous-state trend (CJM horn);
- decaying measure g_k = g e^{−k/4}: Γ converges to 0.0640 vs
  predicted plateau 0.0643 (GSTZ/metastable horn).
Channel counting is the entire difference; with a finite band the
flat case would eventually hit the hybridization ceiling Γ ~ W
(observed in a first run with Γ ≈ W — kept as a methodological note:
golden-rule fits need Γ ≪ bandwidth ≪ recurrence).

**E4 (classical lattice vacuum decay vs UV cutoff — SUPPRESSED, not
divergent).** φ (normal) + χ (ghost) on N sites at FIXED volume
L=32, coupling 2λφ²χ² in the eqs (λ=0.25), vacuum-mimic zero-point
initial data, absolute energy-transfer threshold ΔE_φ = 25, median
ensemble times:
- N = 8/16/32: t_thr = 106/64/46 (rate rising with cutoff);
- N = 64: t_thr = 149 — rate DROPS ~3×. Confirmed with an
  independent seed and 16 samples: N=32 median 55.9 [45.3, 68.2] vs
  N=64 median 158.9 [120.9, 194.2] — non-overlapping quartiles.
- λ=0 control: no growth at any N ✓.
**Verdict: the classical zero-point cascade is UV-finite — even
UV-suppressed.** Plausible mechanism (conjectural): self-consistent
effective-mass shifts m_φ² += 2λ⟨χ²⟩, m_χ² −= 2λ⟨φ²⟩ grow with the
cutoff (⟨φ²⟩ ~ log Λ in 1+1D) and detune the φ↔χ pair resonance.
Consequence for the bridge: the instantaneity danger is NOT visible
in classical lattice dynamics at fixed volume — it lives in the
quantum channel measure (E3), i.e., precisely in the B4 question of
whether the boost orbit counts as multiplicity. Coherent with B2.

### Combined stage-2 statement

The explosion dictionary acquires a verified Fock-space column
(E1+E2); the QFT vacuum question is isolated into a single measured
dichotomy (E3): rate ∝ channel count (no limit) vs rate ∝ measure
(finite) — and the classical field theory (E4) declines to produce
the divergence on its own. What remains for a real QFT statement:
compute the golden-rule channel measure of the actual boost orbit
(relativistic 2-ghost + 2-photon final states) and decide
multiplicity-vs-redundancy — a calculation, not a simulation.

### Caveats

E3 is channel counting without Lorentz kinematics; E4 is classical,
1+1D, median-of-8/16, and the detuning mechanism is unproven;
`qft_bridge_stage2.py` runtime dominated by E4's stiff ensembles.

---

## 2026-07-11 — QFT BRIDGE STAGE 3: the relativistic channel measure

Code: `qft_bridge_stage3.py` (~1 min). The boost-orbit structure of
ghost vacuum decay, computed and numerically verified.

### Theorem (orbit factorization of the ghost vacuum rate)

For vacuum → (normal pair) + (ghost pair) with any Lorentz-invariant
|M|², total 4-momentum zero forces the normal pair's 4-momentum q to
equal the sign-flipped ghost pair's, and (shown in 1+1d; the
structure is general)

  Γ/V = ∫ d²q/(2π)² ρ_n(q) ρ_g(q) |M|²
      = [∫ dη] × (1/2)(2π)⁻² ∫ ds ρ_n(s) ρ_g(s) |M(s)|²,

with ρ(s) the invariant two-body phase-space density and η the pair
rapidity. The first factor — the boost-orbit volume — is INFINITE in
every spatial dimension d; all d-dependence lives in the reduced
∫ds. **Numerical verification (V1, m_n=1, m_g=0.7, contact |M|²=1):**
brute-force integration of the constrained (k1,k2) phase space with
rapidity cutoff |η|<H gives Γ(H)/[H·I_s/(2π)²] = 0.999, 1.000,
1.001, 1.000 at H = 1,2,3,4 (I_s = 0.619222) — linear in the orbit
volume, slope the reduced integral, to 0.1%.

**Self-correction logged:** the stage-1 back-of-envelope "d=1
converges" (scale counting E^{3d−6}) samples a NON-orbit direction
and misses a vanishing Jacobian (v₃ → v₄ van Hove line) along the
boost flow; the orbit-volume divergence is present in d=1 too. The
numerics confirmed the invariance argument over the naive counting.

### Corollary 1 (dimension ladder of the REDUCED measure)

V2, fitted log-log slopes vs the s-cutoff (exact to 3 decimals):
d=1 contact: 0.000 (UV-FINITE reduced integral); d=3 contact: 2.000
(= Λ⁴ in energy); d=3 with the CJM gravitational vertex |M|² ~
s²/M_Pl⁴: 4.000 (= Λ⁸/M_Pl⁴) — **Cline–Jeon–Moore's published
scaling recovered from the orbit-quotiented measure alone.**

### Corollary 2 (E4 coherence)

The classical 1+1D lattice (stage 2, E4) follows single trajectories
— no sum over orthogonal orbit channels — and its rate was UV-finite
/ suppressed: consistent with the d=1 reduced integral's slope 0.
The stage-2 surprise is the quotient-side physics, as it must be.

### Corollary 3 (frame individuation; B3/B4 sharpened)

Members of a boost orbit are distinct outcomes only relative to a
frame (a detector, a bath, a cutoff surface). CJM's conclusion that
only a Lorentz-VIOLATING cutoff regulates the rate is, in this
currency, the statement that the frame which individuates the
channels must be supplied before q_vac is finite: **a coupled ghost
admits a well-defined configuration-space stochastic process only
relative to a preferred frame.** The B4 dichotomy
(multiplicity/instantaneous vs redundancy/metastable) is the choice
of sample space: momentum configurations in a frame vs boost-orbit
equivalence classes. GSTZ metastability = the quotient choice, whose
rate is the reduced integral (UV-finite in d=1, Λ⁴ or Λ⁸/M_Pl⁴ in
d=3).

### Status of paper #2

Theory bridge (B1–B5) + stage-2 numerics (E1–E4) + stage-3 theorem,
corollaries, and verifications now form a complete arc: *the
Ostrogradski ghost's QFT catastrophe is the divergence of a channel
measure over the Lorentz group; whether it is instantaneity or
metastability is the choice of beables; either way the sample space
requires a frame.* Remaining before drafting: (i) check the
factorization statement in d=3 numerically (only d=1 verified);
(ii) read GSTZ §-level to align the redundancy horn with their
actual argument (only the abstract-level claim used so far);
(iii) decide venue/format (letter-length follow-up vs section in a
v2).

### Caveats

Contact-model kinematics; perturbative golden rule throughout; the
d>1 factorization asserted by invariance, verified only in d=1; the
frame-individuation corollary is an interpretation of CJM's result,
not new mathematics; GSTZ engaged only at abstract level so far.

---

## 2026-07-11 — QFT BRIDGE: LITERATURE DEEP READ + ATTRIBUTION
## CORRECTIONS (three parallel full-text reads)

Full-text reads of CJM (hep-ph/0311312), GSTZ (2007.05541), and a
wide sweep. Everything below supersedes the attribution language of
the stage-3 entry.

### CORRECTION 1 — the factorization is GSTZ's, not ours.

GSTZ eq. (88) (quartic coupling, vacuum rate in d spatial dims) is
EXACTLY the [reduced ∫ds] × [divergent boost-orbit ∫dK₀] structure of
our stage-3 "theorem":
  ρ̇₁ ∝ ∫_{4m²}^∞ ds (s−4m²)^{d−2}/s × ∫_{√s}^∞ dK₀ K₀ (K₀²−s)^{d/2−1},
with their diagnosis verbatim: "the vacuum initial state ∅ is now
Lorentz-invariant so that the final state too must be the same in all
frames. This is why the rate contains a dK₀ integral over the
non-compact Lorentz group." CJM's eq. (9) is the regulated special
case (boost capped by formation time γ < t₀√s → Λ¹⁰t₀²/M_Pl⁴; their
Λ⁸/M_Pl⁴ is dimensional analysis under a CMB-frame 3-momentum
cutoff). **Status of our stage 3, corrected: independent rederivation
+ first numerical verification (0.1%, d=1 brute force) of the
GSTZ/CJM decomposition — not a new theorem.** GSTZ is the mandatory
citation for the decomposition; CJM for the Lorentz-violating-cutoff
horn.

### What remains genuinely novel (triple-checked, no prior art found
### under any phrasing)

1. The Markov reading: instantaneous states / Feller explosion /
   minimal non-conservative semigroups applied to ghost vacua; the
   Fock-ladder column of the explosion dictionary (Σ1/λ_n as time to
   infinity); the E1/E2 verifications.
2. Naming the crux: CJM-vs-GSTZ as CHANNEL MULTIPLICITY vs GAUGE
   REDUNDANCY of the boost orbit. GSTZ draw the split only in
   footnote 11 ("other authors regulate the boost divergence ...
   adding a Lorentz-breaking or non-local cut-off"); nobody develops
   it as the decisive question, and nobody ports the bubble
   literature's resolution machinery (below) to ghosts.
3. Frame individuation as a sample-space statement — precedented for
   BUBBLES (Garriga–Kanno–Tanaka 1304.6681: detectors individuate
   the nucleation frame), never applied to ghosts; supported by the
   ghost-condensate mechanism (healthy precisely because the
   background selects a frame).
4. First contact of the stochastic–quantum correspondence with QFT:
   Barandes' corpus is finite-configuration-space throughout and
   explicitly defers infinite ones.

### The decisive map (GSTZ section 5, at equation level)

GSTZ's ladder: classical mechanics = metastable (Nekhoroshev/KAM
"spontaneous lockdown", exponentially long); QM = metastable
(ground-like state, exponentially small outgoing flux, "analogously
to usual tunnelling"); CLASSICAL field theory = NOT metastable
(resonances destroy the hidden invariants; no thermal equilibrium —
ghost temperature T₂<0, entropy grows forever; drift ∝ λ²,
polynomial, lattice-verified); QFT = OPEN: "we do not know the true
rate." Their hoped-for resolution: the V-instability precedent —
Zeldovich/Kobzarev–Okun–Voloshin found the SAME divergent boost
integral for ordinary vacuum decay; Coleman (and Garriga–Shlaer–
Vilenkin) resolved it by expanding around the Lorentz-invariant
bounce, the boost integral being "an over-counting of the same
configuration" (redundancy!). For ghosts, no positive Euclidean
action → no bounce formulation found → question mark in their title
is genuine. They never advocate a preferred frame.

### The bubble-literature precedent (the strongest structural prior)

Kobzarev–Okun–Voloshin (1975) → Coleman (O(4) bounce: boost orbit =
stabilizer of the saddle, not moduli) → Dvali 1109.3422 (revival) →
Dine–Draper–Park 1206.5880 (boosted bubble = DIFFERENT process but
amplitude-suppressed like exp(−(ΔE³/S₁)^{1/2}) → sum converges) →
Garriga–Kanno–Tanaka 1304.6681 (detector individuates the frame).
**The sharp new statement available to us: both bubble resolutions —
saddle symmetry and excitation cost — are structurally ABSENT for
perturbative ghost pair creation, where boost-orbit members are
exactly degenerate in |M|. That absence is what makes the ghost
divergence resistant, and is exactly why the sample-space question
(which configurations are distinct beables) is forced.**

### Other load-bearing reads

- Garriga–Vilenkin 1202.1239 (closest metastable-side precedent):
  D=2 Lorentz-invariant rate FINITE, log-growing in time — matches
  our d=1 reduced integral (slope 0) + causally-capped orbit
  (η_max ~ ln t). In D>2: divergent for point vertices, tamed by
  UV-soft NONLOCAL form factors. They accept multiplicity (boost
  integral = real phase space) and tame |M| instead. [To verify at
  equation level before citing: how an invariant form factor
  interacts with the orbit volume — likely via the same causal
  regulator.]
- CJM details: process is vacuum → 2 ghosts + 2 photons via ONE
  virtual graviton; |M|² effectively s²/M_Pl⁴; Λ ≲ 3 MeV from EGRET
  diffuse gamma flux (Eqs. 4–8); "Lorentz-invariant cutoff fails"
  argument = cutting s leaves the boost integral divergent (their
  words); they DEBUNK CHT's specific φ→gφφ process (vertex removable
  by field redefinition; CHT's 10⁻³ eV bound "incorrect") — cite CHT
  qualitatively only.
- Deffayet–Held–Mukohyama–Vikman 2504.11437 (2025): classical 1+1d
  ghost fields can be benign; high-frequency modes MORE stable
  ("heavy high-frequency ghost fields seem to not violate the
  decoupling theorem") — independent support for our E4 UV
  suppression. Held 2509.18049: global stability results.
- GSTZ sec. 4 vs our E4: their thermal classical drift ∝ λ²T₁T₂(...)
  is the THERMAL regime; our E4 is vacuum-mimic amplitudes — E4
  should be positioned as the zero-point analogue, with their
  lattice-verified Boltzmann drift as the calibrated thermal limit.
- Also for paper #2's related-work section: Hawking–Hertog
  hep-th/0107088 (definition-level rescue — same CATEGORY as
  Mannheim's, exits the state space); Könnig et al. 1605.08757
  (heavy ghosts decay slowly even with trans-Planckian cutoff);
  ghost condensate hep-th/0312099 (frame-selection as cure);
  Babichev 2412.20093 (ghost decay = Cherenkov, manifestly
  frame-anchored); Buoninfante 2606.18349 (ghosts vs unstable
  particles: whether "decay" is even the word); Gomes 2605.21689
  (Lindblad-dissipative ghost stabilization — nearest THEMATIC
  neighbor to a stochastic framing, no explosion mathematics);
  Andreassen–Farhi–Frost–Schwartz 1604.06090 (modern Γ/V
  derivation); Kaplan–Sundrum hep-th/0505265; Rubakov
  hep-th/0604153.

### PRECISION FIXES (referee-hardening, soft spots 2 and 4)

**Fix A — the instantaneous-state statement, probabilist-proof form.**
Overstated version (retire it): "q = ∞ ⇒ no Markov process exists."
Correct version: a state with infinite total exit rate is
*instantaneous*; chains with instantaneous states exist (Kolmogorov's
and Blackwell's examples) but are non-standard — no STABLE, standard,
right-continuous realization. For the regulated family with cutoff Λ,
q_vac(Λ) < ∞ and the minimal semigroup exists; as Λ → ∞ the vacuum
survival probability e^{−q_vac(Λ)t} → 0 for every t > 0: **the
minimal object degenerates to instantaneous killing — the process
exists in the limit only as "the vacuum has zero lifetime."** This is
the sharp statement: not nonexistence, but a zero-lifetime beable
state, with the regulator (= frame) the only thing standing between
the theory and that limit.

**Fix B — two distinct pathologies, kept separate.** (i) LADDER
EXPLOSION: exit rates finite everywhere but growing with occupation,
Σ1/λ_n < ∞ — infinitely many jumps accumulate in finite NONZERO time
(the paper-#1 malicious class; E1/E2). (ii) INSTANTANEITY: infinite
exit rate AT the vacuum itself, from summing finitely-contributing
channels over a non-compact orbit — zero lifetime, t* = 0⁺ (the
Lorentz-invariant QFT ghost, on the multiplicity horn). Both are
failures of conservativity, but (i) is a tail phenomenon in
configuration space while (ii) is a local divergence of the Q-matrix;
paper #2 must not let readers conflate them. The QM→QFT passage is:
malicious QM ghosts realize (i); Lorentz-invariant coupled QFT ghosts
threaten (ii); cutoff-regulated QFT ghosts sit between (transient or
explosive by the ladder criterion, with q_vac(Λ) finite).

**Fix C — Born–Markov scope (soft spot 3, the physicist's
objection).** The jump process is DERIVED from the golden rule; the
instantaneity diagnosis is a translation of the divergent
perturbative rate, inheriting its validity and its doubts (GSTZ: "we
do not know the true rate"). The framework's contribution is that the
translation exposes the disputed assumption — whether boost-orbit
members are distinct outcomes — as a statement about the sample
space, not that it independently settles the rate. State this
verbatim-ish in paper #2.

**Fix D — bubble-contrast scope (soft spot 7).** The degeneracy of
orbit members in |M| is a TREE-LEVEL statement. Whether resummation
generates a Dine–Draper–Park-style suppression for ghost pairs is
open — indeed that unknown IS GSTZ's open question restated. Claim
the absence of the bubble mechanisms only at the order computed.

### Paper #2 thesis, sharpened by the read

The ghost QFT question GSTZ left open ("we do not know the true
rate") is, in the stochastic currency, the question of the sample
space: beables = frame-anchored momentum configurations ⇒ the boost
orbit is channel multiplicity ⇒ q_vac = ∞ ⇒ instantaneous state (no
process; CJM's cutoff = the frame that restores one); beables =
boost-equivalence classes ⇒ redundancy ⇒ rate = the reduced integral
(GSTZ's hoped-for Coleman-analogue; UV-finite in d=1 per our slope-0
result and Garriga–Vilenkin's D=2 finiteness). The bubble literature
resolved the same dichotomy toward redundancy USING structures
(Euclidean saddle symmetry, excitation cost) that ghosts lack — so
for ghosts the dichotomy is not a calculation error but a genuine
ontological fork, which is precisely what a beables-first
reformulation is equipped to say. Barandes-side novelty: first
infinite-configuration-space / QFT contact for the correspondence.

---

## 2026-07-11 — THE FOLIATION THREAD (QFT bridge, stage 4 theory)

Soft spot 5 developed. The pieces assemble into the sharpest
statement of the program so far.

**F1 (structural).** A beables-first QFT needs configurations, and
field configurations (or mode occupations) live on SPATIAL SLICES:
choosing the configuration space is choosing a foliation. This is
not a defect peculiar to us — it is the well-known structure of
Bohmian QFT (hypersurface Bohm–Dirac models), and Barandes' own
corpus stays on finite configuration spaces, deferring exactly this
question. So the natural extension of the correspondence to QFT is
foliation-anchored BY CONSTRUCTION, and the B4 dichotomy is answered
structurally within it: relative to its own foliation, boost-orbit
members are distinct configurations — the MULTIPLICITY horn.

**F2 (the equilibrium shield, and where it fails).** Bohmian lore:
the preferred foliation is empirically invisible in quantum
equilibrium (no-signaling); statistical predictions stay Lorentz
invariant though the ontology is not. Our result says exactly where
this shield BREAKS: a coupled ghost sector makes the foliation
OBSERVABLE, because q_vac — and the decay spectrum, isotropic
precisely in the preferred frame, peaked at the cutoff Λ measured in
that frame — depends on the channel individuation. **Ghosts are
foliation detectors.** For healthy sectors the foliation hides; for
ghost sectors it prints itself on a gamma-ray spectrum (CJM's
EGRET bound is literally this measurement, null so far).

**F3 (the vacuum determines no foliation — instantaneity as
foliation-indeterminacy).** DGNSZ (arXiv:1307.1714, Proc. R. Soc. A
2014) propose extracting the foliation covariantly FROM the wave
function — no absolute structure. Apply it here: the Minkowski
vacuum is Lorentz-invariant, so it determines NO foliation. For a
ghost-coupled theory in pure Minkowski, the beables-first process is
therefore ill-posed in a precise dynamical sense — our zero-lifetime
/ instantaneous-killing statement is the DYNAMICAL EXPRESSION of the
foliation's indeterminacy on a Lorentz-invariant state. The
mathematical pathology and the ontological indeterminacy are the
same fact in two languages.

**F4 (the real universe supplies the foliation — CJM's frame choice
is canonical, not ad hoc).** The actual cosmological quantum state
is NOT the Minkowski vacuum: it has a rest frame (the comoving/CMB
frame), so the DGNSZ extraction succeeds and yields the comoving
foliation. Consequence: CJM's decision to impose the cutoff in the
CMB frame — presented by them as a pragmatic choice — is exactly
what a wave-function-determined-foliation beables theory PRESCRIBES.
In this reading: ghost decay in our universe is well-posed, frame =
comoving, rate finite for finite Λ, and the phantom phenomenology
(isotropy of the would-be gamma-ray signal in the CMB frame; a
dipole matching the CMB dipole from any moving detector) is a
direct empirical probe of the preferred foliation. If DESI-era
w < −1 were confirmed AND the CJM signal ever seen with the CMB
dipole — that would be a foliation detection.

**F5 (the pick-two trilemma — the slogan-grade statement).**
  GHOSTS, LORENTZ INVARIANCE, DEFINITE CONFIGURATIONS: PICK TWO.
- ghosts + beables ⇒ preferred foliation (ghost condensate, Hořava,
  CJM's cutoff frame — all existing rescues in fact pick frames);
- Lorentz + beables ⇒ no coupled ghosts (healthy QFT; the foliation
  exists ontologically but hides at equilibrium);
- ghosts + Lorentz ⇒ no beables (Mannheim/PT, Hawking–Hertog:
  definition-level rescues that exit the sample space — the paper-#1
  verdict, now seen as one horn of a three-way trade).
This upgrades paper #1's trilemma from a menu of completions to a
statement about what any ontology of QFT can simultaneously hold.

**Honesty flags (must appear in any writeup).** (a) F1 states the
NATURAL extension of Barandes' framework, not his committed
position — he explicitly defers infinite configuration spaces; other
extensions (e.g., genuinely covariant beables, if constructible)
would evade F1. (b) The equilibrium-shield leg (F2) is imported from
Bohmian analysis; its transfer to indivisible-process dynamics needs
its own proof. (c) F3/F4 apply DGNSZ's extraction idea in a context
they never considered. (d) All of F2–F4 presume the multiplicity
horn, which the beables framing motivates but which fundamental
frameworks without beables can still dispute (GSTZ's hoped-for
bounce). The trilemma F5 is robust to (d): it is a statement about
combinations, not about which is true.

**Next concrete steps for this thread:** (i) check whether the
equilibrium shield (F2) can be proven within the correspondence
(does no-signaling of the indivisible process protect foliation
invisibility for conservative sectors?); (ii) the dipole
phenomenology of F4 (one paragraph of kinematics — decay products
isotropic in the comoving frame, detector moving at 370 km/s sees a
computable dipole); (iii) position against Kawabata–Ashida–Ueda-type
information results if any apply.

---

## 2026-07-11 — GARRIGA–VILENKIN DEEP READ: soft spot 1 RESOLVED;
## the foliation thread gains its third leg

Full equation-level read of 1202.1239 (+ companion GSV 1109.3422).
Classification of their D>2 rescue against our (a)–(e) menu:
**(a) finite-vacuum-age orbit cutoff, with (d) as the phenomenology
step; explicitly NOT frame-dependent form factors, NOT a different
observable.** Details:

1. **They CONFIRM our premise.** Their own Secs. II–III prove a
   Lorentz-invariant form factor cannot cut the orbit: local vertex
   in D=4 diverges linearly in |P| EVEN AT FINITE T (the energy
   defect Ω → 0 along the orbit, so the time window "provides no
   suppression there"); a single-invariant form factor tames the
   orbit only via the T-window, and then the invariant-mass
   integrals blow up instead (their surprise: "energy is not
   conserved because the interaction is switched on and off").
   Full rescue needs BOTH: (i) the vacuum's finite age — creation
   on a spacelike surface Σ, Gaussian window e^{−x₀²/T²}, "this
   surface breaks Lorentz invariance spontaneously" — cutting the
   orbit at P_max ~ μ²t; AND (ii) full LI nonlocality in all SIX
   vertex invariants, which collimates the decay products
   (θ ≲ μ/p_*) and bounds the invariant masses. Result: Γ_total(t)
   ~ 10⁻⁶(μ⁸/M_Pl⁴)(μt)² — finite at every t, GROWING as t²
   (D=2 analog: ln(mT)). "Metastable" = born-and-aging, never a
   constant rate. They explicitly fault CJM for missing the
   essential role of nonlocality, and Kaplan–Sundrum's
   invariant-softening for the s,s′ runaway.

2. **The literature's own criterion for multiplicity vs redundancy**
   (GV footnote 5 + GSV 1109.3422): the boost integral is an
   OVERCOUNTING precisely when the final state is a boost SINGLET —
   the fluctuation-dressed bubble state is boost-invariant, so
   boosts map it to itself (GSV's answer to Dvali, with Schwinger
   pair creation as the controlled prototype). Non-invariant
   perturbative multiparticle finals (ghost + matter with definite
   P) are genuinely distinct channels; the orbit volume is real,
   and only the vacuum's age regulates it. **So the B4 dichotomy is
   not a global ontology switch — the literature resolves it
   state-by-state via the invariance of the final state, and
   perturbative ghost decay sits on the multiplicity side by this
   criterion.** Our beables framing agrees and explains WHY
   (configurations are frame-anchored); the open GSTZ hope is
   equivalent to finding a boost-singlet saddle for ghost decay.

3. **Fix A, refined (the sharpest form of the instantaneity
   statement):** q_vac is infinite only for the ETERNAL
   Lorentz-invariant vacuum. A vacuum with a birth surface Σ has
   finite, growing exit rate (GV's (μt)²; survival
   S(t) = exp(−V∫Γdt) finite for all finite t). **"A
   Lorentz-invariant ghost vacuum can exist only if it was born —
   and its birth certificate is a foliation."** The instantaneous
   state is the eternal-vacuum idealization, exactly the state
   that (F3) determines no foliation.

4. **Foliation thread, third leg (F4').** Every rescue on record
   supplies a frame/foliation somewhere: CJM — CMB-frame momentum
   cutoff; ghost condensate — the condensate background; Hořava —
   explicit; **GV — the creation surface Σ, doing its work through
   "spontaneous" Lorentz breaking by the vacuum's own history.**
   The pick-two trilemma survives every known example: ghosts +
   beables/calculability ⇒ a foliation enters (as cutoff frame or
   birth surface); ghosts + Lorentz ⇒ exit the sample space;
   Lorentz + beables ⇒ no coupled ghosts.

5. Technical notes for paper #2: GV's loop remark (the orbit
   divergence lives in external momenta only — vacuum-energy loops
   cut at μ, so Λ ~ μ⁴ survives); their allowed window μ ≈
   2×10⁻³ eV (gamma-ray cascade bound vs 0.1 mm gravity tests,
   "marginally consistent"); their P_max ~ μ²T dominance in the
   fully nonlocal model is an ESTIMATE, rigorous only in the
   restricted model — flag if we lean on it. Novelty intact: no
   Fock/rate-equation/Markov treatment of the vacuum anywhere in
   GV or GSV.

---

## 2026-07-11 — M3 RUN: who individuates the frame — RESULT:
## a two-epoch structure (state first, regulator ultimately)

Code: `foliation_m3.py` (+ scratch diagnostics). Design: boosted
thermal baths (classical Jüttner n(k)=T/(u·k), traveling-wave
construction so the φ–π correlation carries direction; fixed spectral
support |k| ≤ 1.2 so the STATE is N-independent), ghost bath hotter
(T_χ=2, T_φ=1; GSTZ drift ∝ T₁T₂(T₂−T₁) vanishes at equal T), frame
estimator v* = (dP_φ/dt)/(dE_φ/dt) by regression (kinematic identity:
production isotropic in the state frame ⇒ v* = v exactly,
mass-independent; lattice-anchored ⇒ v* = 0). Self-test: right-mover
P/E = k/ω ✓. Controls: λ=0 → dE/dt = 0.00000 ✓; v=0 → v* ≈ 0 ✓.

**Run 1 (v=0.35, full window to back-reaction guard):** v*(N) =
0.045 / −0.001 / −0.031 / −0.036 for N = 16/32/64/128 (IQR ~ ±0.15)
— consistent with ZERO at every cutoff, rejecting the naive
state-anchored 0.35.

**Run 2 (spectral diagnosis, N=64, t=80 deep cascade):** the
transferred energy is UV-DIRECTED: fractions 0.10 / 0.27 / 0.57 /
0.05 in bands |k|≤1.3 / 1.3–3 / 3–6 / >6 — the classical ghost
cascade (GSTZ sec. 4 turbulence) pumps energy far above the bath
support; and EVERY band shows v*_band ≈ 0 ± 0.1: deep in the
cascade, the state's frame is erased. Even at N=128 the
energy-carrying band sits where lattice dispersion is ~15%
non-covariant: the cascade always terminates in regulator-owned
territory.

**Run 3 (decisive early-window test, v=0.6, t ∈ [3,25]):**
v* = +0.022 [−0.18, +0.22] at N=64 → **+0.230 [−0.01, +0.45] at
N=128** — the EARLY transfer carries the state's frame, more
faithfully as the lattice recedes (bath streaming P/E ≈ 0.2 for
these massive quanta; isotropic-in-state-frame target 0.6; the
measured value sits in that band at N=128 and nowhere near it at
N=64).

### Interpretation (the M3 theorem-shape)

**Two epochs. Early, covariant epoch: the state individuates — the
transfer is comoving with the bath, and better so as the cutoff
recedes (foliation-from-state confirmed where the dynamics is
continuum-covariant). Late, cascade epoch: ghost dynamics is
UV-seeking, the energy runs to the regulator's territory, and the
state's frame is erased — the regulator individuates.** Whoever owns
the UV ultimately owns the frame. This is precisely the dynamical
content of Garriga–Vilenkin's requirement: without UV-softness
(their nonlocality) the state/age frame cannot hold the line against
the cascade; UV-soft couplings are what let the state's frame
survive its own ghost. Our lattice model exhibits the REASON for
their condition. For the foliation thread: F4 ("the cosmological
state picks the frame") holds in the covariant window but is NOT
sufficient in a UV-local theory — the honest statement is
conditional: state-individuation survives iff the ghost coupling is
UV-soft below the scale where the regulator's frame takes over.

### Caveats

Classical 1+1D, one coupling; wide IQRs (16 runs); N=256
unconfirmed (trend N=64→128 is one step); early-window target band
[bath P/E ≈ 0.2, isotropic 0.6] not sharply discriminated within
noise; the two-epoch reading rests on Run 2's spectral bands plus
Run 3's trend — a dedicated scan (v*, band-resolved, vs time and N)
would firm it. Vacuum runs are impossible in principle (the vacuum
cannot be boosted) — which is F3 in experimental form.

---

## 2026-07-11 — E4-2D: THE DIMENSIONAL REVERSAL, CONFIRMED — after
## two caught artifacts and one formal RETRACTION

Code: `qft_bridge_e4_2d.py` (identical leapfrog machinery in d=1 and
d=2; pre-registered prediction in the docstring BEFORE the data:
d=1 flat/suppressed, d=2 growing — the marginal dimension of the
reduced measure ∫dE E^{3d−6}).

### RETRACTION: the E4-1D "UV-suppression" result was an artifact.

The original E4 vacuum construction (`qft_bridge_stage2.py`,
`vacuum_field`) underweights fine lattices: mode amplitudes were
N^{d}/(2ω)-normalized instead of N^{2d}/(2ω L^d), an error of
(N/L)^{d/2} — the zero-point source SHRANK as the cutoff grew, and
the observed "suppression" (t_thr 46→149 at N=32→64, "confirmed"
with independent seed) was the shrinking source, not physics.
Diagnosed by the ⟨φ²⟩₀ column of the new script (fell with N; the
physical vacuum variance must rise — log in d=1, linear in d=2);
verified by the zp≈1.00 self-check after the fix.
**Scope of contamination:** stage-2 E4's verdict ("classical
cascade UV-finite, even UV-suppressed") — RETRACTED, replaced
below; the "self-consistent mass-detuning" conjecture — retracted;
stage-3 "Corollary 2 (E4 coherence)" — superseded (the corrected
d=1 result is coherent with the slope-0 reduced measure via
SATURATION, see below). **Unaffected:** E1–E3 (no field
construction), all of stage 3's phase-space numerics, M3 entirely
(its thermal bath used the explicit per-mode loop, correctly
normalized), and everything in paper #1.
Second artifact caught in the same sweep: at dt·ω_max = 0.5 the
Verlet drift (up to 21 energy units) exceeded the d=2 threshold and
made the λ=0 CONTROL fire at N≥48 — fixed with dt·ω_max ≤ 0.15;
final run has all controls silent and max drift 1.0 vs thresholds
10/25. Methods lesson, banked: the ⟨φ²⟩₀ column caught bug 1, the
λ=0 control column caught bug 2; each alone would have produced a
publishable-looking false trend.

### RESULT (corrected, controls clean)

Classical ghost vacuum decay rate (1/median t_thr to absorb fixed
ΔE) vs UV cutoff k_max = πN/L at fixed volume, vacuum-mimic data:

d=1 (L=32, λ=0.25, ΔE=25):  N=16..128 → rate 0.0127 / 0.0175 /
  0.0242 / 0.0249 — rising then SATURATING (64→128: +3%): the
  classical decay has a CONTINUUM LIMIT in 1+1d. Consistent with
  the UV-convergent d=1 reduced measure (stage-3 slope 0) and with
  Garriga–Vilenkin's finite D=2 rate.
d=2 (L=16, λ=0.1, ΔE=10):  N=16..64 → rate 0.0205 / 0.1034 /
  0.2712 / 0.8186 — ×40 over ×4 in cutoff, effective power
  k_max^{~2.7}, NO saturation: no continuum limit. THE REVERSAL,
  in the pre-registered direction.

Exponent honesty: the naive channel-counting prediction at the
marginal dimension is log growth; the observed ~k_max^{2.7} is
steeper because the zero-point amplitudes themselves grow with the
cutoff in d≥2 (⟨φ²⟩₀ ∝ k_max: 0.243→1.205 across the sweep),
enhancing the effective vertex — a classical-statistical effect on
top of the phase-space counting. Decomposing the exponent
(amplitude² ~ k_max² × residual log?) is a clean follow-up; the
DIRECTION of the dichotomy (saturation vs unbounded growth) is the
claim, and it is unambiguous.

### Upshot

The dimension ladder is now DYNAMICAL, not just kinematic:
1+1d classical ghost decay converges to a finite continuum rate;
2+1d grows without bound as the regulator recedes — the classical
field theory tracks the reduced-measure dichotomy across its
critical dimension. This patches the "everything numerical was
d=1" vulnerability, replaces a wrong result with a stronger correct
one, and sharpens the M3/GV story: in d=1 the state's frame has a
covariant window because the UV is tame; in d≥2 the UV owns the
dynamics outright — UV-softness (GV nonlocality) is not optional
garnish but the price of any state-anchored frame in the physical
dimension.
[SUPERSEDED IN PART by the decomposition below: the dichotomy is
real but its mechanism is the TADPOLE ladder, not the channel
ladder.]

---

## 2026-07-11 — EXPONENT DECOMPOSITION: the reversal is
## SOURCE-DRIVEN; classical lattices probe the tadpole ladder,
## not the channel ladder

Code: `qft_bridge_decomp.py`. Two runs, all λ=0 controls silent.

**Run 1 (source fixed by spectral truncation |k| ≤ K_C; channels
swept via N).** The purified channel factor is FLAT in both
dimensions: d=2 rates 0.0317/0.0278/0.0229/0.0253 over k_max
3.14→12.57 (power exponent −0.20; even the log fit is weak,
R²=0.80 with the wrong trend); d=1: 0.0222/0.0374/0.0392/0.0281
(exponent +0.11, noise). If the golden-rule channel-log applied
classically, d=2 should have grown ×2.2 across this sweep; it did
not. **The entire ×40 growth of the full d=2 experiment was
source-driven.**

**Run 2 (channels fixed at one N; source amplitude scaled by a).**
rate ∝ a^{+4.96} (d=2, N=32) and a^{+4.45} (d=1, N=64) vs the
perturbative prediction a⁴ — consistent with rate ∝ variance², the
mild excess plausibly from approach to the parametric-instability
threshold at large a (noted, not pursued).

**Reconstruction closes:** full d=2 experiment had ⟨φ²⟩₀ ∝
k_max^{1.16} (measured); rate ∝ variance^{2.48} (Run 2) gives
k_max^{2.9}, vs the observed k_max^{2.7}. ✓ Within fit noise, the
exponent is fully accounted: ~2.7 = (source)^{~2.5×1.16} +
(channels)^{~0}.

### The corrected interpretation (important for paper #2)

There are TWO dimension ladders, and the classical experiment
measures the other one:
- **Tadpole ladder** (source): the zero-point variance
  ⟨φ²⟩ = ∫d^dk/(2ω(2π)^d) diverges as k_max^{d−1} — log at d=1,
  LINEAR at d=2. This is what the classical-statistical lattice
  tracks (Runs 1+2 prove it), and it is the true mechanism of the
  E4-2D continuum-limit dichotomy (still a real dichotomy: d=1
  converges because the tadpole is log; d≥2 has no continuum limit
  because the tadpole is power-divergent).
- **Channel ladder** (golden rule): the reduced decay measure
  ∫dE E^{3d−6} — convergent d=1, marginal-log d=2 — plus the
  always-infinite boost orbit. This is the CJM/GSTZ object. The
  classical dynamics does NOT track it (Run 1 flat), for a clean
  reason: classical fields cannot spontaneously radiate into EMPTY
  modes — spontaneous emission into unoccupied channels is
  intrinsically quantum, and the classical cascade populates high-k
  only by local-in-k flux, insensitive to where the far cutoff
  sits. The known classical-statistical limitation (vacuum
  overcounting/undercounting of spontaneous processes), here
  measured rather than assumed.

Consequences: (i) the "hotter start" objection to E4-2D is
CONCEDED and quantified — and conceding it yields the sharper true
statement above; (ii) numerical support for the channel ladder
rests on the quantum channel toy (stage-2 E3) and the phase-space
integrals (stage 3), NOT on lattice dynamics — paper #2 must say
so; (iii) methods claim for the paper: classical-statistical
vacuum simulations are tadpole-ladder probes; channel-ladder
questions require quantum treatment. (iv) The M3/GV framing
survives unchanged — M3 used thermal (occupied) states where
classical stimulated dynamics is the right physics.

### Caveats

Run-1 flatness is bounded by ensemble noise (±~20%): a channel-log
as large as ~×1.3 across the sweep is not excluded, only the ×2.2
naive prediction; Run-2 exponents carry the threshold-proximity
systematic; K_C truncation leaves nonlinearly-generated support
growth unquantified (the local-cascade reading is an
interpretation, standard in wave turbulence but not proven here).

---

## 2026-07-11 — S1: THE NO-SIGNALING STRESS TEST — all four
## treatments as predicted; NEW COROLLARY (the LHFL signal in
## closed form)

Code: `s1_no_signaling.py` (seconds). Context: Lee–Hsieh–Flammia–
Lee, PRL 112, 130404 (2014) — local PT evolution on one arm of an
entangled pair, treated as fundamental, permits superluminal
signaling. Our framework predicts exactly where the signal lives.
Setup: Bell pair; Alice's message = loss orientation (site 1 vs
site 2 of the dimer); signal = TV distance between Bob's marginals.

**(i) Metric-corrected closed dynamics: NO SIGNAL — max TV
1.7e-16** over t ∈ [0.2,8] (deflation: PT = Hermitian partner's
unitary; local unitaries cannot signal).
**(ii) Dilated open dynamics, no post-selection: NO SIGNAL — max
TV 4.4e-16** (Halmos unitarity 2.6e-15). This was the framework's
kill-shot test: any leak here would falsify paper 1's dilation
story. It is clean.
**(iii) Survival-conditioned (broken phase): the signal appears,
with closed-form magnitude** — verified to 2.2e-16 against

    TV(t) = |p²−q²| / (p²+q²+2r²),   p,q,r as in the
    terminal-indivisibility theorem;  TV(∞) = κ̃/sinθ
           = sqrt(1 − (s/sinθ)²).

Numerics: asymptote 0.707107 hit to 6 digits at t=16 (s=0.5,
θ=π/4); s-sweep at t=25 matches κ̃/sinθ to 6 digits away from the
EP (0.959166, 0.824621, 0.529150 at s=0.2/0.4/0.6; residuals at
s≥0.7 are finite-t, κ̃t ≲ 1.4). TV is non-monotonic: peaks ~0.797
near t≈1 before settling to the asymptote. **NEW COROLLARY of the
terminal-indivisibility theorem: the conditioning ("LHFL") signal
strength of a broken-PT local operation is κ̃/sinθ — zero at the
exceptional point, → 1 deep in the broken phase.**
**(iv) Unbroken PT + conditioning (the actual LHFL construction):
signal present (max TV 0.5774 ≈ 1/√3) under conditioning, ZERO
under treatment (i) with the SAME Hamiltonians.**

### Interpretation (paper-2 FTL section, ready)

The "faster-than-light" capability of local PT operations is
located exactly: it lives in the CONDITIONING — treating the
sub-stochastic (survival-renormalized) process as the whole sample
space — and nowhere else. The closed and dilated dynamics are
no-signaling to machine precision. And the conditioned "signal" is
not operational FTL: constructing the post-selected ensemble
requires Alice-side survival information, which travels
classically; Bob alone cannot filter. So the stochastic currency
resolves the LHFL controversy constructively: same Hamiltonians,
three bookkeepings, signal in precisely one of them, with its
magnitude now a theorem. Connects to the paper-1 theme (the broken
phase is survival-conditioned dynamics) and the paper-2 theme (the
pathology enters through the choice of sample space).

---

## 2026-07-11 — S3: FOLIATION DETERMINACY CURVE (F3 quantitative)

Code: `s3_foliation_determinacy.py` (~1 min; 400 realizations per
point). Construction: 1D lattice ensembles = frame-symmetric
zero-point part (n=1/2 per mode, split ±k — the classical mimic of
the boost-invariant vacuum) + boosted thermal part n_th = T/(u·k)
at v=0.35; frame extraction v̂ = P/E per realization (the 1D
timelike-eigenframe estimator of ⟨T^μν⟩).

Result — the determinacy curve:
  T=0 (vacuum): mean v̂ = 0.0013, scatter 0.121, SNR ≈ 0 — the
  extracted foliation is PURE NOISE; T=0.01: mean −0.012 (wrong
  sign, SNR 1.8 — indeterminacy regime made vivid); T=0.1: 0.024
  (SNR 4); T=1: 0.150 (SNR 34); T=3: 0.219 (SNR 51), tracking the
  thermal (frame-carrying) energy share (0.012 → 0.79) toward the
  massive-bath streaming velocity.

**F3 upgraded from algebra (⟨T^μν⟩ ∝ η^μν has no eigenframe) to a
measured, continuous determinacy curve: the foliation information
content of a state vanishes smoothly at the vacuum.** Ties to F4:
any real cosmological state (thermal share > 0) sits at finite SNR
— the comoving frame is extractable in practice, not just in
principle. Caveat: classical amplitude statistics (exponential/
chaotic-light per mode); a quantum treatment would replace scatter
with quantum estimation bounds — the shape, not the scale, is the
claim.

---

## 2026-07-11 — S2: THE INFINITY-CHANNEL PROTOCOL — all four
## pre-registered predictions confirmed

Code: `s2_infinity_channel.py`. Alice gates the right exit of
V = −x⁴ (explosive) or V = −x² (marginal) with a barrier (her bit);
Bob is a direction-resolved current detector at x = −L+3 (triggers
only on flux ENTERING from the left boundary = arrivals from
infinity); completions: periodic identification (the conservative
"wormhole" of paper-1 V5) vs absorbing layers (the minimal
process). Separation swept L = 6..12 (L=6 flagged: Alice's station
overlaps the launch packet — broken geometry, excluded).

Final table (norm_end certifies the mechanism):
- **Explosive + wormhole: a working one-bit channel through
  infinity with DISTANCE-INDEPENDENT latency.** bit=0: t_B =
  0.179/0.150/0.160 at L = 8/10/12 (flat within the 0.01 timing
  resolution); bit=1: silence (Jmax ≤ 1e-5). Unitary throughout
  (norm 1.000). Latency saturation = the dictionary's finite
  time of flight; measured earlier than the rest-start classical
  round trip (0.43→0.36) via packet momentum tails — the same
  documented effect as paper-1 V4.
- **Explosive + minimal: TOTAL SILENCE at every L and both bits
  (Jmax ≤ 3e-5), norm_end = 0.000** — all mass genuinely lost to
  infinity. Causality by mass loss, exactly as claimed.
- **Marginal + wormhole: the channel exists but its latency GROWS
  with separation** (t_B = 0.940/1.020/1.100 at L = 8/10/12,
  monotonic): no distance-independent channel at or below the
  dictionary's boundary.
- **Marginal + minimal: silence, norm 0.000.**

**"Causality selects the minimal process" is now a table:** the
same interior Hamiltonian either contains a distance-independent
bit channel through infinity (conservative completion, explosive
class — the operationally acausal choice), a distance-penalized
one (marginal class), or none (minimal process). The completion —
regulator data, not physics in H — decides. The explosion
dictionary's time-of-flight integral is measurable as the flat vs
rising latency curve.

Methods note (third caught artifact of the day): the first runs'
timestep was throttled by k_max²/2 — a leapfrog stability criterion
that split-step FFT does not have (its kinetic factor is exact);
fixing dt = 0.3/V_max cut the runtime ~400× for the marginal runs
with identical physics. Earlier CAP-strength leak (absorbing rows
false-triggering at small L) fixed by class-dependent η₀; the
norm_end = 0.000 column now certifies absorption.

## 2026-07-11 — S4b: HORN-3 SILENCE — the decision matrix's column
## discriminant, in the exactly solvable toy

Code: `s4b_horn3_silence.py`. One classical two-mode model
(resonant, coupling g=0.15), three quantizations, the vacuum's fate:
- GHOST (horn 1): ⟨n₁⟩ = sinh²(gt) to 5 decimals (max dev 3.8e-2 at
  ⟨n⟩=8.7, truncation tail) — the decay signal;
- REQUANTIZED (horn 3, Bender–Mannheim sign reassignment; at
  quadratic level pair creation → excitation exchange):
  ⟨n₁⟩ = 0.00e+00 at every t — EXACT silence, vacuum an eigenstate;
- NORMAL TWIN (control): bounded virtual pairs ≤ 0.023 ~ (g/2ω)²
  scale, no secular growth.
Stimulated panel (|2,0⟩): ghost 2 → 26.6 (secular cascade); horn-3
bounded Rabi exchange, mean pinned. **Same modes, same coupling
strength, opposite energy-sign assignment: a decay signal exists in
exactly one quantization** — so, given an established phantom field,
an exhaustive null in the decay-signal search discriminates against
definite configurations rather than against sensitivity. Paper-2
decision matrix, right column, now simulation-backed.

## 2026-07-11 — S4c: THE FOLIATION-DETECTION TEMPLATE (dipole +
## edge + detectability)

Code: `s4c_dipole_template.py`. Mock-sky pipeline: source-frame
sampling, exact aberration+Doppler (β = 1.23e-3), estimator
recovery. TWO analytic slips caught by the MC and fixed (observable
definitions matter: all-photon counts/sr = pure aberration 2β;
thresholded counts add β·E_thr/(Λ−E_thr), NOT Λ/(Λ−E_thr)).
Verified: observable (a) 0.00234–0.00248 vs 2β = 0.00246;
observable (b) 0.00305 vs 2.5β = 0.00308 at N = 4e7; edge-shift fit
through 3% Gaussian energy smearing recovers 1.42e-3 vs β = 1.23e-3
at ~10σ (N = 4e6, 99th-percentile regression per sky band).
**PAPER NUMBERS: dipole 2.5–3.1×10⁻³ (flat spectrum, apex fixed by
the CMB dipole); N_5σ ≈ 8×10⁶–1.2×10⁷ SIGNAL photons; edge
modulation 0.12%, recoverable through 3% instrument resolution at
N ~ few×10⁶. The edge, not the dipole, discriminates against
comoving astrophysical backgrounds; dilution N ∝ 1/f_s².**

---

## 2026-07-11 — S4a: THE BOOKS MUST BALANCE (row discriminant)

Code: `s4a_books_balance.py`. Identical lattices, identical
temperatures (T_cold=1 normal + T_hot=2 partner), identical
|coupling| λ=0.25 — only the partner's energy sign differs:
- HEALTHY partner: ΔE_φ rises and SATURATES at 7.37 ± 1.00 for
  t ∈ [150,300] (equipartition scale) — detailed balance has a
  fixed point;
- GHOST partner: 2.2 → 22.5 → 283 → 1211 → runaway cap (5×10³) by
  t ≈ 150 (first, uncapped run overflowed float64 — the bottomless
  books, literally); λ=0 control: zero.
**Same setup, sign flip only: equilibration vs unbounded flux — the
dynamical discriminant between a genuine phantom sector and any
healthy mimic of the same background.** Decision-matrix rows now
simulation-backed.

### S4 package complete: the decision matrix is fully
### simulation-backed (S4a rows, S4b columns, S4c top-left priced).

---

## 2026-07-11 — PAPER-2 AUDIT (three agents) + FOURTH ARTIFACT
## (S4c dipole circularity) — all fixes applied

**Bibliography agent:** 31/34 confirmed; GSTZ Eq. 88 and CJM Eq. 9
attributions verified against arXiv LaTeX sources with our quotes
verbatim. Fixed: Valentini arXiv ID (quant-ph/0610195 → correct
hep-th/0610032 — the old ID was an unrelated paper), Cline title
completed, Coleman title/erratum.

**Consistency agent** (re-ran 8 scripts): every number in both
papers traces to notebook/scripts. Two critical self-description
errors fixed: "all thirty-two cells clean" → 24 cells with L=6
excluded (L=6 wormhole bit=1 cells FIRE — barrier overlaps launch
packet); the "two artifacts" sentence misattributed the second
(now correctly the Verlet-drift/control-firing bug; the split-step
dt waste was a third, runtime-only artifact). Minors fixed: drift
margin "two orders"→"an order"; GV 1e-6 prefactor restored; sinh²
five-decimals truncation qualifier; completions table regraded
Measured; cor:frame → Claim (grading consistency); I_s/(2π)²
bookkeeping; LHFL treatment-(iv) 0.577 added to body; 8 orphan
bibitems now engaged in a positioned related-work paragraph;
retraction flags added to qft_bridge_stage2.py (E4 docstring) and
stage3's printed commentary.

**Adversarial agent — CRITICAL, the FOURTH caught artifact:** the
S4c dipole was missing the arrival-rate Doppler factor. The mock
sampled a FIXED photon population (aberration-only, 2β by
construction) and so was CIRCULAR — it "confirmed" analytics that
had been wrongly corrected DOWN to match it; the original 3β was
right (cross-check: CMB photon-number dipole is 3β). Fixed: each
mock photon now carries weight (1+βμ); the reweighted MC verifies
3β (0.00357–0.00371 vs 0.00369) and 3.5β (0.00428–0.00433 vs
0.00430) NON-circularly. **Corrected paper numbers: dipole
3.7–4.3×10⁻³; N_5σ ≈ 4.0–5.5×10⁶ signal photons** (error was
conservative — real signal larger). Lesson appended to the methods
ledger: a mock that shares the analyst's observable definition
cannot catch a definition error; the referee could.

Other adversarial fixes applied: tree-level hypothesis moved INTO
Theorem instantaneity; "redundancy horn" → convergent multiplicity
sum (DDP-style escape ≠ redundancy); instantaneous-state
terminology corrected (stable/right-continuous; Blackwell/Chung
cited; no-return clause); Lemma exactness scoped to power-law
ladders; Feller 1940 added; footnote-5 attribution corrected
(criterion → GSV one-directionally; Dvali fn. 5 anticipates the
born vacuum); (n+1)-vs-n replaces the "classical fields cannot
radiate" slogan, EGW (classical-statistical nonrenormalizability)
cited; ±20% channel-log bound imported; shield claim now carries
"in quantum equilibrium" + Valentini 1991; flash remark downgraded
to conditional ("sharpest open flank"; covariant flash law might
implement redundancy; mass-density ontologies noted); trilemma LI
vertex redefined EMPIRICALLY (fixes horn-2 self-contradiction);
LHFL resolution literature cited (Tang 2016 experiment, Brody 2016,
Ju et al. 2019) and abstract rescoped to "recovering the known
resolution ... with the magnitude now in closed form";
nonrelativistic hedge on "acausal"; "exactly two entry points" →
"the two we identify"; f_s knife-edge quantified (Λ⁸ ⇒ half-bound
costs 6×10⁴ in N) + DGB dipole systematics caveat (arXiv:2401.04564
— authors to be completed in the prior-art sweep).

---

## 2026-07-11 — PRIOR-ART SWEEP (2 agents) + S5 (state divergence)

Sweep 1 (claims): trilemma NOT preempted — but both EDGES are prior
art and now cited (CJM ghosts⇒frame; Hardy 1992 realism⇒frame); the
triangle + "same frame" observation is ours. Foliation
observability: one rival equilibrium route exists — Amblard–Drezet
arXiv:2604.17507 (Bohmian arrival times; contested measurability) —
engaged and distinguished in Claim shield. Flash gap confirmed;
Georgii–Tumulka (Bell-process non-explosion) + Chebotarev–Fagnola
(semigroup conservativity) cited as the mathematical neighbors
whose hypotheses ghosts violate. DGBdipole = Kashlinsky,
Atrio-Barandela & Shrader, ApJL 961, L1 (2024) (fixed);
Kachelrieß–Serpico cited for CG methodology. Combined dipole+edge
prediction: unpreempted (assembled from cited parts).

Sweep 2 (probes): paper-1 Sec. 10 now cites the existing apparatus
— Klauck 2019 (passive PT coupler), Xiao PRL 123, 230401 (2019)
(EP information-flow criticality; differentiated: no t_c/floor/
window extraction), Bernardes 2015 (divisibility classes
measurable), Tang 2016 + Ehrhardt 2022 (entangled-pair tailored
loss). ENCROACHMENT handled: Z₂ skin effect observed 2025–26
(acoustic Adv.Mater.; circuit 2604.00888) — prediction repositioned
as the beable-obstruction observable (irreducible nonreciprocity),
not existence. Falling-potential math anchors (Carreau et al. 1990)
+ inverted-HO BEC platform (2606.05125) + DCE (Wilson 2011) cited;
"spacing saturation" framing confirmed ours. t_c closed form,
generator floor, π/κ windows, √(1−(s/sinθ)²) magnitude: all
unpreempted.

**S5 (`s5_state_divergence.py`): the flash flank CLOSED at tree
level.** d⟨N⟩/dt (particle content — ontology-free) tracks M·Γ₁
within 3% to M=32 (flat measure) vs plateau 0.0640 (decaying):
the divergence lives in the STATE. Remark 6.3 upgraded to
Proposition (state) + Remark (event ontologies inherit the
dichotomy; flank narrows to disputing the tree-level state = GSTZ's
question). Paper 2: 19 pages.

---

## 2026-07-11 — TASK CLOSEOUTS

**w=−1 divide (task 7): DECIDED — mostly a pun, correctly weighted.**
The frame-extractability boundary ρ+p=0 coincides with the phantom
divide only for a SINGLE total fluid. Any realistic universe carries
matter/radiation components whose T^μν retains a timelike eigenframe
throughout a dark-energy w=−1 crossing (quintom crossings are
multi-field anyway), so foliation determinacy is never actually lost
at the divide. The paper's existing one-line mention is the right
weight; no section warranted.

**M3 N=256 (task 5): evidence WEAKENED, honestly downgraded.**
N=256: v* median +0.236 [−0.011, +0.455] (positive, matches
original N=128 seed A); but fresh-seed N=128 gave −0.002 — medians
seed-sensitive at ±0.2 with 16 runs. Paper-2 M3 passage rewritten:
early-window anchoring "suggestive rather than established"; robust
features = spectral bands + late-time erasure. A clean test needs
~100-run ensembles (future work).

**Task 8 (`s2b_dirichlet.py`): taxonomy complete.** Dirichlet walls
(DST split-step, exact hard boundaries): Bob-RIGHT fires at
t_B = 0.230/0.230/0.240 for L = 8/10/12 (distance-independent,
matching the wormhole latency scale — same round trip, opposite
side), Bob-LEFT silent, norm 1.000. Three completions, three
signatures: left (wormhole) / right (walls) / silence (minimal).

**M3 100-RUN SETTLEMENT: early-window anchoring is NULL.**
N=128: mean v* = −0.069 ± 0.106 (z=−0.7); N=256: −0.018 ± 0.30
(z=−0.1); heavy-tailed slope-ratio estimator (SE at N=256 implies
std≈3 — near-zero-denominator outliers). The +0.23/+0.24 medians of
16-run ensembles were flukes. Paper-2 M3 passage rewritten: the
covariant-window anchoring is guaranteed by CONTINUUM COVARIANCE as
a principle but is NOT resolved by the lattice at accessible N;
robust findings = UV-directed cascade + late-time frame absence.
Slogan amended: "the state proposes (by covariance); the UV
disposes (by measurement)." Third replication-driven downgrade of
the session — the notebook's honesty ledger now reads: 5 caught
artifacts, 1 retraction, 2 downgrades.

**Tasks 3+4 (`qft_bridge_closeout.py`): both closed.**
GV log growth: Γ(T) with causal cap arccosh(T√s) grows as ln T with
slope 0.6193 vs I_s = 0.6192 over four decades — GV's D=2 result IS
our factorization, regulated by age. d=3 factorization MC:
Γ/V_orb constant (1244/1207/1259 ± ~3%) with the CORRECT hyperboloid
measure sinh²η dη — fifth caught artifact: the first run's "flat in
H" label transplanted the d=1 orbit measure to d=3; the data was
right, the label wrong. Λ⁴ rung measured: slope 4.33 overall,
4.09 on the 8→16 pair (threshold steepening fades). Also: √s=2
sweep point was below pair threshold (empty window) — sweep now
starts at 4.

**Shield core (task 6): PROVED.** Four-line proposition added to
paper 2: Bob's marginal under arbitrary local dilated dynamics is
exactly U_A-independent (p_B = ⟨Ψ|1⊗U_B†|b⟩⟨b|U_B|Ψ⟩); survival
conditioning breaks precisely the first equality — locating the
LHFL signal by proof, not just simulation. Open Problem rescoped to
the field-theoretic/equilibrium extension + sharpness converse.

## 2026-07-11 — FINAL FOUR-AGENT PASS: CLOSED

Prior-art reconfirmation: no preemption of headline claims 2-5;
shield core's unitary case published by Barandes-Hasan-Kagan
(2512.18105, Dec 2025) — cited, ours scoped as the dilation +
conditioning-breakpoint extension. Nine citations added (BHK, DESI
DR2 + review + skeptic, Ovdat, Dubovsky, JGB/Tumulka2020,
KinDipole, LatticeFVD). Adversarial consistency: "publication-
grade"; 2 critical + 5 minor self-description/drift items, all
fixed (B4 fork, abstract scoping, empirical-LI slogan, shield-core
back-references, inverse-not-contrapositive, NEC cite, band
exactness); shield-core proof verified line-by-line; 48/48 + 46/46
citations resolve, zero orphans. Calculations: ALL PASS — 9 scripts
rerun bit-consistent, 5 long-script sets trace verbatim, 6
hand-checks verified, no discrepancies. Threads: 9-thread ranked
strategy delivered; T1-T3 queued as tasks 10-12; T4 (conformal
gravity) / T5 (quantum lattice) next-big-paper candidates.
**Corpus final: paper 1 28pp v1.1, paper 2 21pp. Publish pipeline
(task 9) awaits hold-lift.**

Paper 2 novelty per adversarial sweep:
instantaneity/Markov application, trilemma (third vertex), foliation
observability, all novel; LHFL-resolution and CSA-limitations
claims re-scoped onto their prior art with our increments intact.

### Simulation program S1–S3: COMPLETE

S1: FTL lives only in conditioning (machine-precision no-signaling
for closed/dilated; new corollary TV∞ = κ̃/sinθ). S2: completions
are operationally acausal channels iff explosive class;
minimal = causal. S3: foliation determinacy vanishes continuously
at the vacuum. Together with E1–E4/2D, decomposition, and M3: nine
simulations, every one with inline controls, three documented
self-corrections. Paper #2 numerics closed.
