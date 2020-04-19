"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   19.04.2020 23:43
"""
from typing import List


class Solution:
    def valid_node(self, node, length):
        return 0 <= node < length

    def construct_graph(self, lst):
        graph = {}
        for i in range(len(lst)):
            nodes = []
            if self.valid_node(i - lst[i], len(lst)):
                nodes.append((lst[i - lst[i]], i - lst[i]))
            if self.valid_node(i + lst[i], len(lst)):
                nodes.append((lst[i + lst[i]], i + lst[i]))

            if not graph.get((lst[i], i)):
                graph[(lst[i], i)] = nodes
            else:
                graph[(lst[i], i)] += nodes
        return graph

    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 not in arr:
            return False
        graph = self.construct_graph(arr)
        visited = {(arr[start], start)}
        queue = [(arr[start], start)]

        while len(queue):
            curr_node = queue.pop(0)
            value, index = curr_node
            if value == 0:
                return True
            if graph.get(curr_node):
                for node in graph[curr_node]:
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)
        return False


print(Solution().canReach([3, 0, 2, 1, 2], 2))
