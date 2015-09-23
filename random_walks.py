import random, collections, itertools

def step():
    if random.randrange(2) == 0:
        return -1
    return 1

def simulate_bool(fn, k=100):
    return sum(1 for _ in xrange(k) if fn())/float(k)

def avg(fn, k=100):
    return sum(fn() for _ in xrange(k))/float(k)

def walk(n):
    # Walk on [0,n-1] until hit n-1. Return visited counts.
    counts = [1] + [0]*(n-1)
    pos = 0
    while pos < n-1:
        if pos == 0:
            pos = 1
        else:
            pos += step()
        counts[pos] += 1
    return counts

def walk2(n):
    c = walk(n)
    return [min(x,2) for x in c]

def to_intervals(counts):
    d = collections.defaultdict(list)
    curr = None
    l = 0
    for e, x in enumerate(counts):
        if x == curr:
            continue
        if curr != None:
            d[curr].append((l, e-1))
        curr = x
        l = e
    d[curr].append((l, e-1))
    return d.items()

def pe(c):
    for e, x in enumerate(c):
        print e, x

def pd(c):
    for x in c:
        print x[0], x[1]

# TODO - can we speed this up by compressing data?
# E.g., if we are at position x in [a, b] which is all already double-covered,
# we know probability of getting to a-1 or b+1 first, and thus double-covering
# that (or single-covering if b+1 was not visited yet).

c = walk2(100)
pe(c)
pd(to_intervals(c))
