# https://leetcode.com/problems/sort-the-matrix-diagonally/

from typing import List
import heapq


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat[0])):
            curr_col = i
            curr_row = 0
            heap = []
            while curr_col < len(mat[0]) and curr_row < len(mat):
                heapq.heappush(heap, mat[curr_row][curr_col])
                curr_col += 1
                curr_row += 1
            curr_col = i
            curr_row = 0
            while curr_col < len(mat[0]) and curr_row < len(mat):
                mat[curr_row][curr_col] = heapq.heappop(heap)
                curr_col += 1
                curr_row += 1
        for i in range(1, len(mat)):
            curr_col = 0
            curr_row = i
            heap = []
            while curr_col < len(mat[0]) and curr_row < len(mat):
                heapq.heappush(heap, mat[curr_row][curr_col])
                curr_col += 1
                curr_row += 1
            curr_col = 0
            curr_row = i
            while curr_col < len(mat[0]) and curr_row < len(mat):
                mat[curr_row][curr_col] = heapq.heappop(heap)
                curr_col += 1
                curr_row += 1
        return mat


mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
Solution().diagonalSort(mat)
