from fractions import Fraction
import pickle
# http://pastebin.com/7RDUhi42

filename = "excursions_cache.pickle"
try:
    with open(filename, "r") as f:
        cache = pickle.load(f)
except:
    cache = {}

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

for i in range(50,1500,10):
    val = lower_part(i,9*i/10)
    print "{name:5s} = {dec:5f}".format(name="L_%d"%i,dec=float(val))

with open(filename, "w") as g:
    pickle.dump(cache, g)
