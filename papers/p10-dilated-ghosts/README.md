# A boundary only by the clock

*the black-hole horizon between natural and exit, the membrane paradigm as the minimal semigroup, and the price of exterior unitarity*

![dilated-ghosts](dilated-ghosts.png)

<sub>*Banner image: prompt written by Claude (Anthropic), rendered by ChatGPT (OpenAI).*</sub>

**Paper 10 of the [Indivisible Ghosts program](https://github.com/embeddetech/ghosts-program).** Jonathan Torkelson (2026).

**[Read the paper (PDF)](dilated-ghosts-paper.pdf)** · LaTeX source in [`paper/`](paper/)

> **Status: working draft.** This manuscript is under the program's release-gate audit and is still being revised. It has not been peer reviewed. Read it accordingly; corrections land here as they are made.

## Abstract

**Draft — not for circulation.**

The first paper of this series priced incomplete dynamics in a single currency: for a half-line Schrödinger or diffusion problem, one classical time-of-flight integral simultaneously decides classical completeness, the Weyl limit-point/limit-circle alternative, and the Feller boundary type; conservative dynamics beyond the limit-point regime is a *choice* of self-adjoint extension (boundary data); and the choice-free, regulator-independent object is the minimal sub-stochastic semigroup. This paper runs that dictionary at a black-hole horizon, where it acquires an axis the non-relativistic theory did not have: the classification is *clock-dependent*. Three results, for a scalar field and its radial diffusion analogue on fixed Schwarzschild (with Rindler as warm-up). (i) *A clock-dependence theorem.* In Killing time the horizon is Weyl limit point and a Feller *natural* boundary: infinite time-of-flight, essentially self-adjoint generator, conservative minimal semigroup, no room for boundary data. In horizon-adapted clocks (Painlevé–Gullstrand, infalling proper, hyperboloidal) the time-of-flight is finite and the horizon generically becomes an *exit* boundary (unless the noise can climb an e-folding of the lapse; see below): the exterior generator is only dissipative (non-normal), its minimal semigroup is sub-stochastic, and the lost mass is exactly the flux through the horizon. The two pictures are related by a singular time change whose rate is set by the lapse, and Feller boundary type is not invariant under singular time changes. The stochastic half is proved here—with an exact identity equating Feller’s attainability integral to the clock’s ingoing time-of-flight—while the quantum half is assembled from known limit-point facts and the hyperboloidal-slicing program, cited rather than re-derived. A byproduct of the proof: the finer exit-versus-regular alternative is decided by the *outgoing* integral, and the boundary-data (limit-circle-like) regime opens only when the noise can climb an e-folding of the lapse—the stochastic twin of the near-horizon conformal-quantum-mechanics regime of the literature, and a feature of the isotropic clock idealization that the body argues does not survive a genuine (anisotropic) graph clock. (ii) *The membrane paradigm as the minimal process.* Stretched-horizon completions—brick-wall Dirichlet walls, near-horizon $`U(1)`$ extension families, antipodal S-matrix identifications—are conservative dilations carrying boundary data at a regularized wall; they are mutually equivalent for exterior scattering and thermality—rigorously for the $`U(1)`$ extension family, conjecturally in the multichannel (antipodal) case—but inequivalent for entropy counting, which is exactly the brick wall’s notorious cutoff dependence, read as extension dependence. The wall-independent object is the minimal sub-stochastic semigroup, and wall-removal universality (for local wall conditions) is the exit property (strictly, its interior $`\kappa p D<v_0`$). (iii) *A dictionary entry for the information paradox*—not a resolution. “Does the horizon need extra data?” has a clock-indexed answer: no in Killing time; in infalling time only if one insists on exterior conservativity, in which case the data parameterize inequivalent unitary completions. Firewall-type tensions, insofar as they demand a single clock-independent verdict on what the horizon carries, ask a question that—at the level of a test field’s boundary type—has no clock-independent answer: provably so for the radial diffusion analogue, and at the cited strength of the hyperboloidal program for the field itself.

## Reproducing the results

This paper ships no numerical scripts; its results are closed-form derivations and cited results (see the paper's provenance statement).

## Audit trail and provenance

This manuscript is an experiment in AI-conducted research: the work was carried out by large language models (Claude, Anthropic), directed and reviewed by the author. The paper's provenance statement says who did what. Nothing here should be taken on trust.

- The audit process: [`AUDIT.md`](AUDIT.md)
- Pass-by-pass audit ledger: [`histories/paper10-history.md`](histories/paper10-history.md)
- The full research notebook, the originating conversation, and every companion paper: the [program hub](https://github.com/embeddetech/ghosts-program)

## License

MIT — see [`LICENSE`](LICENSE).
