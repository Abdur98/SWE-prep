class Solution:
    def rotate(self, nums, k):

        for i in range(-1, -k-1, -1):
            temp = nums.pop()
            nums.insert(0, temp)

        return nums

test1 = [0, 1, 2, 3, 4]
test2 = [-1,-100,3,99]
assert (Solution().rotate(test1, 3) == [2, 3, 4, 0, 1])
assert (Solution().rotate(test2, 2) == [3, 99, -1, -100])
