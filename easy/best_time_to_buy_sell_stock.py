"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 01:36
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        while i < len(prices):
            while i + 1 < len(prices) and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i + 1 < len(prices) and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]

            max_profit += (peak - valley)
            i += 1

        return max_profit


print(Solution().maxProfit([1, 2, 3, 4, 5]))
