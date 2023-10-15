"""
 how to use arrays to rearrange elements
 - rearrange array into even and odd numbers [1,3,4,2,7,8 ]
 - rearrange array into positive and negative  numbers [-1,8,-4,-5,2]
 - rearrange array into letters and numbers? [1,a,c,3,b,2]
 - rearrange array into 1's and 0's [0,1,0,1,1,0,0]
"""

# def ArrayoddEven(arr):
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         while left < right and arr[left] % 2 != 0:
#             left += 1        
#         while left < right and arr[right] % 2 == 0:
#             right -= 1
#         if left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1
#     return arr
# print(ArrayoddEven([1,3,4,2,7,8 ])) 


# def negativePositive(arr):
#     pivot = 0
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         while left < right and  arr[left] < pivot:
#             left += 1
#         while left < right and  arr[right] >=  pivot:
#             right -= 1
#         if left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1
#     return arr

# print(negativePositive([-1,8,-4,-5,2]))

def lettersNumbers(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        while left < right and arr[left].isalpha():
            left += 1
        while left < right and arr[right].isdigit():
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

print(lettersNumbers([1,'a','c',3,'b',2]))


def zeroOnes(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        while left < right and arr[left] == 0:
            left += 1
        while left < right and arr[right] == 1:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr
print(zeroOnes([0,1,0,1,1,0,0]))