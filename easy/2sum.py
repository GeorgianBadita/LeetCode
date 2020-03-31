"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 00:23
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)):
            my_dict[nums[i]] = i

        for i in range(len(nums)):
            compl = my_dict.get(target - nums[i], None)
            if compl is not None and compl != i:
                return [i, compl]


print(Solution().twoSum([3, 3], 6))