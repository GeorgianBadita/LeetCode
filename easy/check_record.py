"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   12.04.2020 23:37
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        if len(s) < 3 and 'P' in s:
            return True

        for i in range(len(s) - 2):
            if s[i] == s[i + 1] == s[i + 2] == 'L':
                return False
        return s.count('A') < 2