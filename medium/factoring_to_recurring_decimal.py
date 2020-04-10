"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   09.04.2020 22:49
"""


class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        if numerator % denominator == 0:
            return str(numerator // denominator)
        sign = '-' if (numerator < 0) ^ (denominator < 0) else None
        if numerator < 0:
            numerator *= -1
        if denominator < 0:
            denominator *= -1

        result = []
        repeat_dict = {}
        poz = 0
        while True:
            if numerator in repeat_dict:
                break
            repeat_dict[numerator] = poz
            if numerator == 0:
                break
            res = numerator // denominator
            result.append(str(res))
            poz += 1
            if len(result) == 1:
                result.append('.')
            numerator -= res * denominator
            numerator *= 10
        if numerator != 0:
            poz = repeat_dict[numerator]
            result.insert(1 + poz, '(')
            result.append(')')
        if sign is not None:
            result.insert(0, '-')
        return ''.join(result)


print(Solution().fractionToDecimal(-50, -8))
