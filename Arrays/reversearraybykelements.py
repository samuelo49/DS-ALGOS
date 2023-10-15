"""
Given an array, reverse every sub-array formed by consecutive k elements.
Input:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 3
Output:
[3, 2, 1, 6, 5, 4, 9, 8, 7]
"""


def reverse(arr, k):
    if not arr or len(arr) <= 1 or k < 1:
        return

    def swap(arr, start, end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    i = 0
    while i < len(arr):
        end = min(i + k, len(arr))
        swap(arr, i, end - 1)
        i = end
    return arr


print(reverse([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
