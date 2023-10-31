"""
Given an array of integers, return an array of triplets (in any order) such that i != j != k and nums[i] + nums[j] + nums[k] = 0. Note that the solution set must not include duplicate triplets (i.e., [1, 0, 0] and [0, 1, 0] are duplicative).

Example Inputs and Outputs
Example 1
Input: [-1,0,1,2,-1,-4] Output: [[-1,-1,2],[-1,0,1]]

Example 2
Input: [1,2,7,12] Output: []

Example 3
Input: [7,4,-7,0] Output: [[0,-7,7]], OR [[7,-7,0]], etc.
 
"""
def threeSum(nums,target):
    nums.sort()
    triplets_array = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        leftPtr = i + 1
        rightPtr = len(nums) - 1
        while leftPtr < rightPtr:
            currentSum = a + nums[leftPtr] + nums[rightPtr]
            if currentSum > 0:
                rightPtr -= 1
            elif currentSum < 0:
                leftPtr += 1
            else:
                triplets_array.append([a, nums[leftPtr], nums[rightPtr]])
                leftPtr += 1
                while nums[leftPtr] == nums[leftPtr - 1] and leftPtr < rightPtr:
                    leftPtr += 1
    return triplets_array