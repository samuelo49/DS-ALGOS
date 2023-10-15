"""
Given an array, write 2 recursive functions to find the index of the minimum and maximum
element in an array. If there's a tie-breaker, return the first occurrence.
print(findMinIndex([12, 1234, 45, 67, 1]) == 4)
print(findMinIndex([10, 20, 30]) == 0)
print(findMinIndex([8, 6, 7, 5, 3, 7]) == 4)

print(findMaxIndex([12, 1234, 45, 67, 1]) == 1)
print(findMaxIndex([10, 20, 30]) == 2)
print(findMaxIndex([8, 6, 7, 5, 3, 7]) == 0)
"""


def findMinIndex(arr):
    def getMin(startIndex):
        if startIndex == len(arr) - 1:
            return startIndex
        smallestIndex = getMin(startIndex + 1)
        if arr[startIndex] > arr[smallestIndex]:
            return smallestIndex
        if arr[startIndex] < arr[smallestIndex]:
            return startIndex
        else:
            return min(startIndex, smallestIndex)

    return getMin(0)


def findMaxIndex(arr):
    def getMax(startIndex):
        if startIndex == len(arr) - 1:
            return startIndex
        largestIndex = getMax(startIndex + 1)
        if arr[startIndex] > arr[largestIndex]:
            return startIndex
        if arr[startIndex] < arr[largestIndex]:
            return largestIndex
        else:
            return min(startIndex,largestIndex)
    return getMax(0)

