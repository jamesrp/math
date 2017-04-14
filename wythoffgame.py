import math
import wythoff_aux

losing = set()
N = 300
phi = 0.5 * (1 + 5**0.5)

for s in range(N):
    for j in range(s+1):
        # Examine (j, s - j)
        if all(p not in losing for p in wythoff_aux.moves_from(j, s - j)):
            losing.add((j, s - j))
            losing.add((s - j, j))

A = [x for x in losing if x[0] <= x[1]]
A.sort()
for x in A:
    print x, math.ceil(x[0]*phi)

