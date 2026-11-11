"""Kernels of the product forests from the tree charts (exact rational arithmetic, standard library only).

A product forest F is a set of trees tau_1, ..., tau_R.  The tree tau_r has m_r interaction vertices, m_r + 1
external edges ending on the inputs A or B, and one surviving letter at its root; n = m_1 + ... + m_R is the
loop order.  On the external edge e of tau_r the current is

        y_e = a_e lambda_r + q_r beta_e T ,          T = lambda_A + sum_r (1 - s_r) lambda_r ,

with a_e, beta_e polynomials in the internal parameters of tau_r alone, s_r one of them (the series parameter of
the root) and q_r the fraction of tau_r in the terminal simplex.  The moment with jets (o_e0, o_e1) on the
external edges is

  M_F = int prod_r ds_r  int dmu(q)  prod_r [ <lambda_r, T>^{m_r}  prod_{e in tau_r} y_{e,0}^{o_e0} y_{e,1}^{o_e1} ]_{tau_r} ,

  int dmu(q) prod_r q_r^{c_r} = prod_r (m_r + c_r - 1)! / (n + sum_r c_r + 1)! ,      <u, v> = u_0 v_1 - u_1 v_0 ,

where [ ... ]_tau integrates the remaining internal parameters of the tree with its density iota_tau over a
product of standard simplices.  All tree information enters through the polynomials in s

  W_tau(k, l)(s) = int iota_tau  prod_e a_e^{k_e} beta_e^{l_e} .

A chart record (tables/tree_charts_m<m>.json) lists iota, a_e, beta_e and the simplices of one tree.

    import product_kernels as PK
    f = PK.forests(2)[0]                       # ('A','B'), ('A','B')
    PK.forest_moment(f, ((0, 0),) * 4)         # {((x_1, y_1), (x_2, y_2), (x_A, y_A)): Fraction}
"""
import json, itertools, os
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, comb

HERE = os.path.dirname(os.path.abspath(__file__))
TABLES = os.environ.get('PRODUCT_KERNEL_TABLES') or next(
    (p for p in (os.path.join(HERE, 'tables'), os.path.join(HERE, '..', 'tables')) if os.path.isdir(p)),
    os.path.join(HERE, '..', 'tables'))

# ---------------------------------------------------------------------------------------------------------
# enumeration: full binary rooted trees whose leaves carry A or B (not both children equal leaves)


def _canonical(a, b): return tuple(sorted((a, b), key=repr))


@lru_cache(None)
def trees(n):
    if n == 0: return ()
    out = set()
    if n == 1: out.add(('A', 'B'))
    for t in trees(n - 1):
        out.add(_canonical('A', t)); out.add(_canonical('B', t))
    for i in range(1, n - 1):
        j = n - 1 - i
        if i > j: continue
        for a in trees(i):
            for b in trees(j): out.add(_canonical(a, b))
    return tuple(sorted(out, key=repr))


def size(t): return 0 if isinstance(t, str) else 1 + sum(size(s) for s in t)


def key(t): return t if isinstance(t, str) else '(' + ','.join(map(key, t)) + ')'


def edges_of(f):
    """edges of the forest f (interactions 1..n in depth-first order, A = n+1, B = n+2; the auxiliary edge
    (A, B) is last) and the roots of its trees"""
    n = sum(map(size, f)); A, B = n + 1, n + 2
    nxt = [0]; edges = []; roots = []

    def visit(t, parent=None):
        nxt[0] += 1; v = nxt[0]
        if parent is None: roots.append(v)
        else: edges.append((parent, v))
        for child in t:
            if isinstance(child, str): edges.append((v, A if child == 'A' else B))
            else: visit(child, v)
    for t in f: visit(t)
    return sorted(edges) + [(A, B)], roots


@lru_cache(None)
def forests(n):
    all_trees = tuple(t for k in range(1, n + 1) for t in trees(k))
    out = []

    def rec(rem, start, parts):
        if rem == 0: out.append(tuple(sorted(parts, key=repr))); return
        for i in range(start, len(all_trees)):
            t = all_trees[i]; k = size(t)
            if k > rem: continue
            rec(rem - k, i, parts + (t,))
    rec(n, 0, ())
    return tuple(sorted(set(out), key=repr))


