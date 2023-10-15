"""
Q. Given an unsorted array, perform bubble sort in ascending order.

Examples:
• Given an array: [1] // returns [1]
• Given an array: [3, 1, 2, 4] // returns [1, 2, 3, 4]
"""

def bubbleSort(array):
    for i in range(1,len(array)):
        for j in range(0,len(array)-1):
            if array[j] > array[j + 1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array



# Test Cases
print(bubbleSort([])) # []
print(bubbleSort([1])) # [1]
print(bubbleSort([3, 1, 2, 4])) # [1, 2, 3, 4]
print(bubbleSort([-10, 1, 3, 8, -13, 32, 9, 5])) # [-13, -10, 1, 3, 5, 8, 9, 32]