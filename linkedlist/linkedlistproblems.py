"""
 Node class
 Linked List class
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def SumNodes(node):
    total = 0
    while node is not None:
        total += node.value
        node = node.next
    return total


def countNodes(node) -> int:
    length = 0
    while node is not None:
        node = node.next
        length += 1
    return length


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head is None:
            return node
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = node
        return self.head

    def findMax(self):
        if self.head is None:
            return None
        currentNode = self.head
        maxElement = currentNode.data
        while currentNode is not None:
            maxElement = max(maxElement, currentNode.data)
            currentNode = currentNode.next
        return maxElement
