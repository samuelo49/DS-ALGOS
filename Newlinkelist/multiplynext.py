"""
Given a linked list, multiply each node by the next nodes value, for the last node
multiply by itself.
1->2->3->4->5 => 2->6->12->20->25
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

def multiplyByEachOther(head:Node):
    if head is None:
        return None
    sentinel = Node(0)
    sentinel.next = head
    current = sentinel
    while current.next:
        current.val *= current.next.val
        current = current.next
    current.val *= current.val
    return toString(head)


head1 = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6))))))
head2 = Node(1,Node(2,Node(3,Node(4,Node(5)))))
print(multiplyByEachOther(head1))
print(multiplyByEachOther(head2))

