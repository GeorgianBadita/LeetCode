# https://leetcode.com/problems/number-of-good-pairs/

from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = [0] * 101
        for elem in nums:
            count[elem] += 1

        num_pairs = 0
        for elem in count:
            num_pairs += (elem)*(elem - 1)//2

        return num_pairs
