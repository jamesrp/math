import random

def step():
    if random.randrange(2) == 0:
        return -1
    return 1

def simulate_bool(fn, k=100):
    return sum(1 for _ in xrange(k) if fn())/float(k)

def double_covered_while_single_covering_half():
    n = 1000
    counts = [1] + [0]*(n-1)
    pos = 0
    while pos < n-1:
        if pos == 0:
            pos = 1
        else:
            pos += step()
        counts[pos] += 1
    return all(x >= 2 for x in counts[:n/2])

print simulate_bool(double_covered_while_single_covering_half,50)
