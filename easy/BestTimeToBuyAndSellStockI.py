# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        max_profit = float('-inf')
        smallest_left = prices[0]
        for i in range(1, len(prices)):
            if smallest_left < prices[i]:
                max_profit = max(max_profit, prices[i] - smallest_left)

            smallest_left = min(smallest_left, prices[i])

        return max_profit if max_profit > 0 else 0
