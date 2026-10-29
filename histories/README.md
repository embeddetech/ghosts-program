# Paper process histories

This directory contains one **process-history sidecar per paper**: a
reconstructed audit trail of how each manuscript actually came to be —
every error and miss, every adversarial review, every prior-art search,
every retraction, downgrade, and repositioning, with timestamps where
recoverable.

## Why this exists

The papers in this program were produced by an AI system (Claude
Fable 5, Anthropic) directed by a human author, and the program's
provenance notes promise that the *process* is auditable, not just the
results. These documents redeem that promise at event-level
resolution. They are assembled from primary sources:

- `notes.md` — the running lab notebook (dated entries, written at
  the time of the work);
- the git history, including the `pre-release-history` branch
  preserving the original overnight commit timestamps of paper 1;
- the complete session transcripts of the AI working sessions,
  including every subagent invocation (preserved in the author's
  archive; summarized here);
- the reports of the audit and literature agents (`../research/`).

## What counts as an event

Each history records, chronologically: research results as they
landed; **errors** (with the mechanism that caught each one — an
inline control column, an adversarial agent, an independent
recomputation, a referee-style read, or chance); **misses** (things
that survived one or more audit passes before being caught, recorded
as honestly as the catches); prior-art searches and their verdicts
(preempted / partial / clear), including post-hoc discoveries that
forced repositioning; audit rounds with their finding counts; and the
human author's steering decisions.

## Reading guide (the honesty ledger, program-wide)

Across the program to date: **six caught numerical/analytic artifacts,
one formal retraction, three replication-driven downgrades, one false
proof step caught by adversarial audit (present in two papers), two
chimera citations, one false quotation, and multiple claim-scope
corrections** — every one documented in the paper histories below, in
`notes.md`, and (where they changed a public document) in the papers'
own text. The pattern worth studying: essentially every substantive
error was caught by a *deliberately adversarial* mechanism (control
columns designed to fire, agents instructed to refute), and errors
repeatedly survived audits that were not aimed at them by name.

## Files

- `paper1-history.md` — Indivisible stochastic processes… (the
  overnight paper; 16 results; 4+ audit rounds; v1.0 frozen, v1.1)
- `paper2-history.md` — Ghost vacuum decay as a stochastic process…
  (the QFT bridge; 5 artifacts; 1 retraction; 3 downgrades)
- `paper3-history.md` — The price of a post-selected signal… (theorem
  found by sweep; 1 refuted conjecture; audit upgraded a proposition)
- `paper4-history.md` — Conformal gravity must choose… (1 critical
  proof-step error caught and repaired-to-stronger; root cause traced
  into paper 1)

- `process_timeline_papers12.md` — the mined fine-grained timeline
  of the 26-hour session that produced papers 1 and 2 (all 16
  subagent invocations with timestamps, ~85 human steering events
  paraphrased, every error event with its detector, all seven audit
  rounds, the complete publication register).

## Recoverability statement

From the preserved transcripts, essentially the entire process is
reconstructable at event level. Known gaps, stated for honesty: the
fine grain inside the first overnight research phase (23:38--03:34
UTC) survives only through paraphrased steering messages; the true
git timestamps of the squashed overnight commits survive only via
in-transcript discussion (and the Gitea archive branch); one context
compaction and one user-reported context loss are noted in the
timeline. Nothing else appears missing.

These documents are data. If the reader's interest is the physics,
read the papers; if it is what AI-led research looks like when the
tape is kept, read these.
