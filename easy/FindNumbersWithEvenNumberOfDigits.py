# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num = 0
        for n in nums:
            cnt = 0
            if n == 0:
                cnt = 1
            else:
                cnt = 0
                while n != 0:
                    cnt += 1
                    n = int(n / 10)
            num += 1 if cnt % 2 == 0 else 0

        return num
