# Running log — PT-symmetric / indivisible-stochastic bridge

Continuation of `PT_stochastic_handoff.md`. Baseline experiment: `pt_barandes.py`.

---

## 2026-07-10 — §5.1 DONE: Fixed-beable / Kolmogorov-cycle characterization

**Question.** Which non-Hermitian `H` admit a metric `η` diagonal in the
configuration basis, so the Barandes beables are preserved rather than rotated?

**Answer: the conjecture in the handoff is TRUE, and sharper than expected.**
Code + numerical verification: `fixed_beable_kolmogorov.py` (all checks pass,
including 200/200 randomized trials at n = 3..6).

### Theorem (fixed-beable characterization)

`H` admits a positive diagonal metric `η = diag(d)`, `d_i > 0`, with
`H†η = ηH`, **iff** all of:

- **K1** — every diagonal entry `H_ii` is real;
- **K2** — symmetric coupling support: `H_ij = 0 ⇔ H_ji = 0`;
- **K3** — `H_ij H_ji > 0` for every coupled pair (equivalently
  `arg H_ij + arg H_ji = 0`);
- **K4** — **Kolmogorov cycle condition**: around every cycle of the coupling
  graph, the product of coupling moduli one way equals the product the other
  way.

*Derivation.* The component form of `H†η = ηH` with `η = diag(d)` is
`d_i H_ij = d_j H*_ji`. The `i=j` component gives K1; existence of positive
`d` forces K2; the phase of the off-diagonal relation gives K3; its modulus
gives `d_i/d_j = |H_ji|/|H_ij|`, whose loop-consistency is exactly K4.
Conversely, build `d` along a spanning forest; K4 makes it well defined.

### Corollaries (each verified numerically)

1. **Reality of the spectrum is derived, not assumed.** K1–K4 imply
   `h = η^{1/2} H η^{-1/2}` is Hermitian, so the spectrum is automatically
   real — unbroken antilinearity falls out of the combinatorial conditions.
2. **Uniqueness — cost 4b resolved in this class.** `d` is unique up to one
   scale per connected component of the coupling graph, and the fixed-beable
   process `Γ_ij(t) = (d_i/d_j)|U_ij(t)|²` is invariant under those scales, so
   the process is **unique**. The metric non-uniqueness problem disappears
   exactly when the beables are fixed.
3. **The correction is a pure reweighting.** With diagonal `ρ = diag(√d)`,
   `Γ_ij = (d_i/d_j)|U_ij|²`: same configurations, same beable set; the metric
   enters only as importance weights on the naive transition probabilities.
4. **Classical dictionary (task d).** With hopping rates `q(i→j) := |H_ji|`
   (Barandes column convention), the distribution `π_i ∝ 1/d_i` satisfies
   classical detailed balance `π_i q(i→j) = π_j q(j→i)`. So the metric weights
   are the *inverse* of the Kolmogorov equilibrium distribution of the modulus
   rate graph, and K4 is literally Kolmogorov's criterion from Markov-chain
   theory. Structural characterization: fixed-beable `H` = the positive
   diagonal similarity orbit of Hermitian matrices ("detailed-balanced
   gain/loss").

### Numerical results (from `fixed_beable_kolmogorov.py`)

- **(b) 2×2 canonical PT model fails, as predicted** — via K1 (diagonal
  `e^{±iθ}` not real), consistent with the beable rotation seen in
  `pt_barandes.py`. Note: at n=2 there are no cycles beyond pairs, so K4 is
  vacuous and fixed-beable ⇔ Hermitian *within that family*. The cycle
  condition only bites at n ≥ 3.
- **(c) 3×3 non-Hermitian example passing K1–K4** (built from `d = (1,2,4)`
  with magnitude-asymmetric, phase-antisymmetric complex couplings;
  `‖H − H†‖ ≈ 1.69`): spectrum real `{−1.319, 0.210, 2.009}`; recovered
  `d = (1,2,4)` exactly; naive `|U|²` column sums `(0.40, 1.17, 3.04)` — not
  stochastic — while the reweighted `Γ` is doubly stochastic with
  `‖Γ(2t) − Γ(t)²‖ ≈ 0.41` (genuinely indivisible), **with beables fixed**.
- **Sharp counterexample: only K4 fails.** `H = diag(1,2,3) +` an asymmetric
  positive ring (cycle products 0.216 vs 0.027). Spectrum still real
  `{0.847, 1.840, 3.313}`, positive-definite biorthogonal metric exists, valid
  indivisible process exists (`‖Γ(2t) − Γ(t)²‖ ≈ 0.49`) — but the diagonal
  intertwiner solution space is exactly zero and `ρ` has an 18% off-diagonal
  fraction. **K4 gates fixed beables specifically, not process existence.**
- **Randomized theorem check**: 200/200 trials, n = 3..6 — constructor and
  independent null-space solver agree; K1–K4 ⇒ unique-up-to-scale `d`, real
  spectrum, doubly stochastic fixed-beable `Γ`; perturbing one cycle edge's
  modulus ⇒ K4 fails ⇒ diagonal solution space dimension 0.

### Quotable statement

> A PT/pseudo-Hermitian dynamics admits a fixed-beable indivisible stochastic
> representation iff its coupling graph satisfies the Kolmogorov
> detailed-balance conditions (real diagonal, phase-antisymmetric couplings,
> cycle condition on coupling moduli). The metric weights are then the inverse
> of the detailed-balance stationary distribution, and the fixed-beable
> process is unique.

This resolves conceptual cost 4a of the handoff (dynamics-dependent beables)
by exactly delimiting when it does and doesn't occur, and resolves cost 4b
(metric/process non-uniqueness) within the fixed-beable class. The
deflationary reading deepens: the non-Hermiticity compatible with fixed
beables is precisely classical-detailed-balance gain/loss — a diagonal gauge
of a Hermitian theory.

---

## 2026-07-10 — §5.2 DONE: Broken phase as an open subsystem via dilation

Code: `dilation_bridge.py`. **Result: the broken phase supports a valid,
permanently indivisible sub-stochastic process with zero information
backflow — the two non-Markovianities dissociate, and Barandes
indivisibility is the strictly stronger notion.**

### Construction

1. **Broken PT = post-selection (exact identity).** The canonical dimer is
   balanced gain/loss: `H = cosθ·I + i sinθ σ_z-type + s σ_x`. Subtracting
   the uniform gain, `H_loss = H − i sinθ·I` is pure loss and
   `e^{-iHt} = e^{+sinθ·t} · C(t)` with `C(t) = e^{-iH_loss t}` a contraction
   (verified: singular values ≤ 1 for all t, identity to machine precision).
   The notorious broken-phase runaway is a *scalar normalization*; the
   conditional (normalized) dynamics coincide. Mannheim's broken phase is
   survival-conditioned dynamics of a lossy system.
2. **Halmos dilation, per time t.** `U_big(t) = [[C, √(1−CC†)],[√(1−C†C), −C†]]`
   is exactly unitary (error ~1e-15) with `Γ_big(0) = I`. Barandes needs only
   per-time unistochasticity — the family need not be a group (indivisibility
   *is* the failure to compose) — so `Γ_big(t) = |U_big(t)|²` is an ordinary
   Barandes indivisible process on 4 configs {1, 2, a1, a2}. A finite
   Hermitian generator can't reproduce decay for all t (quasi-periodicity),
   but the per-time dilation sidesteps that entirely.
3. **Reduced process** `Γ_red(t) = |C(t)_ij|²` = top-left block: entries ≥ 0,
   column sums ≤ 1 for all t (verified). Column-sum deficit = leak
   probability; broken-phase survival decays monotonically.

### Diagnostics

- **Divisibility (Barandes-intrinsic).** With `Γ(t₁)` invertible the unique
  divisor candidate is `M = Γ(t₂)Γ(t₁)⁻¹` (column sums automatic), so
  divisibility ⇔ `M` entrywise ≥ 0 (+ col sums ≤ 1 if sub-stochastic).
  Infinitesimal version: classical P-divisibility ⇔ generator
  `L(t) = Γ̇Γ⁻¹` has nonnegative off-diagonals (exact derivative via
  `Ċ = −iH_loss C`; condition-number guarded — early runs showed the
  *magnitudes* of finite-gap violations are conditioning-sensitive, but sign
  and location are robust, e.g. worst broken-phase point has cond(Γ) ≈ 830).
- **Backflow (BLP analog).** TV distance between the two basis-state
  initializations: (a) extended 3-outcome space {1, 2, leaked} — linear;
  (b) conditional (survival-post-selected). Reported in windows [0,20] and
  [20,40].

### Findings (θ = π/4, sweep s = 0.3 … 1.3, EP at s = sinθ ≈ 0.7071)

1. **The reduced process is indivisible in BOTH phases** (t* ≈ 1 everywhere),
   but the *temporal structure* flips at the EP:
   - **Broken/EP**: `min offdiag L(t)` goes negative at t* and **stays
     negative forever**, smoothly approaching a strictly negative constant
     (e.g. −1.207 at s=0.5) — *terminal, persistent indivisibility*, no
     revivals (lock-in to the slow decay mode).
   - **Unbroken**: `L(t)` **oscillates** through recurrent positive
     (divisible) and negative windows at the Rabi period — *recurrent
     indivisibility*, the open-system shadow of closed-system quasi-periodic
     interference.
2. **Information backflow transitions exactly at the EP.** Late-window
   conditional backflow (bf[20,40]) = 0.0000 for every broken s and at the
   EP; jumps to 1.32 at s = 0.72. Broken-phase backflow is a finite
   early-time transient; unbroken accrues per oscillation forever.
   (Matches known PT open-system results, but here derived at the
   stochastic-process level.) Extended-space (linear) classical backflow is
   **identically zero in both phases** — classical marginals with a leak
   outcome never show backflow in this dilation.
3. **Answer to the frontier question: YES, with a precise meaning.** Broken
   PT gives an indivisible process the closed/Hermitian case cannot:
   *terminally* indivisible with monotone leak and zero backflow. A closed
   Hermitian system's `Γ = |U|²` is quasi-periodic — its indivisibility is
   necessarily recurrent. So the two "non-Markovianities" genuinely meet
   here and **dissociate**: broken PT is backflow-Markovian yet
   Barandes-indivisible. Indivisibility is the finer probe of the PT phase:
   it doesn't vanish at the EP — it changes character (recurrent ↔
   terminal).
4. Bonus identity: any 2-site lossy Hamiltonian is a shifted PT dimer, so
   "overdamped open dynamics" and "broken PT" coincide at n=2; the
   stochastic signature of PT breaking is the recurrent→terminal
   indivisibility transition plus loss of backflow.

### Caveats

- Near the EP the oscillation period π/√(s²−sin²θ) diverges; any finite
  window smooths the transition (s=0.72 shows lateNeg=1.00 in [6,12] only
  because its first revival is at t≈23 — the [20,40] backflow window
  correctly catches it). The dichotomy is exact as T→∞.
- Finite-gap violation *magnitudes* are not calibrated (conditioning-
  sensitive); only sign/location are meaningful. Generator trace is the
  robust diagnostic.
- 2×2 toy; terminal-indivisibility asymptote not yet proven analytically.

---

## 2026-07-10 — §5.3 DONE: The exceptional point

Code: `exceptional_point.py`. **Verdict: the EP is a coordinate singularity
of the similarity-to-Hermitian dictionary, not of the stochastic process.**
The crack in the deflationary argument is real (no Hermitian partner exists
at the EP) but harmless at the process level: existence of an indivisible
process is governed by the dilation (§5.2), which is smooth there.

### At the EP (s* = sinθ)

- `H` defective as expected: double eigenvalue cosθ, rank(H − cosθ·I) = 1,
  cond(eigenvector matrix) ~ 1e8 (numerically Jordan).
- Naive `|U|²` grows **polynomially**, fitted exponent 1.95 ≈ 2 (Jordan
  `t·e^{-iEt}` ⇒ t² in probabilities) — sitting exactly between unbroken
  (bounded) and broken (exponential).
- The Hermitian intertwiner space at the EP is 2-dimensional: one **singular
  PSD rank-1** ray and one indefinite direction. The positive-definite cone
  is exited exactly through the singular boundary — no `ρ`, no Hermitian
  partner, the Mostafazadeh deflation genuinely fails *at* this point.

### Collapse scalings from the unbroken side (s = s*(1+ε), κ ~ √(2ε)·sinθ)

Verified over ε = 1e-1 … 1e-7 with log-log slope fits (all to ±0.002):

| quantity | scaling | fitted slope |
|---|---|---|
| cond(η) | ε⁻¹ ~ κ⁻² (Petermann-factor divergence) | −0.998 |
| cond(ρ) (beable-map anisotropy) | ε^(−1/2) ~ κ⁻¹ | −0.499 |
| ‖Γ_ε(t) − I‖ at fixed lab t | ε ~ (κt)² | +0.999 |

So at any fixed lab time the metric-corrected process **freezes to the
trivial identity process** (`h → cosθ·I`, Rabi frequency → 0). A regularized
lab-time limit exists but is trivial — and it is *not* the EP dynamics,
which grows like t². The limit is discontinuous with respect to the physics.

### What genuinely survives: the critical process in rescaled time

On the critically-slowed clock τ = κt, `Γ_ε(τ/κ)` converges (to 1e-10
between ε = 1e-4 and 1e-6) to the universal Rabi process
`Γ_lim(τ) = [[cos²τ, sin²τ],[sin²τ, cos²τ]]` (Rabi axis exactly σ_x — the
same symmetric form as the baseline's unbroken result), which is genuinely
indivisible (‖Γ(2τ) − Γ(τ)²‖ ≈ 0.97). The Jordan linear growth is the
κ → 0 limit of sin(κt)/κ. **But** this survivor is abstract: the beable map
`ρ_ε` that identifies its states with the original configurations diverges
(cond ~ κ⁻¹), so the process outlives the EP while its beable interpretation
does not — the §5.1 beable-rotation cost becoming infinite.

### Reconciliation with §5.2 (the punchline)

Dense sweep s = 0.68 … 0.735 through the EP: every open-side quantity
(reduced-process entries, survival, indivisibility generator floor) varies
smoothly and monotonically through s*, while the closed-side cond(η)
diverges approaching it from above and doesn't exist below. Nothing physical
happens at the EP in the process description; only the Hermitian dictionary
blows up. Combined three-phase picture of the naive process growth —
unbroken: bounded / EP: polynomial / broken: exponential — versus the
dilated sub-stochastic process, which is valid and indivisible throughout.

---

## 2026-07-10 — LEMMA PROVED: terminal indivisibility is exact and analytic

Code: `lemma_terminal_indivisibility.py` (verifies every claim to 1e-11).
§5.2 finding 1 is now a theorem, with sharper structure than the numerics
suggested.

**Lemma.** For the dimer in the broken phase (κ̃ = √(sin²θ − s²) > 0), with
c = cosh κ̃t, shc = sinh(κ̃t)/κ̃ and
`p = c + sinθ·shc`, `q = c − sinθ·shc`, `r = s·shc`:

- `Γ_red(t) = e^{-2sinθ·t} [[p², r²],[r², q²]]`, `det Γ_red = e^{-4sinθ·t}(1−2r²)`;
- the generator off-diagonals are **exactly**
  `L₁₂ = 2spr/(1−2r²)`, `L₂₁ = 2sqr/(1−2r²)`
  (the Wronskian-type combinations r′p − p′r and r′q − q′r are both
  identically the constant s — that is the whole proof).

**Consequences (all verified numerically):**
1. P-divisibility holds precisely on [0, t_c) with
   `t_c = κ̃⁻¹ arcsinh(κ̃/(s√2))` — exactly the time at which `det Γ_red`
   crosses zero. Divisibility dies when and because the process becomes
   singular. (Explains the finite-gap spikes near t ≈ 1.3 in
   `dilation_bridge.py`; exact t_c = 1.3170 at s = 0.5 vs the observed
   grid value 1.35.)
2. For all t > t_c: `L₁₂ < 0` strictly, forever — permanent indivisibility.
3. `L₁₂ → −(sinθ + κ̃)`: the numerically observed floor −1.207 at s = 0.5
   is −(sin(π/4) + 0.5) = −1.2071 exactly; also confirmed at (π/4, 0.3) →
   −1.3474 and (π/3, 0.5) → −1.5731.
4. `L₂₁` flips back positive at `t₀ = κ̃⁻¹ artanh(κ̃/sinθ) > t_c`: late-time
   indivisibility is carried entirely by L₁₂ — transitions *into* the gain
   site.
5. One formula, three regimes: analytic continuation κ̃ → iκ gives the
   unbroken phase, where `1 − 2(s/κ)² sin²(κt)` oscillates through zero
   forever (recurrent windows; note (s/κ)² > 1 always); at the EP
   everything is polynomial with `t_c = 1/(s√2)`, and t_c is continuous
   across the transition (verified to 1e-4).

---

## 2026-07-10 — §5.4 DONE: Pais–Uhlenbeck

Code: `pais_uhlenbeck.py` (grid 44² = 1936 configs, spectral derivatives).
**Verdict: the stochastic-quantum correspondence and the PT no-ghost
construction part ways at PU — they resolve the ghost in incompatible
currencies (beable reality vs energy positivity).**

### A. The ghost realization IS a valid Barandes process (answer to Q-a)

The Ostrogradski Hamiltonian
`H = p₁q₂ + p₂²/2γ + (γ/2)(ω₁²+ω₂²)q₂² − (γ/2)ω₁²ω₂²q₁²` is **Hermitian on
the real configuration space (x, ẋ)**. On the grid: `‖H − H†‖ = 0`,
`Γ = |U|²` doubly stochastic to 2e-14 on 1936 configs, genuinely indivisible
(‖Γ(2t) − Γ(t)²‖ ≈ 2.7), and validated dynamically — Ehrenfest is exact for
quadratic H, and ⟨x(t)⟩ tracks the exact classical fourth-order trajectory
to 3e-3 (residual = packet tails at the box walls). Spectrum runs from −26
to +140: **unbounded below, and completely irrelevant** — the ghost is an
energy-accounting pathology, invisible to the free stochastic process.
Beables are fixed (Hermitian ⇒ K1–K4 with η = 1). Barandes' correspondence
makes perfect sense for free PU, negative energies and all.

### B. The no-ghost move has no stochastic counterpart (answer to Q-b)

Mannheim's positive spectrum requires the ghost mode's vacuum to satisfy
`b†Ω = 0` (position space: e^{+y²/2}) — normalizable only on a rotated
contour. This is a **domain change, not a similarity** (a similarity can't
flip the spectrum), and finite-dimensional machinery can never see it:
- null(b) = |0⟩ at every truncation N (the true vacuum, stable);
  null(b†) = |N−1⟩ — pinned to the truncation edge, escaping to infinite
  energy as N grows; restricted to any fixed low-energy sector,
  σ_min(b†) = 1 exactly. **The PT vacuum has no shadow in the
  real-configuration theory at any cutoff.** Not a beable rotation (§5.1),
  not a coordinate collapse (§5.3) — an exit from the sample space.
- The contour-rotation operator `R = e^{(π/2)D}`, `D = (i/2)(a†² − a²)`
  (the y → −iy dilation): log₁₀ cond(R_N) grows at ~1.2 decades per Fock
  level (53 decades at N = 48); the would-be metric ~(RR†)⁻¹ is unbounded
  with unbounded inverse. The §5.3 collapse at every scale at once, with no
  critical-rescaling survivor.

So: **no valid stochastic process on the original beables realizes the
positive-energy PU.** Barandes keeps real beables and pays in negative
energies; Mannheim buys positive energies and pays with the sample space
itself. The handoff's §4.4a cost (dynamics-dependent beables), taken to the
PU limit, becomes beable *non-existence*.

### C. Equal frequencies (the PU exceptional point)

Classical normal-mode matrix defective (eigenvector cond ~1e8, Jordan
block, secular t·sin(ωt) growth) — yet the Hermitian grid realization
passes through smoothly: ⟨x(t)⟩ tracks the secular classical solution
`2cos(ωt) + ωt·sin(ωt)` to 9e-4 and Γ stays exactly doubly stochastic.
PU-scale confirmation of §5.3: the Jordan/EP pathology lives in the
normal-mode (non-Hermitian) dictionary, never in the process.

### Caveats

Free theory only — interactions (where the ghost instability becomes
physical via vacuum decay) not addressed; dense-spectrum subtleties
(ω₁/ω₂ irrational) not probed; Mannheim's specific PU operator equivalences
not re-derived (the contour-rotation structure of the quadratic ghost mode
is standard and suffices for the structural conclusion); IR/UV grid cutoffs.

---

## 2026-07-10 — INTERACTING PU: the ghost enters the process in three stages

Code: `interacting_pu.py` (quadratic cascade + classical survey + ghost-pair
quantum leak) and `quartic_pu_leak.py` (the decisive probe test).
**Answer to the open question: the instability becomes stochastically
visible in stages — recurrent → transient → explosive — and becomes a
genuine probability pathology exactly when the classical flow is
incomplete.**

### Stage 1 — quadratic interaction: valid process, now TRANSIENT

`H = ω₁a†a − ω₂b†b + g(a†b† + ab)` is Hermitian, so `Γ = |U|²` stays
exactly doubly stochastic forever (verified 2e-14). But the ghost sign
collapses the instability threshold from `g > (ω₁+ω₂)/2` (normal twin, sum
frequency) to `g > |ω₁−ω₂|/2` (difference frequency — zero at resonance).
Exact benchmarks, all matched to ~4 decimals: cascade `⟨n⟩ = sinh²(gt)`;
escape law `P(n ≤ K) = 1 − tanh^{2K+2}(gt) → 0` (rate 2g); detuned growth
consistent with `(g²/κ²)sinh²(κt)`, `κ = √(g²−δ²/4)`; normal twin bounded at
⟨n⟩ ~ 0.006. Energy books exactly balanced throughout: `E_normal = +8.301`,
`E_ghost = −8.301`, `⟨H⟩ = 0` conserved. **"Vacuum decay" is a
configuration-space cascade with balanced energy books: the process is
valid and indivisible but transient — it permanently escapes every finite
region.** First stage where the ghost is *visible* to the process
(transience), still not a pathology.

### Stage 2 — nonlinear, benign regime (Smilga): still only transience

Classical survey: the ghost pair
`(p₁²+ω₁²x₁²)/2 − (p₂²+ω₂²x₂²)/2 + λx₁²x₂²` at moderate amplitude is mostly
*bounded* (benign islands; one escape found at λ=−0.05, x₁=3.5, t*≈72).
Quantum leak test with absorber: onset drifts strongly with box size
(4.4 → 14.4 for L = 12 → 18) — tail-driven asymptotic escape at most.
Benign classically ⇒ transient (at most) stochastically.

### Stage 3 — malicious nonlinearity: EXPLOSIVE — no closed process

Quartic PU (`x⁗ + Ωẍ + ω̄x = (4λ/γ)x³`): classical **finite-time blowup**
for both signs of λ at every amplitude tested (t* = 3.3–6.9, decreasing
with amplitude; dominant balance `x ~ A(t*−t)⁻²`, `A = √(30γ/λ)`).
Quantum (split-step with the three-factor Strang decomposition for the
`p₁q₂` coupling, absorbing layer):
- **Lattice subtlety (decisive for methodology):** finite-time escape needs
  unbounded acceleration, so a grid transports the wavefront only while the
  classical arrival speed < k_max = π/dx. Box-scaling onsets (2.3 → 3.4 →
  9.5 for L = 12/18/24) correlate exactly with v_cl(edge)/k_max =
  1.4/2.4/3.4: the drift is the lattice confining, not the physics. This is
  the same structural fact as §5.4-B: a non-essentially-self-adjoint H has
  **no faithful finite truncation**.
- **Probe test (resolved regime):** quantum probability arrives at radii
  r = 5–8 at t ≈ 1.8–2.2 with bulk weight (>5%), *earlier* than the
  classical center-trajectory law t_cl ≈ 3.0–3.5 (the packet ensemble
  contains faster-escaping ICs), while the free control never passes r ≈ 6.
  Quantum arrival tracks/undercuts the classical finite-time law wherever
  the grid can resolve it; that law saturates at t* < ∞ as r → ∞.

Conclusion: in the continuum/infinite-volume limit, probability reaches
infinity at finite time. **No closed stochastic process on the real
configurations exists for the malicious interacting ghost — only a
sub-stochastic leaky one (the §5.2 dilation structure, now forced by
Hermitian physics rather than PT breaking).**

### The dictionary (closing entry)

In standard stochastic-process language the hierarchy is exactly:
- free / normal-sign: **conservative, recurrent** process;
- ghost + quadratic (and benign nonlinear): **transient** process — valid,
  indivisible, escapes to infinity asymptotically at rate 2g;
- ghost + malicious nonlinear: **explosive** process (the probabilist's
  term of art: infinitely many transitions in finite time, mass leaves the
  state space) — the semigroup is non-conservative and the closed Barandes
  representation fails.

So the Ostrogradski ghost was never an energy problem for the
stochastic-quantum correspondence: it is a *recurrence-classification*
problem. Energetics (unboundedness below) is the classical-physics
diagnosis; transience/explosion is the same disease expressed in the
process's own currency.

### Caveats

- Blowup times are tolerance-sensitive (t* = 5.13 at rtol 1e-8 vs 5.336 at
  1e-11 for the same IC); qualitative structure robust.
- Probe onsets use a 5% bulk-weight threshold; the quantum-earlier-than-
  classical arrivals reflect ensemble spread, not superluminal transport.
- The r → ∞ saturation itself is inferred from (proven) classical blowup +
  quantum tracking in the resolved window — no fixed grid can verify it
  directly (that impossibility being itself one of the findings).
- 2-DOF quantum mechanics; field-theoretic vacuum decay not addressed.

---

## 2026-07-10 — THEOREM: the explosion dictionary (stage 3 sharpened)

Code: `explosion_theorem.py` (all five verifications pass). Stage 3 of the
interacting-ghost result is now a theorem (physics rigor: Weyl alternative
and Reed–Simon II Thms X.9/X.10 cited as rigorous inputs; WKB and
semiclassical quantization used at standard validity; Feller boundary
classification for the stochastic leg).

### Theorem (explosion dictionary, 1D mechanism model)

For `H = p²/2 + V` on the line with an escaping end (`V → −∞`), define the
classical time of flight `T(E) = ∫^∞ dx/√(2(E−V))`.

1. **T = ∞** (sub-quadratic fall, e.g. `V ≳ −Kx²`): limit point ⇒ H
   essentially self-adjoint ⇒ unique unitary `U(t)` ⇒ unique conservative
   Barandes process. The ghost is at most transient.
2. **T < ∞** (super-quadratic fall — the malicious case): limit circle.
   **The one-line identity that runs the whole theorem:** WKB gives
   `|ψ±|² ≈ [2(E−V)]^(−1/2)` for *both* solutions of `(H−z)ψ = 0`, so the
   deficiency solution's L² norm near the escaping end **is** the classical
   time of flight. H loses essential self-adjointness exactly when the
   classical particle reaches infinity in finite time. Consequently:
   - (a) no canonical unitary dynamics: a U(1) family of self-adjoint
     extensions per escaping end (U(2) for two ends, including completions
     that *transmit through infinity*) — boundary data at infinity, not
     contained in H;
   - (b) every extension is conservative but returns probability from
     infinity after the finite classical round trip: discrete spectrum with
     local level spacing `ΔE = π/T_cross(E)`;
   - (c) the regulator-independent (Feller-minimal) object is
     sub-stochastic: an **explosive** process losing mass at the classical
     escape rate; conservativity costs extra-theoretic boundary data;
   - (d) one integral decides all three theories: classical completeness,
     quantum self-adjointness (Weyl), stochastic conservativity (Feller
     exit boundary).

### Verifications (V = −x⁴ malicious vs V = −x² marginal control)

- **V1** — the integral: convergent exactly for α > 2 (α=4: 0.6484 →
  0.6555 over four decades of cutoff; α=2: log-divergent 3.1 → 9.6).
- **V2** — level-spacing law `ΔE = π/T_cross(E, L)` matches measured
  spacings to ~1–3% in all 8 (potential, L) cases; for −x⁴ the spacing
  *saturates* (2.32 vs predicted 2.32 at L=16 — reflection off infinity at
  finite recurrence time), for −x² it decays toward the continuum.
- **V3** — extension = regulator data: the eigenvalue nearest E=10 sweeps
  erratically as the wall moves (10.06, 8.84, 9.82, 10.72, …): no L→∞
  limit for any individual completion, while the spacing is stable.
- **V4** — the minimal process converges and explodes: 1D absorbing-layer
  evolution (1D beats the lattice resolution barrier that blocked the 2D
  runs): absorbed mass at t=1 is 98.6–98.8% **independent of box size**
  (L = 8/12/16), and the onset saturates tracking the classical arrival
  times (0.34/0.38/0.40 → T_esc = 0.4635). Direct verification that
  probability reaches infinity at finite time.
- **V5** — completions observably differ: with a Dirichlet wall the
  probability leaves rightward and returns from the right (P(x>5) = 0.047,
  P(x<−5) = 0.000 at revival); with periodic identification it returns
  from the **left** (0.035 vs 0.013) — a +∞→−∞ wormhole. Both revive
  ~95% of the probability after the finite round trip. Same H on C₀^∞,
  different physics: the completion is genuinely new data.

### Interpretation, tied back to the program

The malicious interacting ghost forces a trilemma, and each horn is now a
computed object: (i) accept the **minimal explosive process** — exactly the
§5.2 sub-stochastic dilation structure, and the only regulator-independent
choice; (ii) buy conservativity with **boundary data at infinity** —
unphysical completions that resurrect probability from infinity (from a
side of your choosing); (iii) repair the spectrum à la Mannheim by moving
the domain — which §5.4-B showed exits the sample space entirely. The
Barandes currency makes (i) the canonical answer: vacuum decay of the
malicious ghost *is* explosion in the standard probabilistic sense.

### Caveats

- The theorem is for the 1D mechanism model; the reduction of the 2-DOF
  malicious systems to it is by dominant-balance structure (super-quadratic
  effective fall along the escape direction), not a rigorous
  multi-dimensional deficiency analysis.
- Spacing law and WKB norms are semiclassical-standard, not re-proven;
  R–S X.9/X.10 supply the rigorous LP/LC inputs.
- V4 onset is earlier than the classical rest-start arrival (packet
  momentum tails), as expected; the L-trend is the claim being tested.

---

## 2026-07-10 — MULTIDIMENSIONAL DEFICIENCY ANALYSIS (the rigorous layer)

Code: `deficiency_multiD.py` (all verifications pass). The 1D explosion
dictionary is upgraded to a channel-based multidimensional theory. Crucial
context: in n ≥ 2 the naive dictionary "classical incompleteness ⇔ quantum
non-self-adjointness" is **false in general** (Rauch & Reed, Commun. Math.
Phys. 29, 105 (1973)) — so the correct structure is channel-wise, and
proving it adds content the 1D story cannot supply.

