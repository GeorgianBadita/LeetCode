# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
