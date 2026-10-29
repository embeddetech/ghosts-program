# Canonical paper numbering — the single source of truth

**The immutable key is the CODENAME.** Series number, repo slug, and local folder
all *derive* from it and may change; the codename never does. When referring to a
paper in chats, commits, the ledger, or any log, **prefer the codename** (or
codename + current series number). A bare number alone is ambiguous across time —
see the legacy decoder below.

This file is machine-read by `histories/check_metrics.py`. Keep the master table's
pipe format intact.

## Master table

| codename | series | slug | folder | status |
|---|---|---|---|---|
| indivisible | 1 | p01-indivisible-ghosts | paper1 | published |
| measurable | 2 | p02-measurable-ghosts | paper2 | proposal (3pp) |
| instantaneous | 3 | p03-instantaneous-ghosts | paper3 | done (23pp) |
| conditioned | 4 | p04-conditioned-ghosts | paper4 | done (8pp) |
| choosing | 5 | p05-choosing-ghosts | paper5 | done (19pp) |
| unfolded | 6 | p06-unfolded-ghosts | paper6 | done (15pp) |
| renormalized | 7 | p07-renormalized-ghosts | paper7 | done (7pp) |
| exorcised | 8 | p08-exorcised-ghosts | paper8 | Fable-authored draft (19pp) |
| many | 9 | p09-many-ghosts | paper9 | Fable-authored draft (15pp) |
| dilated | 10 | p10-dilated-ghosts | paper10 | Fable-authored draft (20pp) |

*Unified 2026-07-18: `folder == series == companion-key` for every paper. The
`folder` column above matches the on-disk directory exactly; the checker
(`histories/check_metrics.py`) enforces `disk == canonical`.*

## Token conventions (going forward)

- **codename** — the invariant reference. Use it.
- **series number** `1..9` — the paper's position in the citation DAG (topological
  sort). Used in prose ("the fifth paper"), the ledger shorthand `pN`, and after
  unification the folder name `paperN`.
- **repo slug** `p0N-<codename>` — already series-based and stable; never rewrite it.
- **bibitem cite key** — the paper's **codename** (`\cite{choosing}`,
  `\cite{unfolded}`, …), matching this table one-to-one. The old
  `Companion`/`CompanionN` scheme is retired (a number-based key would go stale on
  any future reslot; the codename never does).

## Legacy decoder — how to read historical chats, transcripts, and pre-cutover logs

**The codename is the decoder. Numbers are not date-decodable.** The
series-unification happened *mid-day* on 2026-07-18, so a calendar date cannot
tell you which numbering a bare `pN` is in — material from earlier that same day
(the wave-27 work, the architecture audit) is FOLDER-numbered, material from later
that day is SERIES-numbered. Worse, a single continuous session chat log
**straddles the cutover**: its early turns use folder numbers and its later turns
use series numbers, in one file. There is no date or line that cleanly splits it.

Therefore, to resolve any bare number in any historical source, **use the content
to identify the codename, then read the current series number off the master
table** — the codename is invariant and straddle-proof (`choosing` is `choosing`
in every log, every era). Do not trust a bare number's face value in pre-unification
or straddling material.

**Precise cutover anchor (for committed data/docs, not chat logs).** The cutover
is the folder→series **unification commits** of 2026-07-18 (commit messages begin
`Unify numbering`; find them with `git log --grep "Unify numbering"`). Every
*committed* artifact (ledger, histories, folders, `notes.md`) is entirely
folder-numbered in commits *before* them and entirely series-numbered *at/after*
them — clean, because those files are rewritten atomically in the unification
commits. Only free-running **chat/session logs** straddle the moment, and for
those you fall back to the codename as above. Raw captures are immutable
provenance and are NOT rewritten.

Folder → series → codename map (for decoding a bare number once you know its scheme):

| legacy folder # (`pN` / `paperN` in old chats) | codename | current series # |
|---|---|---|
| p1 / paper | indivisible | 1 |
| p2 / paper2 | instantaneous | 3 |
| p3 / paper3 | conditioned | 4 |
| p4 / paper4 | choosing | 5 |
| p5 / paper5 | renormalized | 7 |
| p6 / paper6 | unfolded | 6 |
| p7 / paper7 | exorcised | 8 |
| p8 / paper8 | many | 9 |
| p9 / paper9 | measurable | 2 |

Worked example: a wave-22 transcript that says *"p4 claims audit"* means the
**choosing** paper — which is **series 5** under the current scheme. The active
audit rotation "p1/p2/p4/p6" in pre-cutover logs = **indivisible / instantaneous /
choosing / unfolded** = series **1 / 3 / 5 / 6**.

**Do not** apply this decoder twice. Committed sources after the unification
commits already use series numbering (folder == series) and need no decoding;
folder-scheme committed sources need it; straddling chat logs need it only for
their pre-unification turns — when in doubt, resolve via the codename, which
never needs decoding.

### Two stable-ID layers that are intentionally NOT renumbered

- **Per-paper finding IDs** — `Miss 2.3`, `Error 4.9`, etc. in the history files
  and ledger. The integer prefix is the paper's *legacy folder number* at the
  time the finding was logged. These are permanent identifiers cited in immutable
  git commit messages and chat transcripts, so renumbering them would create
  dangling references. Left as-is; decode the prefix via the map above (e.g.
  `Error 4.9` is a *choosing* = series-5 finding). The ledger's own top-level
  entry numbers (1–54, tracked by `check_metrics.py`) are a separate, scheme-
  independent sequence and are unaffected.
- **History-file bodies** — each `paperN-history.md` *header* names the current
  series + codename, but its dated body uses the numbering of the time (legacy
  folder numbers, capitalized "Paper N" prose, pre-reslot `p0N` slugs). Bodies
  are dated records, not rewritten; decode via the map.

## Why this exists

The 2026-07-15 repo reslot (inserting the experimental proposal at series 2)
made series numbers diverge from the drafting-order folder names, and the audit
logs had been keyed to folder numbers. Keying metrics to a mutable number is the
root cause of every "did we scramble the data?" scare. Anchoring to the codename
removes it: no future reslot can change what `choosing` means.
