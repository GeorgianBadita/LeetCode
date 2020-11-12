# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_result = nums[0]
        for i in range(1, len(nums)):
            xor_result ^= nums[i]
        
        return xor_result


print(Solution().singleNumber([4,1,2,1,2]))