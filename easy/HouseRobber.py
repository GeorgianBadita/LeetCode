# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # if there is no house to rob return 0
        if not nums:
            return 0

        # if there is only one house return its value
        if len(nums) == 1:
            return nums[0]

        # if there are only two houses, rob the one with more money
        if len(nums) == 2:
            return max(nums)

        dp = [0] * len(nums)  # dp[i] - the maximum amount of money which can be robbed from houses [0...i]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
