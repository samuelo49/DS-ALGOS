"""
Given an array of unique integers, find all pairs of elements
 with the minimum absolute difference.
 If there are multiple pairs, return them in ascending order.
 [1,3,6,10,15]
 [3,8,-10,23,19,-4,-14,27] -> [[-14,-10],[19,23],[23,27]]
"""


def minAbsDiffPairs(arr):
    resultStack = []
    arr.sort()
    minAbsDiff = float("inf")
    for i in range(len(arr) - 1):
        absDiff = arr[i + 1] - arr[i]
        pair = [arr[i], arr[i + 1]]
        if absDiff < minAbsDiff:
            resultStack = [pair]
            minAbsDiff = absDiff
        elif absDiff == minAbsDiff:
            resultStack.append(pair)
    return resultStack


print(minAbsDiffPairs([3, 8, -10, 23, 19, -4, -14, 27]))
