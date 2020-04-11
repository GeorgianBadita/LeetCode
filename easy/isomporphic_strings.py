"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   11.04.2020 22:13
"""


class Solution:
    def helper(self, s, t):
        if len(s) != len(t):
            return False
        mapping = {}
        for i in range(len(s)):
            if mapping.get(s[i]):
                char_map = mapping.get(s[i])
                if char_map == t[i]:
                    continue
                else:
                    return False
            mapping[s[i]] = t[i]
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.helper(s, t) and self.helper(t, s)


print(Solution().isIsomorphic("title", "paper"))
