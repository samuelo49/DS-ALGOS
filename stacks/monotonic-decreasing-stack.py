"""
Monotonic decareasing stack - where elements are decreasing in order
e.g 17, 14, 10, 5, 1

"""
def monotonic_decreasing_stack(lst):
    stack = []
    for num in lst:
        while stack and stack[-1] <= num:
            stack.pop()
        stack.append(num)
    return stack

print(monotonic_decreasing_stack([15, 17, 12, 13, 14, 10]))
# time complexity 0(n)
# space complexity 0(n)