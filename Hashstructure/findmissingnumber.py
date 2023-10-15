"""
HashStructures_setMismatch1
You have a set of integers `nums`, which originally contains all
 the numbers from 1 to n. Unfortunately, due to some error,
one of the numbers in *nums* got duplicated to another number in the set,
which results in the repetition of one number and the loss of another number.

You are given an integer array `nums` representing the data after the error.
Return the missing number. If no number is missing, return -1.

Input: nums = [1,2,2,4]
Output: 3

Input: nums = [1,1]
Output: 2

Input: nums = [3,1,2]
Output: -1
"""


def missingNumber(nums):
    maxDistinct = len(nums)
    for i in range(maxDistinct + 1):
        if i not in nums:
            return i
        else:
            return maxDistinct + 1


print(missingNumber([1, 1]))
# print(missingNumber([1,2,2,4]))
# print(missingNumber([3,1,2]))
