"""
Given two arrays of equal length, return an array summing them
together with the second array being traversed in reverse.
array1 = [1, 2, 3]
array2 = [4, 6, 10]
result = [11, 8, 7]

array1 = [1, 5, 10, 12]
array2 = [2, 4, 3, 5]
result = [6, 8, 14, 14]
"""


def sumInReverse(array1, array2):
    result = []
    i = 0
    j = len(array2) - 1
    while i < len(array1):
        result.append(array1[i] + array2[j])
        i += 1
        j -= 1
    return result
print(sumInReverse([1, 2, 3], [4, 6, 10]))
