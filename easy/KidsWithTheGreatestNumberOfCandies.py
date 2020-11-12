# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        if not candies:
            return candies

        max_candies = max(candies)
        return [True if elem + extraCandies >=
                  max_candies else False for elem in candies]
