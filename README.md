# Holomorphic Feynman diagrams in four dimensions and the quantum BPS ring

Botao Li, Kangning Liu, Chi-Ming Chang (November 2026)

Manuscript PDF: [`Holomorphic_Feynman_diagrams_quantum_BPS_ring.pdf`](Holomorphic_Feynman_diagrams_quantum_BPS_ring.pdf) (122 pages; also mirrored at [`All_loop_holomorphic_kernels_full.pdf`](All_loop_holomorphic_kernels_full.pdf) for backward link compatibility).

Companion results repository (supplementary algorithm document, census tables, and exact rational lifting certificates): [`quantum-lifts-results`](https://github.com/lbotao399-stack/quantum-lifts-results).

## Abstract

We compute, at arbitrary loop order, the kernels of the holomorphic Feynman graphs that carry the loop corrections to supersymmetry transformations and to regularized products of local operators in four-dimensional $\mathcal N=1$ supersymmetric gauge theories. Building on the holomorphic graph integrals of Wang and the operatope of Budzik, Gaiotto, Kulp, Wu and Yu, we read the operatope current equations as those of an electrical network, with Schwinger times as resistances and holomorphic momenta as injected currents. Series, parallel and star–triangle reductions, used as changes of variables on Schwinger space, reduce each graph step by step to one loop; iterating them gives the fan, spider and cubic product-forest kernels at arbitrary loop order, and extends the reduction scheme of earlier work while giving it a physical interpretation. These kernels determine the loop-corrected, anomalous supersymmetry transformation of composite operators and the renormalized quantum product that defines the BPS ring. As an explicit application, we give every perturbative correction to the supersymmetry transformation in $\mathcal N=4$ Yang–Mills theory, including its action on operators with arbitrary holomorphic derivatives. Using the marked higher operations of Gaiotto, Kulp and Wu, we also construct and compute the quantum product of operators and prove that, on $\mathbf Q$-cohomology, it is associative, graded commutative and unital, supplying the multiplication of the quantum BPS ring. As a consequence of this ring structure, every multi-graviton operator lifts to a cocycle of the full quantum supercharge, with an explicit and finite all-order completion. We also report a computer census of fortuitous classes and of their lifting: new fortuitous classes and one-loop lifts in $\mathcal N=4$ Yang–Mills theory with several gauge groups, where we have found no two-loop lift so far, two-loop lifts in the Leigh–Strassler and $\beta$-deformations of $\mathcal N=4$ Yang–Mills theory, two-, three- and four-loop lifts in abelian gauge theories, and two- and three-loop lifts in $\mathcal N=2$ $SU(2)$ and $SU(3)$ gauge theories and their singlet deformations.

## Contents

| File | Description |
|---|---|
| [`Holomorphic_Feynman_diagrams_quantum_BPS_ring.pdf`](Holomorphic_Feynman_diagrams_quantum_BPS_ring.pdf) | Compiled manuscript PDF (122 pages) |
| [`main.tex`](main.tex) | LaTeX source of the manuscript (mirrored at [`All_loop_holomorphic_kernels_full.tex`](All_loop_holomorphic_kernels_full.tex)) |
| `figures/vec/` | Vector PDF figures included by `main.tex` |
| [`SQED_two_loop_repro.zip`](SQED_two_loop_repro.zip) | Standalone reproduction package for the two-loop lifting example in massive SQED (Section 2.3; Python 3, standard library only) |
| [`product_kernels/`](product_kernels/) | Kernels of the quantum product through seven loops (Sections 6 and 7): tree charts, moment tables and a reader (Python 3, standard library only) |

## Build

```sh
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

The source compiles cleanly with TeX Live 2025.
