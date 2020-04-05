"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   05.04.2020 19:58
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = []
        for i in range(0, 2 ** (len(nums))):
            sol = []
            for j in range(len(nums)):
                if i & (1 << j):
                    sol.append(nums[j])
            sols.append(sol)
        return sols


print(Solution().subsets([0]))
