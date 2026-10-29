# Methodology timeline (how the research *method* evolved)

An ordered record of **methodology and process changes** in the Indivisible
Ghosts program — tracked by *where in the research process* each change
happened and *what prompted it*, so the meta-research narrative (AI-conducted
research under an adversarial audit gate) has a reconstructable through-line.
Wall-clock dates are annotated `[date]` as a secondary detail; the **spine is
the process sequence**, not the calendar (most of this compressed into a few
days, so datetime ordering would hide the actual progression).

Distinct from: `major-findings-ledger.md` (*what* defects were caught),
`auditor-error-log.md` (*rejected* leads), per-paper `histories/*.md`
(per-pass content).

**Maintenance rule:** append the next stage whenever the *method* changes — a
new/changed gate rule, a model-cadence change, a new agent role, a paper
split/merge decision, a new house rule, or a recurring failure mode + its
recovery protocol. Order by process progression (append at the end); note
what changed, the trigger, and where it's codified; tag the date inline.

---

## Stage 0 — Standing up the gate (before systematic auditing) `[2026-07-11/12]`
The founding method: a paper is release-eligible only after **K consecutive
fully-clean audit passes per lane**, each pass = **three fresh independent
auditors** (claims / numerics / bibliography) given **no histories/notes**
("fresh eyes"). Codified in `publish/release-gate.md`. Motive: make "audited"
*measurable*, not asserted.

## Stage 1 — First passes expose auditor fallibility `[2026-07-12]`
Early auditors produced false positives, so the method gained
**verify-before-apply** (rule 7: re-derive/re-check every lead before editing)
and the **`auditor-error-log.md`** (rejected leads recorded with reasons). The
gate now audits its own auditors.

## Stage 2 — First deep survivors force the gate to react `[2026-07-12/13]`
A MAJOR was found present during a *previously-declared-CLEAN* pass. This
established the **escalation trigger** (K rises when a clean pass is shown to
have missed a MAJOR) and, more deeply, the empirical lesson that **claims-lane
prose (abstract/title "exactly/precisely the condition" phrasings) is the real
blind spot**, not the math. First K bump **2 -> 3**. (major-findings 5-6.)

## Stage 3 — Refining WHO audits and HOW MUCH `[2026-07-13]`
Two coupled refinements, both grounded in the ledger's catch profile:
- **Per-lane K** (provisional): claims **4**, biblio **3**, numerics **3**;
  each lane resets only on its own applied finding. Claims K is highest
  because every deep survivor + both flagship MAJORs were claims-lane.
- **Per-lane model cadence** (supersedes the old Opus-default): claims
  **alternates Opus<->Fable every pass** with adversarial framing;
  biblio/numerics run Opus on counter 0, Fable after. Lesson: model
  **diversity + adversarial framing** is load-bearing, *not* tier — the
  deepest survivors were caught by adversarial Fable after CLEAN Opus passes.
  ([[audit-agent-model-policy]].)

## Stage 4 — Documentation-integrity conventions `[2026-07-13]`
To keep the released artifacts from leaking their own process/AI-accident
tells: **provenance note = number-agnostic** (no in-paper K); **papers
hysteresis-free** (plain \date, no version token/changelog — [[papers-hysteresis-free]]);
**repo pointers = Option A** (Companion* -> own repo; archive -> hub).

## Stage 5 — Instrumenting the program as a dataset `[2026-07-13]`
The program is also a meta-research object, so: **dataset capture** (zip
subagent transcripts + main-conversation JSONL into
`histories/agent-transcripts/` at each wind-down — [[session-end-dataset-capture]])
and the **major-findings ledger** (confirmed CRITICAL/MAJOR + prior-fix
reversals, with **survival depth**).

## Stage 6 — Learning to control the agents `[2026-07-13]`
Recurring subagent failure modes were codified with recovery protocols:
(a) numerics lane "arms a waiter" on a slow run -> SendMessage
abandon-and-report, and if the wait is blocked, **force-kill the python
process**; (b) 64k output-cap blow -> relaunch with COMPACT-OUTPUT; (c) API
timeout -> relaunch. The p1-numerics stall recurred **6x**; a naming ban
proved insufficient (the lane re-derives the banned run standalone) — a
structural fix (fixtures / step-count cap) is the standing mitigation.

## Stage 7 — From reactive to proactive thread-pursuit `[2026-07-13]`
The pivot from "audit what exists" to "extend what's proven":
- **HARD RULE — investigate, don't defer:** if a thread is concretely
  investigable, investigate it NOW; never park a finding as "future work."
  Trigger: I called the Feller-lemma's extensions (multi-D; U(1)<->lateral) a
  *future* "interesting seed"; user: "WHY WOULD WE LEAVE SOMETHING
  UNINVESTIGATED??" ([[investigate-dont-defer]].)
- **New agent role — thread-hunter** (`.claude/agents/thread-hunter.md`): a
  reusable read-only sweep for surfaced-but-unpulled threads, run
  occasionally, that codifies the rule as a proactive process.

