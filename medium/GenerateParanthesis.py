# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/

from typing import List


class Solution:

    def __init__(self):
        self.paranthesis = "()"
        self.sols = []

    def is_consistent(self, solution, par, n):
        count_open = solution.count("(")
        count_closed = solution.count(")")

        if par == '(':
            count_open += 1
        else:
            count_closed += 1

        return count_closed <= n // 2 and count_open <= n // 2 and count_closed <= count_open and len(solution + [par]) <= n

    def is_sol(self, solution, n):
        return len(solution) == n

    def backtrack(self, sol, n):
        for par in self.paranthesis:
            if self.is_consistent(sol, par, n):
                sol.append(par)
                if self.is_sol(sol, n):
                    self.sols.append("".join(sol))
                self.backtrack(sol, n)
                sol.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrack([], 2*n)
        return self.sols

print(Solution().generateParenthesis(3))
