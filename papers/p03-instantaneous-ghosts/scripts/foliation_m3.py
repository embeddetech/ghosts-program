"""
M3 — the foliation experiment: who individuates the frame, the state
or the regulator?

Setup (1+1d lattice, fixed physical volume L): normal field phi and
ghost field chi coupled by lam*phi^2*chi^2, prepared in a BOOSTED
thermal state — classical Juttner occupations n(k) = T/(u.k),
u = gamma*(1, v), built as traveling waves so the phi-pi correlation
carries the propagation direction — with fixed spectral support
|k| <= K_C independent of the lattice. The lattice spacing (UV
regulator, and its non-invariant dispersion) defines a SECOND frame.
Switching on the ghost coupling transfers energy into the normal
sector ("vacuum decay" stimulated by the bath); we measure the frame
of the produced radiation via

    v* = Delta P_phi / Delta E_phi

estimated as the ratio of secular slopes dP/dt / dE/dt.
Exact kinematic targets: production isotropic in the STATE frame
=> v* = v (pair momenta cancel in the state frame, boost supplies
gamma*v*DeltaE' / gamma*DeltaE' = v, mass-independent); production
anchored to the LATTICE frame => v* = 0.

The experiment: sweep the lattice cutoff N (16..128) at fixed state.
If v*(N) stays locked near v as N grows, the frame is selected by
the state (spontaneously, physically) — the "cosmological state
picks the foliation" claim, in silico. If v*(N) drifts toward 0,
the individuation is genuinely a UV/regulator effect (the CJM
picture). Controls: v = 0 (target 0 by symmetry), lam = 0 (no
transfer).

Remark (F3 in the notes): this experiment is POSSIBLE only because a
thermal state has a rest frame. The vacuum cannot be boosted — a
vacuum run has only the lattice frame, which is the foliation-
indeterminacy statement in experimental form.

Two further modes back the quantitative claims in manuscript S5.3:

  --bands       Fourier band-resolved transfer at N = 64, 128, 256
                (nens = NENS each, UNGATED evolution to t = TEND:
                the deep UV-cascade epoch lies beyond the
                back-reaction guard): the fraction of the
                transferred normal-sector energy landing in each
                |k| band (support |k| <= K_C = 1.2; 1.2 < |k| <= 3;
                3 < |k| <= 6; |k| > 6), plus a per-band slope-ratio
                v*_b over the full and the late (t >= TEND/2)
                window.
                Backs "~54% of transferred energy in 3 < |k| <= 6",
                "~83% above support" (at N=64), and band-resolved v* ~ 0.
                The band decomposition is lattice-exact: the
                forward-difference gradient symbol 2 sin(k dx/2)/dx
                and centered momentum symbol sin(k dx)/dx make the
                band sums reproduce e_phi / p_phi identically
                (checked at runtime).

  --settlement [NRUNS]   The multi-run settlement of the EARLY-WINDOW
                estimator: per independent run, v*_early =
                (dP/dt)/(dE/dt) with both slopes fit over
                t in [3, 20] (before the UV cascade erases the state
                frame; the window is a reproduction choice — the
                manuscript quotes only "early window"). Default
                NRUNS = 100 at N = 128 and N = 256; reports
                mean +/- SEM, std, and median, both raw and with
                ill-conditioned runs screened (early dE/dt below
                0.1 x the ensemble median: the slope RATIO of such
                a run carries no frame information and can dominate
                the raw mean — the estimator is heavy-tailed, hence
                the settlement).

Run:  python scripts/foliation_m3.py                  (sweep, minutes)
      python scripts/foliation_m3.py --bands          (~1 min)
      python scripts/foliation_m3.py --settlement     (100 runs, ~5 min)
"""

import sys

import numpy as np
from scipy.integrate import solve_ivp

L, MASS = 32.0, 1.0
K_C, VSTATE, LAM = 1.2, 0.35, 0.3
T_PHI, T_CHI = 1.0, 2.0        # ghost bath hotter: GSTZ drift
                               # ~ T1*T2*(T2-T1) vanishes at equal T
NENS, TEND = 16, 80.0
NT = 161                       # t_eval grid size on [0, TEND]
rng = np.random.default_rng(11)

BANDS = ((0.0, K_C, "|k|<=1.2 (support)"),
         (K_C, 3.0, "1.2<|k|<=3"),
         (3.0, 6.0, "3<|k|<=6"),
         (6.0, np.inf, "|k|>6"))


def omega(k):
    return np.sqrt(MASS**2 + k**2)          # continuum dispersion for ICs


