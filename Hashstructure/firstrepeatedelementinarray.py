"""
Given an array, return the first element is repeated
if you were to traverse the array from left to right.
[1, 2, 3, 2, 1, 1]) == 2
"""


def firstRepeatedElement(input):
    seen = set()
    for num in input:
        if num in seen:
            return num
        seen.add(num)
    return -1

print(firstRepeatedElement([1, 1, 3, 2, 1, 1]))
