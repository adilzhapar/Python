from itertools import collections
def AllSubs(s):
    subs = []
    for i in range(0, len(s)+1):
        hand = [list(x) for x in combinations(s, i)]
        if len(hand) > 0:
             