# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806/

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        start_row = len(matrix) - 1
        start_col = 0

        while start_row >= 0 and start_col < len(matrix[0]):
            if matrix[start_row][start_col] > target:
                start_row -= 1
            elif matrix[start_row][start_col] < target:
                start_col += 1
            else:
                return True

        return False
