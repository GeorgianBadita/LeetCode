# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]
        while sum(rowSum + colSum) > 0:
            min_row_val = 1e9
            min_row_index = -1
            min_col_val = 1e9
            min_col_index = -1
            for i in range(len(rowSum)):
                if rowSum[i] != 0 and rowSum[i] < min_row_val:
                    min_row_val = rowSum[i]
                    min_row_index = i
            for i in range(len(colSum)):
                if colSum[i] != 0 and colSum[i] < min_col_val:
                    min_col_val = colSum[i]
                    min_col_index = i
            if min_row_val <= min_col_val:
                matrix[min_row_index][min_col_index] = min_row_val
                rowSum[min_row_index] = 0
                colSum[min_col_index] -= min_row_val
            else:
                matrix[min_row_index][min_col_index] = min_col_val
                colSum[min_col_index] = 0
                rowSum[min_row_index] -= min_col_val
        return matrix


print(Solution().restoreMatrix([3, 8], [4, 7]))
