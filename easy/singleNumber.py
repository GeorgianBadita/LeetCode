"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   28.03.2020 23:52
"""
from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


print(Solution().singleNumber([4, 1, 2, 1, 2]))
