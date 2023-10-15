"""
RemoveEveryOther Node
1->2->3->4->5
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


def removeEveryOther(head: Node):
    if head is None:
        return None
    current = head
    while current and current.next:
        current.next = current.next.next
        current = current.next
    return toString(head)


head1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
head2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
head3 = None
print(removeEveryOther(head1))
print(removeEveryOther(head2))
print(removeEveryOther(head3))
