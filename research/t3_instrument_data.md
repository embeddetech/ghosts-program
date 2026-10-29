# T3: Instrument + background data for phantom/ghost vacuum-decay MeV forecast

Purpose: inputs for a redshift-integrated diffuse photon spectrum from ghost dark-energy
vacuum decay (Cline-Jeon-Moore mechanism, PRD 70 043543 = hep-ph/0311312), and the COSI
instrument response needed to forecast detectability of the cutoff edge at E ~ Lambda.

All numbers carry a source tag. Confidence flags: [S] = solid (quoted verbatim from source),
[D] = derived here (arithmetic from [S] numbers), [C] = caution (exponent/detail reconstructed,
verify against primary before publication).

---------------------------------------------------------------------------
## 1. COSI (Compton Spectrometer and Imager, NASA SMEX)

Primary refs: Tomsick et al. 2023, arXiv:2308.12362 (mission definition paper);
Tomsick et al. 2021, arXiv:2109.10403 (ICRC); COSI pre-flight background paper
arXiv:2510.25304; balloon calibrations arXiv:2203.00695; HEASARC mission page;
cosi.ssl.berkeley.edu/instrument.

Basics [S, 2308.12362; HEASARC]:
- NASA Small Explorer, planned launch 2027; 2-year prime mission.
- Detector: 16 high-purity double-sided-strip Ge detectors (GeDs), each 8 x 8 x 1.5 cm^3,
  ~1.5 mm^3 position resolution, surrounded by active CsI shields.
- Energy range: 0.2-5 MeV (GeDs). Auxiliary: BTO 30 keV-2 MeV; shields (ACS) 0.1-40 MeV.
- Orbit: equatorial low-Earth orbit. arXiv:2510.25304 uses 530 km altitude,
  inclination 0.25 +/- 0.15 deg; Caputo et al. arXiv:2210.09310 quote 550 km. [S]
- Field of view: >25% of sky instantaneous; N/S rocking survey covers the FULL sky
  every day. [S, 2308.12362]

Energy resolution (FWHM) [S, 2308.12362 Table 1; HEASARC]:
- 6.0 keV at 0.511 MeV  (1.17%)  [% is D]
- 9.0 keV at 1.157 MeV  (0.78%)  [% is D]
- GeD intrinsic performance from balloon calibration: ~0.3% FWHM at 0.662 MeV
  [S, arXiv:2203.00695]; ~3 keV FWHM currently achieved per detector
  [S, cosi.ssl.berkeley.edu]. No published FWHM at exactly 2 MeV; interpolating the
  Table-1 values as FWHM ~ sqrt(a + b*E) gives roughly 11-12 keV (~0.6%) at 2 MeV. [D]

Angular resolution (Compton ARM, FWHM) [S, 2308.12362 Table 1]:
- 4.1 deg at 0.511 MeV; 2.1 deg at 1.809 MeV. (Caputo et al. 2210.09310 quote
  3.8 deg at 0.511 MeV.) Fine for a diffuse/isotropic signal - irrelevant systematic.

Effective area (WEAK POINT - no official table is published in the mission paper text):
- Tomsick et al. 2023 show the effective-area and sensitivity curves only as figures;
  no numeric table in text. [S - confirmed by full-text extraction of ar5iv 2308.12362]
- Balloon COSI (12 GeDs): 9.6 cm^2 photopeak effective area at 0.662 MeV.
  [S, arXiv:1912.00110 / calibration papers]
- Satellite COSI (16 GeDs): "effective area is about 8 cm^2 in the range 0.5-1.5 MeV"
  for reconstructed Compton events [S, Carenza & De la Torre Luque, arXiv:2210.17206,
  EPJC 83 (2023) 110, citing the COSI response]. Falls off toward 0.2 and 5 MeV.
- cosi.ssl.berkeley.edu: effective area per unit detector volume x100 over COMPTEL. [S]
- RECOMMENDATION: for the forecast, either (a) treat A_eff = 8 cm^2 flat over
  0.5-1.5 MeV with a factor ~2 taper at the band edges [C], or (b) pull the actual
  response matrices from the public COSI Data Challenge releases (cosipy/MEGAlib,
  github.com/cositools) - the DC2/DC3 response files contain A_eff(E) on a fine grid.

