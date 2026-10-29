# T4: Vertex/Propagator Conventions for Vacuum-Decay Rate in Pure Conformal (Weyl) Gravity
Data-gathering sheet. All quotes verbatim from cited arXiv sources (fetched 2026-07-11).
ASCII throughout: a_g = alpha_g, C^2 = C_lmnk C^lmnk, box = d_a d^a.

================================================================================
1. ACTION NORMALIZATION (Mannheim)
================================================================================
Source: Mannheim, "Making the Case for Conformal Gravity", arXiv:1101.2186
(Found. Phys. 42, 388 (2012)), Eq. (9):

    I_W = -alpha_g Integral d^4x (-g)^{1/2} C_{lmnk} C^{lmnk}
        = -2 alpha_g Integral d^4x (-g)^{1/2} [ R_{mn} R^{mn} - (1/3)(R^a_a)^2 ]

(the second form uses the Gauss-Bonnet total derivative). Verbatim:
  "the conformal gravity action I_W = -alpha_g int d^4x (-g)^{1/2}
   C_{lambda mu nu kappa} C^{lambda mu nu kappa}"
  "Because the coupling constant alpha_g is dimensionless, the conformal
   theory is power-counting renormalizable."

Field equation, 1101.2186 Eq. (11):

    -4 alpha_g W^{mu nu} + T_M^{mu nu} = 0     i.e.   4 a_g W_mn = T^M_mn

W_mn = Bach tensor. Same convention in the Phys.Rept. review astro-ph/0505266
and in Mannheim-O'Brien fitting papers.

SIGN of a_g (only in-print sign statement found):
Mannheim, Comment on Yoon, arXiv:1506.02479 (PRD 93, 068501 (2016)),
footnote 18, verbatim:
  "Yoon asserts without proof that the sign of the coupling constant alpha_g
   is positive. However, in P. D. Mannheim, Gen. Rel. Gravit. 43, 703 (2011)
   [arXiv:0909.0212] it was found that it is a negative sign for alpha_g that
   leads to a positive sign for the zero-point energy of the bosonic
   gravitational field, just as is needed to cancel the negative zero-point
   energy density of the fermion field."

Note: Flanagan (astro-ph/0605504) writes the same "-alpha_g C_{abcd}C^{abcd}"
Lagrangian but in MTW (+,+,+) conventions, "differing from Mannheim's
conventions (footnote 1)". Watch signature-dependent signs when mixing.

================================================================================
2. GRAVITON PROPAGATOR AROUND FLAT SPACE
================================================================================
Linearization (1101.2186): with g_mn = eta_mn + h_mn and K_mn the
traceless (TT after gauge fixing) part,

  Eq. (21):  W^{mu nu}(1) = (1/2)(d_a d^a)^2 K^{mu nu}
  Eq. (22):  I_W(2) = -(alpha_g/2) Integral d^4x (box K_mn)(box K^mn)

Combining Eq. (11) + Eq. (21):

    -4 a_g * (1/2) box^2 K^mn + T^mn_(TT) = 0
    =>  box^2 K^mn = T^mn_(TT) / (2 a_g)
    =>  momentum space:  K^mn(k) = T^mn_(TT)(k) / (2 a_g k^4)

So the WORKING PROPAGATOR (Mannheim normalization, TT sector):

    D^{mn,rs}(k) = P2^{mn,rs} / (2 alpha_g k^4)         [tensor structure]

where P2 is the transverse-traceless spin-2 projector. No spin-0 pole: the
trace part of h_mn is pure gauge under conformal (Weyl) transformations, so
only the spin-2 (and, per Riegert, a spin-1 partner) sector propagates.
No source I found writes the full projector decomposition explicitly for
pure Weyl gravity in Mannheim's papers; the TT-sector coefficient
1/(2 a_g k^4) above follows directly from Eqs. (9),(11),(21),(22).
(Stelle-style quadratic-gravity literature gives the P2 structure; pure-Weyl
d.o.f. counting from Riegert, below.)

