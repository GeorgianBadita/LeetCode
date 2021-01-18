# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1

        first = 0
        second = 1
        third = 1
        for _ in range(3, n + 1):
            current = first + second + third
            first = second
            second = third
            third = current
        return current
