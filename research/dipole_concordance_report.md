# Dipole Concordance: Cosmological Backgrounds as Independent Estimators of One Preferred Frame

Exploratory data-mining report for the indivisible-stochastic ghosts / preferred-foliation
program. Framing: if there is a single preferred foliation, every background radiation or
source population rides in it, and every dipole is an independent estimator of the same
boost vector (direction + amplitude). Direction concordance tests "one frame"; amplitude
ratios test whether the boost inferred from each population equals the CMB-inferred
beta = v/c = 1.2336e-3.

Date: 2026-07-11. All numbers verified against arXiv sources cited inline; unverified
items are flagged explicitly. ASCII only.

---

## 1. Reference: the CMB dipole (Planck 2018)

- Amplitude: 3362.08 +/- 0.99 uK  ->  beta = 1.2336e-3, v = 369.82 +/- 0.11 km/s
- Apex (galactic): l = 264.021 +/- 0.011 deg, b = 48.253 +/- 0.005 deg
  (equatorial: RA = 167.94 deg, dec = -6.94 deg)
- Source: Planck 2018 results I (arXiv:1807.06205). Note: the Colloquium
  (arXiv:2505.23526) quotes b = 48.243; the Planck legacy value is 48.253. The 0.01 deg
  difference is irrelevant at the precision of everything below. I use (264.021, 48.253).

The CMB dipole itself does not distinguish kinematic from intrinsic origin; that is
precisely what the other estimators test.

## 2. The estimators

### 2.1 CatWISE2020 quasar number-count dipole
- Secrest et al. 2021 (arXiv:2009.14826, ApJL 908 L51): 1,355,352 mid-IR quasars.
  D_obs = 0.01554 toward (l, b) = (238.2, 28.8), i.e. 27.8 deg from the CMB apex
  (their number; independently reproduced by my spherical-trig computation below).
  Ellis-Baldwin expectation D_kin = [2 + x(1+alpha)] beta ~= 0.0073 with alpha ~= 1.26
  (2009.14826; the Colloquium 2505.23526 quotes alpha = 1.06 from W1-W2 color -- both
  appear in the literature; flag: I did not resolve which enters the final 0.0073).
  Excess p = 5e-7 (4.9 sigma, one-sided).
- Secrest et al. 2022 (arXiv:2206.05624, ApJL 937 L31): quasars 4.4 sigma alone,
  joint with NVSS radio galaxies 5.1 sigma; no frequency dependence of the excess.
- Dam, Lewis & Brewer 2023 (arXiv:2212.07733, MNRAS 525, 231): Bayesian reanalysis,
  amplitude 2.7x kinematic, direction consistent with CMB, excess 5.7 sigma; masking
  the Galactic plane worsens, source evolution only mildly helps.
- Rebuttals / reassessments:
  * Abghari et al. 2024 (arXiv:2405.09762): with higher multipoles free and mask-induced
    mode coupling propagated, D ~= 0.010 with large errors; significance drops to
    ~2 sigma (p = 0.014). They flag an unexplained ecliptic-latitude gradient.
  * 2025 reassessment (arXiv:2511.00822): 4.9 sigma -> 3.63 sigma (no clustering
    dipole), 3.44 sigma (random clustering dipole), 3.27 sigma (aligned clustering
    dipole); mask-induced dipole-octupole coupling inflates both estimate and variance;
    anomaly persists but weakened.
  * Clustering properties of CatWISE (arXiv:2510.23769): clustering dipole nonnegligible
    but cannot alone explain the excess.
  * Simulation-based-inference reanalysis (Oayda et al. 2025; found via search, arXiv ID
    not verified by me): confirms amplitude ~2x kinematic but finds the direction
    misaligned from the CMB apex at ~3 sigma once the scanning-law x photometric-noise
    quadrupole is modeled. FLAG: ID unverified; treat as provisional.
- Status: excess amplitude at 2.1-2.7x kinematic; significance contested, 2.0-5.7 sigma
  depending on treatment of clustering, mask coupling, and systematics. Direction within
  ~28 deg of CMB apex in all analyses.

