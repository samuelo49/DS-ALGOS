'''
Given a singly linked list, remove the nth node from the end of the list and return
its head.
Example 1
    llist = 1->2->3->4->5
    n = 3
    
    output: 1->2->4->5, we remove the node=3 since that would the nth node from the end of the list.

Example 2:
    llist = 1->3
    n = 4
    output: 1->3, since n is greater than the number of nodes in the list

Plan
- Use slow and fast pointer essentially acting like the two pointer solution

'''
class ListNode:
    def __init__(self, val= 0,  next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head,n):

    # handle edge cases, empty
    if not head:
        return -1
    # create dummy node to handle any edge cases
    dummy = ListNode(0)
    dummy.next = head

    # Initialize two pointers, slow and fast
    slow = dummy
    fast = dummy 

    # Move the fast pointer n + 1 steps a head
    for _ in range(n + 1):
        if fast is None:
            return "Error: n is greater than the number of nodes we have"
        fast = fast.next
    
    #Move both pointers together until fast reaches end
    while fast:
        fast = fast.next
        slow = slow.next
    
    # Now when fast reaches end, remove the  nth node by updating next pointer of the node before it
    slow.next = slow.next.next

    return dummy.next 


def print_list(node):
    while node is not None:
        print(node.val, end=" ")
        node = node.next
    print()

# Test case 1: Normal case
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
print("Before removing: ", end="")
print_list(head)
head = removeNthFromEnd(head, n)
print(f"After removing {n}th node from end: ", end="")
print_list(head)

# Test case 2: Removing the first node
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 5
print("Before removing: ", end="")
print_list(head)
head = removeNthFromEnd(head, n)
print(f"After removing {n}th node from end: ", end="")
print_list(head)

# Test case 3: Removing the last node
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 1
print("Before removing: ", end="")
print_list(head)
head = removeNthFromEnd(head, n)
print(f"After removing {n}th node from end: ", end="")
print_list(head)

# Test case 4: n is greater than the number of nodes
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 6
print("Before removing: ", end="")
print_list(head)
result = removeNthFromEnd(head, n)
print(f"Result when n is greater than the number of nodes: {result}")

# Test case 5: The list is empty
head = None
n = 1
result = removeNthFromEnd(head, n)
print(f"Result when the list is empty: {result}")