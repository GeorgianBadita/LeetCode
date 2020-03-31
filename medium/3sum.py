"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   28.03.2020 21:40
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol_dict = {}

        for i in range(len(nums) - 1):
            target = -nums[i]
            local_dict = {}
            for j in range(i + 1, len(nums)):
                if target - nums[j] in local_dict:
                    if not (nums[j], nums[i], target - nums[j]) in sol_dict:
                        sol_dict[(nums[j], nums[i], target - nums[j])] = True
                local_dict[nums[j]] = nums[j]
        return [list(x) for x in sol_dict.keys()]


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
