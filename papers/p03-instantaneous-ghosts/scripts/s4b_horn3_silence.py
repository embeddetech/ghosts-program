"""
S4b -- horn-3 silence: the decision matrix's column discriminant,
demonstrated in the exact toy where horn 1 is exactly solvable.

One classical quadratic model: two modes, frequencies w1 = w2 = w
(resonance), bilinear coupling of strength g, mode 2 carrying the
indefinite sign. Three quantizations of the SAME mode content and
coupling strength:

  GHOST (horn 1, the beables reading):
      H = w(a+a - b+b) + g(a+b+ + ab)
      -> the vacuum decays: <n1(t)> = sinh^2(gt) exactly
      (paper 1's cascade; the observable "decay signal").
  REQUANTIZED (horn 3, the Bender-Mannheim sign reassignment, which
  at quadratic level converts pair creation into excitation
  exchange):
      H = w(a+a + b+b) + g(a+b + ab+)
      -> the vacuum is an exact eigenstate: <n1(t)> = 0 identically.
      SILENCE. The positive-spectrum quantization has nothing to
      decay into.
  NORMAL TWIN (control: same pair-creation coupling, healthy signs):
      H = w(a+a + b+b) + g(a+b+ + ab)
      -> bounded virtual-pair occupation ~ (g/2w)^2, no secular
      growth (paper 1's normal twin).

Observable dichotomy for the decision matrix: given the ghost
(phantom field established), horn 1 predicts a secular decay signal,
horn 3 predicts exactly none -- so an exhaustive null in the signal
search discriminates AGAINST definite configurations, not merely
against sensitivity.

Second panel: stimulated version from an excited initial state
|2,0>, showing the dichotomy is not special to the vacuum.

Run:  python scripts/s4b_horn3_silence.py     (~1 minute)
"""

import numpy as np

NF, W, G = 55, 1.0, 0.15


def ops(N):
    a = np.diag(np.sqrt(np.arange(1, N)), 1)
    return a, a.conj().T


def two_mode(N):
    a1, ad1 = ops(N)
    I = np.eye(N)
    A = np.kron(a1, I)
    B = np.kron(I, a1)
    return A, A.conj().T, B, B.conj().T


A, Ad, B, Bd = two_mode(NF)
N1 = Ad @ A
N2 = Bd @ B

H_ghost = W * (N1 - N2) + G * (Ad @ Bd + A @ B)
H_horn3 = W * (N1 + N2) + G * (Ad @ B + A @ Bd)
H_twin = W * (N1 + N2) + G * (Ad @ Bd + A @ B)


def evolve_n1(H, psi0, times):
    w, V = np.linalg.eigh(H)
    c = V.conj().T @ psi0
    out = []
    for t in times:
        psi = V @ (np.exp(-1j * w * t) * c)
        out.append(float(np.real(psi.conj() @ (N1 @ psi))))
    return np.array(out)


vac = np.zeros(NF * NF)
vac[0] = 1.0
exc = np.zeros(NF * NF)
exc[2 * NF] = 1.0                      # |2,0>

times = np.array([0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0])

n_ghost = evolve_n1(H_ghost, vac, times)
n_horn3 = evolve_n1(H_horn3, vac, times)
n_twin = evolve_n1(H_twin, vac, times)

print("=" * 72)
print("S4b: one classical model, three quantizations -- the vacuum's")
print(f"     fate (resonant, g={G}, w={W}, Fock cutoff {NF}/mode)")
print("=" * 72)
print(f"{'t':>5} {'ghost <n1>':>11} {'sinh^2(gt)':>11} "
      f"{'horn-3 <n1>':>12} {'twin <n1>':>10}")
for i, t in enumerate(times):
    print(f"{t:>5.1f} {n_ghost[i]:>11.5f} {np.sinh(G*t)**2:>11.5f} "
          f"{n_horn3[i]:>12.2e} {n_twin[i]:>10.6f}")
dev = np.max(np.abs(n_ghost - np.sinh(G * times) ** 2))
print(f"\nghost vs exact law, max deviation: {dev:.2e} "
      f"(truncation-limited)")
print(f"horn-3 maximum over all t:        {np.max(n_horn3):.2e} "
      f"(exact silence: vacuum is an eigenstate)")
print(f"twin maximum over all t:          {np.max(n_twin):.6f} "
      f"(bounded virtual pairs ~ (g/2w)^2 = {(G/(2*W))**2:.6f})")

# stimulated panel
n_g2 = evolve_n1(H_ghost, exc, times)
n_h2 = evolve_n1(H_horn3, exc, times)
print("\nstimulated panel, initial |2,0>:")
print(f"{'t':>5} {'ghost <n1>':>11} {'horn-3 <n1>':>12}")
for i, t in enumerate(times):
    print(f"{t:>5.1f} {n_g2[i]:>11.4f} {n_h2[i]:>12.4f}")
print("=> ghost: secular growth (stimulated cascade); horn-3: bounded")
print("   Rabi exchange between the modes, mean pinned at the initial")
print("   excitation. Same modes, same coupling strength, opposite")
print("   energy-sign assignment: a decay signal exists in exactly one.")
print("done.")
