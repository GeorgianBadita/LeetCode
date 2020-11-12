# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/

from typing import List


class Solution:

    def is_valid_coord(self, x, y, grid):
        return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])

    def mark_island(self, grid, x, y):
        grid[x][y] = '#'

        for x_inc, y_inc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if self.is_valid_coord(x + x_inc, y + y_inc, grid) and grid[x + x_inc][y + y_inc] == '1':
                self.mark_island(grid, x + x_inc, y + y_inc)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    self.mark_island(grid, i, j)
        return num_islands
