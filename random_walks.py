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

def kcover(n, k):
    # how many times node i was visited
    counts = [1] + [0]*n
    # todo[i-1] == how many x, 0 <= x <= n, have counts[x] < i
    # (for 1 <= i <= k)
    todo = [n] + [n+1]*(k-1)
    # times[i-1] == how long it took to i-cover
    times = []
    i = 0
    steps = 0
    # The level we are currently attempting.
    curr_level = 1
    while curr_level <= k:
        if i == 0:
            i = 1
        elif i == n:
            i = n-1
        else:
            i += step()
        steps += 1
        counts[i] += 1
        if counts[i] <= k:
            todo[counts[i]-1] -= 1
            if todo[counts[i] - 1] == 0 and counts[i] == curr_level:
                times.append(steps)
                curr_level += 1
    return times

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

def avg_list(ls, n, k):
    out = [0 for _ in range(k)]
    for x in ls:
        if len(x) != k:
            raise ValueError("len({0}) != {1}".format(x, k))
        for i in range(k):
            out[i] += x[i]
    return [out[i]/float(n) for i in range(k)]

samples = 1000000
k = 2
for n in range(5,15,3):
    ls = (kcover(n, k) for _ in xrange(samples))
    out = avg_list(ls, samples, k)
    print n, out[1] - out[0], out
