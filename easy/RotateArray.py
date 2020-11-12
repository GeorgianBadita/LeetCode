# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # number of real rotations
        num_rot = k % len(nums)

        while num_rot > 0:
            last = nums[-1]
            del nums[-1]
            nums.insert(0, last)
            num_rot -= 1
        