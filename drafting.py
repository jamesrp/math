# See drafting.txt

import random, itertools, heapq, collections

_COLORS = range(5)
_COLOR_PAIRS = list(itertools.combinations(_COLORS, 2))

_CUTOFF = 0
_LINEAR = 1

Card = collections.namedtuple("Card", ["color", "value"])

def generate_pack(color_strengths):
    output = []
    for _ in range(15):
        color = random.choice(_COLORS)
        value = random.expovariate(1.0/color_strengths[color])
        # Make all values greater than 1, so we can treat negative values as sentinel values throughout.
        output.append(Card(color, value + 1))
    return output

def draft_one_pack(drafters, color_strengths):
    packs = [generate_pack(color_strengths) for _ in range(8)]
    for p in range(15):
        [drafters[i].select(packs[i]) for i in range(8)]
        packs = packs[1:] + packs[:1]

def simulate_draft(drafters, color_strengths):
    draft_one_pack(drafters, color_strengths)
    rdrafters = list(reversed(drafters))
    draft_one_pack(rdrafters, color_strengths)
    draft_one_pack(drafters, color_strengths)
    return [drafter.score() for drafter in drafters]

class Drafter(object):
    def __init__(self, color_biases, interpolation_type, interpolation_param):
        self.color_biases = color_biases
        self.interpolation_type = interpolation_type
        self.interpolation_param = interpolation_param
        cards_picked = 0
        self.values = {pair: 0 for pair in _COLOR_PAIRS}
        self.heaps = {pair: [] for pair in _COLOR_PAIRS}

    def score(self, card=None):
        if card is None:
            return max(self.values.values())
        outcomes = []
        for pair in _COLOR_PAIRS:
            if card.color not in pair:
                outcomes.append(self.values[pair])
                continue
            heap = self.heaps[pair]
            heap_len = len(heap)
            if heap_len == 0:
                outcomes.append(card.value)
            elif heap_len < 23:
                outcomes.append(self.values[pair] + card.value)
            elif heap[0] < card.value:
                outcomes.append(self.values[pair] + card.value - heap[0])
        return max(outcomes)

    def select(self, pack):
        best_values = defaultdict(lambda: -1)
        for i in pack:
            best_values[card.color] = max(best_values[card.color], card.value)

        scores = {}
        for color in best_values:
            bias_score = self.color_biases[color] + best_values[color]
            pool_score = self.score(card = (color, best_values[color]))
            if self.interpolation_type == _CUTOFF:
                if self.cards_picked < self.interpolation_param:
                    scores[color] = bias_score
                else:
                    scores[color] = pool_score
                continue
            if self.interpolation_type == _LINEAR:
                if self.cards_picked >= self.interpolation_param:
                    scores[color] = pool_score
                else:
                    a = fractions.Fraction(self.cards_picked, self.interpolation_param)
                    b = fractions.Fraction(self.interpolation_param - self.cards_picked, self.interpolation_param)
                    scores[color] = a * pool_score  + b * bias_score
                continue
            raise ValueError("Unknown interpolation type " + str(self.interpolation_type))

        color = max(scores, key = lambda c: scores[c])
        pack.remove(Card(color, scores[color])
        color_pairs = [pair for pair in _COLOR_PAIRS if color in pair]
        for pair in color_pairs:
            heapq.heappush(self.heaps[pair], scores[color])
            self.values[pair] += scores[color]
            if len(self.heaps[pair]) > 23:
                self.values[pair] -= heapq.heappop(heap)
