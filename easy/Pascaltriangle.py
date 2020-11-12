# https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/601/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # base cases
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        triangle = [[1], [1, 1]]
        for i in range(2, numRows):
            triangle_row = []
            for j in range(len(triangle[i - 1]) + 1):
                if j == 0 or j == len(triangle):
                    triangle_row.append(1)
                else:
                    triangle_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(triangle_row)
        return triangle