## Stage 8 — Turning audit findings into new mathematics `[2026-07-13]`
- **Constructive-proof-of-a-flagged-leg:** when an audit flags a theorem leg
  as asserted-but-not-constructed, don't just downgrade — launch a Fable
  proof agent to *substantiate-or-downgrade*. First use: p1 `thm:dictionary`
  Feller leg (cross-model-confirmed MAJOR) -> escape-diffusion construction
  (the paper's word "exit" was provably wrong -> "regular") -> embedded as
  Lemma 8.2, and its extensions became Appendices D/E. (major-findings 12.)
- **Cross-model second-pass corroboration is load-bearing:** run the
  two-passes-per-paper cadence with a *different* model on pass 2 *before*
  adjudicating a held finding; both this batch's MAJORs were confirmed/
  escalated by the second model (p5 alpha_g MINOR->MAJOR; p1 leg Fable->Opus).

## Stage 9 — Deciding how the results are packaged `[2026-07-13]`
- **Method:** organization decisions go through a **judge panel** —
  independent keep-monolithic / split advocates + a neutral content-dependency
  map with a scoring matrix — then synthesis.
- **Decision (p1 beachhead): monolith + appendix tier.** Body = physics
  narrative (Part I machinery / Part II ghosts / Part III contact) with the
  dictionary as headline theorem + a one-page results map; the escape/
  deficiency machinery goes behind an appendix wall (App C Feller proof, App D
  multi-D, App E U(1)<->lateral). Rationale: priority/authority + the
  AI-provenance credibility argument (one rigorous monolith signals
  confidence; a burst of thin papers reads as the failure mode skeptics
  expect). Pre-registered fallback: spin the math companion only if a page
  limit forces it, post-acceptance.
- **New-content discipline:** appendices assembled from `research/` notes are
  NEW UN-AUDITED content -> the paper's counters stay 0 and the new material
  needs a fresh audit pass before certification.

## Stage 10 — Dissemination strategy `[2026-07-13]`
The program turns outward. **Strategy** (`publish/dissemination-strategy.md`):
order-of-operations is everything — earn a credibility signal, then let it
gate each next step; hype-first poisons review-first. Goals: (1) serious
domain-expert evaluation [primary, private, cheap-if-it-fails]; (2) arXiv
priority (needs an endorser) + journal, contingent on (1); (3) AI-community
awareness LAST, and **led by the METHODOLOGY paper, not the physics** (the
low-variance contribution — a clean negative is still a result).
- **Corrected fact:** arXiv did NOT ban AI research — only a CS-servers
  review/survey ban + a one-year AUTHOR ban for demonstrable LLM defects
  (hallucinated refs, errors). The gate's bibliography lane targets exactly
  that #1 concern -> lead with the gate. (Earlier "arXiv rejects AI content"
  overstatement corrected.)
