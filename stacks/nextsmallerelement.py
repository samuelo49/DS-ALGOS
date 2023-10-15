"""
Monotonic stack application 
    - Next Smaller Element : This essentially means find the first value on the right smaller than the element

Given an array, print the Next Smaller Element (NGE) for every element. 

The Next smaller Element for an element x is the first smaller element on the right side of x in the array. 
Elements for which no smaller element exist, consider the next smaller element as -1. 
                             i
Input: arr[] = [ 4 , 5 , 2 , 25 ]
Output: 4 -> 2 
        5 -> 2 
        2 -> -1 
        25 -> -1   

"""
def next_smaller_element(lst):
    result = [-1] *  len(lst)
    stack = []

    for i in range(len(lst)):
        while stack and lst[stack[-1]] > lst[i]:
            result[stack.pop()] = lst[i]
        stack.append(i)
    return result
print(next_smaller_element([ 4 , 5 , 2 , 25 ]))
# time complexity 0(n)
# space complexity 0(n)