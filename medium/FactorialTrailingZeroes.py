# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/816/

class Solution:

    def trailingZeroes(self, n: int) -> int:
        num_zeros = 0
        five_pow = 5
        while n // five_pow > 0:
            num_zeros += n // five_pow
            five_pow *= 5
        return num_zeros

print(Solution().trailingZeroes(30))