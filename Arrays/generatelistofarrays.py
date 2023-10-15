"""
Given a target integer X, iterate from 1 to X and return a matrix sequence where
each array starts with 1 and goes up to the current iteration.
Each iteration should increment the array size and values until it reaches X.
"""


def generateSequence(target):
    matrix = []

    for i in range(1, target + 1):
        arr = []
        for val in range(1, i + 1):
            arr.append(val)

        matrix.append(arr)
    return matrix


print(generateSequence(2))
