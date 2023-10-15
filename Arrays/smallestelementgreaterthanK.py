"""
Given a list, write a Python program to find the smallest number which is greater than a specific element K.
# Initializing list
test_list = [1, 4, 7, 5, 10]
 
# Initializing k
k = 6
"""
def smallestNumberGreaterThanK(lst, k):
    smallestNumber = min(num for num in lst if num > k)
    return smallestNumber
test_list = [1, 4, 7, 5, 10]
k = 6
print(smallestNumberGreaterThanK(test_list, 6))