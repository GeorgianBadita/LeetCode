# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        total_sum = 0
        curr_odd_length = 1

        while curr_odd_length <= len(arr):
            sum_for_curr_length = 0
            for start_pos in range(len(arr) - curr_odd_length + 1):
                to_sum = arr[start_pos: start_pos + curr_odd_length]
                sum_for_curr_length += sum(to_sum)

            total_sum += sum_for_curr_length
            curr_odd_length += 2

        return total_sum
