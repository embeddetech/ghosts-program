"""
S5 -- the divergence lives in the STATE: an ontology-free observable
carrying the channel-multiplicity dichotomy.

Context (paper 2, flash-ontology remark -> Proposition): event and
mass-density ontologies (GRW flashes, GRWm) have rates that are
functionals of local quantum-state content, not of any choice of
configuration sample space. If the boost-orbit divergence were an
artifact of slice-beables, such ontologies might escape it. It is
not: the particle-number expectation <N(t)> of the evolving vacuum
carries the same [orbit volume] x [reduced integral] structure as
the decay rate. Any event-rate functional proportional to state
content inherits the dichotomy.

Demonstration in the channel toy (same Hamiltonian as E3): vacuum
coupled to M quasi-continua; <N(t)> = sum of excited-level
occupations (a pure state-content observable; here = 1 - survival,
since each decay deposits one excitation -- which is exactly the
point: state content and exit rate are the same bookkeeping).
Predictions: initial growth rate d<N>/dt ~ M*Gamma_1 for the flat
orbit measure (unbounded with channel count) vs converging to a
plateau for the decaying measure g_k ~ e^{-k/4}.

Run:  python scripts/s5_state_divergence.py     (~1 minute)
"""

import numpy as np

G0, WBAND, NB = 0.02, 8.0, 161
RHO = NB / (2 * WBAND)
GAM1 = 2 * np.pi * G0**2 * RHO
Elev = np.linspace(-WBAND, WBAND, NB)


def n_rate(M, cutoff):
    gks = G0 * (np.exp(-np.arange(M) / 4.0) if cutoff else np.ones(M))
    dim = 1 + M * NB
    H = np.zeros((dim, dim))
    for k in range(M):
        i0 = 1 + k * NB
        H[i0:i0 + NB, i0:i0 + NB] = np.diag(Elev)
        H[0, i0:i0 + NB] = gks[k]
        H[i0:i0 + NB, 0] = gks[k]
    w, V = np.linalg.eigh(H)
    c0 = V[0, :]
    gam_pred = 2 * np.pi * np.sum(gks**2) * RHO
    tf = min(2.5 / gam_pred, 0.4 * 2 * np.pi * RHO)
    ts = np.linspace(0.15 * tf, tf, 12)
    # <N(t)> = 1 - |<0|psi(t)>|^2  (all excited levels carry N=1)
    Ns = np.array([1 - np.abs(np.sum(np.abs(c0) ** 2
                                     * np.exp(-1j * w * t))) ** 2
                   for t in ts])
    # exponential-decay fit of the survival <-> initial dN/dt
    sl = -np.polyfit(ts, np.log(1 - Ns), 1)[0]
    return sl, gam_pred


print("=" * 72)
print("S5: d<N>/dt (state-content observable) vs channel count")
print(f"    per-channel golden-rule rate Gamma_1 = {GAM1:.4f}")
print("=" * 72)
print(f"{'M':>4} | {'flat: dN/dt':>12} {'pred M*Gam1':>12} | "
      f"{'cutoff: dN/dt':>13} {'pred':>8}")
for M in (1, 2, 4, 8, 16, 32):
    rf, pf = n_rate(M, cutoff=False)
    rc, pc = n_rate(M, cutoff=True)
    print(f"{M:>4} | {rf:>12.4f} {pf:>12.4f} | {rc:>13.4f} {pc:>8.4f}")
print()
print("=> the growth rate of the STATE'S particle content scales with")
print("   the channel multiplicity (flat measure: unbounded; decaying")
print("   measure: plateau) -- identically to the exit rate. Any")
print("   ontology whose event/density rate is a functional of local")
print("   state content (slices, flashes, mass density) inherits the")
print("   multiplicity/redundancy dichotomy: the divergence lives in")
print("   the state, not in the choice of sample space.")
print("done.")
