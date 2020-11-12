# https://leetcode.com/problems/shuffle-the-array/

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half = 0
        second_half = n
        result = []
        for _ in range(n):
            result.append(nums[first_half])
            result.append(nums[second_half])
            first_half += 1
            second_half += 1

        return result