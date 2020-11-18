# https://leetcode.com/problems/arithmetic-subarrays/

from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            left = l[i]
            right = r[i]
            sorted_seq = sorted(nums[left:right + 1])
            is_arithm = True
            for j in range(0, len(sorted_seq) - 1):
                if sorted_seq[j + 1] - sorted_seq[j] != sorted_seq[1] - sorted_seq[0]:
                    is_arithm = False
                    break
            res.append(is_arithm)
        return res
