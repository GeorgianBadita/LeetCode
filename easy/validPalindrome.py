"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 02:24
"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower().replace(" ", "")
        first_pointer = 0
        last_pointer = len(s) - 1
        while last_pointer > first_pointer:
            while first_pointer < last_pointer and not ('a' <= s[last_pointer] <= 'z' or '0' <= s[last_pointer] <= '9'):
                last_pointer -= 1
            while first_pointer < last_pointer and not ('a' <= s[first_pointer] <= 'z' or '0' <= s[first_pointer] <= '9'):
                first_pointer += 1
            if s[last_pointer] != s[first_pointer]:
                return False
            last_pointer -= 1
            first_pointer += 1
        return True


print(Solution().isPalindrome("race a car"))
