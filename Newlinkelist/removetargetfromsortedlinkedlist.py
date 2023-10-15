"""
Q. Given a sorted linked list of unique integers, remove a node with the
target value from the list.
Examples:
• Given a linked list: -1 ➞ 1 ➞ 3 ➞ 4, target: 1 // returns -1 ➞ 3 ➞ 4
• Given a linked list: 5, target: 3 // returns 5
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


# 0-1 ➞ 1 ➞ 3 ➞ 4, target: 1 // returns -1 ➞ 3 ➞ 4
def remove(head: ListNode, target: int) -> ListNode:
    sentinel = ListNode(0)
    sentinel.next = head
    current = sentinel
    while current.next:
        if current.next.value == target:
            current.next = current.next.next
        else:
            current = current.next
    return sentinel.next


# Test Cases
LL1 = ListNode(-1, ListNode(1, ListNode(3, ListNode(4))))
print(arrayify(remove(LL1, 1)))  # [-1, 3, 4]
LL1 = remove(LL1, -1)  # Notice we expect this one to return a new head!
print(arrayify(LL1))  # [3, 4]
print(arrayify(remove(LL1, 4)))  # [3]
print(arrayify(remove(LL1, 5)))  # [3]
print(arrayify(remove(ListNode(1), 1)))  # []

"""Recursively"""


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


# 1 ➞ 1 ➞ 3 ➞ 4, target: 1 // returns -1 ➞ 3 ➞ 4
def remove(head: ListNode, target: int) -> ListNode:
    if head is None:
        return None
    elif head.value == target:
        return head.next
    else:
        head.next = remove(head.next,target)
        return head




# Test Cases
LL1 = ListNode(-1, ListNode(1, ListNode(3, ListNode(4))))
print(arrayify(remove(LL1, 1)))  # [-1, 3, 4]
LL1 = remove(LL1, -1)  # Notice we expect this one to return a new head!
print(arrayify(LL1))  # [3, 4]
print(arrayify(remove(LL1, 4)))  # [3]
print(arrayify(remove(LL1, 5)))  # [3]
print(arrayify(remove(ListNode(1), 1)))  # []
