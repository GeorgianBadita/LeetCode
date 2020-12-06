# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

from typing import List


class Solution:
    def __count_matrices_of_size(self, matrix, size):
        count = 0
        for i in range(len(matrix) - size + 1):
            for j in range(len(matrix[0]) - size + 1):
                row_start = i
                row_end = i + size
                col_start = j
                col_end = j + size
                is_square = True
                for row in range(row_start, row_end):
                    continue_square = True
                    for col in range(col_start, col_end):
                        if matrix[row][col] != 1:
                            is_square = False
                            continue_square = False
                            break
                    if not continue_square:
                        break
                if is_square:
                    count += 1
        return count

    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0
        for i in range(1, min(len(matrix), len(matrix[0])) + 1):
            res = self.__count_matrices_of_size(matrix, i)
            if res == 0:
                break
            result += res
        return res