"""
Monotonic increasing stack - the elements are increasing in order
e.g [1, 3, 10, 15, 17]
"""
def monotonic_increasing_stack(lst):
    if not lst:
        return []
    stack = []
    for num in lst:
        while stack and stack[-1] >= num:
            stack.pop()
        stack.append(num)
    return stack 
            
print(monotonic_increasing_stack([1, 4, 5, 3, 12, 10]))
# time complexity 0(n)
# space complexity 0(n)