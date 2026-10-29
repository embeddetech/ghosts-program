"""
T4 rate leg: the reduced (orbit-quotiented) decay measure of pure
conformal (Weyl) gravity, and what the Lorentz-violating-cutoff horn
costs there.

VERTEX PARALLEL (the assumption, flagged; conventions being verified
against Mannheim's papers separately):
  Einstein exchange:  M ~ T (1/(M_Pl^2 q^2)) T,  T ~ s  =>  |M|^2 ~
                      s^2/M_Pl^4   (CJM's vertex; their published
                      Lambda^8/M_Pl^4 follows)
  Weyl exchange:      M ~ T (1/(alpha_g q^4)) T, T ~ s  =>  |M|^2 ~
                      1/alpha_g^2  (dimensionless coupling, s-flat)
So conformal gravity's reduced measure scales like the CONTACT case,
Lambda^4/alpha_g^2 -- the Planck suppression that made GSTZ call the
4-derivative-gravity runaway "cosmologically slow" is absent, because
alpha_g is dimensionless.

This script:
 (1) validates the reduced-integral machinery against paper 2's
     published slopes (contact d=3: 2, CJM: 4 in the s-cutoff), then
     shows the conformal vertex sits on the contact rung with
     1/alpha_g^2 normalization;
 (2) prices the Lorentz-violating-cutoff horn: with rate/V ~
     c Lambda^4/alpha_g^2 (natural units) and decay products of
     energy ~ Lambda, the injected power density over the age of the
     universe must not exceed the critical density; solves for
     Lambda_max(alpha_g);
 (3) sanity checks: the same logic applied to the CJM phantom vertex
     must reproduce a bound in the MeV range (it anchors the method
     to the published 18.8 MeV scale within order-of-magnitude
     prefactor honesty).

All statements tree-level, multiplicity-horn, flat-background --
i.e. the price OF HORN 1 specifically; horn 3 (Bender-Mannheim
zero-norm quantization) evades by exiting the sample space, which is
the trilemma's point. ASCII only; numpy.
"""

import numpy as np

# NOTE ON MODEL CONGRUENCE: these massive external states are a slope-validation
# fixture only. The paper's conformal channel is MASSLESS; masses shift the
# threshold but not the UV slope, which is the only quantity read off here.
MN, MG = 1.0, 0.7            # stage-3 masses (slopes are UV statements)
S_LO = 4 * max(MN, MG) ** 2 + 1e-9


def reduced(Lam_s, vertex):
    """Reduced integral int^Lam_s ds s beta_n beta_g |M|^2 (d=3)."""
    uu = np.linspace(1e-6, np.sqrt(Lam_s - S_LO), 200001)
    ss = S_LO + uu ** 2
    bn = np.sqrt(1 - 4 * MN ** 2 / ss)
    bg = np.sqrt(1 - 4 * MG ** 2 / ss)
    f = ss * bn * bg
    if vertex == 'cjm':
        f = f * ss ** 2          # |M|^2 ~ s^2 (units of M_Pl^-4 outside)
    elif vertex == 'conformal':
        f = f * 1.0              # |M|^2 ~ 1/alpha_g^2 (outside)
    return np.trapezoid(2 * uu * f, uu)


