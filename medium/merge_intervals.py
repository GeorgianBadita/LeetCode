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


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        result = []
        interval = intervals[0]
        for i in range(1, len(intervals)):
            if can_overlap(interval, intervals[i]):
                interval = merge(interval, intervals[i])
            else:
                result.append(interval)
                interval = intervals[i]
        result.append(interval)
        return result


print(Solution().merge([[1, 4], [1, 1]]))
