"""
T4 kickoff: the dictionary cost of quadratic/conformal gravity, mode by
mode -- the equal-frequency Pais-Uhlenbeck exceptional point as field
kinematics.

Facts this script quantifies:
(1) The PU first-order mode matrix A(omega1, omega2) (one field mode of
    fourth-order gravity) has an exceptional point at equal frequencies:
    eigenvalues +-i*omega1, +-i*omega2 merge into two 2x2 Jordan blocks.
    We measure the eigenvector-matrix condition number cond(V) ~
    delta^(-alpha) as delta = omega1 - omega2 -> 0 and fit alpha: the
    per-mode cost of a similarity dictionary with a normal target built
    on the mode decomposition, up to O(1) (normal modes, isospectral
    Hermitian partner, Bender-Mannheim map at quadratic level),
    diverges with this power.
(2) Dispersion sweep: for Stelle-type quadratic gravity, omega1 = k,
    omega2 = sqrt(k^2 + m2^2): delta(k) ~ m2^2/(2k) -> 0 in the UV, so
    the dictionary cost GROWS with k as a power we fit -- massive
    quadratic gravity approaches the exceptional line in the UV.
    Conformal (Weyl) gravity has m2 = 0: delta(k) = 0 identically --
    every mode sits exactly AT the EP (the 1/k^4 double pole).
(3) Process-side control: the Hermitian Ostrogradski realization on an
    (x, xdot) grid remains exactly unitary / doubly stochastic AT the
    EP (companion [indivisible], Sec. 5; re-verified here on a smaller
    grid): the
    stochastic-process description does not see the EP; only the
    similarity dictionary does.

Controls: far-from-EP cond(V) = O(1); exact-EP defectiveness (numerical
rank of eigenvector matrix); doubly-stochastic check at delta = 0.
ASCII only; numpy/scipy.
"""

import numpy as np
from scipy.linalg import expm, eig

GAMMA = 1.0


def mode_matrix(w1, w2, gamma=GAMMA):
    """First-order PU evolution: d/dt (q1,q2,p1,p2) = A (q1,q2,p1,p2).
    q1 = x, q2 = xdot (Ostrogradski)."""
    return np.array([
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0 / gamma],
        [gamma * w1 ** 2 * w2 ** 2, 0.0, 0.0, 0.0],
        [0.0, -gamma * (w1 ** 2 + w2 ** 2), -1.0, 0.0]])


def cond_eigvec(A):
    w, V = eig(A)
    return np.linalg.cond(V)


