"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   11.04.2020 22:33
"""

import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + math.sqrt(1 + 8 * n)) / 2)


print(Solution().arrangeCoins(13))
