"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   09.04.2020 22:49
"""


class Solution:

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    # TODO this
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        if numerator // denominator == numerator / denominator:
            return str(numerator // denominator)
        gcd = self.gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd
        until_period = []
        after_period = []
        numerator_dict = dict()
        while numerator * 10 < denominator * 10:
            numerator *= 10
            until_period.append('0')
        is_cycle = False
        dig_pos = 0
        period_info = None
        float_ = None
        while numerator != 0:
            if numerator in numerator_dict:
                is_cycle = True
                period_info = numerator_dict[numerator]
                break
            numerator_dict[numerator] = dig_pos
            res = numerator // denominator
            dig_pos += 1
            after_period.append(str(res))
            numerator -= res * denominator
            if float_ is None and numerator < denominator:
                float_ = dig_pos
            numerator *= 10

        cnt = 0
        while abs(-cnt - 1) < len(after_period) and after_period[-cnt - 1] == '0':
            cnt += 1
        cnt1 = 0
        while abs(-cnt1 - 1) < len(until_period) and until_period[-cnt1 - 1] == '0':
            cnt1 += 1
        cnt = min(cnt1, cnt)
        if cnt > 0:
            result = until_period + after_period[:-cnt]
        else:
            result = until_period + after_period
        result.insert(1, '.')
        if is_cycle:
            print(float_)
            if period_info == 0:
                float_ = 0
                k = 0
            else:
                k = len(until_period)
            result.insert(2 + period_info - float_ + k, '(')
            result.append(')')
        return ''.join(result)


print(Solution().fractionToDecimal(1, 90))
