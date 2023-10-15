"""
Given an array, return the first element is repeated if you were to
 traverse the array from left to right.
 [1, 2, 3, 2, 1, 1]  --> 2
"""


def firstRepeatedElement(array):
    nonDuplicates = set()
    for num in array:
        if num in nonDuplicates:
            return num
        nonDuplicates.add(num)

    return False

print(firstRepeatedElement([1, 2, 3, 2, 1, 1]))