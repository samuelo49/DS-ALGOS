"""
Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Solution:
1. Brute force- 0(n^2) because we would essentially have to loop through the array twice for each element
2, Use a Hash table to store the element and its index as key value pairs, then while looping check if the difference
between the target and the current element is in the hash table,
if it is then return the index of the current element
"""
def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in lookup:
            return [lookup[difference], i]
        else:
            lookup[num] = i

# Time Complexity: O(n), since we are iterating through the list once
# Space Complexity: O(n), since we are storing the elements in a hash table

# tests
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
