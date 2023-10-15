"""
Create a cycle in a linked list.
"""


class Node:
    def __init__(self, val=0, next=None):
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


def createCycle(head: Node):
    if head is None:
        return None
    sentinel = Node(0)
    sentinel.next = head
    current = sentinel
    while current.next:
        current = current.next
    current.next = sentinel.next
    return toString(sentinel.next)


head1 = Node(1,Node(2,Node(3)))
print(createCycle(head1))
