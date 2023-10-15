"""
Given an array of integers representing piles of rocks (e.g., 3 means 3 rocks),
 modify the input array to rank the piles from 1 to N, representing the least to
the most quantity of rocks.
That is, the pile with the lowest count of rocks should be ranked 1, the second
 lowest should be 2, and so on.
[10, 8, 15, 12, 6, 20, 1]

"""


def rankPiles(piles):
    ranks = {}
    for i in range(len(piles)):
        ranks[piles[i]] = i
    #ranks - >{10: 0, 8: 1, 15: 2, 12: 3, 6: 4, 20: 5, 1: 6}
    sortedKeys = sorted(ranks.keys(), reverse=False)
    # [1, 6, 8, 10, 12, 15, 20]

    rank = 1
    for key in sortedKeys:
        value = ranks[key]
        piles[value] = rank
        rank += 1
    return piles

print(rankPiles([10, 8, 15, 12, 6, 20, 1]))