"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   06.04.2020 22:05
"""


class Solution:

    def myPow(self, x: float, n: int) -> float:

        def pow_helper(a, n):
            res = 1
            while n > 0:
                if n & 1 == 1:
                    res *= a
                n >>= 1
                a = a * a

            return res

        if n == 0:
            return 1
        if n < 0:
            return 1 / pow_helper(x, -n)
        return pow_helper(x, n)


print(Solution().myPow(2.0,
                       12))

