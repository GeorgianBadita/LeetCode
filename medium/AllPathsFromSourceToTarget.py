# https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import List


class Solution:

    def __init__(self) -> None:
        self.__sols = []

    def generate_paths(self, sol: List[int], graph: List[List[int]]):
        current_node = sol[-1]
        for adj in graph[current_node]:
            sol.append(adj)
            if adj == len(graph) - 1:
                self.__sols.append([x for x in sol])
            self.generate_paths(sol, graph)
            sol.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.generate_paths([0], graph)
        return self.__sols


print(Solution().allPathsSourceTarget([[1, 2], [3], [3], []]))
