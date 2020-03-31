"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   28.03.2020 23:48
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        dup_set = set()
        for num in nums:
            if num in dup_set:
                return True
            dup_set.add(num)
        return False

