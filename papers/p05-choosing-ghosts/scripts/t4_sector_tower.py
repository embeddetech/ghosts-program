"""
T4 strengthening: the Fock tower of the conformal point -- from the
mechanical prototype to the field-level statement.

CLAIM 1 (sector tower; the constructive form of Smilga's
infinite-order exceptional point). Let the one-particle (mode) matrix
be a size-2 Jordan pair A = w*1 + N (N v = u, N u = 0) -- the
equal-frequency PU cell of one conformal-gravity mode. Second
quantization dGamma(A) preserves each M-quantum sector
(dim M+1, basis sym(u^s v^(M-s))), and on it:
    (dGamma(N))^M != 0,   (dGamma(N))^(M+1) = 0,
i.e. the sector carries a SINGLE Jordan block of size M+1 at
eigenvalue M*w: secular growth t^M. The growth degree is unbounded
up the tower -- no truncation escapes, and every truncation level
makes it worse.

CLAIM 2 (verified numerically here at the sector level; the ell^2
bounded-dictionary theorem is proved in the paper). Column-
stochasticity of |V|^2 forces unit column norms ||V(t) e_j|| = 1;
a bounded-invertible dictionary cannot hide the growing Jordan
direction from every basis vector (duality), so no closed
stochastic representation exists on the Fock space of even ONE
conformal mode, for ANY bounded metric/similarity.

Checks:
 [1] Jordan structure per sector M = 1..8: nilpotent ranks
     (rank((dGamma(N))^M) = 1, (dGamma(N))^(M+1) = 0), geometric
     multiplicity 1.
 [2] growth exponents: ||exp(-i dGamma(A) t)|| ~ t^M per sector
     (fitted).
 [3] unit-column violation, demonstrated: random bounded S on a
     truncated tower (sectors 0..M_max); max_j ||V(t) e_j|| grows
     without bound in t while column-stochasticity would demand 1.
 [4] control: healthy (diagonalizable, equal frequencies but
     DIAGONAL) one-particle matrix -> every sector diagonalizable,
     ||exp(-i dGamma(A) t)|| = 1 exactly at all t.

ASCII only; numpy/scipy.
"""

import numpy as np
from scipy.linalg import expm
from math import comb, sqrt

rng = np.random.default_rng(7)


def dGamma_sector(A2, M):
    """Second quantization of a 2x2 one-particle matrix A2 on the
    M-boson sector. Basis: |s> = sym(u^s v^(M-s)), s = 0..M, i.e.
    occupation (n_u, n_v) = (s, M-s), normalized Fock states.
    dGamma(A) = sum_{ab} A_ab  a_a^dag a_b  with modes (u=0, v=1)."""
    dim = M + 1
    H = np.zeros((dim, dim), dtype=complex)
    for s in range(dim):
        nu, nv = s, M - s
        # diagonal: A00*nu + A11*nv
        H[s, s] += A2[0, 0] * nu + A2[1, 1] * nv
        # A01 a_u^dag a_v : (nu,nv) -> (nu+1, nv-1)
        if nv >= 1 and s + 1 <= M:
            H[s + 1, s] += A2[0, 1] * sqrt((nu + 1) * nv)
        # A10 a_v^dag a_u : (nu,nv) -> (nu-1, nv+1)
        if nu >= 1:
            H[s - 1, s] += A2[1, 0] * sqrt(nu * (M - s + 1))
    return H


def main():
    print("=" * 72)
    print("T4 strengthening: the Fock tower of the conformal point")
    print("=" * 72)

    w = 1.0
    A_jordan = np.array([[w, 1.0], [0.0, w]], dtype=complex)  # N v = u
    A_healthy = np.array([[w, 0.0], [0.0, w]], dtype=complex)

    # ---------------- [1] Jordan structure per sector -------------------
    print("\n[1] sector Jordan structure (one-particle J_2 => sector "
          "J_{M+1}):")
    ok = True
    for M in range(1, 9):
        H = dGamma_sector(A_jordan, M)
        Nn = H - M * w * np.eye(M + 1)      # nilpotent part
        rM = np.linalg.matrix_rank(np.linalg.matrix_power(Nn, M),
                                   tol=1e-8)
        rM1 = np.linalg.matrix_rank(np.linalg.matrix_power(Nn, M + 1),
                                    tol=1e-8)
        geo = (M + 1) - np.linalg.matrix_rank(Nn, tol=1e-8)
        line_ok = (rM == 1 and rM1 == 0 and geo == 1)
        ok = ok and line_ok
        print("  M=%d : rank(N^M)=%d rank(N^(M+1))=%d geo.mult=%d  %s"
              % (M, rM, rM1, geo, "OK" if line_ok else "FAIL"))
    print("  => every M-quantum sector is a SINGLE Jordan block of "
          "size M+1: %s" % ("CONFIRMED" if ok else "PROBLEM"))

    # ---------------- [2] growth exponents ------------------------------
    print("\n[2] secular growth per sector, ||exp(-i dGamma(A) t)|| ~ "
          "t^M:")
    ts = np.geomspace(30, 3000, 10)
    for M in (1, 2, 4, 6, 8):
        H = dGamma_sector(A_jordan, M)
        ns = [np.linalg.norm(expm(-1j * H * t), 2) for t in ts]
        slope = np.polyfit(np.log(ts), np.log(ns), 1)[0]
        print("  M=%d : fitted exponent %.3f (expect %d)" % (M, slope, M))
    print("  => the growth DEGREE is unbounded up the tower; no")
    print("     truncation escapes, and each level makes it worse --")
    print("     the constructive form of Smilga's infinite-order EP.")

    # ---------------- [3] unit-column violation -------------------------
    print("\n[3] bounded-dictionary unit-column violation (truncated "
          "tower, sectors 0..6):")
    dims = [dGamma_sector(A_jordan, M).shape[0] for M in range(0, 7)]
    Htow = np.zeros((sum(dims), sum(dims)), dtype=complex)
    off = 0
    for M in range(0, 7):
        d = M + 1
        Htow[off:off + d, off:off + d] = dGamma_sector(A_jordan, M)
        off += d
    n = Htow.shape[0]
    S0 = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    U, _, Vh = np.linalg.svd(S0)
    S = U @ np.diag(rng.uniform(0.5, 2.0, n)) @ Vh   # bounded, invertible
    Sinv = np.linalg.inv(S)
    for t in (5.0, 20.0, 80.0):
        V = S @ expm(-1j * Htow * t) @ Sinv
        colnorms = np.linalg.norm(V, axis=0)
        print("  t=%5.1f : max_j ||V e_j|| = %.3e  (column-stochastic "
              "would force 1)" % (t, colnorms.max()))
    print("  => no bounded metric/similarity yields a stochastic "
          "|V|^2 on the tower.")

    # ---------------- [4] healthy control -------------------------------
    print("\n[4] control (diagonalizable one-particle matrix, same "
          "degenerate frequency):")
    worst = 0.0
    for M in (1, 4, 8):
        H = dGamma_sector(A_healthy, M)
        for t in (5.0, 80.0):
            worst = max(worst, abs(np.linalg.norm(expm(-1j * H * t), 2)
                                   - 1.0))
    print("  max | ||exp(-i dGamma t)|| - 1 | = %.2e -- bounded "
          "(unitary), all sectors." % worst)
    print("  degeneracy alone is harmless; the JORDAN pair is what "
          "kills the tower.")

    print("\ndone.")


if __name__ == '__main__':
    main()
