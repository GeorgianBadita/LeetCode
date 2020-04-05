"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   05.04.2020 23:34
"""
from typing import List


def can_overlap(int1, int2):
    return not (int1[1] < int2[0] or int1[0] > int2[1])


def merge(int1, int2):
    return [min(int1[0], int2[0]), max(int2[1], int1[1])]


def create_graph(intervals):
    graph = [[] for _ in range(len(intervals))]
    for i in range(len(intervals) - 1):
        for j in range(i + 1, len(intervals)):
            if can_overlap(intervals[i], intervals[j]):
                graph[i].append(j)
                graph[j].append(i)
    return graph


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = create_graph(intervals)
        visited = [False] * len(intervals)

        def bfs(graph, visited, node):
            node_in_comp = []
            queue = [node]
            visited[node] = True
            while len(queue) > 0:
                curr_node = queue[0]
                node_in_comp.append(curr_node)
                queue.pop(0)
                for neighbour in graph[curr_node]:
                    if not visited[neighbour]:
                        queue.append(neighbour)
                        visited[neighbour] = True
            return node_in_comp

        merged_intervals = []
        for i in range(len(intervals)):
            if not visited[i]:
                to_merge = bfs(graph, visited, i)
                merged = intervals[to_merge[0]]
                for ii in range(1, len(to_merge)):
                    merged = merge(merged, intervals[to_merge[ii]])
                merged_intervals.append(merged)

        return merged_intervals


print(can_overlap([1, 4], [0, 1]))

print(Solution().merge([[1, 4], [0, 1]]))
