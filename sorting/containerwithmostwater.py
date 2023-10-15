
"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1
"""

# def maxArea(height):
#     maxWater = 0
#     left = 0
#     right = len(height) - 1
    
#     while left < right:
#         area = min(height[left], height[right]) * (right - left)
#         maxWater = max(maxWater, area)
#         # move pointer with the smaller height to maximize area
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -=1
#     return maxWater

# def minArea(height):
#     minWater = 0
#     left = 0
#     right = len(height) - 1
#     while left < right:
#         width = right - left
#         height = min(height[left], height[right])
#         area = width * height
#         minWater = min(minWater, area)
#         if height[left] < height[right]:
#             right -= 1
#         else:
#             left += 1
#     return minWater

# def reverseString(s):
#     """

#     Input: s = “a blue whale rhino Boston arepa heaven"
#     “ Output: s = “heaven arepa Boston rhino whale blue a“
#     """
#     words = s.split(" ")
#     reversed_sequence = words[::-1]
    
#     reversed_words = [word[::-1] for word in reversed_sequence]
    
#     return " ".join(reversed_words)

# print(reverseString("a blue whale rhino Boston arepa heaven")) # “heaven arepa Boston rhino whale blue a“

def subarraySum(nums,k):
    """
     Example 1
        Input: nums = [2, 2, 2], k = 4 Output: 2

        Example 2
        Input: nums = [3, 2, 1], k = 3 Output: 2

        Example 3
        Input: nums = [2, 2, -4, 1, 1, 2], k = -3 Output: 1
    """
    num_of_subarrays = 0
    running_sum = 0

    sum_count = {0:1}

    for i in range(0, len(nums)):
        running_sum += nums[i] #2 + 2 = 4
        differenceSum = running_sum - k # 2 - 4 = -2 # 
        if differenceSum in sum_count:
            num_of_subarrays += sum_count[differenceSum]

        sum_count[running_sum] = sum_count.get(running_sum, 0) + 1 # 
    return num_of_subarrays
    
print(subarraySum([2, 2, 2], 4)) # 2