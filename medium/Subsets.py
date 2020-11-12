# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/

from typing import List

class Solution:

    def __init__(self):
        self.sols = []

    def is_consistent(self, sol, elem):
        if len(sol) == 0:
            return True
        return elem > sol[-1]

    def is_sol(self, sol):
        return True

    def backtrack(self, sol, nums):
        for elem in nums:
            if self.is_consistent(sol, elem):
                sol.append(elem)
                if self.is_sol(sol):
                    self.sols.append([x for x in sol])
                self.backtrack(sol, nums)
                sol.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack([], nums)
        self.sols.append([])
        return self.sols

print(Solution().subsets([1, 2, 3]))
