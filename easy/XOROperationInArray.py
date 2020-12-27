# https://leetcode.com/problems/xor-operation-in-an-array/


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = start
        for i in range(1, n):
            xor = xor ^ (2 * i + start)
        return xor
