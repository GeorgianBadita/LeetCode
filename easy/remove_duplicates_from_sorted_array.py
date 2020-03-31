"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   28.03.2020 23:36
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return len(nums)
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1


nums = [5, 5, 5, 5, 5, 6]
print(Solution().removeDuplicates(nums))