Line sensitivity (3 sigma, point source, 2-yr survey) [S, 2308.12362 Table 1]:
- 0.511 MeV: 1.2e-5 ph/cm^2/s   (a secondary summary of the same paper quotes
  7.9e-6 ph/cm^2/s - verify against published PDF Table 1 before using) [C]
- 1.157 MeV (44Ti): 3.0e-6 ph/cm^2/s
- 1.173 / 1.333 MeV (60Fe): 3.0e-6 ph/cm^2/s
- 1.809 MeV (26Al): 3.0e-6 ph/cm^2/s

Continuum / diffuse sensitivity:
- Shown only as Figure 2b of 2308.12362 ("significant improvement" over COMPTEL);
  no numeric values in text. [S]
- Paper explicitly states COSI's continuum sensitivity will constrain the Fermi
  Bubbles and the Galactic Diffuse Continuum Emission -> diffuse analyses are a
  planned product. [S, 2308.12362]
- For an isotropic signal, the relevant figure of merit is exposure x sr, not the
  point-source sensitivity; see derived exposure below.

Background [S, arXiv:2510.25304 "Pre-flight Background Estimates for COSI"]:
- Below ~0.66 MeV: dominated by EXTRAGALACTIC (cosmic) diffuse photons - i.e., the
  signal band 0.2-0.5 MeV is CGB-photon dominated, which is ideal for a CGB-edge
  search (the "background" is the target).
- Above ~0.66 MeV: dominated by delayed activation (cosmic-ray p/alpha) and Earth
  albedo photons. Strong activation lines at 511, 843.8 (27Mg), 1368.1 (24Na) keV.
- Total daily-integrated Compton-event rates ~1-3 Hz after activation buildup
  (read off figures; no single tabulated total). [C]

Survey exposure toward any fixed sky direction (DERIVED, flag in paper as estimate):
- T_mission = 2 yr = 6.31e7 s; instantaneous FoV >= 25% of sky and full-sky daily
  => average fractional live-pointing toward a given direction f ~ 0.25-0.5;
  take duty cycle ~0.85 (SAA/occultation).
- Effective exposure per direction: A_eff * f * duty * T
  ~ 8 cm^2 * 0.3 * 0.85 * 6.31e7 s ~ 1.3e8 cm^2 s   (range 1e8-2.7e8). [D]
- For an isotropic signal integrated over the FoV (Omega ~ pi sr usable), the
  grasp is ~8 cm^2 * pi sr ~ 25 cm^2 sr at 1 MeV. [D]

---------------------------------------------------------------------------
## 2. Measured diffuse MeV gamma-ray background (CGB)

COMPTEL (canonical measurement, 0.8-30 MeV):
- Weidenspointner et al. 2000 (AIP Conf. Proc. 510, 467) + Kappadath PhD (UNH 1998):
  I(E) = (1.05 +/- 0.2)e-4 * (E / 5 MeV)^(-2.4 +/- 0.2)  ph/cm^2/s/sr/MeV,
  valid 0.8-30 MeV. [S]
- Equivalent form used by Cline et al. arXiv:2308.12989:
  dJ/dE = 5.3e-3 * (E / 1 MeV)^(-2.4)  ph/cm^2/s/sr/MeV. [S; = same fit, D-checked:
  1.05e-4 * 5^2.4 = 5.0e-3, consistent within errors]
- No MeV bump; smooth transition, softer below ~3 MeV to harder above. Broken-power-law
  description sometimes used: Gamma ~ 3.3 below 3 MeV, ~2.0 above (as adopted in
  ApJ re-analyses, e.g. iopscience 10.3847/1538-4357/acab69). [S]

SMM/GRS (0.3-8.5 MeV, large 140-deg FoV):
- Watanabe et al. 1997 (AIP Conf. Proc. 410, 1223): spectrum 0.3-3 MeV consistent
  with photon index -2.90 +/- 0.10, normalization 1.32 +/- 0.37 (x1e-4) [C - the
  1e-4 exponent is reconstructed from unit consistency; primary sources quote
  "1.32(+/-0.37) ph/cm^2/s/sr/keV at 0.3 MeV" with the exponent dropped in the
  secondary quote. Cross-check: COMPTEL fit extrapolated to 0.3 MeV gives
  9.5e-5 ph/cm^2/s/sr/keV, i.e. SMM sits ~40% above COMPTEL - consistent with
  published compilation plots]. No MeV bump. [S for index; C for norm]

