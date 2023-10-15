"""
Given a linked list of positive integers, count the elements with odd values from the list.
 Note that 0 is an even number.
 // 1 -> 1 -> 1 -> 1
head = new Node(1, new Node(1, new Node(1, new Node(1))))
console.log(countOdd(head) == 4)
// 1 -> 2 -> 3 -> 4
head = new Node(1, new Node(2, new Node(3, new Node(4))))
console.log(countOdd(head) == 2)
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def countOddValues(head):
    # count = 0
    # if head is None: return 0
    # currentNode = head
    # while currentNode:
    #     if currentNode.val % 2 == 1:
    #         count += 1
    #     currentNode = currentNode.next
    # return count
    if head is None:
        return 0

    return 1 + countOddValues(head.next) if head.val % 2 != 0 else 0


# head = Node(1, Node(2, Node(3, Node(4))))
head = Node(1, Node(1, Node(1, Node(1))))
print(countOddValues(head))
