"""
Q. Given an unsorted array, perform merge sort in ascending order.
Examples:
• Given an array: [1] // returns [1]
• Given an array: [3, 1, 2, 4] // returns [1, 2, 3, 4]
"""
from typing import List, Any


def mergeSort(array):
    if len(array) <= 1:
        return array

    firstHalf = array[:len(array) // 2]
    secondHalf = array[len(array) // 2:]
    firstHalf = mergeSort(firstHalf)
    secondHalf = mergeSort(secondHalf)

    return mergeHelper(firstHalf, secondHalf)


def mergeHelper(array1, array2):
    array3 = []
    i = j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array3.append(array1[i])
            i += 1
        else:
            array3.append(array2[j])
            j += 1
    if i == len(array1):
        array3 += array2[j:]
    else:
        array3 += array1[i:]
    return array3


# Test Cases
print(mergeSort([]))  # []
print(mergeSort([1]))  # [1]
print(mergeSort([3, 1, 2, 4]))  # [1, 2, 3, 4]
print(mergeSort([-10, 1, 3, 8, -13, 32, 9, 5]))  # [-13, -10, 1, 3, 5, 8, 9, 32]
