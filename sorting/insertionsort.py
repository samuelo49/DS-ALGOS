"""
Q. Given an unsorted array, perform insertion sort in ascending order.

Examples:
• Given an array: [1] // returns [1]
• Given an array: [3, 1, 2, 4] // returns [1, 2, 3, 4]

"""

def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array

# Test Cases
print(insertionSort([]))  # []
print(insertionSort([1]))  # [1]
print(insertionSort([3, 1, 2, 4]))  # [1, 2, 3, 4]
print(insertionSort([-10, 1, 3, 8, -13, 32, 9, 5]))  # [-13, -10, 1, 3, 5, 8, 9, 32]
