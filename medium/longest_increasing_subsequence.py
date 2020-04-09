"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   09.04.2020 22:28
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[-1] = 1
        mx = 1
        for i in range(len(nums) - 2, -1, -1):
            best = 0
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    best = max(best, dp[j])
            dp[i] = 1 + best
            mx = max(mx, dp[i])
        print(dp)
        return mx


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
