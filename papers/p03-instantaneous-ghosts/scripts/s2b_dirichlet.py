"""
S2b -- the third completion: Dirichlet walls. Completes the
infinity-channel taxonomy of s2_infinity_channel.py: three
completions of the same interior Hamiltonian, three distinct
direction-resolved signatures at the boundary detectors.

  PERIODIC (wormhole):  Bob-LEFT fires (J>0 at x=-L+3: inbound from
                        the left boundary = through infinity).
  DIRICHLET (walls):    Bob-RIGHT fires (J<0 at x=+L-3: inbound
                        from the right wall = reflection off
                        infinity); Bob-LEFT stays silent.
  ABSORBING (minimal):  both silent; norm -> 0.

V = -x^4 (explosive class), bit=0 (Alice's barrier off), L = 8/10/12.
Dirichlet evolution via sine-transform split-step (DST-I on interior
nodes: exact hard walls, unitary).

Run:  python scripts/s2b_dirichlet.py    (~2-4 minutes)
"""

import numpy as np
from scipy.fft import dst, idst

NGRID, X0, SIG, JTHRESH = 2046, 3.0, 0.6, 1e-3


def run_dirichlet(L):
    N = NGRID
    x = np.linspace(-L, L, N + 2)[1:-1]          # interior nodes
    dx = x[1] - x[0]
    kn = np.pi * np.arange(1, N + 1) / (2 * L)   # DST-I eigenmodes
    V = (-x**4).astype(complex)
    vmax = np.max(np.abs(V))
    dt = min(0.3 / max(vmax, np.max(kn**2) / 2 * 0), 2e-4)
    dt = min(0.3 / vmax, 2e-4)
    psi = np.exp(-(x - X0) ** 2 / (2 * SIG**2)).astype(complex)
    psi /= np.sqrt(np.sum(np.abs(psi) ** 2) * dx)
    expV = np.exp(-1j * V * dt / 2)
    expK = np.exp(-1j * (kn**2 / 2) * dt)
    iL = np.argmin(np.abs(x - (-L + 3.0)))       # Bob-LEFT
    iR = np.argmin(np.abs(x - (L - 3.0)))        # Bob-RIGHT
    t, tmax = 0.0, 3.0
    tL = tR = np.inf
    check = max(1, int(0.01 / dt))
    step = 0
    while t < tmax:
        psi = expV * psi
        a = dst(psi.real, type=1) + 1j * dst(psi.imag, type=1)
        a *= expK
        psi = (idst(a.real, type=1) + 1j * idst(a.imag, type=1))
        psi = expV * psi
        t += dt
        step += 1
        if step % check == 0:
            JL = np.imag(np.conj(psi[iL])
                         * (psi[iL + 1] - psi[iL - 1]) / (2 * dx))
            JR = np.imag(np.conj(psi[iR])
                         * (psi[iR + 1] - psi[iR - 1]) / (2 * dx))
            if JL > JTHRESH and not np.isfinite(tL):
                tL = t
            if JR < -JTHRESH and not np.isfinite(tR):
                tR = t
    norm = np.sum(np.abs(psi) ** 2) * dx
    return tL, tR, norm


print("=" * 68)
print("S2b: DIRICHLET completion, V=-x^4, bit=0")
print("prediction: Bob-RIGHT fires (reflection off infinity),")
print("Bob-LEFT silent, norm conserved")
print("=" * 68)
print(f"{'L':>4} | {'t_B left':>9} {'t_B right':>10} {'norm':>7}")
for L in (8, 10, 12):
    tL, tR, nm = run_dirichlet(L)
    fL = f"{tL:9.3f}" if np.isfinite(tL) else f"{'--':>9}"
    fR = f"{tR:10.3f}" if np.isfinite(tR) else f"{'--':>10}"
    print(f"{L:>4} | {fL} {fR} {nm:>7.3f}")
print()
print("taxonomy (with s2_infinity_channel.py): wormhole -> left;")
print("Dirichlet -> right; minimal -> silence. Three completions of")
print("one Hamiltonian, three signatures: the completion is the")
print("physics.")
print("done.")
