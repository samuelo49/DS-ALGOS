"""
Detect cycle in linked list [3,2,0,-4]
"""


class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def hasCycle(head):
    if head is None:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


LL1 = Node()
print(hasCycle([3, 2, 0, -4]))
