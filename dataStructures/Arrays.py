# 1. Arrays

# Know exactly where everything is in memory so O(1) index (read & write)
# Slow for inserting, removing, iterating

# (modern languages typically have dynamically sized arrays, guaranteeing better amortized performance)

# Interview tip: Use an array when you need data in an ordered list with fast indexing or compact memory footprint. Don’t use an array if you need to search for unsorted items efficiently or insert and remove items frequently


class Array(object):
    ''' sizeofArray: denotes the total size of the array to be initialized
        arrayType: denotes the data type of the array (as all the elements of the array have the same data type)
        arrayItems: values at each position of an array
    '''

    def __init__(self, sizeOfArray, arrayType = int):
        self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))
        self.arrayItems = [arrayType(0)] * sizeOfArray # initialize array with 0s
        self.arrayType = arrayType
        self.count = 0

    def __str__(self):
        return ''.join([str(i) for i in self.arrayItems])

    def __len__(self):
        return len(self.arrayItems)

    # magic methods to enable indexing

    def __setitem__(self, index, data):
        self.arrayItems[index] = data

    def __getitem__(self, index):
        return self.arrayItems[index]

    # private methods to enable array dynamism

    def _resize(self, newCount):
        tempArray = [self.arrayType(0)] * newCount

        for i in range(self.count):
            tempArray[i] = self.arrayItems[i]

        self.arrayItems = tempArray

        self.sizeOfArray = len(tempArray)

    # O(n)
    def search(self, keyToSearch):
        for i in range(self.sizeOfArray):
            if self.arrayItems[i] == keyToSearch:
                return i
        return -1

    def insert(self, data, index):
        if self.sizeOfArray > index:
            for i in range(self.sizeOfArray - 2, index - 1, -1):
                self.arrayItems[i + 1] = self.arrayItems[i]
            self.arrayItems[index] = data
            self.count += 1
        else:
            print('Index {} is out of bounds. Array size is {}'.format(index, self.sizeOfArray))

    def delete(self, data, index):
        if self.sizeOfArray > index:
            for i in range(index, self.sizeOfArray - 1):
                self.arrayItems[i] = self.arrayItems[i + 1]
            self.arrayItems[i + 1] = self.arrayType(0)
            self.count -= 1
        else:
            print('Index {} is out of bounds. Array size is {}'.format(index, self.sizeOfArray))

    def insertDynamic(self, data, index):
        if index > self.sizeOfArray:
            print('Index {} is out of bounds. Array size is {}'.format(index, self.sizeOfArray))
        elif self.count == self.sizeOfArray:
            self._resize(self.sizeOfArray * 2)
            self.insert(data, index)
        else:
            self.insert(data, index)

if __name__ == '__main__':
    testArray = Array(3, int)
    testArray.insert(4, 0)
    testArray.insert(2, 1)
    testArray.insert(0, 2)
    print(testArray)
    testArray.insertDynamic(6, 3)
    print(testArray)
    testArray.insertDynamic(9, 4)
    print(testArray)
