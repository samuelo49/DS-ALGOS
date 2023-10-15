"""
Arrays
    - how do we search?
    - how do we sort?
    - how do we insert?
    - how do we delete?
    - how do we merge?
    - how do we traverse?
    - how do we reverse?
    - how do we rotate?
    - how do we find the max and min?
    - how do we find the median?
    - how do we find the mean?
    - how do we find the mode?
    - how do we find the range?
    - how do we find the sum?
    - how do we find the product?
    - how do we find the difference?


    array = [1, 2, 3, 4, 5]
"""

# def searchArray(arr, x):
#     return x if x in arr else -1
# print(searchArray([1, 2, 3, 4, 5], 3)) #  3
# print(searchArray([1, 2, 3, 4, 5], 10)) # -1

# def sortArray(arr):
#     return sorted(arr)
# print(sortArray([10, 2, 15, 4, 5])) # [1, 2, 3, 4, 5] # O(nlogn) explain how it works

# def insertArray(arr, x):
#     return arr.append(x)
# print(insertArray([1, 2, 3, 4, 5], 10)) # [1, 2, 3, 4, 5, 10]

# def mergeArrays(arr1,arr2):
#     return sorted(arr1 + arr2)
# print(mergeArrays([1, 2, 3, 4, 5], [10, 2, 15, 4, 5])) # [1, 2, 2, 3, 4, 4, 5, 5, 10, 15] 

# def reverseArray(arr):
#     i ,j = 0, len(arr) - 1 
#     while i < j:
#         arr[i], arr[j] = arr[j], arr[i]
#         i += 1
#         j -= 1
#     return arr
# print(reverseArray([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
        
# def rotateleft(arr, k):
#     """
#      when rotating left you essentially want the front k elements to moved to the back
#      and you want the back n - k elements to move to the front
#     """
#     k = k % len(arr)
#     return arr[k:] + arr[:k]
# print(rotateleft([1, 2, 3, 4, 5], 2)) # [3, 4, 5, 1, 2] #

# def rotateright(arr,k):
#     """
#     when rotating right you essentially want the back k elements to the front
#     and the front n -k elements to the back
#     """
#     k = k % len(arr)
#     backelements = arr[-k:]
#     frontelements = arr[:-k]
#     return  backelements + frontelements
# print(rotateright([1, 2, 3, 4, 5], 2)) # [4, 5, 1, 2, 3] #

# dictionary with elements as keys and their frequency as values
# d = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}

# def sortedFunction(arr):
#     """
#     sorted function takes in an iterable and returns a sorted list
#     d = {1: 10,
#           2: 5, 
#           3: 2, 
#           4: 78, 
#           5: 50}
#     """
#     sorted_dict = sorted(arr.items(), key = lambda x : x[1], reverse=False) 
#     return sorted_dict
# print(sortedFunction({1: 10, 2: 5, 3: 2, 4: 78, 5: 50})) # [(4, 78), (5, 50), (1, 10), (2, 5), (3, 2)]

# def findMax(arr):
#     return max(arr)
# print(findMax([1, 2, 3, 4, 5])) # 5

# def findMin(arr):
#     return min(arr)
# print(findMin([1, 2, 3, 4, 5])) # 1

# def findProduct(arr):
#     product = 1
#     for num in arr:
#         product *= num
#     return product

# print(findProduct([1, 2, 3, 4, 5])) # 120

# def compareTwoArrays(arr1,arr2):
#     return set(arr1) == set(arr2)
# print(compareTwoArrays([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])) # True
