"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""
import heapq


def kthlargestNum(array, k):
    array = [-s for s in array]
    heapq.heapify(array)

    count = 1
    while count < k:
        heapq.heappop(array)
        count += 1
    return abs(array[0])

nums = [3,2,1,5,6,4]
k = 2
print(kthlargestNum(nums,k))
