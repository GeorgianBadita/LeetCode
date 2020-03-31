"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 19:46
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        while n:
            bits.append(n & 1)
            n //= 2

        while len(bits) != 32:
            bits.append(0)

        fin = 0
        power = 1
        for i in range(31, -1, -1):
            fin += power*bits[i]
            power *= 2

        return fin


print(Solution().reverseBits(4294967293))
