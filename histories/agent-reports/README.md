# Agent-reports archive

Raw audit-agent transcripts for the release-gate cycles. **Caveat
(2026-07-12):** the harness empties each task's `.output` file after
delivering the agent's result, so of ~124 task files only 2 survived
with content when this archive was made; the rest were already 0 KB.
The durable audit record is therefore:

1. **Per-pass findings** — authoritative, in the history sidecars:
   `../paper6-history.md` (9 passes) and `../paper4-history.md`
   (1 pass). Every finding, severity, and fix is there.
2. **The pivotal report in full** — `p6-pass9-skeptical-referee.md`
   (reconstructed from the session record): the pass that moved
   paper 6 from "polish-ready" to "needs a thesis rescoping."
3. **Surviving raw transcripts** — in `raw/`:
   - `af1b3aa47ee5a4579.jsonl` (274 KB) = paper-6 pass-7 bibliography
     agent, full JSONL.
   - `bnrj7h29b.jsonl` (13 KB) = a background task output.

## Why the reports mostly aren't here verbatim
Each agent's *final report* was delivered to the orchestrator as a
task-notification and processed into the sidecars in real time; the
underlying transcript file was then emptied by the harness. Nothing
decision-relevant is lost — the findings (the actionable content) are
in the sidecars, and every audit is **re-runnable**: the scripts and
manuscripts are versioned, so any pass can be regenerated. What is not
recoverable is the agents' verbatim intermediate reasoning for the
routine (clean/no-action) passes. The one substantive report whose
detailed reasoning has lasting value (pass 9) is preserved in full
here.

## Pass index (detail in the sidecars)
Paper 6, K=2 gate (cross-model; passes 1-6 Fable-era agents, 7-9
Opus-era after the model swap):
- P1: 29 findings (1 CRIT false-converse "complex split => M1-free").
- P2: silent-cone half-domain-scan CRITICAL.
- P3: silent-cone geometry-inverted MAJOR + numerics/biblio.
- P4: 0 crit/major in claims (first); fix-propagation MAJOR (numerics).
- P5: Barandes named-but-uncited (biblio, missed by 4 prior passes).
- P6: NMEP author-list marker resolved; 189-deg endpoint.
- P7: bib fully clean; nit-only (first floor-level pass).
- P8: bib fully clean; **fresh-eyes claims caught the IK
  "complex-direction" mislabel** 6 checklist passes missed.
- P9: **skeptical-referee — 1 CRIT + 3 MAJOR CLAIM-overstatements**
  (see p6-pass9-skeptical-referee.md). Loop PAUSED for Fable rescoping.

Paper 4, K=2 gate, pass 1 (Opus-era): proofs airtight; alpha_g-fork
MAJOR (non-exhaustive), "B.Wang"->"Q.S.Wang" biblio MAJOR (verified),
scope hedges. Detail in `../paper4-history.md`.
