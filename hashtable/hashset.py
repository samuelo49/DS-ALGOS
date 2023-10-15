class HashSet:
    def __init__(self):
        self.key_space = 2096
        self.hashtable = [Bucket() for _ in range(self.key_space)]

    def add(self, key):
        hashKey = hash(key) % self.key_space
        self.hashtable[hashKey].update(key)

    def remove(self, key):
        hashKey = hash(key) % self.key_space
        self.hashtable[hashKey].remove(key)

    def contains(self, key):
        hashKey = hash(key) % self.key_space
        return self.hashtable[hashKey].get(key)


class Bucket:
    def __init__(self):
        self.bucket = []

    def update(self,key):
        foundKey = False
        for i, k in enumerate(self.bucket):
            if key == k:
                self.bucket[i] = key
                foundKey = True
                break
        if not foundKey:
            self.bucket.append(key)

    def get(self,key):
        for k in self.bucket:
            if k == key:
                return True
        return False

    def remove(self,key):
        for i,k in enumerate(self.bucket):
            if k == key:
                del self.bucket[i]







