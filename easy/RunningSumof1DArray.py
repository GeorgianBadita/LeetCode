# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        return nums

