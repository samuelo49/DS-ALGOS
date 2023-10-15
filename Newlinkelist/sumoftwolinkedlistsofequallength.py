"""
Q. Given two linked lists of equal length, sum elements' value
at the same position.
Examples:
• Given two linked lists: 1 ➞ 3 ➞ 5 and -1 ➞ 3 ➞ -10 // returns 0 ➞ 6 ➞ -5
• Given two linked lists: 0 and 0 // returns 0
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


def sumTwoLL(head1: ListNode, head2: ListNode) -> ListNode:
    if head1 is None and head2 is None:
        return None
    node1 = head1
    node2 = head2
    while node1 or node2:
        node2.value += node1.value
        node1 = node1.next
        node2 = node2.next
    return head2


# Test Cases
LL1 = ListNode(1, ListNode(3, ListNode(5)))
LL2 = ListNode(-1, ListNode(3, ListNode(-10)))
print(arrayify(sumTwoLL(LL1, LL2)))  # [0, 6, -5]
print(arrayify(sumTwoLL(ListNode(0), ListNode(0))))  # [0]
print(sumTwoLL(None, None))  # None

