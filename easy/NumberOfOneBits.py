# https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/565/

class Solution:
    def hammingWeight(self, n: int) -> int:
        num_1_bits = 0
        for pow_2 in range(32):
            if n & (1 << pow_2):
                num_1_bits += 1

        return num_1_bits