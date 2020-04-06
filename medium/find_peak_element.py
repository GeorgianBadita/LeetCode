"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   06.04.2020 20:34
"""
from typing import List


class Solution:

    def find_peak(self, arr):
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left - (left - right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid
            else:
                right = mid - 1

        return left + 1

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        return self.find_peak(nums)


nums = [1, 2, 1, 3, 5, 6, 4]
print(Solution().find_peak(nums))