def main():
    print("=" * 72)
    print("T4: dictionary cost of quadratic/conformal gravity at the "
          "PU exceptional point")
    print("=" * 72)

    # ---------------- (1) EP approach: cond(V) vs delta ----------------
    w0 = 1.0
    print("\n[1] cond(V) of the 4x4 mode matrix vs detuning "
          "delta = w1 - w2 (w2 = 1):")
    deltas = np.array([1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6])
    conds = []
    for d in deltas:
        c = cond_eigvec(mode_matrix(w0 + d, w0))
        conds.append(c)
        print("  delta = %.0e : cond(V) = %.3e" % (d, c))
    slope = np.polyfit(np.log(deltas), np.log(conds), 1)[0]
    print("  fitted power: cond(V) ~ delta^%.3f" % slope)
    # control: far from EP
    print("  [ctrl] far from EP (w1=2, w2=1): cond(V) = %.2f (O(1))"
          % cond_eigvec(mode_matrix(2.0, 1.0)))
    # control: exactly at the EP -- defective
    A0 = mode_matrix(w0, w0)
    w, V = eig(A0)
    s = np.linalg.svd(V, compute_uv=False)
    print("  [ctrl] at delta = 0: cond(V) = %.1e; smallest normalized "
          "singular value %.1e" % (s[0] / s[-1], s[-1] / s[0]))
    print("         (numerically defective: Jordan blocks, no "
          "diagonalizing similarity)")

    # ---------------- (1b) the angle law, and its link to cond ---------
    print("\n[1b] eigenvector-angle law and the cond-angle identity "
          "(script-emitted):")
    # The chain eigenvector of the mode matrix for eigenvalue lam is
    # v(lam) = (1, lam, gamma w1^2 w2^2 / lam, gamma lam^2) (rows [0],
    # [1], [2] of A; row [3] is the characteristic constraint). At
    # gamma = 1, w = 1 the merging pair near +i has eigenvectors
    # v(i(1+delta)) and v(i) OF THE SAME detuned matrix; linearizing,
    # their difference is d = delta * (0, i, i, -2) against
    # v = (1, i, -i, -1), so the projective pair angle is
    # sqrt(|d|^2 - |<v,d>|^2/|v|^2)/|v| = delta * sqrt(6-1)/2
    # = (sqrt5/2) delta -- the derived coefficient of the angle law.
    rate = np.sqrt(6.0 - 1.0) / 2.0
    print("  derived pair-angle rate at the EP: sqrt(6-1)/2 = %.6f "
          "(= sqrt5/2 = %.6f)" % (rate, np.sqrt(5) / 2))

    def pair_angle(d):
        w, V = eig(mode_matrix(w0 + d, w0))
        idx = np.argsort(np.abs(w - 1j))[:2]
        u = V[:, idx[0]] / np.linalg.norm(V[:, idx[0]])
        v = V[:, idx[1]] / np.linalg.norm(V[:, idx[1]])
        return np.arccos(min(abs(np.vdot(u, v)), 1.0))

    print("  delta     angle/delta   cond(V)*angle")
    for d in (1e-2, 1e-3, 1e-4):
        th = pair_angle(d)
        c = cond_eigvec(mode_matrix(w0 + d, w0))
        print("  %.0e   %10.5f   %12.4f" % (d, th / d, c * th))
    print("  => angle(pair) = (sqrt5/2) delta (derived above);"
          " cond(V) * angle -> sqrt5 = %.4f:" % np.sqrt(5))
    print("     the 2.00/delta law and the (sqrt5/2) delta angle law "
          "are one statement,")
    print("     cond(V) = sqrt5/angle = 2/delta.")

    # ---------------- (2) dispersion sweep -----------------------------
    print("\n[2] Stelle-type dispersion w1 = k, w2 = sqrt(k^2 + m2^2), "
          "m2 = 1:")
    ks = np.array([1.0, 3.0, 10.0, 30.0, 100.0, 300.0])
    conds_k = []
    for k in ks:
        w2 = np.sqrt(k ** 2 + 1.0)
        c = cond_eigvec(mode_matrix(k, w2))
        conds_k.append(c)
        print("  k = %6.1f : delta(k) = %.3e  cond(V) = %.3e"
              % (k, w2 - k, c))
    slope_k = np.polyfit(np.log(ks[2:]), np.log(conds_k[2:]), 1)[0]
    print("  fitted UV power: cond(V) ~ k^%.3f" % slope_k)
    # units control: same k-scaling with WELL-SEPARATED frequencies
    # isolates the trivial variable-scaling part of cond(V)
    conds_u = [cond_eigvec(mode_matrix(2.0 * k, k)) for k in ks]
    slope_u = np.polyfit(np.log(ks[2:]), np.log(conds_u[2:]), 1)[0]
    print("  [ctrl] units-only control (w1 = 2k, w2 = k): cond(V) ~ "
          "k^%.3f" % slope_u)
    print("  EP-driven excess: k^%.3f (relative detuning delta/k ~ "
          "k^-2, cond ~ (delta/k)^-1" % (slope_k - slope_u))
    print("  on top of the units part)")
    print("  => massive quadratic gravity approaches the exceptional "
          "line mode-by-mode")
    print("     in the UV; conformal gravity (m2 = 0) sits AT it for "
          "every k.")

    # ---------------- (3) process-side control at the EP ---------------
    print("\n[3] Hermitian (Ostrogradski) grid realization AT the EP "
          "(w1 = w2 = 1):")
    N = 20                 # per-axis grid points; dim = N^2 = 400
    L = 7.0
    x = (np.arange(N) - N // 2) * (2 * L / N)
    kvec = np.fft.fftfreq(N, d=(2 * L / N)) * 2 * np.pi
    F = np.fft.fft(np.eye(N), axis=0)
    Finv = np.linalg.inv(F)
    # spectral momentum P = F^-1 diag(k) F, Hermitized
    P = Finv @ np.diag(kvec) @ F
    P = (P + P.conj().T) / 2
    I = np.eye(N)
    X = np.diag(x)
    w1 = w2 = 1.0
    H = (np.kron(P, np.diag(x))                    # p1 q2
         + np.kron(I, P @ P) / (2 * GAMMA)         # p2^2 / 2 gamma
         + GAMMA / 2 * (w1 ** 2 + w2 ** 2) * np.kron(I, X @ X)
         - GAMMA / 2 * w1 ** 2 * w2 ** 2 * np.kron(X @ X, I))
    herm = np.linalg.norm(H - H.conj().T)
    U = expm(-1j * H * 0.7)
    G = np.abs(U) ** 2
    colerr = np.abs(G.sum(axis=0) - 1).max()
    rowerr = np.abs(G.sum(axis=1) - 1).max()
    print("  ||H - H^dag|| = %.2e ; max |col sum - 1| = %.2e ; "
          "max |row sum - 1| = %.2e" % (herm, colerr, rowerr))
    print("  => the process realization is exactly doubly stochastic "
          "AT the exceptional")
    print("     point; the singularity lives only in the similarity "
          "dictionary.")

    print("\ndone.")


if __name__ == '__main__':
    main()
