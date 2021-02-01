# https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = [0] * (365 + 30 + 1)

        dayset = set(days)

        for i in range(365, 0, -1):
            if i not in dayset:
                dp[i] = dp[i + 1]
            else:
                dp[i] = min(dp[i + 1] + costs[0], dp[i + 7] +
                            costs[1], dp[i + 30] + costs[2])

        return dp[1]
