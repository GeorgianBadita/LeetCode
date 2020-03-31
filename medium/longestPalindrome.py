"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   28.03.2020 22:44
"""


class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        max_len = 1
        start = 0
        i = 0
        while i < len(s) - 1:
            k = i

            if s[i] == s[i + 1]:
                p = 0
                while i - p >= 0 and i + p + 1 < len(s) and s[i - p] == s[i + p + 1]:
                    p += 1
                if 2 * p > max_len:
                    max_len = 2 * p
                    start = i - p + 1
            i = k
            if i - 1 >= 0 and s[i - 1] == s[i + 1]:
                p = 1
                while i - p >= 0 and i + p < len(s) and s[i - p] == s[i + p]:
                    p += 1

                if 2 * p - 1 > max_len:
                    max_len = 2 * p - 1
                    start = i - p + 1
            i = k + 1
        return s[start: start + max_len]


print(Solution().longestPalindrome("cbbd"))
