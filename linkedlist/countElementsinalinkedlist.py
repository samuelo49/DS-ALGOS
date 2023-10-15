"""
Given an unsorted linked list, count the number of elements (iteratively or recursively).

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 // returns 3
• Given a linked list: 0 // returns 1
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def count(node: ListNode) -> int:
    # length = 0
    # while node:
    #     node = node.next
    #     length += 1
    # return length

    if node is None:
        return 0
    else:
        return 1 + count(node.next)


# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count(None))  # 0
print(count(LL1))  # 3
print(count(ListNode()))  # 1