### 2.2 Radio continuum dipoles: NVSS, RACS, MALS/MeerKAT
- Wagenveld, Klockner & Schwarz 2023 (arXiv:2305.15335, A&A 675 A72), Bayesian
  estimators. From their results table (as returned by my fetch of the A&A full text):
    NVSS:        D = 1.37 +/- 0.40 (x1e-2), apex (RA, dec) = (174 +/- 21, -18 +/- 17)
    RACS-low:    D = 1.53 +/- 0.37 (x1e-2), apex (170 +/- 18, +8 +/- 15)
    NVSS+RACS:   D = 1.35 +/- 0.28 (x1e-2), apex (169 +/- 9, -6 +/- 8), 4.8 sigma excess
    Kinematic expectation D_kin ~= 4.5e-3.
  SCALE FLAG: the fetched table text said "x1e-3", but that is internally inconsistent
  with the paper's own statements ("amplitude three times as large" as D_kin = 4.5e-3)
  and with the companion Bayesian joint paper (arXiv:2406.01871) quoting NVSS
  10 +/- 5 e-3 and RACS-low 11 +4/-5 e-3. I report x1e-2 as the corrected scale;
  the joint direction and 4.8 sigma are verified.
- Joint Bayesian NVSS+RACS (arXiv:2406.01871, MNRAS 531, 4545): kinematic-direction
  model gives NVSS 10 +/- 5 e-3, RACS-low 11 +4/-5 e-3 vs expected 4.0-4.3e-3
  (ratio 2.8-3.2). Removing ~0.9% of sources as local (clustering) reduces amplitudes
  by 10-15%: nearby LSS explains part, not all, of the excess.
- MALS DR2 / MeerKAT (Wagenveld et al. 2024, arXiv:2408.16619, A&A): 971,980 sources,
  4344 deg2, 10 uJy/beam. At the 400 uJy cut: D = 0.67 +0.31/-0.29 e-2 vs
  D_kin = 0.40e-2 (alpha ~= 0.75, x = 0.69): consistent with purely kinematic CMB
  expectation in amplitude and direction (direction only loosely constrained; converges
  north of celestial equator ~ dec +27). 2 sigma below NVSS/RACS amplitudes. They found
  and modeled a declination-dependent systematic in faint source counts -- a caution for
  all shallow-survey dipoles.
- Older context (Colloquium 2505.23526): NVSS at 25 mJy D = (1.1 +/- 0.3)e-2 (2.2 sigma
  excess); TGSS 150 MHz D fell from 6.5e-2 to 1.4e-2 as flux-calibration systematics
  were fixed -- a worked example of how large spurious dipoles can be.

### 2.3 Diffuse gamma-ray background (DGB) dipole
- Kashlinsky, Atrio-Barandela & Shrader 2024 (arXiv:2401.04564, ApJL 961 L1):
  13 yr Fermi-LAT, iterative source/foreground clipping, 2.74 < E < 115.5 GeV.
  Dipole/monopole = 6-7% (S/N best at 5-30 GeV), stable under Galactic cuts
  (|b|>20,30,45; l cuts), stable in time (A-B split contributes <10% in power),
  ecliptic masking changes nothing.
- Direction (from paper text, exact quotes): for 45 <= l <= 315 and the |b| cuts,
  "the dipoles are at Galactic (l,b) = (270 -> 300, -40 -> 0)"; for the wider 30-330
  longitude range the dipoles sit near l - 360 ~ -30 -> 0 in their projection. 68% CL
  directional uncertainty ~10-20 deg. This is a POORLY CONSTRAINED direction; I adopt
  (285, -20) +/- ~20 as a representative apex and carry the full quoted range.
- Kinematic (Compton-Getting) expectation for v = 370 km/s: ~0.56% (their number).
  Observed amplitude would need v >~ 3000 km/s if kinematic.
- They note amplitude coincidence with the Auger >= 8 EeV dipole (both 6.5-7%) and a
  possible common origin; directional comparison to Auger is confounded by Galactic
  magnetic deflection of UHECRs.
