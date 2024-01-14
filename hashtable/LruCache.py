"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
 evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Notes:
    -> When you think of this, you right away think of a hashmap/ dictionary which maps key--> value.
    -> however we have a limited capacity hence why we need a hashmap and doubly linked list.
    - we are applying the doubly linked list so we can maintain storing the nodes in an ordered manner.
    - we are also able to remove the least recently used nodes in constant time since we have the key -> node in the doubly linked list.


"""

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self,capacity:int):
        self.cap = capacity
        self.cache = {} # mapping the key to the node(key,val)

        self.left = Node(0,0) # to keep track of least recently used
        self.right = Node(0,0) # to keep track of most recently used

        #connect the nodes since its a doubly linked list
        self.left.next = self.right
        self.right.prev = self.left

    # remove from the list 
    def remove(self,node:Node):
        '''
        Before removing =>  [self.left]<-->[leastrecentlusuednode]<-->[recentlyusednode]<-->[self.right]

        After removing =>  [self.left]<-->[node that was most recently used prior]<-->[self.right]
        '''
        prev,nxt = node.prev, node.next
        prev.next, nxt.prev  = nxt, prev

    # insert at right
    def insert(self,node:Node):
        '''
        Before insert => [prev]<-->[self.right]

        After insert =>[prev]<-->[new node]<-->[self.right]
        '''
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self,key):
        if key in self.cache:
            self.remove(self.cache[key]) # remove the  node from current position
            self.insert(self.cache[key]) # move it to the right most position
            return self.cache[key].val
        return -1

    def put(self, key:int, value:int):
        if key in self.cache:
            # remove node from our list
            self.remove(self.cache[key])

        # now we create a new node with the key value pair
        self.cache[key] = Node(key,value)

        # insert the node in our doubly linked list
        self.insert(self.cache[key])


        # we need to check every time when we insert if we have exceeded the capacioty
        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from cache

            lru = self.left.next  # we use our dummy node to point to the least recently used node

            # now we know the node we can remove it from the current position in the linked list
            self.remove(lru)
            
            # we then remove it from our hashmap
            del self.cache[lru.key]


cache = LRUCache(2)
cache.put(1, 1) #cache is {1=1}
cache.put(2, 2) # cache is {1=1, 2=2}
print(cache.get(1))  # return 1
cache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(cache.get(2))  # returns -1 (not found)
cache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(cache.get(1))   # return -1 (not found)
print(cache.get(3))   # return 3
print(cache.get(4))  # return 4