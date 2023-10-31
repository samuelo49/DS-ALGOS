"""
Given an integer array nums, find a 
subarray
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
def maxProduct(nums):
    if not nums:
        return 0
    maxProduct = nums[0]
    currentProduct = 1
    for num in nums:
        if currentProduct == 0:
            currentProduct = 1
        currentProduct *= num
        maxProduct = max(maxProduct, currentProduct)
    return maxProduct
    
# test case
nums = [2,3,-2,4]
print(maxProduct(nums))