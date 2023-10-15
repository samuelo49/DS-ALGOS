"""
Q. Given a linked list, append an element with a target value to the list iteratively.
Examples:
• Given a linked list: 1 ➞ 4 ➞ 5, target: 7 // returns 1 ➞ 4 ➞ 5 ➞ 7
• Given a linked list: 0, target 7 // returns 0 ➞ 7
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array


def append(node, target):
    # if node is None:
    #     return ListNode(target)
    # current = node
    # while current.next is not None:
    #     current = current.next
    # current.next = ListNode(target)
    # return node



    # if node is None:
    #     return ListNode(target)
    #
    # if node.next is None:
    #     node.next = ListNode(target)
    # else:
    #     append(node.next, target)
    # return node

    # empty list case
    if node is None:
        return ListNode(target)
    # we want to append new node at the very head 1->2-3->5
    newNode = ListNode(target)
    # newNode.next = node
    # return newNode
    #we want to append somewhere in a sorted list
    # currentNode = node
    # while currentNode.next:
    #     if currentNode.next.value > target:
    #         tempNode = currentNode.next
    #         currentNode.next = newNode
    #         newNode.next = tempNode
    #         break
    #     else:
    #         currentNode = currentNode.next
    # return node

    #we want to append at the end
    currentNode = node
    while currentNode.next:
        currentNode = currentNode.next
    currentNode.next = ListNode(target)
    return node



# Test Cases

LL1 = ListNode(1,ListNode(2,ListNode(3,ListNode(5))))
# print(arrayify(append(LL1, 2)))  # [1]
# print(arrayify(append(LL1, 7)))  # [1, 4, 5, 7]
# print(arrayify(append(ListNode(), 7)))  # [0, 7]
# print(arrayify(append(LL1, 4)))
# print(arrayify(append(LL1, 6)))
