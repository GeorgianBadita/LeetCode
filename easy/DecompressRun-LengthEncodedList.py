# https://leetcode.com/problems/decompress-run-length-encoded-list/

from typing import List
from functools import reduce


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        return list(reduce(lambda x, y: x + y, [[nums[i + 1]]*nums[i] for i in range(0, len(nums) - 1, 2)], []))
