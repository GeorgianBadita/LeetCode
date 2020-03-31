"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 01:40
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1
        for i in range(l):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        print(s)


Solution().reverseString(['a', 'b', 'c', 'd'])
