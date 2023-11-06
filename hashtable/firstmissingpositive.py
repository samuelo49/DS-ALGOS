"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

"""
def firstMissingPositive(nums):
    # base case, check if 1 is in the array
    if 1 not in nums:
        return 1
    
    # if 1 is in the array, check if the array is only 1
    if len(nums) == 1:
        return 2
    
    # if the array is not only 1, then we can start the algorithm
    # replace all the negative numbers with 1 and numbers greater than len(nums) with 1

    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] > len(nums):
            nums[i] = 1

    # now we have an array with only positive numbers and numbers less than or equal to len(nums)
    # we can use the array as a hash table
    # we can mark the numbers that are in the array by changing the sign of the index of the number
    # for example, if we see 3, we change the sign of nums[3] to negative
    for i in range(len(nums)):
        a = abs(nums[i])
        if a == len(nums):
            nums[0] = -abs(nums[0])
        else:
            nums[a] = -abs(nums[a])

    # now we can check the first positive number in the array
    for i in range(1, len(nums)):
        if nums[i] > 0:
            return i
        
    # if we don't find any positive number, we check if nums[0] is positive
    if nums[0] > 0:
        return len(nums)
    
    # if nums[0] is not positive, we return the next number
    return len(nums) + 1
        
    
# test cases
# nums1 = [1,2,0]
# nums2 = [3,4,-1,1]
nums3 = [7,8,9,11,12]
nums4 = [1,2,3,4,5,6,7,8,9,10]
nums5 = [1,1,1,1,1,1,1,1,1,1]

# print(firstMissingPositive(nums1))
# print(firstMissingPositive(nums2))
print(firstMissingPositive(nums3))
print(firstMissingPositive(nums4))
print(firstMissingPositive(nums5))