HEAO-1 (anchors the low-energy side, < 0.4 MeV):
- Gruber et al. 1999 (arXiv:astro-ph/9903492). Standard analytic fit [C - widely
  reproduced, verify coefficients]:
  3-60 keV:  dJ/dE = 7.877 * E^(-0.29) * exp(-E/41.13)          keV/(cm^2 s sr keV)
  E>60 keV:  dJ/dE = 0.0259*(E/60)^(-5.5) + 0.504*(E/60)^(-1.58)
                     + 0.0288*(E/60)^(-1.05)                     keV/(cm^2 s sr keV)

Recent re-measurements / re-analyses:
- SMILE-2+ balloon ETCC (Takada et al. 2022, ApJ 930, 6 = arXiv:2107.00180;
  proceedings arXiv:2002.05362): measured cosmic background MeV gammas 0.1-10 MeV
  with low background; consistent with SMM/COMPTEL level; no new canonical fit
  supersedes Weidenspointner. [S]
- No modern satellite re-measurement of the 1-30 MeV CGB exists; COMPTEL 2000 remains
  the reference. PBH-constraint literature (e.g. arXiv:2112.15463, arXiv:2201.01265,
  arXiv:2606.10013) still fits to Weidenspointner/Watanabe points. [S]

CGB intensity at requested energies (from the two fits above) [D]:
  E [MeV]   COMPTEL fit dN/dE [ph/cm^2/s/sr/MeV]     note
  0.3       9.5e-2 (extrapolated; SMM: ~1.3e-1)      below COMPTEL range
  1.0       5.3e-3                                    in range
  3.0       3.8e-4                                    in range
  5.0       1.05e-4                                   fit pivot
  10.0      2.1e-5                                    in range

Fermi-LAT IGRB (high-energy anchor):
- Ackermann et al. 2015, ApJ 799, 86 (arXiv:1410.3696): isotropic diffuse
  100 MeV - 820 GeV; power law index 2.32 +/- 0.02 with exponential cutoff at
  279 +/- 52 GeV; I(>100 MeV) = (7.2 +/- 0.6)e-6 ph/cm^2/s/sr (model A). [S]

---------------------------------------------------------------------------
## 3. Status of the ghost/phantom gamma-ray bound (does anyone update CJM 2004?)

Original: Cline, Jeon, Moore 2004 (hep-ph/0311312, PRD 70 043543): gravitationally
mediated vacuum decay -> 2 ghosts + 2 photons; rough estimate gave Lambda ~< 3 MeV
from the cosmic gamma-ray background (and Lambda ~< O(GeV) if only graviton-coupled
with a Lorentz-invariant cutoff... the 3 MeV number is the gamma-ray one). [S]

YES - the bound IS updated, by Cline's own group in 2023:

(a) arXiv:2308.12989 (Cline, Puel, Toma, Wang; PRD 108, 095033, 2023),
    "Phantom fluid cosmology":
    - Process: vacuum -> 2 ghosts + 2 photons via graviton exchange; spin-summed
      matrix element sum|M|^2 = (1/(8 m_P^4)) * (t*u/s)^2 (m_P = reduced Planck mass).
    - Full numerical phase-space integration of the instantaneous spectrum dGamma/dE
      (their Appendix A), Gamma ~ Lambda^8 / m_P^4.
    - Redshifted diffuse flux:
      dJ/dE = (1/(4*pi)) Integral dz [ 1 / (H(z)*(1+z)^3) ] * dGamma/dE((1+z)E)
      (rate per proper volume, constant in time for vacuum decay).
    - Compared to COMPTEL: dJ/dE = 5.3e-3 (E/MeV)^-2.4 /MeV/cm^2/s/sr.
    - RESULT (95% CL): Lambda <~ 18.8 MeV (real scalar ghost);
                       Lambda <~ 17.5 MeV (complex scalar ghost).
      i.e. the careful calculation WEAKENS the 2004 rough 3 MeV bound by ~6x.
    - Also: vacuum -> ghosts + e+e- gives only Lambda <~ 350 MeV (weaker).
    - Cosmology: ghost fluid production mildly preferred by data; modest easing of
      H0 and S8 tensions. [S]

