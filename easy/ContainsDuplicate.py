# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for elem in nums:
            if elem in num_set:
                return True
            num_set.add(elem)

        return False