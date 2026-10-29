"""
Backing for prop:tower's Remark (the sector similarity is positive-diagonal).

On the M-quantum sector of the equal-frequency PU cell A = wI + N (one-particle
size-2 nilpotent, Nv=u, Nu=0, {u,v} orthonormal), dGamma(N) = a_u^dagger a_v acts
on the occupation (beable) basis |s> = |n_u=s, n_v=M-s> as a weighted shift
    |s> -> sqrt((s+1)(M-s)) |s+1>,
whose weights are STRICTLY POSITIVE for s = 0..M-1. A positively-weighted
nilpotent shift equals D J_M D^{-1}, with J_M the standard size-(M+1) nilpotent
Jordan block (ones on the SUBDIAGONAL, matching s->s+1) and D = diag(d_s),
d_0 = 1, d_{s+1} = sqrt((s+1)(M-s)) d_s -- a fixed, POSITIVE diagonal. Hence the
occupation (beable) basis and the Jordan basis differ by a fixed, t-independent
positive-diagonal similarity at every M, so the entrywise sign structure of any
two-time divisor V(T)V(s)^{-1} (V=|U|^2) is invariant: X^occ_{ij}=(d_i/d_j)^2
X^Jordan_{ij}, (d_i/d_j)^2 > 0. (The cross-M "same entry at every M" step uses,
separately, that exp(-i J_M t) is triangular Toeplitz -- offset-k entry
(-it)^k/k!, independent of M; that is proved in the remark, not here.)

NON-SELF-CONFIRMING: the weights are NOT hard-coded from the closed form; they are
built from first-principles ladder operators a_u^dagger, a_v on the 2-mode Fock
space and compared to the closed form. ASCII only; numpy.
"""

import numpy as np


def dGamma_N_closed(M):
    """Closed-form weighted shift: |s> -> sqrt((s+1)(M-s)) |s+1>, dim M+1."""
    d = M + 1
    W = np.zeros((d, d))
    for s in range(M):
        W[s + 1, s] = np.sqrt((s + 1) * (M - s))
    return W


def dGamma_N_ladder(M):
    """Build a_u^dagger a_v from first principles on the 2-mode Fock space
    (n_u, n_v each 0..M), then restrict to the total = M sector. Independent of
    the closed form: uses only a^dagger|n>=sqrt(n+1)|n+1>, a|n>=sqrt(n)|n-1>."""
    K = M + 1  # per-mode truncation (n = 0..M)
    adag = np.zeros((K, K))
    a = np.zeros((K, K))
    for n in range(K - 1):
        adag[n + 1, n] = np.sqrt(n + 1)
        a[n, n + 1] = np.sqrt(n + 1)
    I = np.eye(K)
    au_dag = np.kron(adag, I)   # raise n_u
    av = np.kron(I, a)          # lower n_v
    op = au_dag @ av            # a_u^dagger a_v on the full 2-mode space
    # restrict to the total-quantum = M sector, ordered by s = n_u (n_v = M - s)
    idx = [n_u * K + (M - n_u) for n_u in range(M + 1)]
    return op[np.ix_(idx, idx)]


def check(M):
    Wc = dGamma_N_closed(M)
    Wl = dGamma_N_ladder(M)
    ladder_err = np.max(np.abs(Wc - Wl))          # independence: ladder == closed
    weights = np.array([Wc[s + 1, s] for s in range(M)])
    d = np.ones(M + 1)
    for s in range(M):
        d[s + 1] = weights[s] * d[s]
    D = np.diag(d)
    J = np.zeros((M + 1, M + 1))
    for s in range(M):
        J[s + 1, s] = 1.0                          # standard subdiagonal-ones block
    sim_err = np.max(np.abs(D @ J @ np.linalg.inv(D) - Wc))
    pos = np.all(weights > 0) and np.all(d > 0)
    # independent nilpotent-structure check: single Jordan block of full size
    rank = np.linalg.matrix_rank(Wc)
    nil = np.max(np.abs(np.linalg.matrix_power(Wc, M + 1)))
    single_block = (rank == M) and (nil < 1e-9)
    return weights, pos, ladder_err, sim_err, single_block


def main():
    print("M : positive weights ; D>0 ; ||closed-ladder|| ; ||W-DJD^-1|| ; "
          "single Jordan block?")
    ok = True
    for M in range(1, 13):
        weights, pos, ladder_err, sim_err, single = check(M)
        ok = ok and pos and ladder_err < 1e-10 and single
        print("M=%2d : pos=%s ladder_err=%.1e sim_err=%.1e single_block=%s  %s"
              % (M, pos, ladder_err, sim_err, single, np.round(weights, 3)))
    print("\nALL M<=12: positive weights (ladder-verified) + fixed positive-diagonal "
          "similarity to the standard Jordan block:", ok)


if __name__ == "__main__":
    main()
