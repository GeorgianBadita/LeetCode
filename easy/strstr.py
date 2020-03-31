"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 14:33
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        b1 = 27
        b2 = 29
        mod1 = 10007
        mod2 = 666013

        v1 = v2 = 0
        p1 = p2 = 1
        h1 = h2 = 0

        for i in range(len(needle)):
            v1 = (v1 * b1 + ord(needle[i])) % mod1
            v2 = (v2 * b2 + ord(needle[i])) % mod2

            if i > 0:
                p1 = (p1 * b1) % mod1
                p2 = (p2 * b2) % mod2

        for i in range(len(needle)):
            h1 = (h1 * b1 + ord(haystack[i])) % mod1
            h2 = (h2 * b2 + ord(haystack[i])) % mod2

        if h1 == v1 and h2 == v2:
            return 0

        for i in range(len(needle), len(haystack)):
            h1 = ((h1 - ord(haystack[i - len(needle)]) * p1 % mod1 + mod1) * b1 + ord(haystack[i])) % mod1
            h2 = ((h2 - ord(haystack[i - len(needle)]) * p2 % mod2 + mod2) * b2 + ord(haystack[i])) % mod2

            if h1 == v1 and h2 == v2:
                return i - len(needle) + 1
        return -1


print(Solution().strStr("", "a"))
