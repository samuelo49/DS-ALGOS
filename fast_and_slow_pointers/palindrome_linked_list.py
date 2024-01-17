'''
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

Input: head = [1,2,2,1]
               12,12
Output: true

Input: head = [1,2]
Output: false
Plan
- Overall plan is to split the list in two halves and compare the halves
- however the second half would need to be reversed so can check for a palindrome by 
    comparing it with the first half.
- we need to find the mid point, so from the head -> mid point(first half )
- we then need to reverse the second half(starting from the mid.next position to end of the list)
- then we can loop through the those two halves and compare them to see if they are the same
- Main things to do
    - find linked list mid point
    - reverse a linkedlist
    
'''
class LinkeListNode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
def isPalindrome(head):
    # find the end of the first half and reverse the second hal
    first_half_end = end_of_first_half(head)
    second_half_start = reverse_linked_list(first_half_end.next)

    # check if linked list is palindrome
    result = True 
    first_position = head
    second_position = second_half_start

    while result and second_half_start is not None:
        if first_position.data != second_position.data:
            return False
        first_position = first_position.next 
        second_position = second_position.next
    # restore list and return result
    first_half_end.next = reverse_linked_list(second_half_start)
    return result


# find linkedlist mid point so we can know where the second half starts
def end_of_first_half(head):
    if head is None:
        return None
    slow = head
    fast = head 
    while fast and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow 
# reverse a linked list so we can simulate a state for comparing the two halves to dictate a palindrome
def reverse_linked_list(head):
    if head is None:
        return None
    prev = None
    current = head 
    while current is not None:
        next_node = current.next 
        current.next = prev 
        prev = current 
        current = next_node
    return prev

