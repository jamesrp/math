# Sampling randrange(n) given randrange(m)
import random, collections

# instrumenting random.randrange
count = 0
def randrange(n):
    global count
    count += 1
    return random.randrange(n)

# First version - throwing away extra randomness when retrying
def ntom(n, m):
    states = 1
    outcome = 0
    while states < m:
        states *= n
        outcome = outcome * n + randrange(n)
    if outcome / m < states / m:
        return outcome % m
    return ntom(n, m)

# Optimized version - when retrying, carry over states and outcome
def ntom2(n, m):
    states = 1
    outcome = 0
    while True:
        states *= n
        outcome = outcome * n + randrange(n)
        if states < m:
            continue
        blocksize = (states / m) * m
        if outcome < blocksize:
            return outcome % m
        # Cut down size of ints
        outcome -= blocksize
        states -= blocksize

def streaming_ntom(n, m):
    states = 1
    outcome = 0
    blocksize = m
    while True:
        states *= n
        outcome = outcome * n + randrange(n)
        if states < blocksize:
            continue
        if outcome / blocksize < states / blocksize:
            yield outcome % m
            blocksize *= m
            # TODO - can we throw away some of this data after we are done?

def evaluate(s):
    d = collections.defaultdict(int)
    for e, x in enumerate(s):
        if e >= 1000:
            break
        d[x] += 1
    for v in sorted(d.keys()):
        print v, d[v]
    print "count:", count

print "Naive"
evaluate([ntom(2, 5) for _ in range(1000)])
count = 0
print "Optimized"
evaluate([ntom2(2, 5) for _ in range(1000)])
count = 0
print "Streaming"
evaluate(streaming_ntom(2, 5))