def boosted_bath(N, v, temp):
    """Traveling-wave thermal state, occupations n(k)=T/(u.k),
    support |k|<=K_C. Returns (field, pi_field)."""
    dx = L / N
    x = np.arange(N) * dx
    gam = 1.0 / np.sqrt(1 - v**2)
    f = np.zeros(N)
    fp = np.zeros(N)
    jmax = int(np.floor(K_C * L / (2 * np.pi)))
    for j in range(1, jmax + 1):
        k = 2 * np.pi * j / L
        w = omega(k)
        for sgn in (+1, -1):                # right- and left-movers
            kk = sgn * k
            n_k = temp / (gam * (w - v * kk))
            A = np.sqrt(2 * n_k / (w * L))
            th = rng.uniform(0, 2 * np.pi)
            f += A * np.cos(kk * x + th)
            fp += w * A * np.sin(kk * x + th)
    return f, fp


def lap(f, dx):
    return (np.roll(f, 1) + np.roll(f, -1) - 2 * f) / dx**2


def e_phi(phi, pphi, dx):
    g = (np.roll(phi, -1) - phi) / dx
    return np.sum(0.5 * pphi**2 + 0.5 * g**2
                  + 0.5 * MASS**2 * phi**2) * dx


def p_phi(phi, pphi, dx):
    g = (np.roll(phi, -1) - np.roll(phi, 1)) / (2 * dx)   # centered
    return -np.sum(pphi * g) * dx


def evolve(N, v, lam, tend=TEND, guarded=True):
    """One ensemble member: fresh boosted baths, full nonlinear
    evolution to tend on the NT-point output grid. If guarded, stops
    early when the normal-sector energy doubles (back-reaction
    guard); ungated evolution reaches the deep UV-cascade epoch.
    Returns (ts, Y) with Y = [phi; pphi; chi; pchi] columns."""
    dx = L / N
    tgrid = np.linspace(0.0, tend, NT)
    phi, pphi = boosted_bath(N, v, T_PHI)
    chi, pchi = boosted_bath(N, v, T_CHI)
    e0 = e_phi(phi, pphi, dx)

    def rhs(t, y):
        ph, pp, ch, pc = y.reshape(4, N)
        return np.concatenate([
            pp, lap(ph, dx) - MASS**2 * ph - 2 * lam * ch**2 * ph,
            pc, lap(ch, dx) - MASS**2 * ch + 2 * lam * ph**2 * ch])

    guard = lambda t, y: e_phi(y[:N], y[N:2 * N], dx) - 2.0 * e0
    guard.terminal, guard.direction = True, 1
    s = solve_ivp(rhs, (0, tend),
                  np.concatenate([phi, pphi, chi, pchi]),
                  rtol=1e-8, atol=1e-8,
                  events=(guard if guarded else None),
                  t_eval=tgrid, max_step=0.05)
    return s.t, s.y


def ep_series(ts, Y, N, dx):
    Es = np.array([e_phi(Y[:N, i], Y[N:2 * N, i], dx)
                   for i in range(len(ts))])
    Ps = np.array([p_phi(Y[:N, i], Y[N:2 * N, i], dx)
                   for i in range(len(ts))])
    return Es, Ps


def run_case(N, v, lam):
    """Secular estimator: linear-regression slopes of E_phi(t) and
    P_phi(t) over t in [3, TEND]; v* = dP/dt / dE/dt (oscillations
    average out in the fit). Stops early if the transfer exceeds
    the initial normal-sector energy (back-reaction guard)."""
    dx = L / N
    out = []
    for _ in range(NENS):
        ts, Y = evolve(N, v, lam)
        if len(ts) < 20:                 # need >= t~10 of secular data
            continue
        Es, Ps = ep_series(ts, Y, N, dx)
        m = ts >= 3.0
        dEdt = np.polyfit(ts[m], Es[m], 1)[0]
        dPdt = np.polyfit(ts[m], Ps[m], 1)[0]
        out.append((dPdt / dEdt if dEdt != 0 else np.nan,
                    dEdt, ts[-1]))
    return out


# ------------------------------------------------------------ bands
def band_masks(N, dx):
    kv = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    absk = np.abs(kv)
    masks = []
    for lo, hi, _ in BANDS:
        if lo == 0.0:
            masks.append(absk <= hi)               # include k = 0
        elif np.isfinite(hi):
            masks.append((absk > lo) & (absk <= hi))
        else:
            masks.append(absk > lo)
    return kv, masks


def band_series(ts, Y, N, dx):
    """Fourier band-resolved E_phi(t), P_phi(t). Lattice-exact:
    with the forward-difference gradient symbol |2 sin(k dx/2)/dx|
    and centered momentum symbol sin(k dx)/dx, the sums over all
    bands reproduce e_phi / p_phi to rounding."""
    kv, masks = band_masks(N, dx)
    g2 = (2 * np.sin(kv * dx / 2) / dx) ** 2
    cs = np.sin(kv * dx) / dx
    E = np.zeros((len(masks), len(ts)))
    P = np.zeros_like(E)
    for i in range(len(ts)):
        Ph = np.fft.fft(Y[:N, i])
        Pp = np.fft.fft(Y[N:2 * N, i])
        ek = (dx / N) * (0.5 * np.abs(Pp) ** 2
                         + 0.5 * (MASS**2 + g2) * np.abs(Ph) ** 2)
        pk = -(dx / N) * np.real(np.conj(Pp) * 1j * cs * Ph)
        for b, m in enumerate(masks):
            E[b, i] = ek[m].sum()
            P[b, i] = pk[m].sum()
    return E, P


