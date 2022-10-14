# https://leetcode.com/problems/bus-routes/

from typing import List

class Solution:
    def intersect(self, a, b):
        i, j = 0, 0

        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                return True
            if a[i] < b[j]:
                i += 1
            else:
                j += 1

        return False


    def bsrch(self, lst, target):
        l, r = 0, len(lst) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if lst[mid] == target:
                return True
            if lst[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        if not routes:
            return -1

        graph = []
        for idx in range(len(routes)):
            routes[idx] = sorted(routes[idx])
            graph.append([])

        for idx in range(len(routes)):
            for jdx in range(idx + 1, len(routes)):
                if self.intersect(routes[idx], routes[jdx]):
                    graph[idx].append(jdx)
                    graph[jdx].append(idx)


        seen = set()
        targets = set()
        queue = []

        for idx in range(len(routes)):
            if self.bsrch(routes[idx], source):
                seen.add(idx)
                queue.append((idx, 0))
            if self.bsrch(routes[idx], target):
                targets.add(idx)

        while queue:
            node, depth = queue.pop(0)
            if node in targets:
                return depth + 1

            for child in graph[node]:
                if child not in seen:
                    seen.add(child)
                    queue.append((child, depth + 1))

        return -1