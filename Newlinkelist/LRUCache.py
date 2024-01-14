class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_end(self, node):
        # Remove the node from its current position
        node.prev.next = node.next
        node.next.prev = node.prev

        # Move the node to the end of the list
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_to_end(node)
            return node.val
        else:
            return -1

    def put(self, key: int, val: int) -> None:
        # First step is to check if the key exists, then update it
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self.move_to_end(node)
        else:
            if len(self.cache) >= self.capacity:
                # If the cache is at capacity, remove the least recently used item (head)
                to_remove = self.head.next
                del self.cache[to_remove.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

            # Add the new key-value pair to the end of the list
            new_node = Node(key, val)
            self.cache[key] = new_node
            self.move_to_end(new_node)

# Test Cases

cache = LRUCache(3)

print(cache.get(0))  # -1

cache.put(1, 10)
cache.put(2, 20)
cache.put(3, 30)

print(cache.get(1))  # 10
print(cache.get(2))  # 20

cache.put(4, 40)

print(cache.get(3))  # -1
