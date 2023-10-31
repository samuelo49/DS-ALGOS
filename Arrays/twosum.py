"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

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
"""
def twoSum(nums, target):
    nums.sort()
    leftPtr = 0
    rightPtr = len(nums) - 1
    while leftPtr < rightPtr:
        currentSum = nums[leftPtr] + nums[rightPtr]
        if currentSum == target:
            return [leftPtr, rightPtr]
        elif currentSum < target:
            leftPtr += 1
        else:
            rightPtr -= 1
    return []   

# using hash table

def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in hashmap:
            return [i, hashmap[compliment]]
        else:
            hashmap[nums[i]] = i
    return []

# test case
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))