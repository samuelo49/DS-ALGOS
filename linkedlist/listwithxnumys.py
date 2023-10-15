"""
Given integers X and Y, return the head of a linked list
 with X nodes with value Y.
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def toString(head: Node):
    if not head:
        return "<empty>"
    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next

    return "->".join(parts)


def createLL(count, value):
    if count == 0:
        return 0
    sentinel = Node(0)
    current = sentinel
    while count > 0:
        current.next = Node(str(value))
        current = current.next
        count -= 1
    return toString(sentinel.next)


print(createLL(5, 10))
