"""
Given a linked list, return the second to last element's value.
1 -> 2 => 1

1 -> 2 -> 3 -> 4 => 3
     c    c    c
p    p    p
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def secondToLast(head: Node):
    if head is None or head.next is None:
        return None
    current = head
    while current.next.next:
        current = current.next
    return current.val


head = Node(1, Node(2))
print(secondToLast(head))
