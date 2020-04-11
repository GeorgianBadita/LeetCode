"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   12.04.2020 00:28
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        dp = (num + 1) * [0]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, num + 1):
            if (i & (i - 1)) == 0:
                dp[i] = 1
                continue
            if i % 2 == 0:
                dp[i] = dp[i >> 1]
            else:
                dp[i] = 1 + dp[i - 1]
        return dp

print(Solution().countBits(16))
