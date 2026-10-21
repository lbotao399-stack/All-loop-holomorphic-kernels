# Perturbative quantum corrections and the quantum ring structure of the BPS sector

**Computing all-loop holomorphic Feynman diagrams in four dimensions by circuit reduction** — full version (draft of 21 October 2026).

Botao Li, Peking University

## Abstract

We compute, at arbitrary loop order, the kernels of the holomorphic Feynman graphs that carry loop corrections to supersymmetry transformations and products. Building on the holomorphic graph integrals of Wang and the operatope of Budzik, Gaiotto, Kulp, Wu and Yu, we read the operatope current equations as those of an electrical network, with Schwinger times as resistances and holomorphic momenta as injected currents. Using inductive series, parallel and star–triangle reductions as changes of variables on Schwinger space, we compute every *n*-loop operatope graph of interest here, at arbitrary *n*: its rational Schwinger integrand becomes a polynomial on an explicit product of intervals and simplices, and every Taylor coefficient is a finite factorial sum. These kernels determine the loop-corrected anomalous supersymmetry transformation of composite operators and the quantum renormalized product that constructs the BPS ring. As an explicit application, we give every perturbative correction to the supersymmetry transformation in N=4 Yang–Mills theory, including its action on operators with arbitrary holomorphic derivatives; the one-loop correction is the operator of Budzik and Kulp. Using the marked higher operations of Gaiotto, Kulp and Wu, we also construct and compute the quantum product of **Q**-closed operators and prove that, up to **Q**-exact terms, it is associative, graded commutative and unital, supplying the multiplication of the quantum BPS ring. As a consequence of this ring structure, every multi-graviton operator lifts to a cocycle of the full quantum supercharge, with an explicit and finite all-order completion. We also construct closed all-order completions of several known fortuitous classes in N=4 Yang–Mills theory and confirm that they survive at every perturbative order.

## Contents

| File | |
|---|---|
| [`All_loop_holomorphic_kernels_full.pdf`](All_loop_holomorphic_kernels_full.pdf) | the paper (165 pages) |
| `All_loop_holomorphic_kernels_full.tex` | LaTeX source, a single file with the bibliography included |
| `figures/` | the figures used by the source |
| `SQED_two_loop_repro.zip` | companion package for the two-loop lifting example in massive SQED (Section 9.1); Python 3, standard library only |

## Build

```sh
latexmk -pdf All_loop_holomorphic_kernels_full.tex
```

The source compiles with TeX Live 2025.
