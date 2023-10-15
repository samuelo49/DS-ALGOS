"""
Q. Given a sorted array of unique positive integers and a target integer, check if the array contains a target using binary search and return its index. If the array does not contain the target, return -1.
Note:
• Indexes (indices) follow the zero-based numbering rule (i.e. the index of the first element of an array is 0, not 1).

Examples:
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 1 // returns 0
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 200 // returns 8
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 154 // returns -1

used for searching in a sorted array. 0(logn)
"""


def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        # ignore right half
        if target < array[mid]:
            right = mid - 1
        
        # ignore left half
        elif target > array[mid]:
            left = mid + 1
        
        # else target it at mid
        else:
            return mid
    return -1

# Test Cases
array = [1, 2, 3, 6, 8, 13, 113, 153, 200]
print(binarySearch(array, 1))  # 0
print(binarySearch(array, 200))  # 8
print(binarySearch(array, 8))  # 4
print(binarySearch(array, 154))  # -1
