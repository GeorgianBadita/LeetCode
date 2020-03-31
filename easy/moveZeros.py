"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 00:45
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        num_zeros = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            else:
                num_zeros += 1
        j = len(nums) - 1
        while num_zeros > 0:
            nums[j] = 0
            j -= 1
            num_zeros -= 1
        print(nums)


Solution().moveZeroes([0, 0, 0, 0])
