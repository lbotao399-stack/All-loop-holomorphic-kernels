# Kernels of the quantum product through seven loops

Data for the loop corrections of the quantum product `A ⋆ B` of local operators in the holomorphic twist of
four-dimensional N=1 gauge theories with cubic interactions, as defined in Sections 6 and 7 of the manuscript in
this repository (referred to as [LLC] below).

The supercharge corrections `Q_n` are given by fan graphs, whose kernels have a closed form at every loop order.
The product needs more graphs, the product forests, and their kernels are evaluated graph by graph. This folder
gives them through seven loops, for arbitrary derivatives on the letters.

## The formula

With `n` interaction vertices, the order-`ħ^n` term of the product is [LLC (6.26)]

    [ħ^n](A ⋆ B) = (1/n!) {I^{⊗n}, A, B}^{γ,0}
                 = (-1)^n / (n! (8π²)^n)  Σ_{labelled product forests Γ}  [ I_Γ^{raw cut}(λ; z) · Π_edges Δ_vw (I_1 ⋯ I_n A B) ]_jets
                 = (-1)^n / (8π²)^n  Σ_{forests F}  1/|Aut F|  Σ_{assignments}  M_F(jets; λ) · (ordered fibre contractions),

where

* a forest `F` is a set of full binary rooted trees whose internal vertices are the interactions and whose leaves
  sit on the inputs `A` or `B` (at most one leaf on each input per vertex); the root of every tree keeps one
  uncontracted letter, the surviving letter;
* an assignment sends distinct letters of `A` and of `B` to the external edges;
* `M_F(jets; λ) = Π_e (-1)^{r_e+s_e} r_e! s_e! × [Taylor coefficient of I_F^{raw cut} in the displacement of the edge e]`,
  with `(r_e, s_e)` the numbers of `∂_1, ∂_2` on the input letter contracted along the external edge `e`;
* `M_F` is a polynomial in the sources: `λ_root` becomes a derivative on the surviving letter of that tree,
  `λ_A` a derivative acting on the product of all uncontracted letters of `A`; the input `B` is the base point;
* the fibre contractions `Δ_vw` are applied in the lexicographic order of the edges, right to left, to the
  product `I_1 ⋯ I_n A B`.

## Trees

The kernel of a forest is assembled from data of its trees. Let the tree `τ_r` have `m_r` interaction vertices
(`n = Σ_r m_r`), series parameter `s_r` of its root and fraction `q_r` of the terminal simplex. The current on its
external edge `e` is

    y_e = a_e λ_r + q_r β_e T ,        T = λ_A + Σ_r (1 − s_r) λ_r ,

with `a_e`, `β_e` polynomials in the internal parameters of `τ_r` alone, and

    M_F = ∫ Π_r ds_r ∫ dμ(q)  Π_r [ ⟨λ_r, T⟩^{m_r}  Π_{e ∈ τ_r} y_{e,1}^{r_e} y_{e,2}^{s_e} ]_{τ_r} ,

    ∫ dμ(q) Π_r q_r^{c_r} = Π_r (m_r + c_r − 1)! / (n + Σ_r c_r + 1)! ,        ⟨u, v⟩ = u_1 v_2 − u_2 v_1 ,

where `[ … ]_τ` integrates the remaining internal parameters of the tree, with its density `ι_τ`, over a product
of standard simplices. A tree enters only through the polynomials in `s`

    W_τ(k, l)(s) = ∫ ι_τ  Π_e a_e^{k_e} β_e^{l_e} .

Numbers of trees with `m` vertices and of forests with `n` vertices:

| m, n | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| trees | 1 | 2 | 5 | 12 | 32 | 86 | 243 |
| forests | 1 | 3 | 8 | 23 | 65 | 194 | 576 |

## Tables

`tables/tree_charts_m<m>.json`, `m = 1, …, 7`: one record per tree, numbered `m.i`. They determine every moment of
every forest through seven loops.

| field | meaning |
|---|---|
| `tree` | e.g. `(A,(A,B))` |
| `edges` | ordered edges; vertices `1..m` are interactions (depth first), `A = m+1`, `B = m+2`; the auxiliary edge `(A,B)` is last |
| `external_edges` | edges ending on `A` or `B`, in the order used by `a`, `beta` and by the jets |
| `automorphisms` | `|Aut τ|` |
| `variables`, `s` | number of internal parameters `x_0, …, x_{2m−2}`; index of `s` (integrated over `[0,1]`) |
| `simplices` | the other parameters, grouped into standard simplices `{x_i ≥ 0, Σ x_i ≤ 1}` with Lebesgue measure |
| `density` | `ι_τ`, as a list of `[[exponents], "p/q"]` |
| `a`, `beta` | `a_e`, `β_e` for every external edge, same format |