(b) arXiv:2401.02958 (Cline, review "Phantom Fluid Cosmology -or- Ghosts for Gordon"):
    - Quotes the same update: photon spectrum dn/dE ~ Lambda^7 * t_0 * m_P^-4 *
      Theta(Lambda - E) (step at E = Lambda - THIS is the "cutoff edge" observable);
      bound Lambda < 18 MeV (abstract rounds to ~20 MeV). [S]

(c) arXiv:2308.01333 (Cline et al., "Boosted dark matter from a phantom fluid"):
    - Does NOT re-derive the gamma bound; adopts Lambda <~ 18 MeV ("several MeV"
      in places) as the validity limit, labels the COMPTEL-excluded region in its
      parameter-space plots. DAMIC excess best fit at Lambda ~= 10 keV for the
      ghost->sterile-neutrino channel. [S]

Other post-2004 literature: no independent update of the photon bound found in
2005-2022 searches; closest related is astro-ph/0606133 (lower limit on the scale
of effective gravity from the same graviton-mediated vacuum decay). The
2004 -> 2023 gap means a COSI-era forecast is timely. [S]

IMPLICATION FOR THE FORECAST: use Lambda_max ~ 18.8 MeV (real scalar) as the current
ceiling; note that the edge for Lambda in the 0.2-5 MeV window falls squarely in the
COSI band, and Lambda up to ~19 MeV still yields most flux below 5 MeV given the
E^-? falling spectrum and redshift integration.

---------------------------------------------------------------------------
## 4. Cosmological ingredients

Flat LCDM, Planck 2018 TT,TE,EE+lowE+lensing (arXiv:1807.06209):
- H0      = 67.36 +/- 0.54 km/s/Mpc  = 2.183e-18 s^-1  [conversion D]
- Omega_m = 0.3153 +/- 0.0073
- Omega_L = 0.6847 +/- 0.0073
- t_0     = 13.797 +/- 0.023 Gyr = 4.355e17 s  [conversion D]
- c/H0    = 4451 Mpc  [D]

H(z) = H0 * sqrt(Omega_m*(1+z)^3 + Omega_L)   (flat; radiation negligible z < 50).

Comoving volume element (flat): dV_C = (c/H(z)) * D_C(z)^2 dz dOmega,
D_C(z) = c * Integral_0^z dz'/H(z').

Diffuse intensity from a spatially uniform emitter with photon emissivity
eps(E, z) [ph / (proper cm^3) / s / MeV]:
  dJ/dE (E, z=0) = (c/(4*pi)) * Integral_0^inf dz  eps((1+z)E, z) / ( H(z)*(1+z)^3 )
  [ph/cm^2/s/sr/MeV]
CHECK: with c=1 and eps = dGamma/dE constant in time (vacuum decay), this is exactly
Eq. used by Cline et al. 2308.12989 - formula verified. The (1+z)^3 = proper-volume
dilution x energy-bin stretch (1+z)^-2 net... i.e. (1+z)^-3 total, and E_emit=(1+z)E.

---------------------------------------------------------------------------
## 5. The MeV gap and the mission landscape

