"""
[1,2,3,4,5]
 Array operations
    - accessing element by index 0(1)
    - traversing an array 0(n)
    - appending 
    - insertion 0(n)
    - deletion 0(n)
    - searching in a sorted array 0(log n)
    - reverse
    - suming an array
    - sorting an array in place vs using sorted() to return a new array

Arrays uses
    - mostly used when storing or accessing elements in a sequential manner is required
    - creating other data strucutures like heap, graphs, stacks and queues

Related Array Topics
    - Two pointers
    - Searching 
    - sorting 
    - sliding window patterns

"""
def findElement(arr,k):
    if not arr:
        return False
    if k in arr:
        return True
    else:
        return False
arr1 = [1,2,3,4,5]
print(findElement(arr1, 1)) # time complexity -> 0(n), space complexity - 0(1)


def reverseArray(arr):
    return arr[::-1]
arr1 = [1,2,3,4,5]
print(reverseArray(arr1))

def sumArray(arr):
    if not arr:
        return 0
    return sum(arr)
arr1 = [1,2,3,4,5]
print(sumArray(arr1))

def sortArray(arr):
    arr.sort()
    return arr
arr1 = [6,2,8,4,5]
print(sortArray(arr1))

