"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 20:06
"""


class Solution:
    def isValid(self, s: str) -> bool:
        dct = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        if not s:
            return True
        st = []
        for char in s:
            if char not in dct:
                st.append(char)
                continue
            if len(st) == 0:
                return False

            if not st[-1] == dct[char]:
                return False
            else:
                st.pop()

        return len(st) == 0


print(Solution().isValid('{()[]}'))
