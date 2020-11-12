# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i in range(len(nums)):
            if target - nums[i] in sum_dict and sum_dict[target - nums[i]] != i:
                return [i, sum_dict[target - nums[i]]]
            sum_dict[nums[i]] = i

print(Solution().twoSum([2, 4, 5, 5], 10))
