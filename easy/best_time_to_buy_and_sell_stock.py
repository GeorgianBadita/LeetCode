"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 22:46
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 2 ** 31
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
