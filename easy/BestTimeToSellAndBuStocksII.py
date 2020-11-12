# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0

        for i in range(1, len(prices)):
            curr_profit = max(curr_profit, curr_profit + prices[i] - prices[i - 1])

        return curr_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
