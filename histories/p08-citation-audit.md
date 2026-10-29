# p08-exorcised — citation audit queue (INTERNAL; NOT part of the manuscript)

Per [[pdf-reads-provisional]]: the equation-level citations in `paper8/main.tex`
were extracted by MACHINE read (WebFetch/ar5iv) — a channel not trusted here.
**Re-audit these EVERY biblio pass; require an independent human / actual-PDF
confirmation before circulation; never mark settled on a machine pass.** (An
earlier machine read of the HLZ reference fabricated its author list.)

## Eq-level citations to re-verify against the actual PDFs
| ref | claim | eq (machine-extracted) | status |
|---|---|---|---|
| HLZ 2306.13714 | Neumann future BC | Eq. 30 | machine-only; PDF/human PENDING |
| HLZ | second BC ($\ddot h=k^2h$) | Eq. 59 (cov.) / 64 (Fourier) | machine-only; PENDING |
| HLZ | general Einstein–Λ mode | Eq. 67 | machine-only; PENDING |
| Buoninfante P3 2606.18349 | unstable sum rule $1=C$ | Eq. 34 | machine-only; PENDING |
| P3 | ghost neg-residue pole decomp. | Eq. 40 | machine-only; PENDING |
| P3 | ghost sum rule $Z+Z^*=1+C$ | Eq. 44 | machine-only; PENDING |
| P3 | masking $\sinh^2(\Gamma t/2)$ | Eq. 57 | machine-only; PENDING |
| Buoninfante P2 2605.29047 | general overlap $\sinh^2(\mathrm{Im}\,\Omega\,t)$ | Eq. 88 | machine-only; PENDING |
| P2 | narrow-width $\sinh^2(\Gamma t/2)$ | Eq. 92 | machine-only; PENDING |
| Buoninfante P1 2501.04097 | $(a;b,c)$ prescription taxonomy | Eqs. 5–6 | machine-only; PENDING |
| Anselmi 2503.01841 | only fakeon prescription viable | abstract | machine-only; PENDING |

Publisher/Crossref FIELD checks (title/vol/page/year — more reliable): all 8 refs
resolve; HLZ authors corrected Hertzberg-Loeb-Zhang → **Hell-Lüst-Zoupanos**.

## p08 draft status / remaining (internal)
- v0.4: both propositions proved (numerically backed), effects M and M′ priced,
  pole-sheet/Bochner dictionary; all references field-verified.
- Before circulation: a professional physics read; the standard claims/numerics/
  biblio audit lane; and the eq-level re-verification queued above.

## 2026-07-19 — Fable re-author + merge
p8 was re-authored blind by Fable from the sources, then Fable-merged against the
Opus draft (best-of-each); final is Fable-authored, 18pp. NEW citation added:
PaisUhlenbeck1950 = "On field theories with non-localized action", Phys. Rev. 79,
145 (1950) — the canonical ghost reference, standard fields (low risk; re-confirm
at biblio audit). HLZ eq citations reconciled to (30)/(59)/(64)/(67) per the
ar5iv spot-check. All eq-level citations remain machine-provisional — re-verify
every biblio pass.
