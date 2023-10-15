"""
Write an efficient program for printing k largest elements in an array. Largest elements are returned in order largest to smallest.

Example Inputs and Outputs
Example 1
Input: nums = [3, 7, 2, 1, 8, 5, 9], k = 3
Output: [9,8,7]
"""
import heapq
def kLargestElements(nums,k):
    heap = [-num for num in nums]
    heapq.heapify(heap) 

    result = []
    while k > 0:
        result.append(-heapq.heappop(heap)) #
        k -= 1
    return result

print(kLargestElements([3, 7, 2, 1, 8, 5, 9], 3))

# time complexity 0()