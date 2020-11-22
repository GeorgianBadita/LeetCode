# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

from typing import List


class Solution:

    def bsrch(self, el, vec, start, end):
        while start <= end:
            mid = start + (end - start) // 2
            if vec[mid] > el:
                end = mid - 1
            elif vec[mid] < el:
                start = mid + 1
            else:
                return True

        return False

    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for elem in mat[0]:
            exists_in_all = True
            for row in range(1, len(mat)):
                if not self.bsrch(elem, mat[row], 0, len(mat[row]) - 1):
                    exists_in_all = False
                    break
            if exists_in_all:
                return elem

        return -1
