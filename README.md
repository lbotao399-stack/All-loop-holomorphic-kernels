Latest manuscript: 2026-11-24 15:28:23 (Beijing time) — version `20261124-152823`

# Holomorphic Feynman diagrams in four dimensions and the quantum BPS ring

Botao Li, Kangning Liu, Chi-Ming Chang

**[Holomorphic_Feynman_diagrams_quantum_BPS_ring.pdf](Holomorphic_Feynman_diagrams_quantum_BPS_ring.pdf)** (115 pages). LaTeX source: [`main.tex`](main.tex) with the figures in `figures/vec/`.

This repository keeps only the latest version of the manuscript; earlier versions are in the commit history. `VERSION.json` records the Beijing timestamp and file checksums.

Companion results repository (supplementary algorithm document, census tables, and exact rational lifting certificates): [`quantum-lifts-results`](https://github.com/lbotao399-stack/quantum-lifts-results).

This revision adds three-loop lifts in $SO(11)$, $SO(12)$ and $SO(13)$ in $\mathcal N=4$ Yang–Mills theory. It corrects citations and priority labels, including the attribution of Proposition D.1 to Brandt’s 1993 paper.

## Abstract

We compute at all loop orders the kernels of the holomorphic Feynman graphs governing loop corrections to supersymmetry transformations and regularized operator products in the holomorphic twist of four-dimensional $\mathcal N=1$ supersymmetric gauge theories. Interpreting their current equations as those of an electrical network—with Schwinger parameters as resistances and holomorphic momenta as injected currents—we iterate series, parallel and star–triangle reductions on Schwinger space to obtain the fan, spider and cubic product-forest kernels at all loop orders. Assuming that twisting commutes with quantization for composite operators, we obtain every perturbative correction to the supersymmetry transformation in $\mathcal N=4$ Yang–Mills theory, acting on operators with arbitrary holomorphic derivatives. Using the marked higher operations of Gaiotto, Kulp and Wu, we construct the quantum product and prove that on cohomology of the quantum supercharge it is associative, graded commutative and unital, furnishing the multiplication of the quantum BPS ring; in $\mathcal N=4$ Yang–Mills theory every multi-graviton operator thus admits an explicit finite all-order completion. For the classical gauge groups, every perturbative differential image in the multi-trace ring vanishes upon Cartan restriction. In $\mathcal N=4$ Yang–Mills theory, we find new fortuitous classes and one-loop lifts across several gauge groups, no two-loop lift in the sectors tested, and rationally certified three-loop lifts in $SO(11)$, $SO(12)$ and $SO(13)$. The lowest example we find lies in the level-$34$ BMN sector of $SO(13)$. The glueball lifts in $SO(11)$ and $SO(13)$ remove the excess classical powers relative to their symplectic duals. Beyond $\mathcal N=4$, we find two-loop lifts in the Leigh–Strassler and $\beta$-deformations, and two- to four-loop lifts in abelian and $\mathcal N=2$ gauge theories.

## Contents

| File | Description |
|---|---|
| [`Holomorphic_Feynman_diagrams_quantum_BPS_ring.pdf`](Holomorphic_Feynman_diagrams_quantum_BPS_ring.pdf) | The manuscript (version 20261124-152823; 115 pages) |
| [`main.tex`](main.tex), `figures/vec/` | LaTeX source of the manuscript and its vector figures |
| [`SQED_two_loop_repro.zip`](SQED_two_loop_repro.zip) | Standalone reproduction package for the two-loop lift in massive SQED (Section 2.3; Python 3, standard library only) |
| [`product_kernels/`](product_kernels/) | Kernels of the quantum product through seven loops (Sections 6 and 7): tree charts, moment tables and a reader (Python 3, standard library only) |

## Build

```sh
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

The source compiles cleanly with TeX Live 2025.
