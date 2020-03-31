"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 19:59
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        rez = [[1], [1, 1]]
        for i in range(2, numRows):
            curr_row = [1]
            for j in range(1, i):
                curr_row.append(rez[i - 1][j - 1] + rez[i - 1][j])
            curr_row.append(1)
            rez.append(curr_row)
        return rez


print(*Solution().generate(2))
