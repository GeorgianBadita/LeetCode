"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 23:14
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        MAX_INT = 2 ** 31 - 1
        MIN_INT = 2 ** 31
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        while i < len(s) and s[i] == '0':
            i += 1

        if i == len(s) or s[i] not in [str(x) for x in range(1, 10)] + ['-', '+']:
            return 0
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            if i > 0 and s[i - 1] == '0':
                return 0
            i += 1
        if i == len(s):
            return 0
        num = 0
        while i < len(s) and '0' <= s[i] <= '9':
            dig = int(s[i])
            if sign == 1 and MAX_INT / 10 > num and MAX_INT - num * 10 > dig:
                num = num * 10 + dig
                i += 1
                continue
            if sign == -1 and MIN_INT / 10 > num and MIN_INT - num * 10 > dig:
                num = num * 10 + dig
                i += 1
                continue
            if sign == -1:
                return MIN_INT * sign
            if sign == 1:
                return MAX_INT
            i += 1
        return num*sign


print(Solution().myAtoi("0-1"))