- FLAG: I found no published independent confirmation or rebuttal of this measurement
  through 2026 in my searches; treat the 6-7% number as a single-group result. The
  Fermi-LAT collaboration itself has not (to my knowledge from these searches) published
  a confirming DGB dipole; unresolved-source and foreground-clipping choices dominate
  the systematics budget.

### 2.4 UHECR dipole (Pierre Auger, E >= 8 EeV)
- Science 2017 (arXiv:1709.07321): d = 6.5 +1.3/-0.9 % toward (l, b) = (233, -13),
  ~125 deg from the Galactic center -> extragalactic origin.
- ApJ 976 (2024) update, 19 yr (arXiv:2408.05292) and ICRC2025 (arXiv:2507.19243):
  significance 6.8 sigma above 8 EeV; the 8-16 EeV bin alone now exceeds 5 sigma
  (5.7 sigma); amplitude grows with energy; direction stable; no time variation
  (<0.3%/yr at 95% CL). Search summaries quote d = 0.065 +0.013/-0.009 at (233, -13);
  FLAG: I could not pull the exact 2024 table values (amplitude may be ~0.073 in the
  19-yr set); the direction (233, -13) is stable across all releases.
- Compton-Getting expectation for UHECR at these energies: ~0.6% (Kachelriess & Serpico
  2006, astro-ph/0512498). Observed is ~11x that. Nobody interprets the Auger dipole as
  kinematic: it is read as source anisotropy (local LSS + magnetic deflection).

### 2.5 CMB aberration/Doppler consistency (Planck 2013 XXVII)
- arXiv:1303.5087 (A&A 571 A27): boost signature in the CMB anisotropies themselves
  (aberration + modulation of the fluctuations, not the monopole Doppler).
  Component along the known dipole direction: v = 384 +/- 78 (stat) +/- 115 (syst) km/s.
  Ratio to 369.8 km/s: 1.04 +/- 0.21 (stat) +/- 0.31 (syst). Direction consistent with
  the dipole apex. This is the key internal check that the CMB dipole is (at least
  dominantly) kinematic: an intrinsic dipole would NOT aberrate the fluctuation field.

### 2.6 Other frame-anomaly claims
- Cluster scaling relations / bulk flow: Migkas et al. 2021 (arXiv:2103.13904, A&A 649
  A151): 9% apparent H0 anisotropy, extremum axis (l, b) ~ (280 +/- 35, -15 +/- 20),
  >5 sigma in their MC; alternatively a ~900 km/s bulk flow to >~ 500 Mpc.
  FLAMINGO-simulation reassessment (arXiv:2504.01745): probability in LCDM 0.12%
  (3.2 sigma; 3.6 sigma as a z < 0.1 bulk flow) -- significant but below the original
  claim. 2024 velocity-dispersion follow-up (A&A 2024, aa51755-24) is consistent.
- SN Ia dipole: Sorrenti, Durrer & Kunz 2023 (arXiv:2212.10328, JCAP 11 054):
  Pantheon+SH0ES low-z dipole gives v_sun = 328 +35/-42 km/s toward
  (RA, dec) = (139.4 +7.2/-8.0, 42.0 +7.2/-6.6) -- amplitude consistent with CMB but
  direction off by >3 sigma (my computed separation from the CMB apex: 55.4 deg; the
  signal fades for z_cut >~ 0.05, so this is a LOCAL bulk-flow statement, not a
  cosmological frame statement). Follow-up (arXiv:2403.17741) adds a significant
  quadrupole and negative monopole; a cosmographic analysis (arXiv:2407.07002) reads it
  as infall toward a ~120/h Mpc overdensity. Counterpoint: a 2025 MNRAS study (staf2048)
  finds NO local H0 anisotropy from Tully-Fisher or SN distances.
