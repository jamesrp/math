import random

def one(n, i):
    x = i
    t = 0
    while x > 0 and x < n:
        if random.randrange(2) == 0:
            x -= 1
        else:
            x += 1
        t += 1
    return x, t

def agg(samples, n, i):
    succ = 0
    val = 0
    val2 = 0
    for _ in range(samples):
        res, t = one(n, i)
        if res == 0:
            succ += 1
            val += t
        else:
            val2 += t
    return float(succ)/samples, float(val)/succ, float(val + val2)/samples

for i in [1,2,3,4,5]:
    a, b, c = agg(100000, 10, i)
    print i, a, 3*b, b, c
