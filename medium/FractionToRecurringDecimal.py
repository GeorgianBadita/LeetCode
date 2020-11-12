# https://leetcode.com/problems/fraction-to-recurring-decimal/submissions/

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
        seen = {}
        pos = 0

        while numerator != 0:
            if numerator in seen:
                break
            res = numerator // denominator
            result.append(str(res))
            if len(result) == 1:
                result.append('.')
            seen[numerator] = pos
            pos += 1
            numerator = numerator % denominator
            numerator *= 10

        if numerator != 0:
            result.insert(seen[numerator] + 1, '(')
            result.append(')')

        if sign:
            result.insert(0, sign)
        return ''.join(result)

print(Solution().fractionToDecimal(1232, 990))
