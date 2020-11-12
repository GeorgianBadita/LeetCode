# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return 0

        points = sorted(points, key=lambda x: x[0])
        max_area = points[1][0] - points[0][0]
        for i in range(2, len(points)):
            if points[i][0] - points[i - 1][0] > max_area:
                max_area = points[i][0] - points[i - 1][0]

        return max_area
