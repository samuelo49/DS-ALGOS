"""
Given an array, create a palindrome linked list by iterating through the array
forwards and backwards. The last element should not be repeated.

[] -> 0
[1] -> 1
[1,2]-> 121
[1,2,3] -> 12321
[1,2,2,3] 1223221
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def toString(head):
    if head is None:
        return "<empty>"
    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next
    return "->".join(parts)


def createPalindromeLL(array):
    if len(array) == 0:
        return None
    sentinel = Node(0)
    currentNode = sentinel
    for i in range(len(array)):
        currentNode.next = Node(array[i])
        currentNode = currentNode.next

    for i in range(len(array) - 2, -1, -1):
        currentNode.next = Node(array[i])
        currentNode = currentNode.next
    return toString(sentinel.next)


print(createPalindromeLL([]))
print(createPalindromeLL([1]))
print(createPalindromeLL([1, 2]))
print(createPalindromeLL([1, 2, 3]))
print(createPalindromeLL([1, 2, 3, 4]))
