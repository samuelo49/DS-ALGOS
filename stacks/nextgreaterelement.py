"""
Monotonic stack application 
    - Next Greater Element : This essentially means find the first value on the right greater than the element

Given an array, print the Next Greater Element (NGE) for every element. 

The Next greater Element for an element x is the first greater element on the right side of x in the array. 
Elements for which no greater element exist, consider the next greater element as -1. 
                             i
Input: arr[] = [ 4 , 5 , 2 , 25 ]
Output: 4 -> 5 
        5 -> 25 
        2 -> 25 
        25 -> -1   

"""
def next_greater_element(lst):
    result = [-1] * len(lst)
    stack = []

    for i in range(len(lst)):
        while stack and lst[stack[-1]] < lst[i]:
            result[stack.pop()] = lst[i]
        stack.append(i)
    return result
test_list = [ 4 , 5 , 2 , 25 ]
print(next_greater_element(test_list))