Verbatim (1101.2186, Sec. 5): "D(k) = 1/k^4" for the pure fourth-order
theory, "with poles on the real axis."

DOUBLE-POLE / DIPOLE STRUCTURE. The k^-4 is the degenerate limit of two
second-order poles with opposite-sign residues. 1101.2186 Eq. (25) (also
Mannheim arXiv:2004.00376 Eq. (2.6), Pauli-Villars form):

    D(k, M1, M2) = 1 / [(k^2 + M1^2)(k^2 + M2^2)]
                 = [1/(M2^2 - M1^2)] [ 1/(k^2 + M1^2) - 1/(k^2 + M2^2) ]

Verbatim (1101.2186): "Because of the relative minus sign in (25), one finds
that some of the poles have the negative residues that occur in an indefinite
metric Hilbert space."
Verbatim (equal-mass limit; 1101.2186 / 2004.00376): "the limit is singular.
In consequence, the limit is a quite unusual one in which the Hamiltonian
becomes a non-diagonalizable, Jordan-block Hamiltonian"; "Thus at the
transition point we lose an eigenfunction and the Hamiltonian becomes of
non-diagonalizable, Jordan-block form"; "the propagator becoming
1/(E^2 - omega^2)^2". The would-be ghost states become the ZERO-NORM
Jordan/dipole partners of the graviton in the M1 -> M2 limit.

Particle content (Riegert, Phys. Lett. A 105, 110 (1984), no arXiv;
as summarized in Hell-Lust-Zoupanos arXiv:2306.13714 / JHEP 08 (2023) 168):
six propagating d.o.f. for plane waves of linearized conformal gravity:
a massless ordinary spin-2 state, a massless ordinary spin-1 state, and a
massless spin-2 GHOST state (the dipole partner).
Hell-Lust-Zoupanos abstract, verbatim: "We study the metric perturbations
around the de Sitter and Minkowski backgrounds in Conformal Gravity. We
confirm the presence of ghosts in both cases." (Ghost removable only by
imposing extra Maldacena-type boundary conditions; see Sec. 6.)

================================================================================
3. MATTER COUPLING AND TREE-LEVEL EXCHANGE
================================================================================
Matter couples through the metric exactly as in GR: I_int = (1/2) Int h_mn T^mn
at linear order; the source equation is 4 a_g W_mn = T^M_mn (1101.2186 Eq. 11).
Confirmations from the fourth-order Newtonian-limit literature:

(a) Flanagan, "Fourth Order Weyl Gravity", arXiv:astro-ph/0605504
    (PRD 74, 023002 (2006)), Eq. (10) (weak field, with a scalar sector of
    mass parameter m_p):
        8 alpha_g grad^2 grad^2 Phibar - 2 m_p^2 grad^2 Phibar = rho
    Pure-Weyl limit (m_p -> 0): grad^4 Phibar = rho / (8 a_g).

(b) Yoon, arXiv:1305.0163 (PRD 88, 027504 (2013)), Eqs. (14)-(15):
        grad^4 phi(r) = h(r)
        phi(r) = -(1/8pi) Integral d^3r' h(r') |r - r'|
    i.e. the 1/k^4 Green's function IS the linear potential:
        FT[1/k^4](r) = -r/(8 pi).

(c) Mannheim, arXiv:1506.02479, exterior-solution machinery (verbatim):
        grad^4 B(r) = 3 (T^0_0 - T^r_r) / (4 alpha_g B(r)) = f(r)
        2 beta = (1/6) Int_0^R dr' f(r') r'^4
        gamma  = -(1/2) Int_0^R dr' f(r') r'^2
    with metric B(r > r0) = w - 2 beta/r + gamma r - kappa r^2  (w=(1-6 beta gamma)^{1/2}).

