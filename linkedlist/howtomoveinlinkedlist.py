"""
practice how to move around in a linked list and print the specific node
1->2->3->4->5
h
c

"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def evenNumbers(list):
    if list is None: return 0
    sentinel = ListNode(0)
    current = list
    newNode = sentinel
    while current.next:
        if current.value % 2 == 1:
            newNode.next = ListNode(current.next.value)
            newNode = newNode.next
        current = current.next
    return sentinel.next


def oddNumbers(list):
    if list is None: return 0
    sentinel = ListNode(0)
    current = list
    newNode = sentinel
    while current:
        if current.value % 2 == 1:
            newNode.next = ListNode(current.value)
            newNode = newNode.next
        current = current.next
    return sentinel.next


def createCycle(list):
    current = list
    sentinel = ListNode(0)
    newNode = sentinel
    while current:
        newNode.next = ListNode(current.value)
        newNode = newNode.next
        current = current.next
    newNode.next = sentinel.next
    return sentinel.next


# def createCycle(head):
#     sentinel = Node(0)
#     sentinel.next = head
#     pointer = sentinel
#
#     while pointer.next:
#         pointer = pointer.next
#
#     pointer.next = sentinel.next
#     return sentinel.next

def printList(list):
    if list is None:
        return None
    current = list
    while current:
        print(current.value, '->', end='')
        current = current.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(printList(head))
print(printList(evenNumbers(head)))
print(printList(oddNumbers(head)))
print(printList(createCycle(head)))
