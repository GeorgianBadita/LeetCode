# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

        return max_sum
