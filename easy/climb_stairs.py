"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 22:39
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        a, b = 2, 3
        for _ in range(3, n):
            c = a + b
            a = b
            b = c
        return c


print(Solution().climbStairs(5))
