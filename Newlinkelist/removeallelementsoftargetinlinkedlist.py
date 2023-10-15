"""
Q. Given a linked list and a target integer, remove all nodes with the value target.
Examples:
• Given a linked list: 4 ➞ 2 ➞ 3 ➞ 2 ➞ 2, target: 2 // returns 4 ➞ 3
• Given a linked list: 4, target: 4  // returns an empty list
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


# 0->4 ➞ 2 ➞ 3 ➞ 2 ➞ 2, target: 2 // returns 4 ➞ 3
def remove(node: ListNode, target: int) -> ListNode:
    sentinel = ListNode(0)
    sentinel.next = node
    current = sentinel
    while current.next is not None:
        if current.next.value == target:
            current.next = current.next.next
        else:
            current = current.next
    return sentinel.next


# Test Cases
LL1 = ListNode(4, ListNode(2, ListNode(1, ListNode(1, ListNode(3, ListNode(2, ListNode(2)))))))
LL2 = remove(None, 1)
print(arrayify(LL2))  # []
LL1 = remove(LL1, 1)
print(arrayify(LL1))  # [4, 2, 3, 2, 2]
LL1 = remove(LL1, 2)
print(arrayify(LL1))  # [4, 3]
remove(LL1, 3)
print(arrayify(LL1))  # [4]
LL1 = remove(LL1, 4)
print(arrayify(LL1))  # []
