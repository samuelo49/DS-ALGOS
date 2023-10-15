"""
Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

Example Inputs and Outputs
Example 1
Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3

Example 2
Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7

Example 3
Input: nums = [1,2,3,4,5], left = 2, right = 4
Output: 9
"""
def numSubarrayBoundedMax(nums, left, right):
    count = 0
    subarray_start = -1
    valid_subarrays = 0
    
    for i in range(len(nums)):
        if nums[i] > right:
            subarray_start = i
            valid_subarrays = 0

        if left <= nums[i] <= right:
            valid_subarrays = i - subarray_start

        count += valid_subarrays

    return count
    