"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   12.04.2020 23:15
"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) <= K:
            return points
        heap = []
        for point in points:
            heappush(heap, (-(point[0] ** 2 + point[1] ** 2), point))
            if len(heap) > K:
                heappop(heap)

        return [heappop(heap)[1] for _ in range(K)]


lst = [[3, 3], [5, -1], [-2, 4]]
K = 2

print(Solution().kClosest(lst, K))
