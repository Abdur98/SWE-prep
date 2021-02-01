# Unordered list -> Linked List

# -

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class unorderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, item):
        return

    def search(self, item):
        return

    def isEmpty(self):
        return self.head == None

    def size(self):
        return

    def index(self, item):
        return

    def append(self, item):
        return

    def insert(self, item, pos):
        return

    def pop(self, pos=-1):
        return



if __name__ == "__main__":
    testList = unorderedList()
    testList.add(4)
    testList.add(2)
    testList.add(0)


