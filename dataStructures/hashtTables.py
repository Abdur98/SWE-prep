class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.capacity = 50
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0

        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        self.size += 1
        hashSum = self.hash(key)
        firstNode = self.buckets[hashSum]
        newNode = Node(key, value)
        if not firstNode:
            self.buckets[hashSum] = newNode
            return
        else:
            prev = firstNode
            while firstNode is not None:
                prev = firstNode
                node = firstNode.next
            firstNode.next = newNode

    def find(self, key):
        hashSum = self.hash(key)
        firstNode = self.buckets[hashSum]

        while firstNode and firstNode.key != key:
            firstNode = firstNode.next

        if not firstNode:
            return None
        else:
            return firstNode.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = node

        while node and node.key != key:
            prev = node
            node = node.next

        if not node: return None
        else:
            res = node.value
            self.size -= 1
            prev.next = node.next
            return res

ht = HashTable()
ht.insert('wood', 'apple')
ht.insert('stone', 'legumes')
ht.insert('bamboo', 'beets')
ht.insert('clay', 'beets')

print(ht.find('bamboo'))













