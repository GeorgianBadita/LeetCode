"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   06.04.2020 21:49
"""


class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        i = 0
        j = len(matrix[0]) - 1

        while len(matrix) > i >= 0 and len(matrix[0]) > j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


print(Solution().searchMatrix(
    [[1, 1]], 1
    ))
