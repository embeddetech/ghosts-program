"""
Closeout numerics for two stage-3 loose ends (paper 2).

A. GV LOG-GROWTH REPLICATION (d=1). Garriga-Vilenkin's D=2 result --
   a Lorentz-invariant rate finite at any age T and growing ~ln(mT)
   -- should be our factorization with the causal orbit regulator
   gamma < T*sqrt(s), i.e. eta_max(s,T) = arccosh(T*sqrt(s)).
   Compute Gamma(T) = (2/(2pi)^2)*(1/2) int ds rho_n rho_g
   eta_max(s,T) and verify linearity in ln(T) with slope ~ I_s.

B. d=3 FACTORIZATION MONTE CARLO. Brute-force the constrained
   4-particle phase space in d=3 (Gaussian-smeared energy delta,
   momentum delta exact): verify (i) Gamma(H) linear in the rapidity
   cutoff H at fixed s-cutoff, (ii) reduced growth ~ Lambda_s^2
   (= Lambda^4 in energy) -- the d=3 rung of the dimension ladder,
   previously verified only semi-analytically.

Run:  python scripts/qft_bridge_closeout.py    (~2-4 minutes)
"""

import numpy as np

MN, MG = 1.0, 0.7
rng = np.random.default_rng(71)

# ------------------------------------------------------------------ A
print("=" * 70)
print("A. GV log growth: Gamma(T) with causal orbit cap "
      "eta_max = arccosh(T sqrt(s))")
print("=" * 70)
u = np.linspace(1e-6, 60.0, 200001)
s = 4 * MN**2 + u**2
rr = (1 / np.sqrt(s * (s - 4 * MN**2))) * (1 / np.sqrt(s * (s - 4 * MG**2)))
I_s = np.trapezoid(2 * u * rr, u)
print(f"   (reduced integral I_s = {I_s:.4f})")
print(f"{'T':>8} {'Gamma(T) x (2pi)^2':>18}")
Ts = np.array([10.0, 100.0, 1000.0, 10000.0])
Gs = []
for T in Ts:
    eta = np.arccosh(np.maximum(T * np.sqrt(s), 1.0))
    Gs.append(np.trapezoid(2 * u * rr * eta, u))
    print(f"{T:>8.0f} {Gs[-1]:>18.4f}")
sl = np.polyfit(np.log(Ts), Gs, 1)[0]
print(f"   slope d Gamma / d lnT = {sl:.4f}  vs I_s = {I_s:.4f}"
      f"  ({'LOG GROWTH CONFIRMED' if abs(sl/I_s-1)<0.05 else 'CHECK'})")

# ------------------------------------------------------------------ B
print()
print("=" * 70)
print("B. d=3 factorization Monte Carlo (smeared energy delta)")
print("=" * 70)
SIG = 0.05


def mc_gamma(H, sqrt_s_max, nsamp=6_000_000):
    R = sqrt_s_max * np.cosh(H) * 0.8
    tot, tot2, n = 0.0, 0.0, 0
    for _ in range(6):
        k1 = rng.uniform(-R, R, (nsamp, 3))
        k2 = rng.uniform(-R, R, (nsamp, 3))
        k3 = rng.uniform(-R, R, (nsamp, 3))
        k4 = -(k1 + k2 + k3)
        w1 = np.sqrt(MN**2 + np.sum(k1**2, 1))
        w2 = np.sqrt(MN**2 + np.sum(k2**2, 1))
        w3 = np.sqrt(MG**2 + np.sum(k3**2, 1))
        w4 = np.sqrt(MG**2 + np.sum(k4**2, 1))
        dE = w1 + w2 - w3 - w4
        wgt = np.exp(-dE**2 / (2 * SIG**2)) / (SIG * np.sqrt(2 * np.pi))
        wgt /= (16 * w1 * w2 * w3 * w4)
        E = w1 + w2
        P = k1 + k2
        Pm = np.linalg.norm(P, axis=1)
        ss = E**2 - Pm**2
        eta = np.arctanh(np.clip(Pm / E, 0, 0.9999999))
        ok = (ss > 0) & (ss < sqrt_s_max**2) & (eta < H)
        vals = wgt * ok
        tot += vals.sum()
        tot2 += (vals**2).sum()
        n += nsamp
    mean = tot / n
    err = np.sqrt(max(tot2 / n - mean**2, 0) / n)
    vol = (2 * R) ** 9
    return mean * vol, err * vol


def vorb(H):
    """d=3 boost-orbit volume: integral of sinh^2(eta) d eta."""
    return (np.sinh(H) * np.cosh(H) - H) / 2


print("(i) factorization: Gamma(H) / V_orbit(H) constant, with the")
print("    d=3 orbit measure sinh^2(eta) d eta (NOT flat as in d=1):")
for H in (0.5, 1.0, 1.5):
    g, e = mc_gamma(H, 4.0)
    print(f"   H={H:3.1f}: Gamma = {g:9.3e} +- {e:7.1e}   "
          f"Gamma/V_orb = {g/vorb(H):9.3e}")
print("(ii) reduced growth with the s-cutoff (H = 1.0; threshold at")
print("     sqrt_s = 2, so the sweep starts above it):")
gs, sms = [], (4.0, 8.0, 16.0)
for sm in sms:
    g, e = mc_gamma(1.0, sm)
    gs.append(g)
    print(f"   sqrt_s_max={sm:3.0f}: Gamma = {g:9.3e} +- {e:7.1e}")
sl = np.polyfit(np.log(sms), np.log(gs), 1)[0]
print(f"   log-log slope vs sqrt_s_max = {sl:.2f}  (predict ~4 =")
print("   Lambda^4 in energy; near-threshold suppression steepens the")
print("   low end)")
sl_hi = (np.log(gs[-1]) - np.log(gs[-2])) / (np.log(sms[-1]) - np.log(sms[-2]))
print(f"   upper-interval slope (sqrt_s_max {sms[-2]:.0f} -> {sms[-1]:.0f})"
      f" = {sl_hi:.2f}  (the manuscript's 'over the upper interval' value)")
print("done.")
