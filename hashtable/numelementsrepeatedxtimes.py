"""
Given an array and a target count X, return the number of elements
 that is repeated exactly X times.
 [1, 2, 3, 1, 2, 3], 2 => 3
[1, 2, 3, 1, 2, 3], 3 => 0
[1, 3, 3, 5, 5, 5, 5, 5, 3], 3 => 1
"""


def countExactOccurrences(arr, exactOccurrences):
    countElements = {}
    numCounter = 0
    for element in arr:
        if element not in countElements:
            countElements[element] = 1
        else:
            countElements[element] += 1
    for num, count in countElements.items():
        if count == exactOccurrences:
            numCounter += 1
    return numCounter


print(countExactOccurrences([1, 3, 3, 5, 5, 5, 5, 5, 3], 3))
