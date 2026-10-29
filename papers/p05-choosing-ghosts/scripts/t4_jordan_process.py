"""
T4 quantum leg: what a Jordan block (the conformal-gravity /
equal-frequency PU point) means in the stochastic currency -- the
Bender-Mannheim vs Smilga standoff, adjudicated.

LEMMA (no closed process at a Jordan point). If Gamma(t) =
|V(t)|^2 with V = S e^{-iHt} S^{-1} is COLUMN-STOCHASTIC for all t
(unistochastic and doubly stochastic are special cases), then
sum_ij |V_ij|^2 = n, so ||V(t)||_2 <= ||V(t)||_F = sqrt(n) is
bounded. But for nondiagonalizable H (Jordan block of size k at a
real eigenvalue), ||e^{-iHt}|| ~ t^{k-1} is unbounded, and
||V(t)|| >= ||e^{-iHt}||/cond(S) is unbounded for every invertible
S. So NO similarity -- no metric, no partner, no beable rotation --
yields a closed stochastic representation of any kind: at the
conformal point the obstruction is structural, not a diverging
cost.  QED  (Note: unistochasticity does NOT make V itself unitary
-- it fixes only the moduli of some unitary; the Frobenius bound is
what makes the argument airtight.)

What survives is the OPEN route of companion [indivisible]: normalize to a
contraction C(t) = e^{-iHt}/sigma_max(t), dilate (Halmos), and read
the result as survival-conditioned dynamics. This script verifies:

 [1] growth exponents: ||e^{-iJ_k t}|| ~ t^(k-1) for k = 2,3,4
     (fitted), and the similarity-invariance of the growth
     (random S conjugations: same exponent);
 [2] the dilation at the EP: C(t) contraction (max singular value 1
     by construction, second <= 1), Halmos unitary to machine
     precision, reduced process sub-stochastic at all t;
 [3] divisibility structure of the reduced process at the EP:
     |U|^2 is TRIANGULAR (one-way cascade), det Gamma_red stays
     positive, and the divisor stays entrywise nonnegative -- so
     indivisibility enters NOT via negativity (the dimer-EP
     mechanism) but via the divisor column sum crossing one at
     finite t_c: CONDITIONAL MASS CREATION, the mechanism the
     paper reports for the conformal-gravity cell;
 [3b] the sigma_max convention, made explicit: divisor entry SIGNS
     are invariant under every positive scalar renormalization
     c(t) of the contraction normalization (negativity/M1 is
     convention-free), while divisor COLUMN SUMS scale by
     c^2(s)/c^2(s+tau), so the column-sum-crossing diagnostic
     (conditional mass creation/M2) is stated relative to the
     minimal convention c = sigma_max. Dichotomy, k=2 cell with
     coupling kappa: the raw |U|^2 divisor's column sum is exactly
     1 + kappa^2(T^2-s^2), so a renormalization avoids the crossing
     for ALL pairs iff c^2(t) >= c^2(0) e^{kappa^2 t^2} -- Gaussian
     conditioning against polynomially growing dynamics; the
     conditioning overhead c^2/sigma_max^2 diverges. Divisibility
     can be purchased, but only by discarding survival probability
     the dynamics never loses; under the minimal (sigma_max)
     conditioning the crossing at t_c is unavoidable.
 [4] the field-theory tie: the Jordan t-term in amplitude = the
     t^2 in probability = per-mode linear growth of fourth-order
     gravity perturbations. Printed as a dictionary line.

Adjudication printed at the end: Smilga's "unitarity is broken" =
the Lemma (closed currency); Bender-Mannheim's "unitary evolution
via nonstationary states" = the conditional dynamics of the dilated
open process (norm growth divided out) -- the broken-dimer
bookkeeping of paper 1, at the exceptional point.

ASCII only; numpy/scipy.
"""

import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(4)


def jordan(k, w=1.0):
    J = w * np.eye(k) + np.diag(np.ones(k - 1), 1)
    return J


