# Paper 6 — pass 9 skeptical-referee report (reconstructed from
# the session record, 2026-07-12; Opus-era cross-model agent)

Framing: an agent instructed to review as a hostile journal referee
inclined to reject, hunting for oversold claims after eight prior
verification rounds. It re-derived the theorems (all correct) and
found the problems in the CLAIMS, not the calculations. This is the
report that paused paper 6's loop and defined the Fable rescoping
queue. FINDINGS COUNT: 12 (1 critical, 3 major, 5 minor, 3 nit).

## 1. CRITICAL — "the divisor reads out the direction" is oversold;
the negativity readout is blind to the paper's own flagship instability.
The title promises "the divisor reads them out"; the abstract calls it
"a direction spectrometer." But the delivered result is that negativity
recurrence reads out only Re(delta) — the presence of oscillation —
with an entire silent half-plane: the paper itself states the
negativity-free directions are exactly the +i ray and the EP, plus a
closed silent cone about -i. So a GROWING mode (+i ray) and a DECAYING
mode (-i cone) are both negativity-free and indistinguishable by the
negativity readout: the instrument resolves "oscillatory vs not," not
direction. Sharper: the flagship Ilhan-Kovner "ghost-turned-tachyon"
blowup is a purely imaginary split (+i ray), exactly the negativity-
FREE set — so the "direction spectrometer" cannot detect via negativity
the one instability the paper most celebrates. Sec.2 (IK) and Sec.3
(spectrometer) are never reconciled on this. Fix: scope the claim to
"reads out the real part of the split / oscillatory content," place IK
explicitly in the silent set. [Orchestrator note: the divisor's OTHER
channel — M2 mass-creation — may detect IK, but whether it does for the
size-4 corner block is UNVERIFIED and needs a short computation.]

## 2. MAJOR — "conditional mass creation" (column sum crossing one) is
sigma_max-normalization-dependent, presented as physical mechanism +
photonic observable without flagging the convention.
Divisor M = Gamma(s+tau)Gamma(s)^-1 with Gamma = |U/sigma_max|^2, so
M = V(s+tau)V(s)^-1 * [sigma_max^2(s)/sigma_max^2(s+tau)]. The
NEGATIVITY signal (Prop 1) is invariant under that positive scalar —
correct. But the COLUMN SUM is scaled by it, so "column sum crosses
one" (M2 / conditional mass creation) depends on choosing sigma_max =
largest singular value. p6_divisor_gate.py confirms (hard-coded svd[0]
+ M.sum(axis=0).max()>1). Change the normalization and the onset z_c,
even whether crossing occurs, moves. Used as physics AND as the D5 lab
signal. Referee demands: (a) sigma_max defined in-paper (it never is),
(b) justification it is the canonical/physical choice. Robust,
convention-free content is "negativity-free" (Thm k2); "mass-creating"
is convention-relative and should be labeled so. [SHARED with paper 4,
whose k=2 central result is conditional mass creation.]

## 3. MAJOR — D5 (the device realizing the cascade cell) has no
feasibility citation and needs a non-intensity-only observable.
Sec.5 concedes "a dedicated device-feasibility citation will accompany
the proposal at circulation" — a promissory note where the load-bearing
citation should be. Separately, the readout claims to work "from the
intensity transfer matrices," but Gamma = |U/sigma_max|^2 needs
sigma_max of the COMPLEX U, not fixed by intensities alone; the paper
never says how sigma_max(z) is obtained in the lab. Combined with #2,
the central experimental signature rests on an unstated normalization.

## 4. MAJOR — Thm k2's physical payload ("stacked sectors carry mixed
mechanisms as a theorem") assumes the equal-frequency tower contains
IRREDUCIBLE k>=3 Jordan blocks; this is cited, not established.
The theorem is airtight for a single irreducible J_k, k>=3, and the
discussion honestly carves out "a reducible three-level cascade can of
course remain pure." But "whatever realization stacks Jordan blocks of
growing size (the Smilga tower) cannot present a pure mass-creation
process ... as a matter of theorem" is only true if that tower produces
IRREDUCIBLE blocks >=3, not a direct sum of k=2 cells. That
irreducibility is attributed to Smilga/Companion4 by citation, not
shown here. "As a matter of theorem" overreaches.

## 5. MINOR — "phase phi" denotes two different planes across the two
layers. Layer 1: phi = phase of the detuning Delta (of omega_2^2).
Layer 2: phase of the frequency split delta = a + ib. At finite omega
they share a phase; at the corner they do not (IK = "phi=pi" real, yet
split is +i imaginary). The Delta -> sqrt map relating them is never
stated; this is the root of the finding-1 confusion.

## 6. MINOR — "predicts ... with no free parameters" oversells a
reinterpretation. "The map then predicts growth at (sqrt3/2)gamma_b" —
but the map INGESTS IK's own Delta_eff = -3/4 gamma_b^2; the rate is
then algebra. The independent nonlinear integration (rel 5e-12) is the
real corroboration and should carry the "no free parameters" weight,
not "predicts."

## 7. MINOR — "measured" used throughout for numerical SIMULATION,
including the abstract ("measured window edges"). These are floating-
point computations, not measurements; in a paper that also proposes a
real photonic measurement the conflation is confusing. Reserve
"measured" for the lab; use "computed/verified numerically" otherwise.

## 8. MINOR — Fourier-Bessel band convergence presented at near-theorem
strength but is asymptotic + numerical (a dominant-pole heuristic + a
finite table). Honestly hedged as an "argument," but sits among genuine
theorems; label explicitly as asymptotic/numerical, distinct from Thms.

## 9. MINOR — D5's headline z_c quoted more precisely (+-0.015 cm) than
the quantity is defined (0.91 vs 0.97 = 0.06 cm convention shift). The
error budget is measuring the grid, not the physics.

## 10. NIT — inherited conventions never restated in-paper: sigma_max
(largest singular value), the beable basis = configuration basis where
H is triangular, the Gamma = |U|^2 entrywise construction. Given the
paper's "nothing on trust" stance, a one-paragraph statement is warranted.

## 11. NIT — "the conformal point is a phase boundary" is an interpretive
analogy asserted as fact in the title (no Landau order parameter; the
"phases" are dynamical regimes). Defensible usage, flagged only.

## 12. NIT — provenance/status: "v0.1, not yet audited"; author "makes
no claim to comprehension" — honestly disclosed, but shifts the
evidentiary burden onto proofs/scripts, raising the bar on 2-4.

## Referee bottom line
No fatal calculational error; the two theorems are correct and novel
(the Rayleigh-sum/Bessel-zero sign law is the real contribution). But
three central CLAIMS — "the divisor reads out the direction" (1),
"conditional mass creation" as convention-free physical mechanism +
measurable (2-3), and the stacked tower as mixed-mechanism "as a
theorem" (4) — are stated more strongly than the body supports.
Revisable by rescoping, not new physics; must be fixed before the
thesis reads as established rather than asserted.
