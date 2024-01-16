'''
Check whether or not a linked list list contains a cycle. If a cycle exist, return TRUE.
Otherwise, return FALSE. The cycle means that at least one node can be reached again by
traversing the next pointer

Plan
========
head_1 = 2->4->6->8->10->4
OUTPUT: True, because we can reach node with value of 4 by traversing next after the node
with value of 10.

head_1 = 1->2->3->4->5
OUTPUT: False, because we can't reach a node we already traversed with this list
'''
class LinkedListNode:
    def ___init__(self,val, next=None):
        self.val = val
        self.next = next 

def detect_cycle(head:LinkedListNode):
    if head is None:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