`tables/product_kernels_n<n>.json.gz`, `n = 1, …, 7`: the assembled moments, one record per forest, numbered `n.i`.

| field | meaning |
|---|---|
| `forest` | the trees, e.g. `["(A,B)", "(A,(A,B))"]` |
| `edges` | ordered edges; vertices `1..n` are interactions, `A = n+1`, `B = n+2`; the auxiliary edge `(A,B)` is last |
| `roots` | the vertices carrying the surviving letters |
| `automorphisms` | `|Aut F|` with `A`, `B` fixed |
| `external_edges` | edges ending on `A` or `B`, in the order used by `jets` |
| `sources` | `λ` of every root, then `λ_A` |
| `moments` | list of `{jets, terms}`: `jets[k] = [r, s]` on external edge `k`; `terms = [[exponents], "p/q"]` with exponents of `(λ_root1,1, λ_root1,2, …, λ_A,1, λ_A,2)` |

Only nonzero moments are listed. Maximal total jet order per loop order (`code/product_kernels.py` gives any
other moment):

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| total jet order ≤ | 6 | 4 | 3 | 2 | 1 | 0 | 0 |
| monomials | 3 210 | 71 317 | 531 814 | 1 237 843 | 1 043 554 | 284 385 | 2 684 774 |

## Code

Python 3, standard library only.

* `code/product_kernels.py` — enumeration of trees and forests, the integrals `W_τ(k, l)`, and the moment of any
  forest for any jets from the tree charts:

  ```python
  import product_kernels as PK
  f = PK.forests(2)[0]                      # (A,B), (A,B)
  PK.forest_moment(f, ((0, 0),) * 4)        # {((x_1, y_1), (x_2, y_2), (x_A, y_A)): Fraction}
  ```

* `code/gen_tables.py n J` — writes `tables/product_kernels_n<n>.json.gz`.
* `code/check.py` — the checks of the tables listed below.

## Checks

* Every tree chart agrees with the Laplacian form of the integrand (edge currents, heat-cut minor and Jacobian
  of the change of variables) at a rational point.
* The moments assembled from the trees agree with the reduction of the whole forest as one graph: all forests
  with `n = 1, 2, 3` and total jet order up to 6, 4, 3 (210, 915 and 1852 jet assignments), and all 23 forests
  with `n = 4` at jet order zero.
* Closed forms (`code/check.py`): at one loop `M = ½⟨λ_1, λ_A⟩`; at two loops [LLC (6.30)]

      (A,B)(A,B):  (1/24) ⟨λ_1, λ_2 + 2λ_A⟩ ⟨λ_2, λ_1 + 2λ_A⟩ ,     (A,(A,B)):  −(1/24) ⟨λ_1, λ_A⟩² ,     (B,(A,B)):  +(1/24) ⟨λ_1, λ_A⟩² .

* Every tabulated moment has the grading `Σ (exponents of the first components) = n + Σ_e r_e` and changes by
  `(−1)^n` when the two components are exchanged (`code/check.py`).
* Leibniz rule [LLC (6.13)]. With these kernels, the order-`ħ^n` part of
  `Q(A ⋆ B) − (QA) ⋆ B − (−1)^{|A|} A ⋆ (QB)`, `Q = Q_0 + Q_1 + Q_2 + …`, vanishes identically on random pairs of
  words of the full letter algebra (component engine of the lifting tests, exact arithmetic modulo `2^31 − 1`;
  "jets ≤ k": up to `k` derivatives on every letter):

  | n | theory | pairs of words |
  |---|---|---|
  | 1 | N=4 SU(2) (letters b, c, β, γ) | 110, jets ≤ 2 |
  | 2 | SU(2) | 275 with jets ≤ 1, 46 with jets ≤ 2, 10 with jets ≤ 3 |
  | 2 | SU(3) | 190, jets ≤ 2 |
  | 2 | N=4 SU(2) (letters b, c, β, γ) | 140 |
  | 3 | SU(2) | 126 with jets 0, 46 with jets ≤ 1 |
  | 3 | SU(3) | 38 |
  | 4 | SU(2) | 68, words of up to 4 + 4 letters |
