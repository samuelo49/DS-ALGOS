"""
Given a linked list, swap the head (first element) and the
tail (last element) of the linked list, and return the new head.
nput: [1,2,3,4,5,6]
Output: [6,2,3,4,5,1]
 1   2  3    4    5    6
 lc  lc  lc  lc   lc
 1
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

def swapHeadAndTailLinkedList(head):
    if head is None:
        return None
    sentinel = Node(0)
    sentinel.next = head
    current = sentinel
    headNode = sentinel
    firstNode = head
    prev = None
    while current.next:
        prev = current
        current = current.next
    prev.next = firstNode
    current.next = firstNode.next
    firstNode.next = None
    headNode.next = current
    return toString(sentinel.next)

head1 = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6))))))
print(swapHeadAndTailLinkedList(head1))