EFFECTIVE MATTER-MATTER EXCHANGE (adopted form):

    M(k) ~ (1/2) T1^{mn} [ P2_{mn,rs} / (2 alpha_g k^4) ] (1/2) T2^{rs}
    => static potential between masses m1, m2 (natural units):
       V(r) = + m1 m2 r / (16 pi alpha_g) x O(1)    [FT of 1/k^4 = -r/8pi]

O(1) = tensor-contraction factor from P2 acting on (m u_m u_n) sources;
sign convention tied to sign(a_g) and signature (see Flanagan sign flip, Sec.5).

================================================================================
4. NUMERICAL PARAMETERS AND alpha_g
================================================================================
Fitted values, Mannheim & O'Brien, arXiv:1011.3495 (PRD 85, 124020 (2012));
also PRL 106, 121101 (2011); 111-galaxy + dwarf samples. Verbatim:

    v^2_tot -> N* beta* c^2 / R + N* gamma* c^2 R / 2 + gamma_0 c^2 R / 2
               - kappa c^2 R^2
    "beta* being given by the familiar M_sun G / c^2 = 1.48 x 10^5 cm"
    "gamma* = 5.42 x 10^-41 cm^-1"   (linear potential PER SOLAR MASS)
    "gamma_0 = 3.06 x 10^-30 cm^-1"  (cosmological, mass-independent)
    "kappa  = 9.54 x 10^-54 cm^-2, ~ (100 Mpc)^-2"

IN-PRINT alpha_g VALUE: NONE FOUND. Searched 1101.2186 (full), 1011.3495,
astro-ph/0505266, 1506.02479, 2004.00376, plus web sweeps for numerical
statements. Only in-print constraints: (i) dimensionless; (ii) NEGATIVE sign
(1506.02479 fn. 18, quoting Gen.Rel.Grav. 43, 703). Mannheim deliberately
never converts gamma* to alpha_g, because in his framework the microscopic
source integrals int f r'^2 dr' involve the symmetry-breaking scalar S(x)
and cannot be evaluated as bare point-particle T_mn (his anti-Yoon argument).

DERIVED ESTIMATE (ours, flagged as such). If one takes the flat-space
h T/2 coupling and D = 1/(2 a_g k^4) at face value and matches the measured
per-solar-mass slope gamma*:
  Tree exchange: V(r)/m2 = gamma* c^2 r / 2 per solar mass
  => |alpha_g| ~ M_sun / (8 pi gamma*)   [natural units, M_sun = 5.65e70 cm^-1]
              ~ 4.15e109
  Cross-check via Mannheim's own gamma = -(1/2) Int f r^2 dr with a nucleon
  source (Int dr r^2 T^0_0 = m_p/4pi, m_p = 4.75e13 cm^-1,
  gamma_p = gamma* m_p/M_sun = 4.6e-98 cm^-1):
  => |alpha_g| ~ 3 M_sun/(32 pi gamma*) ~ 3.1e109.
  Both routes agree: |alpha_g| ~ 3-4 x 10^109.
RECOMMENDED RANGE for rate estimates: |a_g| = 1e108 - 1e111 (central 3e109),
sign negative per Mannheim, with the caveat that Mannheim himself would
reject this inversion (Sec. 5) - state it as "naive flat-space matching".

================================================================================
5. CRITIQUES OF THE COUPLING / LIMIT STRUCTURE
================================================================================
(a) Flanagan, astro-ph/0605504. Verbatim: "the theory does not reproduce
Solar System observations in the limit of weak fields and slow motions,
which rules out the theory"; "the conformal invariance is not a fundamental
property of the theory, and instead is an artifact of the choice of
variables." In the physical (Einstein-frame) variables matter couples
standardly and: Regime 1: "Newton's law of gravitation is recovered but with
the sign flipped. The resulting repulsive gravitational force disagrees with
observations." Regime 2: Eddington "gamma = -1 + O(L^2 m_p^2 / alpha_g)"
(Eq. 17), vs. observed gamma ~ +1.

