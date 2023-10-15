"""
Given an array of integers, return a sub-array of 'Left Peaks'.
A Left Peak is defined as an element that is greater or equal in
value to all elements to its right.
find_left_peaks([1, 2, 5, 3, 1, 2]) => [5, 3, 2]
[1]
find_left_peaks([3, 2, 1]) => [3, 2, 1]
"""


def find_left_peaks(arr):
    if not arr:
        return []
    stack = []
    for i in range(len(arr)):
        while stack and stack[-1] < arr[i]:
            stack.pop()
        stack.append(arr[i])
    return stack


print(find_left_peaks([1, 2, 5, 3, 1, 2]))
print(find_left_peaks([1, 2, 5, 3, 6, 2]))
