# https://leetcode.com/problems/buildings-with-an-ocean-view/

from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        max_height = -1
        sol = []

        for index in range(len(heights) - 1, -1, -1):
            if heights[index] > max_height:
                sol.append(index)
            max_height = max(max_height, heights[index])

        return list(reversed(sol))
