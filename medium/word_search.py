"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   05.04.2020 20:49
"""
from typing import List


def is_valid_poz(i, j, grid, char):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == char


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bkt(sol, board, x, y, word, count):
    if count == len(word):
        return True
    for i in range(4):
        if is_valid_poz(x + dx[i], y + dy[i], board, word[count]) and (x + dx[i], y + dy[i]) not in sol:
            sol.add((x + dx[i], y + dy[i]))
            check = bkt(sol, board, x + dx[i], y + dy[i], word, count + 1)
            if check:
                return True
            else:
                sol.remove((x + dx[i], y + dy[i]))
    return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if bkt({(i, j)}, board, i, j, word, 1):
                        return True
        return False


board = [
    ["A", "B", "C"]
]
print(Solution().exist(board, "AB"))
