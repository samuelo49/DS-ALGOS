"""
Sum all the elements in an array
[1,2,3,4] = 10
[-1,-2,-3] = - 6
[] = 0

"""

def sumAllElements(array):
    if not array:
        return 0
    totalSum = array[0]

    i = 0
    while i < len(array):
        if i == len(array):
            return totalSum
        return sumAllElements(array[i])
