"""
Given an array containing numbers, convert this to a singly linked list
and return the head of the list.
print(toString(arrayToLL([1,2])) == "1 -> 2")
print(toString(arrayToLL([1,2,3])) == "1 -> 2 -> 3")
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def toString(head: Node) -> None:
    if not head:
        return "<empty>"

    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next

    return " -> ".join(parts)


def arrayToLL(array):
    sentinel = Node(0)
    currentNode = sentinel

    for i in range(len(array)):
        currentNode.next = Node(array[i])
        currentNode = currentNode.next
    return toString(sentinel.next)

print(toString(arrayToLL([1,2,3])) == "1 -> 2 -> 3")


