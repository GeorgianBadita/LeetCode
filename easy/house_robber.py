"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 23:02
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        profit = [0] * len(nums)
        profit[0] = nums[0]
        profit[1] = max(profit[0], nums[1])
        for i in range(2, len(nums)):
            profit[i] = max(profit[i - 2] + nums[i], profit[i - 1])
        return profit[-1]


print(Solution().rob([2,7,9,3,1]))
