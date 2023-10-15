"""
Q. Reverse a given linked list.
Examples:
• Given a linked list: 13 ➞ 1 ➞ 5 ➞ 3 ➞ 7 ➞ 10 // returns 10 ➞ 7 ➞ 3 ➞ 5 ➞ 1 ➞ 13
• Given a linked list: 1 // returns 1
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array


#        p  c  cc
# #         13 ➞ 1 ➞ 5 ➞ 3 ➞ 7 ➞ 10 // returns 10 ➞ 7 ➞ 3 ➞ 5 ➞ 1 ➞ 13
# # prev <- 13 <-1
def reverse(head: ListNode) -> ListNode:
    if head is None: return None
    curr = head
    following = head
    prev = None
    while curr:
        following = following.next
        curr.next = prev
        prev = curr
        curr = following
    return prev


# Test Cases
LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))
print(arrayify(reverse(ListNode(1))))  # [1]
print(arrayify(reverse(ListNode(1, ListNode(2)))))  # [2, 1]
print(arrayify(reverse(LL1)))  # [10, 7, 3, 5, 1, 13]
print(reverse(None))  # None