- **Reviewer map:** Holmstrom (Jonathan's undergrad prof, U. Tulsa; draft
  already emailed, awaiting reply) = warm gut-check/bridge, NOT domain expert
  (optics/experimental, now Grad Dean). Barandes (Harvard) = THE domain test
  (the correspondence is the whole foundation); anticipated reaction: middle,
  confirming-of-framework with technical pushback (welcomes the extension +
  the "PT gates but doesn't generate" consolidation; questions the
  broken-phase no-go's depth + the speculative ghost application). Bender/
  Mannheim for p5.
- **New meta-thread:** community sentiment toward AI research over time is
  itself trackable data (arXiv-policy timeline + 12x citation-fabrication
  curve are datapoints; our program contributes another).

## Stage 11 — Realign-before-audit + per-paper thread-hunting `[2026-07-13]`
Two coupled process rules:
- **HOUSE RULE (user): always get everything cleaned up and REALIGNED before
  new audit sweeps.** A gate audit should run over a clean, consistent
  corpus, not one with un-incorporated results, stale HANDOFF/ledgers, held
  items, or new un-audited content mid-flight. Sequence: realign (thread-hunt
  -> synthesize -> do the cheap cleanups + incorporate/decide) FIRST, THEN
  launch audit sweeps (ideally in a fresh session for token headroom). The
  thread-hunter sweep is the realignment step, NOT an audit.
- **Thread-hunter fan-out (design fix):** run the thread-hunter PER PAPER
  (one scoped agent each) plus ONE program-level agent (histories/research/
  publish/proposal/p9/cross-cutting), in parallel, then synthesize — instead
  of one agent over the whole corpus (which goes shallow). First fan-out run
  this session (6 papers Fable + program-level Opus). Fold this into
  `.claude/agents/thread-hunter.md` guidance. [[investigate-dont-defer]].

### CONSIDERED (not yet adopted) — paired dual-model audit
User methodological ideal (2026-07-13): run Opus AND Fable on the SAME input
each pass and directly compare. Analysis:
- **Unique value alternation can't give:** a CONTROLLED catch-profile
  differential (same exact text -> what each model catches/misses), which is
  the headline dataset for the meta-research paper. Current alternation runs
  the two models on different text at different passes, so misses can't be
  cleanly attributed to model vs. text.
- **Cost is < 2x for equal confidence:** if a "pass" = both-models-clean
  (union), each pass is stronger evidence, so K can drop (2 paired ~ 4 single).
- **Concentrate the burn:** biblio is Crossref-checkable fact + numerics is
  script-reproducible (models converge there -> a 2nd model is redundant);
  divergence + every deep ledger survivor is CLAIMS-lane. So the high-value
  form = PAIRED claims lane, single-model biblio/numerics.
- **Honest limit:** paired-same-input catches cross-model-visible defects in
  one shot, but NOT the temporal/independent-context effect (a MAJOR was
  caught a pass LATER on unchanged text). Maximal rigor = paired-per-pass AND
  still-multi-pass; they catch different failure modes.
- **Recommendation (pending user decision):** paired Opus+Fable on the CLAIMS
  lane as standard; single-model alternation on biblio/numerics; plus a few
  deliberate fully-paired passes as a meta-paper dataset harvest. Not
  always-paired-everything. [[audit-agent-model-policy]].

## Stage 12 — Biblio lane: claim-SUPPORT, not just metadata `[2026-07-13]`
**Trigger:** the corpus's first confirmed hallucinated/misattributed citation
(major-findings entry 13, p7 GarrigaVilenkin) — a cite whose metadata looked
fine (real authors) but which no paper actually supports; the "low-d log"
result it credited to G-V was really CJM's (cited in the same sentence). Its
sibling BurshteinGoldstein was the mirror case: right paper, title != the
in-text paraphrase, CONFIRMED correct only by a content read. Together they
exposed that our biblio lane verified METADATA (title/authors/venue/DOI,
chimeras, verbatim quotes) but under-drove AUDIT.md's "characterization
fairness" clause — so a metadata-clean-but-topically-wrong cite could pass.
**Change:** the biblio lane must now operationalize claim-support PER CITATION
— read the cited work and confirm it backs the specific in-text claim, not
just that the reference resolves. Two new named failure species: MISATTRIBUTED
(real authors, no supporting paper) and TOPICAL-PARAPHRASE MISMATCH (right
paper, wrong description). Mandatory for load-bearing cites; spot-check the
rest. Codified in release-gate.md rule 6 + AUDIT.md. **Why it matters:** this
is exactly arXiv's #1 AI-slop concern; the fix is what makes the
dissemination plan's anti-hallucination claim true for MISATTRIBUTED cites,
not only fabricated ones. Method note: the catch itself came from
investigate-don't-defer (pulling on a "park it" residual) — [[investigate-dont-defer]].

## Stage 13 — Session-integrity fixes: no premature reset, forced-flush capture, cross-confirm MAJORs `[2026-07-14]`
**Trigger:** a single session surfaced three process failures at once. (a) The
per-session LOOP's "one unit then reset" (step 1 + step 8) fired a "reset and
go" prompt while a CONFIRMED numerics error and two MAJORs sat unapplied —
directly contradicting [[investigate-dont-defer]]. (b) The prior session's 6
do-more subagent transcripts were found UNRECOVERABLE: `.output` files are
0 bytes until the spawning agent's teardown, and that session ended without
capture, closing the flush window ("No transcript found for agent ID"). (c) A
theorem that had JUST been patched (thm:app-ghost, ledger 14 local-time gap)
still carried a SECOND independent MAJOR (ledger 20, the Zeno channel-tail),
caught only by the adversarial Fable pass after a CLEAN Opus pass.
**Change (three protocol edits, all now in force):**
1. **LOOP never prompts a reset while a concretely-actionable follow-up is open**
   (confirmed error, unapplied fix, uncaptured transcript). Token discipline
   caps how many NEW audit sweeps START, not whether the session FINISHES what
   it opened. THE LOOP steps 1/6/8 rewritten. [[investigate-dont-defer]].
2. **FORCED-FLUSH capture** (release-gate/DATASET + [[session-end-dataset-capture]]):
   a completed subagent's transcript can be forced to disk IN-SESSION by
   SendMessage-pinging it a no-op ("reply 'flushed' and stop") — it resumes,
   re-completes, and `.output` flushes (validated: 14 agents, 0 -> 90-570 KB).
   HARD rule: capture at EACH session's own wind-down; never defer to "next
   session" (the flush window closes when the session ends → permanent loss).
3. **Cross-confirm before applying a MAJOR:** a MAJOR that changes a theorem
   gets a targeted, adversarial cross-MODEL confirmation (try-to-refute prompt)
   before the edit. Validated this session: Fable found the Zeno gap, an Opus
   adversary independently confirmed the counterexample satisfies (D),(R) and
   the fix is minimal, THEN the theorem was scoped. Complements the standing
   "cross-model second-pass corroboration is load-bearing" rule.
**Why it matters:** (1) makes the agent finish, not hand off mid-repair; (2)
protects the meta-research dataset (the whole point of the audit program's
transcript archive) from silent teardown loss; (3) keeps theorem edits from
resting on a single model's reading. Data point for the model-diversity thesis:
this session logged the 5th clean-Opus-claims → Fable-MAJOR flip (ledger 20),
on already-patched text — temporal + independent-context diversity both load-
bearing. [[audit-agent-model-policy]] [[major-findings-tracking]].

## Stage 14 — Cross-paper dependency ("seam") audits `[2026-07-14]`
**Trigger:** p6's tower corollary ("negativity at depth two is a theorem for
every sector $M\ge2$") was a confirmed MAJOR (ledger 22) resting on the beable
basis being positive-diagonal-similar to the Jordan basis at general $M$ — a
property p6 asserted "as in the base cell" while crediting the tower structure to
Companion4 (=paper5). paper5 proved the tower STRUCTURE (prop:tower Jordan blocks;
thm:tower) but NEVER the positive-diagonal similarity. So the load-bearing premise
lived in the SEAM between the two papers: paper5's audits pass (its own claims are
sound); p6's fresh-eyes audits read "as in the base cell" as established and, being
single-paper, cannot open paper5 to check. Neither per-paper audit examines the
dependency — and it took a Fable-NIT -> Opus-MAJOR escalation even to surface it
within p6. (Resolution: a one-line strengthening of paper5's own prop:tower — the
shift's weights are POSITIVE, not merely nonzero, so the similarity is
positive-diagonal — added as paper5 Remark rem:posdiag; p6's theorem was then
RESTORED, not downgraded.)
**Change:** add a CROSS-PAPER DEPENDENCY audit dimension. When paper B cites paper
A for a premise ("supplied by the companion", "as in the base cell", "the X of
Companion-N"), an auditor must confirm paper A actually PROVES the specific property
B uses — not merely that A is cited and A's own claims hold. Practically: (1) a
periodic SEAM sweep listing every load-bearing cross-\cite{Companion*} dependency
and checking the cited paper delivers it; (2) when a finding rests on "as in the
base cell / companion", verify at the source and, when provable, fix at the SOURCE
paper (strengthen A) rather than only hedging B. **Why it matters:** per-paper
fresh-eyes auditing (Stages 1-13) is deliberately context-free — its strength on
single-paper claims but its blind spot on inter-paper seams; a multi-paper program
accumulates these seams silently. First instance caught + closed 2026-07-14
(ledger 22, user-prompted "how is this not getting caught in paper5's audits?").
[[investigate-dont-defer]] [[major-findings-tracking]].

## Stage 15 — A proof cross-confirm is NOT a gate audit of the writeup `[2026-07-14]`
**Trigger:** paper5's rem:posdiag (a new proof resolving the p6 tower MAJOR, ledger
22) PASSED a focused Opus MATH cross-confirm (verdict PROOF VALID) — yet a fresh
Fable NEW-CONTENT gate audit then found a MAJOR (ledger 23): the written conclusion
"sign structure invariant up the tower" omitted the load-bearing Toeplitz step (the
$D$-similarity is per-$M$; the cross-$M$ lift needs $e^{-\ii J_M t}$'s offset-only
Toeplitz structure). The cross-confirm reasoned the missing step implicitly (it was
checking whether the MATH is true — it is); the gate audit checked whether the
WRITEUP as it stands is complete — it wasn't. It also caught a dropped global phase
and an unspecified Jordan-block direction.
**Change:** a cross-model math cross-confirm (Stage 13) and a fresh new-content GATE
audit are DIFFERENT checks, and BOTH are required for newly-authored proofs.
Cross-confirm answers "is the claim true?"; the gate audit answers "does the text
prove it — no gaps, no overclaim, right scope?". Never let a validated-math
cross-confirm substitute for auditing the written proof. Corollary for numerics: a
NEW backing script must be re-derived from FIRST PRINCIPLES by a fresh auditor, not
merely re-run — rem:posdiag's script similarity-check was self-confirming (the
subdiagonal ratios telescope back to the weights) until hardened with an independent
ladder-operator construction.
**Why it matters:** the corpus's proofs are its load-bearing claims; a true theorem
with an incomplete writeup still fails peer review. First instance 2026-07-14
(ledger 23). [[investigate-dont-defer]] [[major-findings-tracking]].

