"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   06.04.2020 23:40
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for j in range(len(dp[0])):
            dp[0][j] = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


print(Solution().uniquePaths(7, 3))