- Reviews: "Colloquium: The Cosmic Dipole Anomaly", Secrest, von Hausegger, Rameez,
  Mohayaee & Sarkar, Rev. Mod. Phys. 97 (2025), arXiv:2505.23526 (pro-anomaly,
  ">5 sigma" combined); "Cosmic dipole tensions" (arXiv:2509.18689); Abghari et al.
  (arXiv:2405.09762) for the skeptical case. Quaia quasars and GRBs are too sparse to
  decide (2505.23526; A&A 2025 aa56806-25).

---

## 3. Computed concordance table

Angular separations computed by me from the apexes above via
cos(theta) = sin b1 sin b2 + cos b1 cos b2 cos(l1 - l2), CMB apex (264.021, 48.253)
galactic / (167.94, -6.94) equatorial. Check: CatWISE gives 27.8 deg, reproducing the
published value. Ratio = D_obs / D_kin for that population.

```
Probe (arXiv)                  Apex (gal l, b)     Sep. from   D_obs           D_kin      Ratio  Excess signif.
                                                   CMB apex
------------------------------------------------------------------------------------------------------------------
CMB dipole (1807.06205)        (264.02, 48.25)      0.0 deg    beta=1.234e-3   --         1.00   reference
CMB aberration (1303.5087)     consistent w/ apex   ~0 (weak)  v=384+/-78+/-115 369.8 km/s 1.04   consistent (kinematic)
CatWISE QSO (2009.14826)       (238.2, 28.8)       27.8 deg    1.554e-2        7.3e-3     2.13   4.9sig -> 2.0-3.6sig contested
  " Dam et al. (2212.07733)    ~CMB direction       --         2.7x kinematic  --         2.7    5.7sig
NVSS (2305.15335)              eq (174, -18)       12.5 deg    1.37e-2 [flag]  4.5e-3     3.0    ~3sig
RACS-low (2305.15335)          eq (170, +8)        15.1 deg    1.53e-2 [flag]  4.5e-3     3.4    ~4sig
NVSS+RACS (2305.15335)         eq (169, -6)         1.4 deg    1.35e-2 [flag]  4.5e-3     3.0    4.8sig
MALS/MeerKAT (2408.16619)      dec ~ +27 (loose)   consistent  6.7e-3 +3.1-2.9 4.0e-3     1.7    ~1sig (CONSISTENT w/ kinematic)
DGB Fermi-LAT (2401.04564)     (270-300, -40-0)    68-94 deg   6-7e-2          5.6e-3     ~11-12 "highly significant", NOT kinematic
  " adopted rep. apex          (285, -20)+/-20     70.8 deg    6.5e-2          5.6e-3     11.6   --
Auger >=8 EeV (1709.07321,     (233, -13)          67.2 deg    6.5e-2 +1.3-0.9 ~6e-3      ~11    6.8sig vs isotropy
  2408.05292, 2507.19243)                                      (~7.3e-2 19yr?[flag])
SN Ia Pantheon+ (2212.10328)   eq (139.4, 42.0)    55.4 deg    v=328 km/s      369.8 km/s 0.89   direction off >3sig; z<0.05 only
Clusters/H0 (2103.13904)       (280, -15)+/-35,20  64.8 deg    ~900 km/s flow  370 km/s   ~2.4   >5sig orig; 3.2-3.6sig (2504.01745)
------------------------------------------------------------------------------------------------------------------
Auxiliary separations: DGB rep. apex vs Auger apex = 50.2 deg (consistent within the
DGB's 10-20 deg errors + UHECR magnetic deflection, per 2401.04564's own reading);
Migkas apex vs Auger apex ~ 47 deg; DGB range endpoint (270, -20) vs CMB apex = 68.5 deg.
```

[flag] on Wagenveld amplitudes: scale corrected from an internally inconsistent fetch
(x1e-3 vs x1e-2), see Sec. 2.2. [flag] on Auger 19-yr amplitude: exact updated value
unverified; direction verified stable.

---

## 4. Analysis in the foliation language

### (a) Do all frames concord? One foliation, at what confidence?

Split the estimators into two classes.

