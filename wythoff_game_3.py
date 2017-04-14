losing = set()
N = 200
TYPE = 1 # 1 is take same from 3, 2 is take same from any two piles

def sum_to(n):
    for i in xrange(n+1):
        for j in xrange(n+1-i):
            yield (i, j, n - i - j)

def moves_from(i,j,k):
    for a in xrange(i):
        yield (a,j,k)
    for a in xrange(j):
        yield (i,a,k)
    for a in xrange(k):
        yield (i,j,a)
    if TYPE == 1:
        for a in xrange(1,min(i,j,k)+1):
            yield (i-a,j-a,k-a)
    if TYPE == 2:
        for a in xrange(1,min(i,j)+1):
            yield (i-a,j-a,k)
        for a in xrange(1,min(i,k)+1):
            yield (i-a,j,k-a)
        for a in xrange(1,min(j,k)+1):
            yield (i,j-a,k-a)
        

for s in xrange(N+1):
    print "Processing %d/%d" % (s,N)
    for i,j,k in sum_to(s):
        if all(p not in losing for p in moves_from(i,j,k)):
            losing.add((i,j,k))
            losing.add((i,k,j))
            losing.add((j,i,k))
            losing.add((j,k,i))
            losing.add((k,i,j))
            losing.add((k,j,i))

A = [x for x in losing if x[0] <= x[1] and x[1] <= x[2]]
B = [x for x in A if x[0] > 0]
B.sort()

# For each n, print the smallest tuple where n appears as the least element.
C = {}
for x in B:
    if x[0] in C:
        if C[x[0]] > x:
            C[x[0]] = x
    else:
        C[x[0]] = x

for n in sorted(C.keys()):
    x = C[n]
    print x, float(x[1])/x[0], float(x[2])/x[0]
