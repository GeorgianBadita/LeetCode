# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        cnt = 0
        for par in S:
            if par == "(":
                stack.append(par)
            else:
                if stack:
                    stack.pop()
                else:
                    cnt += 1
        return cnt + len(stack)