# https://leetcode.com/problems/unique-paths-iii/

from typing import List
from functools import reduce


class Solution:
    def __init__(self):
        self.__num_paths = 0
        self.__num_ones = 0
        self.__path_length = 1
        self.__dx = [-1, 0, 0, 1]
        self.__dy = [0, 1, -1, 0]

    def valid_coords(self, x, y, grid):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

    def __generate_paths(self, x, y, grid: List[List[int]]) -> None:
        for i in range(len(self.__dx)):
            new_x = x + self.__dx[i]
            new_y = y + self.__dy[i]
            if self.valid_coords(new_x, new_y, grid) and grid[new_x][new_y] not in [
                -1,
                1,
            ]:
                current_val = grid[x][y]
                grid[x][y] = -1
                self.__path_length += 1
                if (
                    grid[new_x][new_y] == 2
                    and self.__path_length == len(grid) * len(grid[0]) - self.__num_ones
                ):
                    self.__num_paths += 1
                self.__generate_paths(new_x, new_y, grid)

                self.__path_length -= 1
                grid[x][y] = current_val

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.__num_ones = sum([row.count(-1) for row in grid])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.__generate_paths(i, j, grid)
                    return self.__num_paths


print(Solution().uniquePathsIII([[0, 1], [2, 0]]))
