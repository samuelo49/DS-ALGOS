"""
Given the head of a sorted linked list, delete all duplicates such
that each element appears only once. Return the linked list sorted as well.
Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def toString(head: ListNode):
    if not head:
        return "<empty>"
    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next

    return "->".join(parts)


def removeDuplicates(head: ListNode):
    curr = head
    while curr and curr.next:
        if curr.next.val == curr.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return toString(head)


head1 = ListNode(1, ListNode(1, ListNode(2)))
print(removeDuplicates(head1))
