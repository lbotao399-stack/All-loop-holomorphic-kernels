# Perturbative quantum corrections and the quantum ring structure of the BPS sector

**Computing all-loop holomorphic Feynman diagrams in four dimensions by circuit reduction** — current reader snapshot of 4 November 2026 (revision 3788).

Botao Li (Peking University), GPT Astra, Claude Opus 5.5

The current manuscript is available as a [colored PDF](All_loop_holomorphic_kernels_full.pdf) and a [self-contained HTML export](reader/index.html) (download and open locally). Both preserve the reader’s red and blue text, yellow highlights, formulas, figures, and chapter order. The [editable snapshot](reader/document.json) preserves every block, stable ID, and formatting range.

## Abstract

We compute, at arbitrary loop order, the kernels of the holomorphic Feynman graphs that carry loop corrections to supersymmetry transformations and products. Building on the holomorphic graph integrals of Wang and the operatope of Budzik, Gaiotto, Kulp, Wu and Yu, we read the operatope current equations as those of an electrical network, with Schwinger times as resistances and holomorphic momenta as injected currents. Using inductive series, parallel and star–triangle reductions as changes of variables on Schwinger space, we compute every *n*-loop operatope graph of interest here, at arbitrary *n*: its rational Schwinger integrand becomes a polynomial on an explicit product of intervals and simplices, and every Taylor coefficient is a finite factorial sum. These kernels determine the loop-corrected anomalous supersymmetry transformation of composite operators and the quantum renormalized product that constructs the BPS ring. As an explicit application, we give every perturbative correction to the supersymmetry transformation in N=4 Yang–Mills theory, including its action on operators with arbitrary holomorphic derivatives; the one-loop correction is the operator of Budzik and Kulp. Using the marked higher operations of Gaiotto, Kulp and Wu, we also construct and compute the quantum product of **Q**-closed operators and prove that, up to **Q**-exact terms, it is associative, graded commutative and unital, supplying the multiplication of the quantum BPS ring. As a consequence of this ring structure, every multi-graviton operator lifts to a cocycle of the full quantum supercharge, with an explicit and finite all-order completion. We also construct closed all-order completions of several known fortuitous classes in N=4 Yang–Mills theory and confirm that they survive at every perturbative order.

## Contents

| File | |
|---|---|
| [`All_loop_holomorphic_kernels_full.pdf`](All_loop_holomorphic_kernels_full.pdf) | current color-preserving reader export |
| [`reader/index.html`](reader/index.html) | standalone manuscript with embedded fonts and figures; download and open in a browser |
| [`reader/document.json`](reader/document.json) | lossless editable snapshot, revision 3788, 3,627 blocks |
| [`reader/snapshot-manifest.json`](reader/snapshot-manifest.json) | snapshot metadata, validation results, and file hashes |
| `reader/figures/` | image assets referenced by the editable snapshot |
| `All_loop_holomorphic_kernels_full.tex` | original 21 October 2026 LaTeX source, retained unchanged; subsequent reader edits are in `reader/document.json` |
| `figures/` | the figures used by the source |
| `SQED_two_loop_repro.zip` | companion package for the two-loop lifting example in massive SQED (Section 9.1); Python 3, standard library only |

## Build the original LaTeX source

This command builds the original 21 October source. It does not reproduce the updated reader snapshot or its colored PDF.

```sh
latexmk -pdf All_loop_holomorphic_kernels_full.tex
```

The source compiles with TeX Live 2025.
