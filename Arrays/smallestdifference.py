"""
Write a function that takes in two non-empty arrays of integers, finds the pair of numbers(one
from each array) whose absolute difference is closet to Zero, and returns an array containing these
two numbers, with the number from the first array in the first position.

Note that the absolute of two integers is the distance between them on the real number
line.For example,the absolute difference of -5 and 5 is 10, and the absolute difference
of -5 and -4 is 1.
You can assume that there will only be one pair of numbers with the smallest difference.
arrayOne = [-1,5,10,20,28,3]
arrayTwo = [26,134,135,15,7]

sample output = [28,26]

[-1,3,5,10,20,28]
[7,15,26,134,135]
"""


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallestDiff = float("inf")
    currentDifference = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            currentDifference = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            currentDifference = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallestDiff > currentDifference:
            smallestDiff = currentDifference
            smallestPair = [firstNum, secondNum]
    return smallestPair

print(smallestDifference([-1,5,10,20,28,3], [26,134,135,15,7]))