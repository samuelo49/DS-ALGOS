"""
Q. Given an unsorted array, perform selection sort in ascending order.
Examples:
• Given an array: [1] // returns [1]
• Given an array: [3, 1, 2, 4] // returns [1, 2, 3, 4]

Solution:
    We set a current minimum as the first element in the input array
    we then move left to right and search for the smallest element
    if we find the element then we swap the element and the first element.
    we then move the currentminimum to the next element
"""


def selectionSort(array: [int]) -> [int]:
    for i in range(len(array)-1):
        minIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i],array[minIndex] = array[minIndex],array[i]
    return array
# Test Cases
print(selectionSort([]))  # []
print(selectionSort([1]))  # [1]
print(selectionSort([3, 1, 2, 4]))  # [1, 2, 3, 4]
print(selectionSort([-10, 1, 3, 8, -13, 32, 9, 5]))  # [-13, -10, 1, 3, 5, 8, 9, 32]
