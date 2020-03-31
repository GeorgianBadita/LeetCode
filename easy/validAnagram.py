"""
    @author: Badita Marin-Georgian
    @email:  geo.badita@gmail.com
    @date:   29.03.2020 02:19
"""


def hash_word(word):
    freq = [0] * 26
    for letter in word:
        freq[ord(letter) - ord('a')] += 1

    pow = 1
    hash_ = 0
    for i in range(25, -1, -1):
        hash_ += freq[i] * pow
        pow *= 26

    return hash_


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return hash_word(s) == hash_word(t)


print(Solution().isAnagram("rat", "car"))
