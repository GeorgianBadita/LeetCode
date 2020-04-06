"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   06.04.2020 22:02
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_zeros = 0
        pow = 5

        while n // pow:
            num_zeros += n // pow
            pow *= 5

        return num_zeros


print(Solution().trailingZeroes(25))
