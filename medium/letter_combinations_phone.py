"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   04.04.2020 23:12
"""
from typing import List


def get_letter_domain():
    letter_domain = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    return letter_domain


def bkt(sol, digits, sols):
    if len(sol) < len(digits):
        for letter in get_letter_domain()[digits[len(sol)]]:
            sol.append(letter)
            if len(sol) == len(digits):
                sols.append(''.join(sol))
            bkt(sol, digits, sols)
            sol.pop()


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        sols = []
        bkt([], digits, sols)
        return sols


print(Solution().letterCombinations("23"))