def aut_tree(t):
    return 1 if isinstance(t, str) else aut_tree(t[0]) * aut_tree(t[1]) * (2 if t[0] == t[1] else 1)


def aut_forest(f):
    out = 1
    for t, m in Counter(f).items(): out *= aut_tree(t) ** m * factorial(m)
    return out


# ---------------------------------------------------------------------------------------------------------
# tree charts

BITS = 8
MASK = (1 << BITS) - 1


def _pack(ex):
    k = 0
    for i, e in enumerate(ex): k |= e << (BITS * i)
    return k


def _poly(terms):
    out = {}
    for ex, c in terms:
        c = F(c)
        out[_pack(ex)] = c.numerator if c.denominator == 1 else c
    return out


def _pmul(p, q):
    if len(p) < len(q): p, q = q, p
    out = {}
    for kb, cb in q.items():
        for ka, ca in p.items():
            k = ka + kb
            out[k] = out.get(k, 0) + ca * cb
    return out


class Tree:
    """One tree chart and its integrals W(k, l)."""

    def __init__(self, rec):
        self.rec = rec
        self.m = rec['vertices']
        self.nv = rec['variables']
        self.spos = rec['s']
        self.blocks = [tuple(b) for b in rec['simplices']]
        self.ext_edges = [tuple(e) for e in rec['external_edges']]
        self.iota = _poly(rec['density'])
        self.a = [_poly(p) for p in rec['a']]
        self.beta = [_poly(p) for p in rec['beta']]
        self._pw, self._W, self._split = {}, {}, {}

    def pw(self, kind, idx, k):
        kk = (kind, idx, k)
        if kk not in self._pw:
            base = (self.a if kind == 'a' else self.beta)[idx]
            self._pw[kk] = base if k == 1 else _pmul(self.pw(kind, idx, k - 1), base)
        return self._pw[kk]

    def W(self, kl):
        """kl: ((k_e, l_e) for every external edge) -> {power of s: Fraction}"""
        if kl in self._W: return self._W[kl]
        p = self.iota
        for idx, (k, l) in enumerate(kl):
            if k: p = _pmul(p, self.pw('a', idx, k))
            if l: p = _pmul(p, self.pw('b', idx, l))
        out = {}
        for kk, c in p.items():
            if not c: continue
            ex = [(kk >> (BITS * i)) & MASK for i in range(self.nv)]
            num, den = 1, 1
            for blk in self.blocks:
                tot = 0
                for i in blk:
                    num *= factorial(ex[i]); tot += ex[i]
                den *= factorial(len(blk) + tot)
            sp = ex[self.spos]
            out[sp] = out.get(sp, 0) + F(c) * F(num, den)
        out = {k: v for k, v in out.items() if v}
        self._W[kl] = out
        return out

    def split(self, jets):
        """{(i, j): polynomial in s} = coefficient of lambda_0^i lambda_1^j (q T_0)^(J0-i) (q T_1)^(J1-j)
        in int iota prod_e y_{e,0}^{o_e0} y_{e,1}^{o_e1}"""
        if jets in self._split: return self._split[jets]
        out = {}
        ranges = [[(i, j) for i in range(o0 + 1) for j in range(o1 + 1)] for (o0, o1) in jets]
        for choice in itertools.product(*ranges):
            cf, kl, I, J = 1, [], 0, 0
            for (i, j), (o0, o1) in zip(choice, jets):
                cf *= comb(o0, i) * comb(o1, j)
                kl.append((i + j, o0 + o1 - i - j)); I += i; J += j
            d = out.setdefault((I, J), {})
            for sp, c in self.W(tuple(kl)).items():
                d[sp] = d.get(sp, 0) + cf * c
        self._split[jets] = out
        return out

    def phi(self, jets):
        """<lambda, T>^m x (jets): {(c, x, y, u, v): polynomial in s},
        monomial q^c lambda_0^x lambda_1^y T_0^u T_1^v"""
        J0 = sum(o[0] for o in jets); J1 = sum(o[1] for o in jets); m = self.m
        terms = {}
        for (i, j), sp in self.split(jets).items():
            for p in range(m + 1):
                cf = comb(m, p) * (-1) ** (m - p)
                d = terms.setdefault((J0 - i + J1 - j, i + p, j + m - p, J0 - i + m - p, J1 - j + p), {})
                for a, c in sp.items():
                    d[a] = d.get(a, 0) + cf * c
        return terms


