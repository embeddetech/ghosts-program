# Open-thread registry (realignment artifact)

Consolidated output of the per-paper + program-level THREAD-HUNTER fan-out
(first run 2026-07-13). This is the **realignment artifact** the house rule
"clean up + realign before new audit sweeps" produces: one prioritized place
for every surfaced-but-unpulled thread, so an audit/work session executes
without re-deriving. Reconcile + prune this on each thread-hunt.
Classes: PROVABLE-NOW / NEEDS-INVESTIGATION / GENUINELY-OPEN / VERIFY-CITATION
/ DECISION-NEEDED / RE-EXAMINE / AUDIT-NEEDED / INCORPORATE.

## WORK STREAMS — these are different KINDS of work; don't conflate them
The registry is a mixed BACKLOG, not an audit queue. Sort each thread into:
1. **AUDIT SWEEP** — gate passes (claims/numerics/biblio) certifying EXISTING
   content. The "fresh session" work; fresh-eyes discipline + token headroom.
2. **REALIGN-BEFORE-GATE** — cheap hygiene a paper needs BEFORE its audit
   (citation verification, script-backing, self-consistency). Per the house
   rule, this PRECEDES that paper's audit — e.g. verify p7's 6 cites before
   the p7 gate; script-back App D/E before auditing the new p1 content.
