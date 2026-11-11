"""Tables of the product-forest kernel moments, assembled from the tree charts (product_kernels.py).

For every forest with n interaction vertices and every assignment of jets (r, s) to its external edges with
total order <= J, the moment
    M(jets) = prod_e (-1)^{r_e + s_e} r_e! s_e!  x  [Taylor coefficient of the raw-cut kernel in the edge displacements]
            = < prod_e y_{e,0}^{r_e} y_{e,1}^{s_e} >
as a polynomial in the sources lambda_root (one per tree) and lambda_A (two components each).
Usage:  python3 gen_tables.py n J
Output: tables/product_kernels_n<n>.json.gz  (one record per forest)."""
import sys, json, gzip, time, os
import product_kernels as PK

CONV = ('vertices 1..n interactions, A = n+1, B = n+2; edges = increasing pairs in lexicographic order, '
        'auxiliary edge (A,B) last; sources: one two-component lambda per tree root and lambda_A; '
        'moment = prod_e (-1)^(r_e+s_e) r_e! s_e! x Taylor coefficient of the raw-cut kernel; '
        'terms: [[exponents of (lambda_root1_0, lambda_root1_1, ..., lambda_A_0, lambda_A_1)], "p/q"]')


def jets_up_to(k, J):
    """all assignments of (r, s) to k edges with total order <= J"""
    out = []

    def rec(i, left, cur):
        if i == 2 * k:
            out.append(tuple((cur[2 * a], cur[2 * a + 1]) for a in range(k))); return
        for x in range(left + 1):
            rec(i + 1, left - x, cur + [x])
    rec(0, J, [])
    return out


def main(n, J):
    path = os.path.join(PK.TABLES, 'product_kernels_n%d.json.gz' % n)
    data = {'loops': n, 'max_total_jet_order': J, 'conventions': CONV, 'records': {}}
    t0 = time.time(); total = 0
    for ti, f in enumerate(PK.forests(n)):
        rid = '%d.%d' % (n, ti + 1)
        edges, roots = PK.edges_of(f)
        ext = [e for e in edges[:-1] if e[1] > n]
        moments = []
        for jets in jets_up_to(len(ext), J):
            mom = PK.forest_moment(f, jets)
            if not mom: continue
            terms = [[[x for pair in jj for x in pair], str(c)] for jj, c in sorted(mom.items(), reverse=True)]
            moments.append({'jets': [list(j) for j in jets], 'terms': terms}); total += len(terms)
        data['records'][rid] = {
            'id': rid, 'forest': list(map(PK.key, f)), 'edges': [list(e) for e in edges], 'roots': list(roots),
            'automorphisms': PK.aut_forest(f), 'external_edges': [list(e) for e in ext],
            'sources': ['lambda_%d' % r for r in roots] + ['lambda_A'], 'max_total_jet_order': J,
            'nonzero_moments': len(moments), 'moments': moments}
        print('%s %s: %d external edges, %d nonzero moments  [%.0fs]' % (rid, list(map(PK.key, f)), len(ext), len(moments), time.time() - t0), flush=True)
    with gzip.GzipFile(path, 'w', mtime=0) as g:
        g.write(json.dumps(data, separators=(',', ':')).encode())
    print('n=%d J=%d: %d forests, %d terms, %.1f MB' % (n, J, len(PK.forests(n)), total, os.path.getsize(path) / 1e6))


if __name__ == '__main__':
    main(*map(int, sys.argv[1:]))
