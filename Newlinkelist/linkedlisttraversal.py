"""
Node class
How to traverse a linkedlist

1->2->3->4->5
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def traverseList(head: Node):
    if head is None:
        return None

    current = head
    while current and current.next:
        print(current.val,end="->")
        current = current.next
    

head = Node(1,Node(2,Node(3,Node(4,Node(5)))))
print(traverseList(head))