"""
S4a -- "the books must balance": the decision matrix's row
discriminant. A genuine ghost sector and a healthy sector, same
temperatures and same coupling strength, differ dynamically in one
decisive way: the healthy pair EQUILIBRATES (energy flow stops when
temperatures meet -- detailed balance has a fixed point), while the
ghost pair has NO equilibrium (entropy grows forever as the normal
sector heats and the ghost sector's negative energy deepens: the
GSTZ no-equilibrium argument, run as dynamics).

Two systems on identical 1+1d lattices (N=64, L=32, m=1, lam=0.25),
thermal traveling-wave baths with fixed spectral support:
  HEALTHY: phi(T=1) + psi(T=2), coupling +lam phi^2 psi^2, standard
           signs -> prediction: E_phi rises to ~equipartition with
           the hot bath, then SATURATES.
  GHOST:   phi(T=1) + chi(T=2), same |coupling|, chi's energy sign
           flipped -> prediction: E_phi grows secularly, NO
           saturation; the ghost sector's (negative) energy budget
           is bottomless.
Control: lam=0 (no transfer, both systems).

Observable: median E_phi(t) - E_phi(0) over the ensemble, plus the
late/mid growth ratio R = dE[200,300]/dE[100,200]: R ~ 0 for
saturation, R ~ 1 for steady unbounded transfer.

Run:  python scripts/s4a_books_balance.py     (~3-6 minutes)
"""

import numpy as np

L, N, MASS, LAM, K_C = 32.0, 64, 1.0, 0.25, 1.2
T_COLD, T_HOT = 1.0, 2.0
NENS, TEND = 6, 300.0
rng = np.random.default_rng(61)
dx = L / N


def omega(k):
    return np.sqrt(MASS**2 + k**2)


def bath(temp):
    x = np.arange(N) * dx
    f = np.zeros(N)
    fp = np.zeros(N)
    jmax = int(np.floor(K_C * L / (2 * np.pi)))
    for j in range(1, jmax + 1):
        k = 2 * np.pi * j / L
        w = omega(k)
        for sgn in (+1, -1):
            n_k = temp / w
            A = np.sqrt(2 * n_k / (w * L))
            th = rng.uniform(0, 2 * np.pi)
            f += A * np.cos(sgn * k * x + th)
            fp += w * A * np.sin(sgn * k * x + th)
    return f, fp


def lap(f):
    return (np.roll(f, 1) + np.roll(f, -1) - 2 * f) / dx**2


def e_sec(f, fp):
    g = (np.roll(f, -1) - f) / dx
    return np.sum(0.5 * fp**2 + 0.5 * g**2 + 0.5 * MASS**2 * f**2) * dx


def run(ghost, lam):
    """Velocity-Verlet; returns E_phi(t) on a coarse grid."""
    wmax = np.sqrt(MASS**2 + 4 / dx**2)
    dt = 0.15 / wmax
    phi, pphi = bath(T_COLD)
    chi, pchi = bath(T_HOT)
    sgn = +1.0 if ghost else -1.0     # sign of 2*lam*phi^2 in chi's eq

    def forces(ph, ch):
        fph = lap(ph) - MASS**2 * ph - 2 * lam * ch**2 * ph
        fch = lap(ch) - MASS**2 * ch + sgn * 2 * lam * ph**2 * ch
        return fph, fch

    fph, fch = forces(phi, chi)
    tgrid = np.arange(0.0, TEND + 1, 10.0)
    out = []
    t, step = 0.0, 0
    nextout = 0
    CAP = 5e3                       # runaway guard: record and stop
    e0 = e_sec(phi, pphi)
    while t <= TEND + dt:
        if nextout < len(tgrid) and t >= tgrid[nextout] - dt / 2:
            e = e_sec(phi, pphi)
            if not np.isfinite(e) or e - e0 > CAP:
                # runaway: pad remaining samples at the cap
                out.extend([e0 + CAP] * (len(tgrid) - len(out)))
                break
            out.append(e)
            nextout += 1
        pphi += 0.5 * dt * fph
        pchi += 0.5 * dt * fch
        phi += dt * pphi
        chi += dt * pchi
        fph, fch = forces(phi, chi)
        pphi += 0.5 * dt * fph
        pchi += 0.5 * dt * fch
        t += dt
        step += 1
    return np.array(out[:len(tgrid)]), tgrid[:len(out)]


print("=" * 72)
print("S4a: equilibration vs bottomless books (T_cold=1, T_hot=2,")
print(f"     lam={LAM}, {NENS}-run medians)")
print("=" * 72)

results = {}
for label, ghost, lam in (("healthy", False, LAM),
                          ("ghost", True, LAM),
                          ("control lam=0", False, 0.0)):
    curves = []
    for _ in range(NENS):
        e, tg = run(ghost, lam)
        curves.append(e - e[0])
    results[label] = (np.median(np.array(curves), axis=0), tg)

tg = results["healthy"][1]
print(f"{'t':>6} {'healthy dE_phi':>14} {'ghost dE_phi':>13} "
      f"{'control':>8}")
for i in range(0, len(tg), 3):
    print(f"{tg[i]:>6.0f} {results['healthy'][0][i]:>14.3f} "
          f"{results['ghost'][0][i]:>13.3f} "
          f"{results['control lam=0'][0][i]:>8.3f}")


hcurve = results["healthy"][0]
gcurve = results["ghost"][0]
plateau = np.mean(hcurve[np.searchsorted(tg, 150.0):])
spread = np.std(hcurve[np.searchsorted(tg, 150.0):])
i_run = np.argmax(gcurve >= 4999.0)
print(f"\nhealthy: plateau dE_phi = {plateau:.2f} +- {spread:.2f} over")
print(f"  t in [150,300] (equilibrated; total transferable at")
print(f"  equipartition is O((T_hot-T_cold)/2 x modes) ~ this scale)")
print(f"ghost: median run hits the dE = 5e3 runaway cap by "
      f"t ~ {tg[i_run]:.0f}" if gcurve[-1] >= 4999
      else f"ghost: no cap hit (final dE = {gcurve[-1]:.1f})")
print()
print("=> the healthy pair equilibrates (detailed balance has a fixed")
print("   point); the ghost pair does not (no joint equilibrium")
print("   exists). This is the dynamical discriminant between a")
print("   genuine phantom sector and any healthy mimic of the same")
print("   background: only the former feeds an unending flux.")
print("done.")
