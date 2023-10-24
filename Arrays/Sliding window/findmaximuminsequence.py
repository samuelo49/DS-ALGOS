"""
Given an integer list, nums, find the maximum values in all the contiguous subarrays (windows) of size w.
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

"""
def maxSlidingWindow(nums, k):
    n = len(nums)
    output = []
    if n < k:
        return nums
    for start in range(n - k + 1):
        window = nums[start: start + k]
        max_num = max(window)
        output.append(max_num)
    return output
numss = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(numss,k=k))
