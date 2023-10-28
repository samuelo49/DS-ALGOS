"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0] [0,0,2,1,1,2] [0,0,1,1,2,2]
Output: [0,0,1,1,2,2]


Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

step 1: declare two pointers, left and right

left = 0
right = len(nums - 1)

pivot = min(nums)
if element at left is greater than  pivot then swap it with rightPtr, move right
if element at right is greater than element are left then swap move left
"""

def sortColors(nums):
    pivot = min(nums)
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] > pivot:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        else:
            left += 1
    return nums

# nums1 = [2,0,1]
# print(sortColors(nums1))

nums2 = [2,0,2,1,1,0]
print(sortColors(nums2))
            
            