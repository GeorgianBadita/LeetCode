"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   12.04.2020 21:35
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed) or name[0] != typed[0]:
            return False
        p1 = 0
        i = 0
        while i < len(typed):
            if typed[i] == name[p1]:
                i += 1
                if p1 + 1 < len(name) and name[p1] == name[p1 + 1]:
                    p1 += 1
                continue
            if typed[i] != name[p1] and typed[i] != name[p1 + 1]:
                return False
            else:
                if p1 + 1 < len(name):
                    p1 += 1
            i += 1

        return p1 + 1 == len(name)


print(Solution().isLongPressedName("leeellee",
                                   "leeeeeellllee"
                                   ))