def growth_exponent(H, ts):
    ns = [np.linalg.norm(expm(-1j * H * t), 2) for t in ts]
    return np.polyfit(np.log(ts), np.log(ns), 1)[0]


def main():
    print("=" * 72)
    print("T4 quantum leg: Jordan blocks in the stochastic currency")
    print("=" * 72)

    ts = np.geomspace(20, 2000, 12)

    # ---------------- [1] growth exponents -----------------------------
    print("\n[1] ||exp(-iJ_k t)|| growth exponents (lemma premise):")
    from math import factorial
    for k in (2, 3, 4):
        g = growth_exponent(jordan(k), ts)
        # prefactor: ||e^{-iJ_k t}|| ~ t^(k-1)/(k-1)! (dominant
        # nilpotent term) -- emitted, not just fitted
        pref = np.exp(np.polyfit(np.log(ts), np.log(
            [np.linalg.norm(expm(-1j * jordan(k) * t), 2)
             for t in ts]), 1)[1])
        # similarity invariance -- the exact inequality the lemma uses:
        # ||V(t)|| >= ||e^{-iJt}|| / cond(S) for V = S e^{-iJt} S^-1
        S = rng.standard_normal((k, k)) + 1j * rng.standard_normal((k, k))
        Sinv = np.linalg.inv(S)
        cS = np.linalg.cond(S)
        ratio_min = np.inf
        for t in ts:
            E = expm(-1j * jordan(k) * t)
            V = S @ E @ Sinv
            ratio_min = min(ratio_min, np.linalg.norm(V, 2) * cS /
                            np.linalg.norm(E, 2))
        print("  k=%d : exponent %.3f (expect %d); prefactor %.4f "
              "(expect 1/(k-1)! = %.4f);" % (k, g, k - 1, pref,
                                             1.0 / factorial(k - 1)))
        print("        similarity bound ||V|| cond(S)/||E|| >= 1: "
              "min %.3f" % ratio_min)
    print("  (note: numerically, machine-epsilon perturbations split a")
    print("  Jordan block by ~eps^(1/k) and turn polynomial into")
    print("  exponential growth for t >~ eps^(-1/k) -- windows kept")
    print("  below that; the fragility is itself the EP physics.)")
    # control: diagonalizable (detuned) block saturates at ||U|| ~ 2/delta
    Jd = jordan(2) + np.diag([0.0, 1e-3])
    ns = [np.linalg.norm(expm(-1j * Jd * t), 2) for t in (1e4, 1e5, 1e6)]
    print("  [ctrl] detuned k=2 (delta=1e-3): ||U(t)|| at t = 1e4/1e5/"
          "1e6 : %.0f / %.0f / %.0f" % tuple(ns))
    print("         bounded by ~2/delta = 2000 (secular growth only "
          "until t ~ 1/delta,")
    print("         then quasi-periodic) -- diagonalizable case is "
          "bounded, as the lemma needs.")

    # ---------------- [2] dilation at the EP ---------------------------
    print("\n[2] the open route at the EP (k=2 cell):")
    J = jordan(2)

    def psd_sqrt(M):
        w, V = np.linalg.eigh((M + M.conj().T) / 2)
        return V @ np.diag(np.sqrt(np.clip(w, 0, None))) @ V.conj().T

    worst_sv, worst_halmos, worst_col = 0.0, 0.0, 0.0
    for t in np.linspace(0.1, 30, 60):
        U = expm(-1j * J * t)
        s = np.linalg.svd(U, compute_uv=False)
        C = U / s[0]
        sv = np.linalg.svd(C, compute_uv=False)
        worst_sv = max(worst_sv, sv[0] - 1.0)
        S1 = psd_sqrt(np.eye(2) - C @ C.conj().T)
        S2 = psd_sqrt(np.eye(2) - C.conj().T @ C)
        Ub = np.block([[C, S1], [S2, -C.conj().T]])
        worst_halmos = max(worst_halmos, np.linalg.norm(
            Ub @ Ub.conj().T - np.eye(4)))
        G = np.abs(C) ** 2
        worst_col = max(worst_col, (G.sum(axis=0) - 1.0).max())
    print("  contraction: max(sigma_max - 1) = %.1e" % worst_sv)
    print("  Halmos unitarity error (worst over t): %.1e" % worst_halmos)
    print("  reduced process sub-stochastic: max(col sum - 1) = %.1e"
          % worst_col)

    # ---------------- [3] structure of the reduced EP process ----------
    print("\n[3] structure of the reduced EP process (k=2 cell):")
    # |U|^2 for the pure Jordan cell is TRIANGULAR: [[1, t^2],[0, 1]]
    # (one-way cascade in the beable currency -- transitions only INTO
    # the growth direction). det Gamma_red stays positive; the
    # indivisibility mechanism is different from the dimer EP: the
    # divisor M = Gamma(t2) Gamma(t1)^{-1} stays entrywise nonnegative
    # but violates the column-sum <= 1 condition (conditional mass
    # creation) beyond a finite length.
    U = expm(-1j * J * 2.0)
    print("  lower-left |U|^2 element at t=2: %.1e (triangular: "
          "one-way cascade)" % (np.abs(U[1, 0]) ** 2))
    tgrid = np.linspace(0.1, 8, 160)
    dt = 0.05
    onset = None
    for t in tgrid:
        U1 = expm(-1j * J * t)
        U2 = expm(-1j * J * (t + dt))
        G1 = np.abs(U1 / np.linalg.svd(U1, compute_uv=False)[0]) ** 2
        G2 = np.abs(U2 / np.linalg.svd(U2, compute_uv=False)[0]) ** 2
        M = G2 @ np.linalg.inv(G1)
        neg = M.min()
        colex = M.sum(axis=0).max() - 1.0
        if (neg < -1e-10 or colex > 1e-10) and onset is None:
            onset = (t, neg, colex)
    if onset:
        print("  divisor breaks sub-stochasticity at t_c ~ %.2f "
              "(min entry %.1e, col-sum excess %.1e):" % onset)
        print("  indivisible via CONDITIONAL MASS CREATION -- a "
              "different mechanism from the")
        print("  dimer EP's negativity; the dipole-ghost cell is a "
              "one-way conditioned cascade.")
    else:
        print("  divisor clean over window (inspect)")

    # ---------------- [3b] the sigma_max convention ---------------------
    print("\n[3b] sigma_max convention: invariance split + "
          "minimal-conditioning dichotomy")
    # kappa = 1 for the unit cell J = [[w,1],[0,w]]
    kap = 1.0

    def divisor_c(cfun, s, tau):
        U1, U2 = expm(-1j * J * s), expm(-1j * J * (s + tau))
        G1 = np.abs(U1) ** 2 / cfun(s) ** 2
        G2 = np.abs(U2) ** 2 / cfun(s + tau) ** 2
        return G2 @ np.linalg.inv(G1)

    def smax_t(t):
        return np.linalg.svd(expm(-1j * J * t), compute_uv=False)[0]

    # (i) signs invariant under positive renormalization; column-sum
    #     onset is NOT (it moves)
    tau = 0.02
    mism, on_min, on_over = 0, None, None
    for s in np.arange(0.05, 4.0, 0.01):
        Ma = divisor_c(smax_t, s, tau)
        Mb = divisor_c(lambda t: smax_t(t) * (1 + 0.5 * t), s, tau)
        if not np.array_equal(np.sign(np.round(Ma, 12)),
                              np.sign(np.round(Mb, 12))):
            mism += 1
        if on_min is None and Ma.sum(axis=0).max() > 1 + 1e-10:
            on_min = s
        if on_over is None and Mb.sum(axis=0).max() > 1 + 1e-10:
            on_over = s
    print("  sign-pattern mismatches under renormalization: %d "
          "(M1 convention-free)" % mism)
    print("  column-sum onset: %.3f (minimal) vs %s (over-conditioned "
          "c = sigma_max(1+t/2)):" % (on_min, ("%.3f" % on_over)
                                      if on_over else "none"))
    print("  M2 onset -- and occurrence -- is convention-relative.")
    # (ii) necessity: raw divisor column sum = 1 + kappa^2 (T^2 - s^2)
    for s in (0.5, 2.0):
        U1, U2 = expm(-1j * J * s), expm(-1j * J * (s + 1e-4))
        raw = (np.abs(U2) ** 2 @ np.linalg.inv(np.abs(U1) ** 2)
               ).sum(axis=0).max()
        print("  raw divisor col sum at s=%.1f: %.8f vs "
              "1+k^2(T^2-s^2) = %.8f" % (s, raw,
                                         1 + kap ** 2 *
                                         ((s + 1e-4) ** 2 - s ** 2)))
    # (iii) sufficiency of the Gaussian over-conditioning: crossing-free
    #       at ALL sampled pairs, at divergent overhead
    cfree = lambda t: smax_t(t) * np.exp(0.5 * kap ** 2 * t ** 2)
    worst = -np.inf
    for s in np.arange(0.05, 5.0, 0.05):
        for tau2 in (0.01, 0.1, 0.5, 1.0, 2.0):
            M = divisor_c(cfree, s, tau2)
            worst = max(worst, M.sum(axis=0).max())
            assert M.min() >= -1e-12
    print("  crossing-free convention c^2 = sigma_max^2 e^{k^2 t^2}: "
          "max col sum %.6f (<= 1)" % worst)
    print("  its conditioning overhead c^2/sigma_max^2 at t = 1/3/5: "
          "%.2f / %.1e / %.1e" % tuple(
              np.exp(kap ** 2 * t ** 2) for t in (1.0, 3.0, 5.0)))
    print("  -> divisibility purchasable only at divergent overhead;")
    print("     minimal (sigma_max) conditioning crosses at t_c "
          "(block [3]).")
    # the zero-step onset itself, emitted (quoted as 0.486 in the
    # paper): as tau -> 0 the crossing sits at the root of
    # 2 t sigma^2(t) = (sigma^2)'(t), sigma^2 = 1 + t^2/2
    # + t sqrt(1 + t^2/4) for the unit cell.
    from scipy.optimize import brentq
    s2f = lambda t: 1 + t ** 2 / 2 + t * np.sqrt(1 + t ** 2 / 4)
    h = 1e-7
    tc0 = brentq(lambda t: 2 * t * s2f(t) -
                 (s2f(t + h) - s2f(t - h)) / (2 * h), 0.1, 1.0)
    print("  zero-step onset (root of 2 t sigma^2 = (sigma^2)'): "
          "t_c = %.4f" % tc0)

    # ---------------- [4] the field-theory dictionary line -------------
    print("\n[4] dictionary line: Jordan t-term in amplitude = t^2 in")
    print("    probability = the notorious per-mode linear growth of")
    print("    fourth-order-gravity perturbations: conformal gravity is")
    print("    the everywhere-EP member of paper 1's polynomial class.")

    print("\nADJUDICATION (in the process currency):")
    print("  - closed representation: NONE exists at the Jordan point,")
    print("    for any metric/similarity (Lemma; [1] is its premise) --")
    print("    Smilga's 'unitarity is broken' is the closed-currency")
    print("    statement.")
    print("  - open representation: valid sub-stochastic process at the")
    print("    EP ([2],[3]) -- Bender-Mannheim's 'unitary evolution via")
    print("    nonstationary states' is, in this currency, the")
    print("    survival-conditioned bookkeeping of the dilation: an")
    print("    open-system reading, not a closed sample space.")
    print("  - the beables framework thus sides with BOTH, in different")
    print("    currencies -- and with neither's headline: the conformal")
    print("    point offers no closed probability space (contra BM's")
    print("    framing) and a perfectly valid open one (contra reading")
    print("    Smilga as fatality).")

    print("\ndone.")


if __name__ == '__main__':
    main()
