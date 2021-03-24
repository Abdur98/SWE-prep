class Solution:
    def singleNumber(self, nums):
        elems = set()

        # O(n), O(n)
#         for num in nums:
#             if num in elems:
#                 elems.discard(num)
#             else:
#                 elems.add(num)

#         return list(elems)[0]

        # O(n), O(1)

        res = 0

        for num in nums:
            res ^= num

        return res

nums = [4, 1, 2, 1, 2]
assert (Solution().singleNumber(nums) == 4)
