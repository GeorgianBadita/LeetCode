# https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/721/

class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []
        for par in s:
            if par in parenthesis.values():
                stack.append(par)
            else:
                if not stack or stack[-1] != parenthesis[par]:
                    return False
                stack.pop()

        return len(stack) == 0
