class Solution:
    def removeDuplicates(self, nums):
        writePtr = 0
        aLen = len(nums)

        for scanPtr in range(aLen):
            if nums[scanPtr] != nums[writePtr]:
                writePtr += 1
                nums[writePtr] = nums[scanPtr]

        return writePtr + 1

dups1 = [1, 1, 2]
dups2 = [0,0,1,1,1,2,2,3,3,4]
assert (Solution().removeDuplicates(dups1) == 2)
assert (Solution().removeDuplicates(dups2) == 5)