Class I -- boost estimators (number-count and CMB-internal probes with clean kinematic
theory): CMB dipole, CMB aberration, CatWISE quasars, NVSS, RACS, NVSS+RACS joint, MALS.
DIRECTIONS concord emphatically. The joint NVSS+RACS apex is 1.4 deg from the CMB apex
(chance probability for a random direction: (1-cos 1.4)/2 = 1.5e-4); CatWISE is 27.8 deg
away (chance 5.8e-2); NVSS and RACS individually 12-15 deg (each ~1-2e-2); aberration is
consistent along the apex. Treating directions as independent, the naive joint chance
that four independent axes land this close to a pre-specified axis is ~1e-8; even
penalizing heavily for the shared clustering dipole of local LSS (which correlates the
count dipole directions with each other, though NOT with the CMB apex a priori), the
direction concordance is conservatively at the 1e-4 - 1e-5 level. In foliation language:
every population that can measure the axis of the preferred frame measures the SAME
axis. There is one foliation direction, at >4 sigma-equivalent confidence, and no
credible estimator points anywhere else.

AMPLITUDES do not concord within Class I: counts give an inferred boost 2-3x the CMB
value (equivalent to 750-1100 km/s along the same axis), except MALS, which gives 1.0x
within errors. Taken literally, "one frame, disputed speed." Since the aberration of
the CMB fluctuation field independently confirms 370 km/s (1.04 +/- 0.31x), and MALS --
the deepest, best-systematics-controlled radio survey -- agrees with 370 km/s, the
amplitude excesses in shallow catalogs are more naturally read as population-level
(clustering, evolution, x and alpha calibration) or survey-level systematics than as a
faster boost. The Ellis-Baldwin expectation is exquisitely sensitive to the faint-end
source-count slope x measured AT the flux limit; the 2406.01871 result that deleting
0.9% local sources moves the dipole 10-15% shows how soft the amplitude side is.

Class II -- energy-flux / rate anomalies with no clean kinematic expectation: DGB,
Auger UHECR, cluster bulk flow, low-z SN dipole. These do NOT point at the CMB apex
(55-71 deg away) and have amplitudes 10x kinematic (DGB, UHECR) or correspond to
~900 km/s flows (clusters). Interestingly they roughly cluster among THEMSELVES:
Auger (233, -13), DGB (270-300, -40-0), Migkas (280 +/- 35, -15 +/- 20) all sit at
southern galactic latitudes at longitudes 230-300 -- pairwise separations ~47-50 deg,
marginal given their 15-35 deg errors. This looks like the local large-scale-structure
/ source-anisotropy sector, not the frame sector.

Verdict: the foliation-direction estimators concord on one frame at high confidence;
the discordant probes are exactly those where source astrophysics, not the boost,
dominates the dipole.

### (b) The quasar-dipole excess: mundane vs frame-anomaly readings

Mundane ladder (in rough order of current credibility):
1. Mask/multipole coupling + estimator bias: 50% sky coverage couples the octupole into
   the dipole and inflates the variance; significance drops to 3.3-3.6 sigma
   (2511.00822) or even ~2 sigma (2405.09762).
2. Clustering dipole of local LSS: nonneglible, direction-correlated with the kinematic
   dipole for a z-distribution with a low-z tail; explains part of the excess
   (2510.23769, 2406.01871), not all.
3. Ellis-Baldwin calibration: x and alpha are measured at the flux limit and assumed
   universal; redshift evolution of the source population changes D_kin at the tens of
   percent level (Dam 2212.07733 tested this -- modest help only).
4. Survey systematics: unexplained ecliptic-latitude gradient in CatWISE (2405.09762);
   WISE scanning-law-correlated photometric noise (SBI reanalysis); MALS's discovery of
   a declination systematic in its own faint counts is a cautionary tale for NVSS/RACS.
5. Frequency conspiracy problem for all of the above: the excess ratio is ~2-3x from
   150 MHz radio to mid-IR (2206.05624 finds no frequency dependence), which no single
   survey systematic naturally produces -- this is the strongest pro-anomaly card.

