# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

from typing import List


class Solution:

    def is_valid_lines(self, board):
        for line in board:
            vis = 0
            for value in line:
                if value != ".":
                    int_value = int(value)
                    if vis & (1 << int_value):
                        return False
                    vis |= (1 << int_value)
        return True

    def is_valid_cols(self, board):
        for col in range(len(board[0])):
            vis = 0
            for line in range(len(board)):
                if board[line][col] != ".":
                    int_value = int(board[line][col])
                    if vis & (1 << int_value):
                        return False
                    vis |= (1 << int_value)
        return True

    def is_valid_squares(self, board):
        start_x = 0
        stop_x = 2
        start_y = 0
        stop_y = 2
        num_squares = 9
        while num_squares > 0:
            vis = 0
            for line in range(start_y, stop_y + 1):
                for col in range(start_x, stop_x + 1):
                    if board[line][col] != ".":
                        int_value = int(board[line][col])
                        if vis & (1 << int_value):
                            return False
                        vis |= (1 << int_value)

            if stop_x == 8:
                start_x = 0
                stop_x = 2
                start_y += 3
                stop_y += 3
            else:
                start_x += 3
                stop_x += 3
            num_squares -= 1

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.is_valid_cols(board) and self.is_valid_lines(board) and self.is_valid_squares(board)


print(Solution().isValidSudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))