3. **NEW INVESTIGATION / PROOF** (investigate-don't-defer) — prop:revival,
   countable-M, prop:state, chi-vs-p, sign(Re delta), P2 ladder, etc. NOT
   audits; run at the user's pace, own stream.
4. **INCORPORATION / DRAFTING** — horizons/dipole into papers; p9 (time-
   sensitive) + p8 drafting.
5. **AUTHOR DECISION** — dissemination, held NITs, publish-gate lift, optional-
   cite adjudication.
ORDERING: per paper, stream-2 realignment precedes its stream-1 audit;
streams 3/4/5 interleave at the user's pace. The "audit session" should stay
stream-1-focused, with each paper's stream-2 prereqs cleared first.

## CROSS-CUTTING — what multiple sweeps independently flagged (do first)
1. **AUDIT the new p1 monolith content** (SS9 + App C/D/E, +5 bibitems) —
   **DONE 2026-07-13 (gate pass 22)**. Claims Fable = 2 MAJOR (HELD, ledger
   14,15 — BOTH landed on the soft spots this registry predicted) + 6 MINOR +
   5 NIT; biblio Opus CLEAN; numerics Opus App C/D/E PASS (SS9 production-run
   numbers deferred per rails). **APPLIED 2026-07-14** (author "apply all
   recommended"; ledger 14,15 RESOLVED; p1 recompiled clean, 49pp). **SS9
   numerics VERIFIED 2026-07-14** under a `timeout 540` wall-cap (fixtures
   `paper1/scripts/SS9_NUMERICS.md`; prop:bo identity proven exact by hand) --
   caveat cleared; the wall-cap approach IS the structural fix.
2. **paper7's SIX placeholder citations** "[to be verified at audit]" — the
   exact hallucinated-ref failure mode the dissemination strategy leads with,
   in an unaudited draft. [p7, program]. VERIFY-CITATION, mostly trivial.
3. **prop:revival** (p1 App E) — the dictionary's only non-exact leg;
   Olver+stationary-phase, likely promotable to full proof. NEEDS-INVESTIGATION.
4. **Major-findings-ledger BACKFILL QUEUE** (4 items, ledger:91-95) — pure
   transcription from per-paper histories. INCORPORATE, mechanical.
5. **Two never-incorporated research/ GO results** — horizons_scoping_report
   (verdict GO) + dipole_concordance_report (positive) — candidate paper-7/8
   material, priority-perishable. INCORPORATE / DECISION-NEEDED.

## PAPER 1 (monolith, 48pp)
- SS9 + App C/D/E NEW UN-AUDITED (Fable-authored proofs) -> **AUDITED gate
  pass 22 (2026-07-13) + ALL FINDINGS APPLIED 2026-07-14 (author "apply all
  recommended"; ledger 14,15 RESOLVED).**
  Soft spots hit as predicted: thm:extlat(4) (c1) informal killing argument =>
  **confirmed MAJOR (ledger 15)**; App D thm:app-ghost supermartingale proof
  drops the reflection local-time term => **confirmed MAJOR (ledger 14)**.
  Held MINORs incl. eps-normalization App C vs App D, prop:app-ce1 construction
  violates its own C^1 hypotheses, "face"->"slice", n=1-only unitary-boundary.
- App D/E script-backing -> **DONE THIS SESSION** (scripts/appD_escape_
  dictionary.py + Code-availability entry). CAUGHT a numeric slip: central-
  potential absolute T_l values didn't reproduce (1.194->0.447, ~2.67x; ratio
  ->10^{1/3} was exact); fixed to reproduced values. App C/E = algebra, no
  standalone numerics. (Reproducibility gate working as designed.)
- Results map omits SS9 -> **FIXED THIS SESSION** (added row I' + reading path).
- New citations un-swept: inline App-D cites (Freidlin-Wentzell Ann.Probab.21
  (1993) 2215; Ito Berkeley Symp III (1972) 225; Blumenthal 1992; Khasminskii
  Thm 3.5) are house-style-inconsistent + unverified -> promote to bibitems;
  5 new bibitems (Zettl/EverittMarkus/BHS/ChenFukushima/Olver) never gated;
  FischerBL2026 future-dated metadata re-verify. VERIFY-CITATION (biblio pass).
- prop:revival [proved,sketch] -> proof agent. NEEDS-INVESTIGATION.
- thm:app-separable(iv) countable-M completeness (conjectural) -> closest-to-
  provable, but note TENSION: inf_n T_n>0 (needed for uniform-return argument)
  FAILS in the central case where T_l->0 (main.tex:2360). NEEDS-INVESTIGATION.
- rem:phasereceptacle(a) sticky<->L^2(+)C Wentzell b.c. -> established
  machinery; explicit construction could upgrade conjecture->proved row.
  NEEDS-INVESTIGATION (high payoff/effort).
- rem:Ecovariance "R generically E-dependent" asserted-not-shown -> 20-line
  numeric on one coupled U(2) extension exhibits the drift. NEEDS-INVESTIGATION.
- 2D glued certificate = the op:pu lambda>0 endgame; paper says "only assembly
  + error control remains" (Gaussian-beam tails + gluing); infrastructure
  exists (maslov_feasibility/glued_certificate_1d/tail_certificate). Companion-
  scale campaign, NOT a gate item. NEEDS-INVESTIGATION.
- conj:app-coupled (coupled-dictionary) -> GENUINELY-OPEN, leave labeled.
- op:pu (exact quartic-PU deficiency) -> GENUINELY-OPEN, has numerical support.
- microtype expansion=false build fix -> regenerate MiKTeX font maps
  (cosmetic; harmless for arXiv). DECISION-NEEDED (author machine).
- 4 MINORs from passes 20/21 already APPLIED this session (not open).

## PAPER 2 (in gate; scripts NOW co-located)
- **Scripts never auditor-rerun** (pass-1 numerics did arithmetic only b/c
  not co-located; 14 scripts now in paper3/scripts). AUDIT-NEEDED -> next
  numerics pass reruns all + traces every number.
- d=2 grid MINOR now resolvable: sizes=(8,16,32,48,64) in qft_bridge_e4_2d.py;
  state grid in caption + adjudicate the 2.7-vs-2.58 exponent fit. PROVABLE-NOW.
- **prop:state has NO proof** + omitted from the Sec-9 grading -> write the
  5-line tree-level proof OR relabel Claim. PROVABLE-NOW (claims exposure).
- M3 covariant window null (heavy-tailed estimator) -> robust estimator rerun
  of foliation_m3.py could upgrade principle->Measured. NEEDS-INVESTIGATION.
- op:shield converse -> finite/lattice constructive witness sub-thread.
- Script-path normalization (bare name.py, ~14x) — sole paper still on bare
  refs; DEFERRED (user call / at assembly). DECISION-NEEDED.
- Companion/hub URL resolves now checkable; Buoninfante flag deep-read;
  d=3 factorization 3%->1% MC bump. (lower priority)

## PAPER 3 (in gate, 8pp)
- **Held: RKW Cor. 15 constant unverified** (main.tex:254-258) — only open
  gate-pass-1 finding; load-bearing for the priority remark. arXiv:1102.5170
  has LaTeX source -> one fetch closes it. VERIFY-CITATION. **[top]**
- Open-Q (iii) chi-vs-p bound -> one-line mirror of Prop 3.5; add corollary or
  narrow the wording. PROVABLE-NOW.
- Open-Q (i) fidelity-bound extremal family -> aligned-filter ansatz already
  stated; numerics+derivation could upgrade Prop 4.4 to sharp. NEEDS-INVESTIGATION.
- Open-Q (iv) det Gamma vs det M single statement -> cross-paper (touches p1).
- `\date{... --- draft}` carries a status token -> strip at circulation
  (hysteresis-free). RE-EXAMINE.
- t3_cosi_forecast.py orphan -> move at assembly/p9 drafting. DECISION-NEEDED.

## PAPER 4 (in gate; alpha_g MAJOR resolved this session)
- **Caprini-Holscher-Schwarz GW constraint** flagged "VERIFY BEFORE CITING",
  never verified (research note only, not in paper). arXiv:1806.10940 fetch:
  confirm ~1/alpha_g scaling -> optional face-value strengthener, else mark
  dead. VERIFY-CITATION. **[top, ties off this session's fix]**
- **Monotone-death numbers not script-backed** but paper promises all numerics
  reproducible -> add ~15-line block to t4_rate_ladder.py (solar accel
  2.44e-20 vs 0.593; crossover ~1.2e90). PROVABLE-NOW.
- Fresh CLAIMS pass on the applied fork text (abstract + Sec5 + Table1 horn-1
  + closing). AUDIT-NEEDED.
- Holdom/Kuntz registry rows PENDING "careful read" (2408.04089, 2410.08278);
  Holdom prose half-adjudicates what registry marks unread. NEEDS-INVESTIGATION.
- Mannheim-branch strengtheners (moment-naturalness; Flanagan gamma_Edd->-1)
  investigated, not carried in -> author-taste add. DECISION-NEEDED.

## PAPER 5 (UNAUDITED draft)
- SIX placeholder citations -> **DONE THIS SESSION** (verified vs arXiv/
  journal): Ewasiuk title tail, Lagnese full authors+PRB104 L201106, Abel-
  Spannowsky-Williams real title, Deffayet already correct. TWO author-
  decision RESIDUALS: (a) BurshteinGoldstein metadata resolves but real title
  = superconducting-impurity crossover, NOT the "golden-rule onset" paraphrase
  -> confirm topical fit or replace; (b) **GarrigaVilenkin UNRESOLVED** — could
  not identify the paper; D=2 log result likely traces to CJM2004 (already
  cited) -> author reattribute-or-drop. DECISION-NEEDED.
- P2 exponent 0.156 "not converged" -> extend the Lambda ladder several
  doublings (t5_dimension_ladder.py, cheap) to sharpen/bound. NEEDS-INVESTIGATION.
- Schur-drift attribution (static-E0, "not resurgent") asserted-not-shown ->
  energy-dependent fold at one mid config tests it. NEEDS-INVESTIGATION.
- Failed vertex prediction (pre-registered) -> rerun to confirm 0.8620 pair +
  pre-registration record. RE-EXAMINE.
- Full fold at |Q|~81000 abandoned for memory -> iterative solves may fit.
- MPS volume scaling + born-vacuum log growth -> GENUINELY-OPEN.
- No sidecar yet; whole-paper number-tracing at first gate. AUDIT-NEEDED.

## PAPER 6 (claims 0/4; biblio+numerics CERT)
- **Companion-repo content push** (p04/p06 empty) -> known publish-gate dep,
  user-held. DECISION-NEEDED.
- **5 held terminology NITs** (author sign-off) — incl. the tower "is a
  theorem" clause that recurred passes 30 AND 31 (strongest). DECISION-NEEDED.
- sign(Re delta) via M2: answerable from existing 72-phase scan (compare phi
  vs 180-phi) -> sharpens or scopes the two-channel readout. NEEDS-INVESTIGATION.
- Silent-cone dense scan (0.05-deg, already run in agent scratch pass-20) not
  in committed script -> add fine-grid block, upgrade the hedge. PROVABLE-NOW.
- M2 "fires at every direction": exact column-sum law 1+kappa^2(T^2-s^2) for
  the cell suggests a general closed form -> could upgrade sampled->proved.
- "in preparation"/"develop elsewhere" pointers (main.tex:963-970) vs repo
  reality (p8 scripts-only) -> soften/pin (promissory-note species). RE-EXAMINE.
- Optional cite adds thrice no-actioned (WongZengLi 2507.16049, Barandes
  2507.21192) -> adjudicate once, close permanently. DECISION-NEEDED.

## PROGRAM-LEVEL
- Backfill queue (4) INCORPORATE [cross-cutting #4].
- horizons GO + dipole positive INCORPORATE [cross-cutting #5]; resolve the
  p07 identity (horizons vs Maldacena-conditioning) — both target the empty
  p07 slot.
- **p9 drafting is TIME-SENSITIVE** (Barandes-vs-Everett prominence, Mindscape
  323 clock); scoping DONE (p8_mwi_scoping) + inputs ready -> prioritize over
  p8 if forced. GENUINELY-OPEN (drafting).
- p1-numerics STRUCTURAL FIX -> **RESOLVED 2026-07-14**: the orchestrator ran
  the §9 backing scripts directly under a `timeout 540` wall-cap (they all
  complete inside it) + shipped fixtures `paper1/scripts/SS9_NUMERICS.md`. The
  cap-wall-time + fixtures approach worked and is the standing method for §9
  reruns; no future p1-numerics pass need attempt the full runs blind.
- Dissemination (author-gated): Barandes cold-email + "one checkable result"
  per reviewer (agent can pre-draft; deflation consolidation for Barandes);
  arXiv endorser (author); reception log. DECISION-NEEDED.
- Meta-research paper UNNAMED (parked; don't re-ask; keep feeding the timeline).
- Repo HOLD-lift assembly batch (paper7 recompile stale, content push, banner
  art, prior-art sweep) — user-HELD.
- **Dataset capture PENDING** at this session's wind-down (conv 790417fd;
  transcripts flush at teardown). [[session-end-dataset-capture]].