### Theorem C — quadratic ghosts are rigorously safe

Any at-most-quadratic Hamiltonian on ℝⁿ — including the indefinite
cascade `H = ω₁a†a − ω₂b†b + g(a†b†+ab)` at *any* coupling (even deep in
the unstable phase) and the free PU Ostrogradski operator — is essentially
self-adjoint on the Hermite span. *Proof:* quadratics map Hermite level N
into level ≤ N+2 with coefficients O(N), so
`‖Hⁿψ_N‖ ≤ (2C)ⁿ(N/2+n)!/(N/2)!` and every Hermite function is an analytic
vector; Nelson's analytic vector theorem applies. ∎
**Consequence:** unique unitary, unique conservative Barandes process —
"instability ≠ non-uniqueness/explosion" is now a theorem. The
transient/explosive dichotomy of the interacting-ghost section is rigorous
on the transient side.

### Theorem A — channel additivity of deficiency (separable multiD)

Let `H = h₁⊗1 + 1⊗h_⊥` on L²(ℝ×ℝᵐ), with `h₁ = ½p² + V₁`, `V₁`
super-quadratically falling (finite time of flight; limit circle by
R–S X.10), and `h_⊥` self-adjoint with orthonormal eigenbasis {φₙ, Eₙ}.
Since the limit-circle property is independent of the spectral parameter
(Weyl), for **every** channel n, **every** solution u of
`(h₁ − (±i − Eₙ))u = 0` is L², and a two-line distributional computation
gives `H*(u⊗φₙ) = ±i(u⊗φₙ)`, i.e. `u⊗φₙ ∈ ker(H* ∓ i)`. Orthogonality
across n ⇒ **deficiency indices (∞,∞)** (2 per channel for a two-ended
escape; (2M,2M) in an M-channel truncation). ∎
**Consequence:** the conservative completions are parametrized by
unitaries between infinite-dimensional deficiency spaces — a genuine
**S-matrix at infinity**, including completions that scramble the
transverse state on reflection.

### Theorem B — central malicious potentials in ℝᵈ

`−½Δ − c|x|^α`, α > 2: partial-wave separation reduces to radial channels
whose effective potentials differ by subquadratic centrifugal terms ⇒
each channel is limit-circle at infinity ⇒ deficiency indices (∞,∞). ∎

### Theorem D — non-separable channel mixing, rigorously

`H = ½p₂² − |x₂|^α + h_⊥(x₁) + μ f(x₁)g(x₂)` with f, g **bounded**, α > 2:
a bounded symmetric perturbation preserves deficiency indices exactly
(Kato stability), so the indices remain infinite while the coupling
genuinely mixes channels (f odd ⇒ n ↔ n±1). ∎
**Honest boundary:** the physically-arising *unbounded* diagonal couplings
(λx₁²x₂² in the ghost pair, λq₁⁴ in the PU chain) defeat both separation
and relative-boundedness. Whether they preserve infinite deficiency — or
even *restore* essential self-adjointness (a quantum completion, which
Rauch–Reed shows is possible in principle) — is genuinely open. Note the
indefinite-kinetic structure adds a second obstruction: for
`H₀ = h₁⊗1 + 1⊗h_⊥` with h₁ unbounded below, transverse observables are
NOT H₀-bounded (joint spectral cancellations), so the standard
Kato–Rellich transfer fails even for mildly unbounded couplings.

### Numerical fingerprints (M = 4 channels, V₁ = −|x|^{5/2}, bounded
### coupling μ·tanh(x₁)·x₂²/(1+x₂²/10), μ = 0.2)

- **N1 — channel additivity**: wall-regularized level counts in [5,17]:
  measured 34 (L=8) and 37 (L=12) vs channel-sum semiclassical prediction
  `Σₙ∫ T_cross(E−Eₙ,L)/π dE` = 32.3 and 37.1 (3–5%, i.e. ±1–2 levels).
  At μ=0 the spectrum is *exactly* the union of shifted 1D ladders
  (deviation 1e-12).
- **N2 — Kato stability visible**: switching the coupling on (μ: 0 → 0.2)
  shifts individual levels but leaves the window count unchanged
  (34 → 34, 37 → 36).
- **N3 — the S-matrix at infinity (star demo)**: a channel-0 packet slides
  out, reflects off the regulator, and **returns as a channel mixture
  whose content depends on where "infinity" was regularized**:
  fractions (n = 0..3) = (0.583, 0.346, 0.058, 0.014) for L=6 versus
  (0.401, 0.421, 0.143, 0.035) for L=9, with 96%/93% of the probability
  returning and revival times tracking the classical round trips
  (arrivals 0.88/1.06). The completion doesn't just choose a reflection
  phase — it chooses how the transverse state is scrambled.

### Upshot for the program

1. Both sides of the transient/explosive dichotomy are now theorem-level
   for their model classes: quadratic/transient ⇒ rigorously unique and
   conservative (Theorem C); channelized malicious ⇒ rigorously infinite
   deficiency (Theorems A, B, D).
2. In multi-D the trilemma's second horn gets much worse: conservative
   completions of a malicious ghost require an infinite-dimensional,
   channel-scrambling S-matrix at infinity — decoherence-like data
   injected at infinity. The canonical status of the minimal explosive
   (sub-stochastic, §5.2-structured) process is correspondingly stronger.
3. Sharp open problem, precisely delimited: essential self-adjointness of
   the exact quartic-PU Ostrogradski operator and of the λx₁²x₂² ghost
   pair — obstructed by unbounded diagonal coupling + indefinite kinetic
   form; either outcome (infinite deficiency or quantum completion) would
   be interesting.

---

## 2026-07-10 — LITERATURE SWEEP (novelty check; paper updated)

Verdict per result; the paper was amended (8 new citations, attribution
remarks inserted; recompiles clean at 19 pp.):

1. **Dissociation theorem — novelty intact, framing sharpened.** Key prior
   art: Kawabata–Ashida–Ueda, PRL 119, 190401 (2017) — information
   retrieval possible only in the unbroken phase, power-law criticality at
   the EP, and a unitary-embedding ("hidden entangled partner")
   perspective. They did NOT compute divisibility or generators, and work
   with quantum states, not the classical configuration process; no exact
   t_c/floor forms; no terminal-vs-recurrent structure. Also:
   divisibility- vs information-flow-Markovianity are known to be
   inequivalent for quantum channels (Chruściński–Rivas–Størmer, PRL 121,
   080407 (2018)) — our contribution is that the dissociation is exact,
   phase-locked, and permanent at the classical process level. Paper now
   cites both and presents the dilation as the process-level counterpart
   of KAU's embedding. No paper found computing P-divisibility/generator
   negativity of the PT dimer's conditional process.
2. **K1–K4 — matrix core is classical, as suspected.** Parter–Youngs,
   J. Math. Anal. Appl. 4, 102 (1962); Engel–Schneider, Linear Algebra
   Appl. 7, 301 (1973). Paper now attributes the algebra and claims only
   the beables/detailed-balance/uniqueness/real-spectrum reading.
   Reverse direction cited: Van Wesemael et al., arXiv:2510.09467 (Dyson
   maps restoring detailed balance in classical Markov processes).
3. **Barandes × PT bridge — clear.** Nothing found connecting the
   stochastic-quantum correspondence to non-Hermitian/PT systems.
4. **Ghost/explosion framing — clear, and timely.** Two April-2026 papers
   (Deffayet–Fathe Jalali–Held–Mukohyama–Vikman, arXiv:2604.21823;
   Ewasiuk–Profumo, arXiv:2604.21348) prove interacting-ghost stability
   via conserved quantities / moment bounds — complementary
   (recurrence-enforcing mechanisms in our language); no domain theory,
   explosion, or stochastic reading. Salvio–Strumia, EPJC 76, 227 (2016)
   cited in §6 as the negative-norm-configuration-space alternative. No
   prior essential-self-adjointness/deficiency/Feller treatment of
   interacting PU found.
5. **Skin-effect/K1–K4 follow-up — open.** No beables/ontology reading of
   the skin effect found; non-Bloch methods for classical stochastic
   processes exist (useful related work, not preemption).

Net: all three headline claims survive; attribution is now correct; the
interacting-ghost topic is demonstrably active (two 2026 papers).

---

## 2026-07-10 — THEOREM: the skin effect is the obstruction to fixed beables

