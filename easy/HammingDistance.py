# https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/762/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_dist = 0
        for pow_2 in range(32):
            if 1 << pow_2 > x and 1 << pow_2 > y:
                break

            hamming_dist += 1 if (x & 1 << pow_2) != (y & 1 << pow_2) else 0

        return hamming_dist


Solution().hammingDistance(1, 4)
