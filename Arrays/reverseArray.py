"""
Reverse an Array without using any built in functions
- using the two pointer solution
"""


def reverseArray(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return array

print(reverseArray([1, 2, 3, 4, 5,8]))