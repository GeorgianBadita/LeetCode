# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/818/

class Solution:

    def compute_pow(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            half_pow = self.compute_pow(x, n // 2)
            return half_pow ** 2
        else:
            return x * self.compute_pow(x, n - 1)

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        return self.compute_pow(x, n)

print(Solution().myPow(2.000, 10))