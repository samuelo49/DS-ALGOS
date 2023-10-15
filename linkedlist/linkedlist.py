'''
 Implementing a linked list in python
 - created Node class
 -created linked list class
'''


class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertAtHead(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print('Invalid position')
            return
        if position == 0:
            self.insertAtHead(newNode)
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def insertAtEnd(self, newNode):
        # head ==>Emma ==> Esther
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = newNode

    def search(self, searchVal):  # 1 -> 2 -> 3->4 , 3
        if self.head is not None:
            temp = self.head
            found = 0
            index = 0
            while temp is not None:
                index += 1
                if temp.data == searchVal:
                    found += 1
                    break
                temp = temp.next
            if found == 1:
                print(searchVal, "is found at", index)
            else:
                print(searchVal, "not found in the list")
        else:
            print("The list is empty")

    def deleteAtHead(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None

    def deleteAt(self, index):  # 1 -> 2 -> 3->4
        currentNode = self.head
        currentIndex = 0
        while True:
            if currentIndex == index:
                previousNode.next = currentNode.next
                currentNode.next = None
            previousNode = currentNode
            currentNode = currentNode.next
            currentIndex += 1

    def deleteAtEnd(self):
        currentNode = self.head
        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next
        previousNode.next = None

    def deleteAll(self):
        temp = self.head
        while temp is not None:
            self.head = self.head.next
            temp = None

    def deleteEvenNodes(self):
        if self.head is not None:
            oddNode = self.head
            evenNode = self.head.next

            while oddNode is not None and evenNode is not None:
                oddNode.next = evenNode.next
                evenNode = None

                oddNode = oddNode.next
                if oddNode is not None:
                    evenNode = oddNode.next

    def deleteOddNodes(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None

            if self.head is not None:
                evenNode = self.head
                oddNode = self.head.next

                while evenNode is not Node and oddNode is not None:
                    evenNode.next = oddNode.next
                    oddNode = None

                    evenNode = evenNode.next

                    if evenNode is not None:
                        oddNode = evenNode.next

    def reverseList(self):  # 1->2->3->4
        if self.head is not None:
            previousNode = None
            currentNode = self.head
            followingNode = self.head

            while currentNode is not None:
                followingNode = followingNode.next
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = followingNode
            self.head = previousNode

    def swapNodes(self, node1, node2):
        # count nodes
        temp = self.head
        N = 0
        while temp is not None:
            N += 1
            temp = temp.next

        # check if swap positions are valid entries
        if node1 < 1 or node1 > N or node2 < 1 or node2 > N:
            return
        # traverse to where nodes are to be swapped
        position1 = self.head
        position2 = self.head

        for i in range(1, node1):
            position1 = position1.next
        for i in range(1, node2):
            position2 = position2.next

        # swap the nodes
        tempVal = position1.data
        position1.data = position2.data
        position2.data = tempVal

    def printList(self):
        if self.head is None:
            print("Empty Linked List")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


first = Node('John')
linkedList = LinkedList()
linkedList.insertAtEnd(first)
second = Node('Esther')
linkedList.insertAtEnd(second)
third = Node('Sam')
linkedList.insertAtHead(third)
# fourth = Node('Angel')
# linkedList.insertAt(fourth, 1)
# linkedList.removeAtEnd()
# linkedList.removeAtHead()
# linkedList.search('Esther')
linkedList.reverseList()
linkedList.printList()
