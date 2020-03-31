"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 01:49
"""


class Solution:
    def reverse(self, x: int) -> int:
        if 10 > x >= 0:
            return x
        if -1 >= x >= -9:
            return x
        MAX_INT_NEG = 2 ** 31
        MAX_INT_POZ = 2 ** 31 - 1
        sign = -1 if x < 0 else 1
        if x < 0:
            x = -x
        r = 0
        while x:
            if sign == -1 and MAX_INT_NEG > r * 10 and MAX_INT_NEG - r >= x % 10:
                r = r * 10 + x % 10
            elif sign == 1 and MAX_INT_POZ > r * 10 and MAX_INT_POZ - r >= x % 10:
                r = r * 10 + x % 10
            else:
                return 0
            x //= 10

        return r * sign


print(Solution().reverse(2 ** 31 - 1))
