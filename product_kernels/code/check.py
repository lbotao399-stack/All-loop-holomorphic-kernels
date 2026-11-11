"""Checks of the tables (standard library only).

1. closed forms at one and two loops;
2. every moment table is reproduced from the tree charts;
3. grading and exchange of the two components for every tabulated moment:
   the exponents of the 0-components sum to n + (number of d_1 on the contracted input letters), and
   exchanging the components 0 <-> 1 everywhere multiplies the moment by (-1)^n.
Usage:  python3 check.py [maximal loop order of step 2, default 4]"""
import sys, json, gzip, os, time
from fractions import Fraction as F
import product_kernels as PK
import gen_tables as G


def padd(p, q, c=1):
    out = dict(p)
    for k, v in q.items(): out[k] = out.get(k, 0) + c * v
    return {k: v for k, v in out.items() if v}


def pmul(p, q):
    out = {}
    for ka, ca in p.items():
        for kb, cb in q.items():
            k = tuple(a + b for a, b in zip(ka, kb)); out[k] = out.get(k, 0) + ca * cb
    return {k: v for k, v in out.items() if v}


def var(i, nvar):
    return {tuple(int(j == i) for j in range(nvar)): F(1)}


def bracket(u, v):
    """<u, v> = u_0 v_1 - u_1 v_0 for vectors u, v given as pairs of polynomials"""
    return padd(pmul(u[0], v[1]), pmul(u[1], v[0]), -1)


def flat(mom):
    return {tuple(x for pair in k for x in pair): v for k, v in mom.items()}


def closed_forms():
    # one loop: <lambda_1, lambda_A> / 2
    l1 = (var(0, 4), var(1, 4)); lA = (var(2, 4), var(3, 4))
    want = {k: v / 2 for k, v in bracket(l1, lA).items()}
    assert flat(PK.forest_moment(PK.forests(1)[0], ((0, 0),) * 2)) == want
    # two loops, one tree: -+ <lambda_1, lambda_A>^2 / 24
    sq = pmul(bracket(l1, lA), bracket(l1, lA))
    names = [list(map(PK.key, f)) for f in PK.forests(2)]
    for f, nm in zip(PK.forests(2), names):
        got = flat(PK.forest_moment(f, ((0, 0),) * (4 if len(f) == 2 else 3)))
        if nm == ['(A,(A,B))']: assert got == {k: -v / 24 for k, v in sq.items()}
        elif nm == ['(B,(A,B))']: assert got == {k: v / 24 for k, v in sq.items()}
        else:
            # two trees: <lambda_1, lambda_2 + 2 lambda_A> <lambda_2, lambda_1 + 2 lambda_A> / 24
            a = (var(0, 6), var(1, 6)); b = (var(2, 6), var(3, 6)); c = (var(4, 6), var(5, 6))
            two = lambda p: {k: 2 * v for k, v in p.items()}
            x = bracket(a, (padd(b[0], two(c[0])), padd(b[1], two(c[1]))))
            y = bracket(b, (padd(a[0], two(c[0])), padd(a[1], two(c[1]))))
            assert got == {k: v / 24 for k, v in pmul(x, y).items()}
    print('closed forms at one and two loops: ok')


def tables(nmax):
    n = 1
    while os.path.exists(os.path.join(PK.TABLES, 'product_kernels_n%d.json.gz' % n)):
        data = json.load(gzip.open(os.path.join(PK.TABLES, 'product_kernels_n%d.json.gz' % n), 'rt'))
        t0 = time.time(); cnt = bad = 0
        for ti, f in enumerate(PK.forests(n)):
            rec = data['records']['%d.%d' % (n, ti + 1)]
            assert rec['forest'] == list(map(PK.key, f)) and rec['automorphisms'] == PK.aut_forest(f)
            R = len(rec['roots'])
            ref = {tuple(map(tuple, m['jets'])): {tuple(ex): F(c) for ex, c in m['terms']} for m in rec['moments']}
            for jets, mom in ref.items():
                J0 = sum(j[0] for j in jets)
                assert all(sum(ex[0::2]) == n + J0 for ex in mom), 'grading'
                sw = tuple((s, r) for r, s in jets)
                swapped = {tuple(x for i in range(R + 1) for x in (ex[2 * i + 1], ex[2 * i])): (-1) ** n * c for ex, c in mom.items()}
                assert ref.get(sw) == swapped, 'exchange of the components'
            if n <= nmax:
                for jets in G.jets_up_to(len(rec['external_edges']), rec['max_total_jet_order']):
                    cnt += 1
                    if flat(PK.forest_moment(f, jets)) != ref.get(jets, {}): bad += 1
        print('n = %d: %d forests, jets <= %d, grading and exchange ok%s  [%.0fs]' % (
            n, len(PK.forests(n)), data['max_total_jet_order'],
            ', %d moments recomputed from the charts, %d differ' % (cnt, bad) if n <= nmax else '', time.time() - t0), flush=True)
        assert not bad
        n += 1


if __name__ == '__main__':
    closed_forms()
    tables(int(sys.argv[1]) if len(sys.argv) > 1 else 4)