(b) Yoon, arXiv:1305.0163. Verbatim: Mannheim's program "does not reduce to
Newtonian gravity at short distances, unless one assumes undesirable
singularities of the mass density of the proton"; "unlike in the Newtonian
case ... the gravitational attraction depends not only on the total mass,
but also on the mass distribution"; and the sign problem: "the last term of
Eq. (16) yields the negative linear gravitational potential. However, we know
that we want the positive linear gravitational potential to fit the galaxy
rotation curve."

(c) Mannheim reply, arXiv:1506.02479. Verbatim: "Yoon's results only hold
because of the assumption that gravitational sources can be treated the same
way that they are treated in standard Newton-Einstein gravity. Since such an
assumption violates the theory's underlying conformal invariance, Yoon's
conclusions are invalidated." On the vacuum/background: "In a theory with an
underlying conformal symmetry, at the level of the Lagrangian all particles
will be massless and thus propagate as unlocalized massless plane waves that
fill all space. In order to give particles mass one breaks the symmetry
spontaneously by giving a Higgs-type scalar field S(x) a constant vacuum
expectation value S_0." And: "To get the particles to localize into some
finite region of space, one needs S(x) to acquire a spatial dependence in
order to produce a potential well."
IMPLICATION FOR US: Mannheim's own position is that naive flat-Minkowski
perturbation theory with point sources is NOT the right setting; the vacuum
is Minkowski + broken conformal symmetry (constant S_0), and localized
sources drag S(x) with them. Any rate computed in naive flat-space
perturbation theory should be labeled as testing the "face-value" theory,
i.e. the same theory Flanagan/Yoon analyze.

(d) Also relevant: "Conformal Gravity Redux: Ghost-turned-Tachyon"
(arXiv:1403.4664) - the flat-background ghost becomes tachyonic on other
backgrounds; and Hell-Lust-Zoupanos arXiv:2306.13714 (ghosts confirmed on
Minkowski and dS; only non-generic boundary conditions remove them).

