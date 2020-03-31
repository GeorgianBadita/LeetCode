"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   31.03.2020 21:40
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        subst = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        num = 0
        i = 0
        while i < len(s) - 1:
            if f'{s[i]}{s[i + 1]}' in subst:
                num += subst[f'{s[i]}{s[i + 1]}']
                i += 2
                continue
            else:
                num += mapping[s[i]]
            i += 1
        if i < len(s):
            num += mapping[s[i]]
        return num


print(Solution().romanToInt('MCMXCIV'))
