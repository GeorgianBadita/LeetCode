"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 22:57
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum_ = nums[0]
        for i in range(1, len(nums)):
            if sum_ < 0:
                sum_ = 0
            sum_ += nums[i]
            if sum_ > max_sum:
                max_sum = sum_
        return max_sum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
