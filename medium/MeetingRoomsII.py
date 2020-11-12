# https://leetcode.com/explore/interview/card/top-interview-question

from typing import List
from heapq import *


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1

        intervals = sorted(intervals, key=lambda meeting: meeting[0])
        time_heap = []
        heappush(time_heap, (intervals[0][1], intervals[0]))
        num_rooms = 1

        for i in range(1, len(intervals)):
            current_meeting = intervals[i]
            fastest_time = time_heap[0][0]

            if current_meeting[0] >= fastest_time:
                heappop(time_heap)
                heappush(time_heap, (current_meeting[1], current_meeting))
            else:
                num_rooms += 1
                heappush(time_heap, (current_meeting[1], current_meeting))

        return num_rooms
