"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 00:25
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)


print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
