"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   05.04.2020 00:02
"""
from typing import List


class Solution:

    def bkt(self, sol, used, nums, sols):
        for i in range(len(nums)):
            if not used[i]:
                sol.append(nums[i])
                used[i] = True
                if len(sol) == len(nums):
                    sols.append(list(sol))
                self.bkt(sol, used, nums, sols)
                used[i] = False
                sol.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        used = [False] * len(nums)
        sols = []
        self.bkt([], used, nums, sols)
        return sols


print(Solution().permute([1, 2, 3]))
