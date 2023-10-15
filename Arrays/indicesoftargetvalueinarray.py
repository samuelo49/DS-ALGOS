"""
Given an array and a target value X,
return an array of all indices containing value X.
print(indicesOfTarget([30,30,30], 30) == [0,1,2])
print(indicesOfTarget([3, 2, 5, 5, 1], 5) == [2,3])
"""


def indicesOfTarget(input, target):
    result = []
    for i in range(len(input)):
        if input[i] == target:
            result.append(i)
    return result
print(indicesOfTarget([30,30,30], 30))
print(indicesOfTarget([3, 2, 5, 5, 1], 5))
print(indicesOfTarget([], 5))
print(indicesOfTarget([3, 2,3,4], 5))