_charts = {}


def register(rec):
    """make a chart record available (used by the generator of the charts)"""
    _charts[rec['tree']] = rec


@lru_cache(maxsize=None)
def tree(t):
    k = key(t)
    if k not in _charts:
        m = size(t)
        path = os.path.join(TABLES, 'tree_charts_m%d.json' % m)
        for rec in json.load(open(path))['records'].values(): _charts.setdefault(rec['tree'], rec)
    return Tree(_charts[k])


# ---------------------------------------------------------------------------------------------------------
# forests


def _sint(sp, kappa):
    """int_0^1 ds  sp(s) (1 - s)^kappa"""
    return sum(c * F(factorial(a) * factorial(kappa), factorial(a + kappa + 1)) for a, c in sp.items())


def forest_moment(f, jets):
    """f: tuple of trees; jets: (o_0, o_1) for every external edge, in the edge order of the forest.
    Returns {((x_1, y_1), ..., (x_R, y_R), (x_A, y_A)): Fraction}: exponents of lambda of every root, then lambda_A."""
    trs = [tree(t) for t in f]
    n = sum(t.m for t in trs)
    phis, at = [], 0
    for t in trs:
        k = len(t.ext_edges)
        phis.append(t.phi(tuple(jets[at:at + k]))); at += k
    assert at == len(jets)
    umax = [max((kk[3] for kk in ph), default=0) for ph in phis]
    vmax = [max((kk[4] for kk in ph), default=0) for ph in phis]
    U, V = sum(umax), sum(vmax)
    # T_0^U T_1^V is expanded with exponents kappa_r, kappa'_r on (1 - s_r) lambda_r and Delta, Delta' on lambda_A;
    # state: (U, V, C, Delta, Delta') -> {monomial of the roots so far: coefficient}
    states = {(0, 0, 0, 0, 0): {(): F(1)}}
    for r, (t, ph) in enumerate(zip(trs, phis)):
        fu, fv = sum(umax[r + 1:]), sum(vmax[r + 1:])
        psi = {}
        for (c, x, y, u, v), sp in ph.items():
            pre = factorial(t.m + c - 1)
            for kt in range(U + V + 1):
                si = _sint(sp, kt) * pre
                if not si: continue
                for k in range(max(0, kt - V), min(U, kt) + 1):
                    k2 = kt - k
                    d = psi.setdefault((u, v, c, u - k, v - k2), {})
                    mono = (x + k, y + k2)
                    d[mono] = d.get(mono, 0) + si / (factorial(k) * factorial(k2))
        new = {}
        for (U0, V0, C0, D0, E0), pol in states.items():
            for (u, v, c, du, dv), pp in psi.items():
                D1, E1 = D0 + du, E0 + dv
                if D1 + fu < 0 or E1 + fv < 0: continue
                tgt = new.setdefault((U0 + u, V0 + v, C0 + c, D1, E1), {})
                for mono, cf in pol.items():
                    for m2, c2 in pp.items():
                        if not c2: continue
                        kk = mono + (m2,)
                        tgt[kk] = tgt.get(kk, 0) + cf * c2
        states = new
    out = {}
    for (U0, V0, C0, D0, E0), pol in states.items():
        if D0 < 0 or E0 < 0: continue
        w = F(factorial(U0) * factorial(V0), factorial(D0) * factorial(E0) * factorial(n + C0 + 1))
        for mono, cf in pol.items():
            kk = mono + ((D0, E0),)
            out[kk] = out.get(kk, 0) + cf * w
    return {k: v for k, v in out.items() if v}


@lru_cache(maxsize=None)
def moments(n, ti, jets):
    """moment of the forest number ti (from 0) of forests(n)"""
    return forest_moment(forests(n)[ti], jets)
