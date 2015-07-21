import random
import itertools
import bisect
import sys

# Uniform (0,1) random variable.
def u():
    return random.uniform(0,1)

# Return the confidence interval with given precision
# associated with the median of n samples. Parameter k
# controls how may experiments we run to verify this,
# so it should grow as n or precision increase.
def confidence_interval(n, k, precision):
    c = 0
    media = []
    while c < k:
        d = nsamples(u, n)
        d.sort()
        try:
            i = rank_of_true_median(d, 0.5)
            media.append(i)
            c += 1
        except ValueError:
            print None
    lo, hi = interval_endpoints(k, precision)
    media.sort()
    return media[lo], media[hi]

# Returns lo, hi such that
# [lo, hi] covers precision * [0, k]
def interval_endpoints(k, precision):
    lo, hi = k * 0.5 * (1 - precision), round(k * 0.5 * (1 + precision))
    lo, hi = int(lo), int(hi)
    if hi >= k:
        hi = k - 1
    return lo, hi

def nsamples(dist, n):
    return [dist() for _ in range(n)]

def rank_of_true_median(data, median):
    i = bisect.bisect_right(data, median)
    if i:
        return i - 1
    raise ValueError

print confidence_interval(118, 10000, 0.95)
