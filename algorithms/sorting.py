# First, it will be necessary to compare two values to see which is smaller (or larger). In order to sort a collection, it will be necessary to have some systematic way to compare values to see if they are out of order. The total number of comparisons will be the most common way to measure a sort procedure. Second, when values are not in the correct position with respect to one another, it may be necessary to exchange them. This exchange is a costly operation and the total number of exchanges will also be important for evaluating the overall efficiency of the algorithm.

# A stable algorithm maintains the order of duplicate items in a list and is preferred in most cases.

class Sort:

    def __init__(self, alist):
        self.items = alist

    # O(n^2)
    def bubbleSort(self):
        '''
        multiple passes. First pass on list with n items = n-1 comparisons
        At the start of the second pass, the largest value is now in place. There are 𝑛−1 items left to sort, meaning that there will be 𝑛−2 pairs. Since each pass places the next largest value in place, the total number of passes necessary will be 𝑛−1. After completing the 𝑛−1 passes, the smallest item must be in the correct position with no further processing required.
        basically each iteration bubbles up the next largest value (e.g. if come across largest value in first iteration, it will be swapped over and over until it ends up at rightmost end of list)
        '''

        # n-1 passes for list of size n regardless of how items are stored
        res = self.items[:]
        for passNum in range(len(res)-1, 0, -1):
            for i in range(passNum):
                if res[i] > res[i+1]:
                    res[i], res[i+1] = res[i+1], res[i]
        return res

    # Terminating bubble short early if no exchanges needed
    # 'wasted' exchanges in bubble sort are costly but allow us to terminate early (if no exchanges after a pass, list must be sorted)
    def shortBubble(self):
        exchanges = True
        passNum = len(self.items)-1
        res = self.items[:]
        while passNum > 0 and exchanges:
            exchanges = False
            for i in range(passNum):
                if res[i] > res[i+1]:
                    exchanges = True
                    res[i], res[i+1] = res[i+1], res[i]
            passNum -= 1
        return res

    # O(n^2)
    # basically bubble sort except only largest value bubbled up to its correct position in each iteration
    def selectionSort(self):
        res = self.items[:]
        for fillSlot in range(len(res)-1, 0, -1):
            positionOfMax = 0
            for location in range(1, fillSlot + 1):
                if res[location] > res[positionOfMax]:
                    positionOfMax = location
            res[fillSlot], res[positionOfMax] = res[positionOfMax], res[fillSlot]
        return res

    # O(n^2)
    # basically start with assuming sublist list[:1] is sorted. Then start looking at items 1 to n-1 and shifting to the right until appropriate place found for n^th item
    # In general, a shift operation requires approximately a third of the processing work of an exchange (bubble/selection sort) since only one assignment is performed. In benchmark studies, insertion sort will show very good performance.
    def insertionSort(self):
        res = self.items[:]
        for idx in range(1, len(res)):
            currValue = res[idx]
            pos = idx
            while pos > 0 and res[pos - 1] > currValue:
                res[pos] = res[pos - 1]
                pos = pos - 1
            res[pos] = currValue
        return res

    # between O(n) and O(n^2)
    # break original list into sublists based on 'gap', sort each sublist using insertion sort and then sort the overall list using last insertion sort
    # Each pass sorts the list more and more so final insertion sort pretty efficient
    def shellSort(self):
        res = self.items[:]
        sublistCount = len(res) // 2
        while sublistCount > 0:
            for startPos in range(sublistCount):
                self.gapInsertionSort(res, startPos, sublistCount)
            print("After increments of size:", sublistCount, "The list is", res)
            sublistCount = sublistCount // 2
        return res

    def gapInsertionSort(self, res, start, gap):
        for i in range(start+gap, len(res), gap):
            currValue = res[i]
            pos = i

            while pos >= gap and res[pos - gap] > currValue:
                res[pos] = res[pos-gap]
                pos = pos - gap
            res[pos] = currValue

    # O(n * log(n))
    # bottoms up i.e. iterative approach: consider chunks instead of single elems
    # top down/recursive multi-threading (just ensure sort before merge)
    # relatively inefficient for array size <= 7 (use Insertion Sort instead)
    # better than quickSort bc reliable but uses additional memory to store temporary copies of array before merging them
    def mergeSort(self, alist):
        print('Splitting ', alist)
        if len(alist) > 1:
            mid = len(alist) // 2
            rightHalf = alist[:mid]
            leftHalf = alist[mid:]

            self.mergeSort(rightHalf)
            self.mergeSort(leftHalf)

            i, j, k = 0, 0, 0

            # leftHalf and rightHalf considered sorted at this point so start two pointers i & j and iterate char by char and over-write input list
            while i < len(leftHalf) and j < len(rightHalf):
                if leftHalf[i] <= rightHalf[j]:
                    alist[k] = leftHalf[i]
                    i += 1
                else:
                    alist[k] = rightHalf[j]
                    j += 1
                k += 1

            while i < len(leftHalf):
                alist[k] = leftHalf[i]
                i += 1
                k += 1

            while j < len(rightHalf):
                alist[k] = rightHalf[j]
                j += 1
                k += 1
        print('Merging ', alist)

    # generalized merge sort with anonymous lambda function and passing indices as arguments instead of slicing (which is O(k)) -> guaranteed
    # O(n * log(n))
    def mergeSort2(self, alist, leftIdx, rightIdx, compFun):
        if leftIdx >= rightIdx: return
        mid = (leftIdx + rightIdx) // 2

        self.mergeSort2(alist, leftIdx, mid, compFun)
        self.mergeSort2(alist, mid+1, rightIdx, compFun)

        return self.merge(alist, leftIdx, rightIdx, mid, compFun)

    def merge(self, alist, leftIdx, rightIdx, mid, compFun):
        leftHalf = alist[leftIdx:mid+1]
        rightHalf = alist[mid+1:rightIdx+1]

        leftHalfIdx, rightHalfIdx, sortedIdx = 0, 0, leftIdx

        while leftHalfIdx < len(leftHalf) and rightHalfIdx < len(rightHalf):
            if compFun(leftHalf[leftHalfIdx], rightHalf[rightHalfIdx]):
                alist[sortedIdx] = leftHalf[leftHalfIdx]
                leftHalfIdx += 1
            else:
                alist[sortedIdx] = rightHalf[rightHalfIdx]
                rightHalfIdx += 1
            sortedIdx += 1

        while leftHalfIdx < len(leftHalf):
            alist[sortedIdx] = leftHalf[leftHalfIdx]
            leftHalfIdx += 1
            sortedIdx += 1

        while rightHalfIdx < len(rightHalf):
            alist[sortedIdx] = rightHalf[rightHalfIdx]
            rightHalfIdx += 1
            sortedIdx += 1

        return alist

    # O(n * log(n)) if start off with pivot in middle, else can be O(n^2)
    # caa use 'median of three' (start off with mid value btw first, mid and last value) technique to alleviate risk of uneven pivot
    def quickSort(self):
        res = self.items[:]
        return self.quickSortHelper(res, 0, len(res)-1)

    def quickSortHelper(self, alist, leftIdx, rightIdx):
        if leftIdx < rightIdx:
            splitPoint = self.partition(alist, leftIdx, rightIdx)

            self.quickSortHelper(alist, leftIdx, splitPoint - 1)
            self.quickSortHelper(alist, splitPoint + 1, rightIdx)

        return alist

    def partition(self, alist, leftIdx, rightIdx):
        pivotValue = alist[leftIdx]
        leftMark = leftIdx + 1
        rightMark = rightIdx
        done = False

        while not done:
            while leftMark <= rightMark and alist[leftMark] <= pivotValue:
                leftMark += 1
            while alist[rightMark] >= pivotValue and rightMark >= leftMark:
                rightMark -= 1

            if rightMark < leftMark:
                done = True
            else:
                alist[leftMark], alist[rightMark] = alist[rightMark], alist[leftMark]

        alist[leftIdx], alist[rightMark] = alist[rightMark], alist[leftIdx]
        return rightMark


alist = [54,26,93,17,77,31,44,55,20, 22, 3, 5, 7]
s = Sort(alist)
print(s.bubbleSort())
# print(s.selectionSort())
# print(s.insertionSort())
# print(s.shellSort())

# print(s.mergeSort(alist))
# print(s.shortBubble())

# print(s.mergeSort2(alist, 0, len(alist)-1, lambda a, b: a > b))

print(s.quickSort())