- COMPTEL (CGRO, 1991-2000, 0.75-30 MeV) is still the deepest survey of the band;
  no successor has flown. [S, arXiv:2203.07360 Snowmass "Future of Gamma-Ray
  Experiments in the MeV-EeV Range"]
- Fermi-LAT: nominal range 20 MeV - >300 GeV (Atwood et al. 2009, arXiv:0902.1089);
  effective area collapses below ~100 MeV, standard catalogs and the IGRB
  measurement start at 50-100 MeV. So roughly 5-100 MeV is instrumentally weak,
  and 0.2-30 MeV sensitivity is set by 1990s instruments.
- Quantitative gap statement: sensitivity in the ~0.3-100 MeV band is 2-3 orders
  of magnitude worse than in adjacent X-ray and GeV bands; proposed Si-tracker
  missions (e-ASTROGAM/AMEGO class) would improve on COMPTEL by 1-2 orders of
  magnitude. [S, De Angelis et al. arXiv:1608.03739; arXiv:2203.07360]
- Mission status (mid-2026): COSI is the ONLY funded/confirmed MeV mission
  (SMEX, phase C as of 2024, launch 2027). e-ASTROGAM: proposed ESA M5, not
  selected. AMEGO-X: proposed to 2021 MIDEX (launch would have been <= Dec 2028),
  not selected; concept maintained (arXiv:2108.02860). newASTROGAM: presented
  ICRC 2025 (PoS(ICRC2025)572) as a future MeV-GeV proposal. Others one-line:
  MASS concept (arXiv:2312.11900), GECCO concept. => COSI carries the band
  through ~2030.

---------------------------------------------------------------------------
## 6. Machine-readable parameter block (python)

```python
# --- COSI (Tomsick et al 2023, arXiv:2308.12362 unless noted) ---
cosi_energy_range_MeV   = (0.2, 5.0)
cosi_launch_year        = 2027              # NASA SMEX
cosi_mission_yr         = 2.0               # prime mission
cosi_orbit              = {"alt_km": 530., "incl_deg": 0.25}   # arXiv:2510.25304
cosi_fov_sky_fraction   = 0.25              # instantaneous, >25%; full sky daily
cosi_eff_area           = {                 # cm^2, Compton events [CAUTION: no
    0.2: 3.0,                               #  official table; 0.5-1.5 MeV value
    0.5: 8.0,                               #  from arXiv:2210.17206; band-edge
    1.0: 8.0,                               #  values are tapered estimates [C];
    1.5: 8.0,                               #  balloon: 9.6 cm^2 @0.662 (12 GeDs).
    2.0: 6.0,                               #  Use COSI Data Challenge response
    5.0: 2.0}                               #  files (cositools) for real A_eff(E).
cosi_eres_fwhm_keV      = {0.511: 6.0, 1.157: 9.0}       # Table 1
cosi_eres_fwhm_frac     = {0.511: 0.0117, 1.157: 0.0078, 2.0: 0.006}  # 2 MeV interp [D]
cosi_angres_fwhm_deg    = {0.511: 4.1, 1.809: 2.1}
cosi_line_sens_3sig_2yr = {0.511: 1.2e-5, 1.157: 3.0e-6, 1.173: 3.0e-6,
                           1.333: 3.0e-6, 1.809: 3.0e-6}  # ph/cm2/s (point src)
cosi_bkg_note           = "CGB-photon dominated <0.66 MeV; activation+albedo above"  # 2510.25304
cosi_exposure_per_dir   = 1.3e8             # cm^2 s over 2 yr toward fixed direction [D, x2 uncertainty]
cosi_grasp_cm2sr        = 25.0              # ~8 cm^2 x pi sr, 0.5-1.5 MeV [D]

# --- Cosmic gamma-ray background ---
cgb_comptel_fit = {"norm": 1.05e-4, "norm_err": 0.2e-4,   # ph/cm2/s/sr/MeV at 5 MeV
                   "E0_MeV": 5.0, "index": -2.4, "index_err": 0.2,
                   "range_MeV": (0.8, 30.0),
                   "ref": "Weidenspointner 2000, AIP Conf Proc 510, 467"}
# equivalent: 5.3e-3 * (E/MeV)^-2.4  (form used in arXiv:2308.12989)
cgb_intensity   = {0.3: 9.5e-2, 1.0: 5.3e-3, 3.0: 3.8e-4, 5.0: 1.05e-4, 10.0: 2.1e-5}
                  # ph/cm2/s/sr/MeV from COMPTEL fit; 0.3 MeV is extrapolation
cgb_smm_fit     = {"index": -2.90, "index_err": 0.10,
                   "norm_at_0.3MeV_per_keV": 1.32e-4,     # [C] exponent reconstructed
                   "range_MeV": (0.3, 8.0),
                   "ref": "Watanabe et al 1997, AIP Conf Proc 410, 1223"}
igrb_fermi      = {"index": 2.32, "cutoff_GeV": 279.0, "I_gt100MeV": 7.2e-6,
                   "ref": "arXiv:1410.3696"}              # ph/cm2/s/sr

# --- Ghost/phantom bound status ---
ghost_bound_2004    = 3.0     # MeV, rough estimate, hep-ph/0311312 (CJM, PRD 70 043543)
ghost_bound_2023    = {"real_scalar": 18.8, "complex_scalar": 17.5}  # MeV, 95% CL,
                              # arXiv:2308.12989 vs COMPTEL 5.3e-3(E/MeV)^-2.4
ghost_bound_ee      = 350.0   # MeV, from ghosts+e+e- channel (weaker), 2308.12989
ghost_rate_scaling  = "Gamma ~ Lambda^8 / m_P^4; dn/dE ~ Lambda^7 t0 m_P^-4 Theta(Lambda-E)"
                              # arXiv:2401.02958

# --- Cosmology (Planck 2018, arXiv:1807.06209, TT,TE,EE+lowE+lensing) ---
cosmo = {"H0": 67.36, "H0_err": 0.54,       # km/s/Mpc
         "H0_inv_s": 2.183e-18,             # s^-1
         "Omega_m": 0.3153, "Omega_L": 0.6847,
         "t0_Gyr": 13.797, "t0_s": 4.355e17,
         "c_over_H0_Mpc": 4451.0}
# H(z) = H0*sqrt(Om*(1+z)^3 + OL);  dV_C = (c/H) D_C^2 dz dOmega
# dJ/dE = (c/4pi) Int dz eps((1+z)E, z) / (H(z)*(1+z)^3)   [matches 2308.12989]

# --- Fermi-LAT / MeV gap ---
fermi_lat = {"range_MeV": (20.0, 3.0e5), "useful_above_MeV": 50.0,
             "ref": "arXiv:0902.1089"}
mev_gap   = {"band_MeV": (0.3, 100.0), "sens_deficit_orders": (2, 3),
             "refs": ["arXiv:1608.03739", "arXiv:2203.07360"]}
```

---------------------------------------------------------------------------
## 7. Source list

- arXiv:2308.12362  Tomsick et al 2023, COSI mission definition (Table 1 numbers)
- arXiv:2109.10403  Tomsick et al 2021, COSI ICRC
- arXiv:2510.25304  COSI pre-flight background estimates (orbit, background mix)
- arXiv:2203.00695  COSI balloon calibrations (0.3% FWHM at 662 keV)
- arXiv:2210.17206  Carenza & De la Torre Luque (COSI A_eff ~ 8 cm^2, 0.5-1.5 MeV)
- arXiv:2210.09310  Caputo et al, DM prospects with COSI (survey geometry, sensitivities)
- Weidenspointner et al 2000, AIP Conf Proc 510, 467 (COMPTEL CGB fit)
- Watanabe et al 1997, AIP Conf Proc 410, 1223 (SMM CGB)
- arXiv:astro-ph/9903492  Gruber et al 1999 (HEAO-1 hard X-ray background)
- arXiv:2107.00180 / 2002.05362  SMILE-2+ (Takada et al 2022, ApJ 930, 6)
- arXiv:1410.3696   Fermi-LAT IGRB (Ackermann et al 2015)
- hep-ph/0311312    Cline, Jeon, Moore 2004, PRD 70 043543 (original 3 MeV bound)
- arXiv:2308.12989  Cline et al 2023, PRD 108 095033 (UPDATED bound 18.8/17.5 MeV)
- arXiv:2401.02958  Cline 2024 review (spectrum shape, Lambda < 18 MeV)
- arXiv:2308.01333  Cline et al, boosted DM from phantom fluid (adopts ~18 MeV)
- arXiv:1807.06209  Planck 2018 parameters
- arXiv:0902.1089   Fermi-LAT instrument (Atwood 2009)
- arXiv:1608.03739  e-ASTROGAM (MeV gap statement)
- arXiv:2203.07360  Snowmass, future gamma-ray experiments MeV-EeV
- arXiv:2108.02860  AMEGO-X; PoS(ICRC2025)572 newASTROGAM; arXiv:2312.11900 MASS
