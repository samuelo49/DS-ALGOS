"""
 Implementing a hashtable using a nested list/bucket approach
 - implement insert()
 -implement getVal(key)
"""


class HashTable:
    def __init__(self, size):
        self.size = size
        self.hashtable = [[] for _ in range(self.size)]

    def insert(self, key, value):
        hashKey = hash(key) % self.size

        # get bucket/list --> hashed
        bucket = self.hashtable[hashKey]

        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordVal = record
            if recordKey == key:
                foundKey = True
                break
        if foundKey:
            bucket[index] = (key, value)
        else:
            bucket.append(key, value)

    def getVal(self, key):
        hashKey = hash(key) % self.size
        bucket = self.hashtable[hashKey]

        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordVal = record

            if recordKey == key:
                foundKey = True
                break

        if foundKey:
            return recordVal
        else:
            return "No record Found"

    def deleteVal(self, key):
        hashKey = hash(key) % self.size

        bucket = self.hashtable[hashKey]

        foundKey = False
        for index, record in enumerate(bucket):
            recordKey, recordVal = record

            if recordKey == key:
                foundKey = True
                break
        if foundKey:
            bucket.pop(index)
        return

    def __str__(self):
        return "".join(str(item) for item in self.hashtable)


hashtable1 = HashTable(5)

hashtable1.insert('Sam', '100')

print(hashtable1)
print()
