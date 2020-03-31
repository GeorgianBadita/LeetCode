"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 00:24
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = 0
        while x or y:
            if x & 1 != y & 1:
                diff += 1
            x >>= 1
            y >>= 1
        return diff


print(Solution().hammingDistance(1, 4))
