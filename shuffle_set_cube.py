import random
import sys
import collections

mode = "COMMONS"

if mode == "COMMONS":
    DISTINCT_CARDS = 101
    OWNED_COPIES = 4
    BOOSTERS = 24
    CARDS_PER_BOOSTER = 10
elif mode == "UNCOMMONS":
    DISTINCT_CARDS = 80
    OWNED_COPIES = 3
    BOOSTERS = 24
    CARDS_PER_BOOSTER = 3
else:
    sys.exit(1)

def generate_packs_retail():
    packs = []
    for _ in range(BOOSTERS):
        booster = []
        for _ in range(CARDS_PER_BOOSTER):
            card = random.randrange(DISTINCT_CARDS)
            booster.append(card)
        packs.append(booster)
    return packs

def generate_packs_computer_assisted():
    remaining_copies = {i: OWNED_COPIES for i in range(DISTINCT_CARDS)}
    packs = []
    for _ in range(BOOSTERS):
        booster = []
        for _ in range(CARDS_PER_BOOSTER):
            card = random.randrange(DISTINCT_CARDS)
            while remaining_copies[card] == 0:
                card = random.randrange(DISTINCT_CARDS)
            remaining_copies[card] -= 1
            booster.append(card)
        packs.append(booster)
    return packs

def generate_packs_no_replacement():
    # Shuffle all commons together. Sometimes I sort into piles of 1x each
    # and shuffle those to make there not be multiple copies of a common
    # in a pack, but it shouldn't affect this much.
    pool = range(DISTINCT_CARDS) * OWNED_COPIES
    random.shuffle(pool)
    packs = []
    for _ in range(BOOSTERS):
        booster = pool[:CARDS_PER_BOOSTER]
        pool = pool[CARDS_PER_BOOSTER:]
        packs.append(booster)
    return packs

def make_histogram(packs):
    d = {i: 0 for i in range(DISTINCT_CARDS)}
    for p in packs:
        for c in p:
            d[c] += 1
    h = collections.defaultdict(int)
    for c in d:
        h[d[c]] += 1
    return h

def average_histograms(hs):
    h = hs[0]
    for i in hs[1:]:
        for k in i:
            h[k] += i[k]
    for k in h:
        h[k] /= float(len(hs))
    return h

def report(f, name):
    hs = []
    for _ in range(10000):
        p = f()
        h = make_histogram(p)
        hs.append(h)
    h = average_histograms(hs)
    print name
    total = sum(h.values())
    for k in sorted(h.keys()):
        print "{} {:>6.2f} {:>6.2%}".format(k, h[k], h[k] / total)

def print_reports():
    report(generate_packs_retail, "Retail boosters")
    report(generate_packs_computer_assisted, "Tool-assisted")
    report(generate_packs_no_replacement, "Shuffle all into pile")

def booster_name(i):
    if i == -1:
        return "Trash"
    if i < 8:
        return "A" + str(i%8)
    if i < 16:
        return "B" + str(i%8)
    return "C" + str(i%8)

    
def assist_user():
    # Actually generate packs with replacement (until we hit max cards),
    # then transform that into a map[card] -> booster or trash.
    packs = generate_packs_computer_assisted()
    for p in packs:
        print p
    m = {card: [] for card in range(DISTINCT_CARDS)}
    for i in range(BOOSTERS):
        for card in packs[i]:
            m[card].append(i)
    for card in range(DISTINCT_CARDS):
        n = len(m[card])
        for _ in range(OWNED_COPIES - n):
            m[card].append(-1)
        print card, [booster_name(i) for i in m[card]]

assist_user()