Frame-anomaly readings: (i) intrinsic CMB dipole component (early-universe superhorizon
isocurvature / tilted universe), so matter and CMB frames genuinely differ -- but the
aberration measurement caps any intrinsic component at roughly the 30% level (1 sigma),
and the DIRECTION agreement then becomes a coincidence to explain; (ii) genuinely larger
matter boost (local volume moving at ~600-1100 km/s relative to CMB frame within the
survey depth) -- i.e., very-large-scale bulk flow, qualitatively aligned with the
cluster/SN Class II signals; (iii) for the foliation program: if the preferred frame is
defined by the foliation and the CMB rides it exactly, the count-dipole excess is NOT
evidence for a second frame -- its direction concordance is evidence FOR the single
frame, with a disputed amplitude calibration. A real second frame would show up as a
second axis; none is observed.

### (c) What the "many independent estimators of one frame" framing makes visible

1. Direction and amplitude decouple cleanly. Individual papers headline the amplitude
   excess (a 1-parameter tension); the joint view shows a 2-parameter structure:
   directions concord at the 1e-4+ level while amplitudes scatter by 3x. A physical
   second frame generically moves BOTH; a population/systematic effect moves amplitude
   at fixed direction because the direction is inherited from the real boost plus
   direction-correlated clustering. The observed pattern (concordant axes, excess
   moduli) is exactly the systematics/clustering signature, and exactly NOT the
   two-frame signature. This is visible only in the joint view.
2. A joint direction likelihood is cheap and nobody publishes it as the headline:
   multiplying the direction-only chance probabilities of CatWISE + NVSS+RACS alone
   gives ~9e-6 for concordance with a pre-specified axis -- a >4 sigma-equivalent
   confirmation of the kinematic (single-foliation) axis that coexists with the
   amplitude anomaly. The same literature is simultaneously 5-sigma "for" and 4-sigma
   "against" the standard frame depending on which coordinate you read.
3. The excess-amplitude-with-concordant-direction pattern repeats across independent
   backgrounds (radio, IR) but SATURATES: deeper/cleaner data (MALS; aberration) revert
   to ratio ~1. In an estimator-population language: the estimator family is biased
   high in its shallow members and unbiased in its deep members -- a depth-dependent
   bias, not a frame effect. A frame effect cannot know the survey depth.
4. The Class II cluster (Auger / DGB / Migkas axes at b < 0, l ~ 230-300) is itself a
   weak concordance among probes usually discussed separately -- consistent with one
   local-LSS/bulk-flow axis distinct from the boost axis. Two axes in the data: the
   foliation axis (CMB apex) and the local-structure axis (~(260, -15)). Analyses that
   fit only a dipole will mix them; this degeneracy is visible only when all apexes are
   put on one sky.

### (d) Implications for the predicted phantom-decay gamma background dipole

Prediction under test: a phantom-decay gamma background whose dipole is purely
kinematic -- amplitude 3.7e-3 to 4.3e-3 (i.e., (3+Gamma)-type Compton-Getting factor
times beta), apex AT the CMB apex, plus a 0.12% spectral-edge modulation.

What the measured DGB dipole implies:
1. The floor is brutal in raw amplitude. Fermi-LAT's measured DGB dipole is 6-7e-2
   (2401.04564) -- 15-18x the predicted kinematic signal -- and it survives every
   Galactic cut, ecliptic cut, and time split the authors threw at it. Whatever it is
   (unresolved source anisotropy, UHECR-correlated emission, residual foreground), it
   is the noise floor for any kinematic-dipole search in this band. A blind dipole fit
   can never see a 4e-3 signal under a 6.5e-2 contaminant.
2. Direction helps by a factor ~3, not enough alone. The contaminant apex is ~70 deg
   from the CMB apex, so its projection onto the CMB-apex axis is cos(70.8) ~ 0.33,
   i.e. ~2.1e-2 along the predicted axis -- still ~5x the predicted signal. A
   fixed-axis (template) fit reduces but does not solve the problem; the contaminant's
   direction uncertainty (10-20 deg) also makes the projected leakage uncertain at the
   ~1e-2 level, an order of magnitude above the signal.
