# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        num_zeros = 0
        for elem in nums:
            if elem == 0:
                num_zeros += 1

        start_p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start_p] = nums[i]
                start_p += 1
        for i in range(1, num_zeros + 1):
            nums[-i] = 0



