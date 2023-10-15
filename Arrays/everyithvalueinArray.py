"""
Given an array and a number X, return an array containing every *X*th number
 in the input array.
"""


def everyXth(array, x):
    newArray = []
    for i in range(len(array)):
        if array[i] % x == 0:
            newArray.append(array[i])
    return newArray


print(everyXth([1, 2, 3, 4, 5, 6], 2))
