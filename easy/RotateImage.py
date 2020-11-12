# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or (len(matrix) == 1 and len(matrix[0]) == 1):
            return

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix[i]) // 2):
                matrix[i][j], matrix[i][len(matrix[i]) - j - 1] = matrix[i][len(matrix[i]) - j - 1], matrix[i][j]


Solution().rotate([[1, 2], [3, 4]])
