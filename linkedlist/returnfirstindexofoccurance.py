"""
Given a linked list and a target value, return the index of the first occurrence of
that value in the linked list. The index should be zero-indexed.
[1,2,3,4,5,6],9== -1
[1,2,3,4,5,6],2== 1
[] == None
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def firstIndexInLL(node:Node, target):
    if not node:
        return None
    index = 0
    while node:
        if node.val == target:
            return index
        index += 1
        node = node.next
    return -1


first = Node(1)
second = Node(2)
first.next = second
third = Node(3)
second.next = third
fourth = Node(4)
third.next = fourth
fifth = Node(5)
fourth.next = fifth
sixth = Node(6)
fifth.next = sixth

print(firstIndexInLL(first, 9))#-1
print(firstIndexInLL(first, 2))#1
print(firstIndexInLL(first, 6))#5

