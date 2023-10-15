"""
Given an array, rotate the array to the right by k steps,
where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Explanation to rotate Left: [1,2,3,4],3
rotate 1 steps to the left: [2,3,4,1]
rotate 2 steps to the right: [3,4,1,2]
rotate 3 steps to the right: [4,1,2,3]
"""


def reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


# def rotateRight(nums, k):
#     n = len(nums)
#     k = k % n
#     reverse(nums, 0, n - 1)
#     reverse(nums, 0, k - 1)
#     reverse(nums, k, n - 1)
#     return nums

def rotateLeft(nums,k):
    n = len(nums)
    k =  k % n
    reverse(nums,0,n-1)
    reverse(nums,0,n-1-k)
    reverse(nums,n-k, n-1)
    return nums



# print(rotateRight([1, 2, 3, 4, 5, 6, 7], 3))
print(rotateLeft([1,2,3,4], 3))
