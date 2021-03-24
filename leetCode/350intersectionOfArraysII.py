class Solution:
    def intersect(self, nums1, nums2):
        M = len(nums1)
        N = len(nums2)

        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        res = []

        while i < M and j < N:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

        return res

nums1 = [1,2,2,1]
nums2 = [2,2]
assert (Solution().intersect(nums1, nums2) == [2, 2])
