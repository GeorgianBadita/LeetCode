# https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/


class Solution:

    def two_complement(self, num):
        start_flipping = False
        for bit in range(32):
            it_hbit = 1 if num & (1 << bit) > 0 else 0
            if start_flipping:
                if it_hbit == 0:
                    num |= (1 << bit)
                else:
                    num = num & ~(1 << bit)
            if it_hbit > 0:
                start_flipping = True

        return num

    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b

        if b == 0:
            return a

        both_neg = False
        if a < 0 and b < 0:
            a *= - 1
            b *= -1
            both_neg = True

        one_neg = False
        abs_criteria = False
        if a < 0 or b < 0 and not both_neg:
            one_neg = True
            if a < 0 and abs(a) > abs(b):
                abs_criteria = True
            elif b < 0 and abs(b) > abs(a):
                abs_criteria = True
        result = 0
        carry = 0
        for bit in range(0, 32):
            value_a = 1 if a & (1 << bit) > 0 else 0
            value_b = 1 if b & (1 << bit) > 0 else 0

            last_carry = carry
            if value_a == 1 and value_b == 1:
                if last_carry == 1:
                    result |= (1 << bit)
                    carry = 1
                else:
                    carry = 1
            elif value_a == 1 or value_b == 1:
                if last_carry == 0:
                    result |= (1 << bit)
                    carry = 0
                else:
                    carry = 1
            else:
                if last_carry == 1:
                    result |= (1 << bit)
                    carry = 0

        if both_neg:
            return -result
        if one_neg and abs_criteria:
            return -self.two_complement(result)
        return result
