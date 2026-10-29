# Convergence streaks — the strict bar (3 consecutive CLEAN passes, ≥2 by Fable)

**User bar (2026-07-31):** every paper must pass **all 3 lanes** (claims / numerics /
bibliography) on **3 consecutive audit passes**, of which **at least 2 are Fable**.

**CLEAN = zero findings at ANY severity, cosmetic NITs included.** Any applied finding
resets the streak to 0 and clears the model tally. A *rejected* auditor lead (logged to
`auditor-error-log.md`) does NOT reset. A pass that only re-confirms a held human-PDF
item does NOT reset.

**Why the model tally.** The major-findings ledger shows the deepest survivors were
missed by repeated clean *Opus* passes and caught by adversarially-framed *Fable*
(see [[audit-agent-model-policy]]). Three clean Opus passes is weaker evidence than
two clean Fable passes; the bar encodes that. An Opus pass still counts toward the 3 —
it just cannot be more than one of them.

## Baseline as of 2026-07-31 (start of W23)

Reconstructed from the per-paper history sidecars, counting only passes that are
**model-attributed** and recorded **zero applied findings**. This is deliberately
conservative and is **stricter than the `HANDOFF.md` "3/3 CONVERGED" labels** for
p2/p3/p4: those labels were earned under an earlier accounting that credited
convergence re-confirmations, and the sidecars do not record the per-pass model
consistently enough to certify the ≥2-Fable half retroactively. Re-earning them is
cheap; asserting them is not.