================================================================================
6. EXISTING PARTICLE-PRODUCTION / VACUUM-DECAY COMPUTATIONS
================================================================================
(a) Cline, Jeon & Moore, "The phantom menaced: constraints on low-energy
effective ghosts", arXiv:hep-ph/0311312 (PRD 70, 043543 (2004)). THE template
computation: gravity-mediated vacuum decay with ghosts in the spectrum.
Verbatim: "a ghost pair and photon pair are spontaneously created from the
vacuum"; rate "on dimensional grounds, Gamma_{0 -> 2 gamma 2 phi} ~
Lambda^8 / M_p^4"; "The phase space integral is divergent, indicating a
catastrophic instability"; "The divergent nature of the instability can only
be avoided if we impose a Lorentz noninvariant momentum space cutoff on the
final state phase space." Bound: "Lambda <~ 3 MeV" from EGRET diffuse
gamma-ray background ("Demanding that (6) not exceed (7) gives the upper
limit Lambda <~ 3 MeV").
ADAPTATION NOTE [CORRECTED same-day; the original Lambda^8/a_g^2 guess
here was superseded by the contact-rung result -- see t4_rate_ladder.py
and paper 4 Sec. 5]: in pure Weyl gravity the mediator itself is the
1/(a_g k^4) graviton; the 1/k^4 propagator softens the CJM amplitude by
an extra 1/s, making |M|^2 ~ 1/a_g^2 s-FLAT (contact rung), so the rate
is Gamma/V ~ c_ps Lambda^4 / a_g^2 (Lambda = Lorentz-violating cutoff).
Dimensional check: a rate density is energy^4; with a_g dimensionless,
Lambda^8/a_g^2 would be energy^8 and cannot be a rate/volume.

(b) Maldacena, "Einstein Gravity from Conformal Gravity", arXiv:1105.5632.
"four dimensional conformal gravity plus a simple Neumann boundary condition"
reproduces Einstein gravity: the boundary condition "selects the Einstein
solution out of the more numerous solutions of conformal gravity" and
thereby projects out the ghost/dipole modes. If such boundary conditions are
imposed, the decay channel closes by fiat; absent them (generic conformal
gravity), the ghost sector is live (2306.13714 shows Neumann alone is not
sufficient on Minkowski: "the Neumann boundary condition does not lead to a
general solution in Minkowski space").

(c) Bender & Mannheim, no-ghost theorem for the Pais-Uhlenbeck oscillator,
arXiv:0706.0207 (PRL 100, 110402 (2008)); Mannheim hep-th/0608154,
arXiv:2004.00376. In PT/antilinear quantization the equal-frequency
(Jordan-block) theory has NO negative-norm and NO negative-energy states:
"one must use inner products built out of states and their conjugates with
respect to the antilinear symmetry, and these latter inner products are
positive"; "if one were to obtain a negative Dirac norm in a calculation
that would not necessarily mean that the theory was not unitary."
=> In Mannheim's quantization the Cline-Jeon-Moore channel is CLOSED
(no negative-energy final states, dipole partners are zero-norm); in
conventional Dirac-norm quantization it is OPEN and catastrophic.
This dichotomy is the crux for any rate estimate.

(d) Peripheral: 't Hooft's conformal-gravity program (arXiv:1009.0669,
1104.4543) treats the conformal factor as the dominant quantum variable; no
explicit 1/k^4-mediated pair-production rate found there. Recent stability
literature (e.g. "Foundations of ghost stability", arXiv:2408.16832;
Donoghue-Menezes line of work) argues vacuum decay may be avoided/slowed if
ghost couplings are nonlocal or if the ghost is unstable - cite as context.

================================================================================
7. RECOMMENDED CONVENTIONS FOR THE RATE CALCULATION
================================================================================
1. Action: I_W = -a_g Int d^4x sqrt(-g) C^2, field eq. 4 a_g W_mn = T_mn
   (Mannheim 1101.2186 Eqs. 9, 11). Mannheim signature (-,+,+,+) as in his
   papers; convert Flanagan quotes (MTW) explicitly if used.
2. Propagator: D^{mn,rs}(k) = P2^{mn,rs}/(2 a_g k^4), regulated as the
   M2 -> M1 limit of Eq. (25) two-pole form when norms/residues matter.
   Treat the dipole partner per quantization scheme chosen (Dirac vs PT).
3. Vertex: standard (1/2) h_mn T^mn.
4. Coupling value: |a_g| ~ 3e109 (range 1e108-1e111) from naive matching to
   gamma* = 5.42e-41 cm^-1 per M_sun; sign negative (Mannheim). Present the
   rate as a function of a_g with this band highlighted, and state explicitly
   that Mannheim's own framework rejects the naive matching while Flanagan/
   Yoon reject the limit structure entirely - the rate estimate therefore
   applies to "face-value flat-space conformal gravity".
5. Rate template [CORRECTED same-day, matching t4_rate_ladder.py and
   paper 4 Sec. 5]: Cline-Jeon-Moore Gamma ~ Lambda^8/M_p^4 -> here the
   1/(a_g k^4) propagator makes |M|^2 ~ 1/a_g^2 s-flat, i.e. the CONTACT
   rung: Gamma/V ~ c_ps * Lambda^4 / a_g^2 (the original Lambda^8/a_g^2
   template written here was a dimensional slip, energy^8 for an
   energy^4 quantity);
   note the Lorentz-invariant rate is divergent (needs cutoff Lambda), and
   that PT quantization (Bender-Mannheim) or Maldacena boundary conditions
   would set the rate to zero.

SOURCES (arXiv IDs): 1101.2186; astro-ph/0505266; 1011.3495; 1305.0163;
1506.02479; astro-ph/0605504; hep-ph/0311312; 1105.5632; 0706.0207;
hep-th/0608154; 2004.00376; 2306.13714; 1403.4664; 0909.0212 (sign of a_g);
Riegert, Phys. Lett. A 105, 110 (1984).
