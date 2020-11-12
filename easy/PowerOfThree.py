# https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/745/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        max_3pow = 3 ** 19
        return max_3pow % n == 0
