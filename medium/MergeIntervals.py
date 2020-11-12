# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/

from typing import List


class Solution:

    def can_merge(self, first_int, second_int):
        if first_int[0] == second_int[0]:
            return True
        return second_int[0] <= first_int[1] or first_int[1] >= second_int[1]

    def merge_intervals(self, first_int, second_int):
        return [min([first_int[0], second_int[0]]), max([first_int[1], second_int[1]])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        intervals = []
        curr_interval = sorted_intervals[0]
        for i in range(1, len(sorted_intervals)):
            if self.can_merge(curr_interval, sorted_intervals[i]):
                curr_interval = self.merge_intervals(
                    curr_interval, sorted_intervals[i])
            else:
                intervals.append(curr_interval)
                curr_interval = sorted_intervals[i]
        
        intervals.append(curr_interval)
        return intervals
