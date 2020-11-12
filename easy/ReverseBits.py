# https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/648/

class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        for _ in range(32):
            bits.append(n % 2)
            n //= 2

        num = 0
        for i in range(32):
            num += bits[i] * (2 ** (32 - i - 1))

        return num
