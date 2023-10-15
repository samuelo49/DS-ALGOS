"""
Q. Given an unsorted array, return the number of unique elements that appear only once in the array.
Examples:
• Given an array: [3, 1, 1, 2, 3, 1, 1, 1, 4] // returns 2 (unique elements: 2 and 4)
• Given an array: [1] // returns 1 (unique element: 1)
"""


def numUniques(array) -> int:
    countUnique = {}
    countOnce = 0
    for num in array:
        countUnique[num] = 1 + countUnique.get(num, 0)

    for count in countUnique.values():
        if count == 1:
            countOnce += 1
    return countOnce


print(numUniques([]))  # 0

print(numUniques([3, 1, 1, 2, 3, 1, 1, 1, 4]))  # 2

print(numUniques([1]))  # 1
