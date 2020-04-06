"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   06.04.2020 22:49
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        result = 0
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        dividend = abs(dividend)
        divisor = abs(divisor)
        tmp = 0
        for i in range(31, -1, -1):
            if tmp + (divisor << i) <= dividend:
                if sign == -1 and abs(MIN_INT + (1 << i)) >= result:
                    tmp += (divisor << i)
                    result |= 1 << i
                elif sign == 1 and MAX_INT - (1 << i) >= result:
                    tmp += (divisor << i)
                    result |= 1 << i
                else:
                    return 2 ** 31 - 1

        return sign * result


print(Solution().divide(dividend=2**31, divisor=1))
