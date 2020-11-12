# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793/

from typing import List


class Solution:

    
    def __init__(self):
        self.sols = []
        self.mapping = {
        "2": 'abc',
        "3": 'def',
        "4": 'ghi',
        "5": 'jkl',
        "6": 'mno',
        "7": 'pqrs',
        "8": 'tuv',
        "9": 'wxyz'
    }

    def is_consistent(self, sol, child, digits):
        return len(sol + [child]) <= len(digits)
    
    def is_sol(self, sol, digits):
        return len(sol) == len(digits)

    def find_combs(self, sol, digits):
        if len(sol) < len(digits):
            for child in self.mapping[digits[len(sol)]]:
                if self.is_consistent(sol, child, digits):
                    sol.append(child)
                    if self.is_sol(sol, digits):
                        self.sols.append("".join(sol))
                    self.find_combs(sol, digits)
                    sol.pop()


    def letterCombinations(self, digits: str) -> List[str]:
        self.find_combs([], digits)
        return self.sols

print(Solution().letterCombinations("232"))
