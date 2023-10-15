"""
contains duplicates
Given an integer array nums, return true if any value appears at least twice in the array,
 and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
Input: nums = [1,2,3,4]
Output : false
"""


def containsDuplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

nums1 = [1,1,1,3,3,4,3,2,4,2]
nums2 = [1,2,3,4]
print(containsDuplicates(nums1))

"""


"""