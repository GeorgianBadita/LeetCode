# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/


from typing import List


class Solution:

    def find_peak(self, nums, lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] > nums[mid - 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1

        return self.find_peak(nums, 0, len(nums) - 1)


print(Solution().findPeakElement([1,2,1,3,5,6,4]))
