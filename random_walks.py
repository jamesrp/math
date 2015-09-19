import random

def step():
    if random.randrange(2) == 0:
        return -1
    return 1

def simulate_bool(fn, k=100):
    return sum(1 for _ in xrange(k) if fn())/float(k)

def avg(fn, k=100):
    return sum(fn() for _ in xrange(k))/float(k)

def f():
    n, k = 1000, 400
    counts = [1] + [0]*(n-1)
    pos = 0
    while pos < n-1:
        if pos == 0:
            pos = 1
        else:
            pos += step()
        counts[pos] += 1
    return min(x for x in xrange(n) if counts[x] < 2)
    # return all(x >= 2 for x in counts[:k])

print avg(f)
