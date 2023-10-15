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
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                triplets_array.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
    return triplets_array