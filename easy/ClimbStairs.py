# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        a = 1
        b = 2
        c = 0
        for _ in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return c
