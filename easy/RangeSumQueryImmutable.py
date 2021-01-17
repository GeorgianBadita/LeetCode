# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.__nums = nums
        self.__memo = self.__get_part_sums(nums)

    def sumRange(self, i: int, j: int) -> int:
        return self.__memo[j] - self.__memo[i] + self.__nums[i]

    def __get_part_sums(self, nums):
        if not nums:
            return []
        sums = [nums[0]]

        for i in range(1, len(nums)):
            sums.append(nums[i] + sums[-1])
        return sums
