# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2 ** 31
        MAX_INT = 2 ** 31 - 1

        sign = -1 if x < 0 else 1
        x *= sign
        digits = []
        while x != 0:
            digits.append(x % 10)
            x //= 10

        num = 0
        for dig in digits:
            if sign > 0 and MAX_INT // 10 < num or (MAX_INT // 10 == num and dig > MAX_INT % 10):
                return 0
            elif sign < 0 and -1 * (-1 * MIN_INT // 10) > -1 * num or (
                    MIN_INT // 10 == -1 * num and dig > MIN_INT % 10):
                return 0
            else:
                num = num * 10 + dig

        return sign * num


print(Solution().reverse(-1563847412))
print(-2 ** 31)
