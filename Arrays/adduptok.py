"""
Pair that sums up to K
[1, 5, 8, 10, 13, 18], k = 15 => true
"""


def sumToK(array, k):
    left = 0
    right = len(array) - 1
    while left <= right:
        currentSum = array[left] + array[right]
        if currentSum < k:
            left += 1
        elif currentSum > k:
            right -= 1
        else:
            return True
    return False

print(sumToK([1, 5, 8, 10, 13, 18], 15))


