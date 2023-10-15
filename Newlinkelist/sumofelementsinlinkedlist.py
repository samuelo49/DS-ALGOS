"""
sum all the values in the linked list
1->2->3->4->5 => 15
"""

"""Iteratively"""


# class Node:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#
#
# def sumElements(head):
#     if head is None:
#         return None
#
#     # current = head
#     total = 0
#     while head:
#         total += head.val
#         head = head.next
#     return total
#
#
# LL1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
# LL2 = 0
# print(sumElements(LL1))
# print(sumElements(LL2))

"""Recursively"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def sumElements(head):
    if head is None:
        return 0
    return head.val + sumElements(head.next)

LL1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
LL2 = 0
print(sumElements(LL1))

