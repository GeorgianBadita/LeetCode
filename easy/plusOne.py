"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 00:18
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return digits
        if len(digits) == 1:
            if digits[0] < 9:
                digits[0] += 1
                return digits
            else:
                return [1, 0]
        i = len(digits) - 1
        carry = False
        while i >= 0:
            digits[i] += 1
            if digits[i] < 10:
                break
            else:
                digits[i] %= 10
            i -= 1

        if digits[0] == 0:
            carry = True
        if carry:
            digits.insert(0, 1)
        return digits


print(Solution().plusOne([9, 9, 9, 9]))
