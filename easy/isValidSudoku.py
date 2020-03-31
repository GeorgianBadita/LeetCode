"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 00:55
"""
from typing import List


def check_col(board):
    for j in range(len(board[0])):
        freq_col = [False] * 10
        for i in range(len(board)):
            if board[i][j] != '.':
                dig = int(board[i][j])
                if freq_col[dig] is True:
                    return False
                freq_col[dig] = True
    return True


def check_line(board):
    for i in range(len(board)):
        freq_lin = [False] * 10
        for j in range(len(board[0])):
            if board[i][j] != '.':
                dig = int(board[i][j])
                if freq_lin[dig] is True:
                    return False
                freq_lin[dig] = True
    return True


def check_sq(board):
    num_squares = 9
    starti = 0
    startj = 0
    endi = 2
    endj = 2
    while num_squares:

        freq_sq = [False] * 10

        for i in range(starti, endi + 1):
            for j in range(startj, endj + 1):
                if 0 <= i < len(board) and 0 <= j < len(board[0]):
                    if board[i][j] != '.':
                        dig = int(board[i][j])
                        if freq_sq[dig] is True:
                            return False
                        freq_sq[dig] = True
        startj += 3
        endj += 3
        if endj >= 9 or startj >= 9:
            starti += 3
            endi += 3
            endj = 2
            startj = 0
        num_squares -= 1
    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return check_sq(board) and check_line(board) and check_col(board)


print(Solution().isValidSudoku(
    [[".", ".", ".", ".", ".", ".", "5", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."], ["9", "3", ".", ".", "2", ".", "4", ".", "."],
     [".", ".", "7", ".", ".", ".", "3", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", "3", "4", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "."],
     [".", ".", ".", ".", ".", "5", "2", ".", "."]]
))
