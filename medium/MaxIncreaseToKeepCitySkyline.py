# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

from typing import List


class Solution:

    def get_row_maxes(self, grid):
        return [max(row) for row in grid]

    def get_col_maxes(self, grid):
        col_maxes = []
        for j in range(len(grid[0])):
            col_max = grid[0][j]
            for i in range(len(grid)):
                if grid[i][j] > col_max:
                    col_max = grid[i][j]
            col_maxes.append(col_max)
        return col_maxes

    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_maxes = self.get_row_maxes(grid)
        col_maxes = self.get_col_maxes(grid)

        max_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_sum += min(abs(row_maxes[i] - grid[i][j]),
                               abs(col_maxes[j] - grid[i][j]))
        return max_sum
