"""
goldilockFlapjacks([2, -1]) => [true, 2]
goldilockFlapjacks([-1, 2]) => [false, 1]
goldilockFlapjacks([2, -1, 3, -3, 2, -1]) => [true, 4]
len(Stack) > 4 => false
len(Stack) < 0 => false
maxSum ==> max(currentSum,maxSum)
"""


def goldIlockFlapjacks(pancakes):
    isValid = True
    maxSum = 0
    currentSum = 0
    for i in range(len(pancakes)):
        currentSum += pancakes[i]
        if currentSum <= 0:
            isValid = False
        maxSum = max(currentSum, maxSum)
        if maxSum > 4:
            isValid = False
    return [isValid, maxSum]


print(goldIlockFlapjacks([2, -1, 3, -3, 2, -1]))
print(goldIlockFlapjacks([-1, 2]))
print(goldIlockFlapjacks([2, -1]))
