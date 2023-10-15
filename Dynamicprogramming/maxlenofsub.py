"""
Given two integer arrays nums1 and nums2, 
return the maximum length of a subarray that appears in both arrays.
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
"""

def findLength(nums1, nums2) -> int:
    memo = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]     
    for i in reversed(range(len(nums1))):
        for j in reversed(range(len(nums2))):
            if nums1[i] == nums2[j]:
                memo[i][j] = memo[i + 1][j + 1] + 1
    return max(max(row) for row in memo)


print(findLength([1,2,3,2,1], [3,2,1,4,7]))

# time complexity: O(m*n)
# space complexity: O(m*n)