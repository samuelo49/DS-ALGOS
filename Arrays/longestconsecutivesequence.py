"""
Given an unsorted array of integers nums, return the length of the longest consecutive
 elements sequence.

You must write an algorithm that runs in O(n) time.
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.
"""


def longestSeq(arr):
    numSet = set(arr)
    longest = 0

    for n in nums:
        if n - 1 not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(longest, length)
    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longestSeq(nums))
