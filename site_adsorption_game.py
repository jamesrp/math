
cache = {}
def nimber(p):
    if p in cache:
        return cache[p]
    vals = set()
    for q in moves_from(p):
        total = 0
        for x in q:
            total ^= nimber(x)
        vals.add(total)
    mex = 0
    while mex in vals:
        mex += 1
    cache[p] = mex
    return mex

def moves_from(n):
    for i in xrange(1,n+1):
        yield (i - 2, n - i - 1)

def moves_from_opt(n):
    # can go in position i in 1, ..., n;
    # leaves positions 1, ..., i-2; and i+2, ..., n accessible.
    # that is, (i-2, n-i-1), if either of those are nonnegative.
    # Finally, we may use symmetry to avoid half of the returns.

    # Handle small values separately.
    if n < 5:
        if n < 2:
            if n == 1:
                yield (0,) # 1
            yield tuple() # 0
        if n == 4:
            yield (1,) # 4
        yield (0,) # 3, 2
    else: 
        yield (0,n-2)
        yield (0,n-3)
        for i in xrange(3,(n+1)/2 + 1):
            yield (i - 2, n - i - 1)

for i in range(100):
    print i, nimber(i)
