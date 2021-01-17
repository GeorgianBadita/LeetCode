# https://leetcode.com/problems/min-cost-climbing-stairs/


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        if len(cost) <= 2:
            return min(cost)

        cost.append(0)

        first = cost[0]
        second = cost[1]

        for i in range(2, len(cost)):
            third = cost[i] + min(first, second)
            first = second
            second = third

        return min(first, third)
