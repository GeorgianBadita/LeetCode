# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/

from typing import List


class Solution:

    def __init__(self):
        self.used = []
        self.sols = []

    def is_consistent(self, sol, num_to_add, nums):
        return len(sol) <= len(nums) and self.used[num_to_add] is False

    def is_sol(self, sol, nums):
        return len(sol) == len(nums)

    def backtrack(self, sol, nums):
        for i in range(len(nums)):
            if self.is_consistent(sol, i, nums):
                self.used[i] = True
                sol.append(i)
                if self.is_sol(sol, nums):
                    self.sols.append([nums[x] for x in sol])
                self.backtrack(sol, nums)
                sol.pop()
                self.used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [False for i in range(len(nums))]
        self.backtrack([], nums)
        return self.sols


print(Solution().permute([1, 2, 3]))
