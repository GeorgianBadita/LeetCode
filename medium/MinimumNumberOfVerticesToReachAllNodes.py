# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        in_degree = [0] * n

        for edge in edges:
            in_degree[edge[1]] += 1

        return [x for x in range(n) if in_degree[x] == 0]
