# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = depth
        for char in s:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            max_depth = max(max_depth, depth)
        return max_depth