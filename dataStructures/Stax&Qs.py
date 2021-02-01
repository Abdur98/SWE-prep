# Stacks:

# - LIFO: Last In First Out
# - Addition & removal from the same end (typically called the 'top end')
# - Closer to the base = been in stack longest
# - Can be used to reverse order of items (order of insertion = reverse(order of removal)
# - good for balanced symbols/paranthesis check, easily converting integer to binary, infix -> post/pre-fix conversion & evaluation

class Stack:

    def __init__(self, limit = 10):
        self.stack = []
        self.limit = limit

    def __str__(self):
        return ''.join([str(i) for i in self.stack])

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

# Queues:

# - FIFO - First In First Out
# - Items added to one end (typically called 'rear') and removed from other end (typically called 'front')

class Queue:

    def __init__(self, limit = 10):
        self.queue = []
        self.limit = limit

    def __str__(self):
        return ''.join([str(i) for i in self.queue])

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

# Deque

# - Addition/removal from front and rear
# - Good for palindrom checks

if __name__ == "__main__":

    testStack = Stack()
    testStack.push(4)
    testStack.push(2)
    testStack.push(0)
    print('testStack is', testStack)
    print(testStack.peek())
    testStack.pop()
    print(testStack, testStack.size())

    testQueue = Queue()
    testQueue.enqueue(4)
    testQueue.enqueue(2)
    testQueue.enqueue(0)
    print('testQueue is', testQueue)
    print(testQueue.dequeue())
    print(testQueue, testQueue.size())


    def revStr(input):
        tempStack = Stack()
        for char in input:
            tempStack.push(char)

        tempStr = ''
        while not tempStack.isEmpty():
            tempStr = tempStr + tempStack.pop()
        return tempStr


    assert(revStr('satoshi') == 'ihsotas')
    assert(revStr('nakamoto') == 'otomakan')

    def baseConverter(input, base):
        digits = '0123456789ABCDEF'
        tempStack = Stack()
        while input > 0:
            rem = input % base
            tempStack.push(rem)
            input = input // base

        tempStr = ''
        while not tempStack.isEmpty():
            tempStr = tempStr + str(digits[tempStack.pop()])

        return tempStr

    assert(baseConverter(42, 2)) == '101010'
    assert(baseConverter(233, 8) == '351')
    assert(baseConverter(233, 16) == 'E9')

