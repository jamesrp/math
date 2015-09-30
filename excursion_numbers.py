from fractions import Fraction
# http://pastebin.com/7RDUhi42
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
        val -= Fraction(1,r)
        val -= sum(Fraction(1,2*(r-x))*f(x) for x in range(1,r))
    cache[r] = val
    return val

for i in [2**i for i in range(14)]:
    val = f(i)
    #print "{name:5s} = {dec:5f} = {frac}".format(name="p_%d"%i, dec=float(val),frac=val)
    print "{name:5s} = {dec:5f}".format(name="p_%d"%i, dec=float(val))
