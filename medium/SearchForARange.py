# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/

from typing import List


class Solution:

    def find_occurance(self, nums, start, end, elem, first):
        res = None
        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == elem:
                res = mid
                if first:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < elem:
                start = mid + 1
            else:
                end = mid - 1

        return res

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = self.find_occurance(nums, 0, len(nums) - 1, target, True)
        right = self.find_occurance(nums, 0, len(nums) - 1, target, False)
        return [left, right] if left is not None else [-1, -1]


print(Solution().searchRange([5, 7, 7, 8, 10], 8))
