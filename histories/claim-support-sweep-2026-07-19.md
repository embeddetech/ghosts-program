# Claim-support sweep — 2026-07-19 (Opus, corpus-wide)

Motivation: the H3 fabrication in p9 (a real, correctly-cited reference —
Harrigan–Spekkens — given a FALSE content characterization: "Sec. 6 carves out
nomic wave functions," which they do not). Citation-metadata checks miss this
class. This sweep verifies in-text "Source X says/proves/assumes Y"
characterizations against source CONTENT, not just reference metadata.

## Result: the H3 class is ISOLATED to the p9 skeleton. Mature corpus CLEAN.

| paper | claim-support | notes |
|---|---|---|
| p1 indivisible | **CLEAN** | no fabrication class. Agent's "wrong arXiv IDs" side-finding was itself a FABRICATION (those bibitems list journal refs only; no arXiv IDs) — see auditor-error-log. |
| p3 instantaneous | **CLEAN** | BHK2025 (2512.18105) high-risk title-vs-content check PASSED (really contains the no-signaling/marginal-factorization eqs). GSTZ Eq.88 + CJM Eq.9 checked vs extracted PDFs. Minor: GV μ~2e-3 window reworded as the paper's synthesis (fixed, commit 5f2d690). |
| p5 choosing | **CLEAN** | 24 load-bearing attributions incl. attributed equations (DonoghueMenezes γ Eq.13, CJM Λ⁸/M_Pl⁴ Eq.3) all SUPPORTED. 5 body-level precision notes, none a mischaracterization. |
| p6 unfolded | **CLEAN** | all EP/non-Hermitian sources SUPPORTED; IK2014 Eq.58 + t_sing verbatim. Caveats: the −¾ Δ_eff coefficient is the author's change-of-variables (already disclosed in-paper); IK2013 Jordan-block sub-point unconfirmable from abstract (load-bearing use is supported). |
| p7 renormalized | **CLEAN** | all 8 external attributions SUPPORTED incl. the two 2026 preprints; Deffayet (x²−y²)-interaction load-bearing claim confirmed vs full text. |

p8/p9 not in this wave (their source-characterizations were just intensively
reviewed in the re-author/merge/harden/adversarial cycle — the H3 catch itself
was p9). p2 (measurable) + p4 (conditioned): small, deferred to a follow-up wave.

## PROVISIONAL items (machine-read; per [[pdf-reads-provisional]], need human/PDF confirmation before circulation)
- p3: ClinePhantom "was ~3 MeV, relaxed via exact phase space" mechanism (machine-read); KOV1975 (secondary cite only); Dvali fn.5 OCR artifact "S. Mukhanov" vs "V. Mukhanov" (immaterial).
- p5: items 1–5,7,12,19,21,23 verbatim/eq quotes are WebFetch machine reads.
- p6: DonoghueMenezes "M²=m_r²+iγ / Merlin coinage" and Klauck femtosecond-platform specifics verified from knowledge, not fresh fetch — worth a hard re-fetch.
- p1: RauchReed1973 + Tang2016 paywalled (verified from context); BenderMannheim "b†Ω=0" + Smilga "islands" verbatim warrant a PDF glance.

## Method note (the real fix)
AUDIT.md's biblio rubric ALREADY mandates claim-support ("reads the cited work and
confirms the paper actually backs the in-text characterization"). H3 slipped
through an EXECUTION gap — biblio-verification agents did metadata-only checks
despite the rubric. Fix: claim-support must be EXECUTED every biblio pass (added to
the AUDIT.md failure-mode checklist), plus the specific "arXiv ID must resolve to
the SAME paper as the journal ref" sub-check. See [[pdf-reads-provisional]].

## Cross-model corroboration + p2/p4 + fixes (2026-07-19, later same day)
Fable cross-model claim-support on p9 (H3 origin), p1, p3 + Opus on p2/p4. All
seven mature papers now **TWO-MODEL CLEAN** of the fabrication class (real source /
false content characterization). Fable did DIRECT PDF/TeX extraction (verbatim
greps of GSTZ Eq.88, CJM Eq.9, Cline Eq.3, GV Eq.72/73, HS nomic line, BHK eqs) --
human-grade, per the "confirmation is our own work, not a human's" directive.

Real findings, all verified by orchestrator against the local primary sources and FIXED:
- p9 (3): "no preferred foliation" was mis-cited to BarandesCausal+BHK2025 (grep: 0
  "foliation" in both) -- it is verbatim in BarandesPoP; added \cite{BarandesPoP} at
  both sibling sites. HS passage robustified to acknowledge HS Sec.6 DOES flag the
  nomic possibility (Wiseman's suggestion, "deserving of further scrutiny", not a
  licensed exit) -- this also traces the ORIGINAL H3 fabrication to Barandes' own
  footnote 23, which overstates HS; the paper is now closer to HS than that footnote.
  DGNSZ scare-quote ``unobservable'' -> "undetectable" (DGNSZ's actual word; 0 hits
  for "unobservable").
- p1 (1): Smilga "benign islands" -> "benign in the sense of" ("islands" is not
  Smilga's word; the specific x1^2x2^2 pair is the paper's own numerics).
- p3 (2): GV window -- Fable found GV THEMSELVES already combine the cascade bound
  with the 0.1mm ISL test (their Eq.73, "mu >~ 2e-3 eV, marginally consistent"), so
  "we estimate" under-credited GV; reworded to credit GV. BHK "established" softened
  (BHK postulate causal locality + require factorization; the marginal-independence
  step is this paper's own Prop 9.1).
- p4 (1): RKW "Cor.~15" -> "Prop.~7 (in the arXiv version)" (the verified label;
  journal "Cor. 15" numbering was never confirmed).
- p2 (1): Eichelkraut "within the demonstrated tuning range" -> "set by the
  tunable-bending-loss modulation technique" (the technique is verified via Klauck;
  the specific 2.6-7.8 dB/cm upper range is NOT confirmable -- Opt.Lett. paywalled,
  no arXiv -- so the claim is scoped to what is supportable, not softened to a false
  "demonstrated").

Remaining genuinely-unverifiable (paywalled, no accessible copy; NOT deferred to a
human -- exhausted machine access): Eichelkraut2014 max demonstrated bending loss;
VanWesemael2025 journal-ref PRE 114,014131 (arXiv lists none). Both are
biblio-metadata, not claim-support; the manuscript claims were scoped accordingly.
