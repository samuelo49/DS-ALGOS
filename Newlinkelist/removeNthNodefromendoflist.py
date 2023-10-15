"""
Remove the nth node from the end of a linked list. n is 1-indexed.
Assume n will always be smaller or equal to the length of the linked list.

1->2->3->4->5->6, 2  => 1->2->3->4->6

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


def removeNthNode(head, n):
    if head is None:
        return None
    slow = head
    fast = head
    prev = slow
    for i in range(0, n):
        if fast is not None:
            fast = fast.next
        else:
            return -1
    while fast is not None:
        prev = slow
        fast = fast.next
        slow = slow.next
    prev.next = slow.next
    return toString(head)


head1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(removeNthNode(head1, 2))
