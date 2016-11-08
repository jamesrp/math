from fractions import Fraction
import pickle
import  math
# http://pastebin.com/7RDUhi42

filename = "excursions_cache.pickle"
try:
    with open(filename, "r") as f:
        cache = pickle.load(f)
except:
    cache = {}

# f_r and f_{i,r} are defined together, and related by the recurrences below.
# f_{i,r} ranging over i for fixed r is the distribution of the leftmost
# single covered point when we first reach r.
# To derive the formulas, consider a Markov chain with state space (i,r)
# with i = LSC and r = rightmost reached point.
# Initial values for r = 1, 2, 3 (for i = 0, ..., r):
# 0 1
# 1/2 0 1/2
# 1/3 0 1/4 5/12
def f(r): 
    if r in cache:
        return cache[r]
    elif r == 0: 
        val = Fraction(1,1)
    elif r == 1:
        val = Fraction(0,1)
    else:
        val = Fraction(1,1)
        val -= sum(f2(x,r) for x in range(r))
    cache[r] = val
    return val

def f2(i,r):
    if i == 0:
        return Fraction(1,r)
    elif i == r:
        return f(r)
    else:
        return Fraction(1,2*(r-i))*f(i)

def lower_part(r,k):
    return sum(f2(i,r) for i in range(k))

# The following function computes E((r-i)^2) over f2(i,r). This is the 
# expected time to reach the LSC point, given that we start at r.
# That is, C_2 - C_1.
def extra_dct(r):
    total = Fraction(0,1)
    for i in range(r):
        total += (r-i)**2 * f2(i,r)
    return total

for i in range(5,15,3):
    print i, float(extra_dct(i))

with open(filename, "w") as g:
    pickle.dump(cache, g)
