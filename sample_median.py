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

# print check(lambda: random.randrange(100), 1000)
# >>> (49.562, 2.5781559999999915)
# Formula gives var = 1/4nf(m)**2 = 2.5.

# Now look at the data from one run and predict the variance.
def median_variance(xs):
    s = sorted(xs)
    c = len(xs)
    a, b = int(c * .55), int(c * .45)
    return s[c/2], (s[a] - s[b])**2 / (0.01 * 4 * c)

# xs = [random.randrange(100)**2 for _ in range(1000)]
# print median_variance(xs)
# >>> (2601, 27040.0)
# print check(lambda: random.randrange(100)**2, 1000)
# >>> (2462.734, 25236.599244000012)
