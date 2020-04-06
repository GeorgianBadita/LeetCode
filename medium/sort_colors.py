"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   06.04.2020 21:13
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ind, left, right = 0, 0, len(nums) - 1

        while ind <= right:
            if nums[ind] == 0:
                nums[ind], nums[left] = nums[left], nums[ind]
                ind += 1
                left += 1
            elif nums[ind] == 2:
                nums[ind], nums[right] = nums[right], nums[ind]
                right -= 1
            else:
                ind += 1


Solution().sortColors([2, 0, 2, 1, 1, 0])