def run_bands(N, v=VSTATE, lam=LAM, nens=NENS):
    """Ensemble band-resolved transfer at lattice size N, UNGATED
    evolution to t = TEND (the deep UV-cascade epoch lies beyond the
    back-reaction guard, which trips at t ~ 20-35 when E_phi has
    merely doubled -- at the guard the transfer is still dominated
    by 1.2 < |k| <= 3). Emits: the fraction of the transferred
    normal-sector energy Delta E_phi (t = 0 -> TEND) per |k| band,
    and the per-band slope-ratio v*_b = <dP_b/dt> / <dE_b/dt> over
    the full ([3, TEND]) and the late ([TEND/2, TEND]) window."""
    dx = L / N
    nb = len(BANDS)
    dE = np.zeros(nb)
    sE_f = np.zeros(nb); sP_f = np.zeros(nb)   # summed slopes, full
    sE_l = np.zeros(nb); sP_l = np.zeros(nb)   # summed slopes, late
    kept = 0
    for _ in range(nens):
        ts, Y = evolve(N, v, lam, guarded=False)
        E, P = band_series(ts, Y, N, dx)
        if kept == 0:                    # lattice-exactness check
            Es0, Ps0 = ep_series(ts[:1], Y, N, dx)
            assert abs(E[:, 0].sum() - Es0[0]) < 1e-8 * abs(Es0[0])
            assert abs(P[:, 0].sum() - Ps0[0]) < 1e-6 * (abs(Ps0[0]) + 1)
        dE += E[:, -1] - E[:, 0]
        mf = ts >= 3.0
        ml = ts >= 0.5 * ts[-1]
        for b in range(nb):
            sE_f[b] += np.polyfit(ts[mf], E[b, mf], 1)[0]
            sP_f[b] += np.polyfit(ts[mf], P[b, mf], 1)[0]
            sE_l[b] += np.polyfit(ts[ml], E[b, ml], 1)[0]
            sP_l[b] += np.polyfit(ts[ml], P[b, ml], 1)[0]
        kept += 1
    tot = dE.sum()
    print(f"\nband-resolved transfer, N = {N} "
          f"(k_max = {np.pi / dx:.2f}), {kept} ungated runs to "
          f"t = {TEND:.0f}:")
    print(f"  {'band':>20} {'dE (sum)':>10} {'frac':>7} "
          f"{'v*_b full':>10} {'v*_b late':>10}")
    for b, (_, _, name) in enumerate(BANDS):
        print(f"  {name:>20} {dE[b]:>10.2f} {dE[b] / tot:>6.1%} "
              f"{sP_f[b] / sE_f[b]:>10.3f} {sP_l[b] / sE_l[b]:>10.3f}")
    above = dE[1:].sum() / tot
    band36 = dE[2] / tot
    print(f"  total dE_phi = {tot:.2f};  fraction in 3<|k|<=6 = "
          f"{band36:.1%};  fraction above support (|k|>1.2) = {above:.1%}")
    return dE, tot


