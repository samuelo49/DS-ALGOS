'''
Given an integer list, nums, find the maximum values in all the contiguous subarrays(window)
of size w. 
Note: If the window size is greater than the array size, we consider the entire array
as a single window.
Example 1:
nums = [-4, 2, -5, 3, 6], w = 3
OUTPUT = [2,3,6]

Example 2:
nums = [1,2,3,4,5,6], w = 6
OUTPUT = 6

Example 3:
nums = [1,2,3,4,5,6,7,8,9,10], w = 4
OUTPUT = [4,5,6,,7,8,9,10]

Example 4 
nums = [-4,5,4,-4,4,6,7,20] w = 2
OUTPUT = [5,5,4,4,6,7,20]

Example 5
nums = [-4,5,4,-4,4,6,7] w = 10
OUTPUT = [7]

Plan
- Use sliding window technique, where I get the maximum integer in each window then slide 

STEPS
1: Check if the input array is empty. If so, return an empty array.
2. Check if the window size is greater than the length of the input array
  If so, return an array containing the maxium value in the input array.
3: Initialize an output array to store the maximum values.
4. Loop through the input array, maintaining a window of size w. In each iteration:
    - Calculate the maximum value in the current window
    - Append the maximum value to the output array.
    - Slide the window one element to the right. If the maximum value was the element
        being removed, recalculate the maximum value for the new window.
5. After the loop, return the output array.
'''
def max_in_sliding_window(nums, w):
    n = len(nums)
    output = []
    if n < w:
        return [max(nums)]
    for start in range(n - w + 1):
        window = nums[start: start + w]
        maximum_num = max(window)
        output.append(maximum_num)
    return output
\

# optimal solution using a deque to handle the current window operations
from collections import deque
def max_in_sliding_window(nums, w):
    n = len(nums)
    if not nums:
        return []
    
    if w > n:
        return [max(nums)]
    
    # Initialize an output array to store maximum values
    result = []
    current_window = deque()

    # Loop through the input array, maintaining a window of size w.
    for i in range(n):
        while current_window and current_window[0] < i - w + 1:
            current_window.popleft()

        while current_window and nums[current_window[-1]] < nums[i]:
            current_window.pop()

        # add current element to the back of the deque
        current_window.append(i)

        # front of deque is always the maximum of the window
        if i >= w - 1:
            result.append(nums[current_window[0]])
    return result 

# i = 0 current window = [0] result = []
# i = 1 current window = [0] result = []