Code: `skin_effect_beables.py` (all checks pass; produces
`paper1/figs/fig_skin.pdf`). The K1–K4 gauge/continuum question is closed;
the paper gained §3.1 ("Gauge form: the non-Hermitian skin effect is the
obstruction"), Theorem 3.4, Fig. 8, and the Okuma–Kawabata–Shiozaki–Sato
citation (PRL 124, 086801 (2020)). Now 21 pages, compiles clean.

### Gauge-form lemma

K2+K3 ⟺ the couplings can be written uniquely as
`H_jk = t_jk e^{iφ_jk + w_jk}` with `t` symmetric positive, `φ, w`
antisymmetric real — a lattice Peierls substitution `p → p − A − iW` with
real gauge field φ and **imaginary gauge field w** (Hatano–Nelson). K1 =
no on-site gain/loss.

### Theorem (skin obstruction)

1. Fixed beables exist iff the **imaginary flux vanishes through every
   cycle** (Σ_C w = 0 — this is exactly K4). Then `w_jk = χ_j − χ_k` is
   pure gauge, `η = diag(e^{−2χ})` is the exponentiated imaginary gauge
   transformation, and `Γ_jk = e^{2(χ_k−χ_j)}|U_jk|²`. **Real magnetic
   flux is unconstrained.**
2. Classical dictionary: with rates `q(j→k) = |H_kj|`, imaginary flux =
   cycle affinity; zero iff the chain is reversible (Kolmogorov); nonzero
   iff there is a steady-state cycle current. **The skin effect is the
   quantum image of a detailed-balance-violating (irreversible) classical
   cycle.**
3. Hatano–Nelson: a ring with uniform w carries flux Nw ⇒ no fixed
   beables; the PBC spectrum is a complex loop (spectral winding — the
   topological invariant of the skin effect) ⇒ no closed process at all.
   An open chain is a tree ⇒ fixed beables exist at every finite N with
   `d_i = e^{2wi}`; the OBC/PBC dichotomy of the skin effect IS the
   pure-gauge/flux dichotomy.

### Verification (all exact)

- 50/50 random gauge-form graphs with arbitrary real fluxes: constructed
  metric = e^{−2χ} exactly, spectrum real; one quantum of imaginary flux
  through any cycle ⇒ diagonal solution space dim 0.
- HN chain: OBC spectrum = Hermitian chain spectrum to 1e-10; skin
  eigenvectors = e^{−wi} × Hermitian eigenvectors to 5e-15;
  cond(η) = e^{2w(N−1)} to 4 digits at N = 8/16/24/32 — fixed beables
  exact at finite N, exponentially degenerate as N → ∞ (the PU
  unbounded-metric pathology in 1D lattice form).
- HN ring: max|Im E| = 2 sinh w exactly (complex loop).
- Classical ring current: J = −3e-17 at zero imaginary flux, monotone
  nonzero with flux (reversibility ⟺ K4, verified).
- Sub-transition regime (diagonally dominated triangle): binary criterion
  trips at any nonzero flux; beable rotation grows continuously
  (0 → 0.31 for flux 0 → 1.5).

---

## 2026-07-10 — PU-DEFICIENCY EVIDENCE CAMPAIGN (Open Problem 9.6)

Code: `pu_deficiency_evidence.py`. Design: Fock-space (Hermite)
compression as the regulator (regulates position AND momentum — the PU
escape accelerates without bound — and avoids lattice doublers from
p₁q₂; a mode-1 Fourier rotation makes the quartic PU real symmetric);
diagnostic = matched-eigenvalue drift between successive truncations,
measured relative to local spacing in a window near E = 0; calibrated on
known 1D operators; verdicts required to be robust under a basis-scale
change.

### Calibration (window E ∈ [5,15])

- discrete e.s.a. (`p²/2 + x⁴`): drift ratio exactly 0.000 ✓
- continuous e.s.a. (`p²/2 − x²`): ratio → ~0.15, spacing shrinking ✓
- limit circle (`p²/2 − x⁴`, indices (2,2)): spacing saturates, ratio
  stays O(1) erratically forever (0.54, 2.02, 0.42, 0.77) ✓ — the Fock
  analog of the sweeping-wall diagnostic.
- free PU (e.s.a. by the quadratic/Nelson theorem): the 2D baseline:
  ratio ~0.15–0.3, spectrum densifying, old states persisting ✓.

### Verdicts (N per mode = 24…48)

1. **Quartic PU (λ = 0.05): limit-circle-like — evidence AGAINST
   essential self-adjointness.** Drift ratios 1.21, 0.85, 0.79, 1.57
   (basis scale ν₁ = 1.0) and 0.34, 0.98, 0.98, 1.96 (ν₁ = 0.7):
   persistently O(1), NOT decaying with N (largest at the finest
   truncation), ~5× the free-PU baseline computed with identical
   machinery minus the quartic term. The window spectrum reorganizes
   completely between truncations at both basis scales. Evidence that
   the explosion dictionary applies to the physical Mannheim operator
   with (presumably infinite) deficiency indices.
2. **Ghost pair λ = +0.05: quantum-complete, as predicted.**
   Born–Oppenheimer channels W_n(x₂) = ½ω₂²x₂² − (n+½)√(ω₁²+2λx₂²) are
   all confining (quadratic dominates); drift ratios 0.07–0.28 = e.s.a.
   baseline. Prediction → confirmation.
3. **Ghost pair λ = −0.05: SURPRISE — looks quantum-complete despite
   classical maliciousness.** Transverse collapse beyond x₂ = 3.16 and
   classical finite-time escape, yet drift ratios 0.22–0.29,
   indistinguishable from λ > 0. Either diagnostic insensitivity at
   these truncations, or a genuine **Rauch–Reed-type quantum
   completion**: the escape valley is a narrow diagonal channel that
   zero-point energy may wall off. If real: *interactions can
   quantum-cure a classically malicious ghost* — the most interesting
   single finding of the campaign. Tentative; needs larger truncations
   and a valley-resolved (adapted-basis) diagnostic.

### Caveats

Evidence, not proof (no finite computation decides a domain question);
the drift diagnostic's regimes are empirical calibrations; the λ<0
verdict in particular is sensitive to whether N ≤ 48 resolves the
escape valley. The quartic-PU verdict is the strongest (two basis
scales, growing-with-N signal, clean e.s.a. control on the same
operator family).

---

## 2026-07-11 — CONTINUATION 1: exact channelization of the quartic PU

Code: `pu_bo_channels.py`. Open Problem 9.6 advanced from "drift
evidence" to "structural argument + confirmed sign prediction".

### Proposition (exact displaced-oscillator channelization)

In the Fourier-rotated rep (p₁→y, q₁→−p_y), with
`U = exp(−iyp₂/(γΩ))`:
`U(H_PU + λq₁⁴)U† = T(p_y + p₂/(γΩ)) + p₂²/2γ + (γΩ/2)q₂² − y²/(2γΩ)`,
`T(p) = λp⁴ − (γω̄²/2)p²`. **Exact** (hand algebra + Fock-space check via
the terminating BCH series, residual 1.3e-9; note: a naive expm-based
check fails at truncation — displacement operators aren't banded — the
BCH form is the right numerical test). Channel-diagonal part in the
k = p_y representation = **minus** `p̂²/(2γΩ) − λk⁴ + (γω̄²/2)k²`;
interchannel couplings degree ≤ 3 in k (subordinate).

- **λ>0: every channel limit-circle** (channel time of flight 1.74 +
  convergent tail) ⇒ channel-additivity argument for indices (∞,∞).
  Gap to rigor: deficiency stability under the subordinate degree-3
  couplings.
- **λ<0: every channel confining** ⇒ predict quantum completion —
  despite classical finite-time blowup at BOTH signs.

### The sign prediction tested (drift diagnostic)

- Quartic PU λ=−0.05: ratios 0.46, 0.26, 0.36, 0.37 (ν₁=1.0) and 0.17,
  0.33, 0.35, 0.38 (ν₁=0.7): near e.s.a. baseline, sharply separated
  from λ=+0.05 (0.79–1.96). **Prediction confirmed** — the strongest
  evidence yet, being differential (same operator family, same
  diagnostic, opposite verdicts as predicted).
- Extended truncations: λ=+0.05 stays LC-like at N=48→64 (ratios 3.77,
  1.06); ghost pair λ=−0.05 stays at baseline (0.49, 0.32).
- Verdict picture: λ>0 quartic PU escapes through MOMENTUM space along
  LC channels (deficiency); λ<0 quartic PU and λ<0 ghost pair are
  Rauch–Reed quantum-completion candidates (classical escape walled off
  quantum mechanically).

Paper: Proposition 9.7 added to §9 with the confirmed prediction;
`pu_bo_channels.py` in code availability.

---

## 2026-07-11 — CONTINUATION 2: topological classification of the
## skin obstruction

Code: `skin_topology_beables.py`. Paper: Corollary 3.5 added to §3.1.

**Corollary.** For gauge-form couplings, the fixed-beable obstruction is
the class of the imaginary gauge field in H¹(G, ℝ): imaginary FIELD
STRENGTH must vanish through every contractible cycle (no imaginary
magnetic flux — a pointwise condition band-language winding does not
see) and the imaginary HOLONOMY through every non-contractible one (on a
d-torus: ℝ^d of windings, matching the multi-directional skin
classification).

Verified: 3×4 torus — diagonal-metric dim 1 iff (wind_x, wind_y, plaq)
= (0,0,0); each of the three obstructs alone. Cylinder — winding along
the open direction is gauge-removable, periodic direction obstructs
(obstruction lives in H¹ of the actual geometry). **Z₂-type ladder** —
two opposite HN chains (net winding zero, the doubled/Kramers structure
of the Z₂ skin effect): uncoupled dim 2 (metrics e^{±2wi} per chain);
any reciprocal rung coupling ⇒ dim 0 via inter-chain cycles of
circulation 2w (and, in this instance, complex eigenvalues too): **the
beable obstruction detects the doubled skin structure that net winding
misses.** (Side observation for future work: non-gauge-form couplings —
e.g. complex-symmetric hoppings of reciprocal skin classes — are
obstructed at the pairwise level K3, so the full obstruction is graded:
K1 gain/loss ⊕ K3 non-gauge phases ⊕ K4 = H¹ class.)

---

## 2026-07-11 — GAP CLOSED (finite-channel): deficiency stability theorem

Code: `gap_closure_channels.py`. Paper: Theorem 9.8 added after Prop 9.7.

**The observation that closes it:** the PU interchannel couplings are
NOT generic subordinate couplings — `T(k𝟙 + cP₂)` is a polynomial in the
single Hermitian operator P₂, so it is EXACTLY diagonal in the constant
(k-independent) eigenframe of the truncated P₂,M (simple eigenvalues p_ν
= scaled Gauss–Hermite points). No Levinson asymptotics needed.

**Theorem (finite-channel deficiency stability).** For every M, the
M-channel Galerkin model
`S_M = p̂²/(2γΩ) − T(k𝟙 + cP₂,M) − √Ω(N+½)|_M` (λ>0) has deficiency
indices (2M, 2M).
*Proof:* exact frame decoupling into scalar branches
`p̂²/(2γΩ) − T(k + cp_ν)` — each limit-circle at both ends (R–S X.10),
contributing (2,2) — plus the rotated channel-energy matrix, a CONSTANT
BOUNDED Hermitian perturbation, which preserves deficiency indices
(Kato, relative bound 0). ∎

**Verification (all pass):**
- Frame identity: eig(−T(k𝟙+cP₂,M)) = −T(k+cp_ν) to 1.3e-13; the exact
  Fock compression differs from the Galerkin model ONLY on the top ~4
  channels (0.00e0 on the bulk, O(13) on the edge at k=3.7, M=8).
- Falsifiable consequence: with couplings ON, the wall-regularized level
  density equals the all-2M-branch sum Σ_ν T_cross,ν/π: count-based
  spacing matches the prediction at every (M, L) tested (M=1: 1.33 vs
  1.30; M=2: 0.67 vs 0.66; M=3: 0.44 vs 0.45; etc.). Statistics note:
  the MEDIAN gap is biased low where the ±p_ν branch ladders lock into
  near-degenerate parity doublets (M=2 at small L) — count-based density
  is the right statistic.
- Regulator sweep (M=2): the eigenvalue nearest E never converges (LC
  behavior of the coupled system).

**Remaining (sharply delimited, full operator only):** channel-tail
control as M→∞ — the exact compression's top-4-channel edge terms, and
decay of deficiency vectors in channel number. Structurally: the full
operator is a direct integral of LC fibers over spec(p₂) coupled across
fibers by the transverse oscillator (a hybrid of Theorem-A summands and
a fiber-kinetic term). This, plus the rigorous status of the two
quantum-completion candidates (λ<0 quartic PU, λ<0 ghost pair), is what
a specialist would take up.

---

## 2026-07-11 — COMPLETION CANDIDATES: rigorous status + mechanisms

Code: `completion_candidates.py`. Paper: Corollary 9.9 (sign dichotomy)
+ mechanisms paragraph added to §9.

### Corollary (sign dichotomy at every finite channel number) — RIGOROUS

For λ<0 the Theorem-9.8 frame decoupling gives confining branches
`p̂²/(2γΩ) + |λ|(k+cp_ν)⁴ + O(k²)` — each e.s.a. — plus the bounded
rotated channel-energy term (Kato–Rellich): every finite-channel
Galerkin model of the λ<0 quartic PU is essentially self-adjoint. So at
every M: indices (2M,2M) for λ>0, (0,0) for λ<0.
Verified: λ<0 wall spectra converge exponentially (matched drift 2.9e-8
at L 6→8, then 1.1e-13 at 8→10) — maximal contrast to the λ>0 sweep.

### Null-escape analysis: one confirmation, one falsification

Kinetic-form ratio on the escaping momentum (0 = null, 1 = definite),
tracked along actual blowup trajectories at amplitudes 1e2…1e5:
- PU λ>0 (deficiency case): 0.94 → 0.9997 — DEFINITE ✓ (as computed
  analytically: p_u ~ 24γAτ⁻⁵ dominates).
- Ghost pair λ<0: 0.066, 0.014, 0.021, 0.063 — NULL ✓ (diagonal escape,
  p₁² − p₂² ≈ 0): structural rationale for quantum completion (no
  definite-kinetic WKB transport along a null direction).
- **PU λ<0: 0.35 → 0.9998 — FALSIFIES the naive "completion ⇔ null
  escape" conjecture.** Mechanism identified: it climbs a RISING
  potential using negative kinetic energy while hugging u = −cv — i.e.,
  escapes through arbitrarily high mode-2 channels: exactly the channel
  tail the Galerkin models exclude. Two distinct completion mechanisms:
  null-direction escape (ghost pair) vs channel-tail escape (λ<0 PU),
  the latter more tail-sensitive.

### Valley-adapted drift test (λ<0 ghost pair) — verdict robust

Rotated (s,d) Fock bases aligned with the escape diagonal,
(ν_s, ν_d) ∈ {(1,1), (0.5,1.5), (0.3,2.0)}: drift ratios 0.16–0.45 in
all cases, interleaving the free (λ=0, e.s.a.) control's range
(0.09–0.30); nothing near the LC band (0.8–3.8). The completion verdict
is not a basis artifact.

---

## 2026-07-11 — THE M→∞ TAIL: no-compact-witness theorem, 1D certified,
## 2D reduced to fiber-vs-ridge

Code: `tail_certificate.py` (closure-defect diagnostic; original
certificate design corrected) and `glued_certificate_1d.py` (genuine
certificate). Paper: Proposition 9.11 + Remark 9.12 + status paragraph.

### The conceptual result (found by falsifying my own design)

**No compact witnesses.** For any symmetric operator on C₀^∞ and any
Im z ≠ 0, EVERY compactly supported smooth ψ lies in D(S̄), where
‖(S−z)ψ‖ ≥ |Im z|‖ψ‖ holds unconditionally. So no truncated, windowed,
or lattice-regularized function can ever witness deficiency — the
completion data lives entirely at infinity (the domain-side twin of the
S-matrix-at-infinity picture). Consequence: ALL truncation-based
diagnostics (drift, spectra, windows — everything we and anyone else
can run on finite data) are evidence in principle, never proof. My
first certificate design violated this and the numerics faithfully
enforced the bound (all ratios ≥ 1) — theorem as bug-detector.

### The genuine certificate (1D, machine-checked)

Glue WKB tails (only residual: the explicit remainder
a[q″/4q − (5/16)(q′/q)²]) to an exactly integrated interior, C¹ at the
junction: non-compact candidate in D(S*). Results:
- falling quartic (the PU fiber): ratio = **0.0011** ≪ 1 —
  **CERTIFIED not essentially self-adjoint** (von Neumann inequality
  violated by three orders of magnitude).
- confining control: left continuation contains a non-L² real
  exponential — no candidate exists (correct failure).
- falling quadratic (LP-marginal): growing branch polynomial k^{Z/1.12},
  non-L² for Z > 1.12 — no candidate (correct, sharp failure).

### The 2D status (closure-defect diagnostic + reduction)

Windowed 2D candidates measure proximity to the forbidden bound:
falling-channel class hugs it (all five λ>0 beam launches: 1.21–1.29;
1D LC control 1.22), e.s.a. class sits far above (1D confining 4.9;
2D λ<0 control **641**). Evidence-grade: λ>0 behaves LC-like, λ<0
e.s.a.-like, consistent with everything prior.

**Proposition (direct-integral).** The oscillator-free part
A = P̂_k²/(2γΩ) − T(k+cp₂) commutes with p₂: direct integral of LC
fibers, n±(A) = ∞ (rigorous). The full operator adds the transverse
oscillator — unbounded in this frame (Galerkin norms √Ω(M−½) → ∞):
the exact form of the tail question.

**The reduction.** The potential ridge p ≈ −k/c falls only
QUADRATICALLY (limit-point-marginal); fixed-p fibers fall quartically
(LC); beams drift ridge-ward at dp/dk = O(1). A 2D certificate needs
analytic beam tails under the ridge drift: **the fiber-vs-ridge
competition is the mathematical heart of the M→∞ question** — now
precisely what a specialist must resolve, with the 1D machinery
validated end-to-end as the template.

---

## 2026-07-11 — MASLOV FEASIBILITY STUDY: the 2D certificate is
## assembly, not new mathematics

Code: `maslov_feasibility.py`. Paper: feasibility paragraph added to §9.

### Setup insights (before computing)

- In the null-frame (s,w) coordinates the ray equations of the symbol
  reduce EXACTLY to the quartic-PU law s⁗ + γΩs̈ + γω̄²s = 4λs³: the
  escape-ray family IS the classical blowup, with universal amplitude
  S = √(30γ/λ) — a sharp numerical check.
- Time-reversal symmetry ⇒ rest-data rays are DOUBLY explosive (escape
  at both temporal ends) ⇒ the time-integral quasimode
  ψ = ∫e^{izt}φ_t dt has only e^{−Zt*} ≈ 1e-14 boundary terms.
- My earlier "ridge-drift obstacle" applied to artificial fixed-p beam
  launches; true rays don't drift off themselves — beams follow rays.

### Results (all criteria computed)

- **F1**: exponent −1.999; amplitude 24.546/24.547/24.547/24.545 vs
  √600 = 24.4949 (0.2% = finite-s harmonic correction), at four launch
  points, both time directions ✓. (Two numerical traps fixed en route:
  event-time ≠ true t* biases naive exponent fits — extract t* from the
  exact linear law 1/√s = (t*−t)/√S; and the Schur-complement
  transverse curvature is noise-dominated when Im M degenerates along
  the flow — use the second eigenvalue + flow-alignment check.)
- **F2**: Siegel positivity holds along the whole ray (min eig −7e-11 =
  numerical zero, null direction aligned with flow to 1.0000 — benign);
  transverse curvature stays positive (min 1.0e-4), strong terminal
  focusing (σ⊥ = 5.3e-3 at the escape end); zero caustics.
- **F3**: |det δq| ~ τ^{−3.1} ⇒ beam-norm integrand ~ τ^{3.1} → 0:
  N = 0.0824 at Z=6, converged. Anharmonic residual proxy
  η = |U_sss|σ³/(|U|+Z): weighted integral 0.026, decaying fast along
  the escape; η fails (peak 8.2e3) ONLY in a compact interior episode
  of transverse defocusing.

### Verdict

The escape-ray family supports L²-transportable Gaussian-beam tails
exactly where the certificate needs them (the asymptotic ends); the
single-Gaussian ansatz breaks only on a compact interior segment —
which is precisely what the validated 1D template handles by exact
numerical solution. **The 2D glued certificate architecture: numeric
interior (compact) + Gaussian-beam tails along the numerically known
rays + gluing where η is small. Remaining work is assembly and
quantitative error control, not new asymptotic machinery.** All beam
data (t*, S, curvatures, widths, det-exponent, N, η-profile) are
computed and reproducible for whoever assembles it.

---

## 2026-07-11 — FINAL AUDIT + SECOND REFERENCE SWEEP

Full read-through of main.tex (all ~1700 lines) + reference sweep for
the newest material. Findings, all fixed:

1. **Front matter staleness**: abstract and intro item 8 predated the
   last five results — extended to cover channelization + sign
   prediction, finite-channel stability + sign dichotomy,
   no-compact-witness principle, 1D glued-tail certificate, Maslov
   feasibility reduction.
2. **Formatting**: two `\end{figure} Text` jams (Secs. 6 and 7) fixed;
   local-notation note added to the terminal-indivisibility theorem
   (c, σ, p, q, r reused there); outlook updated to state the
   assembly-only reduction; remaining overfulls are 3.7pt and 0.6pt
   (sub-visible).
3. **Bibliography usage**: all entries cited ✓ (34 → 36 after sweep).
4. **Reference sweep finds**: (a) Ralston, MAA Studies in Math 23,
   206 (1982) — the standard Gaussian-beam citation, now cited in the
   feasibility paragraph; (b) **Fischer–Burgarth–Lonigro, J. Phys. A
   59, 255203 (2026)** (arXiv:2508.09044): deficiency indices of
   higher-order squeezing (polynomial-oscillator) operators, including
   cases where added terms RESTORE essential self-adjointness — an
   operator-theoretic precedent for completion-by-interaction, cited
   next to the Open Problem. Nothing found preempting the main claims.
5. **Authorship/AI disclosure**: "we" is the standard authorial
   convention (kept); an Acknowledgments section added disclosing
   extensive AI (Claude/Anthropic) assistance — user may rephrase.

Final: 25 pages, clean compile, submission-grade front-to-back.

### Program status

Sixteen results. Handoff to the physicist reviewer:
1. 2D certificate: architecture + all beam data supplied
   (`maslov_feasibility.py`); assembly/error-control remains.
2. Rigorous e.s.a. for the two completion candidates (λ<0 PU:
   channel-tail escape; λ<0 ghost pair: null-direction escape) —
   genuinely open, mechanisms identified.
- Paper: 25 pp., all claims labeled theorem / certified / evidence;
  review-ready.

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

---

## 2026-07-11 — NEW SESSION: migration + task recovery

Claude-project folder migrated (old DeleteMe-Physics folder →
C--Projects-IndivisibleGhosts native): memory identical by hash;
prior session transcript + 16 subagent logs copied and hash-verified
(34 files); task list #9–20 recovered VERBATIM from the on-disk task
store and recreated (new IDs 1–12). PUSH HOLD still active.

---

## 2026-07-11 — T2 DONE: measurement-chain simulation + 2-page
## photonic-coupler proposal (paper-1 Sec. 10a made concrete)

Code: `t2_measurement_chain.py` (~3 min, 400-trial MC per cell).
Document: `proposal/main.tex` (2 pp + refs, compiled clean).

**Device grounding (Klauck 2019, full-text read):** κ = 0.26 cm⁻¹
(L_c = 6.0 cm), γ = 0.13 ± 0.04 cm⁻¹ measured vs 0.2 DESIGNED (a
~35% loss-realization systematic, unremarked by the authors — banked
into our error narrative), loss via sinusoidal modulation
(Eichelkraut 2014), λ = 815 nm, ladder-of-lengths + per-sample
Hermitian reference + intensity-ratio normalization, HOM position to
0.05 cm, visibility 87±2%. **They ran at γ/2κ ≈ 0.25 — the broken
phase is unexplored for any process-level observable.** Mapping:
s→κ, sinθ→a=γ/2, t→z; broken iff γ>2κ.

**Proposed devices:** D1 (κ=0.10, γ=0.60; t_c=5.10 cm, floor
−0.583 cm⁻¹), D2 deep (0.15, 0.90; 3.40 cm, −0.874), D3 unbroken
control (0.50, 0.30; first window 1.55 cm, period 6.59 cm); ladder
z = 0.5…10 cm × 0.5. Loss range needed: 2.6–7.8 dB/cm power —
within the modulation technique's demonstrated span.

**Key estimator theorem-let (new, load-bearing for the proposal):**
the divisibility onset t_c = det-zero-crossing is estimated from
det of the COLUMN-NORMALIZED transfer matrix, which is exactly
invariant under per-launch calibration errors (det(ΓD) = detΓ·detD
> 0 preserves sign; normalization makes the interpolant invariant
too — verified 2e-14). So the primary observable is immune to the
dominant systematic of intensity experiments.

**Error budget (MC, noise = 2% disorder + 3% calibration + shot +
1e-4 dark):** t_c to ±0.15 cm at 1e4 photons/launch (±0.08 at 1e6;
dark floor bias +0.05 cm, subtractable). Floor: global closed-form
fit with calibration nuisances → ±3%, a 23–29σ detection of
permanent negativity at 1e4 photons; pointwise finite-difference
generator is NOT usable late-ladder (bias −13% at Δz=0.5 and
noise-fragile once survival ~ dark). Dissociation on one data set:
late-window conditional backflow ≤0.02 (broken) vs 0.48 (unbroken)
while floor >23σ negative — two-orders-of-magnitude margin. D3
window period recovered to ±2%.

**Two estimator defects caught by inline controls during
development** (methods ledger, same spirit as the five artifacts):
(i) the naive det-interpolation broke the claimed calibration
invariance (C4 caught it; fixed by column normalization); (ii) the
uncoupled-null control exposed dark-count leakage amplified through
the near-singular matrix inverse (C3 now quantifies it: |L12| 0.00
without dark, 0.065 with) — both now design guidance in the
proposal rather than silent flaws.

---

## 2026-07-11 — TASK 19 (dipole concordance): DONE — exploratory
## verdict: one frame in DIRECTION, a second axis in the local
## probes; amplitude excess is depth-dependent (bias-like)

Agent sweep, full report `research/dipole_concordance_report.md`
(20 arXiv IDs, honesty ledger of unverifiable items). Highlights:
- Boost-class estimators (NVSS+RACS 1.4°, CatWISE 27.8°, Planck
  aberration) CONCORD with the CMB apex in direction (joint chance
  ≲1e-5) but run 2–3× kinematic in AMPLITUDE (4.8–4.9σ each,
  contested down to ~2–3.6σ); the DEEPEST radio survey (MALS
  2408.16619) reverts to ratio ~1.0 — a depth-dependent-bias
  signature, NOT a two-frame signature (a frame cannot know survey
  depth). Foliation reading: direction–amplitude decoupling is the
  joint-view payoff.
- Class-II probes (Auger UHECR, Fermi DGB dipole, Migkas clusters,
  Pantheon+ low-z) do NOT concord (55–70° away) but cluster among
  THEMSELVES near (l≈260, b≈−15) — a second, local-LSS/bulk-flow
  axis, distinct from the foliation axis.
- For our phantom template: measured DGB dipole (6.5e-2, direction
  loose, single-group) is a 15–18× floor over our 3.7–4.3e-3
  kinematic signal; fixed-CMB-apex template fitting cuts leakage to
  ~5×; the 0.12% edge modulation is orthogonal to smooth
  astrophysical dipoles but far below LAT's ~10% energy resolution
  (COSI-class resolution changes this — feeds T3).
- RECOMMENDED TEST (fold into T3): fit the DGB dipole coefficient
  along the FIXED CMB axis as a function of energy and test the
  kinematic scaling (3+Γ(E))β — the aberration-style discriminator,
  feasible on existing Fermi-LAT data.

---

## 2026-07-11 — TASK 20 (horizons-as-Feller-boundaries scoping):
## DONE — verdict GO

Agent scoping search, full report
`research/horizons_scoping_report.md`. Gap map: the OPERATOR half
(horizon boundary conditions as self-adjoint-extension choices)
exists in pieces — Wald 1980 / Ishibashi–Wald (conservative dynamics
= extension choice; cite, never claim), hyperboloidal-QNM program
(dissipative horizon = non-self-adjoint generator), Balachandran+
1810.00020 (U(1) extension family as generalized brick wall, with an
extensions-are-thermally-equivalent lemma), 't Hooft antipodal =
S-matrix-at-the-horizon completion. The PROBABILISTIC half is
absent: zero hits on Feller exit/entrance/natural classification of
a horizon. Sharpest provable candidates: (1) the CLOCK-DEPENDENCE
THEOREM — horizon = natural boundary in Killing time (T=∞, limit
point, conservative minimal semigroup, no data needed) but EXIT
boundary in proper-time-adapted variables (T<∞, sub-stochastic
minimal semigroup), the flip being a singular time change by the
lapse — textbook Feller arguments, provable now; (2) membrane
paradigm = the minimal sub-stochastic process; unitary completions
= conservative dilations with stretched-horizon data; brick-wall
position dependence = extension dependence; (3) information paradox
as clock-indexed [data vs no-data]. Near-misses: Franchi–Le Jan
relativistic diffusion (right process, no classification),
Son–Teaney absorbing stretched horizon. Risk: HIGH on operator-only
claims, LOW on the Feller column. Recommended scope: one paper,
scalar field + radial diffusion, Rindler warm-up + Schwarzschild,
analogue-horizon discriminator section. → Queued as new task T10
(user decision whether to promote).

---

## 2026-07-11 — T1 STEPS 1+2 DONE: triage CLEAR; the trade-off
## THEOREM found and numerically established (dimer exactly extremal)

**Step 1 (triage, agent; full report
`research/t1_literature_triage.md`):** NOT PREEMPTED. The exact
TV-vs-survival trade-off is unposed anywhere: steering literature has
the HJW constraint but never this optimization; postselected-metrology
bounds (Arvidsson-Shukur 1903.02563, Combes-Ferrie-Jiang-Caves) are
Fisher-information-shaped (local), don't imply a TV bound; the whole
LHFL resolution chain never bounds the magnitude. Closest: Reeb-
Kastoryano-Wolf 1102.5170 (Hilbert-metric contraction) and Regula-
Lami-Wilde 2209.10550 (postselected discrimination exponents) — cite
prominently. Toolkit: HJW + SDP duality, Hilbert/Thompson metrics,
SLOCC normal forms.

**Step 2 scoping fact (3-line argument):** with ARBITRARY local
filters the static trade-off is trivial — orthogonal projector
filters give TV = 1 at every p ≤ 1/2. The content is DYNAMICAL:
semigroup contractions are invertible and |det C| =
e^{−∫tr(loss)dt} is a message-independent invariant (X-conjugation
preserves det). The right conserved quantity was hiding in paper 1's
det Γ bookkeeping all along.

**Step 2 result (`t1_region_sweep.py`): the theorem.** For any 2×2
contraction C on one arm of a Bell pair, messages (C, XCX):

    TV_quantum ≤ sqrt(1 − (|det C|/p)²),   p = survival
    equivalently  TV² + (|det C|/p)² ≤ 1   (Pythagorean form)

- Broken-PT dimer saturates EXACTLY, pointwise in t, at every s
  tested (|TV−bound| ≤ 1.3e-15); unbroken dimers saturate too
  (≤4e-13): the whole balanced-gain/loss family is extremal, not
  just the broken phase.
- 0/99,846 random lossy generators violate; min margin 3e-10
  (envelope approached, never crossed).
- The paper-2 beable observable is the DIAGONAL part: TV_cl(25)
  matches κ̃/sinθ to 6 digits at s = 0.3/0.5/0.65; TV_cl ≤ TV_q
  strictly — **the conditioned coherences carry the difference: the
  beable currency sees a strictly weaker conditioning signal than
  the quantum currency.**
- Proof sketch (to write): σ_i = M_i^T/(2p); ||M − XMX||₁ ≤
  2(μ₁²−μ₂²) by Rayleigh quotients (v†Mv ≤ μ₁², (Xv)†M(Xv) ≥ μ₂²);
  (μ₁²−μ₂²)² = 4p² − 4|det C|²; saturation iff X swaps M's
  eigenvectors (loss eigenframe X-antisymmetric = exactly the dimer
  geometry). Controls: Hermitian and X-symmetric-loss dynamics give
  TV = 0 to machine precision.

**Remaining for the T1 paper:** clean proof write-up; arbitrary
ρ_AB (Bell extremality); n-dimensional / unequal-p generalization
(Ky Fan); the classical-TV version's own bound; positioning vs
RKW/RLW per triage. Target unchanged: PRA/Quantum theorem paper.

---

## 2026-07-11 — T3 IN PROGRESS: integrated spectrum built; THE WEDGE
## (a real correction to the s4c edge statistics)

Code: `t3_cosi_forecast.py` (instrument constants pending agent
data). Redshift-integrated arriving spectrum
I(E) = (c/4π)∫dz j((1+z)E, z)/[H(z)(1+z)³]; controls: line-source
closed form 1.1e-5, local-slab limit 1.7e-3, near-edge wedge law
0.6%.

**RESULT (new, modifies how s4c's numbers apply to the cosmological
signal): cosmological integration converts the local STEP edge into
a WEDGE** — I(E) vanishes linearly at Λ (superposition of edges at
Λ/(1+z)); the endpoint stays exactly sharp (I≡0 above Λ) but
near-edge counts scale as (window)², not (window). Edge-window
fractions: ±2% window holds 0.081% of counts (wedge) vs 2.1%
(step) — ×26 penalty at 1% resolution, ×9 at 3%. GV age factor
(t², i.e. rate growing with cosmic age) mildly flattens the low-E
stacking, leaves the wedge intact. Endpoint-regression MC (s4c
style, 8 cosθ bands, quantile estimator): N_5σ(edge, wedge) ≈ 1e7
signal photons vs the step-shape ~1-2e6 — **the cosmological wedge
costs ×5–10 in counts for the edge observable; the dipole
(3.7-4.3e-3, N_5σ ≈ 2.7-3.7e6) is untouched.** Resolution 1% vs 3%
barely matters once the shape is a wedge (quantile statistics
dominate). Estimator slope bias ~−15% (quantile+smearing),
self-calibrating in a template fit; numbers are signal-only
(background dilution adds 1/f_s²). Note for paper 2 v-next: the
s4c edge numbers describe the LOCAL (z≈0-dominated) signal; any
integrated-background version must use the wedge statistics.

COSI forecast + Λ_max re-derivation await the instrument-data agent
(effective area, exposure, CGB levels, Cline 2023-24 overlap).

---

## 2026-07-11 — T3 DONE: the bound moved (3 → 18.8 MeV), the edge
## moved into the MeV gap, and COSI cannot reach it — an honest null
## forecast

Instrument/bound data: `research/t3_instrument_data.md` (agent,
42 sources). **Headline: the CJM 2004 bound is OBSOLETE.**
Cline–Puel–Toma–Wang (arXiv:2308.12989, PRD 108 095033) refit
vacuum → 2 ghosts + 2 photons with exact phase space against
COMPTEL: Λ ≤ 18.8 MeV (real scalar, 95% CL) — 6× weaker. Their
companion 2401.02958 confirms our flat-edge shape (dn/dE ∝
Λ⁷ Θ(Λ−E)) and independently states our redshift integral. No other
post-2004 update exists; COSI (launch 2027, 0.2–5 MeV, ~1% FWHM,
~1.3e8 cm²s/direction over 2 yr) is the only funded MeV mission
through ~2030.

**Forecast (`t3_cosi_forecast.py`, anchor: signal = CGB at
0.8×bound when Λ = bound, factor ~2 proxy):**
- At the current bound the edge sits at ~19 MeV — ABOVE the COSI
  band and inside the MeV sensitivity gap (0.3–100 MeV is 2–3
  orders worse than adjacent bands; no funded mission).
- In-band (0.2–5 MeV) signal fraction: f_s ≤ 2.5e-9 for Λ ≤ 3 MeV,
  1.6e-7 at Λ = 5, 2.2e-3 even at Λ = 18.8 (flat signal under a
  steeply rising CGB). With N_cgb ≈ 5.5e7 full-sky band counts,
  N_sig ≤ 1.2e5 at the bound: **the wedge edge (needs ~1e7 signal
  photons, /f_s² dilution) is unreachable at every allowed Λ.**
- The 21σ "dipole" on total counts is the kinematic dipole of the
  whole CGB — shared with comoving AGN, NOT phantom-specific
  (concordant with the task-19 finding). The discriminating
  observable was always the edge.

**Conclusions banked:** (i) paper 2 updated (two sentences: intro +
tests(b)) to cite the 18.8 MeV bound and note the edge now lives in
the MeV gap; recompiled, 21 pp. (ii) The citable phenomenology
statement for any future write-up: *the phantom spectral edge of a
bound-saturating ghost sector lies in the MeV gap; COSI closes
nothing in-band because Λ⁸ scaling makes sub-5-MeV cutoffs
signal-free; the edge territory (5–19 MeV) waits for a
newASTROGAM-class instrument* — plus the WEDGE correction to the
edge statistics (previous entry), which any MeV-gap mission
forecast must use. (iii) The dipole-mining recommended test
((3+Γ(E))β energy-scaling along the fixed CMB axis on existing
Fermi data) remains the cheapest kinematic-vs-intrinsic
discriminator for the CGB itself, independent of phantoms.
"The phantom menaced, twenty years on" as a standalone paper is
DOWNGRADED to a section-length statement: the honest content is a
null forecast + the wedge statistics + the gap statement.

---

## 2026-07-11 — T1 STEP 3 DONE: theorem set completed, paper 3
## DRAFTED (v0.1, 7 pp — audits pending)

Extended `t1_region_sweep.py` (tests T-E/F/G) + `paper4/main.tex`
("The price of a post-selected signal: a sharp
survival–distinguishability trade-off, saturated by broken-PT
dynamics").

**Theorem upgrades since step 2:**
1. GENERALIZED to effects: the bound needs no single Kraus operator —
   for ANY survival effect 0 ≤ M ≤ 1 with flip-related messages
   (M, XMX): TV² + (√detM/p)² ≤ 1. Projectors have detM = 0 →
   vacuous bound → correctly reproduces the trivial static case
   (TV=1 at p≤1/2); the inequality has content precisely for
   dynamics, where √detM = |detC| = e^{−½∫TrΓdt} is the dissipated
   weight.
2. SATURATION PROVED analytically: dimer Bloch computation gives
   M = e^{−2at}[(c²+(a²+s²)σ_h²)1 + 2ac·σ_h σz + 2as·σ_h² σy] —
   n_x ≡ 0 (numerics: exactly 0.00e0), X-conjugation antipodal ⇒
   equality at every t, every s, BOTH phases.
3. CLASSICAL bound proved (Prop): same RHS via M₁₁M₂₂ ≥ detM;
   extremal family = uncoupled loss (tanh²+sech²=1 identity,
   verified 2e-16); coupled dimer's classical deficit = its
   conditioned coherence; κ̃/sinθ situated as the classical shadow
   of a bound-saturating quantum signal.
4. GENERAL PURE INPUTS (Prop): TV ≤ √(1 − 2detρ_B√(detM₁detM₂)/
   (p₁p₂)) via qubit fidelity identity + Fuchs–van de Graaf;
   0/39,663 violations.
5. CONJECTURE REFUTED (kept in the paper per honesty policy): Bell
   state is NOT extremal at fixed (|detC|, √(p₁p₂)) — counter-
   examples exceed the Bell envelope by up to 0.80. The detρ_B
   dependence is real.
6. GENERAL DIMENSION (Prop): TV ≤ Σ|μ²↓−μ²↑|/(2TrM) via Lidskii +
   Schur convexity; 0/20,000 violations at d=3 and d=4.

## 2026-07-11 — PAPER-3 AUDIT CYCLE (three agents): v0.2, all
## findings applied; one theorem UPGRADED by the audit

**Bibliography agent:** 14/15 OK; RLW journal details verified by
direct web check (IEEE TIT 70, 3453 (2024) — restored; overrides
the triage's abstract-level "69 (2023)"); Bhatia pointer sharpened
to Thm III.4.1; Hübner attribution for the qubit fidelity identity
CONFIRMED correct (not Jozsa).

**Independent calc agent: ALL SEVEN CLAIMS PASS** from scratch
(fresh scripts, first-principles construction of Bob's conditioned
state incl. multi-Kraus decompositions — marginal depends only on
the effect, 6.7e-16; sympy symbolic proof of the dimer Bloch form
on both branches; Haar-random G at d=3,4,5; qubit fidelity identity
vs Uhlmann 2.6e-14; FvdG near-equality "violations" chased to
machine epsilon). Every headline script number reproduced exactly.
**And it caught a code-vs-comment factor-2 mismatch in T-F whose
resolution UPGRADED Prop 5.1:** the code was already testing the
stronger factor-4 bound — which turns out to be PROVABLE
(rearrangement + AM-GM gives Trσ₁σ₂ ≥ 2√(detσ₁detσ₂), so
F² ≥ 4√(detσ₁detσ₂)) and REDUCES EXACTLY to the sharp Bell-state
theorem at ρ_B = 1/2: the general proposition now interpolates to
the main theorem instead of being weaker by a factor 2.

**Adversarial agent:** 0 CRITICAL, 4 MAJOR, 12 MINOR — all fixed:
(1) Prop 5.1 purification bookkeeping corrected (polar
decomposition, unitary absorbed into effect relabeling wlog);
(2+3) factor-4 rewrite + numerics extended to fully independent
message pairs (0/39,460 mixed draws); (4) "deficit = exactly the
coherence" was FALSE as stated — replaced by the exact result it
gestured at, now Corollary (Pythagorean decomposition of the
signal): TV² = TV_cl² + χ², χ = |n_y|/p = 2|Im σ₀₁|, holds for
EVERY effect and flip pair (verified 4.4e-16) — a strictly better
statement than the error; (5) trial count corrected 1.6e5 → 1.8e5;
(6) d=3,4 now Haar+permutation relabelings, margins updated
(1.7e-6, 1.1e-6); (7) Prop 5.2 setup stated for general d;
(8) LHFL resolution history split correctly (Tang located the
signal; Brody/Ju restored consistency); (9) κ̃/sinθ qualified as
configuration-level at first mention; (10) experimental-proposal
pointer fixed (proposal/, not paper 1); (11) extremal rhetoric
tightened ("equality set n_x = 0; the dimer traces it
dynamically"; classical equality set strictly smaller);
(12) strict-deficit claim scoped to broken phase/t>0 (Rabi-node
exception); (13) σ_h → h (Pauli collision); (14) "dissipated
weight" → "accumulated total-loss factor"; (16) 0/39,460 count now
quoted in the manuscript.

Compiles clean, 7 pp. **Remaining before circulating (small):**
full-text read of RKW 1102.5170's postselected-distinguishability
section (triage called it the closest textual overlap; current
"appears never to have been answered" rests on abstract-level
triage), and the user's own read-through.

**Paper 3 status: v0.2, audit-clean.** Open problems recorded in
the draft: sharp general-input bound (extremal family at fixed
detρ_B), multipartite/CV, a trade-off for the coherence side χ of
the Pythagorean decomposition, and the suggestive detΓ/detM
connection to the paper-1 divisibility bookkeeping.

---

## 2026-07-11 — RKW FULL-TEXT READ: PARTIAL OVERLAP FOUND AND
## REPOSITIONED (v0.3) — the audit's last item, and it mattered

Full-text read of Reeb–Kastoryano–Wolf 1102.5170 (all sections +
appendices). **Finding: partial overlap — machinery, not
statement.** Our RHS is a Hilbert-metric quantity in disguise:
√(1−detM/p²) = tanh[h(M,𝟙)/2], and the core inequality is
DERIVABLE in three lines from their published Cor. 15
(TV ≤ tanh[h/4]) + projectivity of h + X-isometry + triangle
inequality. A one-line elementary Bloch proof also exists (both
conditioned states have Bloch radius √(1−detM/p²); flip pair =
antipodal at most). NOT in RKW: any statement trading
distinguishability against survival probability (their h mods out
normalization — their Thm 21 quantifies the probabilities away,
deliberately blind), any steering/bipartite-conditioned setup, the
invariant detM/p², the saturation/extremal analysis, the
decomposition. Their pointwise bound tanh[h(σ₁,σ₂)/4] is SHARPER
off the saturating orbit; ours is the sharp eigenvalue-only
(uniform) closure — and the two coincide exactly on the PT-dimer
orbit (m_x = 0), verified numerically by the agent.

**Repositioning applied (v0.3, 8 pp):** new Remark (Hilbert-metric
reading) states the debt precisely — contraction technology is
RKW's; the statement, the invariant, the operational reading, the
steering formulation, and the equality structure are ours; intro
and discussion claims softened from "never answered" to "never
posed as such, though assemblable from RKW"; the elementary Bloch
proof acknowledged. This is exactly the referee-vulnerability the
triage flagged, now closed on our terms. AUDIT CYCLE COMPLETE.
Remaining before circulating: user read-through only.

---

## 2026-07-12 — PUSH POLICY CHANGED (user) + repo scaffolding

New standing policy from the user: **commit AND push to the local
Gitea (the lab server) as we go — all commits and timing histories
live there; GitHub stays HELD until cleanup.** First Gitea push
done: c3ac721..5726f95 (the full session history).

Repo scaffolding (user-directed): created PUBLIC GitHub repos
`embeddetech/instantaneous-ghosts` (paper 2) and
`embeddetech/conditioned-ghosts` (paper 3) as NAME RESERVATIONS —
README stub only (title + series cross-link + AI-provenance note +
"content arriving"); no papers/scripts pushed, honoring the GitHub
content hold. Clarified for the record: paper 3 contains no ghost
physics (PT dimers/post-selection); "conditioned-ghosts" is series
branding — the conditioning door of paper 2's causality analysis,
priced. User may rename (GitHub renames preserve redirects).
Original paper-1 cover-art prompt recovered from the prior session
transcript; style-matched prompts for covers 2+3 handed to user.

---

## 2026-07-12 — PUBLISH PIPELINE PRE-STAGED (while cover art renders)

`publish/` added to the main repo: full READMEs for both paper repos
(copy-not-move policy settled with user: main repo = canonical
archive, papers cite it; paper repos = curated self-contained views
with COPIES), notebook excerpts (paper 2: QFT-bridge thread through
S1–S3 complete, 1,250 lines; paper 3: T1 entries through the RKW
repositioning), `assemble_repos.ps1` (dry-run verified: stages both
repos completely — 14 scripts + paper + excerpt for paper 2; 1
script + paper + excerpt for paper 3), and the v1.1 release
changelog note. Main README updated: series table (papers 1–3 +
proposal), contents rows for paper3/, paper4/, proposal/, research/,
and 17 new script rows. At hold-lift, remaining manual steps are
listed by the assembly script (banners, content push to the two
stubs, github main push, release swap, social previews).

---

## 2026-07-12 — T4 KICKOFF: the exceptional-point kinematics of
## quadratic/conformal gravity, quantified (t4_ep_dictionary.py)

Task: aim the trilemma at Mannheim's Weyl gravity ("conformal
gravity must choose"). Literature triage (agent) running; kinematic
leg computed first:

**Result 1 (per-mode EP scaling).** The PU first-order mode matrix
(one field mode of fourth-order gravity) has its exceptional point
at equal frequencies; the eigenvector-matrix condition — the cost
of ANY similarity dictionary at quadratic level (normal modes,
isospectral partner, BM map) — diverges as cond(V) = 2.00/delta
(fitted power -0.993 over five decades). Controls: far-from-EP
cond 6.8; at delta=0 numerically defective (no diagonalizing
similarity exists — Jordan blocks).

**Result 2 (the UV exceptional line).** Stelle-type dispersion
(w1 = k, w2 = sqrt(k^2+m2^2)): delta(k) ~ m2^2/2k -> 0, and the
measured cond(V) ~ k^5.0 decomposes honestly via a units-only
control (w1=2k, w2=k: k^3.0) into [variable normalization k^3] x
[EP-driven excess k^2.0 = (relative detuning)^-1, since
delta/k ~ (m2/k)^2]. **Massive quadratic gravity approaches the
exceptional line mode-by-mode in the UV with computable power;
conformal gravity (m2 = 0, the 1/k^4 double pole) sits exactly AT
the exceptional point for every k.**

**Result 3 (process-side control).** The Hermitian Ostrogradski
grid realization AT the EP: ||H-H'|| = 8e-15, Gamma = |U|^2 doubly
stochastic to 1.1e-14 — the stochastic-process description does
not see the EP (confirms paper-1 Sec. 5 at the field-kinematics
framing).

**Paper-shape statement forming:** Bender-Mannheim themselves
proved the equal-frequency PU has NO Hermitian counterpart
(0804.4190 — triage verifying). In our currency: no partner => no
metric-corrected process at the conformal point — the antilinearity
program offers conformal gravity no sample space even at FREE
level, and every mode is at the singular point of the dictionary.
The trilemma engages at tree kinematics, before any decay-rate
argument. Rate leg (part ii) awaits triage verdict on
agravity/GSTZ/Donoghue-Menezes prior art.

---

## 2026-07-12 — T4 TRIAGE VERDICT + RATE LEG SKELETON

**Triage (agent; full report `research/t4_literature_triage.md`):**
Part A PARTIAL-favorable: BM 0804.4190 verified verbatim
(equal-frequency PU "becomes a Jordan-block operator...
nondiagonalizable", "no Hermitian counterpart", unitarity claimed
via nonstationary states); Smilga contradicts IN PRINT ("unitarity
is broken in the equal frequencies limit"; infinite-order EP /
continuous spectrum, 1409.8450); Fring-Marquette-Taira Jan-2026
shows quantization still contested — a live standoff for our
currency to adjudicate. Part B: GSTZ DO treat 4-derivative gravity
but only Planck-suppressed ("cosmologically slow... gravitational
interactions only") and leave the true rate open; NO CJM-style
bound exists for the Stelle ghost; **pure-conformal lane CLEAR**
(dimensionless alpha_g, no Planck-suppression escape, no published
rate). Part C CLEAR: nobody states the trilemma; stochastic
language absent from the entire corpus (zero hits). Closest
neighbors: Deruelle+ 1202.3131 (Weyl ghosts vs LV = a two-horn
mini-trilemma via primordial GW), Hell-Lust-Zoupanos 2306.13714
(Maldacena boundary conditions insufficient), Ilhan-Kovner
1403.4664 (finite-time singularity — explosion-shaped).

**Rate skeleton (`t4_rate_ladder.py`, all controls clean):**
- Vertex parallel [ASSUMPTION, verification agent out]: Einstein
  M ~ T(1/(M_Pl²q²))T → |M|² ~ s²/M_Pl⁴ (reproduces CJM);
  Weyl M ~ T(1/(alpha_g q⁴))T → |M|² ~ 1/alpha_g² (s-flat,
  dimensionless).
- Reduced-integral slopes validate against paper-2 stage 3
  exactly (contact 2.000, CJM 4.000); the conformal vertex sits on
  the CONTACT rung: **rate/V ~ c_ps Lambda⁴/alpha_g² — the Planck
  suppression that made GSTZ call the gravity runaway
  "cosmologically slow" is structurally ABSENT in pure conformal
  gravity.**
- Horn-1 price (energy-density bound, method anchored on the
  phantom vertex: gives 108 MeV vs published 18.8 MeV — right
  direction, order calibrated): Lambda_max = (alpha_g² rho_cr /
  (t0 c_ps))^{1/5} ~ 1e-8 eV at alpha_g = 1 (20-METER cutoff
  wavelength), scaling alpha_g^{2/5} (even alpha_g = 1e-8 gives
  32-km wavelengths). **The Lorentz-violating-cutoff rescue, which
  leaves a phantom an MeV of headroom, leaves conformal gravity's
  ghost sector no laboratory-scale field content at all.**
  Conservative: any actual observational bound on ultra-soft
  injection would push Lambda lower still.
- Scope carried honestly: tree-level, multiplicity horn,
  flat-background Fock quantization — i.e. this is the price of
  HORN 1 specifically; horn 3 (BM zero-norm) evades by exiting the
  sample space (= our kinematic result); horn 2 = no coupled
  ghosts = no conformal gravity. "Conformal gravity must choose"
  now has all three horns priced.

Remaining for T4: vertex-convention verification (agent out);
quantum sector-level Jordan analysis (adjudicate BM-vs-Smilga in
the stochastic currency); assemble + draft + audits.

---

## 2026-07-12 — PROVENANCE-NOTE HARMONIZATION + LINK REWIRING
## (user-directed, all three papers)

(1) "Note on provenance" moved OUT of page 1 in all three papers:
now opens page 2 (after \newpage, before TOC/intro) so abstract
scrapers cannot ingest it. (2) Text standardized on paper 1's note
verbatim in papers 2+3, with one clause adapted: the originating
conversation / briefing / full notebook are "preserved in the
program's main repository" (they live in indivisible-ghosts, not
the per-paper repos). (3) Links rewired for the new repo layout:
paper 2 Code availability -> instantaneous-ghosts (+ main-repo
pointer for notebook/provenance); paper 3 Code availability ->
conditioned-ghosts (+ main-repo pointer); paper 3's Companion2
bibitem -> instantaneous-ghosts URL (paper 2's public home).
Recompiled: paper 1 28pp, paper 2 20pp (gained a page back),
paper 3 8pp; root PDFs refreshed.

---

## 2026-07-12 — T4: VERTEX VERIFIED, RATE CLAIM CORRECTED (the
## alpha_g fork), and the QUANTUM LEG DONE (BM-vs-Smilga adjudicated)

**Vertex conventions (agent; `research/t4_vertex_conventions.md`):**
VERIFIED — I_W = −alpha_g ∫ C² (Mannheim 1101.2186 Eq. 9),
propagator P₂/(2 alpha_g k⁴) (Eqs. 21-22), standard ½hT coupling,
and the 1/k⁴ verbatim as the degenerate two-pole limit (the Jordan
structure, in Mannheim's own equations). |M|² ~ 1/alpha_g² s⁰ stands
(the agent's own "Λ⁸/alpha_g²" line is a dimensional slip — E⁸ for
an E⁴ quantity — noted and discarded).

**CORRECTION to yesterday's rate entry (supersedes "for ANY alpha_g
within 8 decades of unity"):** no numerical alpha_g exists in print;
face-value flat-space matching to Mannheim–O'Brien fits gives
|alpha_g| ~ 3e109 (two routes agree; sign NEGATIVE), at which the
energy-density bound is VACUOUS (Λ_max ~ 5e7 M_Pl). The honest rate
statement is a FORK: (a) face-value branch — decay harmless, but
that same face-value theory fails solar-system tests outright
(Flanagan astro-ph/0605504, Yoon 1305.0163): the branch surviving
vacuum decay is already dead by other observations; (b) Mannheim
branch — he rejects the flat-space inversion, alpha_g is unfixed,
and any alpha_g within ~8 decades of unity forces macroscopic-
wavelength cutoffs (alpha_g = 1: Λ ~ 1e-8 eV ~ 20 m); his only
escape from both branches is the PT/zero-norm quantization, under
which the channel closes identically — which IS horn 3 (exit the
sample space). Trilemma closes either way. `t4_rate_ladder.py`
updated with the fork; slopes still validate (2.000/4.000/2.000).

**Quantum leg (`t4_jordan_process.py`, all controls clean):**
- LEMMA (3 lines, the paper's kinematic anchor): a Jordan-block H
  admits NO closed stochastic representation under ANY
  similarity — unitarity needs bounded ||V(t)||, Jordan gives
  ||e^{−iHt}|| ~ t^{k−1} (measured 1.000/1.999/2.997 for k=2/3/4),
  and similarity preserves unboundedness (exact inequality
  ||V||·cond(S)/||E|| ≥ 1 verified with margin). Detuned control
  saturates at ~2/delta ✓. Numerical remark banked: machine-eps
  perturbations split a Jordan block by eps^{1/k} — polynomial
  turns exponential for t ≳ eps^{−1/k}; the fragility is the EP
  physics.
- OPEN ROUTE VALID at the EP: contraction exact, Halmos unitary
  (1.4e-8, sqrtm-clip limited), reduced process sub-stochastic.
- **NEW MECHANISM for the taxonomy:** the pure Jordan (dipole-ghost)
  cell has TRIANGULAR |U|² — a one-way cascade in the beable
  currency — whose indivisibility enters through the divisor
  violating column-sum ≤ 1 (CONDITIONAL MASS CREATION, onset
  t_c ≈ 0.50) with entrywise nonnegativity intact: different from
  the dimer-EP negativity mechanism. The dipole ghost is a one-way
  conditioned cascade.
- ADJUDICATION of the published standoff: Smilga's "unitarity is
  broken" = the closed-currency Lemma; Bender–Mannheim's "unitary
  evolution via nonstationary states" = the dilation's
  survival-conditioned bookkeeping (open-system reading). Both
  right in different currencies; neither headline survives:
  no closed sample space (contra BM's framing), a perfectly valid
  open process (contra fatal readings of Smilga).
- Dictionary line: the Jordan t-term = fourth-order gravity's
  notorious per-mode linear perturbation growth = paper-1's EP
  polynomial class, realized everywhere in k-space.

T4 remaining: assemble the trilemma section (three horns, each
priced: horn 1 = the fork; horn 2 = no conformal gravity; horn 3 =
BM zero-norm = no sample space + our Lemma), draft, audits.

---

## 2026-07-12 — PAPER 4 DRAFTED (v0.1, 10 pp, pre-audit):
## "Conformal gravity must choose"

`paper5/main.tex` assembles the four T4 legs into the trilemma
paper: Sec. 3 kinematics (everywhere-EP, measured costs, process
side clean), Sec. 4 the no-representation Lemma + BM-vs-Smilga
adjudication + the one-way-cascade/conditional-mass-creation
mechanism, Sec. 5 the contact-rung rate and the alpha_g fork
(scoped explicitly as pricing the multiplicity/Dirac-norm reading
— the branch Mannheim rejects — which is the point of the fork,
not an oversight), Sec. 6 the trilemma Claim ("must choose — and
already has": the Jordan kinematics removes the definite-
configurations seat at the outset) + the escape-route table
(8 published routes, 3 horns, no fourth position). Discussion
grades every claim (theorem/measured/argued/conditional) and
states the Mannheim-side limits honestly (flat-space prototype
only; the field-theoretic S(x)/curved-background structure is not
constrained by the Lemma). Provenance note standardized on p. 2;
AI-contributions section notes the same-day alpha_g self-
correction. Bibliography 32 entries — several journal details
carried from agent reports and MUST be re-verified in the audit
(Smilga SIGMA details, Ilhan-Kovner IDs flagged by triage,
Donoghue-Menezes pairing, Anselmi fakeon citation structure,
Fring-Marquette-Taira 2601.20752, Mostafazadeh 1008.4678).
STATUS: draft v0.1 — needs the house three-agent audit cycle
before circulating.

---

## 2026-07-12 — PAPER-4 AUDIT CYCLE (four agents): v0.2 — the Lemma
## proof step was FALSE and the repair STRENGTHENED it; a root-cause
## fix propagated to PAPER 1

**Adversarial agent (the big one): 1 CRITICAL, 3 MAJOR, 8 MINOR —
all fixed.**
- F1 CRITICAL, exactly the step we aimed it at: the Lemma proof
  opened "unistochasticity requires V(t) unitary" — FALSE as a
  matrix statement (counterexample: (1/sqrt2)[[1,1],[1,1]] is
  singular yet |V|² is unistochastic). ROOT CAUSE INHERITED FROM
  PAPER 1 line 266 ("|U|² is doubly stochastic iff U is unitary" —
  only ⇐ holds). REPAIR (two lines, strictly STRONGER lemma):
  column-stochasticity of |V|² forces Σ|V_ij|² = n, so ||V||₂ ≤
  ||V||_F = √n bounded; Jordan growth unbounded; contradiction. The
  lemma now excludes even non-unistochastic closed representations
  and is consistent with paper 1's per-time-unistochasticity
  definition. Fixed in: paper 4 (statement+proof+new remark), Sec-2
  definition rewritten (no "iff"), t4_jordan_process.py docstring,
  AND paper 1 v1.1 ("iff"→"if" with the converse-fails
  parenthetical). Honesty ledger: the false step survived MY
  drafting and paper 1's four audit rounds; caught only when an
  agent was pointed at it BY NAME.
- F2 MAJOR: "every field mode" overclaimed vs Riegert's spin-1
  content — scoped to spin-2 in abstract+intro (body already had
  it).
- F3 MAJOR: the rate schematic put matter T at both ends — the
  physical channel (vacuum → ghost-graviton pair + photon pair) now
  named; alpha_g counting shown topology-independent; s-flatness
  now FORCED by scale invariance (no dimensionful parameter ⇒ any
  tree 0→4 massless amplitude is s⁰f(alpha_g)) — the conclusion got
  a better foundation than the defect had.
- F4 MAJOR: "no fourth position" undercut by our own Merlin row +
  missing metastability route — table gained a metastability/benign
  -ghosts row (GSTZ + Salvio 1902.09557: "disputes the premise, not
  a horn"), caption honestly hedged ("none we can identify; closest
  candidate is the Merlin route").
- Minors: Halmos 1.4e-8; Λ_max ~5e7 M_Pl; REDUCED wavelength 20 m
  (physical ~130 m); c_ps/ρ_cr/t₀/σ_max/unistochastic/K_μν all
  defined; Mannheim's replies to Flanagan (PRD 75, 124006 — web-
  verified) and Yoon now cited alongside the critiques (fork text:
  "or, if Mannheim's rebuttals stand, one is on the other branch");
  ρ_cr-is-maximally-generous clause added; reduced-measure slopes
  moved Theorem→Measured; O(1) factor on the dictionary lower
  bound; PT-side anticipated reply added to Sec 4.1 (their inner
  product conserves probability — agreed, and that norm choice IS
  the third seat).

**Bibliography agent: 11 fixes** — 2 chimera citations dissolved
(Mostafazadeh: two papers fused; Mannheim2015: three papers fused —
correct target is his Comment-on-Yoon PRD 93, 068501, and both
body claims survive on it); Smilga 1409.8450 real title
("Exceptional points of infinite order give a continuous
spectrum", IJTP 54, 3900); FMT real title; false DM quotation
de-quoted; "survives the classical limit" traced to a THIRD
Anselmi paper (1809.05037, added); Smilga quote scoped to the
nonstandard realization; Deruelle → HLZ for the linear-growth
attribution; Yoon=Newtonian-limit / Flanagan=light-bending split;
GSTZ title is HYPHENATED ("meta-stable?") — verified directly,
fixed here AND in paper 2 (had survived all prior audits); missing
arXiv IDs added; 3 uncited bibitems now cited; Ilhan-Kovner
1301.4879 attribution re-verified directly (IS Ilhan-Kovner; the
triage's doubt was wrong).

**Independent calc agent: A–H ALL PASS**, with analytic upgrades
folded in: the 1/δ scaling DERIVED (non-generic unfolding —
eigenvalue splitting exactly linear, eigenvector angle ∝ δ with
angle/δ = √5/2; generic perturbations give √δ), σ_max = t/2 +
√(1+t²/4) closed form, prefactors → 1/(k−1)!, mechanism dichotomy
double-confirmed (dimer-EP negativity at t≈0.70 vs PU-cell
provable nonnegativity — now cited in text), units control robust
to frequency ratio, fork arithmetic exact to all digits.

**Threads scout:** report in `research/t4_threads_report.md`.
Top: sector-resolved lemma at Smilga's infinite-order EP (in-window
strengthening); paper-5 arc = phase-boundary unfolding + divisor-
mechanism classification ("secretly one theorem"); photonic at-EP
device (γ=2κ) added to the T2 proposal as the first lab observable
of conditional mass creation; FMT adjudication paragraph; trilemma
registry as repo infrastructure; alpha_g standalone note DROPPED
(defenseless alone).

**Paper 4 status: v0.2, 11 pp, audit-clean. Remaining before
circulating: the optional in-window strengthening (sector-resolved
lemma — user decision), and the user read-through.**

---

## 2026-07-12 — PROCESS-HISTORY SIDECARS CREATED (user-directed)

`histories/` added: per-paper audit-trail documents (README +
paper1..4-history.md) — full timelines, errors-and-misses ledgers
with the CATCHING MECHANISM named for every item, prior-art events,
audit rounds, human steering. Assembled from notes.md, git history
(incl. the Gitea pre-release-history branch), this session, and the
research reports; a transcript-mining agent is recovering
fine-grained timings and the 16 subagent invocations of the
papers-1/2 session for an appendix. Purpose per user: data for
analyzing the AI-led research process itself (candidate meta-paper).
Program-wide ledger as of today: 6 caught artifacts, 1 retraction,
2-3 downgrades (counting convention noted in paper-2 history), 1
false proof step present in two papers (caught by aimed adversarial
audit), 2 chimera citations, 1 false quotation. Pattern worth the
meta-paper: every serious error fell to a mechanism DESIGNED to
catch it; generic passes repeatedly missed what aimed passes hit.

**Histories appendix landed:** transcript mining recovered the full
26-hour papers-1/2 session (13 phases, 16 subagent launches in four
waves, ~85 steering events, all 10 error events WITH their
detectors, 7 audit rounds, complete publication register;
UTC = local+5 verified against the user's own squash remark).
Ledger upgrades from the tape: artifact 2.5 (split-step) was caught
by THE USER ("still running?"); the user also caught a Gitea
over-squash at 15:29 UTC — two human-detector events the notebook
had not credited. Appendix: histories/process_timeline_papers12.md;
paper-1/2 histories enriched with verified anchors. Known gaps
stated in histories/README (overnight fine grain; squashed-commit
timestamps; one compaction + one context loss).

---

## 2026-07-12 — T4 IN-WINDOW STRENGTHENING DONE: the sector tower
## (paper 4 v0.3)

The threads-scout top pick, executed. `t4_sector_tower.py` (all
four checks clean) + new Sec. "From the mechanical prototype to the
Fock tower" in paper 4:

**Proposition (sector tower).** One-particle Jordan pair A = w+N
(the equal-frequency PU cell) second-quantizes to a SINGLE Jordan
block of size M+1 in every M-quantum sector: dGamma(N) is a
weighted shift, (dGamma(N))^M != 0, (dGamma(N))^{M+1} = 0, geometric
multiplicity 1 (verified M=1..8; growth exponents fitted
1.000/2.000/3.999/5.999/7.999). The secular DEGREE is unbounded up
the tower — the constructive form of Smilga's infinite-order EP
(1409.8450), now with the block sizes explicit. No truncation
escapes; each level makes it worse.

**Theorem (no bounded dictionary on the Fock tower).** For H =
dGamma(A) and ANY bounded-invertible S on the l2 configuration
space, |S e^{-iHt} S^{-1}|^2 cannot have unit column sums for all
t. Proof: unit column sums force ||V(t)e_j|| = 1; a duality
argument (the v-coefficient functional composed with S^{-1} cannot
vanish on a basis) plants some basis vector on the growing Jordan
direction; the u-coefficient grows linearly; contradiction.
Numerically demonstrated on a truncated tower: max_j ||V e_j|| =
7.5e3 / 3.1e7 / 1.3e11 at t = 5/20/80 under a random bounded S.

**Control:** diagonalizable one-particle matrix at the SAME
degenerate frequency: every sector exactly unitary (2.2e-16) —
degeneracy alone is harmless; the Jordan pair kills the tower.

**Consequence for the paper:** the weakest stated caveat
("mechanical prototype only") is retired; the no-representation
statement now covers the free flat-space Fock tower of every
conformal mode for any bounded metric. Remaining honest limits:
interactions, curved backgrounds, the S(x) sector. Abstract,
discussion tiers, and code availability updated; v0.3. NOTE: the
new section is POST-AUDIT — it should get a focused verification
pass (the two proofs + script) before circulation, though both
proofs are three-liners.

**Sector-tower verification pass (agent): PASS on all items, with
upgrades and three text fixes applied (paper 4 now genuinely
v0.3-audit-clean).** Upgrades: symbolic proof extended to M=10;
exact corner element M!; char poly (x−Mω)^{M+1}; the repo helper
verified correct even on the generic-complex branch the paper never
uses; the theorem chain verified with the actual seed-7 constants
(j*=19, |a|=0.414). Fixes: the theorem parenthetical claimed
e^{−iHt} "defined everywhere" — FALSE (sector norms grow
exponentially in M at fixed t; now stated correctly as sector-wise
dense domain, with the unboundedness noted as a fact); functionals
now explicitly extended-by-zero with the sector-projection argument
spelled out; c defined; the control bound "≤2e-16" was falsified by
its own 2.22e-16 artifact — reworded to machine epsilon; "every
level" → "every level M≥1". Ledger note: a bound falsified by one
machine epsilon is the smallest error this program has recorded;
it still counts.

---

## 2026-07-12 — T5 STAGE 1: the quantum channel-ladder test is
## RUNNING, and the first pass CONFIRMS multiplicity at weak coupling

**Overlap check (agent; `research/t5_overlap_check.md`): CLEAR.**
Deffayet 2604.21823 = 2-dof QM with confining coupling (pure point
spectrum — no decay channels BY CONSTRUCTION; their vacuum is an
integral-of-motion ground state, not free-Fock); Ewasiuk-Profumo =
bounded interactions (excludes phi²chi²); all multimode ghost
numerics in print are CLASSICAL. Method precedents to cite: Lagnese
2107.10176, Abel-Spannowsky-Williams 2506.17388 (false-vacuum MPS),
Burshtein-Goldstein 2410.21941 (FGR-onset methodology in discrete
modes — PARTIAL, normal photons, excited-state decay, no channel
sweep). Either T5 outcome lands in live territory (Deffayet-camp
"stability is interaction-structural" vs GSTZ "metastable escape").

**Stage-1 ED results (`t5_channel_ladder.py`, sparse Krylov,
m=1, L=8, cap 4, P=0 sector, dims 55-594):**
- Channel census: resonant 4-particle channels grow quadratically
  (10/21/36/55 at M=2..5) — the ladder is real in the spectrum.
- **Exact evolution TRACKS the channel-sum (1st-order PT)
  prediction: ratio 0.999→0.995 (t=20) across M=2..5 at
  lambda=0.02.** No structural suppression at the percent level
  while channels grow 5.5x.
- Constant-transfer M sweep (lambda rescaled so perturbative
  transfer is fixed — isolates channel-structural effects from
  back-reaction): residual trend −0.15%/mode-count-step at t=40
  (0.9950→0.9904) — consistent with cap-boundary truncation;
  MUST be pinned by the cap control before any claim.
- Coupling sweep: deviations scale with lambda at fixed M (0.999 →
  0.039 across lambda 0.005→0.32) — ordinary unitarity
  back-reaction, not channel physics.
- Controls: lambda=0 exactly zero; NORMAL twin: 0 resonant channels
  (census sign bug caught and fixed — it had hard-coded the ghost
  sign; dynamics was always right: virtual-only, 1.8e-5), cap 4→6
  at M=2 shifts N(40) by 6.7% (bounded).

**Traps adopted from the overlap agent as REQUIRED controls for
stage 2:** T3 (occupation caps mimic a confined/Deffayet-stable
ghost and can FAKE metastability — show cap-independence of the
short-time rate, cap 4/6/8); T4 (validate the golden-rule window:
rate vs level spacing, pre-recurrence, per Burshtein-Goldstein);
T6 (detuned-cutoff control: sweep the cutoff with UNEQUAL masses so
new modes are off-resonance — rate must NOT grow: separates channel
count from UV content); T1 (state the vacuum choice explicitly:
positive-norm/negative-energy free-Fock, the GSTZ framing —
Deffayet's integral-of-motion vacuum does not exist for phi²chi²).
Stage 2 also: box test (L and M scaled together), golden-rule-window
rate extraction, then the MPS/32-site stage.

---

## 2026-07-12 — T5 STAGE 2: trap controls run — and the data
## CORRECTED two of my own pre-run expectations (the important kind
## of session)

`t5_stage2.py` (cap-6 dims to 3,913; cap-8 at M=2). Honest read:

**[T3] cap independence — EXPECTATION CONTRADICTED.** I predicted
the fixed-transfer ratio deficit would shrink with cap (truncation
artifact). MEASURED: non-monotonic in cap (ratio(t=40) at M=2:
0.9950 cap4 / 0.9324 cap6 / 0.9603 cap8) and the M-trend GROWS with
cap (0.0083 cap4 → 0.0326 cap6, M=2→4). Physics: opening deeper
Hilbert space turns on second-order self-energy shifts that detune
the exactly-resonant shell; the cap-alternation suggests convergent
level-shift physics rather than runaway suppression — but
**distinguishing (a) renormalized-PT-restorable detuning from (b)
incipient GSTZ structural suppression is now THE stage-3 question,
and it is exactly the falsification test working as designed.**
Script's pre-baked conclusion line replaced by the measured facts.

**[T4] diagnostic design flaw (mine):** the short-window t²-fit
picks up off-resonant contributions (fitted coefficient exceeds the
resonant-shell sum increasingly with M, up to 40%); the stage-1
full-PT-curve comparison is the valid statement; T4's coefficient
table is diagnostic-flawed, noted, to be redone with an
intermediate-window fit in stage 3. t_Rabi window values (90-180)
confirm the times used are safely pre-Rabi.

**[T6] detuned control: mechanism CONFIRMED, my "flat in M"
phrasing was sloppy.** Zero resonant channels at every M; transfer
~40x below equal-mass; residual growth with M = the 1/k UV decay of
mass detuning (modes re-approach resonance — the ED echo of the T4
UV-exceptional-line result). Equal-mass growth is channel physics,
not UV content. ✓

**[BOX]:** dynamical transfer/L roughly stable (two larger boxes),
but S_ch·L GROWS with the tower at fixed cutoff — the
finite-volume shadow of paper-2's instantaneity (super-extensive
channel sum). Naive extensivity expectation wrong as printed;
corrected.

**Stage-3 plan (the decisive block):** (i) renormalized PT — recompute
the channel-sum prediction with second-order-shifted energies (or
exact 2-level per channel) and test whether the cap-6 deficit is
restored (verdict (a)) or persists (verdict (b)); (ii) λ-scaling of
the deficit at fixed (M, cap) — self-energy detuning predicts a
definite power; (iii) cap convergence to 8/10 at M=2-3;
(iv) intermediate-window rate extraction; (v) then the MPS stage.
For the histories ledger: two pre-run expectations contradicted by
data and corrected in-script, same hour.

---

## 2026-07-12 — T5 STAGE 3: VERDICT (a) — MULTIPLICITY SURVIVES AT
## THE RENORMALIZED LEVEL. No structural suppression at ED scale.

`t5_stage3.py` — the Schur/Feshbach test: P = vacuum + full
degenerate shell, Q folded exactly via
H_eff = PHP − PHQ(QHQ)^{-1}QHP (static, E0 = 0), evolved and
compared to the full exact dynamics on the shell-population
observable.

**[i] The verdict table (lambda = 0.02, t = 40):** full/Schur =
1.0000/0.9997/0.9993 (cap 4, M = 2/3/4) and 0.9998/0.9984/0.9963
(cap 6) — while full/naive drops to 0.8964. **The entire
beyond-leading-order deficit is folded-space self-energy physics;
the channel-sum rate is correct once standard renormalization is
applied.** (minQgap got small, 0.02-0.04 at cap-6 M=3-4 — the
static folding still closed at the 0.4% level.)

**[ii] Lambda scaling:** naive deficit 0.0057/0.0227/0.0883/0.3144
across lambda = 0.005..0.04 — ~x4 per lambda-doubling, i.e.
lambda^2-dominated at small coupling: the leading naive deficit is
wave-function renormalization (O(lambda^2) population leaking to
Q-space, Z < 1), with the (dE t)^2 ~ lambda^4 detuning taking over
at larger lambda. Both standard renormalization physics. The Schur
column stays at 0.0001-0.0069 THROUGHOUT — including where naive
misses by 31%.

**[iii] Cap convergence (M=2, caps 4/6/8/10, dims to 2568):**
full/Schur flat at 0.9998-1.0000; naive wobbles and converges
(~0.956 by cap 10). Cap-independence of the renormalized statement:
the trap-T3 worry (caps faking metastability) is closed.

**T5 headline (stages 1-3):** the quantum channel ladder is real,
extensive-in-channels, and its multiplicity scaling survives full
nonperturbative evolution once standard self-energy/wave-function
renormalization is applied — no sign of the GSTZ structural
suppression down to 0.4%, across a 5.5x channel sweep, caps to 10,
and couplings spanning naive deficits up to 31%. **The
falsification test came back: papers 2 and 4's load-bearing premise
holds at ED scale.** Honest scope: 1+1d, <= 10 modes, cap 10,
static Schur; the infinite-channel/resummation question (the true
boost-orbit limit) remains analytic territory — what T5 shows is
that finite-channel QUANTUM dynamics contains no mechanism that
erodes the channel sum beyond textbook renormalization.

Remaining for T5: MPS/32-site stage (larger volumes), the
intermediate-window rate extraction, born-vacuum growth signature,
then drafting (this is paper-5-or-6 material; the threads-scout
paper-5 arc may absorb it or it stands alone — user decision).

---

## 2026-07-12 — T5 STAGE 4: rate window, born-vacuum mechanism,
## d=2 spot check

`t5_stage4.py` (M=8, L=16, dim(P=0)=2185; d=2 mini-grid dim 229).

**(A) Proper rate extraction — the two-component structure
CONFIRMED.** Gamma(t) = −dlnP/dt fits a + b·t on t∈[4,30]:
b = 4.28e-5 vs prediction 2·S_exact = 4.53e-5 (6%); a = 2.03e-4 vs
FGR plateau 1.56–1.84e-4 (within the smoothing-width spread). The
honest finite-volume statement: coherent degenerate-shell component
(slope = 2S_exact) + quasi-continuum golden-rule plateau (= smoothed
channel sum). Window t in (1/bandwidth ~ 1, t_Rabi ~ 210) validated.

**(B) Born-vacuum signature — mechanism SHOWN, my narrative line
corrected by the data (ledger item).** With unequal masses the
detuning dies as 1/k, so channel density per unit detuning DIVERGES
toward resonance: the 2pi/t window captures ever-denser channels as
the state ages — the rate is SUSTAINED (flat through t~40, N(t)
still climbing at t=120) and then COLLAPSES when the window
exhausts the finite-M cutoff (N_open: 471→7 across t=5→120). That
is the GV born-vacuum mechanism + CJM regulator in ED. The log-
GROWTH of the rate itself is unresolvable at M=8 — stated honestly;
needs much larger mode counts (see compute discussion). My printed
"rate grows" narrative overstated; fixed in-script same run.

**(C) d=2 spot check — verdict (a) HOLDS off the d=1 line.** 2d
mode shell {−1,0,1}²\0, 48 resonant channels: full/naive = 0.9989,
full/Schur = 1.0000. Mechanism (renormalized multiplicity)
dimension-robust; the d=2 log-RUNG scaling needs a cutoff sweep
beyond laptop ED (flagged as the compute-limited frontier).

MPS 1+1d volume extension: next block (TEBD, position space, free
vacuum via imaginary time on the sign-flipped auxiliary H — design
in place; the sign enters real-time evolution only).

---

## 2026-07-12 — T5: THE DIMENSION LADDER OF THE QUANTUM CHANNEL SUM
## (channel-table scan; pre-registered, incl. a correction of my own
## statement one message earlier)

`t5_dimension_ladder.py`. PRE-REGISTRATION NOTE (ledger): in
conversation I had claimed "d=1 saturates, d=2 is the log rung" —
WRONG, corrected in the docstring BEFORE the first run: the
EXACT-resonant shell saturates in d=1, but the golden-rule channel
sum grows logarithmically there (the near-resonant density IS the
boost-orbit volume; GV's D=2 = 1+1d), and d=2 carries the ~Lambda^2
power rung (paper-2 energy ladder 2(d-1)).

**[C1] Coupling calibration:** analytic channel couplings
(g = lambda/(V sqrt(w1w2w3w4)), 1/sqrt2 per identical pair) match
the exact Hamiltonian vacuum column to 5.7e-16 (88 + 292 channels at
M=4,6). The channel table is exact, so the scan needs no Hilbert
space — O(M^3) enumeration to M=256 (d=1) / shell-8 (d=2) on a
laptop.

**[P1] CONFIRMED:** d=1 exact shell S_res saturates (last doubling
+1.5% at Lambda=100).
**[P2] CONFIRMED (log class):** d=1 Gamma_FGR grows with power-fit
exponent 0.156 (<<1), linear-in-ln slope 2.56e-4/ln over Lambda =
3-100; increments per doubling still decaying slowly — consistent
with log-class growth approaching its asymptote; a larger-Lambda +
eta-scaling analysis is the refinement (the lab server job). This is
Garriga-Vilenkin's D=2 log measured from QUANTUM-calibrated channel
tables — and it dovetails with paper-2 closeout's causal-cap
version (slope = I_s).
**[P3] CONFIRMED:** d=2 power-fit exponent 2.263 vs predicted ~2
(threshold steepening at the small-Lambda end, as in the paper-2
d=3 closeout where 4.3 -> 4.1; expect drift to 2 at larger
Lambda — the lab server job).
**[C3]:** extensivity within 7% under volume doubling.

**The T5 arc now states, in quantum-dynamics-anchored form, paper
2's central kinematic object:** the finite-volume rate has a
saturating coherent piece (the degenerate shell) plus a golden-rule
piece that grows with the cutoff exactly as the reduced-measure x
orbit factorization predicts: log at d=1, power at d=2 — and the
stage-3 Schur result guarantees the dynamics actually delivers
these channel sums (renormalized, verdict a). Remaining T5 queue:
the lab server validation ladder (M=12-14 exact, cap-6, d=2 shell-2
Schur, larger-Lambda ladder refinements), 32-site MPS locally, then
drafting.

---

## 2026-07-12 — T5 CAMPAIGN LIVE ON EMBEDSERVER2

SSH access established (Windows Server, i9-14900KF, 64GB — 42GB
free at start; scipy upgraded 1.14→1.17.1 to clear numpy-2.4 skew).
Polite-tenant protocol: campaign runner sets its own priority to
BELOW_NORMAL via ctypes; incremental flushed result files; jobs
detached (survive disconnect — verified).

`t5_campaign.py` shipped with two job types: ladder_ext (extended
dimension-ladder channel tables, d=1 to M=1024 with 5-eta smoothing
sweep; d=2 shells to 16) and val (lean momentum-class-streamed H
build + exact evolution + naive/Schur ratios).

**First results within minutes:**
- val M=10 cap4 (L=16, dim P=0 with |shell| = 231): full/naive =
  0.8959, **full/Schur = 0.9951 — verdict (a) extends to M=10**
  (at the larger volume the naive deficit deepens to 10% while the
  renormalized prediction stays within 0.5%).
- ladder_ext streaming: d=1 through M=512 (Lambda = 201): S_res
  saturated (3.68e-5, +0.75%/doubling); Gamma_FGR still climbing in
  the log pattern at every eta (5-width sweep for the asymptotics
  analysis when the run completes).
- Queued: val M=12 cap4 (PID 31824), val M=6 cap6 (PID 7980).

---

## 2026-07-12 — T5 CAMPAIGN WAVE 2 (the lab server): verdict (a) at
## M=16 and at full cap-6 depth

- **val M=16 cap4: full/naive = 0.7737 — a 23% naive miss — and
  full/Schur = 0.9924** (|shell| = 561, |Q| = 15,416 sparse-LU
  fold). The strongest single point in the campaign: the
  renormalized channel sum holds where naive loses a quarter of the
  rate.
- **val M=6 cap6 (deep Hilbert, sparse Schur): full/Schur = 0.9884**
  with the complete |Q| = 22,056 fold (169 s). The stage-2 worry is
  fully closed at cap 6.
- val M=8 cap6: build (82,065 states, 412 s) and evolution (64 s)
  fine — naive 0.8620, |shell| = 1001 — but the Schur step died
  silently: OOM signature (LU fill-in stacked on two concurrent
  jobs). Ledger: infrastructure failure, not physics; patched to
  chunked RHS solves and retried SOLO.
- Ratio summary across the campaign so far (full/Schur): 1.0000,
  0.9997, 0.9993, 0.9998, 0.9984, 0.9963, 0.9951 (M=10), 0.9941
  (M=12), 0.9924 (M=16), 0.9884 (cap-6 M=6) — a slow drift worth
  one honest sentence in the paper (static-E0 Schur approximation
  degrading mildly as the fold deepens; the naive column over the
  same span: 0.995 → 0.774).

MPS status: G1 gate FAILED first pass (TEBD 2-4x hot + baseline
offset — first-order Trotter + unconverged imaginary-time vacuum
suspected); per house rules no production MPS runs until gates
pass. Upgraded to second-order Trotter + annealed vacuum prep +
exact-state-injection diagnostic (G0/G1-iso) — running.

---

## 2026-07-12 — T5 MPS: GATE PASSED (after a three-defect forensic),
## production ladder launched; M=8cap6 saga continues

**The MPS gate story (ledger material, full mechanism-attribution):**
G1 failed at first pass (TEBD 2-4x hot, offset 1.7e-3). Forensic
decomposition via targeted controls: (1) G0 (state-prep isolation):
imaginary-time vacuum unconverged — FIXED by annealed 2nd-order
prep; post-fix overlap with the exact ground state = 1.00000000,
energy exact to 6 decimals. (2) First-order Trotter — upgraded to
2nd-order sweeps. (3) Residual constant offset 3e-4 proved
dt-independent AND chi-independent — which exonerated the physics
engine and convicted the TEST HARNESS: the ED reference measured a
ONE-bond observable window while TEBD measured two. Fixed the
harness. **G1 now passes at diff 2-6e-6 — three orders below
signal.** Ledger lesson: two real defects and one harness bug, each
isolated by a control designed to distinguish it; the harness bug
was only findable because the invariance checks cleared everything
else.

**Production ladder launched** (detached, BelowNormal): E1 lambda=0
floor, E3 normal twin, E2 volume sweep L=16/24/32, E4 coupling
scaling, chi=64 spot check. ~2h wall.

**M=8 cap6 (server) attempts 3-5:** attempt 3's diagonal-shift
renPT returned full/renPT = full/naive EXACTLY — the diagonal
self-energies are negligible at this coupling, consistent with
stage-3's lambda^2 (not lambda^4) deficit scaling: **the Schur
fold's work is done by COUPLING (vertex) renormalization, not
energy shifts** — a sharper mechanism attribution than stage 3 had.
Attempt 4 (vertex-corrected renPT2, one sparse matvec) died
mid-evolution (transient memory collision with the server's day
job; second silent kill). Attempt 5 running with phase
CHECKPOINTING (H saved to disk after build — deaths no longer cost
the 8-minute build).

**M=8cap6 CLOSED (attempt 5, checkpointed, completed):**
full/renPT2 = full/naive = 0.8620 exactly — the vacuum-column
vertex correction is ALSO negligible. By elimination (diagonal
shifts ~0, vertex ~0, full fold works at 3 exact points), the
fold's operative piece is the SHELL-SHELL block: second-order
interactions SPLIT the degenerate shell, detuning it from the
vacuum. Mechanism chain now: deficit = degenerate-shell splitting
(+ leakage Z-factor), captured only by the full Feshbach fold.
Prediction ledger: my "vertex ~0.98" prediction FAILED — recorded.
Full fold at |Q|=81k infeasible on shared 64GB (LU fill); the
three exact-fold points (0.9884-0.9998) + the mechanism
elimination chain are the record. Item closed.

---

## 2026-07-12 — PAPER-4 REPO NAMING + COVER-ART PROMPT (user-directed)

Confirmed for the record: paper 4 is fully ghost-literal (the
dipole/degenerate ghost IS its subject), unlike paper 3 where the
name is series branding. Repo-name candidates offered:
degenerate-ghosts (recommended: the equal-frequency degeneracy is
the mechanism), exceptional-ghosts, dipole-ghosts. Decision
deferred to the user post read-through.

Cover-art prompt (chalkboard series style, banner aspect) handed to
user; visual anchors chosen to encode the paper's four results: twin
ghosts merging at the "equal frequencies -- exceptional point"
(kinematics), the fused nondiagonalizable ghost climbing
growing blocks "t, t^2, t^3" (sector-tower lemma), three doors --
priced Lorentz door (20-m cutoff tag), bricked no-ghost door,
glowing ghost-shaped exit (the trilemma, "must choose -- and
already has"), plus a falling-apart "Hermitian translations"
dictionary and a flat rotation curve (conformal-gravity context).
Prompt text lives in the session record; will be preserved in the
histories when the raw-transcript pipeline runs.

---

## 2026-07-12 — COVER IMAGES 2-4 LANDED, REVIEWED, WIRED

User rendered and committed the three new covers; reviewed each
against its prompt and the physics: instantaneous-ghosts (all
elements + a good improvised "inf x 0 = ???"), conditioned-ghosts
(sieve/triangle/no-signaling all correct), degenerate-ghosts (the
best of the set — physics-accurate beyond the prompt: correct
generic sqrt branch-point formula, polynomial-not-oscillation
moral, coalescing-eigenvalue determinant; note its EP formula
states the GENERIC sqrt case, which is fine — the paper's
linear-in-delta non-generic direction is a refinement, not a
contradiction). **User's filename choice settles paper-4 repo
naming: degenerate-ghosts.** Banners wired into the staged READMEs
+ assemble script. Paper-5 repo/prompt: HELD — the paper does not
exist yet (T5 packaging vs threads-scout arc undecided; MPS ladder
still running); naming before content settled has been the
pattern's exception, not its rule.

**Encoding regression caught and fixed (ledger):** my PowerShell
banner-wiring roundtrip read the staged READMEs without UTF-8 and
re-wrote them as mojibake (em-dashes, superscripts). Caught on
post-commit review of the diffs; repaired by character-wise
cp1252/latin-1 -> UTF-8 reversal (0 residual markers, glyphs
verified). Detector: reading one's own diffs. Lesson: -Encoding
utf8 on WRITE does not fix a wrong-encoding READ.

**Cover-image audit (all four, vs prompts, user-directed):**
papers 1-3 COMPLETE (paper 1 audited against the transcript-
recovered original prompt; paper 3 has one trivial deviation:
stamp rendered as handheld sign). Paper 4: both concepts contain
every prompted element; v2 (sparse) DESIGNATED BANNER (reads at
social-preview scale; v1 kept as the annotated edition — its extra
equations are physics-correct). One real defect in v2: track
labels w1(t)/w2(t) should be w1(lambda)/w2(lambda) — parameter,
not time (v1 correct); flagged to user for an optional regen.

**Paper-4 banner decision REVISED (user + agreement):** v2 deleted
from the working tree (preserved in git history); v1 is THE paper-4
banner. Reasoning: absent a regeneration, the choice was dense-but-
correct vs clean-but-mislabeled (v2 carried the omega(t) defect on
the paper's central parameter) — correctness wins; my earlier
v2-as-banner designation was conditional on the label fix and is
withdrawn.

---

## 2026-07-12 — PAPER-5 NAMING + COVER PROMPT (user-directed)

Recommended repo name: **renormalized-ghosts** (the T5 headline:
the channel sum survives full quantum dynamics at the renormalized
level); alternate channeled-ghosts. Robust to the packaging
decision (standalone T5 vs merged with the threads-scout arc —
renormalization remains the centerpiece either way). Series arc:
indivisible -> instantaneous -> conditioned -> degenerate ->
renormalized. Cover prompt handed to user; visual anchors: channel
advent-calendar + tally ("more every time we look"), auditor ghost
with naive-crossed-out vs renormalized-checked columns (verdict a),
origami-folded blackboard ("the deep Hilbert space, folded in
exactly" = Schur), four ghosts/four instruments -> one gauge (the
four methodologies), d=1-log vs d=2-power curves, banner "we tried
to break it. it renormalized." Repos degenerate-ghosts and
renormalized-ghosts NOT yet created (await read-throughs /
packaging decision).

**renormalized-ghosts.png review (v1):** All prompted elements
present and well-executed (vacuum door-calendar + tally, auditor
clipboard naive-vs-renormalized 0.99-it-holds, origami "deep
Hilbert space folded in exactly", four ghosts/four instruments ->
one 0.99 gauge, d=1-log/d=2-power graph, verbatim banner, wide
aspect). TWO HALLUCINATED DEFECTS -> regeneration requested:
(1) ghost labels "(algebra/combinatorics/geometry/bootstrap)" wrong
- actual methods are ED / channel counting / Schur fold / tensor
network; "bootstrap" names a different real technique; (2) invented
moral "the more doors we open, the more the theory knows how to
hide" INVERTS the verdict (nothing hides; the count holds).
Amended prompt pins the four labels and a correct moral ("count the
channels after the fold, not before") and forbids further
additions. Same defect class as the deleted paper-4 v2 (invented
labels) - caught by the same match-image-to-prompt audit.

**renormalized-ghosts.png v2 ADOPTED (replaces v1):** regen
implements both amendments exactly - method labels now (1) exact
diagonalization (2) channel counting (3) Schur fold (4) tensor
network; moral now "count the channels after the fold, not
before." All other elements intact. Remaining nit accepted: naive
column shows "0.1" crossed out (measured naive is 0.774 at M=16,
still falling with M - fair cartoon of the trend; number was never
pinned in the prompt). v1 preserved in git history (c8b1fda).

**renormalized-ghosts v3 prompt issued:** user flagged two interior
details where v1 beat the adopted v2 - the first ghost's easel
(real matrix algebra vs sparse dot plot) and the auditor's
clipboard (sagging-curve-crossed-out vs flat-line-at-0.99 graphs,
reduced to bare numbers in v2). v3 prompt = full original with
everything pinned: v2's corrected method labels + moral, v1's
clipboard graphs and matrix easel, plus the no-additions clause.
Handed to user for render; current adopted file stays v2 until v3
reviewed.

**renormalized-ghosts v3 review:** all pinned elements landed
(labels, moral, matrix easel - now showing a diagonalized matrix,
apt). TWO defects both user-spotted: (1) naive-prediction plot
plunges to zero (measured naive slide is 1.0 -> 0.774 at M=16;
unlabeled axes; and a to-zero decay curve is confusable with the
program's REAL vacuum-survival curves - a failed prediction must
not look like actual physics); (2) tensor-network ghost holds
interlocked metal chain links, not the prompted beads-on-a-string
MPS diagram. v4 prompt pins both: shared-axes clipboard panels
(dashed reference line, naive slides but stays well above zero,
renormalized hugs the line) and an explicit beads+bond-segments
chain. File state: .png and -1.png both hold v2 (user resave
pending finalization), -3.png = v3; leaving names until user picks
final.

**v3 addendum (user-caught, third defect):** the |0> ket vanished
from the vacuum region (present in v1, already missing in v2 -
missed in my v2 review). Root cause: the ket was never in the
prompt - it was a GOOD v1 improvisation with no anchor, so regens
dropped it. v4 prompt now pins it ("labeled vacuum with the ket
symbol |0> written in chalk beneath it"). Lesson for the image
ledger: regeneration only preserves what the prompt pins - good
improvisations must be promoted into the prompt or they evaporate.

**renormalized-ghosts v4 ADOPTED (final):** passes the full pin
list - |0> ket restored, shared-axes clipboard (naive slides but
stays above zero, honest 1.0->0.774 caricature; renormalized hugs
the line), proper beads-and-bonds MPS chain, all labels/moral/
banner/graph intact, no stray improvisations. Red X sits below the
naive graph as a verdict mark - cleaner than the pinned wording.
Accepted nit: door numbers scramble in the distance (all versions;
apt - the ladder blurs as it recedes). Intermediates removed from
tree (v1-v3 in git history). Series covers now COMPLETE through
paper 5. Ledger lesson stands: pin everything, promote good
improvisations into the prompt.

---

## 2026-07-12 — ARC KICKOFF: packaging decision, charter, Arc-B gate

**Packaging DECIDED (delegated by user):** all threads get researched;
presentation = STANDALONE papers, not an omnibus. Paper 5 = T5
standalone (renormalized-ghosts; audiences: lattice/numerical QFT +
foundations). Paper 6 = EP phase-boundary paper (Arc-A unfolding +
Arc-B divisor taxonomy, Arc-C photonic D4 as experimental section;
audience: open-systems/EP + PT-photonics). Arc-D (Maldacena pricing)
-> paper 7 or review capstone; Arc-E/F feed 6/7; Arc-G registry =
infrastructure. Rationale: threads have disjoint audiences; scout's
own sequencing groups A+B+C on one mathematical core which T5 does
not share. Scout items 9 (Mannheim-cosmology reinterpretation) and
10 (alpha_g standalone) stay parked/dropped per scout.

**Agents launched (4, background):** Ilhan-Kovner 1403.4664 mapping
(Arc-A); Maldacena 1105.5632 + HLZ 2306.13714 BC-as-post-selection
scoping (Arc-D); EP-splitting/divisibility/photonic prior-art
re-sweep (watch item); Donoghue-Menezes Merlin-width EP-detuning
check (Arc-E).

**Arc-B GATE RUN (p6_divisor_gate.py, new 6th artifact class):**
divisor M = Gamma(s+dt) Gamma(s)^{-1} of the sigma_max-normalized
process; M1 = entrywise negativity, M2 = column-sum excess.
RESULT: the scout conjecture (M1<->complex/broken, M2<->Jordan,
exhaustive+exclusive) is REFUTED in strong form — generic families
(dimer unbroken/EP/broken; random real-diag, complex-pair, and
conjugated-Jordan ensembles) show BOTH modes, mostly MIXED cells,
at real magnitudes (worst neg entry -9.6e3, worst col excess +7.2e2
at dt=0.5) — NOT tolerance artifacts (magnitude-resolved re-check).
What SURVIVES, cleanly: the triangular cascade (PU-J2) is M1-free
over the entire sweep (worst neg entry exactly 0.0, matching paper
4's proof) and fails purely via M2. Converse FAILS: 25/40
non-cascade complex-pair families were M2-pure on the coarse grid.
Reshaped Arc-B theorem target: prove cascade => M1-free generally;
characterize M1-absence; adversarial numerics on the converse
(fine grid, dt sweep). Key structural insight logged: M2 tracks
TRIANGULAR BEABLE ALIGNMENT, not Jordan structure per se (dimer-EP
is a Jordan point and fails M1-first at s~0.65-0.72 in this
convention).

Errors-and-catches: none this entry; the refuted conjecture was the
scout's stated-as-conjecture, killed by its designed gate — working
as intended.

## 2026-07-12 — ARC AGENT REPORTS 1-3 (Ilhan-Kovner, prior-art re-sweep, Maldacena)

**Arc-A / Ilhan-Kovner (research/p6_ilhan_kovner_mapping.md):**
MAPS PARTIALLY. 1403.4664 is "Conformal Gravity Redux: Ghost-turned-
Tachyon" (title corrected; the PU/Jordan statement lives in companion
1301.4879). Their k=0 blowup = complex-direction unfolding of the
omega=0 Jordan corner, self-induced (mu_eff^2 ~ gamma_b^2 with
tachyonic relative sign), t_c = 2^{3/2}/gamma_0. REPRODUCED LOCALLY:
solve_ivp vs exact Eq.58, reldiff 1e-10..1e-11, blowup t=2.828424 vs
2.828427. Scope guards for paper 6: their EP is the omega=0 corner
(finite-k extrapolation is ours); "self-induced unfolding," never a
linear-spectrum claim; EP language is our overlay; 1301.4879 also has
a STABLE interacting ghost (test case for stability <=> real-direction
unfolding).

**Prior-art re-sweep (research/p6_prior_art_resweep.md):** LANE OPEN,
clock running (Znojil "unitary paths of unfolding" 2606.03789; Fring
cluster 4 papers/5 months => months not years). MUST-CITE:
Kumar-Marto 2603.07150 (ghost->IHO instability, they pick ONE side;
we classify both as unfolding directions), Pimenta 2505.08785
(trace-preserving divisibility geometry; our sub-stochastic
mass-creation channel structurally outside his framework - position
Arc-B against it), Bagchi-Ghosh-Znojil 2606.03789. Photonic at-EP
process-observable lane UNCLAIMED (2503.06977 qubit Liouvillian-EP
experiment = feasibility citation for Arc-C).

**Arc-D / Maldacena scoping (research/p7_maldacena_scoping.md):**
POSSIBLE WITH CAVEATS. Effect identified per mode: Neumann-at-future
= M_k = 1 (x) |f_k=0><f_k=0| (improper; regularize to Gaussian
M_sigma, price sqrt(det M)/p at fixed sigma, sigma->0). Positive-
frequency condition = state prep, NOT the effect (don't double-count).
STRUCTURAL FINDING: HLZ's Minkowski obstruction IS the Jordan block -
flat space = degenerate PU point, graviton(x)partner factorization
singular at H_Lambda=0; dS splits the degeneracy (Delta=3 vs 2).
In-house PREDICTION to check: the survival price degenerates as
H_Lambda->0. Prior art: BC=post-selection slogan exists (Horowitz-
Maldacena, Anastopoulos 2401.07662, Davies-Magueijo 2606.02514 -
cite); ghost-context + quantitative pricing intersection EMPTY.
Five caveats logged in the sidecar; all go in the eventual paper.
Merlin-width agent (Arc-E) still out.

**Arc-E CLOSED (research/p6_merlin_width_check.md), verdict (a):**
the UV exceptional line SURVIVES loop dressing. MY PREMISE REFUTED
(logged): I tasked the agent with the hypothesis "Merlin width =>
frequency-detuning floor Gamma_M/2, cond saturates ~2w/Gamma"; the
correct relativistic statement (DM 1908.02416 Eq 35) is that the
pole shift is Lorentz-invariant in q^2, so the frequency width
gamma/2E_k time-dilates at the SAME 1/k rate as the mass-gap
detuning - both components of the detuning vector vanish together,
no floor. cond_loop = (4k^2/m^2)[1+(gamma/m^2)^2]^{-1/2}, suppression
1-2e-4 at xi=1,N_eff=20; the only qualitative change is a fixed
approach-ray tilt arctan(gamma/m^2) ~ 1.1 deg (asymptotically-free
xi^2 shrinks it further UV-ward) and the dressed near-EP being
"resonance-EP" type ((real, complex) pair, unequal linewidths) -
one paragraph for paper 4, no retraction. Naive fixed-Gamma foil
cond_max ~ 640pi/(xi^2 N_eff) ~ 1e2 must be explicitly DISCLAIMED.
Prior art: Merlin x EP/Petermann connection absent - lane open.
Pre-submission skim queued: "Remarks on ghost resonances" JHEP
02(2025)186. Errors-and-catches: wrong mechanism hypothesis (mine),
caught by agent full-text read - fourth instance this corpus of the
tasking hypothesis dying on the literature; detector named.

ALL FOUR ARC AGENTS NOW REPORTED (A: partial map + reproduction;
sweep: lane open, clock running; D: possible-with-caveats, HLZ
obstruction = Jordan block; E: verdict (a), premise refuted).

## 2026-07-12 — CONCEPTUAL Q&A (user), two framings worth keeping

**Two-slice/memory framing:** second-order dynamics = position alone
non-Markovian; classical fix appends velocity (phase space); Barandes
refuses the fix (configurations only) and indivisibility is the exact
stochastic residue of the missing slice — psi is the appended memory.
Schrodinger first-order because psi packages both slices (Madelung:
|psi|^2 = position slice, grad S/m = velocity slice); Ehrenfest =
F=ma recovered; uncertainty = Fourier lock between the packed slices;
noncommutativity = momentum is trajectory-memory, not slice data.
ITERATED: 4th-order gravity needs FOUR slices ({1,t,t^2,t^3} = paper
4 Jordan block); Ostrogradski promotes extra slices to variables —
THE GHOST IS THE EXTRA MEMORY. Corollaries: Maldacena BC = post-
selection ON the memory slice (hdot=0 at future boundary — ties
Arc-D to paper 3's bound); divisibility is slicing-relative (T10's
thesis); "ghosts are foliation detectors" = memory direction made
visible. Candidate intro framing for papers 6/7 and the eventual
review.

**MWI placement:** Barandes+Mannheim degrade the NO-ALTERNATIVE
argument for psi-ontology (psi and inner product both derived), not
psi-realism itself. Corpus contribution: the trilemma LOCATES
many-worlds as the drop-definite-configurations horn (buys ghosts +
LI); if a ghost sector exists the interpretations separate
OBSERVATIONALLY (foliation-anchored ontology -> visible foliation,
dipole/edge template; no-slicing ontology -> none). Ghosts convert
interpretation into phenomenology. Caveats logged: instantaneity
theorem does not bite Everett (no sample space wanted); division
events <-> branching translation (terminal indivisibility = no
branch structure past t_c) is SUGGESTIVE ONLY — divisor theorems
are not decoherence-functional theorems. Review-paper material.

**MWI scout back (research/p8_mwi_scoping.md):** PBR exit SETTLED BY
BARANDES in print (PoP 2025, non-Markovian/nomic via H&S Sec.6
carve-out - passage only in v3/published; cite PoP not early arXiv);
adequacy unaddressed-in-print. Lane A (Barandes vs Everett article-
length) OPEN but months-scale clock (Mindscape prominence). Lane B
(ghosts adjudicate interpretations) OPEN; Dey-Fring 2603.15395
adjacent-only. TWO NOVELTY UPGRADES: (1) Valentini template needs
Born-rule FAILURE; our claim keeps Born rule INTACT (ghost sector is
the discriminator) - unclaimed anywhere; (2) the "bookkeeping on the
universal psi" objection to Barandes is unclaimed in print
(Aaronson blog only) - we can be first to state AND answer it.
CRITICAL FRAMING CONSTRAINT: Barandes asserts no-preferred-foliation
in print (2402.16935, 2512.18105) - our theorem must be framed as
conditional EXTENSION (ghost sector promotes foliation from
convention to observable), never contradiction of the framework's
founder. Full must-cite list in sidecar.

**New thread candidate (from user Q on BH/big-bang applicability):**
PRICE THE HOROWITZ-MALDACENA BLACK-HOLE FINAL STATE with paper 3's
conditioning bound. HM hep-th/0310281 = post-selection at the
singularity; Gottesman-Preskill critique = "post-selection has a
price" (qualitative); Lloyd-Preskill JHEP 08(2014)126 quantify
fidelity deviations. Our TV^2 + (sqrt(det M)/p)^2 <= 1 is the sharp
form of that price - same machinery as Arc-D (Maldacena dS boundary
conditioning), different spacetime. Natural companion inside the
Arc-D paper or T10. Related notes from the same exchange: T10
horizon = clock-dependent Feller classification (exit in proper
time, natural in Killing time - the time-reparametrization twin of
the EP's basis-change singularity, scout #8); Ilhan-Kovner k=0
blowup IS minisuperspace cosmology (big-crunch-type, complex-
direction unfolding); big bang as ENTRANCE boundary = unwritten
T10 corollary; cosmology = the arena with an accepted preferred
slicing (comoving/CMB frame) - the natural home of a foliation-
anchored ontology (paper 2 dipole template already trades on it).

---

## 2026-07-12 — ARC-B THEOREM: the divisor sees the unfolding direction

**Statement (2x2 cascade divisor dichotomy, proof by elementary
computation + numerics p6_divisor_theorem.py):** For triangular
H = [[w1, c],[0, w2]], c != 0, Gamma(t) = |U(t)/sigma_max|^2,
divisor M = Gamma(s+dt) Gamma(s)^{-1}:
(i) M is upper triangular with nonnegative diagonal (always);
(ii) sign(M_12) = sign[r(s+dt) - r(s)], r(t) = |U12|^2/|U11|^2
(normalization-independent) — VERIFIED 400/400 adversarial random
triangular H, |M_21| residual < 1e-10;
(iii) real split Delta: r = |c|^2(2-2cos(Delta t))/Delta^2
oscillates => NEGATIVITY (M1) RECURS, first onset s* = pi/Delta —
measured ratios 0.9969-0.9995 across Delta = 0.4-2.0; EP limit
Delta->0: r -> |c|^2 t^2 monotone;
(iv) imaginary (decay) split: r = |c|^2(1-e^{(g1-g2)t})^2/(g1-g2)^2
monotone => M1-FREE at all times (worst normalized sign-quantity 0
to machine epsilon over t<=40), indivisibility purely M2 (onsets
0.55-0.75); EP: M1-free, M2 onset 0.48 (paper-4 cross-check: ~0.50).
Closed forms vs numerics: 5e-15, 1e-15, 7e-16.

**Meaning:** within cascade families the divisor failure mode READS
OUT the unfolding direction — real-direction unfolding brings
negativity back with first-return time pi/Delta (diverging as the
EP is approached: negativity pushed to infinity IS the EP signature
at divisor level); complex/decay-direction unfolding and the EP
itself are negativity-free, indivisible purely by conditional mass
creation. This CORRECTS the morning gate's coarser "cascade =>
M1-free" (true only at/complex-of the EP; refuted for detuned real
split by the oscillating cascade ratio) and delivers the scout's
"two threads are secretly one theorem" in corrected form: Arc-A's
oscillatory-vs-explosive dichotomy has an exact divisor-level image.
Photonic corollary for Arc-C: the D4 device's divisor observable
distinguishes the unfolding direction of a near-EP coupler — the
first-return time pi/Delta is measurable as a function of detuning.

**Errors-and-catches this entry:** (1) morning gate conclusion
"cascade => M1-free" was too coarse — caught by doing the algebra
before believing the sweep (detector: closed-form r(t)); (2) first
run of [3] printed "worst entry -9.1e18 (M1-free)" — an
ill-conditioned divisor inverse at gamma*t ~ 40 amplifying roundoff
~19 digits, self-contradicting label printed blindly (detector:
reading the output against the closed form); fixed via the
inversion-free sign identity; artifact preserved in git history;
(3) machine-epsilon honesty rule applied (-2.2e-16 reported as
machine epsilon, not zero — paper-4 lesson).

## 2026-07-12 — RELEASE GATE POLICY + Arc-E paragraph + Arc-G registry

**Release gate (publish/release-gate.md, user-mandated):** no paper
circulates until K consecutive FULLY-CLEAN audit passes (default
K=2, user-settable; any fix resets the counter; fresh agents each
pass, no access to prior audit reports; every number traced every
pass; known-failure-modes checklist grown from the histories
sidecars - false iffs, code-manuscript strength mismatches, chimera
citations, exactness-vs-machine-epsilon, tolerance-masked numerics,
pre-run-expectation contamination, prior-art staleness >30 days).
Motivation: paper-1 iff survived FOUR audits; two numerics artifacts
today. "Audited" becomes measurable: released after N consecutive
clean passes.

**Paper 4 += resonance-EP paragraph (Arc-E closure):** loop dressing
paragraph inserted after the UV-line statement - Lorentz-invariant
pole shift, 1/k time-dilation of the frequency width (no detuning
floor), cond suppression [1+(gamma/m^2)^2]^{-1/2} ~ 1-2e-4, fixed
approach-ray tilt arctan(gamma/m^2), resonance-type EP (unequal
linewidths, not real-axis PT), explicit disclaimer of the
fixed-linewidth cond_max ~ 640pi/(xi^2 N_eff) foil, one-loop/
weak-coupling scope line. Cites existing \cite{DonoghueMenezes}
(1908.02416 already in bib). Recompiled clean, 12pp. NOTE: paper 4
audit counter RESETS to zero under the new gate (content change).

**Arc-G DONE: TRILEMMA_REGISTRY.md** seeded at repo root: 9
classified rows straight from paper 4 Table 1 (audited source), 4
PENDING rows for the 2025-26 wave (Kumar-Marto, Bateman-Turok,
2604.21823, 2605.01966, Znojil cluster) deliberately left without
horn assignments - no classification without a careful read (audit
discipline applies to the registry too). Standing fourth-position
challenge + adjudication log included.

## 2026-07-12 — ARC-B d x d GENERALIZATION (p6_divisor_dxd.py)

**THM-1 (any d x d triangular family):** divisor upper triangular
with nonnegative diagonal (residuals exactly 0.0 over 600 random
families d=3,4,5); per-superdiagonal sign law sign(M_{i,i+1}) =
sign(r_i(T)-r_i(s)), r_i = |U_{i,i+1}|^2/|U_{ii}|^2 — 1408/1408
adversarial sign matches. Proof identical to 2x2 ((A^{-1})_{i,i+1}
= -A_{i,i+1}/(A_ii A_{i+1,i+1})).

**THM-2 (single Jordan block, THE SURPRISE):** V(t) = f(t^2 N),
f(x) = sum x^m/(m!)^2; divisor = h(N), h = f(T^2 x)/f(s^2 x).
c_1 = T^2-s^2 >= 0, but c_2 = (T^2-s^2)(T^2-3s^2)/4 is NEGATIVE for
1 < T^2/s^2 < 3: k >= 3 Jordan cascades are NOT M1-free — negativity
in the SECOND superdiagonal for every step ratio T/s < sqrt(3),
including infinitesimal steps (generator L_{i,i+2} = -t^3 exactly;
L_{i,i+1} = 2t). Closed forms verified to 5.9e-13 (c_2), 5.3e-15
(c_3); window boundary measured T = 1.73250 vs sqrt(3) = 1.73205
(grid 5e-4). PURE CONDITIONAL MASS CREATION IS A STRICTLY k=2
PHENOMENON. Paper 4 unaffected (scoped to the k=2 cell, "the pure
Jordan cell"); paper 6 must state the k >= 3 mixing; Smilga-tower
blocks (k grows with sector) carry mixed-mechanism indivisibility.
c_3 measured POSITIVE over b/a in (1,9].

**THM-3 (detuned bidiagonal chain):** the unfolding-direction
readout is PER BOND — first negativity onset pi/Delta_i per bond i
(measured ratios 0.998-0.9995, d=4 chain, Deltas 0.4/0.6/0.8).
Photonic consequence for Arc-C: a waveguide CHAIN reads out each
bond detuning separately.

**Errors-and-catches:** my hand algebra claimed a negative c_3
window near T^2 = 2s^2 — arithmetic slip (terms wrongly put over a
common denominator), caught by check [3]'s exact closed-form
comparison; docstring corrected before commit. Detector: the
adversarial script disagreeing with its own docstring.

## 2026-07-12 — ARC-B: THE c_m SIGN PATTERN CLOSED (p6_cm_signs.py)

The open question from the dxd session is fully resolved. Structure:
f(x) = sum x^m/(m!)^2 = I_0(2 sqrt x), all zeros on the negative
axis at x_n = -j_{0,n}^2/4 (Hadamard product).

**PROVEN (generator alternation = Rayleigh law):** f prime/f =
sum_n 1/(x + j_n^2/4) (simple poles, positive weights) =>
L_{i,i+1+m} = 2(-1)^m 4^{m+1} sigma_{m+1} t^{2m+1}, sigma_p =
sum_n j_{0,n}^{-2p} = the classical Rayleigh sums, exact rationals:
1, -1/2, 1/3, -11/48, 19/120, -473/4320, 229/3024,
-101369/1935360... VERIFIED against numeric Bessel-zero sums
(200k zeros) to 1e-12..1e-15. STRICT SIGN ALTERNATION AT EVERY
DEPTH: negativity is unavoidable at depth >= 2 for every t —
mass-creation purity is k=2-only, now with the exact coefficient
law and a proof.

**Dominant-pole law (finite steps, verified):** poles of
h = f(rho x)/f(x) sit at x_n independent of rho; residue at x_1
carries J_0(j_1 sqrt(rho)) =>
sign(c_m) -> (-1)^m sign(J_0(j_1 sqrt(rho))),
c_{m+1}/c_m -> -4/j_1^2 = -0.691660 (measured -0.6917 at m~10;
rho=14 slower — near the J_0 band edge 12.949, competing poles).
The negative windows are FOURIER-BESSEL BANDS with edges ->
(j_n/j_1)^2 = 5.269, 12.949, 24.042: measured even-m first-window
edges 3.000 -> 4.778 -> 5.261 -> 5.2689 (m=2..8+, limit 5.269);
odd-m windows -> (5.269, 12.947) at m=11 vs (5.269, 12.949). Exact
polynomials (rational arithmetic) match expm divisors of J_13 to
2.6e-15..9.1e-13.

**Meaning:** the sign map of the deep-cascade divisor is universal
Bessel-zero arithmetic — depends only on depth m and step ratio
rho, on nothing else in the physics. Paper-6 section: "the sign map
of the cascade divisor." Note c_3's total positivity now explained:
odd-m band (5.269, 12.949) requires the polynomial degree to reach
it; degree-3 truncation cannot (first odd window appears at m=5).

## 2026-07-12 — ARC-A MODE-LEVEL UNFOLDING SWEEP (p6_unfolding_sweep.py)

Two inequivalent unfolding kinds at the conformal (k=2 Jordan) point,
each phase-resolved; all predictions verified:

**FAMILY direction** (physical parameters detune omega_2^2 by
Delta = |D|e^{i phi}; linear split, non-generic): growth =
|D| sin(phi)/(2 omega) — verified (reldiff 4.6e-2 dominated by the
|D|=0.1 curvature point; formula is the |D|->0 law). Oscillatory
set = the REAL AXIS of Delta (both signs: phi=0 AND phi=pi give
growth ~1e-14 while omega_2^2 stays positive) — a nuance the map
must state. Stelle control: cond(V) = 2/delta re-verified (ratios
1.008, 1.001 at delta = 5e-3, 5e-4; paper-4 cross-check).

**GENERIC direction** (matrix-entry eps e^{i phi}; Puiseux): growth
= sqrt(eps)|sin(phi/2)| verified to 1.2e-13; exponent fit 0.5000;
random-phase eps=1e-8 noise: growing fraction 1.000 of 500 draws,
median rate ~ sqrt(eps) — "the pure theory is the boundary" is now
a measured statement: the oscillatory set is measure-zero in the
generic directions.

**OMEGA->0 CORNER** (Ilhan-Kovner / conformal cosmology k=0): family
direction becomes Puiseux; growth = sqrt|Delta| |sin(phi/2)|
verified to 6.9e-16. IK check with NO free parameters: Delta =
-(3/4)gamma_b^2 (phi=pi) gives growth 0.433013/0.866025/1.732051 at
gamma_b = 0.5/1/2 vs (sqrt3/2)gamma_b exactly — the frozen-mode
formula from the agent report, the reproduction, and the sweep all
agree.

**THE MAP (paper-6 centerpiece table):** Stelle m^2 = family/phi=0
(oscillatory, cost 2/delta); Merlin width = family/arctan(gamma/m^2)
(growth gamma/2omega — Arc-E recovered); IK self-interaction =
corner/phi=pi (blowup (sqrt3/2)gamma_b); lattice/machine noise =
generic/random phase (growing w.p. 1, rate sqrt(eps)). Divisor image
= THMs 1-4 (real side: M1 recurs pi/Delta per bond; boundary +
complex side: k=2 pure M2). Arc-A numerics COMPLETE; remaining:
paper-6 write-up with the agent report's scope guards (omega=0
corner is theirs, finite-k extrapolation ours; "self-induced
unfolding" phrasing; cite 1301.4879 for the Jordan statement).

## 2026-07-12 — ARC-C DONE: devices D4 + D5 (p6_d4_device.py, proposal v1.1)

**Scout concept CORRECTED:** a reciprocal coupler at its EP is the
DIMER-EP (Jordan vector (1,-i)/sqrt2 — superposition, not a guide):
guide-basis process NOT a cascade; fails by NEGATIVITY (M1 onset
2.15 cm protocol-step / t_c = 1/(kappa sqrt2) = 2.36 cm closed form
at kappa=0.30). The cascade cell needs UNIDIRECTIONAL coupling:
synthetic phase pi/2 + dissipative bus -> H_12 = i(J-Gamma_d),
H_21 = -i(J+Gamma_d), one-way at J = Gamma_d (Hatano-Nelson
asymmetry; HN PRL 77,570 cited for the concept — DEVICE-FEASIBILITY
citation for the photonic realization QUEUED for the proposal audit
pass, do not circulate before verifying one).

**D5 (J = Gamma_d = 0.25/cm) results:** triangularity exact;
mass-creation onset z_c = 0.910 cm at protocol step Dz = 0.25 cm
(pure-cell same-step comparator 0.910 exact; dt->0 limit 1.000 —
onset is PROTOCOL-DEPENDENT, comparator convention fixed after
first sloppy print); det of divisor >= 0.78 — det estimator
PROVABLY BLIND (fingerprint: det-silent + column-sum-loud = cascade;
det-crossing + negativity = dimer); direction spectroscopy z* =
6.16/3.81 cm vs pi/Delta = 6.28/3.93 (Delta = 0.5/0.8).

**Tolerance = physics:** imperfection eta sign maps to unfolding
direction: eta/J = +1/+3/+10% -> negativity re-entry z* = 22.1/
12.7/6.9 cm (real direction); eta/J = -3% -> M1-free past 30 cm
(complex direction). Spec: |eta|/J <= 3% keeps a 6 cm window
certification-clean. MC (400 real., 1e4 photons, T2 error model):
fit recovery unbiased (-0.09% +- 1.96% on J), z_c estimator
+-0.015 cm, eta resolved +-0.0075/cm (= the 3% spec — measurement
bounds its own systematic), z* +-0.22 cm.

**Errors-and-catches:** (1) sloppy z_c comparator (mixed step
conventions) — caught on first output read; (2) eta=10% "min entry
-31.8" was an ill-conditioned-inverse artifact (THIRD conditioning
catch today) — cond>1e8 guard added, artifact resolved to clean
z*=6.9 cm re-entry OUTSIDE the 6cm window; (3) stale-variable crash
in [3] after refactor — fixed. (4) meaningless "5.3e6 sigma"
certification line replaced by the tolerance curve.

Proposal/main.tex v1.1: D4 table row + D4/D5 mechanism-resolving
paragraph + HN bibitem + xcolor fix; compiles clean, 3 pp. Paper-6
science now COMPLETE (Arc-A sweep, Arc-B theorems, Arc-C devices,
Arc-E folded into paper 4); remaining: Arc-D calculation, Arc-F,
write-up, audits.

## 2026-07-12 — ARC-D CORE CALCULATION (p7_maldacena_price.py)

**The price of Maldacena's ghost-removal, per mode, closed form.**
Model (declared): detuned PU (omega_1, omega_2 = omega_1 - delta) as
proxy for the dS Delta=3/Delta=2 split; Minkowski = delta -> 0.
Ostrogradski (q1, q2=xdot) BOTH configuration variables (two-slice
memory) => Neumann effect = multiplication operator M_sigma =
exp(-q2^2/2sigma^2), bona fide; positive-frequency = state prep
(caveat 4 respected). Quantization DECLARED (caveat 2): the
Dirac-normalizable vacuum on real configurations: Psi_0 =
exp(-(a q1^2 + b q2^2)/2 - i c q1 q2), c = w1 w2, b = delta,
a = w1 w2 delta, E0 = delta/2 (coefficient equations verified
exactly; grid E0 = 0.249998 vs 0.25). |Psi_0|^2 widths ~
delta^{-1/2} in BOTH variables = the Ilhan-Kovner EP degeneration,
quantitative. (BM root b = w1+w2 has a < 0: contour-rotation leg of
the left/right/silence taxonomy; not used.)

**PRICE SHEET (both collapse at the conformal point):**
- survival p(sigma,delta) = [1 + 1/(2 sigma^2 delta)]^{-1/2}
  -> sigma sqrt(2 delta) (verified to 6 decimals);
- delivery: conditioned graviton wavefunction has width
  1/sqrt(w1 w2 delta), NOT Einstein's 1/sqrt(w1): fidelity
  F = 2 sqrt(a w1)/(a+w1) ~ 2 sqrt(w2 delta) -> 0 (scaling fit
  0.491 vs 1/2; mixed-rho grid check 0.5500 vs 0.5505).
VERDICT: ghost-removal by future BC is a survival-conditioned
effect whose price diverges at the conformal point at BOTH ends —
pay sqrt(delta) survival, receive sqrt(delta) Einstein fidelity.
dS works because its splitting is O(1); Minkowski is the delta->0
boundary: THE HLZ OBSTRUCTION, PRICED. In-house prediction from the
scoping report: CONFIRMED.

**Errors-and-catches:** first grid eigencheck at delta=0.1 failed on
its own finite differences (residual 4.2 — under-resolved
e^{-i c q1 q2} phase at large |q1 q2|); replaced by exact algebraic
coefficient-equation verification + well-resolved grid sanity at
delta=0.5. Fourth numerics-check artifact today; detector: reading
the residual against the exact algebra.

**Remaining for the paper (paper 7 / capstone):** formal
BC-as-effect mapping theorem; exact paper-3-bound correspondence
(TV/det-M on the message subspace); HLZ alternative M-prime priced;
dS-representation (Delta=3/2) upgrade of the proxy; Gottesman-
Preskill/Lloyd-Preskill positioning; the BH final-state pricing
thread (same machinery at the singularity).

## 2026-07-12 — ARC-F: POLE SHEET -> PROCESS CLASS (p7_buoninfante_map.py)

**Mapping proposition (numerics verified; Buoninfante extraction
agent running for the citation-grade analytic side):** the
ghost-vs-unstable-particle analytic dichotomy has an exact
sample-space image via Bochner:
- SECOND-SHEET resonance: positive Kallen-Lehmann density => A(t) =
  FT of a positive measure => positive-definite => |A(t)| <= 1
  ALWAYS (measured max = 1.000000 exactly on the BW-threshold toy):
  the survival process is sub-stochastic UNCONDITIONED; divisor
  violations only as transient backflow revivals (toy: depths
  ~1e-9, decaying — weakly demonstrated, near quadrature floor;
  the |A|<=1 bound is the exact content).
- FIRST-SHEET CC pair: no positive spectral representation;
  max||e^{-iHt}|| = 1099 >> 1: NO unconditioned sub-stochastic
  survival process exists; sigma_max conditioning MANDATORY, and it
  carries paper 1's terminal class: permanent negativity onset
  t_c measured 0.6400 vs closed form arcsinh(kt/(k sqrt2))/kt =
  0.6487 (step convention), generator floor -2.6031 -> -(a+kt) =
  -2.6180.
- Sheet-crossing sweep: max||U|| crosses 1 EXACTLY at the boundary
  (1.000/1.000/1.000 | 20.1/162754 across g_eff = -0.4..+0.4).
SLOGAN: unstable particles survive unconditioned; ghosts survive
only conditioned. Adjudication sharpened: Donoghue-Menezes pay
microcausality to keep the unconditioned reading; we pay
conditioning to keep causal order — two prices for the same
first-sheet pair (paper-4 Table 1 note upgraded).
Errors-and-catches: zero-size-array crash in the revival summary
(empty early-third positive set) — robustness fix, no physics
change.

**Arc-F CLOSED (research/p7_buoninfante_map.md):** extraction agent
confirmed the discriminant (same CC pair m^2 +- i m Gamma, only the
SHEET differs; ghost = first/physical sheet) and REFINED our Bochner
statement: the ghost continuum rho stays POSITIVE — positivity of
A(t) fails via the discrete NEGATIVE-RESIDUE complex-pole terms
(P3 Eq. 20/40), not via rho; sum rules 1 = C (decay) vs Z+Z* = 1+C
(persistence). Buoninfante's ghost neither decays nor runs away
("anti-instability"); instead multi-particle MASKING with overlap
sinh^2(Gamma t/2). QUANTITATIVE HOOK VERIFIED to 1e-14: our broken
dimer has |U_12|^2 = (kappa/kt)^2 sinh^2(kt t) exactly — with kt =
Gamma/2 this IS his masking law: his anti-instability = closed-
currency statement, our conditioning = beable currency, same
closed form. Taxonomy dictionary: Feynman ghost (causal, negative
norm) = horn 3/conditioning; anti-Feynman (acausal, positive norm)
= the DM/Merlin route (DM uncited by him — connection is OURS to
state carefully); fakeon = the silence leg; Anselmi camp
(2503.01841, JHEP 05(2025)145: "only fakeons viable") = live
controversy our trilemma prices. Lane confirmed OPEN (no PT/
stochastic content in the trilogy). PDF spot-check of equation
numbers queued for the paper-7 audit. ALL ARC THREADS (A-G) NOW
COMPUTATIONALLY COMPLETE.

## 2026-07-12 — PAPER 6 v0.1 DRAFTED (paper6/main.tex, 9pp, compiles clean)

"The conformal point is a phase boundary: unfolding directions, the
sign map of the cascade divisor, and a photonic device that reads
them out." Structure: provenance note p3 (house standard);
Sec 2 direction map (family/generic/corner laws with all measured
numbers; IK reproduction + the three scope guards from the agent
report; cond=2/delta re-verification); Sec 3 divisor image
(Prop per-bond sign law WITH PROOF; THM k=2 purity with proof +
sqrt-3 window; THM Rayleigh sign law with Hadamard proof;
Fourier-Bessel band numerics; c_3 explanation); Sec 4 deformation
dictionary table (Stelle/Merlin/IK/lattice/stacked rows; Merlin
paragraph mirrors the paper-4 insertion); Sec 5 photonic readout
(D4/D5 summary, mechanism fingerprint, tolerance-as-physics);
Sec 6 prior art (Kumar-Marto, Pimenta, BGZ, Chen-Ju,
Sayyad-Starkov, FMT — all from verified sidecars); Sec 7 discussion
(measure-zero boundary; Rayleigh universality flagged as "possibly
a shadow of something better"; pointers to papers 5/7 without
naming). AUDIT HYGIENE BUILT IN: four bibitems carry explicit
"[details to be verified at audit]" markers rather than guessed
metadata; drafted title marked "v0.1, not yet audited". Release
gate counter: 0. Drafting order decided: paper 6 first (lane
clock), paper 5 on MPS data, MWI after.

**Corpus numbering fixed (user query exposed drift):** paper 5 =
T5 standalone (renormalized-ghosts; awaiting MPS data); paper 6 =
phase boundary (v0.1 drafted); paper 7 = conditioning paper
(Arc-D Maldacena pricing + Arc-F Buoninfante mapping; formal
theorems remain); paper 8 = the many-worlds/foundations paper
(task #25; scout complete, no draft). Numbers 7/8 may swap by
completion order; the convention is numbers-at-drafting, now
stated explicitly.

## 2026-07-12 — PAPER 6 AUDIT PASS 1 LAUNCHED + PAPER 8 SKELETON

**Paper 6 first audit cycle:** three fresh agents launched per
release-gate spec (claims/proofs with independent re-derivation
orders; numerics with full script reruns + tolerance spot-checks;
bibliography with per-item web verification + fresh prior-art
spot-checks of Sec 6 claims (a)-(d)). No access to prior audit
reports. Counter at 0; pass 1 results pending.

**Paper 8 skeleton (paper9/main.tex, v0.0):** "Ghosts as an
interpretation experiment: what indivisible processes say to
Everett." Full section structure with claim logic in place and
TODO blocks marking undrafted prose: Sec 2 reconstruction
landscape (Barandes nomic/latent + PBR-exit-by-citation with the
structural-not-convenient point; Mannheim inner-product-derived);
Sec 3 underdetermination + the bookkeeping objection STATED AND
ANSWERED (parity, disanalogy-with-pilot-wave, empirical
decisiveness); Sec 4 trilemma placement (Everett = horn 3, pays
willingly; instantaneity does not bite); Sec 5 the separation
(Born-rule-intact discriminator vs Valentini's nonequilibrium;
DGNSZ 1307.1714 as the counter-position whose loophole we occupy;
conditional stated plainly); Sec 6 what does NOT follow (division
events <-> branching = conjecture only); provenance note p3.
Founder-tension guard hardcoded in the intro. Bibliography seeded
from the scout sidecar with TODO-at-audit markers on every
unverified detail. Numbering note: papers vs threads namespaces
clarified with user (T8/T9/T10 are THREADS; paper 8 = MWI).

**Paper 6 audit pass 1, agent 1/3 (bibliography) REPORTED:**
8 findings (3 MAJOR, 3 MINOR, 2 NIT), all fixed same-hour:
QubitEP2025 completed (Zhang-Han-Wu-Ning-Yang-Zheng, PRL 135,
230203 (2025), "Experimental observation of non-Markovian quantum
exceptional points"); Starkov initial corrected K->G.A. (identity
error) + subtitle added; BGZ full entry (Ann. Phys. 492, 170569
(2026), title verbatim); Chen-Ju exact title ("at exceptional
point", no article) + initials; Smilga published title "giving";
in-text QubitEP characterization reworded to "non-Markovian
quantum EPs of an extended Liouvillian" (their explicit contrast).
Sentence-case nits: house-style decision documented, no change.
Prior-art claims (a)-(d) ALL STAND under fresh searches; zero
chimeras in 19 external refs; Rayleigh/Watson attribution verified
(Watson 2nd ed. pp. 500-502, sec. 15.5). Gate counter remains 0
(findings existed); agents 2/3 (claims/proofs, numerics) pending.

## 2026-07-12 — PAPER 6 AUDIT PASS 1 COMPLETE: 29 findings, all fixed

Three agents reported (full ledger: histories/paper6-history.md).
Totals: 1 CRITICAL + 9 MAJOR + 10 MINOR + 9 NIT = 29; 85 numbers
traced clean; ALL theorem algebra independently confirmed; all four
prior-art claims stood; zero chimeras.

**THE CRITICAL (science correction):** "complex-direction unfolding
stays negativity-free" was a false converse — negativity-free set =
purely imaginary ray + EP only; general delta = a+ib, a!=0 has
non-monotone r (derivative prop e^{-bt}[b cos at + a sin at -
b e^{-bt}]). Verified via new script block: monotone at phase 90deg
ONLY (0 decreasing intervals vs 919-1049 elsewhere). CORRECTED
STATEMENT SHARPENS the paper: the divisor reads out Re(delta); D5
device rows survive (both purely imaginary). Fifth false-converse
catch in corpus history; detector: independent re-derivation order
in the audit prompt.

**Other majors fixed:** family-vs-generic oscillatory sets split in
abstract/caption (real axis vs single ray); Jordan qualifier added
everywhere (reducible 3-level counterexample noted in text); IK
dictionary row weakened to proven content; IK rates reattributed to
frozen-mode check + NONLINEAR reproduction added as public script
block [3b] (blowups to 6 sig digits, reldiff 4.4e-12 — provenance
promise restored); 3%-boundary overclaim -> sufficient-with-
factor-4-margin (true boundary ~12%); QubitEP/Starkov/BGZ/Chen-Ju
bibliography corrections. All minors and nits applied (protocol
flags on 0.48/2.15/6.16/3.81, Rayleigh range 5e-12/2e-15, rescaled
pole variable, t>0, strictly positive diagonal, any-eigenvalue
extension, rho=2,6 scope).

Manuscript recompiled clean. GATE COUNTER: 0 (pass 1 not clean, as
expected for v0.1). Pass 2 with three fresh agents to be launched
against the corrected manuscript.

**Paper 6 pass 2, agent 1/3 (bibliography) reported: 4 findings
(1 MAJOR-process, 1 MINOR, 2 no-action NITs), zero accuracy
errors** — "unusually clean bibliography for this corpus"; Eq.(58)
cross-numbering verified by direct equation count; all in-text
characterizations of cited works confirmed fair against full
texts/abstracts; prior-art claims stand again. MAJOR = repo-state
gate, not text: Companion2/3/4/prop cite content still under the
user's push-hold — RELEASE CHECKLIST ITEM: hold must lift before
paper 6 circulates (added to publish-pipeline task implicitly).
MINOR fixed: Companion2/3 now cite their dedicated home repos
(instantaneous-/conditioned-ghosts) per README convention, with
main-repo source pointer. Recompiled clean. Pass-2 verdict awaits
agents 2/3; counter unchanged (findings exist => pass 2 not clean
under the strict gate).

**Paper 6 pass 2, agent 2/3 (numerics) reported: 6 findings
(1 MINOR, 5 NIT), 43/44 traced clean, all spot-checks PASSED**
(sqrt-3 boundary converges under 10x grid refinement; pi/Delta
ratios -> 1 at finer protocol; z_c 0.905->0.970 monotone toward
the 1.000 zero-step limit; 2000/2000 growing at a new seed with
median 0.707 sqrt(eps) matching theory; curvature-domination
confirmed prop |Delta|). MINOR fixed: eta/J clean-window boundary
made script-traceable — [1b] scan extended (z* = 6.3/6.0/5.8 cm at
12/13/14%), manuscript now quotes the MEASURED ~13% boundary.
NITs fixed: t_c agreement restated as relative ~1e-6 (five-six
sig digits — the gamma_0=1 case rounds short of six); Rayleigh
bound 2e-15 -> 3e-15 (was sitting exactly at its own edge);
vacuous worst_diag control in p6_divisor_dxd.py initialized to inf
(now certifies min diagonals 1.8e-2/8.5e-3/5.3e-3 — was
structurally zero); per-bond range 0.9982-0.9995; z* precision
scoped "about the finite-step offset". Recompiled clean. Awaiting
agent 3/3 (claims/proofs).

## 2026-07-12 — PAPER 6 PASS 2 COMPLETE: 17 findings, all fixed; counter still 0

Second CRITICAL in two passes, and it was in pass 1's own fix: the
negativity-free set is NOT just {imaginary ray, EP} — my
verification scan covered split phases 0-180 only (upper
half-plane) and I generalized. For Im(delta) < 0 there is an open
SILENT CONE within 15.345 deg of the lower real axis (bisection,
scale-invariant; agent proved a = 0.2, b = -0.6 monotone three
independent ways; full-circle scan now in p6_divisor_theorem.py
[6]: monotone at 90 and 210-330, recurring at 0-60, 120-180). The
corrected statement is BETTER: half-plane readout law + a
sharp-threshold silent cone the paper now owns. Root-cause lesson
for the gate checklist: HALF-DOMAIN SCANS GENERALIZED = the
mechanism behind both criticals today; full-domain coverage is now
an explicit audit probe. Numerics agent: 43/44 traced, boundary
made script-traceable (~13%), five nits fixed incl. a vacuous
always-zero control (worst_diag init). Bibliography: zero accuracy
errors; push-hold flagged as circulation gate. All fixes applied,
recompiled (10pp), counter 0; pass 3 launching.

**MPS ladder E2 L=16 (14:30, 5334s):** dE(12)/site = 8.9334e-03,
rate/site = 6.8282e-04. FLOOR COMPARISON (honest): E1 lambda=0
floor 5.728e-02 total / 8 interior sites = 7.16e-03/site; E3
normal twin 5.407e-02/8 = 6.76e-03/site. Ghost signal is only
~25% above the Trotter floor and ~32% above the twin at lambda =
0.06, chi = 40, dt = 0.02. CONSEQUENCE: the E2 extensivity
comparison (L = 16/24/32) is floor-contaminated at this coupling —
interpret only relative to the per-L floor; the DISCRIMINATING
rung will be E4 lambda-scaling (lambda = 0.12 should give ~4x
signal, well clear of floor; lambda = 0.03 will be buried —
predict: ratio ladder readable from the top two rungs only). If
E4 confirms the floor problem, paper-5 production needs a dt =
0.01 re-run of the affected rungs (floor ~ dt^2 => /4) before any
volume-scaling claim is written. NO conclusions drawn until E4
lands (pre-run-expectation rule).

**Release gate K SET: K = 2 (user, 2026-07-12), with escalation
clause — any error caught after a declared-clean pass raises K to
3 for all subsequent releases.** Practical status for paper 6:
passes 1-2 not clean (counter 0); if pass 3 (running) is clean,
counter = 1 and a clean pass 4 releases the paper.

**Paper 6 pass 3, agent 1/3 (bibliography): 3 findings (1 moderate,
2 minor), all wording/pointer — zero external-record errors for the
second consecutive pass** (all 20 bibitems verified; Eq.58 = 34+24
cross-map re-verified independently; Pimenta full-text
trace-preserving confirmation; Merlin footnote-1 sourcing;
novelty claims survive third fresh search). Fixed: Companion4 and
Companion3prop "same repository" ambiguity (created by MY pass-2
fix — a fix introducing a finding, noted) -> explicit main-repo +
source-directory pointers; abstract over-attribution -> "the rate
(sqrt3/2) gamma_b their equations imply" (the rate is our
linearization, not their stated result). Recompiled. Pass 3 NOT
clean (findings exist); counter 0; agents 2/3 pending.

**Paper 6 pass 3, agent 2/3 (numerics): 6 findings (3 MINOR,
3 INFO), zero critical/major, 50 traced clean.** Cone boundary
independently pinned at 195.34485 deg across four grids + brentq
tangency solve (printed 195.345 solid); 500/500 seed-robust
(seeds 1/42/2026); eta/J boundary 13.4-13.6% on 0.2% grid. Fixes:
15.35 -> 15.345 (double rounding); sigma_1 reldiff 5.1e-12 (was
understated as 5e-12); |Delta| interval notation -> discrete
points; onset-ratio protocol step stated at point of use; 13-14%
grid caveat added. INFO item on Eq.(3.24) already resolved by the
parallel pass-3 bibliography agent (verified against arXiv full
text, 34+24=58). Recompiled. Awaiting claims agent (3/3).

**STANDING DIRECTIVE (user, leaving for a while):** rerun paper-6
audit passes autonomously until K=2 consecutive clean; fix-and-
relaunch each round with fresh agents; strict cleanliness = zero
findings of any severity per agent report; if rounds stall at
pure no-action observations for 2 consecutive passes, hold for
user. All results logged (notes + history sidecar + per-fix
commits, pushed to Gitea).

## 2026-07-12 — THROTTLE OPENED (user directive: both PCs, full use)

Local dt=0.02 ladder (PID 62560) STOPPED mid-E2-L24 per user
(superseded); its E1/E3/E2-L16 results stand and are logged above.
NEW dt=0.01 PRODUCTION LADDER, 8 cases (floor, twin, lam 0.03/
0.06/0.12, L24, L32, chi64), one process each:
- the lab server: all 8 cases, launched 14:48:54, ~3 BLAS threads
  each (Store python 3.11 via Start-Process — survived ssh
  disconnect; two false alarms during launch diagnosed: process
  name is python3.11 not python, and logs are end-buffered; CPU
  438-450 s/proc at +15 min = healthy).
- Local PC: floor/twin/lam003/lam012 duplicated as an
  INDEPENDENT-PLATFORM replication (python 3.14, numpy 2.x local).
- 4 accidental held-ssh duplicates on server killed; 8 stray
  schtasks (would have re-fired 23:59) deleted.
GPU: assessed and declined — chi=40-64 SVDs (120-192 sq) are below
GPU payoff; revisit at chi >= 128 with a torch rewrite.
Priority: bumping useless on idle boxes (BelowNormal = Normal when
uncontended) — the speedup is the 8-way parallelism + i9.
ETA: E4 rungs + floor ~1.5-2 h from 14:49 (=> ~16:30); chi64 tail
~4-6 h. Monitor armed (10-min ssh poll, both machines).
dt=0.02 vs dt=0.01 floor comparison = Trotter-origin verification,
free from the two ladders.

**Zero-step onset verified before manuscript edit:** col-sum onset
0.4722/0.4832/0.4854/0.4858 at dt = 0.05/0.01/0.002/0.0005 ->
0.486 (agent's exact solve confirmed). Paper 4's "~0.50" was its
dt=0.05 protocol value — paper-4 fix queued.

**Paper 6 pass 4, agent 1/3 (bibliography): 4 findings (1 MINOR
style, 3 no-action informational) — zero accuracy errors, third
consecutive pass.** All 20 bibitems PASS in the verification
table; IK rate-attribution language verified clean in all three
occurrences; Eq. 58 = 34+24 re-verified; novelty claims survive a
fourth fresh search. Fixed: arXiv IDs added to Klauck2019
(1904.08135) and HatanoNelson1996 (cond-mat/9603165) for internal
style consistency. Standing circulation gates re-confirmed: push-
hold must lift; device-feasibility citation must be added to the
proposal. Strict-gate note: pass 4 therefore NOT clean (minor
existed); claims + numerics agents pending — if subsequent passes
yield only no-action-level items, the stall valve applies (hold
for user).

**Paper 6 pass 4, agent 2/3 (numerics): 3 findings (1 MAJOR,
1 MINOR, 1 NIT), 50 traced clean.** THE MAJOR: my pass-3 0.486 fix
was INCOMPLETE-PROPAGATION — papers 6+4 updated but
p6_d4_device.py still printed "dt->0 limit 0.50/(2J) = 1.000" and
proposal v1.1 still said 0.50/2J, breaking the reproducibility
promise. Fixed all surfaces: script docstring + print now 0.486/
(2J) = 0.972 (rerun verified), proposal -> 0.486/2J = 0.97 cm
(recompiled). Agent independently re-derived the constant
(generator crossing 0.485868; convergence 0.4722->0.4859) — the
manuscript number was right, the ecosystem lagged. NIT: stale
docstring numbers in p6_cm_signs.py ((12.95,23.98)->(12.949,
24.042); c_5 window) fixed. Everything else traced clean incl.
the tau/2 offset law verified at three step sizes and the silent-
cone brackets re-confirmed sharp + scale-invariant. LESSON for
the checklist (candidate): FIX PROPAGATION — a corrected constant
must be grepped across scripts + all companion docs, not just the
paper being audited.

**Paper 6 pass 5, agent 1/3 (bibliography): 6 findings (1 MEDIUM,
2 LOW, 3 notes) — zero accuracy errors AGAIN, but a genuine gap
four prior passes missed: BARANDES NAMED BUT NEVER CITED** (the
framework originator had no bibitem). Fixed: Barandes bibitem
(PoP 2025 + theorem) cited at first mention; Stelle1977 added and
cited in Table 1; Maldacena 1105.5632 added and cited at the
discussion name-check; Merlin coinage now cites 1908.04170
companion; Sec-6 sentence acknowledging the non-Markovian-EP line
(2503.06977 + 2406.18362) as nearest EP-divisibility contact —
NMEPtheory bibitem carries an explicit author-list-to-verify
marker for the next pass (no guessed metadata). Recompiled clean.
Pass 5 not clean; claims + numerics agents pending.

**Paper 6 pass 5, agent 2/3 (numerics): 4 findings (1 MEDIUM,
2 LOW, 1 INFO), 43 claim groups traced clean.** The 0.486
ecosystem verified consistent everywhere incl. the both-directions
rounding story (dt=0.05 detects 0.472, coarse 0.05 grid detects
0.50 — measured); onset-ratio detection law verified analytically
(r(s+tau)-r(s) = 2 sin(Delta(s+tau/2)) sin(Delta tau/2)) and at a
second step size. MEDIUM fixed: my wedge gloss "a single window
over most of the wedge" was untraceable AND wrong — measured: 1
window only at ~189-195 deg (~40% of wedge), 2 at 188, 4 at
181-185 within t<=40, silencing time diverging toward the real
axis; text corrected with measured counts and the script's [6]
scan extended with wedge phases + WINDOW-RUN counting (raw
decreasing intervals != windows — made both printed). LOWs fixed:
one stale 0.50/c comment in p6_d4_device.py (fix-propagation
residue); Sec-5 scan-grid description now states both estimators'
grids (0.01 cm z*, 0.1 cm window scan). INFO: measured z* center
-0.10 vs -tau/2 = -0.125 anchor parenthetical added. Recompiled.
Claims agent (3/3) pending; pass 5 not clean.

## 2026-07-12 — dt=0.01 FIRST RESULTS (local 4): TRUNCATION, NOT TROTTER

Local L=16 cases (51 min each, 4-way parallel): floor (lam=0)
maxabs 0.2305, dE_end/site 2.88e-2; lam003 2.71e-2/site (BELOW
floor); lam012 6.15e-2/site (~2.1x floor); twin 4.45e-3/site (6.5x
BELOW floor). VERDICT-CHANGING PATTERN: the floor got 4x WORSE
going dt 0.02 -> 0.01 (7.1e-3 -> 2.9e-2 per site) — Trotter would
have given /4. Interpretation: the drift is TRUNCATION-dominated
(each halving of dt doubles the chi=40 SVD truncation count); the
interacting twin is cleaner than free evolution because its state
stays lower-entanglement. CONSEQUENCE: finer dt BACKFIRED; the
control parameter is chi, not dt. The dt=0.01 ladder is a
diagnostic, not paper data. DISCRIMINATING PAIR LAUNCHED locally:
floor at chi=64/dt=0.01 (truncation predicts BETTER) and floor at
chi=40/dt=0.04 (truncation predicts BETTER THAN dt=0.02's 5.7e-2;
Trotter predicts 4x WORSE ~0.23). Server 8-case wave still
running (its chi64 case doubles as the key diagnostic). NO
paper-5 conclusions from any of this yet; production protocol
will be redesigned on the diagnostic verdict (likely: coarser dt
+ larger chi, or explicit truncation-error tracking with
extrapolation).

**Paper 6 pass 6, agent 1/3 (bibliography): 2 findings — the
planted NMEPtheory marker RESOLVED (Lin, Kuo, Lambert, Miranowicz,
Nori, Chen, Nat. Commun. 16, 1289 (2025)) and the Barandes PoP
volume added (3(1), 8). Everything else verified including the
Merlin-coinage placement by full-text search of both DM PDFs, the
Eq.(58) closed form against the IK full text, and both novelty
claims (fifth fresh search). Zero accuracy errors — fifth
consecutive pass. Recompiled clean. Claims + numerics pending;
pass 6 not clean under the strict gate (the marker resolution
counts), but this closes the last KNOWN open item in the
manuscript.

**Paper 6 pass 6, agent 2/3 (numerics): 3 findings (1 MODERATE,
2 LOW), 51 traced clean.** MODERATE: my wedge range "1 window at
189-195 deg" wrong at its endpoint — 189 deg has 2 windows (agent
scratchpad, identical conventions); text now quotes only SAMPLED
phases (1 at 190/193, 2 at 188, 4 at 181/185) — the range-endpoint
failure mode is the same generalize-beyond-measurement disease,
now at degree granularity. LOWs: continuous-range phrasing
replaced by sampled-phases phrasing throughout the scan sentence
(cone interior explicitly covered by the bisection instead);
garbled D4 parenthetical rewritten. Everything else traced clean
incl. the full 0.486 ecosystem re-verification and the IK t_c
deficits = gamma_0/1e6 exactly (the blowup-event threshold).
Recompiled. Claims agent (3/3) pending.

## 2026-07-12 — dt=0.01 LADDER COMPLETE (rate/site, chi=40): TRUNCATION-LIMITED

Full dt=0.01 set (server + local agree):
  floor(lam0)  rate 3.17e-3/site   dE_end 2.88e-2
  lam003       rate 3.03e-3        2.71e-2  (at/below floor)
  lam006 L16   rate 3.70e-3        3.47e-2  (~1.2x floor)
  lam012       rate 6.00e-3        6.15e-2  (~1.9x floor, CLEAR)
  twin(lam06)  rate 0.42e-3        0.44e-2  (6-8x BELOW floor)
  L24 lam06    rate 1.06e-3        1.37e-2  (per-site drops with L)
DECISIVE COMPARISON vs dt=0.02: floor/site 7.2e-3 -> 2.9e-2, i.e.
~4x WORSE at half the step. Trotter would improve 4x; truncation
(step-count accumulation of chi=40 discarded weight) gets worse.
The healthy twin staying far below floor while the FREE ghost
(lam=0) saturates it confirms: the free ghost's entanglement
growth is what chi=40 cannot hold. => The control knob is CHI,
not dt; the dt=0.01 ladder was the wrong experiment (my + user's
shared hypothesis that finer dt cleans the floor is REFUTED,
logged). Only lam=0.12 gives clean signal/floor separation at
chi=40.

IMPACT ON PAPER 5 (bounded, stated honestly): the CORE verdict (a)
- renormalized multiplicity survives - rests on ED + Schur folding
(0.988-1.000), NOT on MPS; MPS is the 4th cross-check + the
large-L vehicle. So the verdict is unaffected; what is at risk is
only the MPS-based volume-scaling extension. AWAITING the two
discriminating diagnostics (local, still running): floor at
chi=64/dt=0.01 (truncation predicts SUBSTANTIALLY better) and
floor at chi=40/dt=0.04 (truncation predicts better than dt=0.02).
If chi=64 floor drops far: push chi + extrapolate discarded
weight, rerun the ghost ladder at chi>=64. If it barely moves:
MPS is the wrong tool for large-L here; paper 5 reports the ED/
Schur verdict + the MPS certification at L=16 only, and states the
entanglement barrier honestly as a methods limit. NO paper text
until the chi=64 diagnostic lands.

**Paper 6 pass 7 (FIRST CROSS-MODEL PASS — agents now Opus 4.8
after Fable credit exhaustion; the paper was Fable-authored).**
Agent 1/3 (bibliography): 2 findings, both title-formatting.
Smilga verb "giving"->"give" — this CONTRADICTED pass 6's agent
(which claimed the published IJTP title was "Giving"); resolved by
DIRECT arXiv fetch of 1409.8450 = "...give a continuous spectrum"
(present tense, author-controlled primary source we cite). Set to
"give"; journal capitalization unverified but arXiv is
authoritative for our citation - noted. Donoghue-Menezes serial
comma "stability and"->"stability, and" (published PRD title).
Everything else verified: both completed entries (NMEP 1289,
Barandes 3(1),8) confirmed, no placeholders remain, both novelty
claims survive a sixth fresh search, zero chimeras/misattributions/
false quotations. CROSS-MODEL NOTE: an Opus agent adversarially
checking Fable-authored bibliography found only 2 trivial title
nits and independently re-confirmed all substantive entries -
evidence the corpus is model-robust (see model-swap discussion,
this session). Claims + numerics (also Opus) pending.

**Paper 6 pass 7, agent 2/3 (numerics, Opus): 3 findings, ALL
info/no-action ("no fix required" per the agent), 48 traced
clean.** Cross-model confirmation of substance: the agent verified
that paper 6's diagnosis of the 0.486-vs-0.50 onset (0.50 = coarse
BASE-GRID artifact, not step) is the numerically correct account
and supersedes paper 4's looser "0.05-step" wording. Sampled-phase
discipline verified airtight ("189 appears nowhere"; the 17 quoted
phases = the script tuple exactly). Optional queued item (NOT done
mid-loop, paper 4 not in active cycle): one clause in paper 4
noting its ~0.50 was a base-grid artifact. Findings 2-3 (1.15deg
tilt -> "~1deg"; median 0.69 sqrt(eps) -> "~sqrt(eps)") both
within their own "~". Numerics lane is at the FLOOR: no actionable
finding. Claims agent (3/3) pending.

**PROVENANCE: commit trailer switched to Opus 4.8 from here** (the
model swap point). Rationale: papers remain Fable-authored (their
provenance notes stay true), but audit-fix commits since the swap
are Opus work; git authorship should be literally accurate. Prior
Fable-trailer commits left as-is (no history rewrite).

## 2026-07-12 — FLOOR DIAGNOSTICS: Trotter/truncation TRADEOFF (not pure truncation)

Floor maxabs vs dt at chi=40, L=16, lam=0:
  dt=0.04 : 0.337   (Trotter-dominated, coarse steps)
  dt=0.02 : 0.057   (SWEET SPOT - minimum)
  dt=0.01 : 0.231   (truncation-dominated, too many steps)
NON-MONOTONIC in dt => classic Trotter(O(dt^2) per step) vs
truncation(accumulates with step count) tradeoff, minimized near
dt=0.02. CORRECTS the earlier "pure truncation" read: at dt=0.01
truncation wins, at dt=0.04 Trotter wins, dt=0.02 balances. So
dt=0.02 was ALREADY near-optimal; the user's + my dt=0.01
refinement hypothesis was doubly wrong (finer dt made it worse via
truncation). L32 dt=0.01: dE_end/site = -3.46e-3 (NEGATIVE,
non-extensive vs L16/L24 positive) => truncation worsens with L,
volume law not clean at chi=40.

NOT a floating-point issue (user asked): the floor is 1e-2..1e-1,
14+ orders above machine epsilon; it is DISCARDED-WEIGHT truncation
(re-compression to chi each TEBD step throws away Schmidt values
the free-ghost entanglement growth needs). 128-bit math irrelevant.
Root = entanglement barrier: S(t) grows, MPS holds only S ~ log chi
(chi=40 -> ~3.7). Knob is CHI at dt=0.02. DEFINITIVE TEST LAUNCHED
(server, free HW): floor + ghost at chi=64, dt=0.02, L=16. If floor
drops far below 0.057 -> push chi + plan a chi>=64 volume sweep;
if not -> paper 5 reports ED/Schur verdict + L=16 MPS certification
+ honest entanglement-barrier methods limit. Paper-5 CORE verdict
(a) unaffected either way (rests on ED+Schur, not MPS).

**Compute cleanup 2026-07-12 ~17:40:** server had stale/duplicate
chi=64/dt=0.01 orphans (14:48 + 14:53 launches; the held-ssh
duplicates whose remote python survived TaskStop of the local ssh
client) contending with the definitive chi=64/dt=0.02 test. Killed
all server python + clean-relaunched the sweet-spot pair (floor +
ghost, chi=64, dt=0.02, L=16, 8 threads each) via
clean_relaunch_c64.ps1. dt=0.01 chi=64 point abandoned (secondary;
dt=0.02 is the definitive comparison vs the chi=40/dt=0.02 floor of
0.057). Monitor armed for diag_floor_c64_dt02 / diag_ghost_c64_dt02.
ETA ~2 h. Lesson: TaskStop kills the LOCAL ssh client, not the
REMOTE process it spawned - use detached Start-Process on the server
(not held-ssh) for remote jobs, or kill remotely by name.

## 2026-07-12 ~17:55 — CONVERSATION SWEEP (pre-Fable-handoff)

Reviewed the session dialogue for decision-relevant reasoning not
already on disk. Finding: nearly all DECISIONS were logged in real
time (release-gate.md: K=2 + escalation, clean=zero-findings-
requiring-change, verify-factual-corrections; HANDOFF.md: the Fable
queue; sidecars: all audit findings; notes: all results). The
conversation-only content was mostly PEDAGOGICAL. Persisting the two
explanations that will become paper-5 prose or matter to a fresh
session:

**(1) Why the MPS floor is not a precision issue (=> paper-5 methods
limitation, and answers "would 128-bit help?": NO).** The floor is
TRUNCATION error (discarded Schmidt weight at each TEBD
re-compression to chi), ~1e-2..1e-1, i.e. 14+ orders above machine
epsilon — quad/128-bit precision is irrelevant. It is a
Trotter/truncation TRADEOFF, non-monotonic in dt: Trotter error ~
T*dt^2 (falls as dt->0) vs truncation error accumulating with step
count ~ T/dt (rises as dt->0); sum minimized at dt~0.02 (floor
maxabs 0.057) vs 0.337 at dt=0.04 (Trotter) and 0.231 at dt=0.01
(truncation). Root cause = entanglement barrier: free-ghost S(t)
grows, MPS holds only S ~ log(chi) (chi=40 -> ~3.7). Refining dt
BACKFIRES (more truncations, no more room); the only real knob is
CHI (chi=64/dt=0.02 test pending). For an EXACT integrator (ED,
no truncation) the naive "smaller dt always better" DOES hold —
which is exactly why paper 5's CORE verdict rests on ED+Schur, not
MPS; MPS is the large-L vehicle only. Paper-5 methods para should
state this barrier honestly.

**(2) Model-switch operational facts (Claude Code).** Switching the
MODEL on the same session PRESERVES context (full history re-read /
re-cached for the new model; one-time slower+pricier first message
=> BATCH Fable work, don't flip-flop). Switching ACCOUNTS / a fresh
session LOSES the conversation (only disk artifacts carry). Per-turn
THINKING is ephemeral (not persisted cross-turn) regardless — hence
the discipline of writing conclusions to notes/HANDOFF/commits.
Running shells + monitors survive a model-switch.

All other conversational threads (BH/big-bang applicability + the
Horowitz-Maldacena BH-final-state thread; the two-slice/memory
framing; MWI mind-blowing/both-vertigos framing) are already logged
(notes entries + paper9 skeleton TODOs + scout sidecars). Agent
reports archived under histories/agent-reports/ (raw mostly purged;
pivotal pass-9 referee reconstructed in full).

**Compute cleanup 2026-07-12 ~18:20:** killed leftover LOCAL
diagnostic (PID 87372, t5_floor_diag floorchi64 64 0.01, ~6.6h CPU)
- redundant: chi=64 at dt=0.01 (the truncation-dominated side),
superseded by the definitive chi=64/dt=0.02 run on the lab server.
Local machine now clean (0 python jobs). Server chi=64/dt=0.02
floor+ghost still running (see HANDOFF.md compute-watch block).

## 2026-07-12 — FABLE RESUMED: THE SIGMA_MAX CONVENTION RESOLVED
## (shared pass-9 F2, papers 4+6+proposal+scripts+registry)

The queue's shared item, done first and once. Design (all three new
claims VERIFIED numerically in scratch before entering any text,
then re-verified in the public scripts):

**(1) Definition + justification (the referee's demands a+b):**
sigma_max(t) = largest singular value of U(t). C = U/sigma_max is
the MINIMAL contraction normalization: a unitary (Halmos) dilation
exists exactly when the normalized evolution is a contraction, so
sigma_max is the pointwise-least normalization admitting a
conservative completion — the unique choice that discards no
survival probability beyond what the dynamics itself loses
(||C(t)|| = 1: the least-decaying state is unconditioned at every
time).

**(2) Invariance split (M1 vs M2):** divisor entry SIGNS invariant
under every positive scalar renormalization c(t) (M1/negativity
convention-FREE; measured: 0 sign mismatches over the s-grid);
divisor COLUMN SUMS scale by c^2(s)/c^2(s+tau) (M2 onset moves:
0.490 minimal vs 0.820 under c = sigma_max(1+t/2); occurrence
itself is convention-relative).

**(3) NEW RESULT — the minimality dichotomy (turns the convention-
dependence into physics):** for the k=2 cell with coupling kappa
the raw |U|^2 divisor column sum is EXACTLY 1 + kappa^2(T^2-s^2)
(verified to 8 digits), so a renormalization avoids the crossing at
ALL step pairs only if c^2(t) >= c^2(0) e^{kappa^2 t^2} (necessity
by telescoping products, no smoothness needed), and the Gaussian
envelope c^2 = sigma_max^2 e^{kappa^2 t^2} DOES avoid it (measured
max col sum 0.992762 over the pair grid; e^{-x}(1+x) <= 1).
Divisibility is purchasable, but only at divergent conditioning
overhead c^2/sigma_max^2 (2.72/8.1e3/7.2e10 at t=1/3/5) — i.e.,
only by conditioning away survival probability at a Gaussian rate
against polynomially growing dynamics. Under minimal conditioning
the crossing is unavoidable.

**(4) NEW RESULT — sigma_max is INTENSITY-ACCESSIBLE for the
triangular device (dissolves the observable half of pass-9 F3):**
for lower-triangular U, U^dag U has diagonal = measured column
intensity sums and off-diagonal modulus sqrt(Ghat21*Ghat22), so
sigma_max^2(z) = largest eigenvalue of a matrix built from the
measured intensities ALONE (no phase-resolved characterization).
Exact at triangularity (rel err 6e-16 over the ladder); under
asymmetry imperfection Weyl-bounded by the measured residual entry
sqrt(Ghat11*Ghat12): at eta = 3%J worst |Delta sigma^2| = 4.97e-3
vs bound 5.39e-3, relative 5.1e-3, ZERO violations. The D5
column-sum observable is intensity-only with a data-driven
systematic bound. (F3's feasibility-citation half still open,
queued with the paper-6 rescope.)

**Propagation (all surfaces):** paper6 Sec-3 conventions paragraph
(also discharges F10's restate-conventions nit) + intro flag + D5
section (convention flag + intensity-accessibility); paper5
"what survives" (minimality justification + invariance split +
dichotomy) + abstract flag; proposal v1.1 D5 paragraph (convention
+ intensity route + Weyl bound); TRILEMMA_REGISTRY.md conventions
note; scripts t4_jordan_process.py [3b], p6_divisor_gate.py [4],
p6_d4_device.py [1c] (all rerun clean, outputs above). All three
TeX docs recompiled clean (11pp/12pp/4pp).

Gate counters: papers 4 and 6 both remain at 0 (content changed);
loops still PAUSED pending the remaining queue items (paper-6 F1
rescope next).

## 2026-07-12 — PAPER 6 PASS-9 RESCOPING DONE (v0.2, 13pp): THE
## SECOND CHANNEL (new computation, p6_m2_channel.py)

The pass-9 open question ("does M2 detect the size-4 IK corner?")
answered YES, and better: full ledger in
histories/paper6-history.md (v0.2 entry). Headlines:
- M2 (column-sum) channel fires at EVERY split phase incl. the
  whole M1-silent set (onsets 0.30-0.68, |delta|=0.6); imaginary-
  axis onset ASYMMETRY 0.68 (+i, growing) vs 0.30 (-i, decaying),
  robust at |delta|=0.3 and tau=0.02: the second channel reads the
  sign negativity is blind to. (M2 convention-relative per the
  sigma_max resolution; M1 convention-free.)
- The IK corner is a SIZE-4 block, so Thm-k2 negativity fires
  regardless of direction: M1 onset = first grid point past
  tau/(sqrt3-1) EXACTLY (0.07 vs 0.0683 at tau=.05; 0.03 vs 0.0273
  at tau=.02) for pure/phi=pi/phi=0 alike; M2 onsets direction-
  split 0.80/0.91/0.73. The bond-level silent set never applied to
  the corner. Referee's "spectrometer misses the flagship ghost"
  dissolves: two channels, no silent direction.
- Title rescoped ("...a two-channel photonic readout"); F3
  feasibility citation = Weidemann et al. Science 368, 311 (2020)
  (verified via web, authors+journal+pages; no arXiv preprint
  found — biblio agent should re-verify); F4 anchored on
  Companion4's sector-tower irreducibility; F5-F9, F11 applied
  (measured->computed sweep, band-asymptotics label, z_c precision
  scoping, phase-halving map, Landau disclaimer).
Counter stays 0; pass 10 (three fresh agents) launching next.

## 2026-07-12 — PAPER 4 GATE-PASS-1 RESCOPE DONE (v0.4, 13pp)

Full ledger: histories/paper5-history.md (v0.4 entry). Headlines:
- alpha_g gap CLOSED BY AN EXPLICIT NATURALNESS PRIOR (new
  paragraph): evasion window |alpha_g| ~ 1e13..1e109 (lab-scale
  content returns at 1e13, 100-MeV cutoff at 1e40 via Lambda ~
  alpha^{2/5}) is unadvocated + excluded as a stated prior;
  honest negative: observational closure NOT available (density
  substitution = fifth-root tightening only, factor ~10).
- sqrt5/2 DERIVED (chain-eigenvector pair difference
  delta*(0,i,i,-2) vs (1,i,-i,-1): angle = sqrt(5)/2 delta) and
  cond*angle -> sqrt5 measured 2.2363: cond=2/delta and the angle
  law are ONE law. Emitted in t4_ep_dictionary.py [1b]; prefactors
  1/(k-1)! emitted in t4_jordan_process.py [1].
- F4 hedged to free/kinematic; bounded-inverse metric; norm-1
  dropped; provably->proof-pointer; version v0.4.
Paper 6 pass 10 running concurrently (3 fresh Fable agents);
paper 4 pass 2 launching now. Both counters 0.

## 2026-07-12 — PASSES LANDED: p6 pass 10 + p5 pass 2, all findings
## fixed same-session (full ledgers in the history sidecars)

Paper 6 pass 10: 14 findings. THE MAJOR: the D5 MC least-squares
fit was UNINFORMATIVE on the balanced device (params pinned at
initialization; corr(etahat,eta)=0.02-0.05 across two seeds) — the
quoted "eta resolved +-0.0075" and "z_c +-0.015" were PRIOR
ECHOES. Fixed with closed-form calibration-free estimators
(J +0.5%+-1.7%, corr 0.74; z_c +-0.040 cm; eta certified via
window cleanliness + z* + Weyl residual, non-recovery printed as
permanent control). NEW GATE-CHECKLIST CANDIDATE: MC resolution
claims need truth-estimate CORRELATIONS, not spreads. Claims
MAJOR: universal quantifiers on sampled scans — public scan
densified to 5 deg (72 phases, 0 silent), corner
direction-independence split theorem-vs-computed (12-phase scan,
onset 0.070 at every phase). 0.486 now emitted by scripts on both
paper stacks (root of 2t sigma^2 = (sigma^2)': 0.4859). Smilga
title -> published "Giving" (Crossref DOI verified; reverses
pass-7's arXiv-based choice with the stronger source).

Paper 4 pass 2: 13 findings, ZERO critical/major, all proofs
re-derived clean, 54/54 numbers trace. Fixes: four-scripts count,
0.486 defining equation in-text + emitted, Claim 6.1 boundedness
qualifier, sigma_max flag in the Measured inventory, honest 3e12
meV threshold, linearized qualifier in abstract, tower bridge
sentence, "we argue" hedge, de-quoted BM paraphrase, Smilga
"Giving".

Both papers recompiled clean (13 pp each); proposal updated
(z* protocol labeling + honest MC claims) and recompiled (4 pp).
Counters both 0. Paper 6 PASS 11 + paper 4 PASS 3 launching with
fresh agents. Compute watch still armed (chi=64 job running).

## 2026-07-12 — PASSES LANDED: p6 pass 11 (NEAR-CLEAN: biblio +
## numerics both CLEAN, claims 2 minor + 7 nit) + p5 pass 3
## (1 major quantifier + biblio mis-anchors). ALL FIXED same
## session; full ledgers in the history sidecars.

Highlights: p6's two CLEAN lanes are the first in the corpus under
the strict gate; its claims findings were pure hygiene (deep
JORDAN cascade qualifier, Thm-2 eigenvalue clause, code-avail
scoping + D4-det print, prob-one regraded exact, t_c collision).
p5's major: post-lemma corollary universality qualified (finite-
dim / bounded-inverse). Crossref-verified title reversals: GSTZ
"metastable" (error-4.8's earlier fix had verified the arXiv
form!), IK "Ghost-turned tachyon" (reverses pass-10's arXiv-based
hyphenation) — both propagated corpus-wide with %-comment evidence.
Proximity literature engaged: FTT 2506.21400 + Dey-Fring
2603.15395 cited & differentiated in paper 4; Holdom 2408.04089 +
Kuntz 2410.08278 + FTT + Dey-Fring added as PENDING registry rows
(no horn claims without careful reads). alpha_g two-route matching
now script-emitted. LESSON (gate-checklist candidate): "verified
directly" against arXiv is NOT verification of a JOURNAL-FIRST
bibitem — published-title checks must hit the publisher record
(Crossref), not the preprint.

Recompiled: p5 14pp, p6 13pp, p3 20pp (GSTZ propagation). Counters
both 0. Launching p6 PASS 12 + p5 PASS 4 on OPUS agents (user
directive: audit agents on Opus via model override; Fable reserved
for authoring + the final K-1 confirming pass).

## 2026-07-12 — SESSION WIND-DOWN (user: session limit ~2.5h; no
## new passes; running agents allowed to finish)

State at wind-down (all applied work committed + pushed to Gitea):
- PAPER 6: pass 12 COMPLETE and applied (biblio CLEAN, numerics
  CLEAN ~120/120, claims 2 minor + 2 nit — fixed: "fires
  everywhere"->sampled; corr(Dhat,Delta)=0.86 now PRINTED by
  p6_d4_device.py and cited in-text; abstract no-free-params split;
  generic-direction statement upgraded to analytic). Counter 0.
  PASS 13 NOT LAUNCHED (hold). On resume: 3 Opus agents, same
  prompt shape as pass 12 (see sidecar).
- PAPER 4: pass 4 complete + applied earlier; PASS 5 RUNNING at
  wind-down (3 Opus agents; biblio lane already returned CLEAN —
  first clean p5 lane; claims + numerics pending). Apply any
  findings on arrival; then hold (no pass 6 until user returns).
- PAPER 1: gate PASS 1 RUNNING (claims lane returned: 2 MINOR +
  1 NIT, no critical/major, all 8 theorem groups re-derived clean —
  same-space qualifier for abstract (i); 1-D-monotone scope for the
  explosion dictionary in abstract/intro; WKB approx-vs-exact in
  Thm 6.1's one-line identity. HELD until numerics + biblio lanes
  report, then apply all three lanes together). Numerics lane
  running (19 scripts); biblio lane resumed after a stalled
  sub-batch (its early leak: no refuting prior art; engagement
  candidates Errasti Diez et al. 2408.16832 / Held 2509.18049 —
  VERIFY before citing).
- PAPER 1 biblio lane LANDED (2 MAJOR + 1 MAJOR-engagement +
  3 MINOR; zero chimeras, all 46 items verified, novelty survives):
  "Mendas"->MENDE (Crossref-verified: Carreau/Farhi/Gutmann/Mende,
  DOI 10.1016/0003-4916(90)90125-8); InvertedHO2026 arXiv:2606.05125
  authors ADD (verified: Ji, Schuettelkopf, Bazhan, Cataldini,
  Tajik, Moller, Mazets, Erne, Schmiedmayer); engage Errasti
  Diez-Gaset Rifa-Staudt arXiv:2408.16832 + Held arXiv:2509.18049
  (both arXiv-verified; the claimed Fortschr.Phys. version of
  2408.16832 NOT yet Crossref-verified - cite arXiv-only unless
  confirmed); Mostafazadeh JMP 43,205 subtitle (Crossref-verified);
  ChruscinskiRS2018 attribution fix + ADD Rivas OSID 29, 2250012
  (2022) arXiv:2209.03584 (verified incl. jref); Pimenta framing
  reword. ALL VERIFICATIONS DONE this session — apply directly
  once the p1 numerics lane lands (do not re-verify).
- If agents DIE at the session limit before reporting: relaunch
  that lane fresh on resume (same prompt structure; reports are
  session-scoped, nothing on disk is lost).
- Compute: chi=64/dt=0.02 floor+ghost STILL RUNNING on
  the lab server (launched 17:40, CPU ~2.5h/worker at last check —
  heavier per step than the naive ETA assumed; job is detached and
  survives everything). Re-check per HANDOFF compute block; the
  session-scoped monitor dies with this window — REARM on resume.

## 2026-07-12 ~20:5x — CHI=64 VERDICT: MPS IS BARRIER-LIMITED
## (the fork resolves to the honest-methods-limit branch)

chi=64/dt=0.02, L=16, the lab server (walltime ~11,200 s each):
  floor (lam=0.00): maxabs_dE = 6.2245e-02, dE_end/site = 5.65e-03
  ghost (lam=0.06): maxabs_dE = 9.9534e-02, dE_end/site = 1.21e-02
DECISION (pre-registered rule, HANDOFF compute block): floor
6.22e-2 vs the chi=40/dt=0.02 sweet-spot floor 5.7e-2 — the floor
DID NOT DROP under a 60% bond-dimension increase (log-chi capacity
+13%; within run variation, slightly worse). => The free-ghost
entanglement growth saturates chi at any reachable value; refining
chi is as futile as refining dt was. MPS IS THE WRONG TOOL for the
large-L volume extension at this coupling.

PAPER-5 CONSEQUENCES (per the standing fork):
- CORE verdict (a) — renormalized multiplicity survives — rests on
  ED + Schur folding (0.988-1.000): UNAFFECTED.
- MPS role: 4th cross-check + L=16 certification ONLY. NO chi>=64
  volume sweep. Methods section states the entanglement barrier
  honestly: Trotter/truncation tradeoff floor (dt sweep
  0.337/0.057/0.231 at dt=0.04/0.02/0.01, chi=40) + chi saturation
  (0.057 -> 0.062 at chi 40 -> 64): the floor is a BARRIER
  (S ~ log chi vs linear S(t) growth), not a precision issue.
- Ghost/floor separation at chi=64 is ~1.6x (0.0995/0.0622) at
  lam=0.06 — consistent with the chi=40 picture (only lam=0.12
  separates cleanly).
PAPER 5 DRAFTING IS NOW UNBLOCKED (ED/Schur verdict + L=16
certification + barrier-limit methods paragraph, from the
2026-07-12 conversation-sweep physics notes).

Server cleaned: all python3.11 procs killed post-verdict (0
remain). Compute block in HANDOFF is CLOSED.

## 2026-07-13 — AUDIT.md + PROVENANCE-NOTE AUDIT SENTENCE
## (user-directed: public audit-process doc + page-2 note)

AUDIT.md created at repo root (public-facing: the K=2 gate, the
three fresh lanes, the strict clean definition + escalation
clause, verify-before-apply w/ publisher-record rule, cross-model
verification, the full failure-mode checklist grown from caught
errors, what-it-is-not framing). assemble_repos.ps1 ships it into
each paper repo. The provenance note in every paper gains one
sentence (audit gate + pointer to AUDIT.md/histories/): applied
NOW to papers 2, 3, 5, 8 (not under audit; all recompiled).
QUEUED for papers 1, 4, 6 the moment their current passes land.
COUNTER RULING (user, 2026-07-13): the sentence is administrative
boilerplate (no claims about results/math/numbers/references) and
does NOT reset counters — boilerplate exception added to
release-gate.md rule 3, tightly bounded (identical-across-papers +
no technical claims + ledger-logged). p5's counter-1 SURVIVES the
sentence landing. Anything technical still resets, no exceptions.

## 2026-07-13 — MILESTONE: PAPER 4 COUNTER = 1 (first counter
## movement in the corpus). PASS 8 = FABLE CONFIRMING PASS.

p5 pass 7 (Opus): claims CLEAN + biblio CLEAN + numerics CLEAN on
manuscript/scripts; sole finding = one-token rounding in the CITED
PROVENANCE DOC (fixed). ADJUDICATION under the user-set rule
("zero findings requiring a change to the manuscript or scripts"):
the doc is neither => pass 7 CLEAN by the rule's letter; counter
0 -> 1. Disclosed to user in-session and in the p5 sidecar; if the
stricter reproducibility-chain reading is preferred, reset is
one line. Pass 8 launches on FABLE agents (K-1 confirming pass);
if clean, p5 is release-eligible pending the publish hold +
hold-lift corpus sweep.

p6 pass 14: numerics CLEAN (3rd straight), Mandal CITE applied +
novelty claim narrowed, full Delta->delta split rename (abstract
through Sec 5 + proposal ripple). Counter 0; pass 15 (Opus).
p1 pass 4 running (Opus x3).

## 2026-07-13 — PAPERS 6/7/8 REPO NAMING + COVER PROMPTS
## (user-directed; handed to user for rendering)

Repo names: paper 6 = **unfolded-ghosts** (USER-CONFIRMED
2026-07-13); paper 7 =
**exorcised-ghosts** (alternates priced-/masked-); paper 8 =
**many-ghosts** (alternates everett-/branching-). Series arc:
indivisible -> instantaneous -> conditioned -> degenerate ->
renormalized -> unfolded -> exorcised -> many.

Three chalkboard-series prompts handed to user (full text in the
session record; anchors summarized): p6 = ridge/"the pure theory
is the boundary" banner + direction fan (phi=0/pi oscillate rays)
+ omega->0 corner tumble + two-dial instrument (negativity dial
with 15.3-deg silent cone / column-sum dial no silent region) +
Bessel-band barcode 5.269/12.949/24.042 + two waveguide chips
(EP coupler, one-way pair, z_c=0.91cm) + moral "every neighbor
picks a side; the divisor says which." p8 = "every exorcism has a
price" banner + future-boundary door + cashier receipt
(survival sqrt-delta / fidelity sqrt-delta / total at delta->0:
everything) + two-sheet fold (second sheet unconditioned particle
/ first sheet conditioned ghost — DO NOT SWAP pin) + mask stack
sinh^2(Gamma t/2) + moral = the sheet slogan. p9 = "an
interpretation experiment" banner + same-ghost-on-every-branch
tree + horn-3-paid-willingly door + LEVEL underdetermination
scale + bookkeeping objection in wastebasket + Born-intact dice
vs crossed-out nonequilibrium die + DASHED "division event?"
link pinned "conjecture only" (load-bearing honesty pin) + moral
"the ghosts don't care which story you tell — that is the
result." All labels pinned verbatim; no realistic physics curves
(v3 lesson); pin-everything discipline per the renormalized-v4
ledger lesson.

## 2026-07-13 — RESUMED: ALL THREE LOOPS RELAUNCHED (Opus) +
## PAPER 5 v0.1 DRAFTED (7pp, compiles clean)

Session resumed post-limit. p1 pass-2 leftover (Maslov
"conjecturally") applied pre-launch. Launched: p1 pass 3, p5 pass
6, p6 pass 13 (9 Opus agents) + a paper-5 inventory Explore agent.

**PAPER 5 DRAFTED (paper7/main.tex, v0.1):** "The multiplicity
horn survives renormalization: exact quantum evolution of a
ghost-normal field theory, the folded channel sum, and an
entanglement barrier." Structure: provenance note; intro w/
pre-registered fork (a)/(b); model + channel census (10/21/36/55;
calibration 5.7e-16); THE VERDICT TABLE (full/Schur 0.988-1.000
across M<=16/caps/couplings while full/naive slides 0.995->0.774;
lambda^2 = Z<1 identification; cap convergence; d=2 spot 1.0000);
mechanism-by-elimination section (shell-shell splitting; the
failed vertex-prediction logged); dimension ladder (P1
saturation, P2 log-class evidence exponent 0.156 NOT claimed as
converged asymptote, P3 power 2.263~2 one-shell-deep); MPS
section (gate 2-6e-6; chi=40/dt=0.02 sweet spot; dt
non-monotonicity 0.337/0.057/0.231; chi=64 verdict 0.062 vs
0.057 = saturation per pre-registered rule; NO volume claim;
lam=0.12 separation labeled diagnostic-ladder); prior art from
the overlap sidecar w/ AUDIT-HYGIENE MARKERS on all unverified
bibitem metadata (Lagnese/Abel-Spannowsky-Williams/Burshtein-
Goldstein/Garriga-Vilenkin flagged [to be verified at audit], NO
guessed metadata); strength-graded discussion. chi=64 result
files transcribed into scripts/ (diag_floor_c64_dt02.txt,
diag_ghost_c64_dt02.txt) from the server capture for
reproducibility. Gate counter: 0 (fresh draft, not yet audited).

**Landed lanes so far this round:** p5 pass-6 numerics CLEAN
(55/55); p6 pass-13 biblio CLEAN (optional hardening note: cite
Mandal 2603.25603 near novelty claim A — hold as optional); p1
pass-3 biblio: 1 MINOR across 49 items (Z2experiments first
author T. Liu not X. Liu — Crossref-verified Tingzhi Liu, fix
HELD until p1 claims+numerics lanes land), novelty survives 3rd
sweep, optional neighbor 2604.21826 noted. Two biblio agents
stalled on dead sub-batches and were nudged to finish directly
(recurring failure mode: sub-batch spawning from audit agents —
future prompts should forbid sub-agent spawning for biblio
verification).

## 2026-07-13 — RESCOPE-INTEGRITY RE-AUDIT (p6 + p5): the applied
## rescope HOLDS under fresh adversarial confirmation. CLEAN, no edits.

User-directed, in lieu of the "held rescoping" step (which was found
already APPLIED long ago: p6 v0.2/pass-9, p5 v0.4/gate-pass-1). This
is an UNCOUNTED integrity check, not a counter pass — counters
unchanged (p6 = 1, p5 = 0). Two hostile-referee agents (Opus x1 each,
disjoint files, no histories/notes access — original findings supplied
verbatim as the checklist), each re-derived the fix sites AND re-ran
the scripts.

PAPER 6 — all four original referee findings RESOLVED:
- F1 (CRIT, "reads out the direction" oversold): title = "two-channel
  photonic readout"; negativity scoped to Re(delta) with explicit
  silent sector; IK/+i ray placed IN the silent set; M2 second channel
  re-run (p6_m2_channel.py): fires at every sampled phase (+i 0.68 /
  -i 0.30 / EP 0.48; 72-phase 5-deg scan, 0 silent); size-4 IK corner
  caught by Thm-k2 regardless of direction (M1 onset 0.070 at every
  unfolding). "sampled" hedge present at every no-silent-direction site.
- F2 (MAJOR, sigma_max convention): sigma_max defined, pointwise-least
  justification correct, flagged at every M2 site incl. D5 lab section.
- F3 (MAJOR, D5 feasibility + intensity-accessibility): Weidemann et al.
  Science 368 at the load-bearing site; triangular-device intensity
  reconstruction argument given + algebra verified + p6_d4_device.py
  reproduces accuracy (6e-16 at eta=0; 5.1e-3 vs Weyl 5.39e-3 at 3%).
- F4 (MAJOR, "as a matter of theorem"): now scoped to a single
  irreducible block; reducible carve-out stated. Honest residue:
  block-irreducibility remains an imported (Companion4) premise — the
  finding's criterion permits this; the tower conclusion is no longer
  presented as unconditional.
No new oversold phrasing anywhere. Overall: theses read
established-not-asserted.

PAPER 4 — all findings RESOLVED:
- F1 (MAJOR, alpha_g fork non-exhaustive): evasion window named
  (3e12 <~ |alpha_g| << 1e109), excluded as an explicitly STATED prior
  (not by data); observational non-closure volunteered (fifth-root /
  factor-~10); abstract + horn-1 bullet + closing all separate
  branch-death from window-exclusion; alpha_g^{2/5} arithmetic
  consistent (meV~3e12, 100 MeV~1e40, vacuous~1e109).
- F2 (MAJOR, shared sigma_max): flagged at abstract/body/Measured
  inventory; minimality justification correct; Fock tower kept distinct
  (no finite-dim convention leaks upward).
- F2/F3-coeff: sqrt5/2 derived in-text; one-law framing; t4_ep_
  dictionary.py [1b] emits cond*angle = 2.2363 vs sqrt5 = 2.2361.
Only borderline site (intro summary line + Table 1 horn-1 cell omit the
window) judged acceptable summary compression — the governing bullet two
paragraphs above carries the qualifier. No residue.

META data point: a rescope that survived 15+ subsequent hygiene passes
ALSO survives a targeted adversarial re-read of just the rescoped
theses — evidence the pass-9/gate-pass-1 rescoping was durable, not
merely locally patched. Logged for the meta-paper (rescope-durability).