3. The spectral edge is the only clean discriminator, but it is instrument-limited.
   A 0.12% dipole-locked shift of a spectral edge is far below Fermi-LAT's ~10% energy
   resolution in this range; LAT cannot resolve it. The astrophysical DGB dipole is
   (per 2401.04564) broadband and spectrally smooth over 3-115 GeV, so a
   NARROW-spectral-feature dipole is orthogonal to the contaminant in principle --
   detectability therefore hinges entirely on an instrument with per-mille energy
   resolution at the edge energy (not existing in GeV space; if the edge falls in the
   MeV band, Compton telescopes ~1% resolution get closer but still 10x short).
4. Practical statement of detectability: with current data the prediction
   "D = 3.7-4.3e-3 at the CMB apex" is UNFALSIFIABLE-in-amplitude but has one testable
   corollary: after subtracting/attributing the 6.5e-2 astrophysical dipole (e.g., if
   its UHECR-source origin is confirmed and modeled out), the residual dipole along the
   CMB axis must not be SMALLER than ~4e-3 with the Compton-Getting sign. Conversely,
   the model is already SAFE from the current measurement: the observed DGB dipole
   neither confirms nor excludes a 4e-3 kinematic component (it is a <7% perturbation
   on the measured dipole, well inside its errors).
5. Strategy the concordance framing suggests: use the CMB apex as a fixed template, fit
   the DGB maps for the coefficient along that axis as a function of energy, and look
   for the (3+Gamma(E)) x beta scaling that only a kinematic component has (the
   astrophysical dipole has no reason to track the local spectral index in exactly this
   way). This energy-coherence test is the GeV analog of the aberration test that
   separates kinematic from intrinsic in the CMB, and it does not require resolving
   the 0.12% edge.

---

## 5. Honesty ledger (things I could not verify / known soft spots)

- Wagenveld 2023 amplitude scale (1e-2 vs 1e-3): corrected by cross-checking three
  sources; the corrected values are consistent with the quoted ratio-3 and 4.8 sigma.
- Auger 19-yr amplitude above 8 EeV: 6.8 sigma and direction (233, -13) verified;
  the exact updated amplitude (0.065 vs ~0.073) not pulled from the 2408.05292 table.
- DGB dipole direction: intrinsically loose in the source paper (quoted as ranges);
  my representative apex (285, -20) is an adoption, clearly labeled. No independent
  confirmation of the DGB dipole exists to my knowledge.
- Oayda et al. SBI reanalysis (2025): content from search snippets; arXiv ID unverified.
- CatWISE alpha: 1.26 (2009.14826 fetch) vs 1.06 (2505.23526 fetch) -- both returned by
  source fetches; discrepancy unresolved here, does not move D_kin outside 0.007-0.0075.
- SN Ia separation: my computed 55.4 deg from the CMB apex vs one fetch's paraphrase of
  "approximately 40 deg"; the >3 sigma direction-mismatch claim is the paper's own.
- All angular separations are my own spherical-trig computations; the CatWISE value
  reproduces the published 27.8 deg exactly, validating the pipeline.

## 6. Source list (arXiv IDs)

1807.06205 (Planck 2018 I) ; 1303.5087 (Planck 2013 XXVII) ; 2009.14826, 2206.05624
(Secrest) ; 2212.07733 (Dam) ; 2405.09762 (Abghari) ; 2511.00822, 2510.23769 (CatWISE
reassessments) ; 2305.15335, 2406.01871, 2408.16619 (radio dipoles) ; 2401.04564 (DGB) ;
1709.07321, 2408.05292, 2507.19243 (Auger) ; astro-ph/0512498 (UHECR Compton-Getting) ;
2103.13904, 2504.01745 (clusters) ; 2212.10328, 2403.17741, 2407.07002 (SN Ia) ;
2505.23526 (RMP Colloquium) ; 2509.18689 (dipole tensions).
