"""
Q. Given an array of positive integers, find the first element that occurs k number of times. If no element occurs k times, return -1, and you may assume k is greater than 0.

Examples:
• Given an array: [1, 2, 2, 3, 3], k: 2 // returns 2
• Given an array: [], k: 1 // returns -1
"""


def firstKTimes(input, k):
    countElements = {}
    for num in input:
        if num not in countElements:
            countElements[num] = 1
        else:
            countElements[num] += 1

    for num, count in countElements.items():
        if count == k:
            return num
    return -1


# Test Cases
print(firstKTimes([1, 2, 2, 3, 3], 2))  # 2
print(firstKTimes([1, 2, 2, 3, 3], 3))  # -1
print(firstKTimes([], 1))  # -1
