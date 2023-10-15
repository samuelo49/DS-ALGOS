"""
Given a linked list and a target k, return a linked list containing every kth
element in the list.
# 1 -> 3 -> 6 -> 2 -> 8 -> 9
 s

"""


class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next


def toString(head):
    if head is None:
        return "<empty>"
    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next
    return "->".join(parts)


def everyKthNode(node, target):
    currentNode = node
    sentinel = Node(0)
    newNode = sentinel

    while currentNode is not None:
        for i in range(1, target):
            if currentNode is None:
                return sentinel.next
            currentNode = currentNode.next
        newNode.next = Node(currentNode.val)
        newNode = newNode.next

        currentNode = currentNode.next
    return toString(sentinel.next)

head = Node(1, Node(3, Node(6, Node(2, Node(8, Node(9))))))
print(everyKthNode(head, 3))
