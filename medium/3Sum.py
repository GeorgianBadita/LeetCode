# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        triplets = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    triplets.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif curr_sum < 0:
                    left += 1

                elif curr_sum > 0:
                    right -= 1

        triplets = list(triplets)
        for i in range(len(triplets)):
            triplets[i] = list(triplets[i])
        return triplets


Solution().threeSum([-1, 0, 1, 2, -1, -4])
