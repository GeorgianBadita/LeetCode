# https://leetcode.com/problems/find-center-of-star-graph/

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degree = {}
        max_degree = -1

        for edge in edges:
            u, v = edge
            max_degree = max(max_degree, u, v)

            if u not in degree:
                degree[u] = 1
            else:
                degree[u] = degree[u] + 1

            if v not in degree:
                degree[v] = 1
            else:
                degree[v] = degree[v] + 1

        for key in degree:
            if degree[key] == max_degree - 1:
                return key