def main():
    print("=" * 72)
    print("T4 rate leg: conformal gravity's reduced decay measure and "
          "the cutoff-horn price")
    print("=" * 72)

    # ---------------- (1) slope validation -----------------------------
    print("\n[1] reduced-integral slopes (validation vs [instantaneous] stage 3):")
    Ls = np.geomspace(1e3, 1e6, 8)
    for vtx, expect in (('contact', 2.0), ('cjm', 4.0),
                        ('conformal', 2.0)):
        I = np.array([reduced(L, vtx) for L in Ls])
        slope = np.polyfit(np.log(Ls[-4:]), np.log(I[-4:]), 1)[0]
        print("  %-9s : slope %.3f (expect %.0f; energy power %d)"
              % (vtx, slope, expect, int(round(2 * slope))))
    print("  => conformal vertex sits on the CONTACT rung: rate/V ~")
    print("     c_ps Lambda^4 / alpha_g^2 -- no Planck MASS in the")
    print("     suppression; the suppression is whatever alpha_g is.")
    print("  [conventions VERIFIED -- research/t4_vertex_conventions.md:")
    print("   I_W = -alpha_g int C^2 (Mannheim 1101.2186 Eq. 9),")
    print("   propagator P2/(2 alpha_g k^4) (Eq. 21-22), standard")
    print("   (1/2) h T coupling. Note: |M|^2 ~ 1/alpha_g^2 s^0 is the")
    print("   dimensionally consistent scaling; an E^8 form would not")
    print("   have units of rate/volume.]")

    # ---------------- (2) the cutoff-horn price ------------------------
    # natural units (eV): rate/V = c_ps Lambda^4/alpha_g^2 [eV^4],
    # power density = Lambda * rate/V, injected over t0 <= rho_crit.
    print("\n[2] Lorentz-violating-cutoff horn priced (energy-density "
          "bound) -- THE ALPHA_G FORK:")
    rho_cr = (2.5e-3) ** 4       # eV^4  (~9.1e-30 g/cm^3)
    t0 = 6.6e32                  # eV^-1 (13.8 Gyr)
    c_ps = 1.0 / (2 * np.pi) ** 4   # phase-space prefactor, O(1e-3):
    #   quote results to order of magnitude only
    MPl_eV = 1.22e28
    print("  Lambda_max = (alpha_g^2 rho_cr/(t0 c_ps))^(1/5):")
    for ag, tag in ((1.0, 'natural coupling'),
                    (3e109, 'face-value rotation-curve match'),
                    (1e108, 'match band lo'), (1e111, 'match band hi')):
        lam = (ag ** 2 * rho_cr / (t0 * c_ps)) ** 0.2
        note = ("wavelength ~ %.0e m" % (1.9733e-7 / lam)
                if lam < 1.0 else "= %.0e M_Pl (VACUOUS)" %
                (lam / MPl_eV))
        print("  alpha_g = %8.0e (%s): Lambda_max ~ %8.1e eV  (%s)"
              % (ag, tag, lam, note))
    # the face-value matching itself, script-emitted (two routes;
    # constants and derivation: research/t4_vertex_conventions.md):
    Msun = 5.65e70               # cm^-1 (natural units)
    gstar = 5.42e-41             # cm^-1 per M_sun (Mannheim-O'Brien)
    agA = Msun / (8 * np.pi * gstar)
    agB = 3 * Msun / (32 * np.pi * gstar)
    print("  face-value matching, two routes (constants from")
    print("  research/t4_vertex_conventions.md):")
    print("    route A  M_sun/(8 pi gamma*)    = %.1e" % agA)
    print("    route B  3 M_sun/(32 pi gamma*) = %.1e" % agB)
    print("    -> |alpha_g| ~ 3-4e109, order-unity agreement; central")
    print("       value 3e109 used above.")
    print("  THE FORK (research/t4_vertex_conventions.md):")
    print("  - FACE-VALUE branch: matching the flat-space 1/(2 alpha_g")
    print("    k^4) exchange to the Mannheim-O'Brien fits gives")
    print("    |alpha_g| ~ 3e109 (two routes agree) -> the decay bound")
    print("    is VACUOUS -- but this same face-value theory fails")
    print("    solar-system tests on published analyses (Flanagan")
    print("    astro-ph/0605504; Yoon 1305.0163; both DISPUTED by")
    print("    Mannheim, gr-qc/0703037 and 1506.02479): the branch that")
    print("    survives vacuum decay is dead by other observations, or")
    print("    -- if Mannheim's rebuttals stand -- one is on the other")
    print("    branch.")
    print("  - MANNHEIM branch: he rejects the flat-space inversion")
    print("    (conformal sources; varying Higgs S(x)); then alpha_g is")
    print("    unfixed, and for any alpha_g within ~8 decades of unity")
    print("    the cutoff horn forces MACROSCOPIC-wavelength cutoffs")
    print("    (alpha_g = 1: Lambda ~ 1e-8 eV, ~20 m) -- and the only")
    print("    escape he offers from BOTH branches is the PT/zero-norm")
    print("    quantization, under which the decay channel closes")
    print("    identically. That escape is horn 3: exit the sample")
    print("    space. The trilemma closes either way.")

    # ---------------- (3) anchor sanity check --------------------------
    print("\n[3] anchor check: same energy-density logic on the CJM "
          "phantom vertex")
    # rate/V = c_ps Lambda^8/M_Pl^4; power = Lambda * rate/V; <= rho_cr/t0
    MPl = 1.22e28                # eV
    lam9 = rho_cr / (t0 * c_ps) * MPl ** 4
    lam_ph = lam9 ** (1.0 / 9.0)
    print("  Lambda_max(phantom, energy-density bound) ~ %.1e eV = "
          "%.1f MeV" % (lam_ph, lam_ph / 1e6))
    print("  (published gamma-ray bound: 18.8 MeV -- same order;")
    print("   the energy-density method is calibrated within O(1-10).)")

    print("\ndone.")


if __name__ == '__main__':
    main()
