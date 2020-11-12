# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/804/

from typing import List


class Solution:

    def find_offset(self, nums, start, end):
        while start <= end:
            mid = start + (end - start + 1) // 2

            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] > nums[0]:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    def bsrch(self, nums, start, end, target):
        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        offset = self.find_offset(nums, 0, len(nums) - 1)
        if offset == -1:
            return self.bsrch(nums, 0, len(nums) - 1, target)

        first_side = self.bsrch(nums, 0, offset, target)

        if first_side >= 0:
            return first_side

        return self.bsrch(nums, offset + 1, len(nums) - 1, target)


print(Solution().search([3, 1], 3))
