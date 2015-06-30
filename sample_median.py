import random

def median(lst):
    return sorted(lst)[len(lst)/2]

def sample_median(X, n):
    xs = [X() for _ in xrange(n)]
    return median(xs)

def statistics(xs):
    # Returns mean, variance
    s = sum(xs)
    c = len(xs)
    mean = float(s)/c
    s2 = sum((x-mean)**2 for x in xs)/float(c)
    return mean, s2 

def check(X, n):
    ms = [sample_median(X,n) for _ in range(1000)]
    return statistics(ms)

# Formula gives var = 1/4nf(m)**2
#  = 2.5.
# An example run of check gives
#  (49.562, 2.5781559999999915)
print check(lambda: random.randrange(100), 1000)


