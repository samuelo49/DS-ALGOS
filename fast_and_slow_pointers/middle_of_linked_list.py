'''
Given the head of a singly linked list, return the middle node of the linked list.
If the number of the nodes in the linked list is even, there will be two middle nodes,
so return the second one.

Plan

head = 1->2->3->4->5
OUTPUT: 3 since it is the middle node

head = 1->2->3->4->5->6
OUTPUT : 4 since the list is even
'''
class LinkedListNode:
    def ___init__(self,val, next=None):
        self.val = val
        self.next = next 

def findMiddle(head:LinkedListNode):
    if head is None:
        return False
    
    slow = head
    fast = head 
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
    