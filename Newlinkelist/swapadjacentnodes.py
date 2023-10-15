"""
swap adjacent Nodes in a linked list

1->2->3->4  => 2->1->4->3
1->2->3->4->5  => 2->1->4->3->5
1 => 1
1->2->3 => 2->1->3

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


def swapAdjacentNodes(head: Node):
    sentinel = Node(0)
    sentinel.next = head
    current = head
    prev = sentinel

    while current and current.next:
        #1-2-3-4-5
        firstNode = current #1
        secondNode = current.next #2

        firstNode.next = secondNode.next #1-3
        secondNode.next = firstNode  #2-1

        prev.next = secondNode #0-2
        current = firstNode.next #3, 1-3
        prev = firstNode #prev = 1
    return toString(sentinel.next)


LL1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))

print(swapAdjacentNodes(LL1))
