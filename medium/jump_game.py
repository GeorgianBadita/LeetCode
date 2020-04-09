"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   09.04.2020 20:47
"""
from enum import Enum
from typing import List


class IndexType(Enum):
    BAD = 0,
    GOOD = 1


class SolutionNSQ:
    def canJump(self, nums: List[int]) -> bool:
        dp = [IndexType.BAD] * len(nums)
        dp[-1] = IndexType.GOOD

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if dp[j] == IndexType.GOOD:
                    dp[i] = IndexType.GOOD
                    break

        return dp[0] == IndexType.GOOD


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i

        return last_pos == 0


print(Solution().canJump([3, 2, 1, 1, 4]))
