# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


# ANS

# A simple DP problem, in a way
# Basically, max at index i = max(value[i], value[i] + max at index i-1)
# storing max at index i-1 as localMax basically

class Solution:
    def maxSubarray(nums):
        length = len(nums)
        localMax, globalMax = 0, float('inf')*-1

        for i in range(length):
            localMax = max(nums[i], nums[i] + localMax)
            globalMax = max(globalMax, localMax)

        return globalMax

print(Solution.maxSubarray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
