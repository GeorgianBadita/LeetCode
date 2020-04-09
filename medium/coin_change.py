"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   09.04.2020 21:09
"""
from typing import List
import sys

sys.setrecursionlimit(2 ** 31 - 1)


class Solution:

    def dp_rec(self, coins, amount, res):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if res[amount - 1]:
            return res[amount - 1]

        min_cost = 2 ** 31 - 1
        for coin in coins:
            cnt = self.dp_rec(coins, amount - coin, res)
            if 0 <= cnt < min_cost:
                min_cost = 1 + cnt
        res[amount - 1] = min_cost if min_cost != 2 ** 31 - 1 else -1

        return res[amount - 1]

    def dp_iter(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            mn = dp[i]
            for coin in coins:
                if i - coin >= 0:
                    mn = min(mn, dp[i - coin] + 1)
            dp[i] = mn
        return -1 if dp[amount] > amount else dp[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        return self.dp_iter(coins, amount)


print(Solution().coinChange([1], 11))
