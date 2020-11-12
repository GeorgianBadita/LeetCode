# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits == [9]:
            return [1, 0]

        digits[-1] += 1
        if digits[-1] > 9:
            digits[-1] %= 10
            carry = 1
        else:
            return digits

        for i in range(len(digits) - 2, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10

            if digits[i] > 9:
                digits[i] %= 10

        if carry:
            digits.insert(0, 1)
        return digits

print(Solution().plusOne([1, 9, 9, 9, 9, 9, 9]))