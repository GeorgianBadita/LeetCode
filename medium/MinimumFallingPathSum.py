# https://leetcode.com/problems/minimum-falling-path-sum/

from typing import List


class Solution:

    def valid_coords(self, x, y, matrix):
        return x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[-1])

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        for i in range(len(matrix)):
            for j in range(len(matrix[-1])):
                vals = []
                if self.valid_coords(i - 1, j + 1, matrix):
                    vals.append(matrix[i - 1][j + 1])
                if self.valid_coords(i - 1, j, matrix):
                    vals.append(matrix[i - 1][j])
                if self.valid_coords(i - 1, j - 1, matrix):
                    vals.append(matrix[i - 1][j - 1])
                if vals:
                    matrix[i][j] += min(vals)

        return min(matrix[-1])


print(Solution().minFallingPathSum([[-19, 57], [-40, -5]]))