# ------------------------------------------------------- settlement
def settlement(nruns=100, Ns=(128, 256), early=(3.0, 20.0)):
    """Multi-run settlement of the early-window slope-ratio
    estimator: per independent run, v*_early = (dP/dt)/(dE/dt) with
    both slopes fit over t in [early[0], early[1]]. The estimator is
    a RATIO of fitted slopes and is heavy-tailed: a run whose
    early-window transfer happens to be tiny has an ill-conditioned
    ratio that carries no frame information and can dominate the raw
    mean. Both the raw statistics and a screened set (runs with
    early dE/dt > 0.1 x the ensemble median dE/dt) are therefore
    reported, plus the full-window [3,TEND] estimator for
    reference."""
    for N in Ns:
        dx = L / N
        ve, de, vf = [], [], []
        for _ in range(nruns):
            ts, Y = evolve(N, VSTATE, LAM)
            Es, Ps = ep_series(ts, Y, N, dx)
            m = (ts >= early[0]) & (ts <= early[1])
            if m.sum() >= 5:
                dEdt = np.polyfit(ts[m], Es[m], 1)[0]
                dPdt = np.polyfit(ts[m], Ps[m], 1)[0]
                if dEdt != 0:
                    ve.append(dPdt / dEdt)
                    de.append(dEdt)
            mf = ts >= 3.0
            if len(ts) >= 20:
                dEdt = np.polyfit(ts[mf], Es[mf], 1)[0]
                dPdt = np.polyfit(ts[mf], Ps[mf], 1)[0]
                if dEdt != 0:
                    vf.append(dPdt / dEdt)
        v, d = np.array(ve), np.array(de)
        sem = v.std(ddof=1) / np.sqrt(len(v))
        print(f"N = {N:>3}, {len(v)} runs, early window "
              f"t in [{early[0]:.0f},{early[1]:.0f}]:")
        print(f"    v*_early raw:      mean = {v.mean():+.3f} +/- "
              f"{sem:.3f} (SEM), std = {v.std(ddof=1):.2f}, "
              f"median = {np.median(v):+.3f}")
        keep = d > 0.1 * np.median(d)
        vk = v[keep]
        print(f"    v*_early screened: mean = {vk.mean():+.3f} +/- "
              f"{vk.std(ddof=1) / np.sqrt(len(vk)):.3f} (SEM), "
              f"std = {vk.std(ddof=1):.2f}, "
              f"median = {np.median(vk):+.3f}  "
              f"[{len(vk)}/{len(v)} runs, early dE/dt > 0.1 x median]")
        w = np.array(vf)
        print(f"    v*_full [3,{TEND:.0f}]:    mean = {w.mean():+.3f} +/- "
              f"{w.std(ddof=1) / np.sqrt(len(w)):.3f} (SEM), "
              f"median = {np.median(w):+.3f}")


# ------------------------------------------------------------ modes
def self_test():
    N0 = 64
    dx0 = L / N0
    x0 = np.arange(N0) * dx0
    k0 = 2 * np.pi * 3 / L
    w0 = omega(k0)
    phi_t = np.cos(k0 * x0)
    pi_t = w0 * np.sin(k0 * x0)
    ratio = p_phi(phi_t, pi_t, dx0) / e_phi(phi_t, pi_t, dx0)
    print(f"self-test: right-mover P/E = {ratio:+.4f} vs k/w = "
          f"{k0/w0:+.4f}  ({'OK' if abs(ratio - k0/w0) < 0.02 else 'FAIL'})")


def main_sweep():
    self_test()
    print()
    print("=" * 72)
    print(f"M3: frame of secular energy transfer, v* = (dP/dt)/(dE/dt),")
    print(f"    regression over t in [3,{TEND:.0f}]")
    print(f"    state: boosted thermal, v={VSTATE}, T_phi={T_PHI}, "
          f"T_chi={T_CHI}, |k|<={K_C} (fixed); lam={LAM}")
    print(f"    targets: state-anchored v* = {VSTATE:.2f}; "
          f"lattice-anchored v* = 0")
    print("=" * 72)
    print(f"{'N':>4} {'k_lat':>6} | {'median v*':>9} {'IQR':>17} "
          f"{'med dE/dt':>9} {'runs':>5}")
    for N in (16, 32, 64, 128):
        res = run_case(N, VSTATE, LAM)
        if res:
            vs = np.array([r[0] for r in res])
            rr = np.array([r[1] for r in res])
            print(f"{N:>4} {np.pi/(L/N):>6.2f} | {np.median(vs):>9.3f} "
                  f"[{np.percentile(vs,25):>6.3f},"
                  f"{np.percentile(vs,75):>7.3f}]"
                  f" {np.median(rr):>9.4f} {len(res):>4}/{NENS}")
        else:
            print(f"{N:>4} {np.pi/(L/N):>6.2f} | insufficient data")

    print()
    print("controls:")
    res0 = run_case(64, 0.0, LAM)
    if res0:
        vs0 = np.array([r[0] for r in res0])
        print(f"  v=0, N=64:   median v* = {np.median(vs0):+.3f} "
              f"[{np.percentile(vs0,25):+.3f},"
              f"{np.percentile(vs0,75):+.3f}] "
              f"(target 0)")
    resL = run_case(64, VSTATE, 0.0)
    if resL:
        rr = np.array([r[1] for r in resL])
        print(f"  lam=0, N=64: median dE/dt = {np.median(rr):+.5f} "
              f"(target ~0 - no transfer)")
    print()
    print("verdict key: v*(N) ~ 0.35 and stable as N grows => the STATE")
    print("individuates the frame (foliation is physical/spontaneous);")
    print("v*(N) -> 0 with N => the REGULATOR individuates (CJM picture).")
    print("done.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--bands" in args:
        self_test()
        for N in (64, 128, 256):
            run_bands(N)
    elif "--settlement" in args:
        i = args.index("--settlement")
        nruns = (int(args[i + 1])
                 if len(args) > i + 1 and args[i + 1].isdigit() else 100)
        self_test()
        settlement(nruns)
    else:
        main_sweep()
