"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   05.04.2020 23:16
"""
from typing import List


def first_post_bs(arr, x, low, high):
    while low <= high:
        mid = low - (low - high) // 2
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        if x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return - 1


def last_pos_bs(arr, x, low, high):
    while low <= high:
        mid = low - (low - high) // 2
        if (mid == len(arr) - 1 or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        if x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            first_post_bs(nums, target, 0, len(nums) - 1),
            last_pos_bs(nums, target, 0, len(nums) - 1)
        ]


nums = [5, 7, 7, 8, 8, 10]
target = 6

print(Solution().searchRange(nums, 8))
