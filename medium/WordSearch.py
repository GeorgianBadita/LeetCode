# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/797/

from typing import List


class Solution:

    def valid_coords(self, x, y, board):
        return x >= 0 and y >= 0 and x < len(board) and y < len(board[0])

    def find_word(self, board, word, x, y):
        if len(word) == 0:
            return True

        current_letter = word[0]
        if not self.valid_coords(x, y, board) or board[x][y] != current_letter:
            return False

        current_board_value = board[x][y]

        board[x][y] = -1

        found = False
        for row, col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rest_word = word[1:]
            found = self.find_word(board, rest_word, x + row, y + col)
            if found:
                break

        board[x][y] = current_board_value
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.find_word(board, word, i, j):
                        return True
        return False
