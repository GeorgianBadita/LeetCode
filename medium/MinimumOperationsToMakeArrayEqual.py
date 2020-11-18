# https://leetcode.com/problems/minimum-operations-to-make-array-equal/

class Solution:
    def minOperations(self, n: int) -> int:

        total_ops = 0
        for num in range(n // 2):
            total_ops += n - (2*num + 1)

        return total_ops
