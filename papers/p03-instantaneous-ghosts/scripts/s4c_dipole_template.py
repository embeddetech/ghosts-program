"""
S4c -- the foliation-detection template: dipole amplitude, spectral
edge modulation, and the photon count that decides the decision
matrix's top-left cell.

Physics: on the multiplicity horn, ghost vacuum decay fills the sky
with photons distributed ISOTROPICALLY IN THE INDIVIDUATING FRAME
(the comoving/CMB frame), with a spectral edge at the cutoff Lambda
measured in that frame [CJM: flat dn/dE up to Lambda ~ MeV]. A
detector moving at beta = v/c = 1.23e-3 (370 km/s, the CMB dipole
velocity) sees:

  (1) Compton-Getting dipole: differential flux modulation
      (alpha+2)*beta*cos(theta) for J ~ E^-alpha; for the
      edge-integrated counts of a flat (alpha=0) spectrum the
      amplitude is 3*beta ~ 3.7e-3.
  (2) Edge modulation: the cutoff shifts as
      Lambda(theta) = Lambda*(1 + beta*cos(theta)): amplitude beta
      ~ 0.12% peak. This is the discriminant against mundane
      comoving backgrounds (which share the CG dipole but have no
      universal edge).

Detectability (dipole, apex known from the CMB): the one-parameter
estimator A_hat = 3<cos theta> has per-photon variance 3, so
significance = A*sqrt(N/3) and N_5sigma = 75/A^2.

This script: (i) tabulates amplitudes per spectral index;
(ii) runs a mock-sky Monte Carlo -- source-frame sampling, exact
aberration+Doppler, estimator recovery -- verifying the analytics
and measuring the empirical N_5sigma; (iii) fits the edge shift
under realistic (3%) energy resolution. Honesty: numbers are in
SIGNAL photons; if the ghost signal is a fraction f_s of the
collected diffuse counts, N scales as 1/f_s^2 for the dipole. The
CG dipole alone is degenerate with any comoving background; the
edge modulation is the distinguishing observable.

Run:  python scripts/s4c_dipole_template.py     (~1 minute)
"""

import numpy as np

BETA = 1.23e-3
LAM = 3.0                      # edge (units arbitrary; "MeV")
rng = np.random.default_rng(53)

print("=" * 72)
print("S4c: the foliation-detection template (beta = 1.23e-3)")
print("=" * 72)

# ------------------------------------------------------- analytics
print("\nAnalytic amplitudes: standard differential Compton-Getting")
print("dipole (a+2)*beta for J ~ E^-alpha:")
for alpha in (0.0, 1.0, 2.0):
    print(f"  alpha={alpha:.0f}: {(alpha+2)*BETA:.2e}")
print("count-RATE observables (verified below; each photon weighted")
print("by the arrival-rate factor (1+b*mu) a moving detector sees):")
print(f"all-photon rate dipole 3b = {3*BETA:.2e}; thresholded adds")
print("b*E_thr/(Lambda-E_thr). [An unweighted mock measures only the")
print("aberration part 2b and is blind to the rate factor -- the")
print("circularity a referee caught in an earlier version.]")
print(f"edge modulation amplitude: beta = {BETA:.2e} "
      f"({2*BETA*100:.2f}% peak-to-peak)")

# ------------------------------------------------- mock-sky pipeline
def mock_sky(N, alpha):
    """Source frame: isotropic directions, spectrum E^-alpha with
    edge at LAM (E_min = 0.3). Exact boost to detector frame."""
    Emin = 0.3
    u = rng.random(N)
    if alpha == 1.0:
        E = Emin * (LAM / Emin) ** u
    else:
        p = 1 - alpha
        E = (Emin**p + u * (LAM**p - Emin**p)) ** (1 / p)
    mu = 2 * rng.random(N) - 1.0          # cos(theta) source frame
    g = 1 / np.sqrt(1 - BETA**2)
    # photon moving toward detector: observed energy/direction
    Eobs = g * E * (1 + BETA * mu)
    muobs = (mu + BETA) / (1 + BETA * mu)
    return Eobs, muobs


print("\nMock-sky recovery (alpha=0 flat spectrum), arrival-rate")
print("weighted (w = 1 + b*mu per photon):")
print("  (a) all-photon count RATE: amplitude 3b;")
print("  (b) rate with E_obs > E_thr: 3b + b*E_thr/(Lambda - E_thr).")
E_THR = 1.0
A_a = 3 * BETA
A_b = 3 * BETA + BETA * E_THR / (LAM - E_THR)
print(f"{'N':>10} {'A_hat(a)':>9} {'pred':>8} {'z':>6} | "
      f"{'A_hat(b)':>9} {'pred':>8} {'z':>6}")
for N in (10**6, 4 * 10**6, 10**7, 4 * 10**7):
    E, mu = mock_sky(N, 0.0)
    w = 1 + BETA * mu               # arrival-rate weight per photon
    Aa = 3 * np.sum(w * mu) / np.sum(w)
    za = Aa / np.sqrt(3.0 / N)
    m = E > E_THR
    Ab = 3 * np.sum(w[m] * mu[m]) / np.sum(w[m])
    zb = Ab / np.sqrt(3.0 / m.sum())
    print(f"{N:>10.0e} {Aa:>9.5f} {A_a:>8.5f} {za:>6.1f} | "
          f"{Ab:>9.5f} {A_b:>8.5f} {zb:>6.1f}")
print(f"N_5sigma: observable (a): {75/A_a**2:.2e};  "
      f"observable (b): {75/A_b**2:.2e} signal photons")

# ------------------------------------------------- edge-shift fit
print("\nEdge-shift fit (3% Gaussian energy resolution, N = 4e6):")
E, mu = mock_sky(4 * 10**6, 0.0)
E = E * (1 + 0.03 * rng.standard_normal(len(E)))
bins = np.linspace(-1, 1, 9)
cents, edges = [], []
for i in range(8):
    m = (mu >= bins[i]) & (mu < bins[i + 1])
    if m.sum() > 1000:
        cents.append(0.5 * (bins[i] + bins[i + 1]))
        edges.append(np.percentile(E[m], 99.0))
cents = np.array(cents)
edges = np.array(edges)
slope, icpt = np.polyfit(cents, edges, 1)
print(f"fitted edge vs cos(theta): Lambda_eff*(1 + {slope/icpt:.2e}"
      f"*cos)  [predict {BETA:.2e}]")
resid = np.std(edges - (icpt + slope * cents)) / icpt
print(f"per-bin edge scatter: {resid:.2e} of the edge "
      f"(shift recovered at ~{abs(slope/icpt)/max(resid/np.sqrt(len(cents)),1e-9):.0f} sigma)")

print()
print("PAPER NUMBERS (flat spectrum, apex fixed by the CMB dipole):")
print("thresholded count-rate dipole 4.3e-3 -> N_5sigma ~ 4.0e6")
print("signal photons; all-photon rate dipole 3.7e-3 -> 5.5e6; edge")
print("modulation 0.12%, recoverable through 3% instrument")
print("resolution by percentile regression at N ~ few x 10^6. The")
print("edge, not the dipole, discriminates against comoving")
print("astrophysical backgrounds. Dilution: N scales as 1/f_s^2 for")
print("signal fraction f_s of collected diffuse counts.")
print("done.")
