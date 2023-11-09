"""
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"

class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_count = {} # is to map the keys to their counts 
        self.count_node = {} # maps counts to their nodes 
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key not in self.key_count:
            self.key_count[key] = 0
        count = self.key_count[key]
        self.key_count[key] += 1
        if count > 0:
            node = self.count_node[count]
            node.keys.remove(key)
            if not node.keys:
                self._remove(node)
        node = self.count_node.get(count + 1, None)
        if not node:
            node = Node(count + 1)
            self._add(node, self.count_node.get(count, self.tail.prev))
        node.keys.add(key)
        self.count_node[count + 1] = node

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return
        count = self.key_count[key]
        if count == 1:
            del self.key_count[key]
        else:
            self.key_count[key] -= 1
        node = self.count_node[count]
        node.keys.remove(key)
        if not node.keys:
            self._remove(node)
            del self.count_node[count]
        if count > 1:
            node = self.count_node.get(count - 1, None)
            if not node:
                node = Node(count - 1)
                self._add(node, self.count_node[count])
            node.keys.add(key)
            self.count_node[count - 1] = node

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

    def _add(self, node, prev):
        next = prev.next
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

"""
class Node:
    ''' prev<-[1: {}]->next'''
    def __init__(self,count):
        self.keys = set()
        self.count = count
        self.prev = None
        self.next = None 

class AllOne:
    def __init__(self):
        self.count_node = {} # maps the nodes to their count
        self.key_count  = {} # maps keys to their count
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head


    def inc(self, key: str) -> None:
        # check if key not ik key_count {}, it not then add it then increment count, otherwise just increment count
        if key not in self.key_count:
            self.key_count[key] = 0
        count = self.key_count[key]
        self.key_count[key] += 1

        # now we check if the count of they key is greater than 0
        if count > 0:
            # we get the node with that count
            node = self.count_node[count]
            # remove the key from set of keys since we are about to increment its count
            node.keys.remove(key)
            # after removing check to see if node is empty?
            if not node.keys:
                # delete node if no keys
                self._remove(node)
        # we get the node with count + 1 if present or we get None
        node = self.count_node.get(count + 1, None)

        # if node == None
        if not node:
            #create a new node with that count
            node = Node(count + 1)
            # add it to the list
            self._add(node, self.count_node.get(count,self.tail.prev))

        # if we have a node, add the key to the key set at that node.
        node.keys.add(key)
        
        #update count_node with the count + 1 to the node
        self.count_node[count + 1] = node
    
    
    def dec(self, key: str) -> None:
        # check if we have key?
        if key not in self.key_count:
            return
        
        #key present, so lets get count for key
        count = self.key_count[key]

        # check count for key
        if count == 1:
            del self.key_count[key]
        else:
            self.key_count[key] -= 1

        # get node corresponding to count
        node = self.count_node[count]

        #remove key from keys set at that node
        node.keys.remove(key)

        # check if node' set of keys not empty
        if not node.keys:
            self._remove(node)
            del self.count_node[count]
        
        # get the new node for decremented count
        if count > 1:
            node = self.count_node.get(count - 1, None)

            # case when node == None
            if not node:
                node = Node(count - 1)
                self._add(node, self.count_node[count])
            # we have a node with that count
            node.keys.add(key)
            self.count_node[count - 1] = node

    def getMaxKey(self) -> str:
        #check if list is empty
        if self.tail.prev == self.head:
            return ""
        # iterator over the keys in the set to return first item
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
    
    def _add(self, node, prev):
        # before adding list looks like =>  prevNode<-->nextNode
        next = prev.next
        prev.next = node
        node.prev = prev 
        node.next = next
        next.prev = node
        # after adding node prevNode<-->node<-->nextNode

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev