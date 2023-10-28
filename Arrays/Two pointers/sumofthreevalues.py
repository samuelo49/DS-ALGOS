"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j,
i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
def threeSum(nums):
    nums.sort() # sorting the array in place costs 0(nlogn)
    triplets =  []

    for i, a in enumerate(nums):
        leftPtr = i + 1
        rightPtr = len(nums) - 1

        while leftPtr < rightPtr: # we are running twoSum using leftPtr and rightPtr
            threeSum = a + nums[leftPtr] + nums[rightPtr]
            if threeSum > 0:
                rightPtr -= 1
            elif threeSum < 0:
                leftPtr += 1
            else:
                triplets.append([a,nums[leftPtr], nums[rightPtr]])
                leftPtr += 1
                while nums[leftPtr] == nums[leftPtr - 1] and leftPtr < rightPtr:
                    leftPtr = 1
    return triplets

# tests
nums1 = [-1,0,1,2,-1,-4]
print(threeSum(nums1)) 

nums2 = [0,1,1]
print(threeSum(nums2)) ==  []