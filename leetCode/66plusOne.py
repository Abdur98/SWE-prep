class Solution:
    def plusOne(self, digits):

        n = len(digits)

        for i in range(n):
            idx = n - 1 - i

            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits

        return [1] + digits

digits = [1, 2, 3, 9, 9, 9]
res = [1, 2, 4, 0, 0, 0]
assert (Solution().plusOne(digits) == res)
