"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   11.04.2020 21:00
"""
from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        s = set()
        for elem in A:
            if elem in s:
                return elem
            s.add(elem)


print(Solution().repeatedNTimes([1, 2, 3, 3]))
