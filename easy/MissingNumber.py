# https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/722/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
