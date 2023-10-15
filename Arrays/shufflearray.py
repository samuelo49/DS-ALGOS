"""
Fisher-yates Algo of shuffling an array randomly.
"""
from random import randint


def shuffleRandomly(arr):
    if not arr or len(arr) == 0:
        return arr
    for i in range(len(arr)-1, 0, -1):
        randomIdx = randint(0, i-1)
        arr[randomIdx], arr[i] = arr[i], arr[randomIdx]
    return arr


numbers1 = [1, 2, 3, 4, 5, 6]
print(shuffleRandomly(numbers1))
# [2, 6, 1, 5, 3, 4]