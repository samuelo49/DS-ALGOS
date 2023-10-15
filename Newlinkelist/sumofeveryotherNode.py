"""
Given a linked list of integers, return the sum of every other value,
starting with the second.
1->2->3->4->5->6  =>

counter = 1
sum = 0
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def everyOtherNode(head: Node):
    if head is None:
        return None
    current = head
    counter = 1
    sumValue = 0
    while current:
        if counter % 2 == 0:
            sumValue += current.val
        current = current.next
        counter += 1
    return sumValue


head1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
print(everyOtherNode(head1))
