"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   06.04.2020 20:17
"""
from typing import List


class Solution:

    def __find_pivot(self, arr, left, right):
        while left <= right:
            mid = left - (left - right) // 2
            if mid == 0 or arr[mid - 1] > arr[mid]:
                return mid
            if arr[mid] > arr[0]:
                left = mid + 1
            else:
                right = mid - 1
        return 0

    def bsrch(self, arr, x, left, right):
        while left <= right:
            mid = left - (left - right) // 2
            if arr[mid] == x:
                return mid
            if arr[mid] > x:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.__find_pivot(nums, 0, len(nums) - 1)
        if pivot == 0:
            return self.bsrch(nums, target, 0, len(nums) - 1)
        if target >= nums[0]:
            return self.bsrch(nums, target, 0, pivot - 1)
        return self.bsrch(nums, target, pivot, len(nums) - 1)


nums = [4, 5, 6, 7, 0, 1, 2]
target = 4

print(Solution().search(nums, target))
