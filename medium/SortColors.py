# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        right_zeros = 0
        left_twos = len(nums) - 1
        curr = 0
        while curr <= left_twos:
            if nums[curr] == 0:
                nums[curr], nums[right_zeros] = nums[right_zeros], nums[curr]
                curr += 1
                right_zeros += 1
            elif nums[curr] == 2:
                nums[curr], nums[left_twos] = nums[left_twos], nums[curr]
                left_twos -= 1
            else:
                curr += 1


Solution().sortColors([2, 0, 2, 1, 1, 0])
