# St petersburg bet problem analysis.
# A single bet pays off $2 with 1/2 chance, $4 with 1/4 chance, ..., 
# $ 2^n with 2^(-n) chance.
# So expected value is infinite. But how much should we actually pay for a bet
# if we can repeat as much as we want?

import random, math


def bet():
    # Returns payoff for a single bet
    payoff = 2
    while True:
        if random.randrange(2) == 0:
            return payoff
        payoff *= 2

def simulate(n, k, t):
    # Returns whether someone starting at n and paying k for each bet gets to t
    balance = n
    # Note that this could go on arbitrarily long, but by random walks hopefully
    # it does not.
    while True:
        balance -= k
        balance += bet()
        if balance >= t:
            return True
        if balance < k:
            return False

def analyze(n, k, t, samples):
    successes = 0
    for i in range(samples):
        if simulate(n, k, t):
            successes += 1
    return float(successes)/samples

N = 1000 # starting bank balance
K = None # amount paid for each bet, specified below
T = 99*N # target bank balance

for K in range(3,12):
    print K, analyze(N, K, T, 100)

def cutoff(N):
    t = math.log(N) / math.log(2)
    def fn(x):
        return x + (math.log(x) / math.log(2))
    x = 1
    while fn(x) <= t:
        x += 1
    return x

print cutoff(1000)
