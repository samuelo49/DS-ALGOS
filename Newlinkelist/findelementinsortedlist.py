"""
Q. Given a sorted linked list of unique integers, check if the list
contains an element with a target value.
Examples:
• Given a linked list: 2 ➞ 3 ➞ 5, target: 2 // returns True
• Given a linked list: 2 ➞ 3 ➞ 5, target: 4  // returns False
"""

"""Iteratively"""


# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
#
#
# # 0->2 ➞ 3 ➞ 5
# def search(head: ListNode, target: int) -> bool:
#     sentinel = ListNode(0)
#     sentinel.next = head
#     current = sentinel
#     while current.next:
#         if current.next.value == target:
#             return True
#         else:
#             current = current.next
#     return False
#
#
# # Test Cases
# LL1 = ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(6, ListNode(7, ListNode(10)))))))
# print(search(None, 1))  # False
# print(search(LL1, 2))  # True
# print(search(LL1, 4))  # False
# print(search(LL1, -1))  # False
# print(search(LL1, 10))  # True
# print(search(LL1, 11))  # False

"""Recursively"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# 0->2 ➞ 3 ➞ 5
def search(head: ListNode, target: int) -> bool:
    if head is None:
        return False
    return head.value == target or search(head.next, target)


# Test Cases
LL1 = ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(6, ListNode(7, ListNode(10)))))))
print(search(None, 1))  # False
print(search(LL1, 2))  # True
print(search(LL1, 4))  # False
print(search(LL1, -1))  # False
print(search(LL1, 10))  # True
print(search(LL1, 11))  # False
