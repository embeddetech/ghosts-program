# Overfull \hbox worklist (corpus typography sweep)

> **DONE 2026-07-24 (conv 954cb52d cont'd). Corpus-wide 0 overfull >10pt confirmed
> on fresh `latexmk -g` builds for all 10 papers.** Fixes committed per paper:
> p6 (468pt table → wrapping `p{}` cols, +array); p5 (78pt proof eq → display;
> 112/56pt code block → xurl + `\texttt` `\allowbreak`); p7 (113/87pt code block →
> group redefining `\_` and `/` as breakpoints + local `\emergencystretch`);
> p2 (94pt device table → `\resizebox`, +graphicx; **was CONVERGED, now strictly
> clean**); p8 (28pt Kraus product → `\allowbreak` between factors); p1 (23pt `T_n`
> display → `gathered`; 11pt prop:deflation head → local `\emergencystretch`;
> root PDF refreshed); p3 (17.78pt trilemma bullet → local `\emergencystretch`;
> **was CONVERGED, now strictly clean**). Residual boxes everywhere are <10pt.
> **Process rule now in THE LOOP:** per-paper `grep "Overfull" main.log` (UNFILTERED,
> fresh `-g` build) → require 0 >10pt, every wave.

Discovered 2026-07-24 (audit-campaign W14). Content-focused auditors do NOT catch
overfull \hbox margin overruns — this is a corpus invariant they miss (like the
`\phantomsection` sweep, major-ledger-adjacent minor #110). **Add a per-paper
`grep "Overfull" main.log` (UNFILTERED, on a FRESH `latexmk -g` build) check to
every audit wave.** NOTE the `\\hbox` grep pattern mis-escapes in Git-Bash and gives
FALSE NEGATIVES — always grep the plain word `Overfull`.

Authoritative inventory (fresh `latexmk -g` builds, 2026-07-24). Sizes in pt "too wide":

| Paper | Overfull(s) >10pt | Line range(s) | Likely cause |
|---|---|---|---|
| paper1 | 23.41, 11.18 (+4 small <7pt) | L2248 (display eq); L425–433 | 23pt = display eq `T(E,ω)=∫…, \qquad x_n any base point…` (the `\qquad`+condition too wide → split/break the display); 11pt = long inline math line |
| paper2 | **94.47** | L100–112 (device table) | The 6-col device table (`lccccc`, already `\small`) is far too wide — needs `\resizebox{\textwidth}{!}{…}` (add graphicx if absent) OR `\footnotesize`+`\setlength{\tabcolsep}{3pt}` OR shorten headers. My W1 additions "(D3: window period)" + "asymptote" widened an already-tight table. **p2 is CONVERGED but not strictly clean until fixed.** |
| paper3 | 17.78 (+3 small) | L235–238 | trilemma bullet "coupled ghosts, empirical Lorentz invariance, definite configurations---any" — long words + em-dash, no break; reword or `\-`/`\linebreak`. **p3 CONVERGED but not strictly clean until fixed.** |
| paper5 | **112.62, 78.59, 56.83** | L420–430; L1118–1126 (×2) | wide display equations/tables — inspect; likely need `\resizebox`/`split`/`\!` spacing |
| paper6 | **468.26** (+2 tiny) | L730–754 | MASSIVE — almost certainly a very wide TABLE (deformation/divisor table); needs `\resizebox` or restructure. Top priority. |
| paper7 | **113.62, 87.40** (+1 tiny) | L486–502 (×2) | wide display equation(s)/table — inspect |
| paper8 | 28.52 (+1 tiny) | L820–824 | Prop 5.1(ii) long inline `K=\ee^{-O_2^2/4\tau^2}\ee^{-q_2^2/4\sigma^2}` line; reword/break |
| paper4 | none ✓ | — | fixed W14 (`\allowbreak` at `\texttt` underscores) |
| paper9 | none ✓ | — | |
| paper10 | none significant (4.8, 1.5) | — | |

## Fix recipes
- **Wide tables (p2, p6, likely p5/p7):** `\resizebox{\textwidth}{!}{\begin{tabular}…\end{tabular}}` (needs `\usepackage{graphicx}`), or `\footnotesize`+`\setlength{\tabcolsep}{3pt}`, or restructure/shorten headers.
- **Wide display equations (p1 L2248, p5, p7):** break with `\\`/`split`/`multline`/`gathered`, or reduce `\qquad`→`\quad`, or move trailing conditions to prose.
- **Long inline math / unbreakable words (p1 L425, p3 L235, p8 L820):** reword, or add `\allowbreak`/`\-` hyphenation hints.
- **`\texttt`/`\url` (already hit in p4):** `\allowbreak` at internal underscores (NOT after the slash — that break isn't taken), or load `xurl`.

After each fix: fresh `latexmk -g`, then `grep "Overfull" main.log` (unfiltered) → require ZERO >10pt. Recompile + BOTH gates + commit per paper.
