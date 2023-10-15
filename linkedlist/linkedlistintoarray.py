"""
Given a linked list, return an array with all the elements in reverse.
1 -> 3 -> 5 -> 2
let head = new Node(1, new Node(3, new Node(5, new Node(2))))

"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def toString(head):
#     if head is None:
#         return "<empty>"
#     parts = []
#     while head:
#         parts.append(head.val)
#         head = head.next
#     return "->".join(parts)


def createLLInReverse(node):
    tempArray = []
    while node:
        tempArray.append(node.val)
        node = node.next
    i = 0
    j = len(tempArray) - 1
    while i < j:
        tempArray[i],tempArray[j] = tempArray[j],tempArray[i]
        i += 1
        j -= 1
    return tempArray

head = Node(1, Node(3, Node(5, Node(2))))
print(createLLInReverse(head))
