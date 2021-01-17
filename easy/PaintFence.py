# https://leetcode.com/problems/paint-fence/


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k**2

        first = k
        second = k * k
        for _ in range(2, n):
            third = (first + second) * (k - 1)
            first = second
            second = third
        return third
