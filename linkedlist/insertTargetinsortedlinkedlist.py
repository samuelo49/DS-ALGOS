"""
Q. Given a sorted linked list, insert an element in the appropriate position.
Examples:

• Given a linked list: 1 ➞ 3 ➞ 4, target: 2 // returns 1 ➞ 2 ➞ 3 ➞ 4
• Given an empty linked list, target: 1  // returns 1
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def arrayify(head):
    array = []
    ptr = head
    while ptr is not None:
        array.append(ptr.value)
        ptr = ptr.next
    return array


def insert(head, target):
    if head is None:
        return ListNode(target)

    sentinel = ListNode(0)
    sentinel.next = head
    currentNode = sentinel
    while currentNode:
        if not currentNode.next or target < currentNode.next.value:
            temp = currentNode.next
            currentNode.next = ListNode(target)
            currentNode.next.next = temp
            break
        currentNode = currentNode.next
    return sentinel.next


# Test Cases
LL1 = ListNode(1, ListNode(3, ListNode(4)))
LL2 = ListNode(-3, ListNode(-2, ListNode(-1)))
print(arrayify(insert(LL1, 2)))  # [1, 2, 3, 4]
print(arrayify(insert(LL2, -4)))  # [-4, -3, -2, -1]
print(arrayify(insert(LL2, 0)))  # [-3, -2, -1, 0]
print(arrayify(insert(None, 1)))  # [1]
