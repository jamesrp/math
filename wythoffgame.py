losing = set()
N = 300

def moves_from(a,b):
    for i in xrange(a):
        yield (i,b)
    for i in xrange(b):
        yield (a,i)
    for i in xrange(1,min(a,b)+1):
        yield (a-i,b-i)

for s in range(N):
    for j in range(s+1):
        # Examine (j, s - j)
        if all(p not in losing for p in moves_from(j, s - j)):
            losing.add((j, s - j))
            losing.add((s - j, j))

A = [x for x in losing if x[0] <= x[1]]
A.sort()
for x in A:
    print x

