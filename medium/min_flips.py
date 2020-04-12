"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   12.04.2020 23:25
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        num_flips = 0
        for i in range(32):
            bit_c = c & 1
            bit_b = b & 1
            bit_a = a & 1
            c >>= 1
            b >>= 1
            a >>= 1

            if bit_a | bit_b != bit_c:
                if bit_c == 0 and bit_a == 1 and bit_b == 1:
                    num_flips += 2
                else:
                    num_flips += 1
            if a == b == c == 0:
                break
        return num_flips


print(Solution().minFlips(2, 6, 5))
