"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   11.04.2020 21:03
"""
from typing import List


class Solution:
    def dist(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0
        nr_sol = 0
        for i in range(len(points)):
            dct = {}
            for j in range(len(points)):
                dist = self.dist(points[i], points[j])
                if dct.get(dist):
                    dct[dist] += 1
                else:
                    dct[dist] = 1
            for v in dct.values():
                nr_sol += v * (v - 1)
        return nr_sol


print(Solution().numberOfBoomerangs([[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]))
