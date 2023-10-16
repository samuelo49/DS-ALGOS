
class Node:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

def arrayify(head):
    array = []
    ptr = head
    while ptr is not None:
        array.append(ptr.value)
        ptr = ptr.next
    return array
"""
How to iterate through a linked list
given 1-2-3-4-5-6
print every single node
"""
def iterate_thru_ll(head:Node):
    if head is None:
        return None
    current_node = head
    while current_node and current_node.next:
        print(current_node.value, end="->")
        current_node = current_node.next

# head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6))))))
# print(iterate_thru_ll(head))

"""
How to insert an element into a linked list, 
given a pointer to the node before it in the list
• Given a linked list: 1 ➞ 3 ➞ 4, target: 2 // returns 1 ➞ 2 ➞ 3 ➞ 4
• Given an empty linked list, target: 1  // returns 1
"""
def insert_into_ll_given_target(head,target):
    if head is None:
        return None
    sentinel = Node(0)
    sentinel.next = head
    current_node = sentinel
    while current_node:
        if target < current_node.next.value:
            temp = current_node.next
            current_node.next = Node(target)
            current_node.next.next = temp
            break
        current_node = current_node.next
    return sentinel.next
# head = Node(1,Node(3,Node(4)))
# print(arrayify(insert_into_ll_given_target(head,2)))

"""
* How to remove an element from a linked list, 
given a pointer to the node before it in the list.
Given a sorted linked list of unique integers, remove a node with the
target value from the list.
Examples:
• Given a linked list: -1 ➞ 1 ➞ 3 ➞ 4, target: 1 // returns -1 ➞ 3 ➞ 4
• Given a linked list: 5, target: 3 // returns 5
"""
def remove(head: Node, target: int):
    if head is None:
        return None
    sentinel = Node(0)
    sentinel.next = head
    current_node = sentinel
    while current_node.next:
        # 0 -> -1-> 1 -> 3 -> 4
        if current_node.next.value == target:
            current_node.next = current_node.next.next
            break
        current_node = current_node.next
    return sentinel.next
# head = Node(-1,Node(1,Node(3,Node(4))))
# # print(arrayify(remove(head,1)))
# print(arrayify(remove(head,5)))

"""
* Be able to find the length of a linked list quickly
given this linked list 1-2-3-4-5-6. FInd its length
"""
def find_linkedlist_length(head:Node):
    if head is None:
        return 0
    current = head
    return 1 + find_linkedlist_length(current.next) 

# head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6))))))
# print(find_linkedlist_length(head))

"""
Know the slow & fast pointer technique to solve problems like find the halfway point
given this linked list 1-2-3-4-5-6. FInd its half way point.
"""
def find_mid_point(head:Node):
    if head is None:
        return None
    slow = head
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    return slow.value
# head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6))))))
# print(find_mid_point(head))

"""
Know the slow & fast pointer technique to solve problems like find the kth from the end node
Q. Given a linked list, return the kth element from the end of the list.
   If the k exceeds the length of the list, return -1.
Examples:
• Given a linked list: 13 ➞ 1 ➞ 5 ➞ 3 ➞ 7 ➞ 10, k: 1 // returns 10
• Given a linked list: 13 ➞ 1 ➞ 5 ➞ 3 ➞ 7 ➞ 10, k: 7 // returns -1
"""
def kthFromLast(head:Node, k):
    if head is None:
        return None
    slow = head
    fast = head
    
    for _ in range(k):
        if fast is  not None:
            fast = fast.next
        else:
            return -1
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow.value
# head = Node(13,Node(1,Node(5,Node(3,Node(7,Node(10))))))
# print(kthFromLast(head,7))

"""
* Know how to detect a cycle in a linked list
Detect cycle in linked list [3,2,0,-4]
"""
def hasCycle(head):
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
head = Node(3,Node(2,Node(0,Node(-4,))))
print(hasCycle(head))

