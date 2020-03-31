"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 00:31
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0 or len(nums) < 2:
            return
        how_much = k % len(nums)
        a = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if how_much != 0:
                a[how_much - 1] = nums[i]
                how_much -= 1
                continue
            a[i + k % len(nums)] = nums[i]

        for i in range(len(a)):
            nums[i] = a[i]




Solution().rotate([1, 2, 3, 4, 5, 6, 7], 1)