## Stage 16 — Re-audit AFTER fixing: incomplete fixes hide `[2026-07-14]`
**Trigger:** the first FULL audit wave run over this session's many applied fixes
caught that TWO of the wave's four MAJORs were themselves INCOMPLETE FIXES from
earlier the same session: (a) ledger 24 — the wave-2 fix to thm:app-ghost's
(D)-parenthetical removed one wrong alternative but left another wrong sufficient
condition ($-V_1'\le Kx$, which bounds $\bar v$ from above, not below); (b) ledger
27 — the wave-3 fix to p7's "certifies at L=16" overclaim corrected only 2 of the 4
in-paper instances (the intro and Sec-mps closing survived). A third (ledger 25) was
a cross-paper consistency that the session's OWN new proof (rem:posdiag) created.
**Change:** applying a fix is not the end of the finding. (1) When a fix corrects a
QUANTIFIED/scoped claim, GREP the whole paper for every instance and fix all, not just
the first occurrence. (2) When a fix rewrites a hypothesis/sufficient condition,
re-derive that the REPLACEMENT is actually sufficient (not merely that the old one was
wrong). (3) A fix that STRENGTHENS one paper (a new proof) can INVALIDATE a scoped
claim in a companion — re-check the companions a new theorem touches (Stage 14 in
reverse). (4) Schedule a fresh full re-audit AFTER a batch of fixes; fixes are new
content and carry their own error rate. **Why it matters:** a session that applies many
fixes silently accumulates incomplete ones; only a post-fix re-audit surfaces them —
2/4 of this wave's MAJORs were self-inflicted-incomplete. [[investigate-dont-defer]]
[[major-findings-tracking]].

## Stage 17 -- Every document the corpus cites is in scope for the gate `[2026-07-15]`
**Trigger:** an AUTHOR QUESTION, not a lane. Asked to run the queued "proposal
first-pass audit", the orchestrator described the target; the author asked two
questions the process had never asked -- *"is it its own paper?"* and *"if p6
references it, how has that not been caught in an audit yet?"* Investigation
(ledger 31) found: **p6's biblio lane is CERTIFIED 3/3 on 22 of its 27 bibitems.**
Its own pass 27 states the arithmetic -- "27 bibitems; 22 external verified vs the
arXiv Atom API + Crossref DOIs" -- and 27-22 = the five `Companion*` self-citations,
carved out as a class and given existence-checks only. One of them pointed at a
document that had **never been audited in any lane**, and which p6 leans on for its
D5 error budget. Three biblio passes looked straight at that bibitem (pass 4: D5
device-feasibility gap logged as a *no-action informational*; pass 17: "GitHub repo
existence" verified; pass 21: the push-hold MAJOR) and each saw only whether the
referent EXISTED -- never whether it was any GOOD.
**Root cause -- packaging, not diligence.** The document was filed as a `proposal/`
passenger inside p06. That single packaging choice silently exempted it from BOTH
the audit gate AND every corpus-wide sweep, because it was not "a paper". The
exemption was invisible precisely because nothing declared it: no rule said
"proposals are out of scope"; it just was not in the list. Evidence it was
systematic rather than a one-off -- its `\date` still carried a non-plain
annotation plus a false "arXiv-pending" status long after the plain-date policy
had swept p1/p5/p7/p6 (each paper's `\date` was stripped BY ITS OWN AUDIT: no
audit, no strip); p4's in-text pointer claimed it lived "in the same repository";
and it made three uncited "the companion paper proves..." references with **zero**
companion bibitems -- a one-way citation nobody noticed for four days.
**Change:**
1. **Rule 6 extended (SELF-CITATIONS ARE CITATIONS).** Rule 6 was operationalized
   as "verify against Crossref/arXiv" = an EXTERNAL-record check; an internal
   self-cite has no Crossref record and fell through. The biblio lane must now
   (a) open the referenced document and apply claim-support to it as to any
   external work; (b) check its AUDIT STATUS -- citing an unaudited internal
   artifact for a load-bearing claim is a biblio finding (and is what
   dissemination-strategy.md already forbade as "cross-cite for load-bearing
   belief"); (c) check RECIPROCITY -- a one-way cite is a smell.
2. **Corollary, now a house rule: if it is worth citing, it is worth auditing;
   if it is not worth auditing, do not cite it.** Packaging (a `proposal/`, an
   appendix folder, a sidecar note) never changes scope.
3. **The proposal was promoted to paper 9** (`p09-measurable-ghosts`): its own
   repo, its own history ledger, the full audit bar. Numbering appends (slots 1-8
   are fixed at drafting time; p04-p08 already exist as public name reservations).
   "measurable", not "measured" -- nothing has been measured, and p6 pass 13 had
   already applied a NIT changing its own abstract from "measures" to "would
   measure" for exactly that reason.
**Why it matters:** this is the corpus's first **certification** defect -- every
prior ledger entry is a wrong or overclaimed statement IN a paper; this one is a
wrong statement ABOUT a paper, namely that its bibliography lane had been
verified to the standard. No lane failed: each did exactly what rule 6 specified.
The SPEC had the hole, and a spec hole is invisible to the agents executing it --
which is why it took a question from outside the loop to find. Note the shape for
the meta-research dataset: **the gate cannot audit its own scope.** Ask
periodically what the corpus TOUCHES that the gate does not COVER.
[[major-findings-tracking]] [[investigate-dont-defer]]

## Stage 18 -- Biblio re-cert needs CROSS-MODEL K>=3; a single rule-6-aware pass under-executes self-cite claim-support `[2026-07-16]`

Wave 7 (all-Opus) ran the first re-cert pass of the p5 and p6 biblio lanes under the
amended rule 6 (Stage 17: self-citations are citations; open the referent, apply
claim-support + reciprocity). Both passes declared CLEAN and advanced 0->1. Wave 8
(all-Fable), one day later, re-ran the same two lanes and found self-cite defects in BOTH
that the Opus pass had missed:
- **p6 (MAJOR, ledger 34):** the wave-7 Opus pass DID open the Companion4 referent and
  verified the tower/general-M similarity attribution -- but it checked only THAT site.
  It never checked the SEPARATE Companion4 cite at p6 L298, which attributes a
  Krein-theory / real-symplectic-lattice argument to paper5 that paper5 does not contain.
- **p5 (MINOR):** a Bender-Mannheim PRL/PRD twin-cite mis-target (the Jordan construction
  is in the PRD, not the cited PRL) survived the Opus pass.
- **p3 biblio (MINOR):** a "the companion showed [X and Hawking-Hertog] exit the sample
  space" over-attribution (p01 shows it only for the no-ghost quantization) survived the
  wave-7 Opus biblio pass too.

Lesson: the amended rule 6 is necessary but NOT self-enforcing -- a single pass, even a
rule-6-aware one, tends to check the ONE self-cite site it expects (the load-bearing
theorem the paper obviously leans on) and miss the others. Two rules updated in practice:
1. **Biblio re-cert requires the full cross-model K>=3** just like every other lane; a
   pass-1 CLEAN does not certify. (Wave-7's two pass-1 CLEANs were both premature.)
2. **A biblio pass must enumerate and claim-support EVERY self-cite SITE**, not just the
   referent's headline result. The p6 MAJOR hid precisely in a second, non-obvious site.

This is the wave-scale confirmation of the standing pattern (clean-Opus -> adversarial-Fable
MAJOR): wave 7 all-Opus looked converged across all 8 lanes; wave 8 all-Fable found a genuine
finding in every lane (3 MAJOR), resetting all 8 counters. Model+framing diversity is
load-bearing at the biblio lane, not only at claims.

**Validated at WAVE 9 (2026-07-16, all-Opus):** the Stage-18 remedy was exercised — both
p5 and p6 biblio re-certs ran a full per-SITE amended-rule-6 check (every one of the ~24
p5 / ~20 p6 Companion4 sites opened against its referent source) and BOTH came back CLEAN,
with p5's BenderMannheim twin-cite now verifying correctly targeted and p6's removed Krein
cite confirmed absent. When the pass actually enumerates every site, the defect class Stage
18 targets is caught (or confirmed gone). Re-certs advanced 0->1 toward K=3.

**Reinforced again at WAVE 10 (2026-07-16, all-Fable claims + Fable biblio re-certs):** a
SECOND consecutive cross-model catch. Wave-10 Fable found ANOTHER misattributed Companion4
self-cite (ledger 35: the p6 code-availability paragraph claimed the Merlin-row loop numbers
"reproduce from the companion's SCRIPTS as stated there," but paper5 states they are analytic
and has no such script) that the wave-9 Opus per-site re-cert PASS'd. Two waves, two Companion4
misattributions at DISTINCT sites (wave-8 L298 Krein; wave-10 L1007 provenance), each Fable-caught
after an Opus PASS. Biblio re-cert K>=3 with model alternation is now strongly validated, and a
self-cite "as stated there" claim must be checked against the referent's OWN disclosure, not just
the presence of a plausible result.

## Stage 19 -- A lead that survives a refute-and-re-raise cycle is escalated to a SYMBOLIC verifier, whose result is authoritative over any prose derivation `[2026-07-16]`
The p6 "generic perturbation oscillatory set contained in the phi=0 ray" lead was raised (wave-7
Opus), "refuted" by a cross-model prose derivation (wave-8 Fable: "strictly contained, codim 2,
paper correct"), and re-raised (wave-10 Fable: "only contained mod O(eps)"). The disagreement was
about a SUB-LEADING term while all passes agreed on the leading conclusion (the oscillatory set is
measure zero). A single focused subagent doing an EXPLICIT symbolic (sympy) eigenvalue expansion to
the disputed order settled it in one pass: the oscillatory locus is displaced from the ray by
O(eps) (the wave-8 "exact containment" refutation was itself imprecise), while measure zero holds
exactly. **Change:** when a lead survives one refute-and-re-raise cycle, do NOT trust the latest
prose derivation -- spawn a symbolic-verification subagent (exact expansion to the disputed order);
its result is authoritative. And log the CORRECTION back onto the prior auditor-error-log entry
(don't just add a new row) so a "refuted" verdict that was itself wrong is visibly overturned.

## Stage (2026-07-17, wave-21 wind-down) -- house rule: AUTO-INTEGRATE CONFIRMED FINDINGS
User directive: once an audit finding is CONFIRMED (survives verify-before-apply), integrate it IN-SESSION -- do the computation/lookup if the fix needs one -- and REMOVE it from any "owed" backlog. Never park a confirmed finding as "held for a final pass"/"owed follow-up" where the user might miss it still needs doing. Defensible/rejected leads still go to auditor-error-log (this rule is about confirmed findings only). Demonstrated same session: integrated the parked divisor-number computations (3x3/PU-grid/Gamma_big min-entries, computed from the papers own scripts) + the final-publication biblio polish (5 web-verified journal refs). Memory: auto-integrate-confirmed-findings.md. Extends investigate-dont-defer to post-confirmation audit findings.

## Stage (2026-07-19, p08 drafting + eq-level spot-check) -- house rule: MACHINE PDF/HTML READS ARE PROVISIONAL
User directive: "those pdf readings will need to be continuously audited, I don't trust your reads of pdfs." Machine extraction of equation numbers, verbatim quotes, and paper metadata from PDFs / ar5iv / HTML (WebFetch or a subagent) is a known-unreliable channel and must never be treated as settled on a single read. TRIGGER: while drafting p08-exorcised, a machine read FABRICATED the HLZ author list ("Hertzberg-Loeb-Zhang" for arXiv:2306.13714, actually Hell-Lust-Zoupanos, "On the Ghost Problem of Conformal Gravity"), and a summarizer returned INCONSISTENT eq numbers (56/64/67 vs 30/59/66/67) for that same paper; verify-before-apply caught both. RULE: eq-number and verbatim-quote citations obtained by machine read are PROVISIONAL -- flag them in-text as machine-extracted, keep them in the biblio audit queue, re-audit EVERY biblio pass (continuous, not once), and require an independent (ideally human / actual-PDF) confirmation before circulation. Never mark such a citation "settled" on one machine pass; do not drop the flag merely because a subagent reported "confirmed" (it read the same unreliable channel). Crossref/publisher field checks are more reliable than eq-level/quote extraction but even author lists have been machine-fabricated here, so still cross-check. Memory: pdf-reads-provisional.md. Extends verify-before-apply (rule 7) to machine-read provenance; the flag lives in an INTERNAL file (histories/p08-citation-audit.md), NEVER the manuscript.

## Stage (2026-07-19, after the internal-leak sweep) -- ENFORCED GATE: manuscript cleanliness
User directive: "This is your project, it's your responsibility to keep these papers clean!" -- after internal audit metadata repeatedly leaked INTO the manuscripts: the "release gate / AUDIT.md / histories / pass-by-pass ledger" provenance sentence in 7 papers; biblio-audit % comments that ship in the arXiv .tex source (paper5 ~49 lines); a machine-read "Citation-verification status" remark; a "scout/overlap sidecar" reference. Caught by the user, not by me -- three times in one session. REMEDY: cleanliness is now an ENFORCED invariant, not a promise. **histories/check_manuscripts.py** scans every paper for internal-info leaks (release gate, AUDIT.md, histories/, ledger, audit pass/lane, sidecar, spot-check, provisional, machine-extracted, verify-at-audit, biblio-verify % comments, and \TODO/draft apparatus). Policy: circulation-ready papers (canonical status published/done/proposal) must be PRISTINE -- ANY finding fails; drafts (draft/early) may carry \TODO draft scaffold (warned, not failed) but still fail on real internal leaks OUTSIDE a \TODO. RUN IT before every paper-touching commit and before any circulation, alongside check_metrics.py. Baseline PASS: papers 1-8 clean, paper9 skeleton only expected \TODO markers. The manuscript is the deliverable; audit/verification provenance lives only in internal files. Memories: pdf-reads-provisional.md (metadata half), and this gate (manuscript half).

## Stage (2026-07-19) -- CLAIM-SUPPORT is a distinct, mandatory, EXECUTED biblio check
Trigger: the H3 fabrication in p9 -- a real, correctly-cited source (Harrigan-Spekkens) credited with content it does not contain ("Sec. 6 nomic carve-out"). It passed a metadata-only citation check (reference real, fields correct) and both models' authoring; caught only by an argument-level review + primary-source read. KEY DISTINCTION: citation-METADATA verification ("is this a real paper with these fields?") != CLAIM-SUPPORT verification ("does the source actually say what our sentence attributes to it?"). A valid citation attached to a false characterization passes every metadata check and is MORE dangerous than a fake reference. NUANCE: AUDIT.md's biblio rubric already REQUIRED claim-support; the failure was EXECUTION (biblio agents did metadata-only). REMEDY: (a) claim-support must be executed every biblio pass, added to the AUDIT.md failure-mode checklist as "valid reference, false characterization"; (b) new sub-check "arXiv ID must resolve to the SAME paper as the journal ref" (a correct journal ref can sit beside a wrong preprint ID). Corpus-wide claim-support sweep run 2026-07-19 (histories/claim-support-sweep-2026-07-19.md): mature papers p1/p3/p5/p6/p7 all CLEAN -- the H3 class is isolated to the p9 skeleton. Also: an audit agent's OWN output is a machine read -- one claim-support agent FABRICATED a metadata finding (p1 "wrong arXiv IDs" that the paper does not list); verify-before-apply caught it (auditor-error-log). Memory: pdf-reads-provisional.md extended.

## Stage (2026-07-20, SESSION 2) -- MINOR/NIT get their own queryable registry; cross-model catches self-edits; a "simplification" fix can BURY a real issue
Trigger: the user asked whether ALL findings (incl. MINOR/NIT) are captured for meta-analysis. They were only in per-paper prose histories, not a queryable cross-paper index.
CHANGE 1 -- **new `histories/minor-findings-ledger.md`**: one structured row per MINOR/NIT (date, paper, model, severity, disposition, one-line defect), disposition taxonomy applied/held-defensible/held-biblio/deferred-notation/flagged-numerics/reported. The major ledger stays CRITICAL/MAJOR-only (keeps its survival-depth metric + count-checker clean). MINOR/NIT log here EVERY wave. Backfilled + grown to 78 rows this session. See memory [[major-findings-tracking]] (updated) + [[reporting-no-false-clean]] (new: never call a lane "clean" when MINOR/NIT were found).
CHANGE 2 -- **per-lane model cadence validated HARD**: after the all-Opus matrix (claims+numerics+biblio x10), two Fable cross-model CLAIMS waves on the 7 mature papers caught TWO bugs in the SAME SESSION's own Opus edits (p5 delta>0->delta!=0; p6 traceless-shift coinage) + a p3 false-converse + a p7 ledger-58 sibling miss. Lesson reinforced: alternate models; the adversary that authored/edited a claim shares its blind spots.
CHANGE 3 -- **an orchestrator "simplification" fix can BURY a real issue** (ledger 61, p2): Wave-1 Opus flagged a window-vs-t_c straddle as a NIT; the orchestrator "fixed" it by DROPPING the annotation (masking, not resolving); a same-model Wave-3 re-verify then graded the residue "informational, honest-as-written". Only a cross-model Fable pass + numerics escalated it to a confirmed MAJOR. Bake in: when a fix DELETES a caveat rather than sharpening it, treat that as a smell; re-derive the underlying claim, don't just tidy the prose.
CHANGE 4 -- **numerics lane = run-the-scripts**: this session's numerics auditors executed every script (not eyeballed); every quantitative claim in the corpus now traces to a reproducing script (or an explicitly-declared analytic in-text computation). Fixtures the re-runs appended to must be `git checkout`-restored (the p7 partial-folds .txt).

## Stage (2026-07-23/24): convergence certification — per-lane exhaustion, rotated-framing waves, human-PDF close-out, seam-sweep terminal pass
- **Per-lane × per-paper exhaustion as the convergence bar:** drive EVERY lane (claims, hypothesis-sufficiency, theorem-break, inter-paper consistency, numerics-reproduce, biblio-metadata) over EVERY paper. Reached this session: spine bulletproof (all hypothesis-sufficiency + theorem-break = NOTHING FOUND), all numerics reproduce (p1–p8), all biblio metadata clean (10 papers).
- **Rotated-framing multi-agent waves** (vs re-running identical claims passes): W1 hypothesis-sufficiency, W2 theorem-break ("try HARDEST to break the load-bearing theorem"), W3 abstract-vs-body/reader-misread, W4 completeness-critic/HOSTILE-REFEREE. Different framings catch different defect classes on the SAME converged text; the hostile-referee lens surfaced thesis-level overclaims (p3/p9) automated claims passes miss.
- **SEAM-SWEEP as the terminal framing:** after a paper accumulates many edits in one session, a pass explicitly hunting *collisions between those edits* (a fix not propagated to a summary/box sibling; two edits contradicting; a cross-ref pointing to the wrong sub-item). This caught 2 real misses at "exhaustion" (p9 boxed-conclusion, p10 strength-gradient) that all prior passes missed. **BAKE IN: run a seam-sweep as the last pass on any heavily-edited paper.**
- **Human-PDF close-out loop for borderline-CRITICAL/verbatim items:** user supplies the source PDF → orchestrator DERIVES the resolution → cross-model (Fable) adversarially verifies → apply. Closed p8 F1 (HLZ sign, RESOLVED-IN-FAVOR via ghost-killing/boundary-curvature derivation), confirmed HLZ/RKW citations, and caught 1 real Buoninfante eq-number miscitation the automated lanes missed (vindicates [[pdf-reads-provisional]]: only the human PDF catches internal eq-locator errors).
- **Text-vs-artifact adjudication by derivation:** a script/comment contradicting the manuscript (p6 lattice=generic vs body's open-oscillatory-band) resolved by DERIVING the physics (Hamiltonian unfolding → sign(a²−4b) → open half-spaces), then fixing whichever of {abstract, body, script} is wrong (body right; abstract+script fixed).
- **Cross-model discipline tally:** ~8 real defects caught this session (orchestrator fix-errors + prior-session bugs + the seam misses), none reaching a committed uncorrected edit. Cross-model verification (Fable on Opus fixes, and vice-versa) is load-bearing, not decorative.

## Stage (2026-07-31, W23): the defective-wave sweep, publisher-governs as a prompt-level rule, and model-attributed streaks

- **CHANGE 1 -- when a wave is found defective, re-audit EVERY edit it made.** major-ledger #79 (W21)
  proved the 07-24 biblio wave had applied an arXiv title form over the published one. Only #79's own
  site was reverted. W23 found **three more surviving errors from that same wave** (GSTZ in p3 AND p7,
  Ilhan-Kovner in p6, Konnig in p3), plus a fourth in p1 -- major-ledger #84. A defective premise is
  never load-bearing for exactly one edit. **BAKE IN: a confirmed wrong fix triggers a sweep of that
  wave's full diff, not a point revert.**

- **CHANGE 2 -- "publisher governs" must be stated IN the biblio prompt, not just in the error log.**
  A single W23 p5 biblio pass produced THREE arXiv-over-publisher flags (GSTZ, Ilhan-Kovner,
  Steinwachs), all rejected against Crossref. Auditors reliably default to the arXiv form -- which is
  the exact mechanism that produced #79 and #84. The rule has lived only in `auditor-error-log.md`,
  which fresh-eyes auditors are (correctly) forbidden to read. It therefore has to be in the prompt:
  *for any bibitem citing a journal, the PUBLISHED title/author form governs; verify against Crossref
  or the publisher, and never propose an arXiv form over a published one.*

- **CHANGE 3 -- verifying a REJECTED flag is a first-class discovery channel.** #84 was not found by an
  auditor finding a defect; it was found by the orchestrator checking an auditor flag that turned out
  to be WRONG, and noticing the correct form was missing elsewhere. **BAKE IN: when rejecting a biblio
  flag, grep the corpus for the entry before closing it** -- the rejection establishes the correct
  form, which makes every other copy checkable for free.

- **CHANGE 4 -- MAJOR candidates on a paper's central argument go to an adversarial verifier framed to
  REFUTE, before any edit.** W23 p9: an Opus auditor raised 5 MAJOR candidates; a Fable verifier
  instructed to default to "NOT A DEFECT" confirmed 2, refuted 1, and downgraded 2 to MINOR. Both
  directions paid -- two real defects applied (one, #85, had INVERTED a conclusion), three overreaches
  stopped at the gate. Cheaper and safer than either applying or dismissing on one model's read.

- **CHANGE 5 -- streaks are now MODEL-ATTRIBUTED (`histories/convergence-streaks.md`).** User bar
  (2026-07-31): 3 consecutive all-lane-clean passes per paper, **at least 2 of them Fable**. The prior
  accounting tracked only the count, so a paper could be labelled converged on Opus-heavy evidence --
  weaker, since the ledger's deepest survivors were repeatedly missed by clean Opus passes and caught
  by adversarially-framed Fable. Applying the stricter bar honestly reset p2/p3/p4 off "CONVERGED".

- **CHANGE 6 -- distinguish a numerics COVERAGE GAP from a numerics DISCREPANCY.** The W23 p1 auditor
  skipped a ~30-min blowup integration for runtime. That is not a clean lane and it is not a defect --
  it is an unaudited claim. Logged as a gap and the script re-run in-session. **BAKE IN: a lane may
  only be called clean over code that was actually executed; say which scripts were skipped.**