| paper | codename | streak | passes in streak (model) | Fable in streak | needs |
|---|---|---|---|---|---|
| p1 | indivisible | 1/3 | W22 Opus | 0 | 2 more, **both Fable** |
| p2 | measurable | 1/3 | W22 Fable | 1 | 2 more, ≥1 Fable |
| p3 | instantaneous | 1/3 | W22 Opus | 0 | 2 more, **both Fable** |
| p4 | conditioned | 2/3 | 07-23 Opus, W22 Fable | 1 | 1 more, **Fable** |
| p5 | choosing | 1/3 | W22 Opus | 0 | 2 more, **both Fable** |
| p6 | unfolded | 0/3 | — (W22 Opus: 1 NIT applied) | 0 | 3, ≥2 Fable |
| p7 | renormalized | 0/3 | — (W22 Fable: MAJOR #83) | 0 | 3, ≥2 Fable |
| p8 | exorcised | 0/3 | — (W22 Opus: 1 MINOR + 2 NIT) | 0 | 3, ≥2 Fable |
| p9 | many | 0/3 | — (W22 Fable: 2 MINOR + 3 NIT) | 0 | 3, ≥2 Fable |
| p10 | dilated | 0/3 | — (W22 Opus: 2 NIT applied) | 0 | 3, ≥2 Fable |

## Wave log

### W23 — 2026-07-31
Assignment: Fable — p1, p5, p8, p10.  Opus — p7, p9 (+ a Fable cross-verifier on the
p9 MAJOR candidates).

**Every audited paper took findings. No paper advanced a streak this wave.**

| paper | model | outcome | streak after |
|---|---|---|---|
| p1 | Fable | **claims CLEAN** on full 50pp re-derivation; 2 NIT + 1 numerics coverage gap (gap re-run in-session, all 4 claim sets confirmed) | 0/3 |
| p3 | — | **reset by a cross-paper biblio fix** (major-ledger #84) | 0/3 |
| p5 | Fable | 1 MINOR + 5 NIT; claims/numerics otherwise clean | 0/3 |
| p6 | — | **reset by a cross-paper biblio fix** (#84) | 0/3 |
| p7 | Opus + Fable verify | **1 MAJOR** (#87 wrong mechanism, in the TITLE) + 2 downgraded MINOR + ~10 MINOR/NIT; 2 of 5 MAJOR candidates REFUTED | 0/3 |
| p8 | Fable | 2 MINOR + 2 NIT; **no MAJOR, 2nd consecutive wave** | 0/3 |
| p9 | Opus + Fable verify | **2 MAJOR** (#85 template misattribution, #86 priority overclaim) + 2 MINOR | 0/3 |
| p10 | Fable | 2 MINOR + 3 NIT incl. a theorem-scope gap; no MAJOR | 0/3 |
| p2, p4 | — | not audited this wave | 1/3, 2/3 (unchanged) |

**W23 closed with major ledger 83->87, minor 154->162.** The two adversarial verifier passes (p9, p7) between them took **10 MAJOR candidates down to 3 confirmed**, refuting 3 outright and downgrading 4 -- while the 3 that survived included one that inverted a conclusion (#85) and one that was wrong in a paper's title (#87).

**The wave's other main result is #84**: verifying a *rejected* auditor flag exposed three
surviving wrong bibitems in p3/p6/p7, all from the single 07-24 biblio wave whose
premise (arXiv form over published form) had already been proven defective in W21 by
major-ledger #79 — but only #79's own site was ever reverted. **Process lesson now
baked into THE LOOP: when a wave is found to have applied a wrong fix on a flawed
premise, re-audit EVERY edit that wave made.**

Second result: the p9 pair. An Opus auditor raised 5 MAJOR candidates; an adversarial
Fable verifier confirmed 2, refuted 1, and downgraded 2. Both directions of cross-model
diversity paid — it caught two real defects (one of which *inverted* a conclusion) and
stopped three overreaches from reaching the manuscript.

### W24 — 2026-08-01 (in progress)
**All six auditors Fable**, since every streak is at 0–2 and each needs ≥2 Fable of its 3.
Launched: p4, p7, p9, p8, p2, p10.  Rolling in: p1 (Opus, to cross-verify W23's Fable
claims-clean result), p3, p5, p6.

Two W23 lessons are now built into the prompts:
- **publisher-governs is stated IN the biblio prompt.** It previously lived only in
  `auditor-error-log.md`, which fresh-eyes auditors are correctly forbidden to read — so
  the rule was structurally unenforceable and auditors defaulted to arXiv forms. That is
  the exact mechanism behind #79 and #84.
- **p7, p9 and p10 get a SEAM-SWEEP framing** (hunt collisions between recent edits:
  stale paraphrased siblings, newly-contradicting statements, cross-refs pointing at the
  wrong sub-item). W23 revised p7 in 10+ places including its title and p9 in four
  load-bearing places, and the seam framing has previously caught real misses at
  "exhaustion".
- p7's prompt additionally asks whether any *interpretive mechanism* offered for a
  measured effect actually holds in the paper's own model — the #87 failure mode, where
  every number was right and only the story was wrong.

**p4 is the wave's convergence candidate:** it sits at 2/3 with one Opus + one Fable
already banked, so a single clean Fable pass converges it under the strict bar.

Results: see the W24/W25 wave logs below.

### W24 results — 2026-08-01
Six MAJORs (#84-#88, #91, #92). **Four were in the audit's own prior repairs.**
Every audited paper took findings. p4's CONTENT lanes came back clean (3/3
content) but the corpus-wide #88 repo gate is tracked separately, per the note
below.

### W25 — 2026-08-01: Fable p1/p3/p5/p6 + seam-sweeps p7/p9
**Zero new physics defects.** Two auditor flags REFUTED from primary PDFs.
Three standing human-PDF holds CLOSED — there are now none.

| paper | model | outcome | streak after |
|---|---|---|---|
| p1 | Fable | **CLEAN at every severity** — the cleanest pass the flagship has had | **1/3** |
| p3 | Fable | no MAJOR; 15/15 scripts; 1 MINOR (configuration provenance) | 0/3 |
| p5 | Fable | no MAJOR; 5/5 scripts; 1 MINOR (dropped norm qualifier) | 0/3 |
| p6 | Fable | no MAJOR; 7/7 scripts; 2 script-label fixes, paper was right | 0/3 |
| p7 | Fable seam | #94 reproducibility (RESOLVED, 4th attempt); W24 fixes confirmed | 0/3 |
| p9 | Fable seam | no MAJOR; 6 MINOR, mostly seam damage from W23/W24 edits | 0/3 |

### On the #88 repo gate and streak accounting
#88 is one external condition affecting nine papers identically, and the user
has decided it (the repos will be populated; references stay). It is therefore
tracked as a **circulation gate**, not as a per-paper streak-resetting content
finding — papers are scored on content lanes and separately marked
circulation-ready. That interpretation was flagged to the user rather than
applied silently.

### W26 — 2026-08-01/02: Opus p1, Fable p2/p4/p8/p10, Fable seam-sweep p7

**Zero MAJORs on physics across the whole wave.** Every finding was provenance,
presentation, or editorial residue — several of it the audit's own.

| paper | model | outcome | streak after |
|---|---|---|---|
| p1 | Opus | mathematics CONFIRMED by re-derivation; **5 configuration-provenance MINORs** (λ never stated anywhere; T_esc, ω, E and a homogeneity mismatch all unlabelled) | **0/3** (reset from 1/3) |
| p2 | Fable | physics clean, deterministic; the `d2_sweep` gap CLOSED with new printed block [C6]; 2 MINOR | 0/3 |
| p4 | Fable | **inverted claim in the abstract** ("anisotropy costs survival") found only because the auditor was told to break it | 0/3 |
| p8 | Fable | no MAJOR (4th wave); **the Buoninfante locator hold RESOLVED from the PDFs — the manuscript was right** | 0/3 |
| p10 | Fable | no MAJOR; numerics + biblio clean; Feller convention validated against three known cases | 0/3 |
| p7 | Fable seam | **partial** — independently re-ran `t5_floor_mechanism.py` and reproduced blocks [1]–[3] IDENTICALLY (L=4 exact stationarity, the rank-40 tail, and the D=40 vs D=100 controls all match the archived output). Stopped before the L=16 block: it is a 1–2 h run gated behind `--l16`, and that value was already independently confirmed to six digits (0.249313) in W25. Remaining lanes were reported complete. | 0/3 (unchanged) |

**What this wave establishes.** The physics has now been stable for three
consecutive waves. What still resets streaks is whether a reader could
*reconstruct* the work from the papers alone. By that standard p1 genuinely
failed: a fifty-page published paper whose quoted numbers depend on a quartic
coupling that appears nowhere in the text. That is a real reproducibility
defect, not a nitpick, and it was invisible to every pass that checked only
whether the numbers reproduce *from the scripts*.

**Three verification habits earned their place this wave:**
- *Frame the converged papers as the hardest targets.* p4's inverted abstract
  claim had survived every prior clean pass; it surfaced the moment an auditor
  was told to break the paper rather than confirm it.
- *Re-test clean verdicts cross-model rather than banking them.* p1's Opus pass
  confirmed the mathematics and split off five defects the Fable pass missed.
- *Fetch the PDF.* p8's locator hold resolved in the manuscript's favour, the
  third render-vs-PDF false alarm of the session.

### W27 — not yet launched
Opus p1 (cross-model test of the clean verdict), Fable p2/p4/p8/p10, Fable
seam-sweep p7. p7's auditor is directed to attack the newly-committed
`t5_floor_mechanism.py` rather than trust it. p1 and p4 are framed as the
hardest targets *because* they came back clean — that is where a lazy second
"clean" is cheapest to produce.
