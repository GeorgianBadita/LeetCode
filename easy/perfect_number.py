"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   11.04.2020 22:59
"""
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 6:
            return False
        return sum([x + num // x for x in range(1, int(math.sqrt(num)) + 1) if num % x == 0]) // 2 == num


print(Solution().checkPerfectNumber(7))
