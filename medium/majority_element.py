"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   11.04.2020 00:12
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cand = None

        for num in nums:
            if count == 0:
                cand = num
            if num == cand:
                count += 1
            else:
                count -= 1
        return cand
