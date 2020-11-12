# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/820/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        result = 0
        sign = 1
        if dividend < 0:
            sign *= -1
            dividend *= -1

        if divisor < 0:
            sign *= -1
            divisor *= -1

        two_pows = []
        values = []
        initial_divisor = divisor
        two_power = 1
        while dividend >= initial_divisor:
            values.append(initial_divisor)
            two_pows.append(two_power)
            two_power += two_power
            initial_divisor += initial_divisor

        for i in range(len(values) - 1, -1, -1):
            if values[i] <= dividend:
                dividend -= values[i]
                result += two_pows[i]

        return result * sign
