# Enqueue and Dequeue in O(log n)
# need to keep tree balanced to guarantee logarithmic time
# so create a 'Complete' Binary Tree i.e. all nodes at all levels filled out (except last level, which is filled left to right)
# interesting bc implemented using a single list (not nodes & references, not list of lists). If root at index 1 and parent at index p, left child at 2p and right at 2p+1. Similarly, for node at index n, parent at n//2. Ends up basically being populating the list left to right for each level
# heap order property:for every node x with parent p, the key in p <= key in x
# building a heap from a list is O(n) (log(n) factor is derived from the hight of the tree and for most of the work, tree is shorter than log(n))


class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        # currentSize is the index of k in the heapList
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self, alist):
        # !!!O(n)!!
        # bc heap is complete bin tree, any nodes past halfway point
        # will be leaves and therefore have no children
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i -= 1

bh = BinHeap()
bh.buildHeap([9, 5, 6, 2, 3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
bh.insert(1)
print(bh.delMin())

