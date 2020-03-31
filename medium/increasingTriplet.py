"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   28.03.2020 23:15
"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False

        first_min = second_min = float('inf')
        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True
        return False


print(Solution().increasingTriplet([]))
